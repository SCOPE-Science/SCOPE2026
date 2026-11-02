"""Finite verification of period-three rowmotion via minimal-complement ideals.
No external packages. Counts all connected labelled graphs through five vertices.
"""
from itertools import combinations

def edges(n, mask):
    return [e for j, e in enumerate(combinations(range(n), 2)) if mask & (1 << j)]

def connected(n, E):
    if not E: return False
    seen = {0}
    while True:
        old = len(seen)
        for u,v in E:
            if u in seen: seen.add(v)
            if v in seen: seen.add(u)
        if len(seen) == old: return len(seen) == n

def row_direct(n, E, I):
    # Elements 0..n-1 are vertices; n+j is edge j, covering its two endpoints.
    below = [(0 if i < n else (1 << E[i-n][0]) | (1 << E[i-n][1]))
             for i in range(n+len(E))]
    absent_minimal = 0
    for i in range(n+len(E)):
        if not I & (1<<i) and (I & below[i]) == below[i]:
            absent_minimal |= 1<<i
    J = absent_minimal
    for i in range(n+len(E)):
        if absent_minimal & (1<<i): J |= below[i]
    return J

def count_direct(n, E):
    below = [0]*n + [(1<<u)|(1<<v) for u,v in E]
    cycles3_states = 0
    for I in range(1<<(n+len(E))):
        if any((I>>j)&1 and (I & below[j]) != below[j] for j in range(n,n+len(E))):
            continue
        J=row_direct(n,E,I); K=row_direct(n,E,J); L=row_direct(n,E,K)
        if L==I:
            assert J!=I and K!=I
            cycles3_states += 1
    assert cycles3_states%3==0
    return cycles3_states//3

def predicted(n,E):
    result=0
    for mask in range(4**n):
        c=[]; q=mask
        for _ in range(n): c.append(q%4);q//=4
        # 3 is X, 0-2 are component labels
        if any(c[u]==c[v]==3 for u,v in E):continue
        if any(c[u]!=c[v] and c[u]!=3 and c[v]!=3 for u,v in E):continue
        if any(c[x]==3 and set(c[y] for u,v in E
                  for y in ([v] if x==u else ([u] if x==v else [])))!={0,1,2}
               for x in range(n)):continue
        result+=1
    assert result%3==0
    return result//3

def run():
    total=0
    for n in range(2,6):
        tally={}
        for m in range(1<<(n*(n-1)//2)):
            E=edges(n,m)
            if not connected(n,E):continue
            actual=count_direct(n,E)
            expected=predicted(n,E)
            assert actual==expected,(n,E,actual,expected)
            tally[actual]=tally.get(actual,0)+1
            total+=1
        print('vertices',n,'3cycle_count_frequencies',sorted(tally.items()))
    assert total==771
    print('DIRECT_MINIMAL_COMPLEMENT_ALL_771_GRAPHS_PASS')

if __name__=='__main__':run()
