# Review

Same-model review: passed. Cross-model review: not yet performed.

## Correctness

The coefficient \(\beta(K)\) is well defined and lies in \([1,2]\): the lower bound follows by taking both test bodies equal to \(K\), while Fenchel's mixed-volume inequality supplies the upper bound.

The relative-inradius estimate was checked by retaining the factor \(\beta(K)\) in Langharst--Wang's inner-parallel-body proof. Alexandrov--Fenchel is applied before the Bézout estimate, so the coefficient is raised to the power \(n-1\). The inclusion \(K_s+sM\subseteq K\) supplies the final linear mixed-volume bound. After the exact inner-parallel integral identity, the normalized inradius \(\eta\) obeys
\[
1\le\beta(K)^{n-1}(1-(1-\eta)^n),
\]
which is equivalent to the stated lower bound.

The chord estimate was checked independently from the projected proof. The projection formula converts the two-body mixed-volume inequality to a bound with one factor \(\beta(K)\); Minkowski's first inequality in dimension \(n-1\) raises it to \(\beta(K)^{n-1}\). Layer cake then gives the same scalar inequality for the normalized longest-chord parameter.

For the difference-body bound, the full layer-cake identity for the covariogram was retained rather than evaluated only at zero. The radial function of \(K-K\) equals the longest chord length in each direction. Polar integration and the identity \(\int g_K=V_n(K)^2\) then produce
\[
V_n(K-K)/V_n(K)\ge
[n\beta(K)^{n-1}J_n(\phi_n(\beta(K)))]^{-1}.
\]
At \(\beta=1\), the beta integral \(J_n(1)=1/(n\binom{2n}{n})\) makes this exactly the Rogers--Shephard equality value, providing a consistency check.

Böröczky's Theorem 1 was inspected directly. It states that a Rogers--Shephard deficit \(\delta\) implies
\[
d_{\rm BM}(K,\Delta_n)\le1+n^{50n^2}\delta.
\]
Substituting the proved upper bound on that deficit is therefore valid. The small-defect expansion was checked from
\(J_n'(1)=-nJ_n(1)\) and
\(1-\phi_n(1+\varepsilon)\sim((n-1)\varepsilon)^{1/n}\).

## Originality

Langharst--Wang's complete arXiv version was inspected at the theorem statement, chord proof, covariogram preliminaries, and inner-parallel-body proof. Their paper proves the exact \(\beta=1\) characterization and explicitly notes the connection with Chakerian's Rogers--Shephard argument, but it does not state a quantitative stability theorem, a non-unit coefficient version of the normalized chord/inradius conclusions, or a bound from the Bézout coefficient to the Rogers--Shephard deficit.

Böröczky's Rogers--Shephard stability paper was inspected at Theorem 1. Its input is the difference-body volume deficit and its output is Banach--Mazur distance from a simplex; it does not involve the Bézout mixed-volume coefficient.

Searches covered "Bézout/Bezout coefficient" with Rogers--Shephard, difference bodies, Banach--Mazur distance, relative inradius, simplex stability, the notation \(b_2(K)\), and the recent arXiv identifier. The older Soprunov--Zvavitch, Saroglou--Soprunov--Zvavitch, Szusterman, Xiao, and zonoid-related Bézout literature was also checked through titles, abstracts, and relevant accessible statements. No prior source was found with the quantitative bridge or the displayed global Banach--Mazur bound. Searches of the current SCOPE archive by the same object and claim families found no overlap.

No inaccessible source was identified whose title or accessible metadata specifically indicates this theorem. Because the motivating all-dimensional characterization was submitted on 17 September 2026, unindexed or unpublished parallel work remains a meaningful residual risk.

## Value

The result turns a newly completed qualitative characterization of simplices into a global quantitative stability statement in a standard affine distance. It also isolates two intermediate estimates—uniform normalized relative-inradius and longest-chord bounds—and an explicit lower bound on the difference-body volume. The exact calibration at \(\beta=1\) shows that the bridge is compatible with the sharp Rogers--Shephard equality case rather than merely giving a qualitative compactness consequence.

## Limitations

The exponent \(1/n\) is not proved optimal. The explicit Banach--Mazur constant inherited from the general Rogers--Shephard stability theorem is very large. No converse quantitative estimate from Banach--Mazur distance to \(\beta(K)-1\) is established. The very recent date of the motivating preprint leaves residual originality uncertainty from unindexed parallel work.
