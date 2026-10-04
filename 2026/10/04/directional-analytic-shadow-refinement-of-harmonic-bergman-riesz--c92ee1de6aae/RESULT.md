# Directional analytic-shadow refinement of harmonic Bergman Riesz–Fejér

## Finding

Let \(\alpha>-1\), and let \(a^2_\alpha(\mathbb D)\) be the weighted harmonic Bergman space for
\[
dA_\alpha(z)=(\alpha+1)(1-|z|^2)^\alpha dA(z),
\]
where \(dA\) is normalized area measure. Write
\[
f(z)=c+\sum_{n\ge1}a_nz^n+\sum_{n\ge1}b_n\overline z^{\,n},
\qquad c=f(0),
\]
and set
\[
\beta_n=\|z^n\|_{A^2_\alpha}^2
=\frac{\Gamma(n+1)\Gamma(\alpha+2)}{\Gamma(n+\alpha+2)}.
\]
For every \(|\zeta|=1\), define
\[
F_\zeta(w)
=
c+\sum_{n\ge1}
\bigl(a_n\zeta^n+b_n\overline\zeta^{\,n}\bigr)w^n.
\]
Then \(F_\zeta\in A^2_\alpha\) and
\[
F_\zeta(r)=f(r\zeta)
\qquad(0\le r<1).
\]
If \(\lambda_\alpha\) denotes the analytic weighted Bergman Riesz–Fejér constant used by Andreev and by Halder--Kumar, then
\[
\int_0^1|f(r\zeta)|^2(1-r)^{\alpha+1}\,dr
\le
\lambda_\alpha\|F_\zeta\|_{A^2_\alpha}^2.
\]
Moreover,
\[
\|F_\zeta\|_{A^2_\alpha}^2
=
|f(0)|^2+
\sum_{n\ge1}\beta_n
\left|a_n\zeta^n+b_n\overline\zeta^{\,n}\right|^2
\le
2\|f\|_{a^2_\alpha}^2-|f(0)|^2.
\]
Therefore
\[
\int_0^1|f(r\zeta)|^2(1-r)^{\alpha+1}\,dr
\le
\lambda_\alpha
\bigl(2\|f\|_{a^2_\alpha}^2-|f(0)|^2\bigr).
\]
The zero-at-the-origin hypothesis in the recent harmonic Hilbert-space inequality is thus unnecessary once the constant mode is retained.

For the complete diameter in direction \(\zeta\), the same shadow satisfies \(F_\zeta(-r)=f(-r\zeta)\), hence
\[
\int_{-1}^{1}|f(r\zeta)|^2(1-|r|)^{\alpha+1}\,dr
\le
2\lambda_\alpha
\bigl(2\|f\|_{a^2_\alpha}^2-|f(0)|^2\bigr).
\]
For \(\alpha\ge0\), the known estimate \(\lambda_\alpha\le(1+\alpha)^{-1}\) yields
\[
\int_{-1}^{1}|f(r\zeta)|^2(1-|r|)^{\alpha+1}\,dr
\le
\frac{2}{1+\alpha}
\bigl(2\|f\|_{a^2_\alpha}^2-|f(0)|^2\bigr),
\]
so the coefficient of \(\|f\|_{a^2_\alpha}^2\) is at most \(4/(1+\alpha)<2\pi\) for every \(\alpha\ge0\).

## Assumptions and scope

The result is specific to the Hilbert case \(p=2\). It uses the orthogonal harmonic expansion in the radial weighted measure and the analytic weighted Bergman Riesz–Fejér inequality.

The quantity \(\lambda_\alpha\) is exactly the analytic constant appearing in the cited analytic theorem. No claim is made here that the new harmonic uniform coefficient is the best possible one among all harmonic functions.

The first inequality, involving the exact shadow norm \(\|F_\zeta\|_{A^2_\alpha}\), is direction-sensitive. It can be substantially smaller than the uniform factor-two estimate because analytic and coanalytic coefficients may interfere destructively along a chosen ray.

## Proof

The radiality of \(dA_\alpha\) makes
\[
1,z,z^2,\ldots,\overline z,\overline z^{\,2},\ldots
\]
orthogonal in \(L^2(dA_\alpha)\). Since \(\beta_0=1\),
\[
\|f\|_{a^2_\alpha}^2
=
|c|^2+
\sum_{n\ge1}\beta_n\bigl(|a_n|^2+|b_n|^2\bigr).
\]

Fix \(|\zeta|=1\). The coefficient estimate
\[
|a_n\zeta^n+b_n\overline\zeta^{\,n}|^2
\le
2\bigl(|a_n|^2+|b_n|^2\bigr)
\]
shows that \(F_\zeta\in A^2_\alpha\), with
\[
\|F_\zeta\|_{A^2_\alpha}^2
=
|c|^2+
\sum_{n\ge1}\beta_n
|a_n\zeta^n+b_n\overline\zeta^{\,n}|^2.
\]
For real \(r\in[0,1)\), direct substitution gives
\[
F_\zeta(r)
=
c+\sum_{n\ge1}a_n(r\zeta)^n
+
\sum_{n\ge1}b_n\overline{(r\zeta)}^{\,n}
=f(r\zeta).
\]
The analytic Riesz–Fejér inequality therefore applies directly to the shadow:
\[
\int_0^1|f(r\zeta)|^2(1-r)^{\alpha+1}\,dr
=
\int_0^1|F_\zeta(r)|^2(1-r)^{\alpha+1}\,dr
\le
\lambda_\alpha\|F_\zeta\|_{A^2_\alpha}^2.
\]
Finally,
\[
\|F_\zeta\|_{A^2_\alpha}^2
\le
|c|^2+2\sum_{n\ge1}\beta_n(|a_n|^2+|b_n|^2)
=
2\|f\|_{a^2_\alpha}^2-|c|^2.
\]
This proves the ray estimate.

For the opposite ray,
\[
F_\zeta(-r)=f(-r\zeta),
\]
so applying the analytic inequality to the two half-rays and adding gives the diameter estimate. The explicit \(\alpha\ge0\) bound follows from \(\lambda_\alpha\le(1+\alpha)^{-1}\).

## Verification

The critical step is the exact analytic-shadow identity, not an approximation. The shadow coefficient at degree \(n\) is
\[
a_n\zeta^n+b_n\overline\zeta^{\,n},
\]
so evaluation on the real radius reproduces both the analytic and coanalytic terms of \(f(r\zeta)\) exactly.

The center correction is also exact. The normalized weighted area measure has \(\beta_0=1\), and hence retaining the constant coefficient changes the factor-two bound from \(2\|f\|^2\) to
\[
2\|f\|^2-|f(0)|^2.
\]

As boundary checks, if \(f\) is analytic then \(b_n=0\) and the shadow norm is exactly \(\|f\|_{A^2_\alpha}\), so the statement reduces to the analytic theorem rather than losing a factor of two. If
\[
f(z)=z-\overline z,
\]
then on the positive real ray the shadow vanishes identically, correctly giving zero trace energy there.

No numerical experiment, limiting extrapolation, or unproved coefficient identity is used.

## Relationship to prior work

Halder and Kumar establish the first weighted harmonic Bergman Riesz–Fejér theory. Their general theorem treats \(1<p<\infty\), and their improved Hilbert-space theorem assumes \(f(0)=0\) and proves the one-ray estimate
\[
\int_0^1|f(r\zeta)|^2(1-r)^{\alpha+1}\,dr
\le
2\lambda_\alpha\|f\|_{a^2_\alpha}^2.
\]
Their proof removes the constant term, splits a complex harmonic function into two real harmonic functions, and applies an analytic lift separately to those real components.

The present argument instead packages the complete trace on one ray into a single analytic shadow. This retains the constant mode, preserves analytic/coanalytic cancellation, removes the normalization \(f(0)=0\), and yields the center-energy correction. In particular, the improved \(p=2\) diameter constant extends to every harmonic function, not only normalized ones.

Kasuga's 2025 open-access paper proves the analytic weighted Bergman ray inequality for all positive exponents using the same analytic constant \(\lambda_\alpha\); its \(p=2\) statement records the Andreev estimate used here. That analytic result does not contain the harmonic shadow construction or the center-defect harmonic estimate.

Earlier harmonic Riesz–Fejér papers concern harmonic Hardy spaces and circle-versus-diameter inequalities rather than weighted harmonic Bergman trace estimates. Searches for the center correction, analytic-shadow formulation, and removal of the origin normalization did not locate a published statement implying the result above.

## Limitations

No best harmonic constant is claimed. The estimate
\[
|u+v|^2\le2(|u|^2+|v|^2)
\]
can be sharp coefficientwise, so improving the uniform factor two requires information beyond the separate harmonic Bergman norm, but the theorem does not prove a global optimality statement.

The argument uses the Hilbert structure and does not extend verbatim to \(p\ne2\).

The literature comparison for the 2022 harmonic Hardy-space paper was made from its accessible abstract and scope rather than a full-text novelty determination; no noncoverage claim for hidden details of that article is needed for the accepted result.

## References

1. H. Halder and R. Kumar, *Riesz Theorem and Riesz-Fejér inequality for weighted harmonic Bergman spaces with applications to Möbius invariant spaces*, arXiv:2607.11795v1, 2026.
2. K. Kasuga, *Fejér-Riesz Type Inequalities for Weighted Bergman Spaces*, Far East Journal of Mathematical Sciences 142 (2025), 237–242, DOI:10.17654/0972087125014.
3. V. V. Andreev, *Fejér–Riesz type inequalities for Bergman spaces*, Rendiconti del Circolo Matematico di Palermo 61 (2012), 385–392, DOI:10.1007/s12215-012-0097-z.
4. S. Das and A. Sairam Kaliraj, *A Riesz-Fejér type inequality for harmonic functions*, Journal of Mathematical Analysis and Applications 507 (2022), 125812.
