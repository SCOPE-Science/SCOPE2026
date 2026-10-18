# A theta-function spectral-edge transition for monomial Dirichlet composition–differentiation operators

## Finding

For every fixed real \(0<\alpha<1\), integers \(k\ge2\) and \(m\ge0\), consider the weighted Dirichlet Hilbert space
\[
\mathcal D_\alpha=\left\{f(z)=\sum_{j\ge0}a_jz^j:\ \|f\|_\alpha^2=\sum_{j\ge0}(j+1)^{1-\alpha}|a_j|^2<\infty\right\}
\]
and the compact composition–differentiation operator
\[
T_hf(z)=z^m f^{(k)}(e^{-h}z),\qquad h>0.
\]
Put \(\beta=(1-\alpha)/2\), and for \(x\ge k\) define
\[
g_h(x)=\sum_{i=0}^{k-1}\log(x-i)-h(x-k)
+\beta\log\frac{x-k+m+1}{x+1}.
\]
For sufficiently small \(h>0\) the function \(g_h\) has a unique continuous maximizer \(x_h>k\). Set \(M_h=\exp(g_h(x_h))\) and \(\vartheta_h=x_h-\lfloor x_h\rfloor\). The location and height satisfy
\[
x_h=\frac{k}{h}+\frac{k-1}{2}+\frac{\beta(k-m)}{k}+O(h),
\qquad h^kM_h\longrightarrow\left(\frac{k}{e}\right)^k.
\]

**Critical high-Schatten lattice law.** For every function \(p_h>0\) satisfying \(p_hh^2\to\tau\in(0,\infty)\),
\[
\boxed{\quad M_h^{-p_h}\|T_h\|_{\mathcal S_{p_h}}^{p_h}
=\Theta_{k,\tau}(\vartheta_h)+o(1),\qquad
\Theta_{k,\tau}(\vartheta)
=\sum_{\ell\in\mathbb Z}\exp\!\left(-\frac{\tau(\ell-\vartheta)^2}{2k}\right).\quad}
\]
The error is valid without fixing a fractional-part subsequence. In particular, for the natural choice \(p_h=\tau/h^2\), the normalized Schatten-power sum does **not** converge as \(h\downarrow0\): along explicit parameter sequences it approaches both distinct values \(\Theta_{k,\tau}(0)\) and \(\Theta_{k,\tau}(1/2)\). The shift of the moving lattice center depends explicitly on the Dirichlet exponent \(\alpha\) and the multiplier degree \(m\), even though the limiting Gaussian curvature does not.

**Diffuse edge regime.** If \(p_h\to\infty\) while \(p_hh^2\to0\), then
\[
\boxed{\quad M_h^{-p_h}\|T_h\|_{\mathcal S_{p_h}}^{p_h}
\sim \sqrt{\frac{2\pi k}{p_hh^2}}.\quad}
\]
Thus \(p_h\asymp h^{-2}\) is exactly the crossover between an increasingly broad Gaussian packet of singular values near the operator norm and the discrete theta-function edge. These assertions concern the Schatten **power sum** normalized by a smooth spectral envelope; they do not identify an independent audit or any global theorem about arbitrary composition operators.

## Assumptions and scope

The coefficient Hilbert norm above, rather than an unnormalized area-integral convention, fixes all constants. The differentiating order \(k\), multiplier degree \(m\), and exponent \(\alpha\) are fixed while \(h\downarrow0\). Real \(p_h>0\) is permitted, including the Schatten quasi-norm range below one, although in the two asymptotic regimes \(p_h\to\infty\). The two regimes do not cover \(p_hh^2\to\infty\). The parameter \(M_h\) is the maximum of a continuous extension of the singular-weight logarithms; it is not asserted to equal the discrete operator norm at every \(h\).

The source family is a special case of the generalized weighted composition–differentiation operators considered in the 2026 weighted Dirichlet study [1]. The original arXiv source appeared on April 30, 2026; its later version, publicly available October 7, 2026, includes the displayed weighted formulation. Only the earliest public date is used for eligibility.

## Proof

**Step 1: exact singular representation.** The normalized monomials \(e_j(z)=z^j/(j+1)^\beta\) form an orthonormal basis. For every integer \(j\ge k\),
\[
T_he_j=w_{j,h}e_{j-k+m},\qquad
w_{j,h}=\frac{j!}{(j-k)!}e^{-h(j-k)}
\left(\frac{j-k+m+1}{j+1}\right)^\beta.
\]
The vectors \(e_{j-k+m}\) are mutually orthogonal, while \(e_0,\ldots,e_{k-1}\) lie in the kernel. Therefore \(T_h^*T_h\) is diagonal with entries \(w_{j,h}^2\) for \(j\ge k\), together with \(k\) zero entries. In particular, all nonzero singular values (including multiplicity) are the numbers \(w_{j,h}=e^{g_h(j)}\). As \(j\to\infty\) with \(h\) fixed, \(w_{j,h}=O(j^ke^{-hj})\), so \(T_h\) is compact and belongs to every positive Schatten class, with the exact identity
\[
\|T_h\|_{\mathcal S_p}^p=\sum_{j=k}^\infty e^{p g_h(j)}\qquad(p>0).
\]
The orthogonality, not a finite truncation, proves this infinite singular spectrum.

**Step 2: a unique smooth spectral edge.** For \(x\ge k\), differentiation gives
\[
g_h'(x)=\sum_{i=0}^{k-1}\frac{1}{x-i}-h
+\beta\left(\frac{1}{x-k+m+1}-\frac{1}{x+1}\right),
\]
\[
g_h''(x)=-\sum_{i=0}^{k-1}\frac{1}{(x-i)^2}
+\beta\left(\frac{1}{(x+1)^2}-\frac{1}{(x-k+m+1)^2}\right)
< -\frac1{x^2}+\frac\beta{(x+1)^2}<0.
\]
The inequality uses \(0<\beta<1/2\). For sufficiently small \(h\), \(g_h'(k)>0\), whereas \(g_h'(x)\to-h\) as \(x\to\infty\). Hence a unique \(x_h>k\) solves \(g_h'(x_h)=0\) and maximizes \(g_h\).

Uniform large-\(x\) expansions yield
\[
g_h'(x)=\frac{k}{x}-h
+\frac{\frac{k(k-1)}2+\beta(k-m)}{x^2}+O(x^{-3}).
\]
Solving this equation asymptotically gives
\[
x_h=\frac{k}{h}+c_{k,m,\alpha}+O(h),\qquad
c_{k,m,\alpha}=\frac{k-1}{2}+\frac{\beta(k-m)}{k}.
\]
Furthermore
\[
g_h''(x_h)=-\frac{h^2}{k}+O(h^3),
\qquad
h^k e^{g_h(x_h)}\to(k/e)^k.
\]
All remainders in this step depend only on the fixed parameters.

**Step 3: the critical discrete-Gaussian limit.** Write \(p=p_h\), assume \(ph^2\to\tau>0\), and put \(x_h=N_h+\vartheta_h\) with \(N_h=\lfloor x_h\rfloor\). For any fixed integer \(\ell\), Taylor's theorem and the preceding curvature expansion imply, uniformly in the bounded offset \(\ell-\vartheta_h\),
\[
p\bigl(g_h(N_h+\ell)-g_h(x_h)\bigr)
=-\frac{\tau(\ell-\vartheta_h)^2}{2k}+o(1).
\]
This convergence may be summed. To justify the interchange rigorously, fix a small \(\eta>0\). On \(|x-x_h|\le\eta/h\), the explicit formula for the second derivative implies \(g_h''(x)\le-c h^2\), with \(c>0\) independent of small \(h\); since the first derivative vanishes at the center,
\[
p(g_h(j)-g_h(x_h))\le-c' (j-x_h)^2
\]
for sufficiently small \(h\) and \(|j-x_h|\le\eta/h\). For \(|j-x_h|>\eta/h\), strict concavity gives an initial deficit at least a fixed negative constant and a one-sided slope of order \(h\); the resulting tails form dominated geometric series after exponentiation by \(p\asymp h^{-2}\). Equivalently, the asymptotic profile \(g_h(x)-g_h(x_h)\to k\log(y/k)-(y-k)\) for \(y=hx\) on compact positive intervals isolates the unique macroscopic maximum, while the exponential term controls arbitrarily large \(y\). These estimates justify uniform truncation in \(\ell\), followed by the finite-offset Taylor limit. Therefore
\[
\sum_{j\ge k}e^{p(g_h(j)-g_h(x_h))}
=\sum_{\ell\in\mathbb Z}e^{-\tau(\ell-\vartheta_h)^2/(2k)}+o(1),
\]
which proves the central formula without an assumption that \(\vartheta_h\) itself converges.

**Step 4: two genuinely different phase limits.** Fix \(\vartheta\in[0,1)\). For each large integer \(N\), choose
\[
h_{N,\vartheta}
=\sum_{i=0}^{k-1}\frac1{N+\vartheta-i}
+\beta\left(\frac1{N+\vartheta-k+m+1}-\frac1{N+\vartheta+1}\right)>0.
\]
The strict-concavity equation makes the maximizer exactly \(x_{h_{N,\vartheta}}=N+\vartheta\), and \(h_{N,\vartheta}\to0\). With \(p_h=\tau/h^2\), the normalized mass converges to \(\Theta_{k,\tau}(\vartheta)\). Poisson summation for the classical Gaussian gives
\[
\Theta_{k,\tau}(\vartheta)=\sqrt{\frac{2\pi k}{\tau}}
\sum_{r\in\mathbb Z}e^{-2\pi^2kr^2/\tau}e^{2\pi i r\vartheta}.
\]
Consequently
\[
\Theta_{k,\tau}(0)-\Theta_{k,\tau}(1/2)
=2\sqrt{\frac{2\pi k}{\tau}}
\sum_{r\in\mathbb Z:\ r\ \mathrm{odd}}e^{-2\pi^2kr^2/\tau}>0.
\]
The two different phase limits prove genuine nonconvergence at the critical scale.

**Step 5: the diffuse regime.** Assume \(p\to\infty\), \(ph^2\to0\), and put \(\sigma_h=(h\sqrt p)^{-1}\to\infty\). For any fixed real \(u\), Taylor expansion on the window \(x=x_h+\sigma_hu\), using \(g_h''(x_h)=-h^2/k+O(h^3)\) and \(g_h'''(x)=O(h^3)\) on \(x\asymp h^{-1}\), gives
\[
p(g_h(x_h+\sigma_hu)-g_h(x_h))
=-\frac{u^2}{2k}+o(1).
\]
Indeed, the scaled cubic remainder is \(O(p^{-1/2})\) and the curvature error is \(O(h)\). The inner-window quadratic upper bound from Step 3 supplies an integrable Gaussian majorant, while the macroscopic exterior loses a fixed fraction of the maximum and is negligible because \(p\to\infty\). The lattice spacing in \(u\) is \(\sigma_h^{-1}\to0\); its Riemann sums converge to \(\int_{\mathbb R}e^{-u^2/(2k)}\,du=\sqrt{2\pi k}\). Thus the Schatten power sum is asymptotic to \(\sigma_h\sqrt{2\pi k}\), as claimed.

## Verification

The accompanying standalone `checker.py` directly evaluates the exact infinite-dimensional singular-weight formula on controlled finite index windows. It tests the predicted phase-dependent theta factors for distinct differentiation orders, monomial multipliers and Dirichlet exponents; it also tests the diffuse Gaussian scaling and strict separation between integer and half-integer phases. Running `python checker.py` produces `PASS 38 finite numerical diagnostics; theorem proved separately`. These tests are not an exhaustive proof; every limiting interchange and every spectral identity is justified analytically above.

## Relationship to prior work

Barik, Sen and Paul [1] establish boundedness, compactness, Hilbert–Schmidt criteria and norm information for generalized weighted composition–differentiation operators on weighted Dirichlet spaces. Their source supplies the motivating operator family but does not state a variable-order Schatten asymptotic at \(p_h\asymp h^{-2}\), a Jacobi-theta edge law, or the explicit monomial-dependent phase shift. Allen, Heller and Pons [2] analyze first-order composition–differentiation on the classical Dirichlet space and obtain norm and spectrum formulas for particular monomial symbols, not the present varying-exponent edge. The Gaussian Poisson formula [3] is classical and is used as a tool, not claimed as new. Earlier fixed-exponent singular-value asymptotics for differences of Dirichlet composition–differentiation operators concern different operators and a different asymptotic regime, and do not imply this discrete high-order edge law.

## Limitations

The high-Schatten phase transition is proved for the explicit monomial multiplier and strict radial dilation, not arbitrary analytic inducing maps. The classical Jacobi-theta mechanism itself is not new. The theorem does not classify the regime \(p_hh^2\to\infty\), and it does not assert uniformity when \(\alpha\), \(k\), or \(m\) vary with \(h\). The displayed nonconvergence concerns normalized Schatten power sums, not the Schatten norm or the usual operator norm individually. Existing general discrete Laplace asymptotics may offer an alternative derivation; independent priority assessment remains necessary.

## References

[1] S. Barik, A. Sen and K. Paul, *Weighted composition-differentiation operators on weighted Dirichlet spaces*, arXiv:2605.00213, first public version 2026-04-30; revised PDF arXiv:2605.00213v2 (2026-10-07), https://arxiv.org/abs/2605.00213.

[2] R. F. Allen, K. C. Heller and M. A. Pons, *Composition-differentiation operators on the Dirichlet space*, arXiv:2207.09015v2 (2022), https://arxiv.org/abs/2207.09015.

[3] NIST Digital Library of Mathematical Functions, §20.7(viii), theta-function transformations of the lattice parameter, https://dlmf.nist.gov/20.7.viii (classical Poisson/Jacobi identity used in Step 4).
