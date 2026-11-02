#!/usr/bin/env python3
"""Exact integer checks for a twisted cubic Ising ring; Python standard library only."""

FIELDS_TWICE = [-8,-6,-5,-4,-2,-1,0,1,2,3,4,5,6,8]

def expected(n,q):
    a=abs(q)
    if n%2:
        if a<6: return (-6*n,2)
        if a==6: return (-6*n, independent_count(n))
        return (6*n-2*n*a,1)
    if a<2:return (-6*n+8,2*n)
    if a==2:return (-6*n+8,4*n)
    if a<6:return (-6*n+12-2*a,2*n)
    if a==6:return (-6*n,independent_count(n))
    return (6*n-2*n*a,1)

def independent_count(n):
    x,y=2,2
    for _ in range(2,n+1):x,y=y,2*y+x
    return y-((-1)**n)

def transfer_minimum(n,q):
    states=[(-1,-1),(-1,1),(1,-1),(1,1)]
    best=[10**9,0]
    for start,(a,b) in enumerate(states):
        dp={start:(2*a*b-q*(a+b),1)}
        for _ in range(1,n):
            nxt={}
            for prev,(value,cnt) in dp.items():
                x,y=states[prev]
                for j,(u,v) in enumerate(states):
                    e=value+2*(x*u+y*v+u*v)-q*(u+v)
                    old,k=nxt.get(j,(10**9,0))
                    if e<old:nxt[j]=(e,cnt)
                    elif e==old:nxt[j]=(e,k+cnt)
            dp=nxt
        for last,(e,cnt) in dp.items():
            x,y=states[last]
            z=e+2*(x*b+y*a)
            if z<best[0]:best[:]=[z,cnt]
            elif z==best[0]:best[1]+=cnt
    return tuple(best)

def check():
    cases=0; evals=0; indcheck=0
    for n in range(3,11):
        v=2*n; full=(1<<v)-1
        observed={q:[10**9,0] for q in FIELDS_TWICE}
        ind=0
        for mask in range(1<<v):
            rotate=((mask<<1)&full)|(mask>>(v-1))
            cutcycle=(mask^rotate).bit_count()
            cutchord=(mask^( (mask<<n)&full | (mask>>n) )).bit_count()//2
            F=3*n-cutcycle-cutchord
            M=v-2*mask.bit_count()
            E=-6*n+4*F
            if F==3*(n-mask.bit_count()):ind+=1  # direct independent-set criterion e(S)=0
            for q in FIELDS_TWICE:
                z=E-q*M
                old,count=observed[q]
                if z<old:observed[q]=[z,1]
                elif z==old:observed[q][1]=count+1
            evals+=1
        assert ind==independent_count(n),(n,ind,independent_count(n))
        indcheck+=1
        for q in FIELDS_TWICE:
            actual=tuple(observed[q]);want=expected(n,q)
            assert actual==want,(n,q,actual,want)
            cases+=1
        print(f'n={n:2d} independent_sets={ind:6d} field_tests={len(FIELDS_TWICE)}')
    extra=0
    for n in range(3,65):
        for q in FIELDS_TWICE:
            actual=transfer_minimum(n,q)
            want=expected(n,q)
            assert actual==want,(n,q,actual,want)
            extra+=1
    print(f'PASS {cases} brute-force field-and-degeneracy comparisons, {indcheck} independent-set enumerations, {evals} complete spin configurations; {extra} independent twisted-transfer comparisons for n=3..64; h=field_twice/2, J=1')
if __name__=='__main__':check()
