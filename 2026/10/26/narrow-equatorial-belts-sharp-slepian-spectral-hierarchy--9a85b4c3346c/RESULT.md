# Narrow equatorial belts: sharp Slepian spectral hierarchy

## Finding

Let \(S^2\) carry ordinary surface measure \(d\Omega\). For an integer \(L\ge0\), let \(\mathcal B_L=\bigoplus_{\ell=0}^L\mathcal H_\ell(S^2)\), and let \(C_{L,\varepsilon}=P_L\mathbf1_{\{|\omega_3|<\varepsilon\}}P_L\) on \(\mathcal B_L\), with \(0<\varepsilon<1\). This is the squared-energy concentration operator on a symmetric equatorial belt.

For absolute azimuthal order \(m=0,\ldots,L\), set \(k=L-m+1\). Denote the \(k\) eigenvalues in this order sector, in decreasing order, by \(\lambda_{m,j}(\varepsilon)\), \(0\le j<k\). Set
\[
 h_j=\frac{2}{2j+1}\left(\frac{2^j}{\binom{2j}{j}}\right)^2,\quad
 a=j-\frac12,\quad s=\left\lfloor\frac{L-m-j}{2}\right\rfloor,
\]
\[
 D_{m,j,L}=\sum_{r=0}^{s}\frac{(2r+a+m+1)(r+a+1)_m}{(r+1)_m}
 \left(\frac{(a+1)_r}{r!}\right)^2.
\]
Here \((z)_r=z(z+1)\cdots(z+r-1)\) and \((z)_0=1\). Every coefficient \(D_{m,j,L}\) is strictly positive. **For fixed \(L\)** and every admissible \((m,j)\),
\[
 \boxed{\lambda_{m,j}(\varepsilon)=h_jD_{m,j,L}\varepsilon^{2j+1}\bigl(1+O_L(\varepsilon^2)\bigr).}
\]
Azimuthal order \(m=0\) occurs once, and each \(m>0\) sector occurs twice. Thus the successive spectral powers \(\varepsilon,\varepsilon^3,\ldots,\varepsilon^{2L+1}\) occur with respective asymptotic multiplicities \(2L+1,2L-1,\ldots,1\); this refers to **power scales**, not exact repeated eigenvalues at nonzero belt width.

In particular the global least concentration eigenvalue is eventually simple and satisfies the sharp law
\[
 \boxed{\lambda_{\min}(C_{L,\varepsilon})=
 \left(\frac{2^L}{\binom{2L}{L}}\right)^2
 \varepsilon^{2L+1}\bigl(1+O_L(\varepsilon^2)\bigr).}
\]
Up to a unit complex phase, its globally normalized eigenfunction tends in \(L^2(S^2)\) to \(\sqrt{(2L+1)/(4\pi)}\,\omega_3^L\). Writing \(M_L=\max_{0\le m\le L}D_{m,0,L}\), the **sharp leading spectral condition number** is
\[
 \kappa(C_{L,\varepsilon})=
 2M_L\left(\frac{\binom{2L}{L}}{2^L}\right)^2
 \varepsilon^{-2L}\bigl(1+O_L(\varepsilon^2)\bigr).
\]
For \(L=0\), the operator has the single eigenvalue \(\varepsilon\), consistently with the formulas.

## Assumptions and scope

All statements are for the full **complex** harmonic space of degrees zero through \(L\), ordinary (unnormalized) surface area, an equator-centered symmetric belt \(|\omega_3|<\varepsilon\), and the limit \(\varepsilon\downarrow0\) with integer \(L\) fixed. The operator acts on the finite-dimensional domain \(\mathcal B_L\), rather than on all \(L^2(S^2)\). Its spectrum is positive for every \(\varepsilon>0\) by analytic continuation for spherical polynomials.

## Proof

**1. Angular separation and normalization.** Put \(x=\cos\theta=\omega_3\). In the sector \(e^{im\phi}\), spherical-harmonic separation identifies a unit vector with
\[
 f(\theta,\phi)=\frac{e^{im\phi}}{\sqrt{2\pi}}(1-x^2)^{m/2}p(x),
 \qquad \deg p\le k-1,
\]
where \(p\) has unit norm for the inner product \(\int_{-1}^1p(x)\overline{q(x)}(1-x^2)^m\,dx\). This follows from the associated Legendre polynomials: after removing \((1-x^2)^{m/2}\), the degrees \(m,m+1,\ldots,L\) span the complete polynomial space of degree at most \(k-1\). Consequently the belt concentration matrix is
\[
 G_{m,\varepsilon}=\int_{-\varepsilon}^{\varepsilon}(1-x^2)^m v(x)v(x)^*\,dx,
\]
where \(v(x)\) is the column of any orthonormal polynomial basis in this weighted space. The positive and negative azimuthal orders have identical matrices.

**2. Exact leading exterior-power determinant.** Let \(a_r=v^{(r)}(0)/r!\), \(0\le r<k\), regarded as column vectors. These vectors form a basis. Set \(A_j=(\langle a_r,a_t\rangle)_{0\le r,t\le j}\), \(U_j=(\mu_{r+t})_{0\le r,t\le j}\), \(\mu_n=\int_{-1}^1y^n\,dy\), and \(\det A_{-1}=\det U_{-1}=1\). Taylor expansion under \(x=\varepsilon y\), followed by the exterior Cauchy–Binet identity, yields for the elementary symmetric spectral sum of order \(j+1\):
\[
 e_{j+1}(G_{m,\varepsilon})=
 \varepsilon^{(j+1)^2}\det A_j\det U_j
 \bigl(1+O_L(\varepsilon^2)\bigr).
\]
Indeed the unique smallest sum of \(j+1\) distinct Taylor degrees is \(0+1+\cdots+j\); terms of odd relative order vanish by equatorial parity, while the factor \((1-\varepsilon^2y^2)^m\) changes the leading moments only by relative order \(\varepsilon^2\). Both determinants are positive. Since each successive spectral order is two powers smaller than its predecessor, \(e_{j+1}\) is its top \(j+1\) eigenvalue product up to relative \(O_L(\varepsilon^2)\). Taking ratios of consecutive symmetric sums gives
\[
 \lambda_{m,j}(\varepsilon)=\varepsilon^{2j+1}
 \frac{\det A_j}{\det A_{j-1}}
 \frac{\det U_j}{\det U_{j-1}}
 \bigl(1+O_L(\varepsilon^2)\bigr).
\]
This argument establishes the power hierarchy without assuming the limiting eigenvalues are distinct across different azimuthal sectors.

**3. Evaluation-jet norm and explicit endpoint kernel.** The uniform-moment quotient \(\det U_j/\det U_{j-1}\) is the squared \(L^2([-1,1])\) norm of the monic Legendre polynomial of degree \(j\), namely \(h_j\). The other quotient is the squared norm of the degree-\(j\) Taylor coefficient functional after restricting to polynomials vanishing to order at least \(j\) at zero. Writing \(p(x)=x^jg(x)\) therefore identifies it with
\[
 \frac{\det A_j}{\det A_{j-1}}
 =\sup_{\deg g\le k-j-1}\frac{|g(0)|^2}{\int_{-1}^1|g(x)|^2x^{2j}(1-x^2)^m\,dx}.
\]
Evenness of the weight means the odd part of \(g\) only increases the denominator. Thus write \(g(x)=q(x^2)\), \(\deg q\le s\), and substitute \(y=x^2\). The denominator becomes \(\int_0^1|q(y)|^2y^{j-1/2}(1-y)^m\,dy\). The supremum is the endpoint Christoffel kernel for shifted Jacobi polynomials \(P_r^{(a,m)}(1-2y)\), \(a=j-1/2\). Their endpoint values are \((a+1)_r/r!\) and their squared norms are
\[
 \frac{(r+1)_m}{(2r+a+m+1)(r+a+1)_m}.
\]
Summing squared endpoint values divided by these norms gives exactly \(D_{m,j,L}\), proving the complete constants.

**4. Extremal sector and instability.** Each sector has \(k=L-m+1\) successively ordered powers \(\varepsilon^{2j+1}\). Hence the exponent \(2L+1\) occurs only at \((m,j)=(0,L)\); every other eigenvalue is asymptotically larger. At this index \(s=0\) and \(D_{0,L,L}=(2L+1)/2\), whence \(h_L D_{0,L,L}=(2^L/\binom{2L}{L})^2\). The leading exterior-power eigenline converges to the common nullspace of the first \(L\) Taylor coefficient functionals, namely the span of \(x^L\); normalizing on the sphere gives the asserted limiting eigenfunction. The highest spectral scale is \(2M_L\varepsilon(1+O_L(\varepsilon^2))\), and division by the least scale proves the condition-number formula. Finally, counting sectors present at order \(j\) gives \(1+2(L-j)\) eigenvalues on that power scale, whose sum over \(j\) equals \((L+1)^2\).

## Verification

Run `python verification.py` from this package. It uses only the Python standard library and checks the closed endpoint-Jacobi coefficient against independently inverted **exact rational** moment matrices, the monic Legendre norm against moment Schur complements, the least-eigenvalue coefficient, and the dimension count for finite test ranges. Recorded execution: `PASS 832 exact rational consistency checks`. Separate high-precision diagonalizations for orders through \(L=6\) (175 coefficient comparisons at small positive widths) gave maximum relative finite-width deviation \(0.021199467238421\), consistent with the proved \(O_L(\varepsilon^2)\) correction. The analytical determinant and Jacobi identities above, not the finite tests, prove the theorem for arbitrary fixed \(L\).

## Relationship to prior work

Simons–Dahlen–Wieczorek (2004), especially its concentration-matrix and axisymmetric sections, provides the foundational spherical Slepian formulation and matrix reduction. Simons–Dahlen (2006) treats **the equatorial belt itself** and the complementary double polar cap, including exact commuting matrices and numerical eigenvalue profiles; it is the closest primary comparison. Bates–Khalid–Kennedy (2016) develops efficient computation for arbitrary regions. Roddy–McEwen (first public 2021) motivates use of spherical Slepian modes for incomplete-region wavelets. These sources establish the concentration operator and numerical or algorithmic framework, but the inspected primary texts do not state the fixed-bandwidth **complete odd-power hierarchy**, all Jacobi endpoint coefficients, unique weakest mode, or sharp condition-number exponent and constant. The 2006 paper's simultaneous small-cap/high-bandwidth scaling is a different limiting regime. Published hemispherical parity and determinant results concern a nonshrinking hemisphere and do not imply the small-belt constants. The present result makes no claim of originality for the spherical Slepian construction, its matrix formula, associated Legendre separation, or Jacobi orthogonality.

## Limitations

The expansion is not uniform as \(L\to\infty\). It gives asymptotic, not exact finite-width eigenvalues or a closed classification of which \(m\) maximizes the leading scale for every \(L\); that coefficient is nonetheless given by an explicit finite maximum. Different sectors with the same power can have distinct leading constants. The limiting least eigenfunction does not by itself reproduce the sharp leading **energy** coefficient without width-dependent lower-order corrections. The full 2021 wavelet paper could not be inspected due to a large-file access limitation, so an unobserved specialized comparison remains a priority risk. No independent scholarly audit has occurred.

## References

1. P. J. Roddy and J. D. McEwen, *Slepian Scale-Discretised Wavelets on the Sphere*, arXiv:2106.02023 (first public June 3, 2021), https://arxiv.org/abs/2106.02023 .
2. F. J. Simons, F. A. Dahlen, and M. A. Wieczorek, *Spatiospectral Concentration on a Sphere*, arXiv:math/0408424 (2004), https://arxiv.org/abs/math/0408424 .
3. F. J. Simons and F. A. Dahlen, *Spherical Slepian Functions and the Polar Gap in Geodesy*, arXiv:math/0603271 (2006), https://arxiv.org/abs/math/0603271 .
4. A. P. Bates, Z. Khalid, and R. A. Kennedy, *Efficient Computation of Slepian Functions for Arbitrary Regions on the Sphere*, arXiv:1608.05479 (2016), https://arxiv.org/abs/1608.05479 .
