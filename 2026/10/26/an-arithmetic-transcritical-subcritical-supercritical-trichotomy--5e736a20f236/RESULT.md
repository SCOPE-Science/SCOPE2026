# An arithmetic transcritical–subcritical–supercritical trichotomy for self-consistent expanding circle maps

## Finding
For each integer \(b\ge2\), let \(\mathbb T=\mathbb R/\mathbb Z\), and define the nonlinear transfer evolution of a probability density \(\rho\) by
\[
\mathcal F_{b,\kappa}(\rho)=(f_{u})_*\rho,\qquad
f_u(x)=bx+u\sin(2\pi bx)\pmod1,\qquad
u=\kappa\int_{\mathbb T}\cos(2\pi y)\rho(y)\,dy,\quad u=\nu.
\]
Here pushforward means the Perron–Frobenius density under the indicated map. For every real \(\kappa\), the uniform density \(\rho\equiv1\) is fixed. Put \(\delta=1+\pi\kappa\); its nontrivial local analytic fixed-density bifurcation at \(\delta=0\) obeys the following exact degree-dependent classification. In a sufficiently small joint neighborhood of \((\rho,\kappa)=(1,-1/\pi)\), the *only* nonuniform analytic probability-density solutions are:

- \(b=2\): exactly one for each small \(\delta\ne0\), with mean-field displacement \(u=-\delta/(2\pi)+O(\delta^2)\); the branch crosses the uniform state (transcritical).
- \(b=3\): exactly two for each small \(\delta>0\), and none for \(\delta\le0\), with \(u_\pm=\pm\sqrt\delta/(2\pi)+O(\delta)\) (subcritical relative to loss of linear stability).
- \(b\ge4\): exactly two for each small \(\delta<0\), and none for \(\delta\ge0\), with \(u_\pm=\pm\sqrt{-2\delta}/\pi+O_b(|\delta|)\) (supercritical).

The **linear** eigenvalue of the uniform state selected by the cosine mean field, \(-\pi\kappa\), is independent of \(b\), yet the nonlinear branch topology changes twice with \(b\).

## Assumptions and scope
Here \(b\) is a fixed integer at least two, \(\kappa\) is real in a sufficiently small \(b\)-dependent neighborhood of \(-1/\pi\), and densities are real-analytic, normalized, nonnegative and sufficiently close to \(1\) in a fixed analytic strip norm. The associated circle maps are expanding: \(f'_u(x)=b[1+2\pi u\cos(2\pi bx)]>1\) for sufficiently small \(|u|\). The count is of density fixed points, not orbits modulo translation or stability classes; all nonuniform densities are distinct. Neighborhoods and remainder constants may depend on the fixed \(b\). The result does not classify distant invariant densities or singular invariant measures.

## Proof
**Analytic reduction.** Write \(E_b(x)=bx\pmod1\) and \(g_u(x)=x+u\sin(2\pi x)\), so \(f_u=g_u\circ E_b\). The Perron–Frobenius operator of \(E_b\) is
\[
(P_b\psi)(z)=\frac1b\sum_{j=0}^{b-1}\psi((z+j)/b).
\]
For each small \(u\), the expanding analytic map \(f_u\) has a unique normalized analytic invariant density \(r_{b,u}\) near one and \(r_{b,0}=1\). For completeness this follows directly by applying analytic implicit-function theory to \(r-\mathcal L_{g_u}P_b r=0\) on the affine space of normalized analytic strip functions: \(P_b\) improves strip width by factor \(b\), and \(\mathcal L_{g_u}\) consumes arbitrarily little of that gained width for \(u\) small. On the zero-mean subspace, \(I-P_b\) has bounded inverse \(\sum_{n\ge0}P_b^n\), since successive deletion of nonmultiples of \(b\) gives super-exponential Fourier decay on a fixed analytic strip. The analytic family is real and strictly positive near \(1\). Uniqueness of the invariant probability density for each expanding full-branch \(f_u\) also follows from the standard spectral gap.

Define the real-analytic scalar moment
\[
M_b(u)=\int_\mathbb T\cos(2\pi x)r_{b,u}(x)\,dx.
\]
The self-consistency condition is exactly \(u=\kappa M_b(u)\). For any fixed point near the uniform density, \(u\) is small and its density must be \(r_{b,u}\); conversely a small scalar solution produces a positive analytic fixed density. Moreover \(M_b(0)=0\), so the uniform branch occurs at \(u=0\) for all \(\kappa\).

**Exact cubic expansion.** With \(s(x)=\sin(2\pi x)\), the analytic transfer identity is
\[
\mathcal L_{g_u}\psi=\sum_{j=0}^{3}\frac{(-u)^j}{j!}\,\partial_x^j[s(x)^j\psi(x)]+O(u^4),
\]
where the error is in a slightly narrower analytic strip. Let \(r_{b,u}=1+\sum_{n=1}^3u^n r_n+O_b(u^4)\). Comparing coefficients gives the finite, exactly solvable recurrence
\[
(I-P_b)r_n=\sum_{j=1}^n\frac{(-1)^j}{j!}\partial_x^j[s^jP_b r_{n-j}],\qquad r_0=1,
\]
with every \(r_n\) of zero mean. In complex Fourier notation, \(P_b(e^{2\pi ikx})=e^{2\pi i(k/b)x}\) if \(b\mid k\), and zero otherwise. Thus \((I-P_b)^{-1}=\sum_{m\ge0}P_b^m\) is a *finite sum on these zero-mean trigonometric polynomials*.

In particular \(r_1=-2\pi\cos(2\pi x)\). Writing \(c_j=\cos(2\pi jx)\), the next coefficients are
\[
\begin{array}{c|c|c}
b&r_2/\pi^2&r_3/\pi^3\\\hline
2&4(c_1+c_2)&-7c_1-8c_2-9c_3\\
3&4c_2&-8c_1-9c_3\\
b\ge4&4c_2&c_1-9c_3.
\end{array}
\]
The distinctions arise exactly because \(P_2c_2=c_1\) and \(P_3c_3=c_1\), whereas no corresponding low-order mode folding occurs for \(b\ge4\). Taking the first cosine coefficient divided by two yields
\[
M_b(u)=\begin{cases}
-\pi u+2\pi^2u^2-\frac72\pi^3u^3+O(u^4),&b=2,\\
-\pi u-4\pi^3u^3+O(u^4),&b=3,\\
-\pi u+\frac12\pi^3u^3+O_b(u^4),&b\ge4.
\end{cases}
\]
The included exact-rational checker independently implements this Fourier recurrence through degree three.

**All local branches.** Divide the scalar equation \(u-\kappa M_b(u)=0\) by \(u\) analytically and set \(G_b(u,\delta)=1-\kappa M_b(u)/u\), where \(\kappa=(\delta-1)/\pi\). For \(b=2\), \(G_2=\delta+2\pi u+O(u^2+|\delta u|)\), so the implicit-function theorem produces exactly one small nonzero solution whenever \(\delta\ne0\), with the asserted expansion. For \(b=3\), \(G_3=\delta-4\pi^2u^2+O(|\delta|u^2+|u|^3)\); for \(b\ge4\), \(G_b=\delta+\tfrac12\pi^2u^2+O_b(|\delta|u^2+|u|^3)\). Since \(\partial_{uu}G_b\) has a strict sign in a neighborhood, \(G_b\) is locally strictly concave for \(b=3\) and strictly convex for \(b\ge4\). Its unique nearby extremum yields exactly two simple zeros on the specified side and none on the other, by continuity and the Weierstrass preparation (or elementary convexity) argument. The displayed square-root laws follow by balancing the leading terms; at \(\delta=0\) there is no distinct nonuniform root sufficiently near zero. Finally, linearizing \(\mathcal F\) at density \(1\) sends the cosine mode to \(-\pi\kappa\) times itself, establishing the common threshold.

## Verification
The standalone script `check_fourier.py` verifies every displayed Fourier coefficient using only Python's standard-library exact rational arithmetic, for expansion degrees \(b=2,3,4,5,6,8,10,20\). It computes the coefficient recurrence, checks zero mean and Fourier conjugate symmetry, and verifies the three moment coefficients. The script terminates with `EXACT_FOURIER_COEFFICIENTS_PASS`, and `checker_output.txt` records its output. These are finite checks supporting the symbolic coefficient computation; the analytic implicit-function and root-exhaustion arguments provide the infinite-family proof.

## Relationship to prior work
Ahmad and Tanzi (2026) develop observable Lyapunov exponents and linearization of nonlinear self-consistent transfer operators for globally coupled maps. Bardet, Keller and Zweimüller (2008) demonstrate pitchfork bifurcation for a different piecewise fractional-linear mean-field model. Bahsoun and Liverani (2024) develop a general transfer-operator bifurcation setting. Sélley and Bálint (2015) study diffusive coupling of expanding circle maps. None of the inspected specific results supplies the sign-changing cubic Fourier coefficient or the degree-two/three/four-and-above *classification* for the sine-forced separable model. Prior results concerning the linear eigenvalue are not claimed as new. General nonlinear spectral perturbation techniques may be applicable, but the model-specific arithmetic classification is not an immediate statement of the inspected references.

## Limitations
This is a local real-analytic density classification for fixed integer degree, not a global classification of all invariant laws. Stability of every nonuniform branch under iteration of the nonlinear transfer operator is not asserted. The coefficients depend on the exact sine forcing and cosine observable; a generic nonseparable or noisy coupling need not exhibit the trichotomy. Independent review and comprehensive priority verification remain outstanding.

## References
1. Masood Ahmad and Matteo Tanzi, *Observable Lyapunov Exponents for Globally Coupled Maps in the Mean-Field Limit*, arXiv:2609.27484v1, first posted 2026-09-23, https://arxiv.org/html/2609.27484v1 .
2. Jean-Baptiste Bardet, Gerhard Keller and Roland Zweimüller, *Stochastically stable globally coupled maps with bistable thermodynamic limit*, arXiv:0812.4040, https://arxiv.org/abs/0812.4040 .
3. Wael Bahsoun and Carlangelo Liverani, *Mean field coupled dynamical systems: Bifurcations and phase transitions*, arXiv:2402.11076, https://arxiv.org/abs/2402.11076 .
4. Fanni M. Sélley and Péter Bálint, *Mean-field coupling of identical expanding circle maps*, arXiv:1512.05556, https://arxiv.org/abs/1512.05556 .
