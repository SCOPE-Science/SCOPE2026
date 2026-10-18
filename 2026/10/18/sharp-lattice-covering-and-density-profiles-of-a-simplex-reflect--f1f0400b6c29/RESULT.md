# Sharp lattice covering and density profiles of a simplex–reflection hexagon

## Finding
Let \(T=\operatorname{conv}\{(0,0),(1,0),(0,1)\}\), and set \(S_\lambda=(1-\lambda)T+\lambda(-T)\), for every real \(0\le\lambda\le1\). For the standard integer lattice \(\Lambda=\mathbb Z^2\), write \(\mu_\Lambda(K)\) for the least dilation factor whose lattice translates cover the plane. With \(m_\lambda=\min\{\lambda,1-\lambda\}\), the exact covering-radius and inverse-radius formulas are
\[
\boxed{\mu_\Lambda(S_\lambda)=\frac{2}{1+m_\lambda},\qquad
\mu_\Lambda(S_\lambda)^{-1}=\frac{1+m_\lambda}{2}.}
\]
The inverse covering radius is an increasing then decreasing piecewise-affine profile, attaining its unique maximum \(3/4\) at \(\lambda=1/2\). In particular this profile is different from the decreasing–increasing interpolation profile exhibited by a previously studied pair of lattice-covering parallelograms.

Moreover, the area and lattice-covering density of the optimal dilate are
\[
\operatorname{area}(S_\lambda)=\frac{1+2\lambda(1-\lambda)}2,
\qquad
\boxed{\Theta_\Lambda(S_\lambda):=\mu_\Lambda(S_\lambda)^2\operatorname{area}(S_\lambda)
=\frac{2(1+2\lambda(1-\lambda))}{(1+m_\lambda)^2}.}
\]
The latter decreases strictly on \((0,1/2)\) and increases strictly on \((1/2,1)\), with its unique minimum \(4/3\) at the balanced difference body and endpoint values \(2\).

For \(0<\lambda<1/2\), the unique point of maximal lattice-gauge distance in \(\mathbb R^2/\mathbb Z^2\) is represented by \(((1-\lambda)/(1+\lambda),(1-\lambda)/(1+\lambda))\). For \(1/2<\lambda<1\), it is represented by \((2(1-\lambda)/(2-\lambda),2(1-\lambda)/(2-\lambda))\). At \(\lambda=1/2\) there are precisely two such points, represented by \((1/3,1/3)\) and \((2/3,2/3)\). All conclusions are invariant under a simultaneous unimodular change of basis.

## Assumptions and scope
For a full-dimensional compact convex set \(K\subset\mathbb R^2\) and the lattice \(\Lambda=\mathbb Z^2\), define
\[
\mu_\Lambda(K)=\inf\{r\ge0:rK+\Lambda=\mathbb R^2\}.
\]
If the origin lies in the interior of \(K\), let \(g_K(z)=\inf\{r\ge0:z\in rK\}\) be its Minkowski gauge. The function \(z\mapsto\min_{k\in\Lambda}g_K(z-k)\) is periodic; its maxima modulo \(\Lambda\) are the deepest holes. The unique-versus-two deepest-hole classification only concerns \(0<\lambda<1\), when the body contains the origin in its interior. The covering-radius and area formulas include both triangular endpoints. The density \(\Theta_\Lambda\) is that of the minimum-radius lattice covering, not the unrestricted optimum over all lattices.

## Proof
**1. Explicit Minkowski hexagon.** For \(t>0\), let \(K_t=T+t(-T)\). Direct maximization of the six facet directions, or convexification of the sums of the two vertex sets, gives
\[
K_t=\{(u,v):-t\le u,\ v,\ u+v\le1\}.
\]
The six vertices in cyclic order are \((1,0),(1,-t),(0,-t),(-t,0),(-t,1),(0,1)\). The shoelace formula gives
\[
\operatorname{area}(K_t)=\frac{1+4t+t^2}{2}.
\]
Its gauge is the elementary maximum
\[
 g_t(u,v)=\max\{u,v,u+v,-u/t,-v/t,-(u+v)/t\}.
\]

**2. Exact covering for \(0<t\le1\).** Put \(a=1/(1+2t)\), \(s=2a\). Then \(1/3\le a<1\), \(st=1-a\), and \(4a\ge1+a\). We show that the four translates \(sK_t+(0,0),(1,0),(0,1),(1,1)\) cover \([0,1]^2\).

Given \((x,y)\in[0,1]^2\), if \(x+y\le2a\), its two nonnegative coordinates and their sum satisfy all six inequalities for \(sK_t\). If \(x+y\ge1+a\), both coordinates are at least \(a\); thus \((x-1,y-1)\) has both components in \([-st,0]\), with sum at least \(-st\), and is in \(sK_t\).

Suppose instead that \(2a<x+y<1+a\). At least one coordinate is at least \(a\), and at least one is at most \(2a\). More precisely there is an ordering with \(x\ge a\) and \(y\le2a\), or the reversed ordering: if this failed, either both coordinates would be less than \(a\), contradicting the lower sum bound, or both would exceed \(2a\), contradicting \(x+y<1+a\le4a\). In the first ordering, \(x-1\ge a-1=-st\), \(0\le y\le s\), and \(-st<x+y-1<s\). Consequently \((x-1,y)\in sK_t\); the other ordering uses the translate \((0,1)\). This proves \(\mu_\Lambda(K_t)\le s\).

For the reverse inequality consider \(p=(a,a)\). If \(p\in sK_t+k\) for an integer vector \(k\), each coordinate of \(k\) must lie in \(\{0,1\}\): a coordinate \(\le-1\) gives a residual exceeding \(s\), while one \(\ge2\) gives a residual below \(-st\). Of the four candidates, \(k=(0,0)\) gives residual sum \(2a=s\); \(k=(1,0)\) or \((0,1)\) gives one residual coordinate \(a-1=-st\); and \((1,1)\) fails the residual sum lower bound. Thus \(p\) lies on the boundary of every covering translate that contains it. Since \(K_t\) contains the origin in its interior, \(p\) lies in no smaller common dilate, and \(\mu_\Lambda(K_t)\ge s\). Therefore
\[
\mu_\Lambda(K_t)=\frac2{1+2t}\quad (0<t\le1).
\]

**3. Reflection and normalization.** The identity \(K_t=-tK_{1/t}\) and the invariance of the covering radius under a central reflection give \(\mu_\Lambda(K_t)=t^{-1}\mu_\Lambda(K_{1/t})=2/(t+2)\) for \(t\ge1\). For \(0<\lambda<1\), put \(t=\lambda/(1-\lambda)\), so \(S_\lambda=(1-\lambda)K_t\) and \(\mu_\Lambda(S_\lambda)=\mu_\Lambda(K_t)/(1-\lambda)\). This is the claimed piecewise formula. At \(\lambda=0\) and \(\lambda=1\), each endpoint is a reflected standard unimodular triangle of covering radius \(2\): the unit square fits in \(2T\), and points approaching \((1,1)\) from below cannot be covered by a smaller dilate of \(T\).

**4. Area and density.** Scaling the area identity in step 1 yields \(\operatorname{area}(S_\lambda)=[1+2\lambda(1-\lambda)]/2\). Multiplying by the square of the proved covering radius yields the density formula. For \(0<\lambda<1/2\), direct differentiation gives
\[
\frac{d}{d\lambda}\Theta_\Lambda(S_\lambda)
=-\frac{12\lambda}{(1+\lambda)^3}<0.
\]
Symmetry under \(\lambda\mapsto1-\lambda\) proves strict increase on the other side and the stated endpoint and minimum values.

**5. Exact deepest-hole bifurcation.** The coverage proof also determines equality. For \(0<t\le1\), within the open region \(x+y<2a\), the translate at the origin covers strictly, and within \(x+y>1+a\), the translate at \((1,1)\) covers strictly. In the intervening open strip, when \((x-1,y)\in sK_t\), all its inequalities are strict except possibly when \(x=a\) or \(y=2a\). If \(x=a\), the alternative translate \((0,1)\) covers strictly because \(y>a\); if \(y=2a\), that same translate covers strictly because \(a<y\) and \(x<1-a\le2a\). The symmetric ordering is identical. On the boundary \(x+y=2a\), one of the two mixed translates covers strictly except when \(x=y=a\). On \(x+y=1+a\), a mixed translate covers strictly except when \(a=1/3\) and \(x=y=2/3\). Hence the sole deepest hole for \(0<t<1\) is \((a,a)\); for \(t=1\) the deepest holes are \((1/3,1/3)\) and \((2/3,2/3)\). Reflection by \(K_t=-tK_{1/t}\) reflects these periodic maximizers to \((-a,-a)\) for \(t>1\); converting modulo \(\mathbb Z^2\) and replacing \(t\) by \(\lambda/(1-\lambda)\) gives precisely the three parameter cases in the finding.

The unimodular version follows from \(U\mathbb Z^2=\mathbb Z^2\) and area invariance for every \(U\in\mathrm{GL}_2(\mathbb Z)\).

## Verification
An independent rational-arithmetic script `verify_covering.py` checks all six hexagon vertices, the shoelace area, radius reciprocity under reflection, and explicit deepest-hole identities. It also checks the covering inequality at \(6{,}728\) rational test points across eight positive rational choices of \(t\), together with density endpoint values. Run from the unpacked package with `python verify_covering.py`; the expected output begins `PASS: 6728 exact rational grid-point checks`. The infinite statements and exact classifications are established by the geometric proof, not by finite enumeration.

## Relationship to prior work
Codenotti, Freyer and Krivokuća, *Minimal covering bodies and Brunn–Minkowski type inequalities for the covering radius* (arXiv:2606.14442v1, first public 2026-06-12), prove sharp general inequalities concerning the covering radius of planar Minkowski sums and exhibit a sharp pair of covering parallelograms. Their published general lower bound does not specify the covering radius of the asymmetric simplex-plus-reflection family at each parameter; their pair of parallelograms yields an opposite-shaped interpolation profile. Codenotti, Santos and Schymura, *The Covering Radius and a Discrete Surface Area for Non-Hollow Simplices* (2021; DOI below), study lattice simplex covering radii and include the standard unimodular simplex as a known exact case, but do not state the two-triangle reflection interpolation and its density/deepest-hole changes.

A separate published calculation of simplex-asymmetric-difference-body **Mahler product** studies a polarity/volume-product invariant, not a fixed-lattice covering radius. The distinction of invariants matters: its rational volume-product formula does not provide a covering or a deepest-hole certificate. A public published exact covering profile of a **pair of parallelograms** likewise concerns different bodies and yields a different numerical function. These are the closest identified comparisons, not claims of a comprehensive proof of bibliographic uniqueness.

## Limitations
The covering lattice is fixed to \(\mathbb Z^2\) (or its simultaneous affine unimodular images). The result does not assert a covering optimum among arbitrary planar lattices, any higher-dimensional analogue, or a new universal Brunn–Minkowski inequality. The deepest-hole assertion concerns positive weights on both triangles; the singular triangle endpoints are excluded. A pre-existing exact interpolation calculation under alternative terminology remains a bibliographic risk; scientific priority has not received independent adjudication.

## References
1. G. Codenotti, A. Freyer, K. Krivokuća, *Minimal covering bodies and Brunn–Minkowski type inequalities for the covering radius*, arXiv:2606.14442v1 (2026-06-12), https://arxiv.org/abs/2606.14442.
2. G. Codenotti, F. Santos, M. Schymura, *The Covering Radius and a Discrete Surface Area for Non-Hollow Simplices*, Discrete & Computational Geometry **67** (2022), 65–111, first online 2021-11-17, https://doi.org/10.1007/s00454-021-00330-3.
3. Published comparison: *Exact covering-radius profile of the sharp planar parallelogram pair* (2026), publicly indexed geometric result; full mathematical statement compared.
4. Published comparison: *Strict Mahler-product monotonicity along simplex asymmetric difference bodies* (2026), published geometric finding on a different invariant.
