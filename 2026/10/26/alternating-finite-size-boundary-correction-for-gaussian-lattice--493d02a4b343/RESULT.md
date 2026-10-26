# Alternating finite-size boundary correction for Gaussian lattice interpolation

## Finding
For every fixed real \(0<p<1\), let \(G_N(p)=(p^{(j-k)^2})_{0\le j,k<N}\), \(u_N=(1,\ldots,1)^\mathsf T\), and \(E_N(p)=u_N^\mathsf T G_N(p)^{-1}u_N\). The theta bulk factor is
\[
\Theta(p)=\sum_{k\in\mathbb Z}p^{k^2}=\prod_{j\ge1}(1-p^{2j})(1+p^{2j-1})^2>0.
\]
There is a finite explicit edge constant \(C(p)\) such that, as \(N\to\infty\),
\[
\boxed{E_N(p)=\frac{N}{\Theta(p)}+C(p)-\frac{2p}{(1+p)^2\Theta(p)}(-p)^N+O_p(p^{2N}).}
\]
The coefficient of the alternating correction is strictly nonzero for every \(0<p<1\). In particular the normalized residual obeys
\[
\lim_{N\to\infty}\frac{E_N(p)-N/\Theta(p)-C(p)}{(-p)^N}=-\frac{2p}{(1+p)^2\Theta(p)}.
\]
The finite-size correction therefore alternates in sign for all sufficiently large \(N\); an estimate merely giving an unspecified exponentially small remainder misses its exact phase and rate.

Put \(q=p^2\), \((q;q)_n=\prod_{j=1}^n(1-q^j)\), \((q;q)_0=1\), and
\[
{n\brack j}_q=\frac{(q;q)_n}{(q;q)_j(q;q)_{n-j}},\qquad R_n(p)=\sum_{j=0}^n(-p)^j{n\brack j}_q.
\]
Then for every integer \(N\ge1\) the exact interpolation energy and the edge constant are
\[
E_N(p)=\sum_{n=0}^{N-1}\frac{R_n(p)^2}{(q;q)_n},\qquad
C(p)=\sum_{n=0}^{\infty}\left(\frac{R_n(p)^2}{(q;q)_n}-\frac1{\Theta(p)}\right).
\]
The series for \(C(p)\) converges absolutely.

## Assumptions and scope
The stationary Gaussian kernel is \(K_p(x,y)=p^{(x-y)^2}\) on \(\mathbb R\); its restriction to the consecutive integer locations \(0,1,\ldots,N-1\) has Gram matrix \(G_N(p)\). Every \(G_N(p)\) is strictly positive definite. The minimum squared reproducing-kernel Hilbert space norm over functions satisfying \(f(j)=1\) at these integer sites is precisely \(E_N(p)\). The theorem concerns this fixed-spacing, fixed-parameter limit; no uniformity is asserted as \(p\downarrow0\) or \(p\uparrow1\).

## Proof
**1. Fourier positivity and the interpolation interpretation.** The Jacobi triple-product identity gives the strictly positive circle density
\[
w_p(\theta)=\sum_{k\in\mathbb Z}p^{k^2}e^{ik\theta}
=\prod_{m\ge1}(1-p^{2m})\big|1+p^{2m-1}e^{i\theta}\big|^2.
\]
Its Fourier moments are \(p^{k^2}\). Thus the Gram matrix of the monomials \(1,z,\ldots,z^{N-1}\) in \(L^2(w_p(\theta)d\theta/(2\pi))\) is \(G_N(p)\). The squared norm of evaluation of these polynomials at \(z=1\) equals \(u_N^\mathsf T G_N^{-1}u_N\). By the representer theorem the same quantity is the minimum squared RKHS norm of a Gaussian-kernel interpolant of the constant data \(1\).

**2. Explicit orthogonal polynomials.** Define
\[
P_n(z)=\sum_{k=0}^n(-1)^{n-k}p^{n-k}{n\brack k}_{p^2}z^k.
\]
These are monic. For each integer \(0\le j<n\), the moment inner product is
\[
\langle P_n,z^j\rangle
=p^{n+j^2}(-1)^n\sum_{k=0}^n(-1)^k(p^{-1-2j})^k{n\brack k}_{p^2}p^{k^2}
=(-1)^np^{n+j^2}(p^{-2j};p^2)_n=0,
\]
where the finite \(q\)-binomial identity is used in the last step. [Equivalently, the polynomial \(\sum_k [z^k]P_n\,p^{k^2}t^k=(-1)^np^n(t;p^2)_n\) vanishes at \(t=p^{-2j}\).] Since the polynomial is monic and orthogonal to lower degrees, its squared norm equals \(\langle P_n,z^n\rangle\), namely
\[
\|P_n\|^2=\sum_{j=0}^n(-1)^jp^{j(j+1)}{n\brack j}_{p^2}=(p^2;p^2)_n.
\]
Further, \(P_n(1)=R_n(p)\), by reversing the summation index. Resolving point evaluation into this orthogonal basis proves the exact identity for \(E_N(p)\).

**3. Meromorphic coefficient asymptotics.** By the ordinary \(q\)-binomial generating function, for sufficiently small \(|t|\),
\[
F_p(t):=\sum_{n\ge0}\frac{R_n(p)}{(q;q)_n}t^n
=\frac1{(t;q)_\infty(-pt;q)_\infty}.
\]
The first three poles in order of modulus are simple, at \(t=1\), \(t=-p^{-1}\), and \(t=p^{-2}\). The residues in the normalized forms \(A_0/(1-t)\) and \(A_1/(1+pt)\) are
\[
A_0=\frac1{(q;q)_\infty(-p;q)_\infty},\qquad
A_1=\frac{p}{1+p}A_0.
\]
Subtract these two principal parts and also the principal part at \(t=p^{-2}\). The remainder is holomorphic on a disk of radius strictly exceeding \(p^{-2}\), because the next pole has modulus \(p^{-3}\). Cauchy's coefficient estimate therefore yields
\[
\frac{R_n(p)}{(q;q)_n}=A_0+A_1(-p)^n+O_p(p^{2n}),
\]
where the third pole itself contributes \(O_p(p^{2n})\). Since \((q;q)_n=(q;q)_\infty(1+O_p(p^{2n}))\), writing \(U=(-p;p^2)_\infty^{-1}\), we obtain
\[
R_n(p)=U\left(1+\frac{p}{1+p}(-p)^n+O_p(p^{2n})\right).
\]

**4. Extracting the sharp boundary term.** Triple-product factorization at \(\theta=0\) gives \(U^2/(q;q)_\infty=1/\Theta(p)\). Squaring the preceding expansion and dividing by the norm yields
\[
\frac{R_n(p)^2}{(q;q)_n}=\frac1{\Theta(p)}\left(1+\frac{2p}{1+p}(-p)^n+O_p(p^{2n})\right).
\]
Consequently the defining series for \(C(p)\) is absolutely convergent. The tail removed by truncation at \(n=N\) is
\[
\sum_{n=N}^\infty\left(\frac{R_n(p)^2}{(q;q)_n}-\frac1{\Theta(p)}\right)
=\frac{2p}{(1+p)^2\Theta(p)}(-p)^N+O_p(p^{2N}),
\]
by summing the two geometric bounds. Since \(E_N-N/\Theta\) is the partial sum of these differences, subtracting this tail proves the asserted expansion and its nonvanishing signed leading coefficient.

## Verification
The standalone `check.py` implements exact rational-arithmetic Gaussian elimination for the Gram matrix, exact \(q\)-binomial coefficients and polynomial orthogonality, and compares both computations of \(E_N\). High-precision decimal tests additionally check the predicted first-pole coefficient and signed finite-size remainder for several values of \(p\). Run `python3 check.py`; its actual output is preserved in `check-output.txt`. Finite checks corroborate algebra; the above pole and Fourier arguments prove the infinite-parameter theorem.

## Relationship to prior work
The polynomial family and its theta-function weight belong to classical Rogers–Szegő/orthogonal-polynomial theory; the finite-dimensional Christoffel identity is standard. Gover (1991) studies inverse formulas for the same type of Gaussian Toeplitz matrices, and Böttcher (2022) develops general large-matrix inverse-entry asymptotics. Karvonen (2021) treats Gaussian kernels and absence of global polynomial functions in translation-invariant RKHSs. The claim here is the explicit, nonzero alternating \((-p)^N\) correction to the minimum constant-data interpolation energy, with an absolutely convergent edge constant and smaller \(O_p(p^{2N})\) remainder. It is not a claim of novelty for basic inversion, Rogers–Szegő polynomials, or the leading bulk term.

## Limitations
All asymptotic constants and big-O bounds may depend on the fixed parameter \(p\). The result is for consecutive equally spaced sites and identical unit target values. It does not quantify condition numbers, solve arbitrary interpolation data, or prove priority over all earlier Gaussian-Toeplitz literature. The full text of Gover's 1991 paper could not be inspected; its published abstract supports inverse recurrences, not a stated parity-sensitive boundary law. A more general result could conceivably imply this specialization. Independent review remains unperformed.

## References
1. T. Karvonen, *Bumps and polynomials in RKHSs of translation-invariant kernels*, arXiv:2102.10628 (original public preprint dated 2021-02-21), https://arxiv.org/abs/2102.10628.
2. A. Böttcher, *Entries of the inverses of large positive definite Toeplitz matrices*, Acta Sci. Math. 88 (2022), 85–99, https://doi.org/10.1007/s44146-022-00007-0.
3. M. J. C. Gover, *Properties of the Inverse of the Gaussian Matrix*, SIAM J. Matrix Anal. Appl. 12 (1991), 541–548, https://doi.org/10.1137/0612039.
4. NIST Digital Library of Mathematical Functions, §18.33, *Polynomials Orthogonal on the Unit Circle*, https://dlmf.nist.gov/18.33.
5. G. Szegő, *Orthogonal Polynomials*, 4th ed., American Mathematical Society (1975), cited for classical theta-weight polynomial machinery.
