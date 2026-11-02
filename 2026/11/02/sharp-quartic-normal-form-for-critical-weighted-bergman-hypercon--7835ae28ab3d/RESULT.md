# Sharp quartic normal form for critical weighted Bergman hypercontractivity

## Finding

At the sharp dilation radius \(r=1/\sqrt2\) for the weighted analytic Bergman \(L^2\)-to-\(L^4\) inequality, the constant extremizer has a genuine quartic (not quadratic) defect in its first holomorphic direction. After optimizing over *all* higher analytic coefficients, the exact fourth-order coefficient is \(1/[\alpha^2(\alpha+1)]\). The uniquely optimal second-order correction is the quadratic Taylor coefficient of an exponential, \(b_2=a^2/2\). Every analytic mode of degree at least three has a strictly positive, explicitly determined quadratic penalty.

More precisely, use the normalized measure and monomial moments described below. For every \(f(z)=1+az+\sum_{n\ge2}b_nz^n\) in \(A_\alpha^2\), let
\[
D_\alpha(f)=\|f\|_{A_\alpha^2}^{4}-\|f(\cdot/\sqrt2)\|_{A_\alpha^4}^{4},\qquad H=\Big(\sum_{n\ge2}\mu_n|b_n|^2\Big)^{1/2}.
\]
As \(|a|+H\to0\), uniformly over the infinitely many coefficients,
\[
\boxed{\begin{aligned}
D_\alpha(f)= {}&\frac{|a|^4}{\alpha^2(\alpha+1)}
+\frac{2}{\alpha(\alpha+1)}\left|b_2-\frac{a^2}{2}\right|^2\\
&+\sum_{n\ge3}\left(2-2^{2-n}\right)\frac{n!}{(\alpha)_n}|b_n|^2
+o_\alpha\!\left(|a|^4+H^2\right).
\end{aligned}}\]
The remainder is little-o of the *whole leading form*, so the expansion is stable under simultaneous, arbitrarily high-degree perturbations.

If \(a_j\ne0\) tends to zero and \(H_j\to0\), the sharp asymptotic inequality is
\[
\liminf_{j\to\infty}\frac{D_\alpha(f_j)}{|a_j|^4}\ge\frac{1}{\alpha^2(\alpha+1)}.
\]
Equality in the limit holds **if and only if**
\[
 b_{2,j}=\tfrac12a_j^2+o(|a_j|^2),\qquad
 \Big(\sum_{n\ge3}\mu_n|b_{n,j}|^2\Big)^{1/2}=o(|a_j|^2).
\]
The polynomials \(f_a(z)=1+az+\tfrac12a^2z^2\) realize sharpness. For comparison, the affine family has the *exact*, strictly larger deficit
\[
D_\alpha(1+az)=\frac{\alpha+2}{2\alpha^2(\alpha+1)}|a|^4.
\]
With the unit-norm first-mode coordinate \(u=a/\sqrt\alpha\), the optimal quartic coefficient is \(1/(\alpha+1)\), exposing the disappearance of this finite-weight obstruction in the high-weight Gaussian scaling (without asserting uniformity in that limit).

## Assumptions and scope

Fix any real \(\alpha>1\) and the unit disk \(\mathbb D\). Equip analytic functions with
\[
 d\mu_\alpha(z)=\frac{\alpha-1}{\pi}(1-|z|^2)^{\alpha-2}\,dA(z),\qquad
 \|f\|_{A_\alpha^p}^p=\int_{\mathbb D}|f(z)|^p\,d\mu_\alpha(z).
\]
The measure is a probability measure, monomials are orthogonal, and
\[
\mu_n=\|z^n\|_{A_\alpha^2}^2=\frac{n!}{(\alpha)_n},\quad
(\alpha)_n=\alpha(\alpha+1)\cdots(\alpha+n-1),\quad \mu_0=1.
\]
The statement concerns every \(f\in A_\alpha^2\) satisfying \(f(0)=1\) sufficiently close to the constant function in Hilbert norm; the phase and amplitude of a general nonzero constant may be removed using homogeneity. There is no restriction to finite-degree polynomials. The critical radius \(1/\sqrt2\) and the nonnegativity of \(D_\alpha\) follow from the established weighted Bergman hypercontractivity theorem of Melentijević (2022 preprint, 2023 journal publication), not from the perturbative computation alone.

## Proof

**1. Moment identity.** For \(f(z)=\sum_{n\ge0}c_nz^n\), orthogonality gives
\[
\|f\|_{A_\alpha^2}^2=\sum_{n\ge0}\mu_n|c_n|^2,
\qquad \|f(r\cdot)\|_{A_\alpha^4}^4
=\sum_{n\ge0}\mu_nr^{2n}\left|\sum_{k=0}^nc_kc_{n-k}\right|^2.
\]
The second identity is valid for every \(f\in A_\alpha^2\) when \(r<1\): the strict dilation yields bounded analytic functions and hence a square in \(A_\alpha^2\). The identities can first be derived for polynomials and extended by analytic evaluation bounds.

**2. Separate the resonant second-order polynomial.** Put \(h(z)=\sum_{n\ge2}b_nz^n\), \(H=\|h\|_2\), \(r=1/\sqrt2\), and
\[
 P(z)=1+2az+a^2z^2+2h(z),\qquad
 R(z)=2azh(z)+h(z)^2.
\]
Then \(f(z)^2=P(z)+R(z)\), while \(R\) has no coefficients of degrees zero, one, or two. Consequently the cross term \(\langle P(r\cdot),R(r\cdot)\rangle\) involves only the degree-at-least-three tail \(2h(r\cdot)\), not the constant or the critical first mode.

**3. Exact leading part.** Orthogonality and \(r^2=1/2\) give
\[
\begin{aligned}
\|f\|_2^4-\|P(r\cdot)\|_2^2
={}&\mu_1^2|a|^4+2H^2
-\frac{\mu_2}{4}|a^2+2b_2|^2\\
&-\sum_{n\ge3}4\mu_n2^{-n}|b_n|^2
+2\mu_1|a|^2H^2+H^4.
\end{aligned}
\]
Since \(H^2=\mu_2|b_2|^2+\sum_{n\ge3}\mu_n|b_n|^2\), the first line and the first sum complete squares as
\[
\left(\mu_1^2-\frac{\mu_2}{2}\right)|a|^4
+\mu_2\left|b_2-\frac{a^2}{2}\right|^2
+\sum_{n\ge3}\left(2-4\cdot 2^{-n}\right)\mu_n|b_n|^2.
\]
The needed exact scalar identity is
\[
\mu_1^2-\frac{\mu_2}{2}=\frac{1}{\alpha^2(\alpha+1)}.
\]

**4. Infinite-dimensional error control.** At radius \(r=1/\sqrt2\), the reproducing-kernel estimate implies
\[
\|h(r\cdot)\|_\infty\le(1-r^2)^{-\alpha/2}H,
\quad\|h(r\cdot)\|_2\le H.
\]
Therefore
\[
\|R(r\cdot)\|_2\le C_\alpha(|a|+H)H,
\quad\big|\langle P(r\cdot),R(r\cdot)\rangle\big|
\le 2H\,\|R(r\cdot)\|_2.
\]
Using the exact identity \(\|P+R\|_2^2=\|P\|_2^2+2\operatorname{Re}\langle P,R\rangle+\|R\|_2^2\), the remaining error is bounded by
\[
C_\alpha(|a|+H+(|a|+H)^2)H^2
+2\mu_1|a|^2H^2+H^4
=o_\alpha(|a|^4+H^2).
\]
This bound is uniform in the number and placement of Fourier modes, because it uses only \(H\). The leading form is comparable above and below, with positive \(\alpha\)-dependent constants, to \(|a|^4+H^2\); indeed, \(2-2^{2-n}\ge3/2\) for every \(n\ge3\), and \(\mu_2|b_2|^2\le2\mu_2|b_2-a^2/2|^2+(\mu_2/2)|a|^4\). Hence \(D_\alpha=Q_\alpha(1+o_\alpha(1))\), for the positive form \(Q_\alpha\) displayed in the finding.

**5. Sharpness and rigidity.** The positive leading form is at least \(|a|^4/[\alpha^2(\alpha+1)]\). Equality up to lower-order terms forces all its remaining nonnegative summands to be little-o of \(|a|^4\), precisely the two stated conditions on the higher coefficients. Conversely these conditions reduce the leading form to the single quartic term and make the remainder negligible. The quadratic-corrected polynomials attain the constant in the limit; direct substitution in the moment identity yields the affine comparison formula. This proves the exact coefficient, uniqueness of the nonlinear tangent correction, and all-mode rigidity.

## Verification

A standalone, standard-library Python checker is included as `checks/check.py`. It computes Bergman monomial moments, the fourth-power norm of a critically dilated square, the proposed leading form and the exact \(f^2=P+R\) remainder using rational arithmetic with real and imaginary components. The replay command is `python3 checks/check.py`; it passed 550 exact assertions for five rational weight parameters greater than one, complex polynomial modes and two perturbative scales. The proof above supplies the all-real-weight and infinite-dimensional arguments; finite tests do not certify them independently.

## Relationship to prior work

Melentijević, *Hypercontractive inequalities for weighted Bergman spaces* (first preprint 7 November 2022), establishes the sharp global \(L^p\)-to-\(L^q\) dilation contractivity used here. Its Theorem 1 proves the nonnegative deficit but does not state the sharp quartic stability normal form, optimal quadratic corrector, or all-mode rigidity. Bayart, Brevig, Haimi, Ortega-Cerdà and Perfekt (first preprint 24 January 2017) establish analogous sharp inequalities for certain weights and discuss the first-mode perturbation determining the critical dilation; these do not quantify the fourth-order flatness. Melentijević's 2025 stability work concerns convex functionals and *different-weight* Bergman inclusions, not this fixed-weight dilation deficit. Kalaj and Zhu's 2026 perturbative Bergman-ball work proves conditional, truncated level-set and different-weight comparison statements; it does not imply the present explicit fixed-weight fourth-order normal form.

The coefficient calculations use classical orthogonal monomial identities rather than claiming novelty for them. Searches and the inspected literature found no covering statement, but this does not establish absolute priority; an earlier direct perturbation in hypercontractivity or a general quantitative stability theorem might contain an equivalent form.

## Limitations

This is a **local** theorem near the constant extremizer for each fixed \(\alpha>1\) and only at \(p=2,q=4,r=1/\sqrt2\). It does not characterize all global extremizers, give a global quantitative stability estimate, establish uniform estimates as \(\alpha\to1\) or \(\alpha\to\infty\), or handle other exponent pairs. Historical-priority searches are inherently incomplete. The computation checker supplies supplementary exact finite evidence; there is no independent mathematical validation or certification.

## References

1. P. Melentijević, *Hypercontractive inequalities for weighted Bergman spaces*, arXiv:2211.03655 (first posted 2022-11-07); Bull. London Math. Soc. 55 (2023), 2611–2616. https://arxiv.org/abs/2211.03655
2. F. Bayart, O. F. Brevig, A. Haimi, J. Ortega-Cerdà, K.-M. Perfekt, *Contractive inequalities for Bergman spaces and multiplicative Hankel forms*, arXiv:1701.06897 (first posted 2017-01-24); Trans. Amer. Math. Soc. 371 (2019), 681–707. https://arxiv.org/abs/1701.06897
3. P. Melentijević, *Stability of convex functionals on weighted Bergman spaces with applications*, arXiv:2508.01939 (2025). https://arxiv.org/abs/2508.01939
4. D. Kalaj, J.-F. Zhu, *Contraction properties for holomorphic functions via isoperimetric stability on the Bergman ball*, arXiv:2603.22524 (2026). https://arxiv.org/abs/2603.22524
