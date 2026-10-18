# Odd-grid completeness and even-grid obstruction for finite Gaussian spectrogram tomography

## Finding
Let \(m\ge 2\) be an integer and let \(X=\{x_1,\ldots,x_m\}\) and \(Y=\{y_1,\ldots,y_m\}\) be arbitrary sets of \(m\) pairwise distinct real numbers each. For \(z\in\mathbb C\) set
\[
v_m(z)=(1,z,\ldots,z^{m-1})^{\mathsf T}.
\]
Consider the real-linear map on Hermitian \(m\)-by-\(m\) matrices
\[
\mathcal T_{X,Y}(H)=\big(v_m(x+iy)^*H v_m(x+iy)\big)_{(x,y)\in X\times Y}\in\mathbb R^{m^2}.
\]
**Theorem.** For every choice of distinct nodes as above, \(\mathcal T_{X,Y}\) is bijective **if and only if \(m\) is odd**. For even \(m\), write the real monic polynomials
\[
p_X(u)=\prod_{x\in X}(u-x),\qquad p_Y(u)=\prod_{y\in Y}(u-y).
\]
The explicit nonzero real polynomial
\[
Q(z,\bar z)=p_X(\operatorname{Re}z)-(-1)^{m/2}p_Y(\operatorname{Im}z)
\]
is of bidegree at most \((m-1,m-1)\) in \((z,\bar z)\), and is therefore represented by a nonzero Hermitian kernel matrix \(H_Q\) satisfying \(\mathcal T_{X,Y}(H_Q)=0\).

In particular, for odd \(m\), the \(m^2\) magnitudes of any holomorphic polynomial \(P\) of degree at most \(m-1\), measured at \(X+iY\), determine \(P\) up to one unimodular scalar. Multiplying the intensity at each node by any known positive weight, such as the Gaussian spectrogram factor, does not change the assertion. The even-\(m\) statement concerns **Hermitian lifting**; it does *not* assert a phase-retrieval ambiguity between two pure polynomial signals for every even \(m\).

## Assumptions and scope
All nodes are real, distinct within their own coordinate set, and arbitrary otherwise; the two sets may have different spacing and need not be symmetric or equally spaced. The matrix space is all Hermitian matrices, not just rank-one projectors. No quantitative lower bound uniform over near-colliding grids is asserted. Gaussian STFT sampling is invoked only through the standard Bargmann representation in which the spectrogram of a truncated Hermite signal equals a known positive Gaussian factor times \(|P(z)|^2\), up to scaling of \(z\). Thus the theorem is a precise finite-dimensional statement about unweighted evaluation as defined above.

## Proof
Write \(n=m-1\), \(z=x+iy\), and \(w=x-iy\). The complexification of the Hermitian polynomial space is
\[
\mathcal V_n=\operatorname{span}_{\mathbb C}\{z^j w^k:0\le j,k\le n\},\quad \dim_{\mathbb C}\mathcal V_n=m^2.
\]
Real-valued members of \(\mathcal V_n\) correspond uniquely to Hermitian coefficient matrices. It suffices to study point evaluation of \(\mathcal V_n\) at \(X\times Y\).

**Even \(m\).** The leading homogeneous part of \(p_X(x)-(-1)^{m/2}p_Y(y)\) is \(x^m-(-1)^{m/2}y^m\). In the coordinates \(z,w\), the coefficients of \(z^m\) and \(w^m\) both vanish, since \(i^{-m}=(-1)^{m/2}\). Every remaining monomial in degree \(m\) has exponents in \(\{1,\ldots,m-1\}\); the lower-degree terms have total degree at most \(m-1\). Hence the displayed polynomial lies in \(\mathcal V_{m-1}\). It is nonzero, real-valued, and vanishes on \(X\times Y\), proving singularity.

**Odd \(m\).** We prove that no nonzero \(Q\in\mathcal V_n\) vanishes on \(X\times Y\). Let \(d\) be its total degree. If \(d\le n\), for each fixed \(y\in Y\) the polynomial \(x\mapsto Q(x,y)\) has degree at most \(n\) and vanishes at all \(m=n+1\) elements of \(X\), hence is identically zero; applying the same argument to its coefficients as polynomials in \(y\) gives \(Q=0\), a contradiction.

Suppose instead \(n+1\le d\le 2n\), and write \(d=n+r\) with \(1\le r\le n\). Because \(Q\in\mathcal V_n\), its leading homogeneous part is necessarily
\[
H_d(x,y)=(x^2+y^2)^r P(x,y),
\]
where \(P\) is homogeneous of degree \(n-r=k-1\), with \(k=m-r\). Indeed every top-degree monomial \(z^j w^{d-j}\) has both exponents at least \(r\).

Since \(Q\) vanishes on the Cartesian grid, polynomial division by the two monic node polynomials gives \(Q=p_X(x)A(x,y)+p_Y(y)B(x,y)\): divide first in \(x\), then note that every coefficient of the remainder vanishes at all nodes of \(Y\). The top homogeneous form therefore belongs to the monomial ideal \((x^m,y^m)\). Equivalently, the coefficients in \(H_d\) of all the \(k\) monomials
\[
x^{r+h}y^{r+k-1-h},\qquad h=0,\ldots,k-1,
\]
are zero: their two exponents are strictly below \(m\).

Write \(P=\sum_{s=0}^{k-1}c_s x^s y^{k-1-s}\). The \(k\) conditions just obtained are \(B_{r,k}c=0\), where the matrix, indexed by \(0\le h,s<k\), is
\[
(B_{r,k})_{hs}=\begin{cases}
\binom{r}{(r+h-s)/2},&r+h-s\text{ is even and }0\le(r+h-s)/2\le r,\\
0,&\text{otherwise}.
\end{cases}
\]
We show that \(B_{r,k}\) is invertible whenever \(m\) is odd (hence \(r+k=m\) is odd).

If \(r=2q\), its two parity blocks have entries \(\binom{2q}{q+u-v}\). Such a Toeplitz matrix is positive definite, because for any nonzero coefficient vector \(c\), its quadratic form, with one of the two harmless Fourier-index conventions, equals
\[
\frac1{2\pi}\int_0^{2\pi}|1+e^{it}|^{2q}\left|\sum_v c_v e^{ivt}\right|^2dt>0.
\]
This includes \(q=0\), when the block is the identity.

If \(r=2q+1\), then \(k\) is even. Permuting rows and columns by parity makes \(B_{r,k}\) off-diagonal, with two square blocks that are transposes of one another. One is the Toeplitz matrix \(T\) with entries \(\binom{2q+1}{q+u-v}\). It is strictly accretive: its quadratic form is the Fourier integral with symbol \((1+e^{it})|1+e^{it}|^{2q}\), whose real part is \((1+\cos t)|1+e^{it}|^{2q}>0\) almost everywhere. Thus \(T\) and its transpose are both nonsingular.

In both cases \(B_{r,k}c=0\) forces \(P=0\), contradicting the definition of the leading homogeneous part. Therefore evaluation on \(\mathcal V_n\) is injective. Its domain and codomain both have complex dimension \(m^2\), so it is bijective. Restricting to Hermitian matrices yields a bijection of real spaces of the same dimension.

Finally, if \(|P_1|^2=|P_2|^2\) at every grid point for odd \(m\), the Hermitian matrices formed from their coefficient outer products have identical evaluations and hence coincide. Two vectors with the same rank-one outer product differ by a unimodular scalar (with the zero-vector case immediate). This proves the stated pure-signal consequence.

## Verification
The companion program `check_cartesian.py` constructs the Hermitian intensity evaluation matrix over the finite field of order \(1009\), and computes its rank by modular Gaussian elimination, for two different families of distinct Cartesian nodes and each \(m=2,\ldots,10\). In every case odd orders have full rank; even orders have an observed nullity \(m/2\), which is **not** claimed as a theorem here. For each order and each \(1\le r<m\), the program separately verifies the predicted ranks of the middle-coefficient matrices \(B_{r,m-r}\). Its exact output is `check_output.txt`. All of the infinite family is proved analytically above; testing finitely many orders is not a substitute for that proof.

Reproduce with `python3 check_cartesian.py` in a Python environment with only the standard library. The only modulus is the prime \(1009\), and the deliberately different node families are specified in the program. Modular nonzero determinants establish exact rank for those particular grids, not for arbitrary real grids; the analytic argument supplies universality.

## Relationship to prior work
De Dios Pont, Greilhuber, Liehr and Taylor (arXiv:2609.28341, first posted September 23, 2026) give discrete point-set uniqueness for full STFT phase retrieval with Gaussian-polynomial windows; their accessible abstract addresses existence of an infinite uniformly discrete sampling set, rather than a parity-dependent **square finite Cartesian-grid Hermitian tomography** criterion. Its full text was inaccessible in the present literature inspection, so an unnoticed related lemma remains a priority risk.

Abreu, Luef and Ziyat (2025) establish Gabor-frame and polyanalytic Fock sampling/interpolation results on the flat cylinder; their full-text sections on sampling, interpolation, and the explicit remark that the paper does not directly study phase retrieval were examined. Grohs and Liehr (2024, first published 2023) prove stable reconstruction for Gaussian shift-invariant spaces, including approximation from finite spectrogram grids; their finite grids are approximation instruments for an infinite function space, not exactly \(m^2\) coherent-state projectors on the first \(m\) Hermite modes. The rank-versus-pure-state distinction is essential: full Hermitian tomography is a stronger requirement than ordinary phase retrieval.

## Limitations
The theorem supplies no uniform condition-number bound: approaching colliding nodes can make invertible odd-grid matrices arbitrarily ill-conditioned. Even-grid singularity is established for the real-linear Hermitian lift, not for the nonlinear pure-state map in every dimension. No assertion is made about rectangular grids of unequal cardinalities, non-Cartesian sampling, all of Fock space, or optimal placement of nodes. Historical priority beyond the inspected indexed literature cannot be ruled out, especially because the complete September 2026 manuscript could not be read.

## References
1. J. de Dios Pont, J. Greilhuber, L. Liehr, M. A. Taylor, *Phase retrieval from a uniformly discrete point set*, arXiv:2609.28341v1 (2026-09-23), https://arxiv.org/abs/2609.28341.
2. L. D. Abreu, F. Luef, M. Ziyat, *Gabor Frames for Quasi-Periodic Functions and Polyanalytic Spaces on the Flat Cylinder*, J. Fourier Anal. Appl. 31 (2025), article 68, https://doi.org/10.1007/s00041-025-10196-1.
3. P. Grohs, L. Liehr, *Stable Gabor Phase Retrieval in Gaussian Shift-Invariant Spaces via Biorthogonality*, Constructive Approximation 59 (2024), 61–111, first published October 4, 2023, https://doi.org/10.1007/s00365-023-09629-1.
4. P. Grohs, L. Liehr, M. Rathmair, *Phase retrieval in Fock space and perturbation of Liouville sets*, Rev. Mat. Iberoam. 41 (2025), 969–1008, https://doi.org/10.4171/RMI/1517 (abstract compared, not inspected in full).
