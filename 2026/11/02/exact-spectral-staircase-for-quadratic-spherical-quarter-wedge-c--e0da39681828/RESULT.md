# Exact spectral staircase for quadratic spherical quarter-wedge concentration

## Finding

Let \(d\ge3\), let \(S^{d-1}\subset\mathbb R^d\) carry normalized surface measure, and let \(V_{\le2}=\mathcal H_0\oplus\mathcal H_1\oplus\mathcal H_2\) be the complex spherical-harmonic band of degrees zero through two. For the open orthogonal quarter-wedge
\[
C_d=\{x\in S^{d-1}:x_1>0,\ x_2>0\},
\]
define the self-adjoint concentration operator \(T_d=P_{V_{\le2}}\mathbf1_{C_d}|_{V_{\le2}}\). Its eigenvalues lie strictly between zero and one. The **entire spectral staircase**, including multiplicities, is
\[
\begin{array}{c|c}
\text{eigenvalue range}&\text{number, counted with multiplicity}\\ \hline
(0,1/4)&2d-1\\
\{1/4\}&d(d-3)/2\\
(1/4,1/2)&2\\
(1/2,1)&d-1.
\end{array}
\]
In particular \(1/2\) is never an eigenvalue; exactly \(d-1\) modes concentrate more than half their energy in the quarter-wedge, despite \(\dim V_{\le2}=d(d+3)/2\). The eigenvalue \(1/4\) has *exactly* the indicated multiplicity (zero when \(d=3\)).

The **complete eigenvalues**, not only their locations, are obtained from one explicit generalized \(4\times4\) eigenproblem, one explicit pair of scalar roots, one pair of roots each repeated \(d-2\) times, a singleton repeated \(d-2\) times, and the \(1/4\) plateau. The largest concentration eigenvalue is the largest root of the \(4\times4\) problem. It is strictly greater than \(3/4\), is simple for every \(d\ge3\), and therefore has a unique maximizing complex line.

Put
\[
\mu_d=\frac{\Gamma(d/2)}{\sqrt\pi\Gamma((d+1)/2)},\qquad
\nu_d=\frac2{\pi d},\qquad
\tau=\frac1{2\pi},\qquad
\eta_d=\frac{d\sqrt{d+2}\,\mu_d}{2\sqrt2(d+1)}.
\]
The four **scalar symmetric** eigenvalues are the roots of \(\det(K_d-\lambda G_d)=0\), where
\[
G_d=\begin{pmatrix}
1&0&2/d&0\\
0&2/d&0&0\\
2/d&0&8/[d(d+2)]&0\\
0&0&0&1/[d(d+2)]
\end{pmatrix}
\]
and
\[
K_d=\begin{pmatrix}
1/4&\mu_d/2&1/(2d)&\nu_d/4\\
\mu_d/2&(1+d\nu_d)/(2d)&3\mu_d/[2(d+1)]&\mu_d/[2(d+1)]\\
1/(2d)&3\mu_d/[2(d+1)]&2/[d(d+2)]&\nu_d/(d+2)\\
\nu_d/4&\mu_d/[2(d+1)]&\nu_d/(d+2)&1/[4d(d+2)]
\end{pmatrix}.
\]
The two **scalar antisymmetric** eigenvalues are
\[
\frac14-\frac\tau2\ \pm\ \sqrt{\frac{\tau^2}{4}+\frac{\eta_d^2}{4}}.
\]
The two **transverse-vector symmetric** eigenvalues, each with multiplicity \(d-2\), are
\[
\frac14+\frac\tau2\ \pm\ \sqrt{\frac{\tau^2}{4}+\eta_d^2}.
\]
The **transverse-vector antisymmetric** eigenvalue is \(1/4-\tau\), with multiplicity \(d-2\), and the **transverse traceless-quadratic** eigenvalue is \(1/4\), with multiplicity \(d(d-3)/2\). These descriptions account for all \(d(d+3)/2\) eigenvalues, counting coincidences additively.

## Assumptions and scope

The domain is the intersection of exactly two perpendicular open hemispheres of the round real sphere, in *every integer dimension \(d\ge3\)*; the sphere has its ordinary uniform probability measure. The band contains **all** degrees zero, one, and two, not just pure degree two. Eigenvalues refer to the energy ratio \(\int_{C_d}|f|^2d\sigma/\int_{S^{d-1}}|f|^2d\sigma\). There is no weighting, sample discretization, noise, or claim about larger bands or non-right-angle wedges. Boundary great spheres have measure zero.

## Proof

**1. Exact moments.** Write \(u=x_1\), \(v=x_2\), and \(y=(x_3,\dots,x_d)\). For nonnegative integers \(a,b\), the normalized absolute moments are
\[
M_{a,b}=\mathbb E|u|^a|v|^b
=\frac{\Gamma(d/2)\Gamma((a+1)/2)\Gamma((b+1)/2)}{\pi\Gamma((d+a+b)/2)}.
\]
They satisfy \(M_{a+2,b}=(a+1)M_{a,b}/(d+a+b)\) and the symmetric recurrence in \(b\), starting with \(M_{0,0}=1\), \(M_{1,0}=M_{0,1}=\mu_d\), and \(M_{1,1}=\nu_d\). For each transverse coordinate \(y_j\),
\[
\mathbb E\bigl[y_j^2|u|^a|v|^b\bigr]=\frac{M_{a,b}}{d+a+b}.
\]
For a monomial in \(u,v\), its quarter-wedge integral equals one quarter of the corresponding absolute moment. On the whole sphere its integral vanishes if either exponent is odd, and otherwise equals the absolute moment. The same rules hold with an additional transverse factor \(y_j^2\), using the last formula. These follow from independent coordinate-sign symmetry and the beta/Dirichlet distribution of squared coordinates.

**2. Exhaustive invariant decomposition.** The group \(O(d-2)\) rotating \(y\) and the swap \(u\leftrightarrow v\) preserve both quadratic forms. The entire band splits orthogonally, both globally and on \(C_d\), into:

* the four-dimensional scalar symmetric span of \(1,u+v,u^2+v^2,uv\);
* the two-dimensional scalar antisymmetric span of \(u-v,u^2-v^2\);
* for each of the \(d-2\) transverse directions, the symmetric vector span of \(y_j,(u+v)y_j\) and the one-dimensional antisymmetric vector span of \((u-v)y_j\);
* the trace-free homogeneous quadratic polynomials in \(y\), of dimension \((d-3)d/2\).

The last dimension is zero when \(d=3\). The dimensions add to \(d(d+3)/2\), the dimension of the complete band. Orthogonality uses odd transverse coordinate signs and the zero spherical mean of trace-free transverse quadratics. In the last sector \(|f|^2\) is even separately in \(u,v\), so its energy fraction is exactly \(1/4\).

**3. Exact block matrices.** In the ordered scalar-symmetric basis of Step 2, the full-sphere and quarter-wedge Gram matrices are exactly \(G_d,K_d\) displayed above. Both are positive definite for \(d\ge3\). For the scalar-antisymmetric block, they are
\[
G_- = \begin{pmatrix}2/d&0\\0&4/[d(d+2)]\end{pmatrix},\qquad
K_- = \begin{pmatrix}(1-d\nu_d)/(2d)&\mu_d/[2(d+1)]\\
\mu_d/[2(d+1)]&1/[d(d+2)]\end{pmatrix}.
\]
For one transverse-vector symmetric block they are
\[
G_v = \begin{pmatrix}1/d&0\\0&2/[d(d+2)]\end{pmatrix},\qquad
K_v = \begin{pmatrix}1/(4d)&\mu_d/[2(d+1)]\\
\mu_d/[2(d+1)]&(1+d\nu_d)/[2d(d+2)]\end{pmatrix}.
\]
The one-dimensional antisymmetric vector block has full norm \(2/[d(d+2)]\) and quarter norm \((1-d\nu_d)/[2d(d+2)]\). Taking the generalized eigenvalues and normalizing the two-by-two Gram matrices gives the two explicit pairs above. The tensor-block eigenvalue is \(1/4\). This proves the complete spectral parametrization.

**4. Exact position of every eigenvalue.** Direct determinant and trace identities yield
\[
\begin{split}
\operatorname{tr}(G_d^{-1}K_d)&=1+\frac1{2\pi},\\
\det(K_d-G_d/4)&=\frac{\mu_d^2\nu_d^2(d-2)^2}{64(d+1)^2(d+2)^2}>0,\\
\det(K_- -G_-/4)&=-\frac{\mu_d^2}{4(d+1)^2}<0,\\
\det(K_v-G_v/4)&=-\frac{\mu_d^2}{4(d+1)^2}<0.
\end{split}
\]
The symmetric matrix \(K_d-G_d/4\) is indefinite because its first two-coordinate principal submatrix has negative determinant \(-\mu_d^2/4\). Its determinant is positive; therefore its inertia is exactly two positive and two negative eigenvalues. Sylvester's law of inertia implies that exactly two of the four generalized eigenvalues lie above \(1/4\), and exactly two below.

The scalar-antisymmetric eigenvalues straddle \(1/4\) by the negative determinant, and both lie below \(1/2\), since their positive sum equals \(1/2-1/(2\pi)<1/2\). Similarly, the vector-symmetric eigenvalues straddle \(1/4\). To show its upper eigenvalue exceeds \(1/2\), log-convexity of \(\Gamma\) gives \(\sqrt d\,\mu_d>\sqrt{2/\pi}\), and hence
\[
\eta_d^2>\frac{d(d+2)}{4\pi(d+1)^2}\ge\frac{15}{64\pi}>\frac1{16}.
\]
Therefore its upper eigenvalue exceeds \(1/4+\eta_d>1/2\).

It remains to place the four-dimensional scalar sector. The trial polynomial \(p_d=(1+\sqrt d\,u)(1+\sqrt d\,v)\) belongs to it and has Rayleigh quotient
\[
\frac{\int_{C_d}|p_d|^2d\sigma}{\int_{S^{d-1}}|p_d|^2d\sigma}
=\frac14+\frac{\sqrt d\,\mu_d(2d+1)/(d+1)+2/\pi}{4-2/(d+2)}
>\frac34.
\]
The strict final inequality follows from \(\sqrt d\,\mu_d>\sqrt{2/\pi}\), \((2d+1)/(d+1)\ge7/4\), and \((7/4)\sqrt{2/\pi}+2/\pi>2\). Thus the largest scalar-symmetric eigenvalue exceeds \(3/4\). Since the sum of all four is \(1+1/(2\pi)\), the remaining three positive eigenvalues have sum below \(1/4+1/(2\pi)<1/2\). Exactly one scalar-symmetric eigenvalue exceeds \(1/2\), and it is simple. By the previous inertia calculation, the second eigenvalue above \(1/4\) lies below \(1/2\).

All eigenvalues are strictly between zero and one: a nonzero degree-two polynomial cannot vanish on either the open wedge or its open complement, by real-analytic unique continuation. Combining the strict placements across all blocks gives the four displayed multiplicities, the absence of \(1/2\), and the uniqueness of the maximizer. The largest scalar root dominates every other block: the largest vector-symmetric root is less than its positive trace \(1/2+1/(2\pi)<3/4\), while the other non-scalar-symmetric sectors lie below \(1/2\).

## Verification

The standalone `symbolic_checker.py` reconstructs all four reduced Gram pairs from the moment recurrence and verifies nine exact symbolic trace, determinant, and normalization identities. The independent `checker.py` instead enumerates a full monomial basis of the degree-at-most-two spherical band, constructs its *unreduced* Gram matrices from multivariate spherical moments, and compares their numerical generalized spectra against the reduced blocks. It checks every dimension \(3\le d\le12\), the exact interval counts, total trace, positive definiteness and sharp-sector identification. The executed outputs were `SYMBOLIC_IDENTITIES_PASS 9` and `QUADRANT_CHECKS_PASS 515`. Reproduce with `python symbolic_checker.py` and `python checker.py` after installing the packages in `requirements.txt`.

The infinite family, exact multiplicities, and sharp optimizer are established by the proof above, not by numerical extrapolation. Computations are supplementary cross-checks.

## Relationship to prior work

Simons, Dahlen, and Wieczorek developed spherical Slepian concentration on arbitrary surface regions and the general finite-dimensional eigenproblem; those foundational facts are prior [1]. Michel, Plattner, and Seibert developed spin-weighted scalar/vector/tensor Slepian techniques and cap commuting operators [2]. Roddy and McEwen studied Slepian wavelets for incomplete and irregular spherical regions [3]. These works motivate localizing a low harmonic band but do not, in the inspected material, supply the fixed-size quadratic right-wedge matrices, the exact four-interval count, the protected \(1/4\)-eigenspace, or the unique sharp top eigenline in every dimension. The current geometry has two interacting perpendicular sign cuts, rather than one reflection-symmetric hemisphere, so a one-cut spectral pairing does not determine its spectrum.

## Limitations

The formulas apply only to the complete degrees-zero-through-two band on a round sphere cut by *perpendicular* hemispheres. They do not give spectra for higher degree, non-right-angle wedges, nonuniform measures, or finite noisy sample schemes. The top eigenvalue is characterized as the largest root of an explicit fixed-size generalized eigenproblem rather than by a radical formula. Mathematical correctness has undergone one internal analytic and computational review; independent validation and exhaustive historical-priority assessment are not claimed. General concentration frameworks can compute the same operator numerically for a specified dimension; the present claim concerns the all-dimensional exact pattern and closed block formulas.

## References

[1] F. J. Simons, F. A. Dahlen, and M. A. Wieczorek, *Spatiospectral concentration on a sphere*, SIAM Review **48** (2006), 504–536; first public preprint arXiv:math/0408424 (2004-08-31). https://arxiv.org/abs/math/0408424

[2] V. Michel, A. Plattner, and K. Seibert, *A Unified Approach to Scalar, Vector, and Tensor Slepian Functions on the Sphere and Their Construction by a Commuting Operator*, arXiv:2103.14650, first public 2021-03-26. https://arxiv.org/abs/2103.14650

[3] P. J. Roddy and J. D. McEwen, *Slepian Scale-Discretised Wavelets on the Sphere*, arXiv:2106.02023, first public 2021-06-03. https://arxiv.org/abs/2106.02023
