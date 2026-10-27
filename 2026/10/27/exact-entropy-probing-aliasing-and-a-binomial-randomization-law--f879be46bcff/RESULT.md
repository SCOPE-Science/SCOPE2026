# Exact entropy-probing aliasing and a binomial randomization law on cycles

## Finding

Let \(m\geq3\) and \(L\geq2\) be integers, put \(n=mL\), and let \(C_n\) be the unweighted cycle. Write \(\mathcal L_n\) for its graph Laplacian, \(\rho_n=\mathcal L_n/(2n)\) for its unit-trace density matrix, and \(f(t)=-t\log t\), with \(f(0)=0\). Let \(S_n=\operatorname{tr}f(\rho_n)\). Color vertex \(j\in\{0,\ldots,n-1\}\) by its residue modulo \(m\), use its \(m\) indicator vectors \(v_r\), and set
\[
T_{m,L}=\sum_{r=0}^{m-1}v_r^{\mathsf T}f(\rho_n)v_r.
\]
For every real \(s\geq3\), define the absolutely convergent positive series
\[
F(s)=2\sum_{h=1}^{\infty}\frac{1}{sh((sh)^2-1)}.
\]
Then the **exact deterministic probing deficit** is
\[
\boxed{S_n-T_{m,L}=F(m)-F(mL)
 =2\sum_{\substack{h\geq1\\L\nmid h}}\frac{1}{mh((mh)^2-1)}>0.}
\]
For fixed \(m\), it increases strictly with \(L\), and its sharp supremum over all such cycle sizes is \(F(m)\), approached as \(L\to\infty\) but never attained. For all \(m\geq3\) the convergent expansion is
\[
\boxed{S_n-T_{m,L}=2\sum_{q=0}^{\infty}
 \frac{\zeta(2q+3)}{m^{2q+3}}
 \left(1-L^{-(2q+3)}\right).}
\]
In particular, uniformly for integers \(L\geq2\) as \(m\to\infty\),
\[
S_n-T_{m,L}=
\frac{2\zeta(3)(1-L^{-3})}{m^3}+O(m^{-5}).
\]

For the **antipodal two-vertex classes** \(L=2\), independently give each vertex a uniform sign \(\xi_j\in\{-1,1\}\), and replace the indicator \(v_r\) with \(w_r=\xi_r e_r+\xi_{r+m}e_{r+m}\). Define
\[
T_m^{\pm}=\sum_{r=0}^{m-1}w_r^{\mathsf T}f(\rho_{2m})w_r,
\qquad \Delta_m=F(m)-F(2m).
\]
Then for independent uniform signs \(\varepsilon_0,\ldots,\varepsilon_{m-1}\),
\[
\boxed{T_m^{\pm}-S_{2m}\ \overset{d}{=}
 -\frac{\Delta_m}{m}\sum_{r=0}^{m-1}\varepsilon_r.}
\]
Thus the complete error distribution is binomial:
\[
\Pr\left\{T_m^{\pm}-S_{2m}
 =-\frac{\Delta_m}{m}(m-2k)\right\}
 =2^{-m}\binom mk,\qquad k=0,\ldots,m.
\]
It follows exactly that
\[
\mathbb E T_m^{\pm}=S_{2m},\quad
\operatorname{Var}(T_m^{\pm})=\frac{\Delta_m^2}{m},\quad
\left|T_m^{\pm}-S_{2m}\right|\leq\Delta_m,
\]
with equality in the last bound with probability \(2^{1-m}\). In the family of increasing even cycles,
\[
\Delta_m\sim\frac{7\zeta(3)}{4m^3},\qquad
\sqrt{\mathbb E\left|T_m^{\pm}-S_{2m}\right|^2}
 \sim\frac{7\zeta(3)}{4m^{7/2}},
\]
and \(\sqrt m(T_m^{\pm}-S_{2m})/\Delta_m\) converges in law to a standard normal variable. The two estimators each use exactly \(m\) quadratic-form evaluations with \(f(\rho_{2m})\).

## Assumptions and scope

Vertices are cyclically numbered. The cycle Laplacian has diagonal entries \(2\), nearest-neighbor entries \(-1\), and all other entries zero. The density matrix \(\rho_n\) is positive semidefinite and singular with trace one; its zero eigenvalue is handled by continuity of \(f\). Coloring by residue modulo \(m\) is a distance-\((m-1)\) coloring, because vertices in one class are separated by at least \(m\) graph edges. The Rademacher variables at all \(2m\) vertices are mutually independent. All matrix-function and quadratic-form evaluations are exact. No randomization or approximation of the matrix function itself is assumed.

The error comparison is an absolute-error comparison for these cycle families, not a blanket claim of superiority on arbitrary graphs or for arbitrary probe allocations.

## Proof

**1. Fourier diagonalization.** The Fourier modes \(u_j(k)=n^{-1/2}\exp(2\pi i jk/n)\) diagonalize \(\rho_n\), with eigenvalues
\[
\lambda_j=\frac{1-\cos(2\pi j/n)}{n},\qquad j=0,\ldots,n-1.
\]
For \(r\in\{0,\ldots,m-1\}\), the indicator of \(\{r,r+m,\ldots,r+(L-1)m\}\) has Fourier support exactly at modes \(j=Lt\), where \(t=0,\ldots,m-1\). At each such mode its squared Fourier coefficient is \(L^2/n\). Summing over all \(m\) indicator vectors yields weight \(mL^2/n=L\), and hence
\[
T_{m,L}=L\sum_{t=0}^{m-1} f\!\left(\frac{1-\cos(2\pi t/m)}{n}\right).
\]
Let \(h(\theta)=1-\cos\theta\) and \(g(\theta)=h(\theta)\log h(\theta)\), continuously extended to zero. The average of \(h\) over any complete \(s\)-point equally spaced grid is one for \(s\geq3\). Writing
\[
A_s=\frac1s\sum_{j=0}^{s-1}g(2\pi j/s),
\]
we therefore have \(S_n=\log n-A_n\) and \(T_{m,L}=\log n-A_m\). The deficit is \(A_m-A_n\).

**2. Exact Fourier coefficients.** In the integrable or Abel-summed Fourier sense,
\[
\log(1-\cos\theta)=-\log2-2\sum_{j=1}^{\infty}\frac{\cos(j\theta)}{j}.
\]
If \(\widehat g_k=(2\pi)^{-1}\int_{0}^{2\pi}g(\theta)e^{-ik\theta}\,d\theta\), multiplication by \(1-\cos\theta\) gives for every integer \(k\geq2\)
\[
\widehat g_k=-\frac1k+\frac12\left(\frac1{k-1}+\frac1{k+1}\right)
 =\frac{1}{k(k^2-1)}=\widehat g_{-k}.
\]
This identity may also be justified first with Abel damping, followed by convergence in \(L^1\). Since \(g\) is continuous and its Fourier coefficients decay cubically, its Fourier series converges absolutely to \(g\). For \(s\geq3\), exact grid aliasing then gives
\[
A_s=\widehat g_0+2\sum_{h\geq1}\widehat g_{sh}
 =\widehat g_0+F(s).
\]
Subtracting at \(s=m\) and \(s=mL\) proves \(\Delta=F(m)-F(mL)\). The difference removes exactly those positive terms with \(L\mid h\), proving strict positivity.

**3. Sharp rates and cycle-size extremum.** The terms defining \(F(s)\) are strictly decreasing in \(s\), hence \(F(m)-F(mL)\) increases strictly with \(L\) and tends to \(F(m)\). For \(m\geq3\), the positive geometric series
\[
\frac1{mh((mh)^2-1)}
 =\sum_{q\geq0}\frac{1}{m^{2q+3}h^{2q+3}}
\]
may be summed in either order by monotone convergence. Subtracting the terms whose index is divisible by \(L\) proves the exact zeta expansion. The displayed asymptotic follows by bounding the remaining convergent terms uniformly in \(L\geq2\).

**4. Exact antipodal randomization law.** Put \(B=f(\rho_{2m})\). Circulant symmetry makes every antipodal entry \(B_{r,r+m}\) equal to one constant \(b\). Every color class has two vertices, so the deterministic trace formula reads
\[
T_{m,2}=\operatorname{tr}B+2mb,
\qquad b=-\frac{\Delta_m}{2m}<0.
\]
The independent signed probes satisfy
\[
\sum_{r=0}^{m-1}w_r^{\mathsf T}Bw_r
 =\operatorname{tr}B+2b\sum_{r=0}^{m-1}\xi_r\xi_{r+m}
 =S_{2m}-\frac{\Delta_m}{m}\sum_{r=0}^{m-1}\varepsilon_r,
\]
where the products \(\varepsilon_r=\xi_r\xi_{r+m}\) are independent fair signs. Elementary binomial counting establishes the entire finite distribution, expectation, variance, and sharp pathwise bound. There are precisely two extreme all-equal sign configurations among \(2^m\) sign products. For \(L=2\), the zeta expansion has leading coefficient \(2(1-2^{-3})\zeta(3)=7\zeta(3)/4\). The classical central limit theorem applied to independent fair signs completes the proof.

## Verification

Run `python verify.py` with Python 3 and no third-party packages. It checks \(248\) exact rational Fourier-coefficient identities, independent finite Fourier diagonalizations versus the analytic series for \(28\) cycle instances, binomial distributions by enumeration, and the predicted leading asymptotic. Its successful output is `PASS: 1175 finite symbolic, independent Fourier, series, binomial and asymptotic checks`.

The proof above, not the finite verifier, establishes the infinite Fourier aliasing, all admissible dimensions, strict monotonicity, and asymptotic limits. Infinite sums are controlled by absolute convergence; the zero eigenvalue is handled by the continuous entropy convention.

## Relationship to prior work

Benzi, Rinelli, and Simunec (arXiv:2212.09642, especially Section 3.1, Lemma 3.5 and Proposition 3.6) prove nonpositivity of separated off-diagonal entropy entries of symmetric \(M\)-matrices and a general lower-bound property for deterministic probing. They also give a universal error bound which, for this cycle normalization and coloring distance \(m-1\), is of order \(m^{-2}\). The exact finite-cycle Fourier alias, sharp cubic coefficient, and its sharp cycle-size envelope are not those general statements.

Frommer, Rinelli, and Schweitzer (arXiv:2308.07722, Sections 2--3) give generic stochastic probing constructions, variances, and sign-based comparisons. These are important ingredients of the context, not claimed as original. The explicit entropy-dependent finite binomial law and its exact \(\Delta_m\) coefficient, tied to the cycle's spectrum, constitute the more specific calculation here. Frommer, Schimmel, and Schweitzer (arXiv:2009.01589) analyze general graph-coloring trace probing and approximation bounds; they do not supply the displayed cycle-specific entropy law in the inspected material. Standard Fourier aliasing, cycle eigenvalues, and the Rademacher-sum distribution are classical tools and not individually claimed as new.

## Limitations

These are analytic identities for unweighted finite cycles and the precisely specified periodic or antipodal coloring; the randomized full distribution uses classes of size exactly two. Changing graph weights, signs' dependence, or matrix-function evaluation accuracy may change the formulas. The sharp rate is along increasing families of cycles (and probe counts), not a universal complexity exponent for an arbitrary fixed matrix. No finite-precision implementation or floating-point error analysis is asserted. Publication priority may remain uncertain in literature not fully indexed or inspected.

## References

1. M. Benzi, M. Rinelli, and I. Simunec, *Computation of the von Neumann entropy of large matrices via trace estimators and rational Krylov methods*, arXiv:2212.09642, first posted 19 December 2022, Sections 2--3. https://arxiv.org/abs/2212.09642
2. A. Frommer, M. Rinelli, and M. Schweitzer, *Analysis of stochastic probing methods for estimating the trace of functions of sparse symmetric matrices*, arXiv:2308.07722, first posted 15 August 2023, Sections 2--3. https://arxiv.org/abs/2308.07722
3. A. Frommer, C. Schimmel, and M. Schweitzer, *Analysis of probing techniques for sparse approximation and trace estimation of decaying matrix functions*, arXiv:2009.01589, first posted 3 September 2020. https://arxiv.org/abs/2009.01589
