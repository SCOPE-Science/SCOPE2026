"""Independent forward BFS plus shortest-word multiplicity and Parikh check.
Run: python3 verify_bruteforce.py
"""
from collections import deque

def check(n):
    states = [(i,j) for i in range(n) for j in range(i+1,n)]
    def action(p,letter):
        q = [(x+1)%n if letter=='a' else (0 if x==n-1 else x) for x in p]
        if q[0]==q[1]: return None
        return tuple(sorted(q))
    # Forward BFS independently from each pair to first synchronized state.
    for i,j in states:
        dist = {(i,j):0}
        count = {(i,j):1}
        words = {(i,j):''}
        queue=deque([(i,j)])
        best=None;best_count=0;witness=None
        while queue:
            p=queue.popleft();d=dist[p]
            if best is not None and d>=best: continue
            for letter in 'ab':
                q=action(p,letter)
                if q is None:
                    if best is None:
                        best=d+1; witness=words[p]+letter
                    if best==d+1: best_count+=count[p]
                else:
                    if q not in dist:
                        dist[q]=d+1;count[q]=0;words[q]=words[p]+letter;queue.append(q)
                    if dist[q]==d+1:
                        count[q]+=count[p]
        gap=j-i
        turns=min(gap,n-gap)
        if gap*2 < n:
            ca=(n-1)*gap-i;cb=gap
        else:
            ca=(n-1)*(n-gap)-j;cb=n-gap
        assert best==ca+cb, (n,i,j,best,ca+cb)
        assert best_count==1,(n,i,j,best_count)
        assert witness.count('a')==ca and witness.count('b')==cb,(n,i,j,witness)
    return len(states)

if __name__=='__main__':
    for n in range(3,24):check(n)
    print('FORWARD_BFS_VERIFY_OK n=3..23; all pairs; minimum length; unique shortest word; exact letter counts')
