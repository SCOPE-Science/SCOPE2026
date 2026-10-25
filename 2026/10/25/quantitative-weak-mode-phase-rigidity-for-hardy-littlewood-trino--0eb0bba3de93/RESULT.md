# Quantitative weak-mode phase rigidity for Hardy–Littlewood trinomials

## Finding
For every integer \(k\ge2\), every exponent \(2k<p<2k+2\), and \(N=k+2\), define the normalized moment
\[
M_{k,p}(\rho,\phi)=\frac1{2\pi}\int_0^{2\pi}
\left|1+e^{it}+\rho e^{i\phi}e^{iNt}\right|^p\,dt,
\qquad\rho\ge0,\quad\phi\in\mathbb R.
\]
Write \(a=p/2>2\) and
\[
c_{k,p}=\frac{\Gamma(p)}{\Gamma(a+N)\Gamma(a-N+1)}<0,
\qquad
r_{k,p}=\min\left\{1,\frac{p|c_{k,p}|}{18\pi a(a-1)9^{a-2}}\right\}.
\]
Then **for every** \(0<\rho<r_{k,p}\), the complete coefficient-phase response is strictly increasing on \((0,\pi)\) and strictly decreasing on \((\pi,2\pi)\). In particular, the **unique** minimizing coefficient phase is \(\phi=0\), and the **unique** maximizing phase is \(\phi=\pi\), modulo full turns. More precisely, for \(0\le\phi\le\pi\),
\[
\begin{aligned}
&p|c_{k,p}|\rho\left(1-\frac\rho{r_{k,p}}\right)(1-\cos\phi)
\\&\hspace{4em}\le M_{k,p}(\rho,\phi)-M_{k,p}(\rho,0)
\\&\hspace{4em}\le p|c_{k,p}|\rho\left(1+\frac\rho{r_{k,p}}\right)(1-\cos\phi).
\end{aligned}
\]
The coefficient is the **exact first-order phase-response constant**:
\[
\lim_{\rho\downarrow0}\frac{M_{k,p}(\rho,\pi)-M_{k,p}(\rho,0)}\rho
=2p|c_{k,p}|.
\]
For fixed \(0<\alpha<1\), setting \(p=2k+2\alpha\) yields the explicit high-degree law
\[
2p|c_{k,p}|\sim\frac{2(2k)^{\alpha-1}}{|\Gamma(\alpha-1)|}
\qquad(k\to\infty).
\]
Thus the infinitesimal sign-reversal effect has a polynomially decaying, rather than exponentially decaying, phase contrast in the growing-degree family.

## Assumptions and scope
The domain is the circle with probability Lebesgue measure. The first two Fourier coefficients are fixed exactly at \(1\), the highest coefficient has prescribed modulus \(\rho\), and only its phase varies. The integer degree and open exponent restrictions are essential for the stated explicit radius: \(k\ge2\), \(N=k+2\), \(2k<p<2k+2\), whence \(a>2\). The radius is a **proved sufficient threshold**, not claimed optimal; the inequalities are not asserted for arbitrary \(\rho\). The coefficient \(c_{k,p}\) is real and negative because \(a-N+1\in(-1,0)\).

## Proof
Set \(z=e^{it}\), \(B=1+z\), and \(W=z^N\overline B\), so \(|B|\le2\) and \(|W|\le2\). Write
\[
A=|B|^2,\quad u(\phi,t)=\operatorname{Re}(e^{i\phi}W),
\quad Q(\rho,\phi,t)=A+\rho^2+2\rho u.
\]
Then \(Q=|B+\rho e^{i\phi}z^N|^2\ge0\), \(|u|,|u_\phi|\le2\), \(u_{\phi\phi}=-u\), and \(0\le Q,A\le9\) for \(0\le\rho\le1\). Since \(a>2\), twice differentiating \(Q^a\) in \(\phi\) is valid even at its zeros. It gives
\[
M_{\phi\phi}=-2a\rho\int Q^{a-1}u\,dm
+4a(a-1)\rho^2\int Q^{a-2}(u_\phi)^2\,dm,
\tag{1}
\]
where \(dm=dt/(2\pi)\).

The first-order coefficient is
\[
\int A^{a-1}u\,dm=c_{k,p}\cos\phi.
\tag{2}
\]
Indeed, \(B=2e^{it/2}\cos(t/2)\) for \(-\pi<t<\pi\). Thus \(\int W|B|^{p-2}dm\) is the cosine Fourier integral
\[
\frac1{2\pi}\int_{-\pi}^{\pi}
(2\cos(t/2))^{p-1}\cos((N-\tfrac12)t)\,dt,
\]
which evaluates, by the classical beta integral for cosine powers, to
\[
\frac{\Gamma(p)}{\Gamma(a+N)\Gamma(a-N+1)}.
\]
This proves (2) including its sign; it is not an appeal to numerical quadrature.

For \(0\le\rho\le1\), the bounds \(|Q-A|\le5\rho\) and
\[
|Q^{a-1}-A^{a-1}|\le5(a-1)9^{a-2}\rho
\]
follow by the mean-value theorem. Subtracting the first-order term in (1), the first integral costs at most \(20a(a-1)9^{a-2}\rho^2\) and the second at most \(16a(a-1)9^{a-2}\rho^2\). Therefore
\[
\left|M_{\phi\phi}+p\rho c_{k,p}\cos\phi\right|
\le36a(a-1)9^{a-2}\rho^2=K_p\rho^2.
\tag{3}
\]
The phase moment is even and full-turn-periodic, by complex conjugation and \(t\mapsto-t\); consequently \(M_\phi(\rho,0)=M_\phi(\rho,\pi)=0\). Integrating (3) from the *nearer* of these endpoints gives
\[
\left|M_\phi+p\rho c_{k,p}\sin\phi\right|
\le K_p\rho^2\min\{\phi,\pi-\phi\}
\le\frac{\pi K_p}{2}\rho^2\sin\phi
\tag{4}
\]
for \(0\le\phi\le\pi\). Here \(\sin\phi\ge(2/\pi)\min\{\phi,\pi-\phi\}\). By the explicit definition of \(r_{k,p}\), inequality (4) yields
\[
p|c_{k,p}|\rho(1-\rho/r_{k,p})\sin\phi
\le M_\phi\le
p|c_{k,p}|\rho(1+\rho/r_{k,p})\sin\phi.
\tag{5}
\]
For \(0<\rho<r_{k,p}\), the lower bound is strictly positive when \(0<\phi<\pi\); phase symmetry gives the reverse monotonicity on the complementary half-circle. Integration of (5) from \(0\) to \(\phi\) proves the displayed quantitative phase gap. Expanding the two-sided bound as \(\rho\downarrow0\) and evaluating at \(\phi=\pi\) proves the exact linear contrast.

Finally, for \(p=2k+2\alpha\),
\[
c_{k,p}=\frac{\Gamma(2k+2\alpha)}
{\Gamma(2k+\alpha+2)\Gamma(\alpha-1)}.
\]
The standard gamma-ratio asymptotic yields \(c_{k,p}\sim (2k)^{\alpha-2}/\Gamma(\alpha-1)\). As \(p/(2k)\to1\), multiplication by \(2p\) yields the displayed power-law contrast. This is an asymptotic for the first-order coefficient, **not** a claim uniform in positive \(\rho\) as \(k\to\infty\).

## Verification
The standalone `verify_weak_mode.py` independently checks the beta/gamma coefficient against direct cosine integration for four degrees, checks coefficient negativity and the derived radius, samples the phase response at 32 phase steps, and compares four small-amplitude sign contrasts. Its verified terminal output is `VERIFY_OK gamma_integrals=4 phase_grid=32 linear_slopes=4 radius_bounds=4`. Higher-degree phase samples use a numerically resolvable amplitude that need not lie below the certified radius; these are illustrative checks, not a proof of a stronger radius. Exact inequalities (1)--(5), not numerical sampling, establish the general theorem.

## Relationship to prior work
Pan, You, Wang, Zhou and Chen proved the fixed unit-amplitude comparison \(M_{k,p}(1,\pi)>M_{k,p}(1,0)\) for every degree and exponent interval, not the complete phase response at small prescribed amplitude. Krenedits proved small-degree unit-amplitude cases and records the older Boas construction with **both** nonconstant coefficients small, \(1+re^{it}\pm r^{k+2}e^{i(k+2)t}\). That construction is not the balanced-two-mode limit \(1+e^{it}+\rho e^{i\phi}e^{i(k+2)t}\) with \(\rho\downarrow0\) and does not imply this explicit all-phase bound. A published high-order phase-rigidity result proves continuous phase monotonicity for \(\rho=1\) and \(k\ge23\); its quantified domain fixes a different coefficient magnitude and does not imply the present \(\rho\)-neighborhood for all \(k\ge2\). The exact gamma/Fourier coefficient identity is classical; the contribution here is the explicit uniform-in-phase finite-amplitude monotonicity certificate and its sharp infinitesimal contrast, not that identity itself.

## Limitations
The explicit sufficient radius is conservative and rapidly small for large degrees. No assertion is made about maximal admissible amplitude, unit amplitude for low degrees, or global monotonicity outside the certified neighborhood. The exact high-degree power law concerns only the derivative as \(\rho\downarrow0\). The result is conditional on the complete originality comparison documented in the accompanying review; older formulations of small-amplitude three-term majorant phase inequalities may yet be found. Independent scientific validation has not occurred.

## References
1. G. Pan, C. You, H. Wang, J. Zhou, and Y. Chen, *Mockenhaupt's Three-Term Hardy--Littlewood Majorant Conjecture*, arXiv:2609.09740, first submitted 9 September 2026; primary MSC 42A05. https://arxiv.org/abs/2609.09740.
2. S. Krenedits, *Three-term idempotent counterexamples in the Hardy-Littlewood majorant problem*, arXiv:1006.0409, first submitted 2 June 2010; primary MSC 42A05. https://arxiv.org/html/1006.0409v3.
3. *Global coefficient-phase rigidity for high-order three-term majorants*, publicly available research record, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-global-coefficient-phase-rigidity-for-high-order-three-term-majo--ddd32718a69a.
4. *Even phase moments recover the normalized geometry of a three-frequency spectrum*, publicly available research record, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-even-phase-moments-recover-the-normalized-geometry-of-a-three-fr--7849dda51c79.
