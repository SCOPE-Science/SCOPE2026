"""Exhaustively verify outer multiset resolving polynomials for matching-deleted K_(p,q)."""
from collections import Counter,deque

def proposed(p,q,t):
    a2=t*(p-t)+t*(q-t)+(p*q if p!=q else 2*t*(p-t))
    a3=t*(t-1)+t*(p-t)*(q-1)
    if q!=p+1:
        a3+=t*(t-1)+t*(q-t)*(p-1)
    a4=(t*(t-1)*(t-2+(p-t)*(q-t)) if p!=q else 0)
    return {p+q:1,p+q-1:p+q,p+q-2:a2,p+q-3:a3,p+q-4:a4}

def exact(p,q,t):
    n=p+q
    adj=[set() for _ in range(n)]
    for i in range(p):
        for j in range(q):
            if i==j and i<t:continue
            adj[i].add(p+j);adj[p+j].add(i)
    d=[]
    for u in range(n):
        arr=[1000]*n;arr[u]=0;que=deque([u])
        while que:
            v=que.popleft()
            for w in adj[v]:
                if arr[w]>arr[v]+1:arr[w]=arr[v]+1;que.append(w)
        d.append(arr)
    assert max(map(max,d))<=3
    c=Counter()
    for mask in range(1<<n):
        S=[i for i in range(n) if mask>>i&1]
        outs=[i for i in range(n) if not(mask>>i&1)]
        sigs=[tuple(sorted(d[i][j] for j in S)) for i in outs]
        if len(set(sigs))==len(sigs):c[len(S)]+=1
    return dict(c)

def main():
    checks=0
    for p in range(3,6):
        for q in range(p,7):
            for t in range(p+1):
                proposed_c=Counter({k:v for k,v in proposed(p,q,t).items() if v})
                exact_c=Counter(exact(p,q,t))
                if proposed_c!=exact_c:
                    print('FAIL',p,q,t,proposed_c,exact_c);raise SystemExit(1)
                checks+=1
    for p,q,t in [(3,3,3),(3,4,3),(4,5,3)]:
        proposed_c=Counter({k:v for k,v in proposed(p,q,t).items() if v})
        exact_c=Counter(exact(p,q,t))
        if proposed_c!=exact_c:
            print('FAIL',p,q,t,proposed_c,exact_c);raise SystemExit(1)
        checks+=1
    tested=[(p,q,t) for p in range(3,6) for q in range(p,7) for t in range(p+1)]+[(3,3,3),(3,4,3),(4,5,3)]
    assert checks==46
    print('PASS',checks,'parameter triples;',sum(2**(p+q) for p,q,t in tested),'vertex subsets tested')
    for p,q,t in [(3,3,0),(3,3,1),(3,3,3),(3,4,1),(3,4,2),(3,4,3),(4,5,4)]:
        print(p,q,t,dict(sorted(exact(p,q,t).items())))
if __name__=='__main__':main()
