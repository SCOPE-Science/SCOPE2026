"""Exact rational checks for circumballs of stable-set polytopes of graph cones.
Run: python3 cone_verify.py (standard library only)."""
from fractions import Fraction as F
from itertools import combinations

def cycle(n):
    return n, {(min(i,(i+1)%n), max(i,(i+1)%n)) for i in range(n)}

def complement_cycle(n):
    _, es=cycle(n)
    return n, {(i,j) for i in range(n) for j in range(i+1,n) if (i,j) not in es}

def clique(n):
    return n, set(combinations(range(n),2))

def multipartite(r,a):
    n=r*a
    return n, {(i,j) for i in range(n) for j in range(i+1,n) if i//a!=j//a}

def check(n,edges, tag):
    assert edges and n>=2
    independent=[]
    for m in range(1<<n):
        if all(not ((m>>i)&1 and (m>>j)&1) for i,j in edges):
            independent.append(m)
    alpha=max(m.bit_count() for m in independent)
    maximals=[m for m in independent if m.bit_count()==alpha]
    for v in range(n):
        assert sum((m>>v)&1 for m in maximals)==F(len(maximals)*alpha,n), (tag,'not uniform',v)
    a=F(alpha); N=F(n)
    Q=a-a*a/N; D=1+a*a/N; delta=D-Q
    lam=max(F(0),delta/(2*D)); t=(1-lam)*a/N
    R2=Q+D*lam*lam
    assert 0<=lam<=F(1,2) and 0<t<F(1,2),tag
    hubdist=N*t*t+(1-lam)**2
    if delta>=0: assert hubdist==R2,tag
    else: assert hubdist<R2,tag
    for m in independent:
        k=m.bit_count()
        d=N*t*t+lam*lam+k*(1-2*t)
        assert d<=R2 and (d==R2)==(k==alpha),(tag,m,d,R2)
    c=[t]*n+[lam]
    for j in range(n):
        expected=(1-lam)*F(sum((m>>j)&1 for m in maximals),len(maximals))
        assert c[j]==expected,(tag,j)
    assert c[-1]==lam
    mean_square=(1-lam)*sum(
        (sum((F((m>>i)&1)-c[i])**2 for i in range(n))+lam*lam)/len(maximals)
        for m in maximals
    )+lam*hubdist
    assert mean_square==R2,(tag,mean_square,R2)
    return (tag,n,alpha,len(independent),len(maximals),str(delta),str(lam),str(R2))

def main():
    stats=[]
    for n in range(3,14):
        stats.append(check(*cycle(n),f'C{n}'))
    for n in range(5,14):
        stats.append(check(*complement_cycle(n),f'coC{n}'))
    for n in range(2,12):
        stats.append(check(*clique(n),f'K{n}'))
    for r in range(2,6):
        for a in range(1,4):
            if r*a<=14: stats.append(check(*multipartite(r,a),f'Kpart{r}x{a}'))
    assert any(row[5][0]=='-' for row in stats), 'no screening case'
    print('EXACT_CHECKS_OK graph_classes=',len(stats), 'indicator_vertices=',sum(x[3] for x in stats), 'max_contacts=',sum(x[4] for x in stats))
    print('SCREENED_SAMPLES', [x for x in stats if x[0] in ('coC8','coC9','coC10')])

if __name__=='__main__':main()
