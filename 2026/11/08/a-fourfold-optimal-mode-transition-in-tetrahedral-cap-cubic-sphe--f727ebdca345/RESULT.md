# A fourfold optimal-mode transition in tetrahedral-cap cubic spherical harmonics

## Finding
Let \(v_1=(1,1,1)/\sqrt3\), \(v_2=(1,-1,-1)/\sqrt3\), \(v_3=(-1,1,-1)/\sqrt3\), and \(v_4=(-1,-1,1)/\sqrt3\). For each \(1/\sqrt3\le c<1\), consider the union of four spherical caps
\[
\Omega_c=\bigcup_{j=1}^4\{x\in S^2:x\cdot v_j\ge c\}.
\]
Their interiors are disjoint, including at the endpoint where boundaries touch. On the seven-dimensional complex space \(\mathcal H_3\) of spherical harmonics of **exact degree three**, form the concentration operator \(T_c=P_3\mathbf1_{\Omega_c}P_3|_{\mathcal H_3}\).

The **entire spectrum** consists of these three exact branches, with the stated multiplicities:
\[
\begin{aligned}
\lambda_A(c)&=2-\frac{35}{18}c-\frac{35}{9}c^3+\frac{21}{2}c^5-\frac{20}{3}c^7, &&\text{multiplicity }1,\\
\lambda_B(c)&=2-\frac{119}{108}c-\frac{245}{54}c^3+\frac{77}{12}c^5-\frac{25}{9}c^7, &&\text{multiplicity }3,\\
\lambda_C(c)&=2-\frac{35}{12}c+\frac{35}{6}c^3-\frac{119}{12}c^5+5c^7, &&\text{multiplicity }3.
\end{aligned}
\]
Their mutually orthogonal eigenspaces are
\[
\begin{aligned}
 A&=\operatorname{span}_{\mathbb C}\{x_1x_2x_3\},\\
 B&=\operatorname{span}_{\mathbb C}\{x_i(5x_i^2-3):i=1,2,3\},\\
 C&=\operatorname{span}_{\mathbb C}\{x_1(x_2^2-x_3^2),\ x_2(x_3^2-x_1^2),\ x_3(x_1^2-x_2^2)\}.
\end{aligned}
\]
Here these homogeneous cubics are restricted to \(S^2\); \(x_i(5x_i^2-3)\) is the restriction of the harmonic cubic \(x_i(5x_i^2-3|x|^2)\).

Define the algebraic transition
\[
\boxed{\ c_*=\sqrt{\frac{9+\sqrt{33}}{24}}\approx0.7838091457358.\ }
\]
For \(1/\sqrt3\le c<c_*\), the **unique top eigenspace is the three-dimensional space \(C\)**. For \(c_*<c<1\), the **unique top eigenspace is the one-dimensional space \(A\)**. At the unique interior top-eigenvalue crossing \(c=c_*\), the top eigenvalue has multiplicity **four**, with eigenspace \(A\oplus C\); the remaining branch \(B\) lies strictly below. Thus an optimally localized degree-three harmonic switches sharply from an off-diagonal cubic triplet to the tetrahedrally invariant cubic \(x_1x_2x_3\) when the four equal caps shrink through this angle.

## Assumptions and scope
All integrals use normalized surface area \(d\sigma=dA/(4\pi)\); eigenvalues are energy fractions \(\int_{\Omega_c}|Y|^2d\sigma/\int_{S^2}|Y|^2d\sigma\). The parameter \(c\) is cosine of cap radius \(\theta\), and the disjointness threshold is \(c=1/\sqrt3\). The four caps may be rotated together. Complex linear combinations are allowed. The space is the pure degree-three eigenspace, not the low-pass space through degree three. The theorem does not concern overlapping caps or varying cap apertures.

## Proof
**1. A symmetry-adapted orthogonal decomposition.** Every displayed basis polynomial is harmonic of degree three before restricting to the sphere. Full-sphere orthogonality follows from parity and coordinate-permutation invariance. On \(S^2\), the normalized squared norms of the unnormalized generators are
\[
\int (x_1x_2x_3)^2d\sigma=\frac1{105},\quad
\int x_1^2(5x_1^2-3)^2d\sigma=\frac47,\quad
\int x_1^2(x_2^2-x_3^2)^2d\sigma=\frac4{105}.
\tag{1}
\]
The four tetrahedral vertices are permuted by even coordinate-sign flips and by all permutations of the coordinates. These transformations preserve \(\Omega_c\). Every cross-sector quadratic form vanishes by these symmetries. For instance the scalar generator \(x_1x_2x_3\) is fixed by all even sign flips, while each \(B\) generator changes sign under one such flip; scalar-to-\(C\) cross terms vanish after exchanging the two coordinates inside the parenthesis of a \(C\) generator. Likewise \(B\)-to-\(C\) terms vanish by sign flips or by swapping the two squared coordinates; distinct generators within a triplet are orthogonal by a suitable even sign flip. Coordinate permutations make the three diagonal entries within each triplet identical. Consequently \(T_c\) is scalar on each of \(A,B,C\), whose dimensions sum to seven.

**2. Evaluation of the three scalar values.** All four cap integrals of the square of any one of the generators agree, since the even coordinate-sign flips take the north tetrahedral vertex to the remaining three and preserve the squared generator. Fix \(v=(1,1,1)/\sqrt3\), and write a point of its cap as
\[
 x=u v+\sqrt{1-u^2}(\cos\phi\,e+\sin\phi\,f),\quad
 e=(1,-1,0)/\sqrt2,\quad f=(1,1,-2)/\sqrt6,
\]
where \(c\le u\le1\) and \(0\le\phi<2\pi\). Each full four-cap integral is \(2\int_c^1\langle q(x)^2\rangle_{\phi}\,du\). Circle averaging the squares of the three representatives \(q_A=x_1x_2x_3\), \(q_B=x_1(5x_1^2-3)\), and \(q_C=x_1(x_2^2-x_3^2)\) gives the **exact** polynomials
\[
\begin{aligned}
\langle q_A^2\rangle_\phi&=(24u^6-27u^4+6u^2+1)/108,\\
\langle q_B^2\rangle_\phi&=(300u^6-495u^4+210u^2+17)/54,\\
\langle q_C^2\rangle_\phi&=-(u-1)(u+1)(12u^4-5u^2+1)/18.
\end{aligned}
\tag{2}
\]
To check the circle average without any asymptotic approximation, expand each cubic in \(u,\sqrt{1-u^2},\cos\phi,\sin\phi\) and apply \(\langle \cos^{2i}\phi\sin^{2j}\phi\rangle=(2i)!(2j)!/[4^{i+j}i!j!(i+j)!]\), with odd powers integrating to zero. Dividing the resulting four-cap integrals by the corresponding full-sphere squared norms (1), and integrating the polynomials in (2), produces the three stated eigenvalue polynomials. This proves their formulas and multiplicities for every admissible \(c\), including the tangency boundary.

**3. Sharp concentration and the fourfold crossing.** Direct factoring of the differences yields
\[
\begin{aligned}
\lambda_A-\lambda_C&=\frac{35}{36}c(1-c^2)(12c^4-9c^2+1),\\
\lambda_A-\lambda_B&=\frac7{108}c(1-c^2)(60c^4-3c^2-13),\\
\lambda_B-\lambda_C&=\frac7{27}c(1-c^2)(30c^4-33c^2+7).
\end{aligned}
\tag{3}
\]
On the allowed interval, the first difference has exactly one zero, at \(c_*\); its other positive zero is \(\sqrt{(9-\sqrt{33})/24}<1/\sqrt3\). The positive zero of \(60c^4-3c^2-13\) is approximately \(0.700818\), strictly below \(c_*\); the larger positive zero of \(30c^4-33c^2+7\) is approximately \(0.901663\), strictly above \(c_*\), and its smaller positive zero is below \(1/\sqrt3\). These orderings also follow directly by substituting \(c_*^2=(9+\sqrt{33})/24\) in the three quadratics in \(c^2\). Hence on \([1/\sqrt3,c_*)\), branch \(C\) strictly exceeds both others, whereas on \((c_*,1)\), branch \(A\) strictly exceeds both others. At \(c_*\), \(\lambda_A=\lambda_C>\lambda_B\). Since the Rayleigh quotient of a self-adjoint positive operator is maximized precisely by its top eigenspace, this proves the sharp concentration statement, all optimizers, and the fourfold degeneracy. Finally,
\[
\lambda_A+3\lambda_B+3\lambda_C=14(1-c)=7\sigma(\Omega_c),
\]
consistent with the degree-three addition-theorem trace formula.

## Verification
`verify.py` is a standalone symbolic and independent numerical checker with dependencies in `requirements.txt`. It computes the circle averages from polynomial expansions, integrates them symbolically, checks the three eigenvalue identities, all three difference factorizations, the trace, and the exact algebraic critical value. Independently it builds the full seven-by-seven concentration Gram matrix in the explicitly normalized spherical-harmonic basis and integrates every cap by high-order Gauss-Legendre and angular quadrature at five cap sizes, including the critical one. The numerical comparison checks all off-block entries and all eigenvalue multiplicities. These finite tests supplement, but do not replace, the exact algebraic proof for all allowable radii.

## Relationship to prior work
Simons, Dahlen, and Wieczorek supply the general spectral-concentration eigenproblem on the sphere and methods for polar caps. Speckbacher and Hrycak (2019), and Jaming and Speckbacher (2020), establish general spherical large-sieve concentration inequalities but do not provide the three exact spectral branches and this fourfold transition. Michel, Plattner, and Seibert (2021) investigate commuting operators for single spherical caps and higher tensor ranks, not tetrahedral unions.

A related already established complete **degree-two** spectrum for regular-simplex cap unions has two branches and includes a different fivefold scalar crossing for tetrahedral caps at \(c=\sqrt{3/7}\). That theorem does **not** imply this degree-three transition: here a new one-dimensional tetrahedral-invariant cubic appears alongside two inequivalent three-dimensional sectors, and the optimal sector changes at \(\sqrt{(9+\sqrt{33})/24}\), with *fourfold* rather than total degeneracy. Other prior results concerning full-sphere degree-two norm extremizers, uniform-volume moments of solid Platonic bodies, and hemisphere restriction are different spectral or geometric invariants.

## Limitations
The theorem is confined to the equal, nonoverlapping tetrahedral cap mask and pure harmonic degree three. It does not give the spectrum for low-pass bands, overlapping caps, arbitrary simplex dimensions, or cap perturbations. It describes a top-eigenvalue crossing, not equality of all seven eigenvalues. The third-degree tetrahedral basis is classical, and a previously unlocated geometric or cubature calculation could contain an equivalent polynomial spectrum; independent historical verification is still desirable.

## References
1. F. J. Simons, F. A. Dahlen, and M. A. Wieczorek, *Spatiospectral concentration on a sphere*, arXiv:math/0408424v1, first public 2004-08-31.
2. M. Speckbacher and T. Hrycak, *Concentration estimates for band-limited spherical harmonics expansions via the large sieve principle*, arXiv:1909.01670v1, first public 2019-09-04.
3. P. Jaming and M. Speckbacher, *Concentration estimates for finite expansions of spherical harmonics on two-point homogeneous spaces via the large sieve principle*, arXiv:2004.02474v1, first public 2020-04-06.
4. V. Michel, A. Plattner, and K. Seibert, *A Unified Approach to Scalar, Vector, and Tensor Slepian Functions on the Sphere and Their Construction by a Commuting Operator*, arXiv:2103.14650v1, first public 2021-03-26.
