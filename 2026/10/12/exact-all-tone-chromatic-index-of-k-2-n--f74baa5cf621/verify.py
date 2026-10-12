from itertools import product

def predicted(n,t):
    return n*(t+max(0,t-n+1))

def construct(n,t):
    q=min(t,n-1)
    r=t-q
    E=[]; F=[]
    for i in range(n):
        E.append({('a',i,s) for s in range(1,t+1)})
    for j in range(n):
        lab={('a',(j+s)%n,s) for s in range(1,q+1)}
        lab |= {('b',j,h) for h in range(1,r+1)}
        F.append(lab)
    return E,F

def check(n,t):
    E,F=construct(n,t)
    assert all(len(x)==t for x in E+F)
    # within each clique of L(K_{2,n}) labels are disjoint
    for A in (E,F):
        for i in range(n):
            for j in range(i+1,n):
                assert A[i].isdisjoint(A[j])
    # matched cross pairs are adjacent; off-diagonal cross pairs are distance 2
    for i in range(n):
        for j in range(n):
            z=len(E[i]&F[j])
            if i==j: assert z==0
            else: assert z<=1
    palette=set().union(*(E+F)) if E+F else set()
    assert len(palette)==predicted(n,t)
    # independently reproduce the lower-bound accounting
    U=set().union(*E)
    assert len(U)==n*t
    r=max(0,t-n+1)
    outside=sum(len(F[j]-U) for j in range(n))
    assert outside==n*r
    return len(palette)

cases=0
for n in range(1,81):
    for t in range(1,81):
        check(n,t); cases+=1
# boundary identities against known special cases
for t in range(1,81):
    assert predicted(1,t)==2*t
    assert predicted(2,t)==4*t-2
for n in range(2,81):
    assert predicted(n,1)==n
    assert predicted(n,2)==(6 if n==2 else 2*n)
print(f'ALL CHECKS PASSED; construction_cases={cases}; n_range=1..80; t_range=1..80; boundary_star_cases=80; boundary_C4_cases=80; t1_t2_cases={79*2}')
