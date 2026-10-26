"""Exact integer/rational certificates for a nine-dimensional lattice Hardy cutoff."""
import json
import math
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def partitions(total, maximum=None):
    if maximum is None:
        maximum = total
    if total == 0:
        yield ()
    else:
        for a in range(min(total, maximum), 0, -1):
            for suffix in partitions(total-a, a):
                yield (a,) + suffix

def orbit_data(radius):
    d = 9
    classes = [p for s in range(1, radius+1)
               for p in partitions(s) if len(p) <= d]
    indices = {p:i for i,p in enumerate(classes)}
    mult=[]; squares=[]; adjacency=[]
    for p in classes:
        size=2**len(p)*math.factorial(d)//math.factorial(d-len(p))
        for v in set(p):
            size //= math.factorial(p.count(v))
        mult.append(size)
        squares.append(sum(v*v for v in p))
        representative=list(p)+[0]*(d-len(p))
        nbr={}
        for j in range(d):
            for sign in (-1,1):
                z=representative[:]
                z[j]+=sign
                label=tuple(sorted((abs(x) for x in z if x), reverse=True))
                k=indices.get(label)
                if k is not None:
                    nbr[k]=nbr.get(k,0)+1
        adjacency.append(nbr)
    return classes,mult,squares,adjacency

def cert(radius):
    path=ROOT/f'certificate_R{radius}.json'
    entry=json.loads(path.read_text('utf-8'))
    assert entry['dimension']==9 and entry['radius']==radius
    classes,mult,squares,adjacency=orbit_data(radius)
    w=entry['ordered_partition_values']
    assert len(w)==len(classes)
    assert all(type(t) is int and t>0 for t in w)
    residual=[]
    for i in range(len(classes)):
        q=squares[i]
        neighbors=sum(count*w[j] for j,count in adjacency[i].items())
        residual.append((72*q-49)*w[i]-4*q*neighbors)
    return classes,mult,squares,adjacency,w,residual

c11,m11,q11,n11,w11,r11=cert(11)
assert len(c11)==191
assert min(r11)>0
c12,m12,q12,n12,w12,r12=cert(12)
assert len(c12)==264
exact_gap=sum((Fraction(m12[i],q12[i])*w12[i]*r12[i]
               for i in range(len(c12))),Fraction(0))
assert exact_gap<0
print('R11_orbits',len(c11),'smallest_exact_positive_residual',min(r11))
print('R12_orbits',len(c12),'four_times_energy_minus_49_times_Hardy',exact_gap)
print('R12_gap_is_strictly_negative',exact_gap<0)
print('EXACT_CERTIFICATES_PASS')
