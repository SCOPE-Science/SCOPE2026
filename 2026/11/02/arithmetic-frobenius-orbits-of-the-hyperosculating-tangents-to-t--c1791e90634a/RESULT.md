# Arithmetic Frobenius orbits of the hyperosculating tangents to the Klein quartic in characteristic three

## Finding
Let \(K\subset\mathbf P^2_{\mathbb F_3}\) be the plane curve
\[
K:\quad X^3Y+Y^3Z+Z^3X=0.
\]
For a geometric point \(P\in K\), call its tangent **hyperosculating** if its intersection multiplicity with \(K\) at \(P\) equals four. Every geometric tangent has contact order at least three, but exactly **28** tangent lines are hyperosculating. They are in bijection with the \(28\) distinct roots in \(\overline{\mathbb F}_3\) of
\[
 u^{91}=1,\qquad u^{28}+u^7+1=0,
\]
via
\[
P_u=[1:u^{10}:u],\qquad
L_u:\ u^3X+Y+u^{30}Z=0.
\]
The absolute Frobenius \(u\mapsto u^3\) has **six** orbits on these \(28\) points (and on their tangent lines), with orbit sizes
\[
\boxed{1,\ 3,\ 6,\ 6,\ 6,\ 6}.
\]
Consequently, for every integer \(n\ge1\), the number of \(\mathbb F_{3^n}\)-rational hyperosculating tangent lines, equivalently of rational hyperosculation points, is
\[
\boxed{H(n)=1+3\mathbf1_{3\mid n}+24\mathbf1_{6\mid n}}.
\]
Their smallest common finite splitting field is \(\mathbb F_{3^6}\), although the curve and its tangent map are defined over \(\mathbb F_3\). No line is tangent at two distinct geometric points. These last statements concern fourfold contacts, **not** the entire flex locus: every geometric point is an ordinary flex or a hyperflex in characteristic three.

## Assumptions and scope
All equations use the displayed integral plane model reduced modulo \(3\), and all points are geometric unless a field is explicitly indicated. A tangent line is rational over a field when its homogeneous coefficients admit a common normalization in that field. The symbol \(\mathbf1_E\) denotes \(1\) when condition \(E\) holds and \(0\) otherwise. Hyperosculation is the exact intersection multiplicity \(4\) on a smooth degree-four curve; this condition is intrinsic and does not invoke the classical Hessian, which vanishes identically in this characteristic.

## Proof
**1. Smoothness and tangent contact.** Write \(F=X^3Y+Y^3Z+Z^3X\). In characteristic three,
\[
(F_X,F_Y,F_Z)=(Z^3,X^3,Y^3),
\]
which cannot vanish simultaneously at a projective point. Thus \(K\) is smooth and geometrically integral of genus \(3\). At \(P=[a:b:c]\) its tangent line is
\[
L_P:\ c^3X+a^3Y+b^3Z=0.
\]
For any vector \(D=(r,s,t)\), the exact expansion is
\[
F(P+hD)=F(P)+h(c^3r+a^3s+b^3t)
+h^3(br^3+cs^3+at^3)+h^4F(D).
\]
There is no quadratic term: every tangent has intersection multiplicity at least \(3\). On each coordinate point the tangent has contact exactly \(3\); for example, at \([1:0:0]\) the line \(Y=0\) cuts out \(XZ^3=0\), giving intersection multiplicity \(3\) at that point. Cyclic symmetry treats the other two. Any hyperosculation point therefore satisfies \(abc\ne0\).

**2. Exact hyperosculation criterion.** Since the field is perfect, the cubic coefficient above is the cube of a linear functional. It vanishes on the whole tangent plane to \(K\) at \(P\) precisely when it is a scalar multiple of the cube of the linear tangent equation. Comparing coefficients yields
\[
(b,c,a)=\gamma(c^9,a^9,b^9).
\]
Normalize \(a=1\) and put \(c=u\). Comparison of the middle coefficient gives \(\gamma=u\); the remaining two give
\[
b=u^{10},\qquad ub^9=1.
\]
Thus \(u^{91}=1\). Conversely these two equations ensure equality of the cubic functional with \(uL_P^3\). Substitution into \(F(P)=0\) yields
\[
0=u^{10}+u^{31}+u^3=u^3(u^7+u^{28}+1).
\]
Since \(u\ne0\), the complete geometric hyperosculation locus consists exactly of the displayed \(P_u\) with the two equations in the finding. At each, the degree-four line intersection has multiplicity exactly \(4\), because a line cannot be a component of the smooth irreducible quartic. The tangent expression becomes \(u^3X+Y+u^{30}Z=0\); the nonzero \(Y\)-coefficient also shows that distinct \(u\) yield distinct tangents.

**3. Number and Frobenius orbits.** Set \(v=u^7\). The geometric conditions become
\[
 v^4+v+1=(v-1)(v^3+v^2+v-1)=0,\qquad v^{13}=1.
\]
The cubic has no root in \(\mathbb F_3\), hence is irreducible. Moreover \(v^4+v+1\) divides \(v^{13}-1\) over \(\mathbb F_3\); direct polynomial division verifies this identity. Therefore the four \(v\)-roots consist of \(1\) and three primitive thirteenth roots, all simple. Each has seven distinct preimages under the separable map \(u\mapsto u^7\) among the ninety-first roots, so there are exactly \(28\) hyperosculation points. When \(v=1\), one preimage \(u=1\) has order \(1\) and six have order \(7\). For each of the three primitive-thirteenth-root values of \(v\), exactly one preimage belongs to the group of thirteenth roots (because exponent seven is invertible modulo thirteen), and the other six have exact order \(91\). Thus the counts by multiplicative order are
\[
\#\{\operatorname{ord}(u)=1,7,13,91\}=(1,6,3,18).
\]
The multiplicative orders of \(3\) modulo \(7,13,91\) are respectively \(6,3,6\). Hence Frobenius orbit sizes are \(1,6,3,6,6,6\), giving the asserted six orbits and the formula for \(H(n)\). The displayed normalized tangent coefficient \(u^3\) belongs to \(\mathbb F_{3^n}\) if and only if \(u\) does (Frobenius is bijective), so points and tangents have identical fields of definition. Since order \(91\) occurs, their least common field is exactly \(\mathbb F_{3^6}\).

**4. Exclusion of other doubly tangent lines.** Every tangent to \(K\) has contact order at least \(3\). If one line were tangent at two distinct points it would intersect the quartic with total multiplicity at least \(3+3=6\), contradicting Bézout's theorem. Thus the hyperosculating lines constitute the only special bitangent-like contacts, with contact \(4\) at a single point, and there are no two-point bitangents.

## Verification
The standalone pure-Python script `verify_klein_frob.py` constructs \(\mathbb F_{3^6}\) using the irreducible polynomial \(v^6+v+2\) and checks all \(728\) nonzero field elements independently against both the original quartic equation and the cubic tangent-contact condition. It verifies all \(28\) parametrizations, the distinct tangent equations, root multiplicative-order distribution \((1,6,3,18)\), orbit sizes \((1,3,6,6,6,6)\), and the exact rational counts in degrees \(1\) through \(12\). Its terminal check string is `KLEIN_CHAR3_HYPERFLEX_28_ORBITS_1_3_6_6_6_6_F729_PASS`. The general proof uses polynomial identities, smoothness, and multiplicative-group reasoning; finite enumeration alone would not establish the theorem over the algebraic closure.

## Relationship to prior work
The standard Klein quartic and its complex bitangent arrangement are classical. Janasz--Pokora--Zieliński (2023, arXiv:2308.16514) study incidences of bitangents of the complex Klein quartic and other symmetric quartics; they explicitly work over the complex numbers (Section 1) and do not state the present prime-field Frobenius-orbit spectrum. Elkies (1999, Section 3) describes exceptional geometry in characteristic three, including that all points flex and that there are 28 fourfold tangencies. His model over a suitable residue field has all 28 distinguished points over \(\mathbb F_9\); the present statement concerns the **specific displayed \(\mathbb F_3\)-model**, and distinguishes its different arithmetic twisting, including nontrivial degree-six Frobenius orbits. Dolgachev--Martin (2024, Section 4) classify geometric automorphism groups of smooth quartics in odd characteristic and identify the characteristic-three Klein/Fermat equivalence; their classification over an algebraic closure does not specify this rational-model Frobenius permutation. Known geometric contact counts and automorphism classifications are not claimed as new.

## Limitations
The finding determines the arithmetic permutation and splitting field of the hyperosculation supports and lines for the displayed plane model, not every incidence of the 28 lines, the zeta function, or its complete automorphism representation. The 28 fourfold-contact count is known; the claimed refinement is the exact \(\mathbb F_3\)-Frobenius decomposition and field-by-field formula for this model. Priority against unindexed arithmetic discussions of Klein-quartic twists is not established by unsuccessful searches, and independent external mathematical validation has not been performed.

## References
- M. Janasz, P. Pokora and M. Zieliński, *On arrangements of smooth plane quartics and their bitangents*, arXiv:2308.16514, first public 31 August 2023, especially Sections 1 and 3. https://arxiv.org/abs/2308.16514
- N. D. Elkies, *The Klein Quartic in Number Theory*, in *The Eightfold Way*, MSRI Publications 35 (1999), pp. 51--102, especially discussion of characteristic three at pp. 79--81. https://dash.harvard.edu/entities/publication/73120378-7d3e-6bd4-e053-0100007fdf3b
- I. Dolgachev and G. Martin, *Automorphisms of del Pezzo surfaces in odd characteristic*, Journal of the London Mathematical Society 109 (2024), e12905, especially Section 4. https://doi.org/10.1112/jlms.12905
