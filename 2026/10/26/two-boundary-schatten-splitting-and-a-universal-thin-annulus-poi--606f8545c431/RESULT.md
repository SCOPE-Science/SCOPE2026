# Two-boundary Schatten splitting and a universal thin-annulus Poisson spectrum

## Finding

Fix \(\alpha>-1\). Consider harmonic extension from two circles bounding a thin planar annulus. With equal boundary-channel weights but with a volume weight vanishing (or diverging) only at the outer circle, the two high-frequency singular branches have **different polynomial orders**: \(\kappa^{-(\alpha+1)/2}\) and \(\kappa^{-1/2}\). Consequently there is a sharp Schatten transition at \(\alpha=0\). Moreover, after multiplying the Schatten sum by the logarithmic annulus thickness, a finite, explicit universal matrix-integral coefficient emerges. The complete statement and normalizations follow.

For \(0<\varepsilon<\infty\), put \(\Omega_\varepsilon=\{z\in\mathbb C:e^{-\varepsilon}<|z|<1\}\). Give both boundary circles their **normalized angular measures** and define
\[
 \mathcal H_\partial=L^2(\mathbb T,d\theta/(2\pi))\oplus L^2(\mathbb T,d\theta/(2\pi)),\qquad
 \|(f_o,f_i)\|_\partial^2=\tfrac12(\|f_o\|_2^2+\|f_i\|_2^2).
\]
On the annulus use the probability-normalized volume measure
\[
 d\mu_{\varepsilon,\alpha}(z)=
 \frac{(1-|z|^2)^\alpha\,dA(z)}{\int_{\Omega_\varepsilon}(1-|w|^2)^\alpha dA(w)}.
\]
Let \(P_{\varepsilon,\alpha}\) take a pair of \(L^2\) Dirichlet boundary traces to its harmonic extension in \(L^2(\Omega_\varepsilon,d\mu_{\varepsilon,\alpha})\).

For \(\kappa\ge0\) and \(0\le s\le1\) define
\[
 u_\kappa(s)=\frac{\sinh(\kappa(1-s))}{\sinh\kappa},\qquad
 v_\kappa(s)=\frac{\sinh(\kappa s)}{\sinh\kappa},
\]
with continuous values \(u_0(s)=1-s\), \(v_0(s)=s\). Define the positive definite, symmetric \(2\times2\) matrix
\[
 G_\alpha(\kappa)=2(\alpha+1)\int_0^1 s^\alpha
 \begin{pmatrix}u_\kappa(s)^2&u_\kappa(s)v_\kappa(s)\\
 u_\kappa(s)v_\kappa(s)&v_\kappa(s)^2\end{pmatrix}ds.
\]
For all \(p>\max\{2,2/(\alpha+1)\}\),
\[
 \boxed{\lim_{\varepsilon\downarrow0}\varepsilon
 \|P_{\varepsilon,\alpha}\|_{\mathcal S_p}^{p}
 =2\int_0^\infty\operatorname{tr}\bigl(G_\alpha(\kappa)^{p/2}\bigr)d\kappa
 \in(0,\infty).}
\]
For **every fixed** \(\varepsilon>0\), independently of the thin limit,
\[
 \boxed{P_{\varepsilon,\alpha}\in\mathcal S_p
 \quad\Longleftrightarrow\quad p>\max\{2,2/(\alpha+1)\}.}
\]
The two asymptotic squared-singular-value branches for angular order \(k\to\infty\), with \(\kappa=k\varepsilon\), are the two numbers, up to individual relative errors tending to zero,
\[
 \boxed{\frac{2^{-\alpha}\Gamma(\alpha+2)}{h_\varepsilon^{\alpha+1}}\,\kappa^{-(\alpha+1)}
 \quad\text{and}\quad
 \frac{(\alpha+1)e^{-2\varepsilon}}{h_\varepsilon}\,\kappa^{-1},
 \qquad h_\varepsilon=\frac{1-e^{-2\varepsilon}}{2\varepsilon}.}
\]
These correspond to the outer and inner Dirichlet circles respectively; ordering depends on \(\alpha\). Both \(k\) and \(-k\) occur and have the same two singular values. Uniformly for all \(k\ge0\), the squared singular values of \(P_{\varepsilon,\alpha}\) differ by a multiplicative \(1+O_\alpha(\varepsilon)\) from the eigenvalues of \(G_\alpha(k\varepsilon)\) as \(\varepsilon\downarrow0\).

## Assumptions and scope

The Laplacian is Euclidean in two real dimensions. The input measure is **not physical arclength**: it is equal normalized angular measure on each boundary component, with the overall factor \(1/2\) in the squared norm. This factor fixes all spectral constants. The range weight \((1-|z|^2)^\alpha\) is **one-sided**: it has a boundary power at the outer circle but remains strictly positive at the inner circle. The theorem covers all \(\alpha>-1\), all \(\varepsilon>0\) for Schatten membership and fixed-width high frequencies, and \(\varepsilon\downarrow0\) for the matrix profile and sharp finite-Schatten coefficient. No assertion is made for a weight defined using the distance to both boundary components.

## Proof

**1. Exact separation into two-dimensional Fourier fibers.** For boundary inputs with Fourier mode \(e^{ik\theta}\), let \(s=-\log r/\varepsilon\) and \(\kappa=|k|\varepsilon\). The unique harmonic extension is
\[
 e^{ik\theta}\bigl(a\,u_\kappa(s)+b\,v_\kappa(s)\bigr).
\]
Indeed the radial Laplace equation becomes a second-order constant-coefficient equation in \(s\), and the displayed hyperbolic-sine functions attain the prescribed data at \(s=0\) and \(s=1\). At \(k=0\), the solutions are affine in \(s\). Orthogonality of distinct angular Fourier modes under the radial measure makes the extension an orthogonal direct sum of these fibers.

The normalized radial density in the \(s\)-coordinate is exactly
\[
 w_{\varepsilon,\alpha}(s)=
 \frac{2\varepsilon(\alpha+1)e^{-2\varepsilon s}(1-e^{-2\varepsilon s})^\alpha}
 {(1-e^{-2\varepsilon})^{\alpha+1}},\qquad \int_0^1w_{\varepsilon,\alpha}(s)ds=1.
\]
Since the boundary coefficient norm is \((|a|^2+|b|^2)/2\), the fiber squared-singular-value matrix is
\[
 G_{\varepsilon,\alpha}(\kappa)=2\int_0^1 w_{\varepsilon,\alpha}(s)
 \begin{pmatrix}u_\kappa^2&u_\kappa v_\kappa\\u_\kappa v_\kappa&v_\kappa^2\end{pmatrix}ds.
\]
The two profile functions are linearly independent, so this matrix is positive definite at every finite \(\kappa\). This establishes the exact spectral decomposition; for \(k\ge1\) the matrices occur twice, at Fourier orders \(\pm k\).

**2. Uniform thin-annulus comparison.** Set \(h(t)=(1-e^{-t})/t\), with \(h(0)=1\). Algebra gives the exact ratio
\[
 \frac{w_{\varepsilon,\alpha}(s)}{(\alpha+1)s^\alpha}
 =\frac{e^{-2\varepsilon s}h(2\varepsilon s)^\alpha}
 {h(2\varepsilon)^{\alpha+1}}.
\]
For fixed \(\alpha>-1\), smoothness and positivity of \(h\) at the origin give \(1-C_\alpha\varepsilon\le w_{\varepsilon,\alpha}(s)/((\alpha+1)s^\alpha)\le1+C_\alpha\varepsilon\), **uniformly for** \(0<s\le1\) and all sufficiently small \(\varepsilon\). Integrating rank-one positive semidefinite matrices yields the Loewner inequalities
\[
 (1-C_\alpha\varepsilon)G_\alpha(\kappa)
 \preceq G_{\varepsilon,\alpha}(\kappa)
 \preceq(1+C_\alpha\varepsilon)G_\alpha(\kappa),
\]
for all \(\kappa\ge0\). Courant–Fischer supplies the asserted **uniform relative eigenvalue** estimates, even when a branch is exponentially or polynomially small.

**3. Exact high-frequency boundary-layer powers.** Uniformly for \(0\le s\le1\) and \(\kappa\ge1\),
\[
 u_\kappa(s)=e^{-\kappa s}\frac{1-e^{-2\kappa(1-s)}}{1-e^{-2\kappa}},\qquad
 v_\kappa(s)=e^{-\kappa(1-s)}\frac{1-e^{-2\kappa s}}{1-e^{-2\kappa}}.
\]
Near \(s=0\), \(w_{\varepsilon,\alpha}(s)\sim(\alpha+1)h_\varepsilon^{-(\alpha+1)}s^\alpha\); near \(s=1\), \(w_{\varepsilon,\alpha}(s)\to(\alpha+1)e^{-2\varepsilon}/h_\varepsilon\). The elementary Laplace integral \(\int_0^\infty s^\alpha e^{-2\kappa s}ds=\Gamma(\alpha+1)(2\kappa)^{-(\alpha+1)}\) proves the two stated diagonal constants. Since \(|u_\kappa(s)v_\kappa(s)|\le C e^{-\kappa}\) throughout the interval, the off-diagonal entry is \(O(e^{-\kappa})\), negligible relative to either diagonal entry. Therefore the two eigenvalues have precisely the two displayed asymptotic sizes. The endpoint \(\alpha=0\) has equal power orders but still exponentially negligible mixing.

**4. Sharp Schatten boundary and coefficient.** For each nonzero angular order there are two singular values, each asymptotic to the square root of its boundary-layer squared eigenvalue. Their positive \(p\)-powers are summable exactly if both
\[
 \frac{p(\alpha+1)}2>1\qquad\text{and}\qquad \frac p2>1.
\]
At either equality, the corresponding positive harmonic series diverges; the finite \(k=0\) sector does not change membership. This proves the if-and-only-if threshold without an appeal to a general compactness theorem.

Finally, for \(p\) strictly above the threshold, the continuous positive function \(F_\alpha(\kappa)=\operatorname{tr}(G_\alpha(\kappa)^{p/2})\) is bounded near \(\kappa=0\) and integrable at infinity by the same boundary-layer powers. The uniform relative comparison from Step 2 makes the true trace summand \(F_\alpha(k\varepsilon)(1+O_{\alpha,p}(\varepsilon))\) uniformly in \(k\). Because every nonzero positive angular order appears twice, the integrable Riemann-sum limit
\[
 \varepsilon\sum_{k\in\mathbb Z}F_\alpha(|k|\varepsilon)
 \longrightarrow2\int_0^\infty F_\alpha(\kappa)d\kappa
\]
proves the asserted universal coefficient and its strict positivity. All quantifiers are as stated: fixed weight exponent \(\alpha\), fixed admissible \(p\), and \(\varepsilon\downarrow0\).

## Verification

The accompanying standalone `verification/verify.py` independently integrates the exact Fourier Gram matrices with Jacobi quadrature. It verifies positivity, the unweighted exact eigenvalue formulas, the two distinct high-frequency constants, and finite instances of the uniform thin-collar comparison. The checker prints a finite assertion count; its finite checks are corroboration, not a replacement for the proof above. The exact \(\alpha=0\), \(\varepsilon=0\) eigenvalues additionally simplify to
\[
 \lambda_+(\kappa)=\frac{\kappa+\sinh\kappa}{\kappa(1+\cosh\kappa)},\quad
 \lambda_-(\kappa)=\frac{\sinh\kappa-\kappa}{\kappa(\cosh\kappa-1)},
\]
with limits \(1\) and \(1/3\), respectively, at the origin.

## Relationship to prior work

Auchmuty [1] establishes a general-domain singular-value decomposition of the unweighted Poisson extension via a biharmonic Steklov eigenproblem. Ureyen [2] develops weighted harmonic Bergman spaces on a real hyperbolic ball, focusing on atomic decomposition, interpolation, and inclusion. Rozenblum [3] studies boundary-supported Toeplitz forms **on weighted harmonic Sobolev spaces** using powers of distance to the entire boundary. None of these inspected results states the present one-sided-weight two-component high-frequency constants, global-in-mode thin-annulus relative matrix profile, or volume-normalized sharp limiting Schatten coefficient. Standard localized spectral theory may independently imply parts of the exponent threshold, so that power law alone is not offered as exclusive novelty. The joint quantitative thin-collar statement is the assessed contribution.

## Limitations

The operator acts on angularly normalized (not arclength-normalized) boundary \(L^2\) data. The weight has a power singularity at only the outer boundary, so the results do **not** transfer unchanged to symmetric boundary-distance weights. The singular-value asymptotics are for fixed width with high frequency, while the trace coefficient is a different joint high-frequency/thin-width limit. The theorem makes no claim about general annular geometries, nonradial coefficients, non-Euclidean harmonicity, or \(p\) at or below the Schatten threshold beyond nonmembership. Mathematical priority relative to nonindexed earlier annular Poisson literature remains to be independently checked.

## References

1. Giles Auchmuty, *The S.V.D. of the Poisson Kernel*, arXiv:1610.06836v1, first publicly posted 2016-10-21. https://arxiv.org/abs/1610.06836
2. A. Ersin Ureyen, *Harmonic Bergman Spaces on the Real Hyperbolic Ball: Atomic Decomposition, Interpolation and Inclusion Relations*, arXiv:2303.12137v1, first publicly posted 2023-03-21. https://arxiv.org/abs/2303.12137
3. Grigori Rozenblum, *Boundary Toeplitz type operators in weighted harmonic Sobolev spaces*, Boletín de la Sociedad Matemática Mexicana **31** (2025), article 97. https://doi.org/10.1007/s40590-025-00793-x
