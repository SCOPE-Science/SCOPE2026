# Cubic Walsh projection constants have two-root lattice fluctuations

## Finding
For integers \(N\ge3\), write \(\mathcal B_{=3}^N\) for the real span of the degree-three Walsh characters on \(\{-1,1\}^N\), with the supremum norm, and let \(\lambda_N=\lambda(\mathcal B_{=3}^N)\) be its absolute projection constant. Define
\[
\phi_0=\frac1{\sqrt{2\pi}},\qquad \phi_a=\phi_0e^{-3/2},\qquad c=\frac{2\phi_0+8\phi_a}{6},\qquad B_2(u)=u^2-u+\frac16,
\]
\[
\delta_N=\begin{cases}0,&N\ \mathrm{even},\\\frac12,&N\ \mathrm{odd},\end{cases}
\qquad \theta_N=\left\{\frac{\sqrt{3N}-N}{2}\right\}.
\]
Braces denote fractional part. The projection constant admits the *uniform lattice-phase expansion*
\[
\boxed{\lambda_N=cN^{3/2}+\frac{\sqrt N}{6}\left[-\frac52\phi_0-4\phi_a-12\phi_0B_2(\delta_N)-48\phi_aB_2(\theta_N)\right]+O(1).}
\]
Its second coefficient has no limit. Precisely,
\[
\boxed{\limsup_{N\to\infty}\frac{\lambda_N-cN^{3/2}}{\sqrt N}=-\frac{\phi_0}{4},\qquad
\liminf_{N\to\infty}\frac{\lambda_N-cN^{3/2}}{\sqrt N}=-\frac{3\phi_0}{4}-2\phi_a.}
\]
There is also an exact finite-dimensional boundary formula. With \(K_N=\left\lceil (N-\sqrt{3N-2})/2\right\rceil-1\), \(H_N=\lfloor(N-1)/2\rfloor\), and \(\binom ab=0\) if the lower index is out of range, set
\[
P_N(L)=\binom N3\left[\binom{N-3}{L}-2\binom{N-3}{L-1}+\binom{N-3}{L-2}\right].
\]
Then
\[
\boxed{\lambda_N=2^{1-N}[2P_N(K_N)-P_N(H_N)].}
\]

## Assumptions and scope
The cube carries normalized counting measure, and all function spaces and projection constants are over the real scalars. For \(N\ge3\), the Walsh support is every three-element subset of \(\{1,\ldots,N\}\); no lower-degree terms occur. The absolute projection constant is the least norm obtainable when projecting onto an isometric copy of the finite-dimensional space in an ambient \(\ell_\infty\)-space. The known invariant-projection formula of Defant–Galicer–Mansilla–Mastyło–Muro identifies it with the \(L^1\) norm of the Walsh projection kernel. That reduction and the leading Gaussian-limit constant are **prior results**, not the novelty claim.

## Proof
**1. Reduction and exact finite identity.** Let \(\varepsilon_i\) be independent fair signs, \(S_N=\sum_{i=1}^N\varepsilon_i\), and let \(Q_{3,N}\) denote the degree-three Walsh kernel. Newton's identities and \(\varepsilon_i^2=1\) give
\[
Q_{3,N}=\sum_{i<j<k}\varepsilon_i\varepsilon_j\varepsilon_k
=\frac{S_N^3-(3N-2)S_N}{6},\qquad
\lambda_N=\mathbb E|Q_{3,N}|.
\]
For exactly \(k\) negative signs, \(S_N=N-2k\). The coefficient-wise identity
\[
2^N\mathbb E[Q_{3,N}\mathbf1_{\{k\}}]=\binom N3\bigl[\binom{N-3}{k}-3\binom{N-3}{k-1}+3\binom{N-3}{k-2}-\binom{N-3}{k-3}\bigr]
\]
shows that the partial sum through \(L\) telescopes to \(P_N(L)\). On the positive-\(S_N\) half of the sign distribution the kernel is positive for \(S_N>\sqrt{3N-2}\), negative for \(0<S_N<\sqrt{3N-2}\), and zero at a root. The positive half ends at \(H_N\); the outer positive sector ends at \(K_N\). Using the symmetry of the absolute value under global sign change proves the stated boundary formula, including the cases when a root is an attainable integer.

**2. Local binomial expansion.** Set \(t=S_N/\sqrt N\), \(h=2/\sqrt N\), \(f(t)=t^3-3t\), \(g_N(t)=f(t)+2t/N\), \(\varphi(t)=(2\pi)^{-1/2}e^{-t^2/2}\), and \(H_4(t)=t^4-6t^2+3\). Uniform Stirling expansion on \(|t|\le\sqrt{C\log N}\), with any sufficiently large fixed \(C\), gives the lattice local limit
\[
\mathbb P\{S_N/\sqrt N=t\}
=h\varphi(t)\left[1-\frac{H_4(t)}{12N}+O\left(\frac{1+|t|^{12}}{N^2}\right)\right].
\]
Gaussian concentration and polynomial moment bounds make the complementary tails smaller than any prescribed inverse power of \(N\) by choosing \(C\) large. Consequently, with all sums taken on the parity lattice \(\mathcal L_N=\{(N-2k)/\sqrt N:0\le k\le N\}\),
\[
\frac{6\lambda_N}{N^{3/2}}
=h\sum_{t\in\mathcal L_N}\varphi(t)\left|g_N(t)\right|\left(1-\frac{H_4(t)}{12N}\right)+O(N^{-2}).
\]
The error follows by summing the integrable polynomial-times-Gaussian pointwise remainder, while bounding the tails separately.

**3. Continuum term and moving cusps.** Direct Gaussian integration on the intervals separated by \(0\) and \(\pm\sqrt3\) gives
\[
I_0=\int\varphi(t)|f(t)|\,dt=2\phi_0+8\phi_a,
\]
\[
I_1=\int\varphi(t)\left(2t\operatorname{sgn}f(t)-\frac{H_4(t)}{12}|f(t)|\right)\,dt=-\frac52\phi_0-4\phi_a.
\]
Here \(\operatorname{sgn}f\) may be defined arbitrarily at the three zeros, a set of Gaussian measure zero. The exact roots of \(g_N\) are \(0\) and \(\pm\sqrt{3-2/N}\). The latter shift only \(O(N^{-1})\) in standardized coordinates, hence only \(O(N^{-1/2})\) in lattice phase. This phase change contributes \(O(N^{-3/2})\) to the normalized lattice sum because \(B_2\) is uniformly Lipschitz on the circle.

For a continuous rapidly decaying piecewise smooth function \(F\) with finitely many derivative jumps \(\Delta F'(r)\), the shifted-lattice Euler summation formula is
\[
h\sum_{t\in a+h\mathbb Z}F(t)=\int F(t)\,dt-\frac{h^2}{2}\sum_r\Delta F'(r)B_2\!\left(\left\{\frac{r-a}{h}\right\}\right)+O(h^3).
\]
This follows by splitting at each jump and applying the Euler summation formula on the smooth intervals; the remainder is bounded by integrals of the piecewise third derivative. Applied to \(F=\varphi|f|\), its derivative jumps are \(6\phi_0\) at zero and \(12\phi_a\) at each of \(\pm\sqrt3\). The zero phase is \(\delta_N\), while the two nonzero roots have Bernoulli phase equal to \(B_2(\theta_N)\) by reflection symmetry \(B_2(1-u)=B_2(u)\). Since \(h^2=4/N\), the total normalized cusp correction equals
\[
-\frac{12\phi_0B_2(\delta_N)+48\phi_aB_2(\theta_N)}{N}.
\]
The smooth contributions combine as \(I_0+I_1/N\), with an \(O(N^{-3/2})\) normalized remainder. Multiplying by \(N^{3/2}/6\) gives the expansion with absolute \(O(1)\) remainder.

**4. Sharp oscillatory limits.** The periodic Bernoulli polynomial satisfies \(-1/12\le B_2(u)\le1/6\), with the minimum at \(u=1/2\) and maximum at integral \(u\). The maximal expression is realized asymptotically by odd \(N\) with \(\theta_N\to1/2\), giving \(-\phi_0/4\); the minimal expression is realized by even \(N\) with \(\theta_N\to0\), giving \(-3\phi_0/4-2\phi_a\). To justify both attainments, for either fixed parity the sequence \(\sqrt{3N}/2\) is strictly increasing to infinity with increments tending to zero; its fractional parts are therefore dense in \([0,1]\). Shifting by \(-N/2\) only changes this phase by a constant on a fixed parity. The \(O(1)/\sqrt N\) error vanishes, proving the limsup and liminf.

## Verification
The standalone standard-library checker `verify_cubic.py` compares the exact telescoped boundary formula with the complete rational Walsh-kernel sum for every \(3\le N\le400\), tests the Gaussian integration constants through independently evaluated expressions, and compares the phase formula with direct log-binomial summation at large finite dimensions. This finite evidence is auxiliary; the global theorem follows from the analytical identities, uniformly controlled local central limit expansion, and cusp Euler summation. See `VERIFICATION.md` for the actual run scope.

## Relationship to prior work
Defant, Galicer, Mansilla, Mastyło and Muro proved the invariant-projection reduction for Boolean-cube Walsh spectral spaces, and the leading asymptotic at every fixed degree; both results are used here. Their 2023 analysis includes the cubic \(N^{3/2}\) scale and Gaussian Hermite leading constant, but does not state the above dimension-dependent second term or sharp limsup and liminf. A publicly available result on the *second* homogeneous Walsh level gives a different one-root, parity-free oscillation of order one; it does not imply the present two-root cubic correction, whose order is \(\sqrt N\) and which has a separate parity phase. Dominici's pointwise Krawtchouk asymptotics do not evaluate this absolute binomial average to the required order.

## Limitations
The theorem concerns exactly degree three and real scalars. The lattice-phase coefficient oscillates and is not a universal constant. No analogous formula for all higher odd degrees is asserted. The leading asymptotic and the invariant-projection identity are established background; the asserted new contribution is the explicit finite boundary reduction and second-order phase law with sharp extrema. Equivalent results might exist under binomial absolute-deviation or Krawtchouk terminology; an independent originality assessment has not been performed.

## References
1. A. Defant, D. Galicer, M. Mansilla, M. Mastyło, S. Muro, *Projection constants for spaces of multivariate polynomials*, arXiv:2208.06467v1 (first publicly posted 2022-08-12).
2. A. Defant, D. Galicer, M. Mansilla, M. Mastyło, S. Muro, *Asymptotic insights for projection, Gordon–Lewis and Sidon constants in Boolean cube function spaces*, arXiv:2302.00233v1 (first publicly posted 2023-02-01); IMRN 2024.
3. D. Dominici, *Asymptotic analysis of the Krawtchouk polynomials by the WKB method*, arXiv:math/0501042 (2005), for pointwise asymptotics rather than absolute-moment phase coefficients.
4. *A lattice-phase second term for second-chaos projection constants on the Boolean cube*, public published-finding corpus 2026 record, URL: https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-a-lattice-phase-second-term-for-second-chaos-projection-constant--ec79809353f9 (quadratic, not cubic).
