# Review of sharp GRS recovery for degree-deleted cubic evaluation codes

## Correctness (PASS)

The hypotheses require distinct evaluation values and the exact elementary-symmetric MDS test on each triple. The row-deleted Vandermonde determinant gives the projective-arc property. A dimension-three MDS code is GRS exactly when its columns lie on a nonsingular conic. The six quadratic monomials after substitution have degrees \(\{0,1,2,3,4,6\}\) for the first family and \(\{0,2,3,4,5,6\}\) for the second. Division by the six-point root polynomial proves that the missing coefficient is precisely \(-e_1\), respectively \(-e_5\). Nonzero quadratics cannot vanish at seven distinct parameters, and the five-point arc conic is nonsingular. The five-packing is proved by an at-most-one extension equation on each five-set, including the case of evaluation zero. No extrapolation from finite tests is used in the all-field argument.

The independent-in-form rank calculation in the bundled verifier reproduces the exact conic criteria in all arc-admissible five-, six-, and seven-subsets over \(\mathbb F_{11}\) and \(\mathbb F_{13}\), checks explicit seven-point examples over \(\mathbb F_{17}\), \(\mathbb F_{19}\), and \(\mathbb F_{23}\), and verifies a direct smooth-conic witness for the six-point \(\mathbb F_{19}\) example. It ends with `VERIFY_OK`.

## Originality (PASS)

Ning's 2025 preprint (arXiv:2507.04689) introduces and investigates these exact row-deleted GRS subcodes but does not classify their puncturing-to-GRS profiles. Jin--Ma--Xing--Zhou (arXiv:2411.14779, Proposition VI.1) establish non-GRS under the *strict* restriction \(n>2k\), so for dimension three this covers retention of seven or more coordinates. However, their Proposition V.1 for the first family **also asserts** non-GRS under the weaker \(n\ge2k\), including six points. The explicit MDS smooth-conic example below refutes that asserted equality case as well. The five-point GRS phenomenon and projective-conic recognition are classical and not counted as novel.

Abdukhalikov--Ding--Verma (arXiv:2506.04080, Theorem 3.2) use the weaker restriction \(n\ge2k\) in asserting the code is non-GRS whenever it is MDS. At equality \(n=2k=6\), the displayed example over \(\mathbb F_{19}\) is MDS yet its columns satisfy the explicit nonsingular conic \(XY+14XZ+18Y^2+4YZ+Z^2=0\), making it GRS. Thus neither paper’s weaker non-GRS assertion can legitimately imply the new six-point classification; the counterexample supplies a directly checkable conflicting implication. The strict longer-length statements remain valid and credited. Searches using symmetric-coefficient, Schur-square, GRS-puncturing, six-point-conic and deleted-row aliases found no prior explicit equivalence or five-packing classification for these two families. The closest full-text comparisons are explained in `AUDIT.json`. Unindexed results remain a residual risk, not novelty evidence.

## Value (PASS)

The natural question is not the already-known MDS property, but how much of a non-GRS degree-deleted evaluation code must be punctured before an ordinary GRS structure reappears. The theorem resolves this question for both cubic deleted-row families at every allowable length: the only possible optimum counts are \(n-6\) and \(n-5\), explicitly distinguished by an elementary symmetric test, with a full classification and incidence bound for all optimal six-subsets. Both regimes actually occur. The six-coordinate result also identifies a sharp equality-boundary exception to a stronger non-GRS statement in the prior literature. This is a motivated complete boundary classification, not a distance-table lookup or an arbitrary finite instance.

## Limits and sources

No claim is made for other dimensions, evaluation at infinity, extension constructions, or arbitrary MDS codes. The finite enumerations validate examples and the checker implementation, but the proof of the infinite finite-field statement is the polynomial/conic argument. Principal sources: Ning, arXiv:2507.04689 (2025); Jin--Ma--Xing--Zhou, arXiv:2411.14779 (2024); Abdukhalikov--Ding--Verma, arXiv:2506.04080 (2025); Márquez-Corbella--Pellikaan, arXiv:1508.02187 (2015), Appendix D. Independent review has not been performed.

Self-review: passed. Independent audit: not yet performed.
