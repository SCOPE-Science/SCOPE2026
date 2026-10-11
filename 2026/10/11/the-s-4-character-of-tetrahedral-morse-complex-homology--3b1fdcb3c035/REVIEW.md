# Review

Claim reviewed: For the natural action of \(S_4\) permuting the vertices of the tetrahedron \(\Delta^3\), the rational \(S_4\)-module \(H_4(\mathcal M(\Delta^3);\mathbb Q)\) has character values \((99,1,-1,0,-1)\) on the cycle types \((1^4),(2,1^2),(2^2),(3,1),(4)\). Consequently, \[H_4(\mathcal M(\Delta^3);\mathbb Q)\cong 4S^{(4)}\oplus13S^{(3,1)}\oplus8S^{(2,2)}\oplus12S^{(2,1,1)}\oplus4S^{(1,1,1,1)}.\]

## Correctness
**PASS.** The object and action are explicit. The verifier reconstructs all \(28\) primitive regular pairs and all \(12{,}820\) nonempty Morse-complex simplices, reproducing the established face vector. It verifies a complete face-poset matching over all \(58{,}680\) Hasse covers, leaving critical vector \((1,0,0,2,101,0,0)\). The signed Morse boundary \(d_4\) contains a determinant-\(-1\) full-rank minor, so its Smith invariants are \((1,1)\), independently giving reduced homology \(\mathbb Z^{99}\) only in degree \(4\). For each \(S_4\) conjugacy class, the signed trace on simplicial chains is enumerated directly, and equivariant Euler--Poincaré then yields the stated homology character. Character inner products give the stated irreducible multiplicities.

## Originality
**PASS, with the residual search risk recorded in `AUDIT.json`.** The 2019 source explicitly says the Morse-complex homotopy type remained elusive even for the \(3\)-simplex. The 2026 exact paper solves the nonequivariant homotopy type and gives structural results, but searches of its accessible full text for “equivariant,” “representation,” “symmetric group,” and \(S_4\) do not produce the claimed homology representation. The 2021 automorphism paper determines the automorphism group but not its action on homology. Targeted published-finding corpus and web searches for the character, representation, and equivalent formulations returned no matching statement.

## Value
**PASS.** This is a natural symmetry refinement of a canonical benchmark singled out repeatedly in the Morse-complex literature. The nonequivariant rank \(99\) does not determine how tetrahedral relabelings act. The decomposition identifies the precise proportions of all five irreducible \(S_4\)-types, supplying data relevant to equivariant topology, fixed-point/Lefschetz questions, and symmetry-aware comparisons of Morse-complex constructions.

## Closest literature and limitations
Closest literature consists of arXiv:1909.11440 for the motivating gap and permitted primary classification, arXiv:1904.10907 for the automorphism group, arXiv:math/0011234 for the original face-vector and homology computation, and arXiv:2604.18172 for the now-known nonequivariant homotopy type. None of the inspected statements supplies the character or decomposition claimed here. The result remains rational and equivariant-homological rather than a full equivariant homotopy classification.

Same-model review: passed. Independent audit: not yet performed.
