# Self-review

## Correctness — PASS

The even-rectangle condition is equivalent to the binary row-plus-column representation, unique up to a common flip. Fixed-point equations are reconstructed separately for the identity, class-transposition, and class-three-cycle cosets of the full wreath action. In the identity coset, the rank-one binary fixed character and cycle-index identities give the named-class count. In the transposition coset, the exchanged-edge block requires an even-cycled square permutation; the fixed third-class permutation contributes squared-cycle weights, including the all-four-divisible correction. In the three-cycle coset, two order reversals cancel, leaving a block fixed under conjugate permutations. Burnside's lemma then gives the claimed formula. The sharp modulus-four statement follows because the only modulus-four term is positive at every positive multiple of four and zero at every integer congruent to two mod four. No hidden asymptotic assumption is used.

The independent-from-formula affine fixed-point checker exhaustively covers all class permutation cosets and internal permutations through \(n=4\), and symbolic integrality is tested over more sizes. These computations corroborate but are not substituted for the infinite proof.

## Originality — PASS, with explicit residual risk

The 2013 primary source identifies exactly the semigeneric class and supplies a Ramsey expansion, not the three-class unlabelled fixed-point orbit count. The 2019 source gives a binary equivalence-class characterization and unique ergodicity, not a finite full-wreath orbit formula. Cherlin supplies structural classification, not this counting refinement in the inspected discussion. A published published-finding corpus exact Stirling-layer profile concerns injective labelled tuple orbits, which is not equivalent to quotienting triples of rank-one binary orientation matrices by all three-class relabellings. The closest accessible prior two-part character handles only one edge block, whereas the new count explicitly requires three coupled blocks, 3-cycle cosets, and a nonzero period-four correction. Searches for the exact values and synonyms gave no covering enumeration. Highly specialized or unindexed literature may contain the same count implicitly; search failure cannot prove absolute novelty.

## Value — PASS

The three-class balanced configuration is the first natural case where two-part semigeneric parity orientations interact under a nontrivial cycle of class labels. The theorem gives a complete unlabelled classification for every size, not isolated computed cases, and identifies a sharp period doubling caused specifically by side-exchange symmetry. The degree-nine growth and explicit first coefficients support comparisons of labelled versus unlabelled ages and of named versus unnamed equivalence classes. No broader asymptotic theorem or independently certified uniqueness is claimed.

## Limits and closest literature

Primary sources: Cherlin's discussion of the imprimitive semigeneric directed graph; Jasiński–Laflamme–Nguyen Van Thé–Woodrow, arXiv:1310.6466, Section 10; Jahel, arXiv:1902.04903, Sections 1–2. Closest related published enumerator: the exact Stirling-layer profile of the semigeneric complete multipartite digraph (published-finding corpus identifier `2026/10/4/SCOPE-exact-stirling-layer-orbit-profile-of-the-semigeneric-complete-m--5135d85e91a6`), whose implication reaches labelled patterns but not the full unlabelled symmetry quotient. The two-class parity-character method is a previously established subcase. Residual risk: an indexed record or book section may implicitly contain the tripartite Burnside sum; no complete universal novelty certification is possible.

Self-review: passed. Independent audit: not yet performed.
