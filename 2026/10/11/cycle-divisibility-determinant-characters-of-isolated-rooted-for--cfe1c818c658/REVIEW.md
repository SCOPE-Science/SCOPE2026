# Independent mathematical audit

## correctness

PASS

Exact Y_m identification with Knudson–Owens–White Theorem 9.5 gives integral homology concentrated in degree m−3 with the stated sphere count, including m=3 (six vertices, five reduced H_0 classes). For any g with cycle lengths λ_i, a g-equivariant parent map on a non-root source cycle i selects a distinct target cycle j with λ_j | λ_i and one of λ_j equivariant phases. The original forest is acyclic iff this finite quotient parent graph is acyclic: a quotient directed cycle lifts to a directed cycle after finitely many phase traversals. Each non-root cycle gives simplicial sign times arc-action parity (−1)^λ_i(−1)^(λ_i−1)=−1, so a quotient forest with s non-root cycles has weight (−1)^s. The signed directed matrix–forest theorem with edges weighted −λ_j gives det(I−L_I), with empty determinant 1. Inclusion–exclusion over nonempty forced isolated quotient cycles imposes exactly the actual original-vertex-isolation condition; the augmented Lefschetz sign and single-degree concentration yield (−1)^(m−2) times the boxed determinant sum. A separate exact-rational Python checker enumerated all parent functions and fixed simplices for all 26 conjugacy classes m=3..6, independently recomputing the signed Lefschetz traces and determinant formula, including dimension ranks (5,25,189,2041). The finite check corroborates, but does not replace, the uniform combinatorial proof.

## originality

PASS

Best-of-knowledge PASS for the isolated-original-vertex subcomplex, not for the known nonequivariant rank or general determinant input. The exact matching Knudson–Owens–White object is only non-equivariantly classified; Bernardi–Klivans gives a general weighted forest determinant, not the restricted homology character. Kozlov/Stanley treat the unrestricted directed-forest complex, whose character does not by itself fix the isolated subcomplex. The all-cycle-type orbit-divisibility plus isolated-orbit Lefschetz formula is not implied by inspected prior statements. Kozlov 1999 original full text was inaccessible and an unindexed equivalent remains possible; this limitation alone is not adverse coverage.

## value

PASS

The exact isolated-vertex rooted-forest subcomplex occurs naturally in a recent full strong-Morse-complex analysis and has a published sphere-wedge rank but no determined permutation action in the checked primary theorem. A closed character valid simultaneously for all m≥3 and every conjugacy type determines the complete rational S_m module, not a small instance or arbitrary invariant. Nonidentity traces distinguish genuinely different representations with the same Betti count; e.g. m=4 has 25-dimensional top homology but a transposition has trace −3. The cycle-divisibility phase weights, signed Lefschetz and isolate inclusion–exclusion are nontrivial and enable exact further representation-theoretic questions. No claim of a global strong-Morse-complex equivariant equivalence, integral module decomposition, or explicit general Specht multiplicities is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
