#!/usr/bin/env python3
# Exact illustrative tests for complementary binary-pattern progression reflection.
from itertools import product

def bits(n):
    return bin(n)[2:]

def occurrences(w, v):
    return sum(w[i:i+len(v)] == v for i in range(len(w)-len(v)+1))

def E(n,v):
    z=len(v)-len(v.lstrip('0'))
    return occurrences('0'*z+bits(n),v)

def delta(v):
    a=len(v)-len(v.lstrip('0'))
    return int(a>0 and '1' in v and v=='0'*a+'1'*(len(v)-a))

N=0
for size in range(2,9):
 for vt in product('01',repeat=size):
    v=''.join(vt)
    if not ('0' in v and '1' in v):continue
    u=''.join('1' if x=='0' else '0' for x in v)
    for d in range(1,16):
     for start in range(0,31):
      a=5
      xs=[start+i*d for i in range(a)]
      L=max(x.bit_length() for x in xs)+size+2
      ys=[(1<<L)-1-x for x in xs[::-1]]
      assert all(E(ys[i],u)==E(xs[a-1-i],v)+delta(u) for i in range(a)),(v,u,start,d)
      assert all((E(ys[i],u)-E(ys[0],u))==(E(xs[a-1-i],v)-E(xs[-1],v)) for i in range(a))
      N+=1
print('PASS complementary pattern reflection checks:',N,'configurations;','both colors and exact counts.')
