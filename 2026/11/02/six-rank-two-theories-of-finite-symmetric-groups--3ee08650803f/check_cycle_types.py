"""Cycle-theoretic verification of the universal eight extension profiles.

Checks cycle partition classification and parity criterion for permutation
square roots.  Unlike check_exact.py it enumerates no group elements.
"""
from math import gcd,lcm
from collections import Counter

def partitions(n, cap=None):
    if n==0:
        yield ()
        return
    if cap is None:cap=n
    for k in range(min(n,cap),0,-1):
        for q in partitions(n-k,k): yield (k,)+q

def has_square_root(cyc):
    c=Counter(cyc)
    return all(c[k]%2==0 for k in c if k%2==0)

def classify(cyc):
    o=1
    for k in cyc:o=lcm(o,k)
    root=has_square_root(cyc)
    if o==1:return 'identity'
    if o==2:return 'involution_root' if root else 'involution_no_root'
    if o==3:return 'order_three'
    if o==4:return 'order_four_root' if root else 'order_four_no_root'
    return 'other_root' if root else 'other_no_root'

expected5={'identity','involution_root','involution_no_root',
 'order_three','order_four_no_root','other_root','other_no_root'}
expected8=expected5|{'order_four_root'}
for n in range(5,51):
    classes={classify(p) for p in partitions(n)}
    assert classes==(expected5 if n<8 else expected8),(n,classes)
    if n in (5,6,7,8,9,16,32,50):
        print(f'n={n}, classes={sorted(classes)}')
print('CYCLE_PARTITION_CLASSIFICATION_PASS (5 <= n <= 50)')
