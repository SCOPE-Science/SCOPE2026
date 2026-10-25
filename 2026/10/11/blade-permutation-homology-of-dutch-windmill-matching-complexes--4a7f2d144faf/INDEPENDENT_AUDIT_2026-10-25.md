# Independent mathematical audit

## correctness

PASS

PASS. The final claim is for every n>=2 and k>=1, m=3k+1 or 3k+2, on reduced rational homology of the matching complex of n cycles C_m sharing a vertex, under blade permutations preserving cyclic coordinates. Independently verify a_0=1,a_1=0,a_r=a_(r-1)-a_(r-2), giving the six-periodic sequence (1,0,-1,-1,0,1). In a pi-fixed matching, all noncentral blade edge patterns must be constant on each permutation cycle; an edge incident to the common center is unique and must occur on a fixed blade. The orbit-signed sum is F(pi)=A^{c(pi)}-2f(pi)B A^{c(pi)-1}, where A=a_(m-2), B=a_(m-3). On an invariant matching of size s comprising o edge orbits, the simplex orientation sign (-1)^(s-o), times augmented chain sign (-1)^(s-1), equals (-1)^(o-1); including the empty simplex gives reduced Lefschetz=-F. The published Donovan--Scoville Theorem 5.8 concentrates reduced homology in degree nk-1 with rank 1 when m=3k+1 and in degree nk with rank 2n-1 when m=3k+2. Substitution A=(-1)^k, B=0 or B=(-1)^k respectively and sgn(pi)=(-1)^{n-c(pi)} yields exactly sgn(pi)^k and sgn(pi)^k(2f(pi)-1). Over Q, character equality determines the module, so the second is sgn^k tensor (trivial + 2 standard). A separately written fixed-edge-orbit matching enumerator verified all 70 permutations across (n,m)=(2,4),(2,5),(3,4),(3,5),(3,7),(4,4),(4,5); finite checks corroborate but do not establish the all-parameter theorem. Both levels of the Git tree (7 top-level entries; 2 artifact blobs) were independently reconstructed from Git hashes.

## originality

PASS

PASS on a documented best-of-knowledge basis. The exact Dutch-windmill family, including the rank 1 and 2n-1 wedge cases, is already in Donovan--Scoville (NYJM 29 (2023), Theorem 5.8, pp. 1409-1410), but the full theorem and proof give nonequivariant homotopy types, not action characters. The new fixed-orbit Lefschetz calculation determines nonisomorphic S_n-modules which the rank theorem cannot distinguish. Bate--Everitt--Ford--Ramos compute complete-hypergraph matching cohomology and asymptotic representations for fibre-closed families; Dong--Wachs treat the complete-graph matching complex; neither determines the joined-cycle blade action. Shiyue Li proves equivariant log-concavity of graded matching permutation representations for all graphs, not explicit reduced homology characters. Two related published mathematical findings were read: the extended-star Morse complex has a sign-twisted augmentation module for a different object, while the single-cycle dihedral matching-complex formula lacks the common-center coupling and does not imply the windmill S_n-character. Four fresh semantic mathematical-result searches and exact web alias searches found no distinct prior claim of this complete windmill formula; the self-hit is excluded as priority evidence. The author thesis full file could not be accessed (403) and is a residual risk, not a basis for a false noncoverage assertion. Unindexed cactus/windmill equivariant calculations remain possible. Search nonappearance is not proof of novelty.

## value

PASS

PASS. The subgroup S_n permuting identically parametrized cycle blades is canonical for this infinite natural graph family. The known wedge multiplicities alone cannot show whether a blade transposition acts by +1 or -1, or which standard isotypic components appear. The exact all-n and all-k parity-sensitive character and the explicit sgn^k tensor (1+2 Std) decomposition supply natural equivariant information, including traces at every conjugacy class, which can be used in symmetry-invariant and quotient homology calculations. This is a motivated structural refinement, not a known-table recomputation. It does not claim integral lattice decomposition or the larger within-blade automorphism group.

The dated certificate retains the supplied scientific assessment, sources and limitations.
