# Bounded-remainder Schatten moments and an arcsine energy law for finite Cesàro matrices

## Finding

For each integer \(n\ge 1\), let \(C_n\) be the \(n\)-by-\(n\) classical Cesàro matrix over \(\mathbb R\) or \(\mathbb C\), with \((C_n)_{ij}=1/i\) for \(1\le j\le i\le n\), and zero otherwise. Put \(B_n=C_nC_n^*\), \(H_n=\sum_{i=1}^n1/i\), and \(c_k=\binom{2k-2}{k-1}\) for integers \(k\ge1\). **Every even Schatten moment has a sharp logarithmic coefficient and a dimension-uniform remainder:** for all \(n\ge1\) and integers \(k\ge2\),
\[
-kc_k\le \operatorname{tr}(B_n^k)-c_kH_n\le k\zeta(2)4^{k-2}.
\tag{1}
\]
For \(k=1\), \(\operatorname{tr}(B_n)=H_n\) exactly. Therefore
\[
\lim_{n\to\infty}\frac{\|C_n\|_{S_{2k}}^{2k}}{H_n}=\binom{2k-2}{k-1}
\quad(k\ge1).
\tag{2}
\]
The upper moment remainder in (1) is explicit but not claimed optimal. For example, an exact finite identity is \(\operatorname{tr}(B_n^2)=2H_n-\sum_{j=1}^n j^{-2}\).

Let \(\lambda_{1,n},\ldots,\lambda_{n,n}\) be the eigenvalues of \(B_n\). The canonical Hilbert–Schmidt-energy-weighted spectral probability measure
\[
\mu_n=\frac1{H_n}\sum_{j=1}^n\lambda_{j,n}\delta_{\lambda_{j,n}}
\tag{3}
\]
converges weakly, as \(n\to\infty\), to the arcsine law on \([0,4]\) with density
\[
\frac{\mathbf1_{(0,4)}(x)}{\pi\sqrt{x(4-x)}}.
\tag{4}
\]
Every fixed polynomial test has a computable error of order \(H_n^{-1}\), directly from (1). This is a trace-weighted, not the usual eigenvalue-counting, spectral limit.

## Assumptions and scope

All matrices are finite and act on Euclidean \(\ell_2^n\); statements hold over both real and complex scalars. The moment order \(k\) is a fixed positive integer when passing to the limit; the finite bounds (1) hold simultaneously for all \(n\ge1\) and \(k\ge2\). Here \(\zeta(2)=\sum_{j=1}^\infty j^{-2}=\pi^2/6\). Schatten norms are defined by \(\|C_n\|_{S_{2k}}^{2k}=\operatorname{tr}((C_nC_n^*)^k)\). A measure has weak convergence if integrals of all continuous functions on \([0,4]\) converge. No quantitative rate is asserted for arbitrary continuous test functions.

## Proof

**1. Exact Gram kernel and spectral containment.** Directly,
\[
(B_n)_{ij}=\frac{\min(i,j)}{ij}=\frac1{\max(i,j)}.
\tag{5}
\]
It is positive definite because \(C_n\) is invertible, and \(\operatorname{tr}B_n=H_n\). With Schur weights \(w_i=i^{-1/2}\), the integral estimates \(\sum_{j=1}^i j^{-1/2}\le2\sqrt i\) and \(\sum_{j=i+1}^\infty j^{-3/2}\le2/\sqrt i\) imply
\[
\sum_{j=1}^n(B_n)_{ij}w_j
=\frac1i\sum_{j\le i}j^{-1/2}+\sum_{j>i}j^{-3/2}\le4w_i.
\]
The symmetric Schur test yields \(0<B_n\le4I\), placing every eigenvalue in \((0,4]\). Its trace is the normalization in (3).

**2. A continuous cube approximation with a uniform boundary error.** For \(k\ge2\), write \(x_{k+1}=x_1\) and define on \([1,\infty)^k\)
\[
F_k(x_1,\ldots,x_k)=\prod_{r=1}^k\frac1{\max(x_r,x_{r+1})}.
\]
It decreases in each coordinate. Its integer-cube sum is the exact trace
\[
S_{n,k}=\sum_{i_1,\dots,i_k=1}^nF_k(i_1,\ldots,i_k)
=\operatorname{tr}(B_n^k).
\]
Let \(T=\log(n+1)\) and \(I_{T,k}=\int_{[1,n+1]^k}F_k(x)\,dx\). Coordinatewise monotonicity makes \(0\le S_{n,k}-I_{T,k}\). On the unit cube beginning at an integer vector \(i\), the pointwise error is at most \(F_k(i)-F_k(i+\mathbf1)\). Telescope one coordinate at a time, sum the differing coordinate over \(1,\ldots,n\), discard the nonnegative far boundary, and use monotonicity on the remaining coordinates. This proves
\[
0\le S_{n,k}-I_{T,k}
\le k\sum_{i_2,\ldots,i_k=1}^nF_k(1,i_2,\ldots,i_k).
\tag{6}
\]
The common face sum is exactly \(u^*B_n^{k-2}u\) for \(u_j=1/j\); in particular for \(k=2\) it is \(\sum_jj^{-2}\). By the Schur bound and \(\|u\|_2^2\le\zeta(2)\),
\[
0\le S_{n,k}-I_{T,k}\le k\zeta(2)4^{k-2}.
\tag{7}
\]
The dependence on dimension has disappeared.

**3. Exact logarithmic integral coefficient and its constant boundary deficit.** Set \(x_r=e^{t_r}\). Since \(\max(a,b)=\tfrac12(a+b+|a-b|)\), the Jacobians cancel the diagonal part of the exponent and yield
\[
I_{T,k}=\int_{[0,T]^k}
\exp\left(-\frac12\sum_{r=1}^k|t_r-t_{r+1}|\right)dt,
\quad t_{k+1}=t_1.
\tag{8}
\]
Anchor \(t_1\), let \(v_1=0\), \(v_r=t_r-t_1\) for \(r\ge2\), and put
\[
V(v)=\sum_{r=1}^k|v_r-v_{r+1}|,
\qquad R(v)=\max_{1\le r\le k}v_r-\min_{1\le r\le k}v_r.
\]
The set of admissible anchors has length \((T-R(v))_+\), so
\[
I_{T,k}=\int_{\mathbb R^{k-1}}e^{-V(v)/2}(T-R(v))_+\,dv.
\tag{9}
\]
On a cyclic path, the two routes between a largest and a smallest coordinate each contribute at least \(R(v)\) to total variation. Thus \(2R(v)\le V(v)\). Consequently, with \(c_k=\int e^{-V/2}dv\),
\[
0\le c_kT-I_{T,k}
=\int e^{-V/2}\min\{T,R(v)\}\,dv
\le\frac12\int V(v)e^{-V(v)/2}dv.
\tag{10}
\]
Because \(V\) is positive homogeneous of degree one and the domain is \(\mathbb R^{k-1}\), scaling gives
\[
\int_{\mathbb R^{k-1}}e^{-aV(v)}\,dv
=(2a)^{-(k-1)}c_k\quad(a>0).
\]
Differentiating at \(a=1/2\), justified by exponential decay from \(V\ge2\max_{r\ge2}|v_r|\), establishes \(\tfrac12\int Ve^{-V/2}dv=(k-1)c_k\). Therefore
\[
c_k(T-k+1)\le I_{T,k}\le c_kT.
\tag{11}
\]

**4. Evaluating the coefficient.** Take \(h(t)=e^{-|t|/2}\), whose Fourier transform under \(\widehat h(\xi)=\int h(t)e^{-i\xi t}dt\) is \((\xi^2+1/4)^{-1}\). The integral defining \(c_k\) is \(k\)-fold convolution \(h^{*k}(0)\). Fourier inversion and the classical gamma integral give
\[
c_k=\frac1{2\pi}\int_{\mathbb R}(\xi^2+1/4)^{-k}d\xi
=\frac{(2k-2)!}{((k-1)!)^2}
=\binom{2k-2}{k-1}.
\tag{12}
\]
The integral converges for all \(k\ge2\); the \(k=1\) identity \(\operatorname{tr}B_n=H_n\) was established separately.

**5. Trace bounds.** Since \(\log(n+1)\le H_n\le\log(n+1)+1\), combine (7) and (11):
\[
-kc_k\le S_{n,k}-c_kH_n\le k\zeta(2)4^{k-2}.
\]
This is (1). The harmonic number diverges, so division by \(H_n\) proves (2). Direct grouping of pairs by their maximum proves the optional exact check
\[
\operatorname{tr}(B_n^2)=\sum_{m=1}^n\frac{2m-1}{m^2}
=2H_n-\sum_{m=1}^n\frac1{m^2}.
\]

**6. Energy-weighted arcsine convergence.** The probability measure (3) is supported on \([0,4]\) by Step 1. For each integer \(m\ge0\), its \(m\)-th moment is
\[
\int x^m\,d\mu_n(x)=\frac{\operatorname{tr}(B_n^{m+1})}{H_n}
\longrightarrow c_{m+1}=\binom{2m}{m}.
\tag{13}
\]
For the density in (4), substitute \(x=4\sin^2\theta\) and apply the beta integral to obtain the same moments \(\binom{2m}{m}\). Polynomials are dense in \(C([0,4])\); compact support then upgrades moment convergence to weak convergence. In particular, for a polynomial \(p(x)=a_0+\sum_{m=1}^M a_mx^m\), (1) supplies the explicit bound
\[
\left|\int p\,d\mu_n-\int p\,d\mu_\infty\right|
\le\frac1{H_n}\sum_{m=1}^M|a_m|(m+1)
\max\left\{\binom{2m}{m},\,\zeta(2)4^{m-1}\right\}.
\tag{14}
\]
This completes the proof.

## Verification

The accompanying standard-library `CHECK.py` computes rational matrices with entries (5), multiplies them exactly, and tests the stated two-sided finite trace bounds for every pair \(1\le n\le10\), \(1\le k\le6\). All 60 computed traces pass. It separately checks the exact fourth-Schatten-moment identity and the combinatorial moment coefficients. These finite checks corroborate arithmetic but are **not** used as a proof of the infinite-dimensional limiting assertion; Steps 1–6 supply that proof. Reproduction: `python CHECK.py` from the directory containing the extracted file.

## Relationship to prior work

The 2011 finite-Cesàro norm discussion explicitly identifies the matrix with entries \(1/\max(i,j)\) and studies its largest singular value and inverse tridiagonal matrix. This does **not** determine asymptotic traces of every fixed power: one spectral edge cannot control a growing aggregate of eigenvalues. Lacruz–León-Saavedra–Petrović–Zabeti (2014), inspected in complete open-access HTML, study extended eigenvalues of discrete and continuous Cesàro operators, not the trace-weighted spectral measures (3). The publicly available *Logarithmic spectral edge of higher singular values of finite Cesàro matrices* studies each fixed singular-value rank in the limit; it does not assert (1), the \(O(1)\) remainder for all Schatten moments, or (4). The 2026 *A discrete Mellin calculus in the Toeplitz algebra* concerns multiplication modulo Hilbert–Schmidt classes in the infinite operator algebra; only its abstract was accessible and an uninspected theorem may overlap. Classical Wiener–Hopf trace asymptotics offer a related analytic framework, but no inspected source states the finite-Cesàro inequalities (1). An incomplete literature search cannot certify worldwide novelty.

## Limitations

The moment bound is exact as to its leading \(H_n\) coefficient, but its additive constants are not claimed sharp for \(k\ge3\). Only fixed integer moments are asymptotically classified; uniformity as the moment order grows is not asserted. The arcsine limit uses Hilbert–Schmidt energy weights, not unweighted eigenvalue counting or the ordinary empirical distribution of singular values. Finite tests are not infinite proofs. Historical publications not retrievable in full, particularly the foundational 1965 Cesàro paper and the 2026 discrete-Mellin preprint, present residual bibliographic overlap risk.

## References

1. A. Brown, P. R. Halmos, A. L. Shields, *Cesàro operators*, Acta Sci. Math. 26 (1965), 125–137. Bibliographic record: https://acta.bibl.u-szeged.hu/14062/ .
2. Suvrit, *Norm of Cesaro matrix*, MathOverflow question 72416, first posted 9 August 2011; includes N. D. Elkies's 11 August 2011 reply: https://mathoverflow.net/questions/72416/norm-of-cesaro-matrix .
3. M. Lacruz, F. León-Saavedra, S. Petrovic, O. Zabeti, *Extended eigenvalues for Cesàro operators*, arXiv:1403.4844v1 (19 March 2014), https://arxiv.org/html/1403.4844v1 .
4. C. Bellavita, G. Stylogiannis, *A discrete Mellin calculus in the Toeplitz algebra*, arXiv:2609.09453v1 (8 September 2026), https://arxiv.org/abs/2609.09453 (abstract consulted).
5. *Logarithmic spectral edge of higher singular values of finite Cesàro matrices*, public research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-logarithmic-spectral-edge-of-higher-singular-values-of-finite-ce--502b7b013a69 (full `RESULT.md` inspected).
