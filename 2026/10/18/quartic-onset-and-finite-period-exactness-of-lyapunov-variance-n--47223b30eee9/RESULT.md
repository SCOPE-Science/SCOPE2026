# Quartic onset and finite-period exactness of Lyapunov variance near doubling

## Finding
Let \(\mathbb T=\mathbb R/\mathbb Z\), and for real \(\varepsilon\) with \(|\varepsilon|<1/(16\pi)\) define the orientation-preserving, degree-two expanding map
\[
f_\varepsilon(x)=2x+\varepsilon\bigl(\sin(4\pi x)-2\sin(2\pi x)\bigr)\pmod1.
\]
For each integer \(n\ge1\), give the \(2^n-1\) points of \(\operatorname{Fix}(f_\varepsilon^n)\) equal weights. Let \(V_n(\varepsilon)\) be the population variance of their normalized logarithmic multipliers
\[
\chi_{n,\varepsilon}(p)=\frac1n\log\bigl((f_\varepsilon^n)'(p)\bigr).
\]
Then, for **every fixed integer \(n\ge5\)**,
\[
\boxed{V_n(\varepsilon)=\frac{36\pi^4}{n}\varepsilon^4+O_n(|\varepsilon|^5)\quad(\varepsilon\to0).}
\]
Moreover the asymptotic periodic-orbit variance \(\sigma_\varepsilon^2=\lim_{n\to\infty}nV_n(\varepsilon)\) exists, and
\[
\boxed{\sigma_\varepsilon^2=36\pi^4\varepsilon^4+o(\varepsilon^4)\quad(\varepsilon\to0).}
\]
In particular the standard deviation in the periodic-multiplier central limit theorem is \(\sigma_\varepsilon=6\pi^2\varepsilon^2+o(\varepsilon^2)\); the fluctuations turn on **quartically in variance**, not quadratically. The same leading constant occurs in the scaled population variance of every fixed period at least five.

## Assumptions and scope
The expansion bound \(f_\varepsilon'(x)\ge2-8\pi|\varepsilon|>3/2\) ensures a uniformly expanding circle covering. Its fixed-point set counts points whose least period divides \(n\), not only primitive cycles. Variance is with respect to the uniform distribution on that finite set, not with respect to Lebesgue measure. The limit \(\varepsilon\to0\) with \(n\) fixed in the first formula is distinct from the limit \(n\to\infty\) at fixed \(\varepsilon\) defining the second. The constants implicit in \(O_n\) can depend on \(n\), and no estimate uniform in both parameters is claimed. The infinite-period limit corresponds to the maximal-entropy invariant probability measure, not the absolutely continuous invariant measure.

## Proof
**1. Tangent to the conjugacy orbit.** Put \(q(x)=\sin(2\pi x)\), \(T(x)=2x\pmod1\), and \(u(x)=q(Tx)-2q(x)\). The diffeomorphism \(H_\varepsilon(x)=x+\varepsilon q(x)\pmod1\) is orientation-preserving for the indicated parameter range. Write \(g_\varepsilon=H_\varepsilon^{-1}\circ f_\varepsilon\circ H_\varepsilon\). Taylor expansion of the lifts, uniformly in every fixed \(C^r\) norm, gives
\[
\begin{split}
f_\varepsilon(H_\varepsilon x)&=2x+\varepsilon q(2x)+\varepsilon^2q(x)u'(x)+O(\varepsilon^3),\\
g_\varepsilon(x)&=2x+\varepsilon^2v(x)+O(\varepsilon^3),\\
v(x)&=q(x)u'(x)=2\pi\bigl(\sin(6\pi x)-\sin(2\pi x)-\sin(4\pi x)\bigr).
\end{split}
\]
Consequently
\[
\log g_\varepsilon'(x)=\log2+\varepsilon^2B(x)+O_{C^1}(\varepsilon^3),
\quad B(x)=2\pi^2\bigl(3\cos(6\pi x)-\cos(2\pi x)-2\cos(4\pi x)\bigr).
\]
The derivative of \(H_\varepsilon\) telescopes around every periodic orbit, so the periodic multipliers of \(g_\varepsilon\) and \(f_\varepsilon\) agree exactly.

**2. Uniform fixed-period perturbation.** For \(n\ge1\), let \(M=2^n-1\). The \(M\) periodic points of \(T\) are \(x_k=k/M\), \(0\le k<M\). By uniform expansion and the implicit function theorem, for fixed \(n\) they continue to periodic points of \(g_\varepsilon\) displaced by \(O_n(\varepsilon^2)\). Thus, for the corresponding exponents,
\[
\chi_{n,\varepsilon}(k)=\log2+\varepsilon^2B_n(x_k)+O_n(\varepsilon^3),
\quad B_n(x)=\frac1n\sum_{j=0}^{n-1}B(T^jx).
\]
Define \(S_m(k)=\sum_{j=0}^{n-1}\cos(2\pi m2^jk/M)\). Since \(2^n\equiv1\pmod M\), one has \(S_2=S_1\) identically and therefore
\[
B_n(x_k)=\frac{6\pi^2}{n}\bigl(S_3(k)-S_1(k)\bigr).
\]

**3. Exact all-period character orthogonality.** For \(n\ge5\), the \(2n\) residue classes \(\{\pm2^j:0\le j<n\}\) are distinct modulo \(M\), as are \(\{\pm3\cdot2^j:0\le j<n\}\), and the two families are disjoint. To check this, divide any putative collision by the invertible factor \(2^j\) modulo the odd number \(M\). Collisions within the first family would require \(2^k\equiv\pm1\pmod M\) for \(1\le k<n\), excluded by \(1<2^k\le2^{n-1}<M-1\). Cross-family collisions would require \(3\cdot2^k\equiv\pm1\pmod M\); for \(k\le n-2\) the integer lies strictly between \(1\) and \(M-1\), and for \(k=n-1\) strictly between \(M+1\) and \(2M-1\). Finally, within the second family a nontrivial collision would require \(M\mid3(2^k\pm1)\). For \(1\le k\le n-2\), one has \(0<3(2^k\pm1)<M\); for \(k=n-1\), both quantities lie strictly between \(M\) and \(2M\). The inequalities use \(n\ge5\). Thus all stated residue classes are distinct and nonzero.

Orthogonality of characters of the finite cyclic group \(\mathbb Z/M\mathbb Z\) now yields, with \(\mathbb E_M\) denoting the average over \(k\),
\[
\mathbb E_M S_1=\mathbb E_M S_3=0,\qquad
\mathbb E_M S_1^2=\mathbb E_M S_3^2=n/2,\qquad
\mathbb E_M(S_1S_3)=0.
\]
It follows that \(\operatorname{Var}_M(B_n)=36\pi^4/n\). Squaring the \(O_n(\varepsilon^3)\) remainder in Step 2 against the \(O(\varepsilon^2)\) leading fluctuations gives \(V_n(\varepsilon)=\varepsilon^4\operatorname{Var}_M(B_n)+O_n(|\varepsilon|^5)\), proving the first box. In particular \(V_5(\varepsilon)>0\) for all sufficiently small nonzero \(\varepsilon\), and the perturbed map cannot be smoothly conjugate to \(T\): a smooth conjugacy would make every periodic multiplier equal to \(2^n\).

**4. Uniform Green--Kubo limit.** Let \(\mu_\varepsilon\) be the unique maximal-entropy invariant measure for \(g_\varepsilon\); \(\mu_0\) is Lebesgue measure. The normalized unweighted inverse-branch transfer operator
\[
(\mathcal L_\varepsilon\varphi)(x)=\tfrac12\sum_{g_\varepsilon y=x}\varphi(y)
\]
preserves constants. For every \(j\ge1\) and continuously differentiable \(\varphi\), the inverse-branch derivative formula and \(\inf g_\varepsilon'>7/6\) imply
\[
\| (\mathcal L_\varepsilon^j\varphi)'\|_\infty\le(6/7)^j\|\varphi'\|_\infty.
\]
Invariance of \(\mu_\varepsilon\) then bounds the centered sup norm by the same right-hand side. Indeed \(g_\varepsilon'=f_\varepsilon'(H_\varepsilon x)H_\varepsilon'(x)/H_\varepsilon'(g_\varepsilon x)\), and \(H_\varepsilon'\in(7/8,9/8)\), giving \(\inf g_\varepsilon'>(3/2)(7/9)=7/6\). The measures \(\mu_\varepsilon\) converge weakly to \(\mu_0\), since any subsequential limit is stationary for \(\mathcal L_0\) and its invariant probability is unique. These observations give a uniformly summable correlation bound for \(C^1\) observables.

Let \(h_\varepsilon=\log g_\varepsilon'\) and \(\widehat h_\varepsilon=h_\varepsilon-\int h_\varepsilon\,d\mu_\varepsilon\). Step 1 and convergence of the measures imply \(\varepsilon^{-2}\widehat h_\varepsilon\to B\) in \(C^1\), because \(\int B\,d\mu_0=0\). Therefore dominated convergence applies to the Green--Kubo series
\[
\sigma_\varepsilon^2=\int\widehat h_\varepsilon^2\,d\mu_\varepsilon
+2\sum_{j\ge1}\int\widehat h_\varepsilon(\widehat h_\varepsilon\circ g_\varepsilon^j)\,d\mu_\varepsilon.
\]
The periodic-point variance limit and its equality with this series follow from the expanding-map periodic-orbit variance theorem of Drach--Fu--Kaloshin--Li--Liverani [1, Section 4], applicable at every sufficiently small nonzero \(\varepsilon\) by Step 3. At \(\varepsilon=0\) all multipliers are exactly constant. At any other parameter in the stated expansion range, either the map is smoothly conjugate to the linear doubling map (and all periodic variances are identically zero), or the cited expanding-map theorem gives the existence of the same limit and its Green--Kubo representation.

Write \(C_m(x)=\cos(2\pi mx)\). The limiting observable is \(B=2\pi^2(-C_1-2C_2+3C_3)\). Fourier orthogonality under Lebesgue measure gives
\[
\int B^2\,dx=28\pi^4,\qquad
\int B(x)B(Tx)\,dx=4\pi^4,\qquad
\int B(x)B(T^jx)\,dx=0\quad(j\ge2).
\]
Hence the Green--Kubo limit divided by \(\varepsilon^4\) tends to \(28\pi^4+2(4\pi^4)=36\pi^4\). Its strict positivity yields the displayed standard-deviation asymptotic.

## Verification
The standalone standard-library script `CHECK.py` uses exact rational Fourier-character accounting for every period \(5\le n\le20\), checks exceptional shorter periods, and independently solves the nonlinear periodic-point equations at periods \(5,6,7,8\) for a small perturbation. Run `python3 CHECK.py`; expected terminal line begins `CHECK_OK`. The exact all-period character lemma, the limit and its error orders are analytical assertions proved above, not deductions from finite numerical checks.

## Relationship to prior work
Drach, Fu, Kaloshin, Li and Liverani [1] establish Gaussian periodic-multiplier statistics and the Green--Kubo identification of the asymptotic variance for general expanding circle maps. They do not state an explicit small-parameter, order-four coefficient for this two-harmonic family, nor the matching leading constants at every fixed period at least five. Shub and Sullivan [2] prove smooth rigidity related to periodic multipliers but do not estimate periodic-multiplier variance. Previous work on random switching of integer expanding maps [3] obtains an exact **first-order-in-switching-probability** variance for a deterministic coboundary; its noise model and observable are different from the smooth deterministic deformation here. A sharp pair-correlation variance computation for integer beta maps [4] concerns shrinking target collisions, not logarithmic derivative multipliers. The new calculation is the explicit quartic cancellation and finite-period resonance threshold, not the general central limit or rigidity principles.

## Limitations
The theorem treats one specified smooth two-harmonic family close to the doubling map and the maximal-entropy distribution. It does not give a universal quartic coefficient for arbitrary perturbations, an error bound uniform in both period and parameter, or an exact finite-parameter variance. The expansion for each fixed period begins with the common constant only from period five; lower-period collisions differ. Although targeted comparisons found no covering statement, an unindexed perturbative Fourier or cohomological calculation could conceivably imply the same formula.

## References
1. K. Drach, Z. Fu, V. Kaloshin, Z. Li and C. Liverani, *Normal distribution of Lyapunov exponents of periodic orbits for expanding circle maps*, arXiv:2511.15662v1 (first public submission 19 November 2025), particularly Sections 1 and 4. https://arxiv.org/abs/2511.15662
2. M. Shub and D. Sullivan, *Expanding endomorphisms of the circle revisited*, Ergodic Theory and Dynamical Systems **5** (1985), 285--289. https://doi.org/10.1017/S014338570000290X
3. *Distinct integer beta maps eliminate zero variance and give an exact noise-onset coefficient*, publicly available mathematical research record, 11 October 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-distinct-integer-beta-maps-eliminate-zero-variance-and-give-an-e--c097279b5a2a
4. *Sharp second-moment inflation for expanding circle-map pair correlations*, publicly available mathematical research record, 11 October 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-second-moment-inflation-for-expanding-circle-map-pair-corr--d5c688b954c6
