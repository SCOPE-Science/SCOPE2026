# Spectral-power trace cancellation for Dirichlet Bernstein–Durrmeyer operators on simplices

## Finding

For every fixed integer \(d\ge2\), Dirichlet shape vector \(\boldsymbol\theta=(\theta_0,\ldots,\theta_d)\) with all \(\theta_i>0\), and real \(s>0\), put \(A=\sum_{i=0}^{d}\theta_i\). The positive Bernstein–Durrmeyer averaging operator \(M_{n,\boldsymbol\theta}\) on the standard \(d\)-simplex, defined below, has the spectral-power trace
\[
\begin{aligned}
\operatorname{tr}(M_{n,\boldsymbol\theta}^{s})
={}&\frac{\Gamma(d/2)}{2(d-1)!s^{d/2}}\,n^{d/2}\\
&+\frac{(d+1-A)\Gamma((d-1)/2)}{4(d-2)!s^{(d-1)/2}}\,n^{(d-1)/2}
+O_{d,A,s}\!\left(n^{(d-2)/2}\right).
\end{aligned}
\]
In particular, for every dimension, the entire second-order term cancels precisely on the natural hyperplane \(A=d+1\), which includes normalized Lebesgue measure on the simplex. The trace depends on the shape vector only through its sum \(A\).

In dimension \(d=2\), this cancellation extends to a computable finite correction: for every \(A>0\),
\[
\boxed{\displaystyle
\operatorname{tr}(M_{n,\boldsymbol\theta}^{s})
=\frac{n}{2s}+\frac{(3-A)\sqrt{\pi n}}{4\sqrt{s}}
+\frac{3A^2-12A+14}{12}+\frac{A}{4s}-\frac{1}{6s^2}
+O_{A,s}(n^{-1/2}).}
\]
For the critical total shape \(A=3\), two of these trace laws are in fact exact for every integer \(n\ge1\):
\[
\operatorname{tr}(M_{n,\boldsymbol\theta})=\frac{n+2}{2},\qquad
\operatorname{tr}(M_{n,\boldsymbol\theta}^{2})=\frac{(n+2)^2}{4(n+1)}.
\]
The complete dimension-two constant for general real \(s>0\) is \(5/12+3/(4s)-1/(6s^2)\) at \(A=3\).

## Assumptions and scope

Let \(S_d=\{(x_1,\ldots,x_d):x_i\ge0,\ \sum_{i=1}^d x_i\le1\}\), and set \(x_0=1-\sum_{i=1}^d x_i\). The probability law \(\rho_{\boldsymbol\theta}\) has Dirichlet density
\[
\frac{\Gamma(A)}{\prod_{i=0}^{d}\Gamma(\theta_i)}
\prod_{i=0}^{d}x_i^{\theta_i-1}\,dx_1\cdots dx_d.
\]
For a nonnegative integer multi-index \(\beta\) with \(|\beta|=n\), define the Bernstein polynomial \(B_{n,\beta}(x)=\frac{n!}{\prod\beta_i!}\prod x_i^{\beta_i}\). With \(\langle f,g\rangle=\int_{S_d} f\overline g\,d\rho_{\boldsymbol\theta}\), define the finite-rank operator
\[
(M_{n,\boldsymbol\theta}f)(x)
=\sum_{|\beta|=n}B_{n,\beta}(x)
\frac{\langle f,B_{n,\beta}\rangle}{\langle1,B_{n,\beta}\rangle}.
\]
The operator is positive, selfadjoint, and a contraction on \(L^2(\rho_{\boldsymbol\theta})\); its nonzero eigenvalues are positive. Every power \(s>0\) is defined by the finite-dimensional spectral functional calculus, with zero eigenvalues remaining zero. The asymptotics hold as integers \(n\to\infty\) with fixed \(d,A,s\), uniformly for \(A\) and \(s\) in compact subintervals of \((0,\infty)\); no joint growing-dimension claim is made.

## Proof

**Exact eigenspaces.** For a monomial of total degree \(j=u_1+\cdots+u_d\le n\), its Bernstein–Dirichlet posterior average is
\[
\frac{\langle x_1^{u_1}\cdots x_d^{u_d},B_{n,\beta}\rangle}
{\langle1,B_{n,\beta}\rangle}
=\frac{\prod_{i=1}^{d}(\beta_i+\theta_i)_{u_i}}{(n+A)_j},
\]
where parentheses denote rising factorials. Multinomial moments show that the top homogeneous part of its image is \(\frac{(n)_{\underline j}}{(n+A)_j}x_1^{u_1}\cdots x_d^{u_d}\). The integral kernel is symmetric because it is a sum of products \(B_{n,\beta}(x)B_{n,\beta}(y)/\langle1,B_{n,\beta}\rangle\). Consequently selfadjointness and polynomial-degree filtration imply that each orthogonal polynomial degree \(j\) subspace is an eigenspace, with multiplicity \(\binom{j+d-1}{d-1}\) and eigenvalue
\[
\lambda_{n,j}=\prod_{r=0}^{j-1}\frac{n-r}{n+A+r},\qquad 0\le j\le n.
\]
This gives the exact finite identity
\[
T_{n,d,A}(s):=\operatorname{tr}(M_{n,\boldsymbol\theta}^{s})
=\sum_{j=0}^{n}\binom{j+d-1}{d-1}\lambda_{n,j}^{s}.
\]
It also proves the asserted dependence solely on \(A\), without assuming equal Dirichlet parameters.

**Gaussian window and dimension-dependent cancellation.** Put \(h=n^{-1/2}\), \(t=jh\). For each fixed \(A>0\), expansion of the logarithm of the exact product gives, on the Gaussian window,
\[
\log\lambda_{n,j}
=-t^2-(A-1)ht
+h^2\left(\frac A2t^2-\frac16t^4\right)
+O_A\!\left(h^3(1+t)^8\right).
\]
A uniform tail bound follows from \(\log(1-u)\le-u\):
\[
0<\lambda_{n,j}\le
\exp\!\left(-\frac{j^2+(A-1)j}{2n+A}\right)
\quad\text{when}\quad A\ge1.
\]
For arbitrary \(A>0\), replacing the numerator by \(j^2+\min(A-1,0)j\) and taking a sufficiently large constant denominator yields the same Gaussian domination \(\lambda_{n,j}\le C_A\exp(-c_A j^2/n)\); alternatively the first \(\lfloor j/2\rfloor\) factors already give such a bound. Thus contributions from \(j>n^{1/2+1/32}\) are smaller than every power of \(n^{-1}\). Local Taylor remainders, multiplied by the Gaussian majorant, can be summed term by term. In particular,
\[
\lambda_{n,j}^{s}=e^{-st^2}
\left(1-s(A-1)ht+O_{A,s}\!\left(h^2(1+t)^8\right)\right).
\]
For \(d\ge2\), the multiplicity polynomial has its two top terms
\[
\binom{j+d-1}{d-1}
=\frac{j^{d-1}}{(d-1)!}
+\frac{d(d-1)}{2(d-1)!}j^{d-2}+O_d\!\left((1+j)^{d-3}\right).
\]
Euler–Maclaurin summation or a singularity-free half-line Riemann sum produces the two asserted powers of \(n\). The first coefficient is \(\Gamma(d/2)/(2(d-1)!s^{d/2})\). The second combines the multiplicity correction with the \(s(A-1)ht\) term; using \(\Gamma((d+1)/2)=\frac{d-1}{2}\Gamma((d-1)/2)\), it equals \((d+1-A)\Gamma((d-1)/2)/(4(d-2)!s^{(d-1)/2})\). The Gaussian bounds justify the claimed \(O(n^{(d-2)/2})\) remainder. For \(d=2\), retaining one additional order gives the stronger formula below.

**Exact dimension-two constant.** For \(d=2\), the multiplicity is exactly \(j+1\), and a second-order expansion is
\[
\begin{aligned}
\lambda_{n,j}^{s}=e^{-st^2}\bigg[1-s(A-1)ht
+h^2\bigg(\Big(\frac{sA}{2}+\frac{s^2(A-1)^2}{2}\Big)t^2-\frac{s}{6}t^4\bigg)\bigg]
+O_{A,s}\!\left(h^3(1+t)^{12}e^{-c_st^2}\right).
\end{aligned}
\]
Write \(a(t)=-s(A-1)t\) and \(b(t)=\left(sA/2+s^2(A-1)^2/2\right)t^2-st^4/6\). After multiplying by \(j+1=t/h+1\) and summing, the constant correction contains \(-1/12\) from the Euler–Maclaurin derivative of \(te^{-st^2}\), \(+1/2\) from the endpoint of \(e^{-st^2}\), and the integrals \(\int_0^\infty e^{-st^2}a(t)\,dt\) and \(\int_0^\infty te^{-st^2}b(t)\,dt\). Their sum is
\[
\frac5{12}-\frac{A-1}{2}+\frac{A}{4s}
+\frac{(A-1)^2}{4}-\frac{1}{6s^2}
=\frac{3A^2-12A+14}{12}+\frac{A}{4s}-\frac{1}{6s^2}.
\]
The integrated Gaussian-weighted remainder is \(O_{A,s}(h)\); the same half-line Euler–Maclaurin formula gives \(O(h)\) for all omitted endpoint terms. This proves the refined expansion.

**Two finite exact identities.** If \(A=3\), set \(N=2n+2\) and \(c_k=\binom Nk\). The product above simplifies to \(\lambda_{n,j}=c_{n-j}/c_n\). Thus
\[
T_{n,2,3}(s)=c_n^{-s}\sum_{k=0}^{n}(n+1-k)c_k^s.
\]
For \(s=1\), the elementary telescoping identity \((N/2-k)c_k=(N/2)(\binom{N-1}{k}-\binom{N-1}{k-1})\) yields \(T_{n,2,3}(1)=(n+2)/2\). For \(s=2\), the telescoping identity
\[
(N/2-k)c_k^2
=\frac{(k+1)^2c_{k+1}^2-k^2c_k^2}{2N}
\]
yields \(T_{n,2,3}(2)=(n+2)^2/(4(n+1))\). Both hold for every \(n\ge1\).

## Verification

The standalone `VERIFY.py` reconstructs the finite Bernstein–Dirichlet Gram matrices using gamma-function integrals, independently checks their eigenvalues against all theoretical multiplicities, checks both critical rational trace identities with exact fractions, and compares spectral sums with the asymptotic expansions across multiple shapes, powers, and dimensions. Running `python VERIFY.py` produced `VERIFIED 148 independent checks: Gram spectra, rational traces, asymptotic refinements`. The finite checks are cross-checks only; the infinite limiting assertions follow from the product expansion, Gaussian majorization, and Euler–Maclaurin argument above.

## Relationship to prior work

The multivariate Bernstein–Durrmeyer eigenvalues and degree multiplicities are classical, and are explicitly described in E. E. Berdysheva and K. Jetter (2010, §3.2.2). Wang, Yang, and Duan (2011) analyze approximation orders on simplices, and Abel and Berdysheva (2010) study fixed-function differential asymptotic expansions using spectral properties. A later composition-kernel identity of Abel, Acu, Heilmann, and Raşa (2025) gives complementary finite-operator formulas. These are acknowledged ingredients; the stated result concerns **growing-rank traces of arbitrary real spectral powers**, the uniform dimension-dependent cancellation, and an explicit triangular order-one term. Fixed-function operator asymptotics alone do not provide uniform control of the growing polynomial eigenspaces needed for these traces. Complete bibliographic priority is not established.

## Limitations

The method requires fixed dimension and strictly positive Dirichlet parameters and power. It supplies only the displayed two-term expansion in arbitrary dimension, and the order-one refinement only in dimension two; no claims about negative powers, nonsymmetric weights, growing dimension, or non-Dirichlet measures are made. The eigenvalue formula itself is previously known. Some plausible historical primary text, particularly Abel–Berdysheva (2010), could not be fully inspected; an equivalent historical trace asymptotic cannot be ruled out. The accompanying finite computations do not constitute an independent proof of the asymptotic limit.

## References

1. E. E. Berdysheva and K. Jetter, *Multivariate Bernstein–Durrmeyer operators with arbitrary weight functions*, Journal of Approximation Theory 162 (2010), 576–598, DOI: 10.1016/j.jat.2009.11.005. Available online 22 November 2009; see §3.2.2 for the known eigenvalues and multiplicities.
2. U. Abel and E. E. Berdysheva, *Complete asymptotic expansion for multivariate Bernstein–Durrmeyer operators and quasi-interpolants*, Journal of Approximation Theory 162 (2010), 201–220, DOI: 10.1016/j.jat.2009.04.004.
3. J. Wang, C.-Y. Yang, and S. Duan, *Approximation Order for Multivariate Durrmeyer Operators with Jacobi Weights*, Abstract and Applied Analysis (2011), article 970659, DOI: 10.1155/2011/970659.
4. U. Abel, A. M. Acu, M. Heilmann, and I. Raşa, *A representation for the integral kernel of the composition of multivariate Bernstein–Durrmeyer operators*, arXiv:2512.17297 (19 December 2025).
