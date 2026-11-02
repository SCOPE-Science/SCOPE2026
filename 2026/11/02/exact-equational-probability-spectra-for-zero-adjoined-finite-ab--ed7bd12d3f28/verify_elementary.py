"""Finite direct check of equational probabilities in elementary-abelian groups with absorbing zero."""
from itertools import product
from fractions import Fraction

def actual_p(p,d,k,e,f):
    G=list(product(range(p),repeat=d)); S=[None]+G
    total=0
    for xs in product(S,repeat=k):
        vals=[]
        for coeff in (e,f):
            if any(xs[i] is None for i,c in enumerate(coeff) if c!=-1):
                vals.append(None)
            else:
                vals.append(tuple(sum(c*xs[i][j] for i,c in enumerate(coeff) if c!=-1)%p for j in range(d)))
        total+=vals[0]==vals[1]
    return Fraction(total,len(S)**k)

def symbolic(p,d,k,e,f):
    q=p**d; s=Fraction(q,q+1)
    I={j for j,c in enumerate(e) if c!=-1};J={j for j,c in enumerate(f) if c!=-1}
    if not I or not J: raise ValueError('nonempty terms required')
    c=1 if all((e[j] if e[j]!=-1 else 0)-(f[j] if f[j]!=-1 else 0)==0 or ((e[j] if e[j]!=-1 else 0)-(f[j] if f[j]!=-1 else 0))%p==0 for j in range(k)) else Fraction(1,q)
    return 1-s**len(I)-s**len(J)+(1+c)*s**len(I|J)

def run():
    checks=0
    for p,d,k in [(2,1,3),(3,1,3),(2,2,3),(2,1,4)]:
        words=[e for e in product([-1,0,1],repeat=k) if any(x!=-1 for x in e)]
        # 0 stands for an exponent divisible by p, 1 for exponent 1.
        for e in words:
            for f in words:
                x=actual_p(p,d,k,e,f); y=symbolic(p,d,k,e,f)
                assert x==y,(p,d,k,e,f,x,y)
                checks+=1
        print(f'PASS p={p} d={d} arity={k} equations={len(words)**2}')
    for q in [2,3,4,8,9,25]:
        s=Fraction(q,q+1)
        vals=set()
        for i in range(1,18):
            for j in range(1,18):
                for u in range(max(i,j),i+j+1):
                    for c in [1,Fraction(1,q)]:
                        v=1-s**i-s**j+(1+c)*s**u
                        assert Fraction(1,q+1)<=v<=1
                        vals.add(v)
        assert Fraction(1,q+1) in vals and 1 in vals
        print(f'PASS q={q} analytic-bound tested={len(vals)} distinct truncated values')
    print(f'VERIFY_OK equations={checks}')
if __name__=='__main__':run()
