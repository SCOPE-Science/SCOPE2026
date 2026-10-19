# Exact coordinate-correlation spectrum and dimension-delayed sign reversal for the twisted baker map

## Finding
For the twisted baker map in every dimension \(M\geq2\) and normalized Lebesgue stationary measure \(m\), the entire infinite matrix of two-time coordinate covariances is determined exactly by powers of an explicit \(M\)-by-\(M\) rational matrix \(B_M\). The centered first-coordinate autocovariance \(C_M(n)\) has rational generating function
\[
\boxed{\sum_{n\geq0}C_M(n)z^n=\frac{(1-z/2)^{M-1}}{3\big[(1-z/4)(1-z/2)^{M-1}+z^M/2^{M+1}\big]}.}
\]
Its sign changes for the first time **at exactly the ambient dimension**:
\[
\boxed{C_M(n)=\frac{1}{3\cdot4^n}>0\quad(0\leq n<M),\qquad C_M(M)=\frac13\left(4^{-M}-2^{-(M+1)}\right)<0.}
\]
The transfer matrix has characteristic polynomial
\[
\boxed{\det(\lambda I-B_M)=(\lambda-1/4)(\lambda-1/2)^{M-1}+2^{-(M+1)}.}
\]
The exact exponential autocovariance rate \(\rho_M=\limsup_{n\to\infty}|C_M(n)|^{1/n}\) lies in \((0,1)\), equals the maximum modulus of the roots of this polynomial, and tends to \(1\) as \(M\to\infty\). More quantitatively, there is a pair of roots satisfying
\[
|\lambda_M|=1-\frac{\log3}{2M}+O(M^{-2}).
\]
This exhibits dimension-dependent slowing of a natural geometric correlation despite measure-theoretic Bernoulli mixing in each fixed dimension.

## Assumptions and scope
For an integer \(M\geq2\), let \(X=[-1,1]\times[0,1]^{M-1}\) and define
\[
F(x_1,\ldots,x_M)=
\begin{cases}
(1+2x_1,x_2,\ldots,x_M),&x_1<0,\\
(1-2x_M,x_1,\ldots,x_{M-1}),&x_1\geq0.
\end{cases}
\]
Let \(m\) be the normalized \(M\)-dimensional Lebesgue probability on \(X\). The two inverse branches on \(X\) have constant Jacobian determinant magnitude \(1/2\), proving that \(m\) is invariant. The centered coordinate observables are \(\xi_1(x)=x_1\) and \(\xi_j(x)=x_j-1/2\) for \(2\leq j\leq M\). Write
\[
C_{ij}(n)=\int_X\xi_i(x)\xi_j(F^nx)\,dm(x),\qquad C_M(n)=C_{11}(n).
\]
The matrix \(B_M\) has nonzero entries, for \(M\geq2\),
\[
(B_M)_{1,1}=1/4,\quad(B_M)_{1,2}=1/2,\quad
(B_M)_{i,i}=(B_M)_{i,i+1}=1/2\ (2\leq i<M),
\]
\[
(B_M)_{M,1}=-1/4,\qquad(B_M)_{M,M}=1/2,
\]
with all unlisted entries zero. For \(M=2\) the first and last rows are distinct, so the displayed assignments remain unambiguous.

## Proof
**1. Transfer closure.** The inverse branches and their probabilities under \(m\) are
\[
G_L(y)=((y_1-1)/2,y_2,\ldots,y_M),\qquad
G_R(y)=(y_2,\ldots,y_M,(1-y_1)/2).
\]
Since both branches cover \(X\) and have volume contraction \(1/2\), the Perron–Frobenius operator on densities or observables is
\[
(P\varphi)(y)=\tfrac12\varphi(G_Ly)+\tfrac12\varphi(G_Ry).
\]
Evaluating the \(M\) centered coordinate functions on the two inverse branches gives the exact vector identity \(P\xi=B_M\xi\), with no constant term. Induction yields \(P^n\xi=B_M^n\xi\) for every integer \(n\geq0\).

**2. Entire covariance matrix.** For any integrable \(u\) and bounded \(v\), change of variables on the two full branches gives \(\int u(x)v(F^nx)\,dm(x)=\int (P^nu)(y)v(y)\,dm(y)\). Independence of the coordinates under \(m\) yields
\[
\int\xi_j\xi_k\,dm=v_j\mathbf1_{j=k},\qquad v_1=1/3,\qquad v_j=1/12\ (j\geq2).
\]
Consequently
\[
\boxed{C_{ij}(n)=v_j(B_M^n)_{ij}\quad(i,j=1,\ldots,M;\ n\geq0).}
\]

**3. Exact resolvent.** The matrix \(I-zB_M\) is upper bidiagonal apart from its lower-left entry \(z/4\). Its determinant is
\[
D_M(z)=(1-z/4)(1-z/2)^{M-1}+z^M/2^{M+1}.
\]
Deleting row and column one leaves an upper-triangular matrix with diagonal \(1-z/2\). Cramer's rule therefore yields \([(I-zB_M)^{-1}]_{11}=(1-z/2)^{M-1}/D_M(z)\). Multiplying by \(v_1=1/3\) proves the generating function and the displayed characteristic polynomial.

**4. Sharp first sign reversal.** Factoring \((1-z/2)^{M-1}\) from the denominator shows that its first-coordinate resolvent is
\[
\frac{1}{1-z/4+z^M/[2^{M+1}(1-z/2)^{M-1}]}.
\]
Formal power-series expansion therefore agrees with \((1-z/4)^{-1}\) through degree \(M-1\), and at degree \(M\) first acquires the correction \(-2^{-(M+1)}\). Since \(2^{M-1}>1\) for \(M\geq2\), the corrected coefficient is negative. No numerical asymptotic argument is involved.

**5. Exact rate and dimensional slowdown.** The characteristic roots satisfy
\[
(4\lambda-1)(2\lambda-1)^{M-1}=-1.
\]
No root has modulus at least one, because \(|4\lambda-1|\geq3\) and \(|2\lambda-1|\geq1\) there. Moreover the numerator \((1-z/2)^{M-1}\) has no common root with \(D_M(z)\), since \(D_M(2)=1/2\). Thus every nonzero characteristic root is a genuine pole of the covariance generating function, with no cancellation. Cauchy–Hadamard gives \(\rho_M=\max\{|\lambda|:\lambda\in\operatorname{spec}B_M\}<1\).

To prove dimension slowdown, put \(h=1/M\), \(s=2\lambda-1=e^{hw}\). The characteristic equation becomes
\[
(2e^{hw}+1)e^{(1-h)w}+1=0.
\]
At \(h=0\) it has the simple complex root \(w_0=-\log3+i\pi\), because its derivative in \(w\) is \(-1\). The analytic implicit-function theorem produces a root \(w(h)=w_0+O(h)\) for all sufficiently small positive \(h\). Therefore \(\lambda=(1+e^{h w(h)})/2=1+w_0/(2M)+O(M^{-2})\), whose modulus is \(1-(\log3)/(2M)+O(M^{-2})\). The spectral radius is at least this modulus and strictly below one, so \(\rho_M\to1\). This does not claim that the displayed root always has maximal modulus, nor assert the sharp \(1/M\) coefficient for \(\rho_M\).

For the concrete two-dimensional case, the eigenvalues are \((3\pm i\sqrt7)/8\) and one obtains the explicit closed form
\[
C_2(n)=\frac{2^{-n}}{3}\left(\cos(n\phi)-\frac{\sin(n\phi)}{\sqrt7}\right),\quad\phi=\arccos(3/4).
\]

## Verification
The standalone standard-library program `verify_twisted_baker_affine.py` constructs the exact rational transfer matrices and checks their full affine branch action. It compares inverse-word enumerations, finite rational resolvent coefficients, determinants and the earliest sign reversal for dimensions \(2\leq M\leq8\), plus planar closed-form diagnostics. Run `python verify_twisted_baker_affine.py`; expected output begins `PASS: 3483 exact-rational identities / finite floating diagnostics`. The all-dimensional claims, absence of pole cancellation and complex root asymptotics follow from the proof, not the finite computation.

## Relationship to prior work
Saiki, Takahasi and Yorke introduced the map, established Lebesgue invariance and a Bernoulli coding, and proved qualitative mixing (Theorem D). Their spectral results concern Jacobians of *forward periodic-orbit derivatives*, not the finite-dimensional Perron–Frobenius action on centered coordinates. A separate published exact-real-spectrum classification also concerns those forward periodic Jacobians and does not imply the averaged inverse-branch covariance resolvent. The new statement is specifically the complete coordinate covariance matrix, rational generating function, first negative lag exactly equal to dimension and nonuniform dimensional affine mixing rate. Classical transfer-operator and Cauchy–Hadamard techniques are used as tools, not claimed as new methods.

## Limitations
The result is restricted to the given piecewise-affine map, the normalized Lebesgue stationary law and coordinate-linear observables. It does not give a uniform mixing rate for all measurable or smooth observables, a full infinite-dimensional transfer-operator spectrum, or the precise first-order coefficient of the maximal spectral radius as dimension tends to infinity. The result is not an independence or cryptographic statement. Independent historical priority assessment could uncover a general transfer-theoretic statement that subsumes the calculation; a failed title or keyword search is not evidence of novelty by itself.

## References
1. Y. Saiki, H. Takahasi and J. A. Yorke, *The twisted baker map*, arXiv:2202.04304, first public preprint 9 February 2022; revised 13 January 2023; journal DOI 10.1088/1361-6544/acb4d3. Original map: Section 1; invariant Lebesgue measure: Section 1; Theorem D and Section 3: mixing and Bernoulli isomorphism.
2. *Exact real-spectrum residue law for the twisted baker map*, published mathematical note available through https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-real-spectrum-residue-law-for-the-twisted-baker-map--f1bd1c74fb3b (forward periodic derivative-spectral classification, not transfer covariances).
