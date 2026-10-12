"""Independent threshold-clique verification using greedy color bounds.
Run: python3 verify_secondary.py (Python 3, standard library only).
"""
from itertools import combinations, product

SYMBOLS = '0123'

def eligible(A):
    B=set(SYMBOLS)-set(A)
    out=[]
    for x in product(SYMBOLS,repeat=4):
        w=''.join(x)
        if w[0] not in A or w[3] not in B:
            continue
        # The first and last symbols differ; only a length-2 self-border can remain.
        # It is exactly the alternating period-two condition.
        if w[0]==w[2] and w[1]==w[3]:
            continue
        out.append(w)
    return out

def conflict(x,y):
    if sum(x[i]!=y[i] for i in range(4)) <= 1:
        return True
    # Nontrivial prefix-suffix matches, computed by suffix/prefix lengths.
    for r in (1,2,3):
        if x[4-r:]==y[:r] or y[4-r:]==x[:r]:
            return True
    return False

def graph(W):
    neighbor=[0]*len(W)
    for i in range(len(W)):
        for j in range(i+1,len(W)):
            if not conflict(W[i],W[j]):
                neighbor[i]|=1<<j
                neighbor[j]|=1<<i
    return neighbor

def color_order(P, neighbors):
    order=[]; upper=[]; color=0
    while P:
        color += 1
        Q=P
        while Q:
            vbit=Q & -Q
            v=vbit.bit_length()-1
            order.append(v)
            upper.append(color)
            P &= ~vbit
            Q &= ~vbit
            Q &= ~neighbors[v]
            Q &= P
    return order,upper

def count_cliques(neighbors, target):
    def dfs(P, depth):
        if depth==target:return 1
        if P.bit_count() < target-depth:return 0
        ordered,colors=color_order(P,neighbors)
        total=0
        for i in range(len(ordered)-1,-1,-1):
            if depth+colors[i]<target:
                break
            v=ordered[i];vbit=1<<v
            total+=dfs(P & neighbors[v],depth+1)
            P &= ~vbit
        return total
    return dfs((1<<len(neighbors))-1,0)

def main():
    count12=count13=0; report=[]
    for size in (1,2,3):
        for A in combinations(SYMBOLS,size):
            W=eligible(A)
            G=graph(W)
            c12=count_cliques(G,12)
            c13=count_cliques(G,13)
            report.append((''.join(A),len(W),c12,c13))
            count12+=c12;count13+=c13
    assert len(report)==14
    assert all(c13==0 for _,_,_,c13 in report)
    assert sum(c12==4 for _,_,c12,_ in report)==6
    assert all(c12 in (0,4) for _,_,c12,_ in report)
    assert count12==24 and count13==0,(count12,count13)
    print('SPLIT_REPORT',report)
    print('TWELVE_SETS',count12,'THIRTEEN_SETS',count13)
    print('VERIFY_OK')
if __name__=='__main__':main()
