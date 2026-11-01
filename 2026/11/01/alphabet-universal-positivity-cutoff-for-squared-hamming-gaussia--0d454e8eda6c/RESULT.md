# Alphabet-universal positivity cutoff for squared-Hamming Gaussian kernels

## Finding
Let \(s\ge2\) and \(n\ge2\) be arbitrary integers. On the full Hamming product \(X=\{0,1,\ldots,s-1\}^n\), let \(h(x,y)=|\{i:x_i\ne y_i\}|\). For \(0\le u\le1\), define \(K_u(x,y)=u^{h(x,y)^2}\), with \(0^0=1\). Define
\[
B_n(u)=\sum_{k=0}^{n}(-1)^k\binom nk u^{k^2}.
\]
For every \(n\ge2\), there is a uniquely specified number \(\rho_n\) with \(1/n<\rho_n<1/(n-1)\) (with the upper bound \(1\) when \(n=2\)) satisfying \(B_n(\rho_n)=0\). The numbers \(\rho_n\) decrease strictly with \(n\). Then, **independently of the alphabet size**,
\[
K_u\succeq0\quad\Longleftrightarrow\quad u\in[0,\rho_n]\cup\{1\}.
\]
For \(0\le u<\rho_n\), the matrix is strictly positive definite of rank \(s^n\). At \(u=\rho_n\), it is positive semidefinite of rank \(s^n-(s-1)^n\), and its kernel is exactly the top nontrivial-character Fourier sector of dimension \((s-1)^n\). For \(\rho_n<u<1\), it is indefinite. At \(u=1\), it has rank one. For \(n=1\), it is positive semidefinite for every \(u\in[0,1]\), and positive definite exactly when \(u<1\).

Equivalently, for finite Gaussian bandwidth \(t\ge0\), \(\exp[-t h(x,y)^2]\) is positive semidefinite precisely when \(t=0\) or \(t\ge-\log\rho_n\). In particular, \(\log(n-1)<-\log\rho_n<\log n\) for \(n\ge3\).

## Assumptions and scope
The domain is the **entire** finite Cartesian product; the underlying distance is unnormalized Hamming distance, not Euclidean distance. A distance-radial function is positive definite here when its full \(s^n\)-by-\(s^n\) kernel matrix is positive semidefinite. The alphabet can be identified with the cyclic group \(\mathbb Z/s\mathbb Z\), but neither primeness nor a field structure is needed. Strict positive definiteness refers to distinct points. The isolated case \(u=1\) is the constant kernel; \(u=0\) is the identity kernel.

## Proof
**1. Fourier diagonalization.** Regard \(X\) as \((\mathbb Z/s\mathbb Z)^n\). Every group character is an eigenvector of the translation-invariant matrix \(K_u\). A character nontrivial in exactly \(j\) coordinates has eigenvalue
\[
\lambda_{n,s,j}(u)=\sum_{a=0}^{n-j}\sum_{b=0}^{j}
 \binom{n-j}{a}\binom jb(s-1)^a(-1)^b u^{(a+b)^2},
\qquad 0\le j\le n,
\]
with multiplicity \(\binom nj(s-1)^j\). Indeed, summing a nontrivial one-coordinate character over all nonzero group elements gives \(-1\), while a trivial character gives \(s-1\). The top-sector eigenvalue is \(\lambda_{n,s,n}(u)=B_n(u)\), independent of \(s\).

**2. Critical roots.** Write \(B_m(u)=\sum_{k=0}^{m}(-1)^k\binom mk u^{k^2}\). For \(m=2\),
\[
B_2(u)=(u-1)(u^3+u^2+u-1).
\]
The cubic increases strictly and has a unique root \(\rho_2\in(1/2,3/5)\); on \((0,1)\), \(B_2\) is positive before this root and negative afterwards.

For \(m\ge3\), at \(u=1/m\), the constant and linear terms cancel and the remaining alternating series begins with a positive term. Its consecutive absolute terms from index \(2\) decrease strictly, so \(B_m(1/m)>0\). At \(u=1/(m-1)\), the same alternating-tail estimate gives
\[
B_m(u)\le1-mu+\binom m2u^4
=-\frac1{m-1}+\frac{m}{2(m-1)^3}<0.
\]
Here and below, the required decrease follows from the ratio
\[
\frac{\binom m{k+1}u^{(k+1)^2}}{\binom mk u^{k^2}}
=\frac{m-k}{k+1}u^{2k+1}<1\qquad(k\ge2)
\]
in the displayed parameter ranges.

We prove inductively that \(B_m\) decreases strictly on \([0,\rho_{m-1}]\), has its unique zero there, and \(\rho_m<\rho_{m-1}\). The identity
\[
B_m(u)=B_{m-1}(u)-\sum_{k=0}^{m-1}(-1)^k\binom{m-1}k u^{(k+1)^2}
\]
and the alternating tail bound yield
\[
B_m(\rho_{m-1})\le-\rho_{m-1}
 [1-(m-1)\rho_{m-1}^3]<0.
\]
The bracket is positive: for \(m=3\), use \(\rho_2<3/5\); for \(m\ge4\), use \(\rho_{m-1}<1/(m-2)\). For derivatives, the terms of \(B_m'(u)+m\) form a decreasing alternating tail beginning positively at index \(2\) on \([0,\rho_{m-1}]\). Hence
\[
B_m'(u)\le-m+4\binom m2u^3
=m\bigl[-1+2(m-1)u^3\bigr]<0.
\]
For \(m=3\) this follows from \(u<3/5\); for \(m\ge4\), from \(u<1/(m-2)\) and \(2(m-1)<(m-2)^3\). The derivative-tail ratio is bounded at index \(2\) by \(3(m-2)u^5/4<1\) and decreases thereafter. Thus the claimed unique roots and their strict decrease follow by induction. In particular, \(B_m(u)<0\) whenever \(\rho_m<u\le\rho_{m-1}\).

**3. Sufficiency for every alphabet.** For \(0<u\le\rho_n\) and \(0\le j<n\), group the Fourier eigenvalue by its \(a\)-index, writing
\[
H_{j,a}(u)=\sum_{b=0}^j(-1)^b\binom jb u^{(a+b)^2}.
\]
For \(a=0\), \(H_{j,0}(u)=B_j(u)>0\), using strict decrease of the roots (and \(B_0=1\), \(B_1=1-u\)). For \(a\ge1\), \(j\le n-1\) and \((a+b)^2-a^2\ge3b\) when \(b\ge1\), whence
\[
H_{j,a}(u)\ge u^{a^2}\bigl[2-(1+u^3)^j\bigr]>0.
\]
Indeed, if \(n\ge3\), then \((1+u^3)^j\le\exp((n-1)u^3)\le e^{1/(n-1)^2}\le e^{1/4}<2\). If \(n=2\), the only nontrivial case with \(a,j\ge1\) is \(H_{1,1}=u-u^4>0\). All coefficients \(\binom{n-j}{a}(s-1)^a\) are nonnegative, so \(\lambda_{n,s,j}(u)>0\) for \(j<n\). The sole possible zero is \(B_n(u)\), which is nonnegative precisely until \(u=\rho_n\). The rank and strictness assertions follow from the Fourier multiplicities. At \(u=0\), \(K_u=I\).

**4. Necessity, including disconnected admissibility.** The binary alphabet is an induced two-symbol subproduct of any larger alphabet, so positive semidefiniteness for \(s>2\) implies it for \(s=2\). For \(n=2\), \(B_2(u)<0\) throughout \((\rho_2,1)\), proving failure. Suppose the binary statement established in dimension \(n-1\). If \(\rho_n<u\le\rho_{n-1}\), the top Fourier eigenvalue \(B_n(u)\) is negative by Step 2. If \(\rho_{n-1}<u<1\), the restriction to an \((n-1)\)-coordinate binary subcube is already indefinite by induction. This excludes all \(\rho_n<u<1\) in every dimension. Finally \(u=1\) is the rank-one all-ones kernel.

## Verification
The supplied `verify.py` uses only the Python standard library. It recomputes exact rational Fourier formulas, compares their multiplicity-weighted trace to \(s^n\), and checks independent direct character sums on small products. Numerical root tests cover \(2\le n\le18\) and \(s\in\{2,3,5\}\), including endpoint-nullity patterns. Execute `python verify.py`; expected output begins `CHECK_OK`. These finite checks support the algebra but are not the proof of the infinite-dimensional and all-alphabet quantifiers.

## Relationship to prior work
Jayasumana et al. (arXiv:1412.0265, Sec. V) explain the general negative-type criterion for Gaussian kernels at **every** bandwidth, and explicitly distinguish kernels positive for only some bandwidths. Feragen, Lauze, and Hauberg (arXiv:1411.0296, Theorems 1–3 and Sec. 3) analyze geodesic exponential kernels on continuous geodesic spaces and do not give finite Hamming-product spectral thresholds. Both sources concern neighboring, but not dominating, claims.

A separate earlier binary-alphabet result, *A sharp Gaussian positive-definiteness dimension cutoff on Boolean Hamming cubes*, establishes a restricted \(0<u\le1/16\) parameter window for \(s=2\). The present theorem does not claim that restricted region as new. Its distinct claim is the complete \(0\le u\le1\) criterion simultaneously for all alphabet sizes, together with the alphabet-dependent exact boundary nullity. Standard finite Fourier diagonalization supplies the spectral starting point; the uniform positivity proof and sharp exclusion of all larger parameters supply the classification.

## Limitations
The criterion is for the full Hamming Cartesian product, not arbitrary subsets under an independently chosen metric, and does not classify powers other than the square. The proof establishes no novelty certification outside the sources reviewed; an equivalent statement may exist in older association-scheme literature. No independent audit has been performed.

## References
- A. Feragen, F. Lauze, S. Hauberg, *Geodesic Exponential Kernels: When Curvature and Linearity Conflict*, arXiv:1411.0296 (first public version 2014-11-02), CVPR 2015. https://arxiv.org/abs/1411.0296 ; https://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Feragen_Geodesic_Exponential_Kernels_2015_CVPR_paper.pdf
- S. Jayasumana, R. Hartley, M. Salzmann, H. Li, M. Harandi, *Kernel Methods on Riemannian Manifolds with Gaussian RBF Kernels*, arXiv:1412.0265 (first public version 2014-11-30), Sec. V. https://arxiv.org/abs/1412.0265
- *A sharp Gaussian positive-definiteness dimension cutoff on Boolean Hamming cubes*, earlier binary-only mathematical finding, overlap statement inspected (limited to \(0<u\le1/16\)).
