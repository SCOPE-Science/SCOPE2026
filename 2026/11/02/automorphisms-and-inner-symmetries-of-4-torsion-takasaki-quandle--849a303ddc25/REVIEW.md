# Scientific review

## Correctness — PASS

The formula follows from the intrinsic orbit decomposition of the core quandle: each orbit is exactly a residue modulo two, and quandle preservation forces an affine permutation of these orbits and one unrestricted translation on each fiber. The proof separately reconstructs necessary conditions, verifies sufficiency, counts parameters without overcounting, and proves that the right translations span exactly the identity fiber function plus all constant fiber functions. It treats every integer \(d\ge1\), not only tested cases. The companion checker exhaustively evaluates the permitted permutation/image patterns for \(d=1,2\), checks the inner-group rank for \(1\le d\le4\), and returns `VERIFY_OK`. Computation is supporting evidence rather than an infinite proof.

## Originality — PASS, with historical qualification

The closest new source, Bardakov–Sangare (arXiv:2610.18676, initial posting 2026-10-13), poses as Question 3.5 the automorphism groups of products containing even-dihedral factors. Its explicit automorphism formula is restricted to Latin Alexander quandles and therefore does not imply the displayed result for \(R_4^d\). The 2017 paper arXiv:1705.10607, §5, supplies the usual affine subgroup and a formula for the inner group, but the stated Corollary 5.5 predicts \(2^{2^d}\) inner automorphisms, in direct contradiction to the explicit generator relations for \(d\ge2\). Hou (2011, doi:10.1016/j.jalgebra.2011.06.027) asserts determination of general Alexander-quandle automorphism groups in the abstract; no full text was accessible for an exact implication comparison. This is a significant historical-coverage risk, particularly for the full-group specialization, despite the 2026 paper continuing to pose even-dihedral product cases. The 2014/2015 affine-mesh theory is broader in principle, but the inspected representation/isomorphism results do not state this concrete automorphism-group decomposition or corrected group order. The 2025 small-quandle enumeration ends at order ten, below \(4^2\). Searches for alternative Takasaki, core-quandle and even-dihedral formulations found no directly covering published record. This is evidence for qualified originality, not proof of universal historical priority.

## Mathematical value — PASS

The theorem resolves the first uniform all-ranks non-Latin family in the explicitly posed even-dihedral-product problem, giving the entire automorphism group, the exact size, the displacement group, the inner group, and a sharp count of non-affine symmetries. It also exposes and corrects a consequential infinite-family rank error in a prior inner-group statement rather than merely renaming a known fact. This is structurally meaningful independently of its elementary proof. It does not cover arbitrary even moduli or all medial quandles.

## Closest sources and residual limits

Bardakov–Sangare, arXiv:2610.18676v1 (§3 and Question 3.5); Bardakov–Nasybullov–Singh, arXiv:1705.10607v3 (§5, especially Theorem 5.3 and Corollary 5.5); Jedlička–Pilitowska–Stanovský–Zamojska-Dzienio, arXiv:1409.8396v2 (affine meshes, representation and isomorphism theorem); Salix–Wood, arXiv:2510.26673v1 (small enumerations). Hou’s general Alexander-quandle automorphism result and mesh specialization might reproduce part of the formula, and unindexed earlier group classifications could affect priority. No extrapolation to other groups is intended.

Self-review: passed. Independent audit: not yet performed.
