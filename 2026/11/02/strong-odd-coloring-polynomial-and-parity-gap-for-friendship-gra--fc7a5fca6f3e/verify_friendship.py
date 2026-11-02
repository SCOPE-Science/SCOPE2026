from itertools import product
from math import comb

def g_formula(k,m):
    numer=sum((-1)**j*comb(k,j)*((k-2*j)**2-k)**m for j in range(k+1))
    assert numer%(2**k)==0,(m,k,numer)
    return numer//(2**k)

def p_formula(m,q):
    return q*sum(comb(q-1,k)*g_formula(k,m) for k in range(2,min(q-1,2*m)+1))

def via_state_dp(m,q):
    # Track two masks: used and parity for each color in a single petal.
    Q=q-1
    dp={(0,0):1}
    for _ in range(m):
        nxt={}
        for (used,parity),ways in dp.items():
            for a in range(Q):
                for b in range(Q):
                    if a==b:continue
                    pair=(1<<a)|(1<<b)
                    state=(used|pair,parity^pair)
                    nxt[state]=nxt.get(state,0)+ways
        dp=nxt
    return q*sum(ways for (used,parity),ways in dp.items() if used==parity)

def vertex_brute(m,q):
    n=1+2*m
    neigh=[set() for _ in range(n)]
    for j in range(m):
        a,b=2*j+1,2*j+2
        for x,y in [(0,a),(0,b),(a,b)]:neigh[x].add(y);neigh[y].add(x)
    ans=0
    for colors in product(range(q),repeat=n):
        if any(colors[u]==colors[v] for u in range(n) for v in neigh[u] if u<v):continue
        if all(all(sum(colors[v]==c for v in neigh[u])%2==1 for c in set(colors[v] for v in neigh[u])) for u in range(n)):
            ans+=1
    return ans

if __name__=='__main__':
    trials=0
    for m in range(1,9):
        for q in range(1,8):
            a=p_formula(m,q)
            b=via_state_dp(m,q)
            assert a==b,(m,q,a,b)
            trials+=1
        if m%2:assert p_formula(m,3)==3*2**m
        else:assert p_formula(m,3)==0 and p_formula(m,4)==0 and p_formula(m,5)==5*(12**m+3*4**m)//8
    cases=0
    for m in range(1,4):
        for q in range(1,7):
            a=p_formula(m,q)
            b=vertex_brute(m,q)
            assert a==b,(m,q,a,b)
            cases+=1
    print('VERIFY_OK independent_parity_dp_cases=',trials,'direct_graph_color_cases=',cases,'all_optimal_formulas=True')
    for m in range(1,7):print('m=',m,'P(q=3,4,5,6)=',[p_formula(m,q) for q in (3,4,5,6)])
