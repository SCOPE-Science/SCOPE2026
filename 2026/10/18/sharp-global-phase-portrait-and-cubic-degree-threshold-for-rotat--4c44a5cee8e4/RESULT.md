# Sharp global phase portrait and cubic degree threshold for rotational planar maps

## Finding
Identify the real plane with \(\mathbb C\). Consider real polynomial maps of degree at most three which commute with every rotation, are global smooth diffeomorphisms, and have a hyperbolically attracting fixed point at the origin. They are precisely the linear contractions \(F(z)=az\), with \(0<|a|<1\), and the cubic maps
\[
 F_{a,b}(z)=z(a+b|z|^2),\qquad 0<|a|<1,\quad b\ne0,
\]
whose parameters satisfy the **sharp global-diffeomorphism criterion**
\[
 \operatorname{Re}(\overline a b)>-\frac{\sqrt3}{2}|a||b|. \tag{1}
\]
Every map in the cubic class has exactly one positive invariant radius. With \(m=|a|^2\), \(c=\operatorname{Re}(\overline a b)\), and \(d=|b|^2\), the squared radius is
\[
 s_* = \frac{-c+\sqrt{c^2+d(1-m)}}{d}>0. \tag{2}
\]
The open disk \(|z|<\sqrt{s_*}\) is exactly the attraction basin of the origin; all orbits starting outside its closure escape to infinity. The boundary circle is invariant and carries the rigid rotation by \(\zeta=a+b s_*\), where \(|\zeta|=1\). Its outward radial multiplier is exactly
\[
 \lambda_{\mathrm{rad}}=1+2s_*\sqrt{c^2+d(1-m)}>1. \tag{3}
\]
The origin is the **unique** fixed point precisely when \(\zeta\ne1\). In that case all nonzero periodic points, if any, lie on this circle: if \(\zeta\) has finite multiplicative order \(q\ge2\), every circle point has least period \(q\); if \(\zeta\) has infinite order, the circle has no periodic points and every circle orbit is dense.

**Sharp realization:** For every integer \(q\ge2\), one can realize this configuration with a degree-three real polynomial global \(C^\infty\) diffeomorphism whose **full invertible linear symmetry group** is exactly \(SO(2)\), with its only fixed point a hyperbolic sink and its invariant circle of least period \(q\). No such nonzero periodic point is possible in degree at most two. Indeed, for \(q\ge3\) put \(\zeta=e^{2\pi i/q}\), \(a=b=\zeta/2\); for \(q=2\) put \(a=-1/2+i/4\) and \(b=-1/2-i/4\). In both cases the invariant circle is \(|z|=1\) and its radial multiplier is \(2\). The same first construction realizes every irrational circle rotation by replacing \(2\pi/q\) with an irrational multiple of \(2\pi\).

## Assumptions and scope
A "polynomial map" here means a polynomial in the two real coordinates, **not** a polynomial automorphism with polynomial inverse. A "global smooth diffeomorphism" means a bijection of \(\mathbb R^2\) with a \(C^\infty\) inverse. Rotational equivariance means \(F(e^{i\theta}z)=e^{i\theta}F(z)\) for all real \(\theta\), \(z\). The attracting fixed point has \(0<|a|<1\). No hypothesis is imposed on the eigenvalues of the derivative away from the origin, and the cubic maps are not globally dissipative. The classification concerns the full real polynomial degree-at-most-three class and forward iterates on the entire plane, rather than only small perturbations of a local normal form.

## Proof
**Equivariant polynomial normal form.** Write any real polynomial map as a polynomial in \(z\) and \(\overline z\). Under rotation a monomial \(z^p\overline z^{\,r}\) picks up weight \(p-r\). Equivariance for all rotation angles forces \(p-r=1\). Degree at most three therefore permits exactly \((p,r)=(1,0)\) and \((2,1)\). Hence \(F(z)=z(a+b|z|^2)\). Its differential at the origin is complex multiplication by \(a\). Since it is a smooth diffeomorphism with an attracting origin, necessarily \(0<|a|<1\). If \(b=0\) the map is a global linear contraction.

**Sharp invertibility region.** Suppose \(b\ne0\) and write \(s=|z|^2\). In real Cartesian coordinates direct differentiation yields
\[
 \det DF(z)=m+4cs+3ds^2=:Q(s). \tag{4}
\]
A global diffeomorphism must have positive determinant everywhere: it is positive at the origin and cannot vanish or change sign. For \(c\ge0\), \(Q(s)>0\) for all \(s\ge0\). For \(c<0\) its minimum on the positive half-line is attained at \(s=-2c/(3d)\), with value \(m-4c^2/(3d)\). Thus the necessary condition is exactly (1), with strict inequality. Conversely, (1) makes \(Q(s)>0\) on the half-line. The squared output radius is \(H(s)=s|a+bs|^2\), and \(H'(s)=Q(s)>0\), with \(H(0)=0\) and \(H(s)\to\infty\). Consequently the radial map is a bijection of \([0,\infty)\). Because \(H\) is strictly increasing, \(a+bs\) never vanishes for \(s\ge0\) (a zero would make the image radius vanish for positive input). At each radius the angular map is a rotation. Thus \(F\) is globally bijective; its everywhere nonsingular Jacobian and inverse-function theorem yield a global smooth inverse. At equality in (1) the Jacobian vanishes at a positive radius, so the strict boundary is sharp.

**Exact global dynamics.** An invariant circle of positive radius must solve \(|a+bs|^2=1\). This is
\[
 ds^2+2cs+(m-1)=0.
\]
Since \(d>0\) and \(m-1<0\), the roots have opposite signs and there is exactly one positive root, namely (2). For \(0<s<s_*\), \(|a+bs|<1\); for \(s>s_*\), \(|a+bs|>1\). Hence radii of iterates strictly decrease inside the circle and strictly increase outside. Inside they converge to zero: a positive limit would have to solve the unique positive fixed-radius equation. Outside they diverge: a finite limit would similarly be an impossible positive fixed radius above \(s_*\). The boundary map is multiplication by \(\zeta=a+b s_*\) of unit modulus. The radial map is \(\rho(r)=r|a+b r^2|\); differentiating at the fixed radius gives \(\rho'(\sqrt{s_*})=Q(s_*)=1+2s_*(c+ds_*)\). Formula (2) implies \(c+ds_*=\sqrt{c^2+d(1-m)}>0\), proving (3). A nonzero fixed point requires \(a+bs=1\), hence necessarily \(s=s_*\), proving the fixed-point and periodic-point classification.

**Exact realizations and minimality.** For \(q\ge3\), \(a=b=\zeta/2\) has \(m=c=d=1/4\), so (1) holds, \(a+b=\zeta\ne1\), and \(s_*=1\). On the circle multiplication is the primitive \(q\)-th root \(\zeta\); (4) gives radial multiplier \(Q(1)=2\). For \(q=2\), the stated Gaussian-rational coefficients satisfy \(m=d=5/16\), \(c=3/16\), \(a+b=-1\), so (1) holds, again \(s_*=1\), and \(Q(1)=2\). The local derivative \(a\) is nonreal in each construction. Any invertible real-linear symmetry commuting with \(F\) commutes with \(DF(0)\), and hence must act by multiplication by a nonzero complex constant \(w\). Commuting with the nonzero cubic term then forces \(|w|=1\). Accordingly the full invertible linear symmetry group is exactly the rotations, without reflections or extraneous homotheties. For an irrational rotation angle \(\theta\), choose \(a=b=e^{i\theta}/2\), with the same verification. Finally, equivariance excludes all degree-two terms; every equivariant polynomial of degree at most two is linear, and an attracting linear map has no nonzero periodic points. This proves the cubic threshold.

## Verification
The Jacobian identity (4), the boundary multiplier, and Gaussian-rational \(q=2\) coefficients were checked symbolically; the accompanying `verify.py` independently checks their polynomial identities and runs finite examples of the constructive family. These computations corroborate, but do not replace, the quantified proof above. The inverse and all-radius conclusions are established analytically by the positivity of \(H'\) and the uniqueness of the positive root; finite trajectory tests are not invoked for those conclusions.

## Relationship to prior work
Alarcón, Castro and Labouriau's 2012 study of symmetric planar maps motivates the question of what symmetry plus an attracting unique fixed point says about global behavior. Its \(SO(2)\) radial reduction is useful but its argument asserting that a unique fixed point forces no positive fixed radius cannot be used without an extra condition. Their 2014 review explicitly observes that fixed radial values correspond to invariant circles and need not be excluded by local attraction. The independent 2012 construction of \(\mathbb Z_q\)-equivariant homeomorphisms with prescribed least-period-\(q\) points establishes a broader qualitative obstruction, but does not provide the sharp smooth-polynomial degree threshold, exact \(SO(2)\) symmetry, global-diffeomorphism coefficient region, and complete cubic radial phase portrait in this finding. The earlier polynomial Markus–Yamabe work requires spectral conditions throughout the plane, not merely at the origin; those conditions are not asserted here. All novelty conclusions are limited to these precise structural and quantitative differences, not to the already known possibility of local-but-not-global attraction or invariant circles in general.

## Limitations
The statement concerns global smooth inverses of real polynomial maps, not polynomial inverses. It does not assert dissipativity, existence of an attracting nonzero cycle, robustness of a rational circle rotation under symmetry-breaking perturbations, or a global classification for degrees exceeding three. Rational circle rotations produce continuous families of periodic points, not isolated hyperbolic periodic cycles (the radial multiplier is expanding and the tangential multiplier has modulus one). The invariant circle may support no periodic points when its rotation angle is irrational. Novelty risk remains from classical equivariant polynomial normal forms and any earlier unlocated explicit global coefficient classifications; independent audit has not been performed.

## References
1. B. Alarcón, S. B. S. D. Castro, and I. S. Labouriau, *Global Dynamics for Symmetric Planar Maps*, arXiv:1202.0779v1 (first public version 2012-02-03), especially §4.1, Proposition 4.2; author's open-access PDF: https://cmup.pt/cmup/islabour/Contents/PPt/GlobalDynSymPlanarMaps.pdf.
2. B. Alarcón, S. B. S. D. Castro, and I. S. Labouriau, *Discrete Symmetric Planar Dynamics*, arXiv:1405.6877v1 (2014-05-27), especially §5, on fixed radial radii as invariant circles.
3. B. Alarcón, S. B. S. D. Castro, and I. S. Labouriau, *A Local but Not Global Attractor for a \(\mathbb Z_n\)-Symmetric Map*, arXiv:1201.4818 (2012), especially Theorem 3.1; https://arxiv.org/html/1201.4818v2.
4. B. Alarcón, S. B. S. D. Castro, and I. S. Labouriau, *The Discrete Markus–Yamabe Problem for Symmetric Planar Polynomial Maps*, Indagationes Mathematicae 23 (2012), 603–608; authors' open-access copy: https://cmup.pt/cmup/islabour/Contents/PPt/SymmPlanarMaps.pdf.
