# Independent mathematical audit

## correctness

PASS

The two factors are invertible integral symplectic shears, and global permutation order is exactly matrix order by testing basis states. For B the bipartite adjacency, B²=diag(bJ_a,aJ_b) and B³=abB. Independently replayed RESULT.md:37–101 using Cayley–Hamilton on A(z)=[[1,z],[1,1+z]]: A^k=F_kA−F_(k−1)I with F_0=0, F_1=1, F_(k+1)=(2+z)F_k−F_(k−1). In Z[z]/(z³−abz), the full congruence is equivalent to simultaneous vanishing of U_k=F_k−F_(k−1)−1 and V_k=F_k after substitution z=B. Modulo two B² vanishes for two even parts, is nonzero but B³ vanishes in the mixed case, and B³=B in the odd case. The resulting orders 4,8,6 have nonidentity witnesses at every maximal proper divisor (U_2=B, U_4=B² in the mixed case, U_3=B+B² for odd parts). Exhausting the eight possible coefficient classes of ab mod 8 by this recurrence reproduced the valuation witnesses of RESULT.md:93 (replay: /workspace/reproductions/5.py). Unit entries of B witness the even-even valuations 1,2; the odd-size part coefficient in B² witnesses the mixed valuations 1,2 when ab≡0 mod 4 and valuation 2 when ab≡2 mod 4. In the odd case the witnesses are 2(I+B²) mod 4 and 4(I+B²) mod 8, and I+B² is nonzero mod 2 whenever some part has more than one vertex. For K_(1,1) the exact U_6 is 44(B+I), V_6 is 72(B+I); hence the valuation is 2, not 1, at the base order 6. To lift, the order at each next modulus divides twice the previous order by squaring I+2^sE; after valuation r≥2 the square increases the valuation by exactly one. The checked anchors give all five regimes including both s=1 and s=2. The uploaded direct-matrix regression was inspected, not executed.

## originality

PASS

The very close catalogue result on the same bipartite adjacency uses L_BU_B, whereas the frozen theorem uses L_IU_B. This is not just an ordering or similarity convention: the full formulas even have differing arithmetic dependencies. Known period methods and lifting principles are credited; the five exact regimes for the stated composition are the supported distinct finding.

## value

PASS

Global order is the exact interval after which all states of a natural finite symplectic shear network recur. The classification covers every modulus exponent and both graph-part sizes, exposes which arithmetic distinctions matter and shows why the single edge delays lifting. This is more informative than a modulus-dependent period search or a general recurrence that leaves its first valuations unresolved. No assertion about a distribution of primitive state periods is needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
