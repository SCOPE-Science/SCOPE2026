# Review

## Correctness

**PASS.**

The main identity was checked directly against the normalization in Ge--Li--Li. They set \(E=R-\operatorname{Id}\), prove
\[
2\operatorname{tr}E=\operatorname{Scal}-n(n-1),
\]
and normalize \(H_1(E)=2\operatorname{tr}E/[n(n-1)]\). Thus
\[
\binom{n/2}{1}H_1(E)=\operatorname{tr}E/(n-1).
\]
Their Lemma 2.1 gives \(H_j(E)\ge0\) for every relevant \(j\) when \(E\ge0\).

For even \(n=2m\), their exact Pfaffian expansion is
\[
e_g=\frac2{\omega_n}\sum_{j=0}^m\binom mjH_j(E).
\]
On the simply connected cover, positive curvature operator and the Böhm--Wilking theorem give sphere topology, so Chern--Gauss--Bonnet yields
\[
\omega_n=\sum_{j=0}^m\binom mj\int H_j(E).
\]
Subtracting the \(j=0\) volume term proves the exact even-dimensional defect identity.

For odd \(n=2m+1\), their boundary density is
\[
b_g=\omega_n^{-1}\sum_{j=0}^m\binom{n/2}{j}H_j(E)
\]
and the expander filling gives \(\int b_g\le1\) under the strict hypothesis. The non-strict case follows by their same constant-rescaling device: for \(g_a=ag\), \(a<1\), one has \(R_{g_a}>\operatorname{Id}\), and the polynomial integrands converge as \(a\uparrow1\). This proves the odd-dimensional hierarchy.

The passage to non-simply-connected manifolds is valid because \(R\ge\operatorname{Id}\) implies \(\operatorname{Ric}\ge(n-1)g\), so Bonnet--Myers makes the fundamental group finite. On the universal Riemannian cover, volume and all invariant curvature-polynomial integrals are multiplied by \(q=|\pi_1(M)|\), giving the reference volume \(\omega_n/q\).

The Schatten consequences use only positivity: for \(E\ge0\), \(\|E\|_{S_1}=\operatorname{tr}E\) and \(\|E\|_{S_p}\le\|E\|_{S_1}\). The superlevel estimate is ordinary Markov inequality. The sectional-curvature consequence is valid because a unit decomposable two-form \(\xi\) satisfies \(K(\xi)-1=\langle E\xi,\xi\rangle\le\|E\|_{S_\infty}\).

The nonlinear curvature-floor estimate was checked from the source paper's eigenform formula. If \(a=\lambda_{\min}(E)\), every eigenvalue of \(E\) is at least \(a\); replacing the eigenvalues by \(a\) in the positive sum gives \(H_j(E)\ge a^jH_j(\operatorname{Id})=a^j\). Thus the full defect hierarchy controls \(P_n(a)=\sum_j\binom{n/2}{j}a^j\). In even dimension this is \((1+a)^{n/2}-1\). On the constant-curvature metric with \(k=1+\tau\), equality holds pointwise in all these comparisons, and the resulting concentration inequality is exactly an equality.

Sharpness was checked on \(g_k=k^{-1}g_{\mathbb S^n}\): \(E=(k-1)\operatorname{Id}\), \(\dim\Lambda^2=n(n-1)/2\), and \(\operatorname{Vol}=\omega_nk^{-n/2}\). The ratio of integrated trace excess to volume deficit tends to \(n-1\) as \(k\downarrow1\), so the coefficient cannot be reduced.

## Originality

**PASS, to the best of our knowledge.**

The full v1 text of Ge--Li--Li, arXiv:2609.19851, was inspected. It proves the sharp total scalar-curvature theorem and explicitly develops the positive \(H_j(E)\) expansions used here, but it does not state a Bishop-volume-deficit stability theorem, a Schatten-norm estimate, the nonlinear curvature-floor concentration law, or the sharp trace-norm constant. Searches within the paper found no occurrences of “stability”, “deficit”, “Schatten”, or “almost maximal”. Its introduction motivates the idea that regions of large curvature should occupy small volume, while the published theorem is formulated in terms of total scalar curvature.

Related almost-maximal-volume literature under Ricci lower bounds was checked for equivalent coverage. Perelman's almost-maximal-volume theorem and the Chen--Rong--Xu quantitative space-form rigidity results concern topological/Gromov--Hausdorff rigidity rather than an explicit integral norm of the full curvature operator. Kwong's 2026 refinement combines a Ricci lower bound with scalar-curvature information to improve Bishop volume comparison; it does not imply the present full curvature-operator trace-norm estimate under the stated hypotheses.

Targeted searches for combinations of “Bishop volume deficit”, “curvature operator”, “L1”, “trace norm”, “Lipschitz--Killing”, “almost maximal volume”, and equivalent sphere-pinning terminology did not locate the defect hierarchy (1) or the sharp estimate (2). Current successful SCOPE records were also searched by the source arXiv identifier, curvature-operator terminology, Bishop deficit, and Lipschitz--Killing terminology without a collision.

No inaccessible paper was identified as a specific likely source of prior coverage. The principal originality risk is that the result is a short but nontrivial reorganization of an extremely recent theorem and its proof identities; a later revision or unindexed parallel observation could state the same stability consequence.

## Value

**PASS.**

The result converts a scalar integral inequality into a quantitative full-curvature stability statement. Under \(R\ge\operatorname{Id}\), positivity turns the scalar excess into the trace norm of the complete curvature-operator excess, so the Bishop volume deficit controls every Schatten \(L^1\) norm. Retaining all higher positive curvature polynomials yields a genuinely nonlinear consequence: the volume of the region where \(R\ge(1+\tau)\operatorname{Id}\) decays like the reciprocal of \(P_n(\tau)\), and in even dimension like \(((1+\tau)^{n/2}-1)^{-1}\). This directly realizes the curvature-versus-volume mechanism motivating the source paper.

The trace-norm coefficient is optimal to first order. More strongly, in even dimensions the nonlinear floor-concentration bound is exactly saturated by every round rescaling of curvature \(1+\tau\). The defect identity therefore records an exact nonnegative budget involving every Lipschitz--Killing curvature excess, not merely a one-term restatement of the scalar estimate.

## Limitations and residual risk

- The pointwise hypothesis \(R\ge\operatorname{Id}\) is substantially stronger than a Ricci lower bound.
- No higher-\(L^p\) estimate for curvature magnitude is established here without additional geometric input.
- The trace-norm coefficient and the even-dimensional nonlinear curvature-floor bound are sharp on round rescalings; no optimality claim is made for each individual higher-order \(H_j\) bound separately.
- The odd-dimensional hierarchy is an inequality because the expander filling contributes a nonnegative interior Euler term.
- The main input theorem is extremely recent, so later revisions or unindexed parallel observations remain a genuine originality risk.
- This is a structural consequence of Ge--Li--Li rather than an independent proof of their total scalar-curvature estimate.
- Independent audit has not been performed.

Same-model review: passed. Independent audit: not yet performed.
