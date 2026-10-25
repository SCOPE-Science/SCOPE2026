"""Independent p-rank checker via Artin-Schreier branch support in degree-two projection."""
from bideg23 import nsm
from collections import Counter
import sympy as sp
z=sp.symbols('z')

def rank_branch(mask):
    B=sum(((mask>>(4+j))&1)*z**j for j in range(4))
    assert B!=0
    constant,factors=sp.factor_list(B,modulus=2)
    roots=sum(sp.degree(f,z) for f,e in factors)
    if ((mask>>7)&1)==0:roots+=1
    assert roots in (1,2,3)
    return roots-1

C=Counter();D=Counter()
for mask,w,n1 in nsm:
 r=rank_branch(mask)
 C[r]+=w;D[(n1,r)]+=w
print('Branch support p ranks',sorted(C.items()))
print('Branch joint',sorted(D.items()))
