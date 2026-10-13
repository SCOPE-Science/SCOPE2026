#!/usr/bin/env python3
"""Exact arithmetic for harmonic characters and Platonic cover invariants."""
from math import gcd

def fejer(n,order,power=1):
    """Trace of H_0+...+H_(n-1) at angle 2*pi*power/order.
    Reduce the integer Laurent sum modulo Phi_order without floats.
    """
    if order==1: return n*n
    coefficients=[0]*order
    for j in range(-n+1,n):
        coefficients[(power*j)%order]+=n-abs(j)
    if order in (2,3,5):
        reduced=[coefficients[i]-coefficients[-1] for i in range(order-1)]
    elif order==4:
        reduced=[coefficients[0]-coefficients[2],coefficients[1]-coefficients[3]]
    else:
        raise ValueError('order not needed in this certificate')
    assert reduced[1:]==[0]*(len(reduced)-1),reduced
    return reduced[0]

def pair(a):
    return (a,0) if isinstance(a,int) else a

def dot(a,b):
    return (a[0]+b[0],a[1]+b[1])

def times(n,a):
    return (n*a[0],n*a[1])

# Each class is (cardinality, rotation order, angle numerator).
# The pairs (0,1),(1,-1) encode phi=(1+sqrt(5))/2 and its conjugate.
cases=[
 ('tetra',3,12,[(1,1,0),(3,2,1),(4,3,1),(4,3,2)],
  {'triv':([1,1,1,1],1),'rot3':([3,-1,0,0],1)},
  {2:2,3:2},2,3,[(1,1),(1,3)]),
 ('octa',4,24,[(1,1,0),(6,2,1),(3,2,1),(8,3,1),(6,4,1)],
  {'triv':([1,1,1,1,1],1),'two':([2,0,2,-1,0],1),
   'std3':([3,1,-1,0,-1],1),'rot3':([3,-1,-1,0,1],1)},
  {2:5,3:3,4:3},3,4,[(1,1),(1,2),(1,3),(1,3)]),
 ('icosa',6,60,[(1,1,0),(15,2,1),(20,3,1),(12,5,1),(12,5,2)],
  {'triv':([1,1,1,1,1],1),'three':([3,-1,0,(0,1),(1,-1)],1),
   'three_conj':([3,-1,0,(1,-1),(0,1)],1),
   'four':([4,0,1,-1,-1],2),'five':([5,1,-1,0,0],2)},
  {2:13,3:9,5:5},5,6,[(1,1),(2,3),(2,4),(2,5)])]
for name,d,group_order,classes,irreps,quotients,inertia,nsubs,factors in cases:
    n=d-1; g=n*n
    traces=[fejer(n,m,a) for size,m,a in classes]
    assert sum(size for size,m,a in classes)==group_order
    assert sum(size*t for (size,m,a),t in zip(classes,traces))==group_order
    for k,t in enumerate(traces):
        total=(0,0)
        for chars,mult in irreps.values():
            total=dot(total,times(mult,pair(chars[k])))
        assert total==(t,0),(name,k,total,t)
    for chars,mult in irreps.values():
        scalar=(0,0)
        for (size,m,a),t,c in zip(classes,traces,chars):
            scalar=dot(scalar,times(size*t,pair(c)))
        assert scalar==(group_order*mult,0),(name,scalar,mult)
    assert g==sum(dim*power for dim,power in factors)
    for order,quotient_genus in quotients.items():
        cyc=[g]
        for j in range(1,order):
            m=order//gcd(order,j)
            possibilities={t for (size,class_order,a),t in zip(classes,traces) if class_order==m}
            assert len(possibilities)==1
            cyc.append(possibilities.pop())
        assert sum(cyc)==order*quotient_genus
        defect=2*g-2-order*(2*quotient_genus-2)
        assert defect==(2*(order-1) if order==inertia else 0)
    assert 2*g-2==group_order*(1-1/inertia)
    assert 2*nsubs==group_order//inertia
    print(name,'genus',g,'characters',traces,'quotients',quotients,'factor_dimensions',factors,'branch_order',inertia)
print('VERIFY_OK')
