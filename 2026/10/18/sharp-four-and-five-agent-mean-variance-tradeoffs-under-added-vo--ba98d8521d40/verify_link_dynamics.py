"""Exact rational verification of consensus-time mean/variance tradeoffs under link updates.
Only Python standard-library modules are required.
Run: python verify_link_dynamics.py
"""
from fractions import Fraction as F
from itertools import combinations, permutations


def solve(A, b):
    """Gauss-Jordan elimination with rational pivots."""
    n = len(b)
    X = [[F(a) for a in row] + [F(c)] for row, c in zip(A, b)]
    for k in range(n):
        p = next((i for i in range(k,n) if X[i][k]), None)
        assert p is not None, 'nonabsorbing component failed'
        if p != k: X[k], X[p] = X[p], X[k]
        a = X[k][k]; X[k][k:] = [v/a for v in X[k][k:]]
        for i in range(n):
            if i == k or X[i][k] == 0: continue
            a = X[i][k]
            X[i][k:] = [u-a*v for u,v in zip(X[i][k:],X[k][k:])]
    return [row[-1] for row in X]


def moments(n, edges):
    """Continuous-time link dynamics: total update-attempt rate n; fair initial bits."""
    es = {tuple(sorted(e)) for e in edges}
    adj = [[int(tuple(sorted((i,j))) in es) for j in range(n)] for i in range(n)]
    assert all(sum(row)>0 for row in adj)
    allmask=(1<<n)-1
    states = [s for s in range(1,allmask) if s < (s^allmask)]
    ix = {s:j for j,s in enumerate(states)}
    Q=[[F(0) for _ in states] for _ in states]
    for i,s in enumerate(states):
        for v in range(n):
            disagree=sum(adj[v][w] for w in range(n) if ((s>>v)&1)!=((s>>w)&1))
            if not disagree:continue
            rate=F(disagree*n,2*len(es))
            Q[i][i]+=rate
            t=s^(1<<v)
            if t not in (0,allmask):
                j=ix[min(t,t^allmask)];Q[i][j]-=rate
    m1=solve(Q,[1]*len(states))
    m2=solve(Q,[2*u for u in m1])
    # Verify defining equations without relying on the elimination implementation.
    assert all(sum(row[j]*m1[j] for j in range(len(states)))==1 for row in Q)
    assert all(sum(row[j]*m2[j] for j in range(len(states)))==2*m1[i] for i,row in enumerate(Q))
    mu=sum(m1,F(0))/2**(n-1)
    second=sum(m2,F(0))/2**(n-1)
    return mu,second-mu*mu,second


def connected(n, edges):
    a=[set() for _ in range(n)]
    for u,v in edges:a[u].add(v);a[v].add(u)
    reach={0}
    todo=[0]
    while todo:
        v=todo.pop()
        for w in a[v]-reach:reach.add(w);todo.append(w)
    return len(reach)==n


def canonical(n, edges):
    pairs=list(combinations(range(n),2));es=set(edges)
    return min(tuple(int(tuple(sorted((p[u],p[v]))) in es) for u,v in pairs)
               for p in permutations(range(n)))


def graphs(n):
    pairs=list(combinations(range(n),2));seen=set()
    for bits in range(1,1<<len(pairs)):
        es=[pairs[i] for i in range(len(pairs)) if bits>>i&1]
        if not connected(n,es):continue
        can=canonical(n,es)
        if can not in seen:
            seen.add(can);yield es


def main():
    # Every graph of order <= 5 is generated as an unlabeled isomorphism class.
    expected_graphs={2:1,3:2,4:6,5:21}
    expected_pairs={2:0,3:1,4:11,5:80}
    expected_ct={2:(0,0),3:(0,0),4:(3,0),5:(0,1)}
    expected_count={2:(0,0),3:(0,0),4:(3,0),5:(0,1)}
    for n in range(2,6):
        ng=0;npairs=0;ct=[0,0];steps=[0,0]
        for es in graphs(n):
            ng+=1;old=moments(n,es)
            for edge in combinations(range(n),2):
                if edge in es:continue
                new=moments(n,es+[edge]);npairs+=1
                dm=new[0]-old[0];dv=new[1]-old[1]
                # The update-count clock equals the number of independent
                # rate-n exponential waiting intervals in the continuous clock.
                dv_steps=n*n*dv-n*dm
                if dm<0 and dv>0:ct[0]+=1
                if dm>0 and dv<0:ct[1]+=1
                if dm<0 and dv_steps>0:steps[0]+=1
                if dm>0 and dv_steps<0:steps[1]+=1
        assert ng==expected_graphs[n] and npairs==expected_pairs[n]
        assert tuple(ct)==expected_ct[n] and tuple(steps)==expected_count[n]
        print(f'n={n}: connected classes={ng}, nonedge additions={npairs}, continuous-time opposite sign counts={tuple(ct)}, update-count opposite sign counts={tuple(steps)}')

    # Type I: augment a four-node star with one leaf-to-leaf edge.
    old=moments(4,[(0,1),(0,2),(0,3)])
    new=moments(4,[(0,1),(0,2),(0,3),(1,2)])
    dmu=new[0]-old[0];dv=new[1]-old[1]
    assert dmu==F(-1,68) and dv==F(6257,18496)
    assert 4*dmu==F(-1,17) and 16*dv-4*dmu==F(6325,1156)
    print('star witness: time differences',dmu,dv,'update-count differences',4*dmu,16*dv-4*dmu)

    # Type II: K5 minus 01,24,34, then add 01.
    missing={(0,1),(2,4),(3,4)}
    E=[e for e in combinations(range(5),2) if e not in missing]
    old=moments(5,E);new=moments(5,E+[(0,1)])
    dmu=new[0]-old[0];dv=new[1]-old[1]
    assert dmu==F(123113,152733984)
    assert dv==F(-22700792201015951,583191746712806400)
    assert 5*dmu==F(615565,152733984)
    assert 25*dv-5*dmu==F(-22794809895876911,23327669868512256)
    print('dense witness: time differences',dmu,dv,'update-count differences',5*dmu,25*dv-5*dmu)
    print('ALL EXACT CERTIFICATES PASSED')

if __name__=='__main__':main()
