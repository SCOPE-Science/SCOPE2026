# Review: universal local Hausdorff–Gromov–Hausdorff Jung constant

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The scaling step was checked directly against Theorem 4 of Adams–Frick–Majhi–McBride.

If \(h=d_{\mathrm H}(A,M)\) and the metric is multiplied by \(\lambda^2=(\delta/h)^2\), then both Hausdorff and Gromov–Hausdorff distances are multiplied by \(\lambda\), sectional curvature is divided by \(\lambda^2\), and convexity radius is multiplied by \(\lambda\). Thus the rescaled curvature parameter is exactly
\[
q_h=\kappa_+h^2/\delta^2.
\]
For positive curvature, the second term in their minimum has a positive limit while the first equals \(\alpha_n(q_h)\delta\). The restriction
\[
\delta<\pi/[4(c_n+1)]
\]
places the first term strictly below the second for all sufficiently small \(h\), giving the stated scale-sensitive lower bound after scaling back. The Taylor coefficient follows from the standard expansion of \(\sin x/x\).

The upper estimate was checked against the inequalities in Schott's proof of Theorem 3.6. His transported correspondence obeys
\[
\operatorname{Mot}\le rK_r\ell_n,\qquad
\operatorname{dis}\le r\bigl(K_r\ell_n+2(K_r-K_r^{-1})\bigr),
\]
with \(\ell_n=2c_n\). Smooth normal coordinates give \(K_r=1+O(r^2)\), so both quantities are \(2c_nr+O(r^3)\); the correspondence formula for \(d_{\mathrm{GH}}\) then gives
\[
d_{\mathrm{GH}}(M\setminus B_r(a),M)\le c_nr+O(r^3).
\]
The scale-sensitive lower bound applies to the same deleted-ball subset, so the two estimates combine to the claimed two-sided cubic asymptotic.

Scaling consistency, the Euclidean case, the nonpositive-curvature case, and the one-dimensional exception were checked separately. No empirical computation is used in place of proof.

## Originality

The closest prior results inspected were:

- Adams–Frick–Majhi–McBride, Theorem 4, which gives a fixed-metric lower coefficient \(\alpha(n,\kappa)\). For positive \(\kappa\), their stated coefficient is strictly below the Euclidean Jung constant.
- Adams et al., arXiv:2607.18447, which establishes the Euclidean/normed-space Jung lower bound.
- Schott, arXiv:2609.12625, which proves exact Euclidean sharpness and a Riemannian deleted-ball upper bound approaching the Euclidean constant. Its introduction explicitly identifies tightness of the Riemannian comparison with the earlier lower theorem in the nonpositive-curvature case.

Searches included combinations of “Hausdorff vs Gromov–Hausdorff”, “Riemannian”, “positive curvature”, “Jung constant”, “dense subset”, “deleted ball”, “punctured ball”, “asymptotic”, “scale”, and the constant \(\sqrt{(n+1)/(2n)}\). The current SCOPE archive was also checked by source identifier and synonymous claim terms. No record or external source was found stating the scale-optimized lower bound with curvature parameter \(\kappa h^2\), the curvature-independent limit
\[
\lim_{h\downarrow0}\mathcal C_M(h)=c_n,
\]
or the matching \(c_nr+O(r^3)\) deleted-ball asymptotic.

The main residual risk is that the lower bound is obtained by a concise rescaling optimization of a published theorem, so an equivalent observation could occur in discussion, notes, or work not indexed under the same terminology. The motivating converse preprint is recent, which also leaves some risk of not-yet-indexed parallel work. No inaccessible paper was identified whose title or abstract gives concrete evidence of the same result.

## Value

The result removes the positive-curvature gap left between the best fixed-metric lower coefficient and Schott's Euclidean-model upper construction. It shows that the sharp infinitesimal constant is universal across all closed Riemannian manifolds and that curvature enters only at quadratic order in the distance ratio. The scale-sensitive inequality also applies to every sufficiently dense compact subset, not only to the deleted-ball examples used for sharpness.

The matching cubic estimate for deleted geodesic balls turns the leading-order statement into a quantitative local model and gives a canonical asymptotically extremizing family on every manifold.

## Limitations

The optimal coefficient of the \(h^2\) correction in the ratio is not determined. The theorem does not classify asymptotically extremizing subsets, and the deleted-ball correspondence is not proved exactly optimal away from the flat model. The statement is restricted to smooth closed Riemannian manifolds of dimension at least two. No independent audit has yet been performed.
