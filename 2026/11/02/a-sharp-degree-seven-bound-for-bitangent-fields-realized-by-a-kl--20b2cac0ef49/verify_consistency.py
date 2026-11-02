"""Compare two independently generated full symplectic-cycle inventories."""
import csv
from collections import Counter

def parse(path):
    rows=open(path,encoding='utf-8').read().splitlines()
    hist={}
    for line in rows:
        if line.startswith('cycle '):
            parts=line.removeprefix('cycle ').split(', count ')
            assert len(parts)==2
            key=tuple(int(x) for x in parts[0].strip(',').split(',') if x)
            assert sum(key)==28 and key not in hist
            hist[key]=int(parts[1])
    return hist

# Independently reconstruct all supplied transvection permutations from the
# symplectic pairing and the Arf-one quadratic refinements.
def sym_pair(a,b):
    return (((a&7)&(b>>3)).bit_count()+(((a>>3)&7)&(b&7)).bit_count())%2
def q0(a):
    return ((a&7)&(a>>3)).bit_count()%2
odd=[c for c in range(64) if q0(c)==1]
assert len(odd)==28
ix={c:i for i,c in enumerate(odd)}
with open('theta_generators.txt',encoding='utf-8') as f:
    lines=f.read().splitlines()
assert int(lines[0])==len(lines)-1==18
for line in lines[1:]:
    w,*perm=map(int,line.split())
    assert 1<=w<=63 and len(perm)==28
    expected=[ix[c^(w if (q0(w)^sym_pair(w,c)^1)==1 else 0)] for c in odd]
    assert perm==expected

a=parse('result_theta.txt');b=parse('result_matrices.txt')
assert a==b and len(a)==25 and sum(a.values())==1451520
minima=Counter()
for cycles,count in a.items(): minima[min(cycles)]+=count
assert dict(sorted(minima.items()))=={1:984852,2:71820,3:96768,4:90720,7:207360}
assert a[(7,7,7,7)]==207360
with open('group_cycle_spectra.csv','w',newline='',encoding='utf-8') as f:
    w=csv.writer(f);w.writerow(['cycle_lengths','elements','least_orbit'])
    for key,cnt in sorted(a.items()):w.writerow([';'.join(map(str,key)),cnt,min(key)])
print('GROUP_ELEMENTS',sum(a.values()),'CYCLE_PROFILES',len(a))
print('MINIMUM_ORBIT_HISTOGRAM',dict(sorted(minima.items())))
print('VERIFY_GROUP_OK')
