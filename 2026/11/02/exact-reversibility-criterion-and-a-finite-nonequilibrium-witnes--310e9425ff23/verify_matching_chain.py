"""Exact finite-state verification of Bell-measurement matching-chain reversibility."""
from fractions import Fraction
from itertools import combinations
from math import comb

def matchings(n):
    def rec(vertices):
        if not vertices:
            yield ()
            return
        a=vertices[0]
        for rest in rec(vertices[1:]):
            yield rest
        for j in vertices[1:]:
            remaining=tuple(x for x in vertices[1:] if x!=j)
            for rest in rec(remaining):
                yield tuple(sorted(((a,j),)+rest))
    return sorted(set(rec(tuple(range(n)))))

def bell_update(state,i,j):
    d={a:b for a,b in state}
    d.update({b:a for a,b in state})
    a=d.get(i); b=d.get(j)
    if a==j:return state
    new=set(state)
    if a is not None:new.remove(tuple(sorted((i,a))))
    if b is not None:new.remove(tuple(sorted((j,b))))
    new.add(tuple(sorted((i,j))))
    if a is not None and b is not None:new.add(tuple(sorted((a,b))))
    return tuple(sorted(new))

def site_update(state,i):
    return tuple(edge for edge in state if i not in edge)

def chain(n,p,w):
    states=matchings(n);W=sum(w.values()); rows={}
    for M in states:
        T={s:Fraction(0) for s in states}
        for i in range(n):
            T[site_update(M,i)]+=p/n
        for (i,j),v in w.items():
            T[bell_update(M,i,j)]+=(1-p)*v/W
        assert sum(T.values())==1
        rows[M]=T
    return rows

def check(n,w):
    p=Fraction(2,7);P=chain(n,p,w);W=sum(w.values());z={ij:Fraction(n)*(1-p)*v/(2*p*W) for ij,v in w.items()}
    prod={M:__import__('math').prod([z[ij] for ij in M]) for M in P}
    eq=[(M,T) for M in P for T in P if prod[M]*P[M][T]!=prod[T]*P[T][M]]
    return len(P),len(eq),eq[:1],P

for n in (4,5,6):
 v=[Fraction(i+2) for i in range(n)]
 wa={(i,j):1/(v[i]+v[j]) for i,j in combinations(range(n),2)}
 count,errs,_,_=check(n,wa)
 assert errs==0,(n,errs)
 print('additive',n,'states',count,'detailed-balance mismatches',errs)
 wb={(i,j):Fraction(1,j-i) for i,j in combinations(range(n),2)}
 count,errs,examples,P=check(n,wb)
 assert errs>0
 print('distance inverse',n,'states',count,'mismatches',errs)
 # Five-state cycle: empty->(0,2)->(0,2),(1,3)->(0,1),(2,3)->(0,1)->empty.
 s0=();s1=((0,2),);s2=((0,2),(1,3));s3=((0,1),(2,3));s4=((0,1),)
 cycle=[s0,s1,s2,s3,s4]
 num=__import__('math').prod(P[x][y] for x,y in zip(cycle,cycle[1:]+cycle[:1]))
 den=__import__('math').prod(P[y][x] for x,y in zip(cycle,cycle[1:]+cycle[:1]))
 assert num/den==Fraction(1,2),(num/den,n)
 print('Kolmogorov cycle ratio',num/den)
 wc={(i,j):Fraction(1,(j-i)**2) for i,j in combinations(range(n),2)}
 _,errs,_,P2=check(n,wc)
 assert errs>0
 num2=__import__('math').prod(P2[x][y] for x,y in zip(cycle,cycle[1:]+cycle[:1]))
 den2=__import__('math').prod(P2[y][x] for x,y in zip(cycle,cycle[1:]+cycle[:1]))
 assert num2/den2==Fraction(1,4)
 print('distance squared cycle ratio',num2/den2)
 # One vertex potential is negative but each reciprocal pair weight is positive.
 vn=[Fraction(-1)]+[Fraction(i+2) for i in range(1,n)]
 wd={(i,j):1/(vn[i]+vn[j]) for i,j in combinations(range(n),2)}
 _,errs,_,_=check(n,wd)
 assert errs==0
 print('signed potentials',n,'detailed-balance mismatches',errs)
print('ALL TESTS PASSED')
