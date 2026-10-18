# Fibonacci resonance and log-periodic singular-gap growth for a torus diffusion

## Finding
Let \(\mathbb T^2=(\mathbb R/2\pi\mathbb Z)^2\) carry normalized Haar probability measure. The generator of the stationary Brownian diffusion with constant incompressible drift is
\[
L_a=\Delta+a(\partial_x+\alpha\partial_y),\qquad
\alpha=\frac{\sqrt5-1}{2}=\phi^{-1},\quad
\phi=\frac{1+\sqrt5}{2},\quad a>0.
\]
Write \(H_0=L^2_0(\mathbb T^2)\) and define its *squared* smallest singular value by
\[
\gamma(a)=\inf\{\|L_au\|_2^2:u\in H^2(\mathbb T^2)\cap H_0,\ \|u\|_2=1\}.
\]
Let \(F_1=F_2=1\) and \(F_{n+1}=F_n+F_{n-1}\). For all sufficiently large real \(a\),
\[
\boxed{\gamma(a)=\min_{n\ge2}\big[(F_{n-1}^2+F_n^2)^2+a^2\phi^{-2n}\big].}\tag{1}
\]
The minimum is over a finite effective set at each \(a\); competing minimizers can tie at transition parameters. Define
\[
A=\frac{(1+\phi^{-2})^2}{25},\quad
f(x)=Ax^4+x^{-2},\quad
H(t)=\min_{j\in\mathbb Z} f(\phi^j t^{-1/3}),\qquad t>0.
\]
Then \(H\) is a positive, continuous, nonconstant function satisfying \(H(\phi^3t)=H(t)\), and
\[
\boxed{\frac{\gamma(a)}{a^{4/3}}=H(a)+o(1)}\qquad(a\to\infty).\tag{2}
\]
All asymptotic phases are attained. With
\[
x_*=\big(2A\big)^{-1/6},\qquad
x_c=\big[A\phi^2(\phi^2+1)\big]^{-1/6},
\]
the sharp extremal constants are
\[
\boxed{\liminf_{a\to\infty}\frac{\gamma(a)}{a^{4/3}}=f(x_*)
=\frac{3A^{1/3}}{2^{2/3}}=0.801898675219\ldots,}\tag{3}
\]
\[
\boxed{\limsup_{a\to\infty}\frac{\gamma(a)}{a^{4/3}}=f(x_c)
=0.992555716422\ldots.}\tag{4}
\]
Every number in the interval between the two constants occurs as a subsequential limit. In particular \(\sqrt{\gamma(a)}\asymp a^{2/3}\) and the \(L^2\)-relaxation time of averages in [1] is \(\Theta(a^{-2/3})\). This does **not** assert that this relaxation time has an exact leading constant, nor that the ordinary semigroup relaxation time accelerates.

## Assumptions and scope
The diffusion and its Laplacian use the \(2\pi\)-periodic torus, not the unit-period torus; this fixes all numerical constants. The norm on \(H_0\) is the standard \(L^2\) norm of normalized Haar measure. The operator domain is the mean-zero Sobolev space \(H^2\); its generator is a normal, not generally self-adjoint, operator. The square in the definition of \(\gamma\) matters. The source's \(s(L_a)\) equals \(\sqrt{\gamma(a)}\). Fourier frequencies in \(\mathbb Z^2\) include both signs; the zero frequency is excluded. Statements (1)--(4) hold for the single specified golden-ratio slope. The \(o(1)\) in (2) is uniform in logarithmic phase. No rate uniform over other irrational slopes is asserted.

## Proof
**1. Exact spectral reduction.** On the Fourier character \(e^{i(px+qy)}\), the generator has eigenvalue \(-(p^2+q^2)+ia(p+\alpha q)\). Fourier orthogonality and normality give
\[
\gamma(a)=\min_{(p,q)\in\mathbb Z^2\setminus\{(0,0)\}}
\big\{(p^2+q^2)^2+a^2(p-\alpha q)^2\big\}.\tag{5}
\]
The sign change in \(q\) is only a reindexing. The minimum exists since the quartic term diverges with \(|p|+|q|\).

**2. Fibonacci frequencies and an upper comparison.** Fibonacci's explicit formula gives
\[
F_n=\frac{\phi^n-(-\phi)^{-n}}{\sqrt5},\qquad
F_{n-1}-\alpha F_n=(-1)^n\phi^{-n}.\tag{6}
\]
Select \(n\) so that \(F_n\asymp a^{1/3}\). Substituting \((p,q)=(F_{n-1},F_n)\) into (5) proves \(\gamma(a)\le C a^{4/3}\) for all large \(a\) and some finite \(C\). Any minimizing frequency then satisfies \(|p-\alpha q|\le\sqrt C a^{-1/3}<1/2\). In particular \(q\ne0\). Changing both signs makes \(q>0\); \(p\) is necessarily the unique nearest integer to \(\alpha q\).

**3. Exact Fibonacci reduction.** Fix \(n\ge2\) and an integer \(F_n\le q<F_{n+1}\). The two integer vectors \((F_{n-1},F_n)\) and \((F_n,F_{n+1})\) form a unimodular basis. Thus every integer pair has a unique representation
\[
(p,q)=r(F_{n-1},F_n)+s(F_n,F_{n+1}),\qquad r,s\in\mathbb Z.
\]
By (6) its discrepancy is
\[
|p-\alpha q|=\phi^{-n}|r-s/\phi|.\tag{7}
\]
If \(s\ge1\), the bound \(q<F_{n+1}\) forces \(r\le-1\), so \(|r-s/\phi|>1\). If \(s\le0\), positivity of \(q\) forces \(r\ge1\), giving \(|r-s/\phi|\ge1\). Hence \(|p-\alpha q|\ge\phi^{-n}\), with equality at \((F_{n-1},F_n)\). Moreover the nearest-integer function is nondecreasing, and \(F_{n-1}\) is the nearest integer to \(\alpha F_n\) by (6); therefore \(p\ge F_{n-1}\). Both nonnegative spectral terms in (5) for \((p,q)\) are consequently at least those of the Fibonacci pair. Every minimizing frequency is Fibonacci, proving (1). This argument handles the duplicated small denominator \(F_1=F_2=1\) by starting at \(n=2\).

**4. Uniform geometric phase limit.** By (6),
\[
(F_{n-1}^2+F_n^2)^2=A\phi^{4n}(1+O(\phi^{-2n})).\tag{8}
\]
For fixed \(s>0\), set \(a=\phi^{3N}s\) and index the candidates in (1) by \(n=N+j\). After division by \(a^{4/3}\), each fixed \(j\) converges to
\[
A\phi^{4j}s^{-4/3}+\phi^{-2j}s^{2/3}
=f(\phi^j s^{-1/3}).\tag{9}
\]
This convergence is uniform for \(s\) in any compact subset of \((0,\infty)\). It also holds after taking minima: the first term of (9) diverges uniformly as \(j\to+\infty\), and the second as \(j\to-\infty\). These bounds exclude all but finitely many \(j\) uniformly in such compact sets; (8) supplies uniform convergence on the remaining finite set. Therefore
\[
\lim_{N\to\infty}\frac{\gamma(\phi^{3N}s)}{(\phi^{3N}s)^{4/3}}=H(s),
\]
uniformly on \(1\le s\le\phi^3\). Shifting \(j\) shows \(H(\phi^3s)=H(s)\). Every large \(a\) is \(\phi^{3N}s\) for some integer \(N\) and \(1\le s<\phi^3\), proving (2) with its uniform error.

**5. Exact extremal phase constants.** Differentiation gives a single minimum of \(f\) at \(x_*=(2A)^{-1/6}\) with value (3). The geometric lattice \(\{\phi^j x:j\in\mathbb Z\}\) has its lowest value of \(f\) at one of the two consecutive points straddling \(x_*\). Thus, choosing a representative \(x\in[x_*/\phi,x_*]\), the envelope is \(\min\{f(x),f(\phi x)\}\). On this interval \(f(x)\) decreases while \(f(\phi x)\) increases. Its maximum is attained at their unique crossing. Solving \(f(x)=f(\phi x)\) yields \(x=x_c\), which lies strictly between \(x_*/\phi\) and \(x_*\), establishing (4) and the strict inequality between (3) and (4). Continuity and the free phase \(s>0\) supply every intermediate accumulation value.

**6. Consequence for time averages.** Equation (1.33) of [1] bounds the average relaxation time between \(2(1-e^{-1})/\sqrt{\gamma(a)}\) and \(2e/\sqrt{\gamma(a)}\). The positive finite extrema above imply \(\sqrt{\gamma(a)}\asymp a^{2/3}\), so the average relaxation time has order \(a^{-2/3}\). The bounds do not identify an exact leading constant for that time. The ordinary relaxation time is unchanged by the drift because each Fourier semigroup mode has modulus \(e^{-(p^2+q^2)t}\).

## Verification
Run `python3 verify_golden_slope.py` with Python 3.11 or later. It independently diagonalizes finite Fourier windows for five prescribed drift amplitudes, using the analytic quartic lower bound to make each finite search exhaustive. It checks Fibonacci residuals and best-denominator comparisons and compares the normalized minima against the proposed logarithmic phase envelope at large amplitudes. It also checks the stationary points and crossing algebra numerically to 64 decimal digits. These calculations corroborate the identities but cannot prove the quantifiers over all \(a\), \(n\), or \(j\); the argument above supplies those proofs.

## Relationship to prior work
Sznitman and Widmayer [1, Example 1] prove qualitative acceleration of the time-average relaxation for any irrational constant torus direction while ordinary relaxation does not accelerate. Their Theorem 1.3 addresses divergence of the squared singular-value gap, and their equation (1.33) connects that gap to the relaxation time of averages. Neither their stated Example 1 nor their proofs gives the exact golden-slope gap minimizer, phase-dependent leading profile, or limiting constants (3)--(4). The new assertion refines their *same model*, not their general criterion.

Chatterjee [2, Theorem 2.5 and Section 3.10] proves a related \(N^{4/3}\) relaxation-time order for a **finite discrete torus** with irrational quadratic transition probability, using Diophantine estimates. It has a different asymptotic parameter and a different generator, and it states two-sided order estimates rather than the above continuous-diffusion log-periodic profile. The Eberle–Lörler [3] and Xu [4] treatments concern general singular-gap/relaxation principles. The golden-ratio best-approximation facts in (6)--(7) are classical and are not claimed as new. The contribution is the sharp spectral optimization and its nonconvergent phase profile for the natural diffusion in [1].

## Limitations
The explicit constants are tied to the \(2\pi\)-torus and golden slope; changing torus convention or diffusion normalization changes them. A period in the leading normalized gap does not assert exact periodicity at finite \(a\), and no analogous law is proved for other quadratic irrationals or variable drifts. The time-average relaxation statement is an order bound only. Relevant general papers [3] and [4] were identified by their bibliographic records and abstracts; their complete texts could not be inspected here, so an unrecognized stronger implication remains a residual originality risk. A differently framed prior calculation of the same golden-slope lattice minimum is also possible.

## References
[1] A.-S. Sznitman and K. Widmayer, *On Large Drift Enhancement for the Relaxation Time of Averages*, arXiv:2610.12425v1 (first posted 8 October 2026), especially Theorems 1.3--1.4, equation (1.33), and Section 2 Example 1. https://arxiv.org/html/2610.12425v1

[2] S. Chatterjee, *Spectral gap of nonreversible Markov chains*, arXiv:2310.10876v3; *Annals of Applied Probability* 35 (2025), 2644--2672, especially Theorem 2.5 and proof in Section 3.10. https://arxiv.org/pdf/2310.10876

[3] A. Eberle and F. Lörler, *Relaxation times of non-reversible Markov processes*, arXiv:2607.10801 (2026). https://arxiv.org/abs/2607.10801

[4] R. Xu, *Singular-value gap of nonreversible Markov processes*, arXiv:2606.01683 (2026). https://arxiv.org/abs/2606.01683
