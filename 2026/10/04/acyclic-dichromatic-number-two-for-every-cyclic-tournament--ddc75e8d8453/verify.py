#!/usr/bin/env python3

def arc(n,u,v):
    m=(n-1)//2
    return u!=v and ((v-u)%n) in range(1,m+1)

def check(m):
    n=2*m+1
    A=list(range(m+1))
    B=list(range(m+1,2*m+1))
    # Each colour class is transitive in increasing order.
    for X in (A,B):
        for p,u in enumerate(X):
            for v in X[p+1:]:
                assert arc(n,u,v)
    # Cross-part topological order a_m,b_{m-1},a_{m-1},...,a_1,b_0,a_0.
    order=[m]
    for j in range(m-1,-1,-1):
        order.append(m+1+j)
        order.append(j)
    pos={v:i for i,v in enumerate(order)}
    assert len(order)==n and len(pos)==n
    for a in A:
        for b in B:
            u,v=(a,b) if arc(n,a,b) else (b,a)
            assert pos[u] < pos[v]
    # Explicit directed triangle 0 -> m -> 2m -> 0.
    assert arc(n,0,m) and arc(n,m,2*m) and arc(n,2*m,0)
    return n

def main():
    checked=0
    max_order=0
    for m in range(1,201):
        max_order=check(m)
        checked+=1
    print(f"ALL CHECKS PASSED; parameters={checked}; max_order={max_order}")

if __name__=='__main__':
    main()
