"""Independent count of faces of the five-cube closed-radius-two Cech complex."""
from collections import Counter
N=32
F=set()
for center in range(N):
    ball=sum(1<<v for v in range(N) if (center^v).bit_count()<=2)
    x=ball
    while x:
        F.add(x)
        x=(x-1)&ball
counts=Counter(x.bit_count()-1 for x in F)
print('faces',len(F))
print('f_vector',' '.join(f'{i}:{counts[i]}' for i in sorted(counts)))
print('reduced_euler',sum((-1)**d*count for d,count in counts.items())-1)
assert len(F)==1910200
assert (sum((-1)**d*count for d,count in counts.items())-1)==71
