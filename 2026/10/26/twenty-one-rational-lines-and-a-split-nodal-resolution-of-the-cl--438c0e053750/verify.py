#!/usr/bin/env python3
"""Finite-field checks for the characteristic-five Clebsch cubic.

All calculations are exact in F5 and F25=F5[a]/(a*a-3).
Analytic arguments in RESULT.md, not these finite tests, establish
geometric completeness and all-extension point counts.
"""
from itertools import combinations, permutations, product


def field(q):
    if q == 5:
        return list(range(5)),lambda x,y:(x+y)%5,lambda x,y:x*y%5,lambda x:(-x)%5,0,1
    assert q == 25
    E=list(range(25))
    def add(x,y):
        a,b=x%5,x//5
        c,d=y%5,y//5
        return (a+c)%5+5*((b+d)%5)
    def mul(x,y):
        a,b=x%5,x//5
        c,d=y%5,y//5
        return (a*c+3*b*d)%5+5*((a*d+b*c)%5)
    def neg(x):return (-x%5)+5*((-(x//5))%5)
    return E,add,mul,neg,0,1


def sum_field(v,add,zero):
    s=zero
    for x in v:s=add(s,x)
    return s


def surface_counts(q):
    E,add,mul,neg,zero,one=field(q)
    cubes={x:mul(mul(x,x),x) for x in E}
    squares={x:mul(x,x) for x in E}
    num=0
    for pivot in range(4):
        for tail in product(E,repeat=3-pivot):
            x=(zero,)*pivot+(one,)+tail
            x4=neg(sum_field(x,add,zero))
            if sum_field((cubes[t] for t in (*x,x4)),add,zero)==zero:
                num+=1
    directions=set();conic=set()
    for pivot in range(3):
        for tail in product(E,repeat=2-pivot):
            # representative of the plane sum(u_0,...,u_3)=0
            y=(zero,)*pivot+(one,)+tail
            u=(*y,neg(sum_field(y,add,zero)))
            if sum_field((squares[t] for t in u),add,zero)==zero:
                conic.add(u)
                if sum_field((cubes[t] for t in u),add,zero)==zero:
                    directions.add(u)
    assert len(conic)==q+1,(q,'conic',len(conic))
    assert len(directions)==6,(q,'directions',len(directions))
    assert num==q*q+6*q+1,(q,'surface',num)
    print('q',q,'surface_points',num,'conic_points',len(conic),'base_directions',len(directions))


def rref_lines_five():
    for i,j in combinations(range(4),2):
        u=[0]*4;v=[0]*4;u[i]=1;v[j]=1
        freeu=[k for k in range(i+1,4) if k !=j]
        freev=list(range(j+1,4))
        for vals in product(range(5),repeat=len(freeu)+len(freev)):
            uu=u[:];vv=v[:]
            for k,t in zip(freeu,vals):uu[k]=t
            for k,t in zip(freev,vals[len(freeu):]):vv[k]=t
            yield tuple(uu),tuple(vv)


def normalize_4(v):
    for x in v:
        if x:return tuple((t*pow(x,-1,5))%5 for t in v)
    raise AssertionError('zero vector')


def line_check():
    nlines=0; through=0; seen=[]
    for u,v in rref_lines_five():
        def on(u4):
            full=(*u4,(-sum(u4))%5)
            return sum(t**3 for t in full)%5==0
        if all(on(tuple((u[k]+t*v[k])%5 for k in range(4))) for t in range(5)) and on(v):
            nlines+=1;seen.append((u,v))
            if any(all((s*u[k]+t*v[k])%5==1 for k in range(4)) for s,t in product(range(5),repeat=2)):
                through+=1
    assert nlines==21,(nlines,through)
    assert through==6,(nlines,through)
    assert len(list(rref_lines_five()))==806
    # Six permutations of (0,1,2,3,4) modulo adding a constant
    # and multiplying by a nonzero scalar (directions through the node).
    dirs=set()
    for w in permutations(range(5)):
        u=tuple((w[i]-w[4])%5 for i in range(4))
        dirs.add(normalize_4(u))
    assert len(dirs)==6,len(dirs)
    # The induced six-point action is sharply three-transitive.
    all_dirs=sorted(dirs)
    def act_on_dir(w,perm):
        # Direction in the full five-coordinate hyperplane, with last entry zero.
        v=(*w,0)
        z=[v[perm[i]] for i in range(5)]
        u=tuple((z[i]-z[4])%5 for i in range(4))
        return normalize_4(u)
    actions=[]
    for sigma in permutations(range(5)):
        act=tuple(all_dirs.index(act_on_dir(w,sigma)) for w in all_dirs)
        actions.append(act)
    assert len(set(actions))==120
    assert len({(act[0],act[1],act[2]) for act in actions})==6*5*4
    for u in dirs:
        assert sum(u)%5==0
        assert sum(t*t for t in u)%5==0
        assert sum(t**3 for t in u)%5==0
    # Fifteen pairwise-partition lines, each from (s,-s,t,-t,0).
    diagonal=set()
    for zero_index in range(5):
        others=[j for j in range(5) if j!=zero_index]
        for pair in combinations(others,2):
            if others[0] not in pair:continue
            rest=[j for j in others if j not in pair]
            a=[0]*5;b=[0]*5
            a[pair[0]]=1;a[pair[1]]=4
            b[rest[0]]=1;b[rest[1]]=4
            # canon RREF by listing projective points on span in F5^5
            pts=set()
            for s,t in product(range(5),repeat=2):
                w=tuple((s*a[i]+t*b[i])%5 for i in range(5))
                if not any(w):continue
                for z in w:
                    if z:break
                pts.add(tuple((pow(z,-1,5)*e)%5 for e in w))
            diagonal.add(frozenset(pts))
    assert len(diagonal)==15,len(diagonal)
    print('F5 lines total',nlines,'through_node',through,'other',nlines-through,'diagonal',len(diagonal),'S5_triples',len({(a[0],a[1],a[2]) for a in actions}))


if __name__=='__main__':
    surface_counts(5)
    surface_counts(25)
    line_check()
    print('VERIFY_OK')
