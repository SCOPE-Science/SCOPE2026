# All 65 nodes of the characteristic-five Barth sextic are split and reduced

## Finding

Let \(R=\mathbb Z[\tau]/(\tau^2-\tau-1)\). The prime \((5,\tau-3)\) is the unique prime of \(R\) above \(5\). Consider the homogeneous Barth sextic over \(R\):

\[
4(\tau^2X^2-Y^2)(\tau^2Y^2-Z^2)(\tau^2Z^2-X^2)
 -(1+2\tau)(X^2+Y^2+Z^2-W^2)^2W^2=0.
\]

Over \(k=\overline{\mathbb F}_5\), its special fiber is the sextic surface \(B_5\subset\mathbb P_k^3\) defined by

\[
F=(X^2+Y^2)(Y^2+Z^2)(Z^2+X^2)-2(X^2+Y^2+Z^2-W^2)^2W^2.
\]

**Theorem.** The complete geometric singular locus of \(B_5\) consists of exactly \(65\) ordinary double points, all rational over \(\mathbb F_5\). In the chart \(W=1\) the squared-coordinate triples, up to permutation, are precisely

\[
(0,0,1),\quad (0,4,4),\quad (1,1,1),\quad (1,1,4),
\]

with \(6,12,8,24\) distinct points respectively, a total of \(50\). The remaining \(15\) are the pairwise intersections of the six distinct lines in \(W=0\):

\[
X=\pm2Y,\qquad Y=\pm2Z,\qquad Z=\pm2X.
\]

The projective Jacobian singular scheme is reduced of degree \(65\). In particular \(B_5\) is geometrically integral and normal.

## Assumptions and scope

The base is an algebraically closed field \(k\) of characteristic exactly \(5\), with its prime subfield \(\mathbb F_5\). The ambient space is \(\mathbb P^3_k\), not affine three-space. The integral model is the displayed sextic over \(R\); its meaning at the ramified prime is fixed by the specified specialization \(\tau\mapsto3\). An ordinary double point means a surface hypersurface germ with nondegenerate quadratic tangent cone in three local variables.

## Proof

**Reduction.** In \(R/(5,\tau-3)\), \(\tau^2=4=-1\), \(1+2\tau=2\), and \(4(-1)^3=1\). The displayed equation therefore reduces identically to \(F\).

**All affine singular points.** Set \(W=1\), put \(a=x^2,b=y^2,c=z^2\), and write \(s=a+b+c\). The affine equation is

\[
f=(a+b)(b+c)(c+a)-2(s-1)^2.
\]

Writing \(T=s^2+s-1\), direct formal differentiation in characteristic five yields

\[
(f_x,f_y,f_z)=\bigl(2x(T-a^2),2y(T-b^2),2z(T-c^2)\bigr).
\]

Let \((x,y,z)\) be a geometric singular point. If all three coordinates vanish then \(f=-2\ne0\). If precisely one is nonzero, the equation forces its square to be \(1\), giving the six points of squared type \((0,0,1)\).

If precisely two are nonzero, write their squares as \(a,b\). The derivative equations imply \(a^2=b^2\), hence \(b=a\) or \(b=-a\). In the second case \(s=0\) and \(f=-2\ne0\). In the first case the derivative equation is \(3a^2+2a-1=0\), whose roots in characteristic five are \(2,4\). Substitution into \(f\) leaves only \(a=4\). Thus this case consists of the twelve points of type \((0,4,4)\).

If all three are nonzero, the derivatives give \(a^2=b^2=c^2=T\). Write \(a,b,c\in\{t,-t\}\) for some \(t\ne0\). When all three are equal, the derivative condition becomes \(3t^2+3t-1=0\), with roots \(1,3\); the equation \(f=0\) leaves only \(t=1\), producing eight points of type \((1,1,1)\). Otherwise, up to permutation the squares are \((t,t,-t)\), so \(s=t\) and the derivative condition says \(t^2=t^2+t-1\), hence \(t=1\). The equation then vanishes, and the remaining twenty-four points have type \((1,1,4)\). This proves geometric completeness of the affine list over \(k\), without inference from a finite-field enumeration.

**Affine tangent cones.** For \(v=(x,y,z)\), \(a_i=v_i^2\), the Hessian entries at any point are

\[
H_{ii}=2(T-a_i^2)+4a_i(2s+1-2a_i),\qquad
H_{ij}=4v_iv_j(2s+1)\quad(i\ne j).
\]

At the respective representatives \((0,0,1),(0,2,2),(1,1,1),(1,1,2)\), the determinants \(\det H\) modulo five are \(1,4,4,1\). Permuting coordinates or changing individual signs leaves the determinant unchanged. Hence all \(50\) affine points have nondegenerate quadratic tangent cones and are ordinary double points.

**The plane at infinity.** At \(W=0\), the defining polynomial is \((X^2+Y^2)(Y^2+Z^2)(Z^2+X^2)\). Since \(-1=2^2\) in \(\mathbb F_5\), this is a product of the six distinct linear equations listed in the theorem. No three are concurrent: simultaneous vanishing of any two different quadratic factors gives, up to permutation, \(X^2=Z^2=-Y^2\), whence the third factor is \(-2Y^2\ne0\); the two lines from any one factor meet at a coordinate vertex not on the other factors. Thus the six-line arrangement has precisely \(\binom 62=15\) distinct pairwise intersections, all rational over \(\mathbb F_5\). Since the derivative with respect to \(W\) vanishes identically on \(W=0\), precisely those fifteen points are singular on the surface.

For each such point \(P\), \(S(P):=X(P)^2+Y(P)^2+Z(P)^2\ne0\): at the coordinate vertices this is clear, while at a meeting of different quadratic factors it equals the negative square of the shared nonzero coordinate. In local coordinates \(u,v,w\), where \(u,v\) are the two incident line equations, the quadratic tangent cone of the surface is

\[
\lambda uv-2S(P)^2w^2,
\]

with \(\lambda\ne0\). In characteristic five this is a nondegenerate ternary quadratic form. All fifteen points at infinity are therefore ordinary double points.

**Scheme structure and integrality.** At an ordinary double point in characteristic different from two, the invertible Hessian implies that the local Jacobian ideal cuts out its reduced residue point. The singular scheme is therefore exactly the disjoint union of these sixty-five rational reduced points, of degree \(65\). Because the hypersurface has only isolated singularities, it cannot be reducible or nonreduced over \(k\): distinct projective surface components in \(\mathbb P^3\) meet along a curve and repeated components are singular in positive dimension. The hypersurface satisfies \(S_2\), and isolated singularities give \(R_1\); by Serre's criterion it is normal.

## Verification

Execute `python3 check.py` using the standard Python library. This checks the finite-field polynomial specialization, finds the \(50\) affine rational singular points with the stated squared-coordinate distributions, evaluates every affine Hessian determinant, and checks the fifteen infinity intersections together with their nonzero transverse-square coefficients. The code does **not** use finite enumeration as proof that there are no other geometric points; that statement follows from the exhaustive algebraic case split above. The explicit Hessian formulas are reproduced in the checker.

## Relationship to prior work

Barth's classical sextic and its \(65\) nodes over the complex numbers are established facts; no construction or complex node count is claimed as new. The 1994 Jaffe preprint already cites Barth's \(65\)-node construction. The historical equation is reproduced by Oliver Labs and by the full 2017 exposition of Bauer–Hulek–Rams–Sarti–Szemberg. MathWorld also describes the classical \(50+15\) distribution. A finite-field computation in the Orbiter documentation discusses a reduction at characteristic eleven. The statement proved here instead concerns the **ramified prime five**, proves noncollision and nondegeneracy after reduction, and identifies the exact split Jacobian scheme over \(\mathbb F_5\). Statements over \(\mathbb C\), and finite-field computations in characteristic eleven, do not imply this without additional reduction and tangent-cone checks.

## Limitations

The statement is for the specified projective integral model and its indicated characteristic-five specialization, not every integral model or every twist of the sextic. The familiar characteristic-zero upper bound of \(65\) nodes is not asserted as a general upper bound in characteristic five. The complete original 1996 article was not available for direct inspection; equivalent older modular descriptions or explicit coordinates that immediately specialize could weaken originality. No independent scientific validation has been carried out.

## References

- W. Barth, *Two projective surfaces with many nodes, admitting the symmetries of the icosahedron*, Journal of Algebraic Geometry **5** (1996), 173–186.
- D. B. Jaffe, *On sextic surfaces having only nodes (preliminary report)*, arXiv:alg-geom/9411012, first posted 1994-11-17. https://arxiv.org/abs/alg-geom/9411012
- T. Bauer, K. Hulek, S. Rams, A. Sarti, and T. Szemberg, *Wolf Barth (1942–2016)*, Jahresbericht der Deutschen Mathematiker-Vereinigung (2017), section 2.4. https://link.springer.com/article/10.1365/s13291-017-0164-7
- O. Labs, *The Barth Sextic*, IMAGINARY explanatory board, page 1. https://www.imaginary.org/sites/default/files/explanation-boards-Oliver-Labs_EN.pdf
- E. Weisstein, *Barth Sextic*, MathWorld. https://mathworld.wolfram.com/BarthSextic.html
- A. Betten and collaborators, *Orbiter Users Guide*, example computing the Barth sextic over \(\mathbb F_{11}\) (search-visible excerpt; full document not inspected). https://www.math.colostate.edu/~betten/orbiter/users_guide.pdf
