# The flat length-24 singular scheme and Cremona dual of primitive Heisenberg quartics in characteristic two

## Finding

Let \(k\) be an algebraically closed field of characteristic \(2\), and let \(a,e\in k^\times\) and \(b,c,d\in k\). Consider the normal quartic surface \(X_{a,b,c,d,e}\subset\mathbf P^3_k\) cut out by
\[
\begin{aligned}
F={}&a(x^4+y^4+z^4+w^4)\\
&+b(x^2y^2+z^2w^2)+c(x^2z^2+y^2w^2)\\
&+d(x^2w^2+y^2z^2)+e\,xyzw.
\end{aligned}
\]
The adjective *primitive* specifies that the five displayed integral monomial orbit sums, without factors of \(2\) or \(4\), are retained before reduction; it does not assert that the characteristic-two fiber is invariant under a nondegenerate Heisenberg group scheme.

Set \(r=\#\{\beta\in\{b,c,d\}\text{ counted with their indices}:\beta=0\}\). Then:

1. The complete scheme-theoretic singular locus \(\Sigma=V(F,F_x,F_y,F_z,F_w)\) is the disjoint union of six length-four Cartier divisors on the coordinate edges. It has length \(24\). More strongly, \(\Sigma\) is finite flat of rank \(24\) over the coefficient base \(\operatorname{Spec}k[a,a^{-1},b,c,d,e,e^{-1}]\).
2. An edge with coefficient \(\beta\in\{b,c,d\}\) contributes two distinct \(A_1\) singularities, each with local Jacobian length \(2\), if \(\beta\ne0\); it contributes one \(A_3\) singularity, with local Jacobian length \(4\), if \(\beta=0\). Therefore the entire ADE basket is exactly
\[
(12-4r)A_1+2rA_3,
\]
with \(12-2r\) distinct singular points. There are no other singularities. The minimal resolution is a K3 surface with \(12+2r\) exceptional \((-2)\)-curves.
3. The Gauss map of \(X\) is the restriction, on the dense coordinate torus, of the standard cubic Cremona involution
\[
[x:y:z:w]\longmapsto[yzw:xzw:xyw:xyz].
\]
It is separable and birational onto its dual surface. That dual surface is the degree-\(12\) irreducible hypersurface obtained by applying the same Cremona substitution to \(F\). Thus all four ADE strata have the same dual degree \(12\), despite their different reduced singular-point counts.

This gives a complete wall-crossing classification on the open parameter set \(ae\ne0\): the ADE basket changes exactly along \(bcd=0\), but the singular scheme's flat length and the dual degree do not change.

## Assumptions and scope

Throughout, \(k\) is algebraically closed of characteristic \(2\); there are no restrictions on \(b,c,d\), including intersections of the three coordinate walls. Both \(a\) and \(e\) must be nonzero. Results concern the stated *primitive integral monomial-orbit spread* and its special fiber, not the direct characteristic-two reduction of the differently scaled generators in Eklund's complex parametrization. No assertion is made for \(a=0\), \(e=0\), or for other integral lattices with the same characteristic-zero generic fiber.

The coefficients of the six edges are paired as follows: \(b\) belongs to edges \(xy\) and \(zw\), \(c\) to \(xz\) and \(yw\), and \(d\) to \(xw\) and \(yz\).

## Proof

**0. Why the integral model is natural.** The integral sign changes \((x,y,z,w)\mapsto(x,y,-z,-w)\) and \((x,y,z,w)\mapsto(x,-y,z,-w)\) force the exponents of any invariant degree-four monomial to have the same parity. Thus the only possible exponent types are one fourth power, a product of two squares, or \(xyzw\). The two double transpositions \((x,y,z,w)\mapsto(z,w,x,y)\) and \((x,y,z,w)\mapsto(y,x,w,z)\) partition these monomials into exactly five orbits: the four pure powers, the three distinct perfect matchings of pairwise squares, and the product \(xyzw\). Their orbit sums have disjoint monomial supports and constitute a primitive \(\mathbf Z\)-basis of the degree-four invariants of these integral signed permutations. Therefore the unscaled five-term family is a canonical saturated integral spread, even though its characteristic-two symmetry group is degenerate.

**1. The complete singular scheme and flatness.** Since the derivatives of every square vanish in characteristic \(2\), the four partial derivatives are exactly
\[
(F_x,F_y,F_z,F_w)=e(yzw,xzw,xyw,xyz).
\]
As \(e\) is invertible, their saturated homogeneous ideal is the squarefree monomial ideal \((yzw,xzw,xyw,xyz)\). Its projective zero locus is the reduced union of the six coordinate edges of the tetrahedron. The four vertices are excluded from \(X\), because at each vertex \(F=a\ne0\). Consequently these six edge intersections with \(X\) are pairwise disjoint, even scheme-theoretically.

For each edge with homogeneous coordinates \([u:v]\) and associated \(\beta\), the restricted equation is
\[
a(u^4+v^4)+\beta u^2v^2=0.
\]
This is a degree-four effective Cartier divisor on \(\mathbf P^1\) because \(a\ne0\); the affine chart \(v=1\) contains all its zeros and gives the monic polynomial \(u^4+(\beta/a)u^2+1\). Hence each edge contributes a finite flat family of rank \(4\) over the entire coefficient base. Their disjoint union is exactly the relative Jacobian singular scheme and has rank \(6\cdot4=24\).

**2. Support and multiplicities.** In the algebraically closed field, the edge equation is the square
\[
\bigl(\sqrt a(u^2+v^2)+\sqrt\beta\,uv\bigr)^2.
\]
If \(\beta\ne0\), the binary quadratic in parentheses has two distinct roots (its derivative in the coordinate \(u/v\) is \(\sqrt\beta\ne0\)), each of multiplicity two after squaring. If \(\beta=0\), it is \(\sqrt a(u+v)^2\), so its square has one root of multiplicity four. All roots have \(uv\ne0\) because \(a\ne0\). Summing across the two edges for each \(\beta\) gives the stated support count and multiplicities.

**3. Intrinsic ADE types.** Work at a point on any edge. Choose local edge parameter \(s\) vanishing at the point, and two coordinates \(u,v\) transverse to the edge. The restriction \(h(s)=F(s,0,0)\) vanishes to exact order \(m=2\) when \(\beta\ne0\), and \(m=4\) when \(\beta=0\). More explicitly, in a chart where the edge is \(y=1,z=w=0\) and the root is \(x=t\), put \(x=t+s\). The characteristic-two binomial identities and the edge-root equation give exactly \(h(s)=\beta s^2+a s^4\); hence its order is as asserted, with no higher-order ambiguity. In the local equation, the polar pairing of the quadratic part in \(u,v\) has coefficient \(e\,xy\), where \(x,y\) denote the two nonzero edge coordinates; this is a unit along the entire formal edge neighborhood. All other terms arise from squares and therefore have zero transverse polar pairing. Moreover, \(u=v=0\) is a critical section in the two transverse directions: both transverse derivatives vanish identically there.

The formal splitting lemma for a nondegenerate binary quadratic polar form over the complete coefficient ring \(k[[s]]\) now applies: the transverse quadratic form splits into two distinct linear factors over the algebraically closed residue field, their changes of variables lift formally, and successive higher-order terms are absorbed inductively into the two transverse coordinates. The critical section remains at the origin, hence the constant term stays \(h(s)\). Thus the completed local equation is \(UV+h(s)\). As \(h(s)=s^m\cdot\varepsilon(s)\) with \(\varepsilon(0)\ne0\), scaling \(U\) by a unit yields \(UV+s^m\). These are precisely the rational double point normal forms \(A_1\) (\(m=2\)) and \(A_3\) (\(m=4\)) in characteristic two. Direct differentiation of the normal form yields completed Jacobian algebra \(k[[s]]/(s^m)\), in agreement with the edge-divisor calculation.

**4. Normality and K3 resolutions.** The singular locus is finite. A nontrivial factorization of the quartic into hypersurfaces in \(\mathbf P^3\) would force an entire intersection curve into its singular locus; a repeated factor would likewise force a positive-dimensional singular set. Therefore \(F\) is absolutely irreducible and reduced. The hypersurface is \(S_2\), and its finite singular locus gives regularity in codimension one, so Serre's criterion proves normality. Resolving rational double points is crepant; adjunction gives trivial canonical sheaf, and the hypersurface cohomology sequence gives \(H^1(\mathcal O_X)=0\). Thus its minimal resolution is K3. An \(A_1\) contributes one exceptional curve, and an \(A_3\) contributes three, giving \((12-4r)+3(2r)=12+2r\) curves.

**5. The dual.** The displayed derivatives show that on \(xyzw\ne0\) the Gauss map is the standard cubic Cremona involution \(\tau\). The map is an isomorphism of the ambient projective coordinate torus and is its own inverse there; hence its restriction to the dense torus of the irreducible surface \(X\) is birational and separable onto its image. The closure is cut out by
\[
G(X,Y,Z,W)=F(YZW,XZW,XYW,XYZ).
\]
Every monomial of \(G\) has degree \(12\). Its characteristic-two Laurent-polynomial zero set on the torus is the birational transform of the geometrically integral reduced hypersurface \(F=0\); therefore its torus equation is reduced and irreducible. No coordinate is a factor of \(G\): the four nonzero monomials \(a(YZW)^4\), \(a(XZW)^4\), \(a(XYW)^4\), \(a(XYZ)^4\) each miss one distinct coordinate, and their exponent patterns are all different. Consequently \(G\) is irreducible as a homogeneous polynomial and defines the dual hypersurface with degree exactly \(12\).

## Verification

The self-contained `verify.py` performs exact arithmetic over \(\mathbf F_4\), with all projective points of \(\mathbf P^3(\mathbf F_4)\) exhaustively enumerated. For \(a=e=1\) and four representatives with respectively \(r=0,1,2,3\), it checks the exact gradient, the singular-point counts \(12,10,8,6\), the six edge supports, the multiplicity-weighted total \(24\), and the predicted \(A_1/A_3\) counts. Separately it checks the support of the degree-twelve transformed polynomial and verifies the Cremona involution identity at every coordinate-torus point over \(\mathbf F_4\).

Run `python3 verify.py` from this directory; it prints a line beginning `VERIFY_OK` on success. The infinite-field classification, formal local normal forms, geometric normality, and geometric dual degree are proved algebraically above, not inferred from finite-field tests.

## Relationship to prior work

Eklund, *Curves on Heisenberg invariant quartic surfaces in projective 3-space* (first preprint 19 October 2010, arXiv:1010.4058), Section 2.3, studies the five-dimensional invariant linear system in characteristic zero. His generators are scaled as \(g_0=M_0\), \(g_1=2M_1\), \(g_2=2M_2\), \(g_3=2M_3\), and \(g_4=4M_4\), where \(M_i\) are exactly the unscaled monomial sums here. Naively reducing **those scaled generators** modulo two yields only \(M_0\) and **does not** give our quartic family. Instead, we choose the saturated degree-four integral invariant lattice generated by the five primitive orbit sums before reduction. This distinction is essential; all special-fiber assertions depend on it. The results here do not follow from the characteristic-zero smoothness, Picard or conic statements.

Catanese, *Singularities of normal quartic surfaces I (char=2)* (arXiv:2106.09988), Section 4, treats the fully symmetric quartic subsystem, including a known twelve-singular-point locus. That contains the symmetric specialization \(b=c=d\) of the present family at the level of reduced support, so that specialization's singular-point count is **not claimed as new**. The source does not directly supply the three independent pairing-parameter walls, their simultaneous \(A_1\)-to-\(A_3\) collisions, the constant relative Jacobian length \(24\), or the degree-twelve Cremona dual identification for every member of the present family.

Catanese and Schütt, *Singularities of normal quartic surfaces II (char=2)* (arXiv:2110.03078), establishes general bounds and analyzes characteristic-two quartics and Gauss maps. Its general statements on the maximum number of singular points, ADE types, and Gauss estimates are consistent with the current classification but do not, in the material inspected, state or imply the coefficientwise classification and finite-flat scheme above. The singular-support computation, exact local types, and dual equation are supplied here.

Catanese and Schütt, *Singularities of normal quartic surfaces III (char=2, non-supersingular)* (arXiv:2206.03295), Example 19, is especially close: it already studies the **broader** characteristic-two family \(q^2+l_1l_2l_3l_4=0\), states that its generic member has twelve nodes, and records six \(A_3\) singularities in its classical symmetric Dwork specialization. Thus neither the generic twelve-node count nor the six-\(A_3\) endpoint nor the mere equation \(q^2+xyzw\) is new. The precise contribution here is the all-parameter classification of the natural *primitive Heisenberg invariant subspread* with its three independent pairing walls, **scheme-theoretic finite-flat length \(24\)** and universal **degree-\(12\) separable Cremona dual**. Example 19 does not state these combined scheme, wall or dual assertions. This is the closest implication comparison and makes the result more narrowly scoped than a claim of inventing a twelve-nodal family.

## Limitations

The result concerns the exact five-term primitive integral spread, restricted to the coefficient-open set \(ae\ne0\); different integral scalings have different reductions. The assertion of originality is necessarily conditioned on the inspected material, since specialized coordinate changes or older treatments of this particular characteristic-two spread might already encode the same calculations. This note gives no independent audit or external validation, and it does not compute the full Néron–Severi lattices of the resolved K3 surfaces. The finite-field test cannot establish the universal statements without the proof given above.

## References

1. D. Eklund, *Curves on Heisenberg invariant quartic surfaces in projective 3-space*, arXiv:1010.4058, first submitted 2010-10-19, especially Section 2.3 (five invariant generators and their integer scaling).
2. F. Catanese, *Singularities of normal quartic surfaces I (char=2)*, arXiv:2106.09988, especially Section 4 (symmetric quartics).
3. F. Catanese and M. Schütt, *Singularities of normal quartic surfaces II (char=2)*, arXiv:2110.03078, especially Sections 1–3 (singularities, Gaussian defects and dual varieties).
4. F. Catanese and M. Schütt, *Singularities of normal quartic surfaces III (char=2, non-supersingular)*, arXiv:2206.03295, especially Example 19 (general \(q^2+l_1l_2l_3l_4\) quartics, generic twelve nodes, and special six \(A_3\) points).
