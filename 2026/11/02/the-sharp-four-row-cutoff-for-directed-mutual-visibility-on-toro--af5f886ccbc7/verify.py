#!/usr/bin/env python3
"""Self-contained exact and constructive checks for directed mutual visibility.
No third-party packages are required.
"""
from itertools import combinations, product
from collections import deque


def forward_distance(a,b,mod):
    return (b-a)%mod


def admissible(m,n,S):
    """All ordered selected pairs admit a shortest directed path with no internal S.

    Path steps in the unique monotone coordinate rectangle of size (dx+1)(dy+1).
    The recurrence is an exhaustive directed acyclic reachability calculation.
    """
    S=set(S)
    for a in S:
        for b in S:
            if a==b:continue
            dx=forward_distance(a[0],b[0],m)
            dy=forward_distance(a[1],b[1],n)
            dp=[[False]*(dy+1) for _ in range(dx+1)]
            dp[0][0]=True
            for x in range(dx+1):
                for y in range(dy+1):
                    if (x,y)==(0,0):continue
                    point=((a[0]+x)%m,(a[1]+y)%n)
                    if point in S and (x,y)!=(dx,dy):continue
                    dp[x][y]= (x>0 and dp[x-1][y]) or (y>0 and dp[x][y-1])
            if not dp[dx][dy]:return False
    return True


def independent_check(m,n,S):
    """Unrelated BFS from graph arcs restricted to shortest paths.
    A path of exactly the shortest directed length exists iff internal selected
    vertices can be avoided; positive coordinate steps ensure distance lower bound.
    """
    S=set(S)
    for a in S:
        for b in S:
            if a==b:continue
            dist=forward_distance(a[0],b[0],m)+forward_distance(a[1],b[1],n)
            seen={a};queue=deque([(a,0)]);success=False
            while queue:
                node,t=queue.popleft()
                if node==b:
                    assert t==dist
                    success=True;break
                if t>=dist:continue
                x,y=node
                for nxt in (((x+1)%m,y),(x,(y+1)%n)):
                    if nxt in S and nxt!=b:continue
                    if nxt in seen:continue
                    seen.add(nxt);queue.append((nxt,t+1))
            if not success:return False
    return True


def all_possible_rows(n):
    return [()]+[(j,) for j in range(n)]+list(combinations(range(n),2))


def certify_small(m,n,minimum_forbidden):
    """Exhaust all vertex sets of cardinality at least minimum_forbidden.
    Three selected vertices in any directed row/column are impossible;
    thus rows/columns of occupancy at most two are an exhaustive reduction.
    """
    count=0;hist={}
    opts=all_possible_rows(n)
    for rows in product(opts,repeat=m):
        k=sum(len(row) for row in rows)
        if k<minimum_forbidden:continue
        if any(sum(j in row for row in rows)>2 for j in range(n)):continue
        S={(i,j) for i,row in enumerate(rows) for j in row}
        count+=1;hist[k]=hist.get(k,0)+1
        if admissible(m,n,S):
            raise AssertionError(('unexpected feasible set',m,n,k,rows))
        # Cross-check independent BFS on the entire boundary census.
        if independent_check(m,n,S):
            raise AssertionError(('independent contradiction',m,n,k,rows))
    return count,hist


def main():
    witnesses={
        4: [[],[0],[1,3],[1,3]],
        5: [[0],[1,3],[1,4],[2,4]],
        6: [[0,2],[0,3],[1,4],[2,4]],
    }
    for n,rows in witnesses.items():
        S={(i,j) for i,row in enumerate(rows) for j in row}
        assert len(S)=={4:5,5:7,6:8}[n]
        assert admissible(4,n,S)
        assert independent_check(4,n,S)
    print('BASE_WITNESSES_OK 4=5 5=7 6=8')
    for n,threshold in [(4,6),(5,8)]:
        count,hist=certify_small(4,n,threshold)
        assert (count,hist)==({4:(2946,{6:2040,7:816,8:90}),
                               5:(2490,{8:2490})}[n])
        print('EXHAUSTIVE_UPPER_OK',n,count,sorted(hist.items()))
    S6={(i,j) for i,row in enumerate(witnesses[6]) for j in row}
    for n in range(6,31):
        # The same selected vertices live in rows 0,...,5.
        assert admissible(4,n,S6),n
        assert independent_check(4,n,S6),n
    print('CYCLE_EXTENSION_TEST_OK 6..30')
    print('VERIFY_OK')

if __name__=='__main__': main()
