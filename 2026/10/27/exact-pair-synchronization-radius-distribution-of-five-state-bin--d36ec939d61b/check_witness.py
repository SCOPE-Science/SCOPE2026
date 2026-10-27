"""Check every prescribed-pair merge distance in a standard five-state example."""
from collections import deque
from itertools import combinations
A=(1,2,3,4,0)
B=(0,1,2,3,0)
expected=(5,10,7,1,4,9,6,3,8,2)
def distance(pair):
    q=deque([(pair,0)])
    visited={pair}
    while q:
        (u,v),depth=q.popleft()
        for letter in (A,B):
            new=tuple(sorted((letter[u],letter[v])))
            if new[0]==new[1]:
                return depth+1
            if new not in visited:
                visited.add(new)
                q.append((new,depth+1))
    raise AssertionError('prescribed pair cannot be merged')
assert tuple(map(distance,combinations(range(5),2)))==expected
u,v=0,2
for letter in 'aaaabaaaab':
    f=A if letter=='a' else B
    u,v=f[u],f[v]
assert u==v
# The relabeling sends the standard example to the first forward-program extremizer.
p=(0,2,3,1,4)
aa=[0]*5
bb=[0]*5
for i in range(5):
    aa[p[i]]=p[A[i]]
    bb[p[i]]=p[B[i]]
assert tuple(aa)==(2,4,3,1,0)
assert tuple(bb)==(0,1,2,3,0)
print('WITNESS_OK: distances, a length-ten merger, and relabeling agree')
