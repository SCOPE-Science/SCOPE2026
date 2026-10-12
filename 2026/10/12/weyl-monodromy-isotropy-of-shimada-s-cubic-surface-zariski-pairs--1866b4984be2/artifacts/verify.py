from sympy.combinatorics import Permutation, PermutationGroup

# Shimada, arXiv:2401.15930, Eq. (2.5), with 1-based labels converted below.
cycles = [
[(4,21),(5,20),(6,19),(7,24),(8,23),(12,22)],
[(1,2),(8,12),(9,13),(10,14),(11,15),(22,23)],
[(2,3),(7,8),(13,16),(14,17),(15,18),(23,24)],
[(3,4),(8,9),(12,13),(17,19),(18,20),(24,25)],
[(4,5),(9,10),(13,14),(16,17),(20,21),(25,26)],
[(5,6),(10,11),(14,15),(17,18),(19,20),(26,27)],
]

def perm_from_transpositions(ts):
    a=list(range(27))
    for i,j in ts:
        i-=1; j-=1
        a[i],a[j]=a[j],a[i]
    return Permutation(a)

gens=[perm_from_transpositions(c) for c in cycles]
G=PermutationGroup(gens)
assert G.order()==51840
elts=list(G.generate_schreier_sims())

def stab(S):
    S={i-1 for i in S}
    H=[g for g in elts if {g(i) for i in S}==S]
    K=[g for g in H if all(g(i)==i for i in S)]
    # Induced permutations on the marked lines.
    ordered=sorted(S); pos={x:i for i,x in enumerate(ordered)}
    image={tuple(pos[g(x)] for x in ordered) for g in H}
    return PermutationGroup(H), K, image

S1=(1,2,3,4,5)
S2=(1,2,3,4,21)
T1=(1,2,3,4,5,27)
T2=(1,2,3,4,21,26)

H1,K1,I1=stab(S1)
H2,K2,I2=stab(S2)
J1,L1,A1=stab(T1)
J2,L2,A2=stab(T2)
assert (H1.order(),H2.order(),J1.order(),J2.order())==(120,240,120,120)
assert (len(K1),len(K2),len(L1),len(L2))==(1,2,1,1)
assert (len(I1),len(I2),len(A1),len(A2))==(120,120,120,120)
# The nontrivial pointwise kernel for S2 is exactly sigma_6.
sigma6=gens[5]
assert sigma6 in K2 and sigma6.order()==2
# It is central in the full S2 stabilizer.
assert all(sigma6*g == g*sigma6 for g in H2.generate_schreier_sims())
# Direct-product splitting: the derived subgroup has order 60, and adjoining
# the following involution gives a complement of order 120.
D=H2.derived_subgroup()
assert D.order()==60
comp_cycles=[(1,4),(7,13),(8,16),(10,19),(11,20),(22,25)]
tau=perm_from_transpositions(comp_cycles)
assert tau in H2 and tau.order()==2
C=PermutationGroup(list(D.generators)+[tau])
assert C.order()==120
assert sigma6 not in list(C.generate_schreier_sims())
# C acts faithfully and as all S5 on the five marked lines.
S={i-1 for i in S2}; ordered=sorted(S); pos={x:i for i,x in enumerate(ordered)}
CI={tuple(pos[g(x)] for x in ordered) for g in C.generate_schreier_sims()}
assert len(CI)==120
print('W(E6)_order=51840')
print('orbit_sizes=S1:432 S2:216 T1:432 T2:432')
print('stabilizer_orders=S1:120 S2:240 T1:120 T2:120')
print('pointwise_kernels=S1:1 S2:2 T1:1 T2:1')
print('S2_kernel_generator=sigma6')
print('S2_derived_order=60 complement_order=120')
print('isotropy=S1:S5 S2:C2xS5 T1:S5 T2:S5')
print('VERIFY_OK')
