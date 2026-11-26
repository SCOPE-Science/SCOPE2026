# The eight singular genus-three fibers of the Yu–Zhu 85-line quintic pencil

## Finding

For every \(t\in\mathbb C\setminus\{0,1\}\), the residual-quartic pencil through \(L=V(a,b)\) on the Yu–Zhu quintic \(X_t\) has exactly eight singular fibers. In the base coordinate \(r=a/b\), five fibers are four-line stars at \(r=0,\infty\) and \(r^3=t^{-1}\). The other three, at \(r^3=1\), are pairs of smooth conics with two tangencies each. The singularities of a star and of a conic pair are respectively one ordinary quadruple point and two \(A_3\) tacnodes. All fibers are reduced; every other fiber is a smooth plane quartic of genus three.

A four-line star has topological Euler characteristic \(5\), and a conic pair has Euler characteristic \(2\). The sum of their defects relative to a smooth fiber is \(5\cdot9+3\cdot6=63\), and \(e(X_t)=55\).

## Assumptions and scope

In coordinates \([u:v:a:b]\) on \(\mathbb P^3_{\mathbb C}\), set
\[
X_t=V\bigl((a-b)(u^4-3v^4)-6(a+b)u^2v^2+ab(b^3-ta^3)\bigr),\qquad t\ne0,1.
\]
Yu and Zhu prove that \(X_t\) is smooth and has exactly 85 lines [1, Theorem 1.1 and Lemma 3.1]. Each plane through \(L\) cuts the sum of \(L\) and a residual plane quartic. The claim concerns only the fibration by these residual divisors on \(X_t\), not other pencils or a quotient surface.

## Proof

**The pencil has no base points.** Removing the common divisor \(L\) from the plane sections gives a pencil in \(|H-L|\), where \(H\) is the hyperplane class. Outside \(L\) every point belongs to exactly one plane of the pencil. For a finite parameter \(r\), substitute \(a=rb\) and remove the factor \(b\). In plane coordinates \([u:v:b]\) the resulting equation is
\[
Q_{r,t}=f_r(u,v)+c b^4=0,\qquad
f_r=A u^4+B u^2v^2+C v^4,
\quad (A,B,C,c)=(r-1,-6(r+1),-3(r-1),r(1-tr^3)).
\]
On \(L\), the coefficient of \(r\) and the constant coefficient of \(f_r\) cannot both vanish: that would force \(u^2v^2=u^4-3v^4=0\) for some \([u:v]\in\mathbb P^1\). Thus the pencil defines a morphism to \(\mathbb P^1\), extending the ratio \([a:b]\). At \(r=\infty\), set \(b=0\) and remove \(a\); the equation in \([u:v:a]\) is \(u^4-6u^2v^2-3v^4=0\).

**Finite parameters with \(c=0\), and infinity.** The finite zeros are \(r=0\) and the three roots of \(r^3=t^{-1}\). At each, \(A,C\ne0\) and
\[
B^2-4AC=48(r^2+r+1)\ne0,
\]
since none of these parameters is a cube root of unity. Hence the quadratic in \((u/v)^2\) has distinct nonzero roots and \(f_r\) has four distinct projective roots. The binary form at infinity has the same property (its quadratic discriminant is \(48\)). Each binary form therefore cuts four distinct lines through the single vertex \([0:0:1]\) in its plane. Their distinct tangent directions give one ordinary quadruple point, and they have no other intersections.

**Finite parameters with \(c\ne0\).** The derivative in \(b\) is \(4cb^3\), so a singular point requires \(b=0\). On this line the quartic is singular exactly at a repeated root of \(f_r\). For \(r\ne1\), the test is \(B^2-4AC=0\) because \(A,C\ne0\); there is no root lost at infinity in \([u:v]\). For \(r=1\) the form is \(-12u^2v^2\) and has two double roots. Equivalently, all and only the parameters with \(r^3=1\) give singular fibers in this case. They have \(c=r(1-t)\ne0\).

At \(r=1\) the polynomial \(f_r\) is a nonzero multiple of \((uv)^2\). At a primitive cube root of unity the identity
\[
(r-1) f_r=\big((r-1)u^2-3(r+1)v^2\big)^2-12(r^2+r+1)v^4
\]
shows that it is a nonzero multiple of the square of a binary quadratic with two distinct projective roots. In either case the quartic equation splits into two distinct conics \(q(u,v)\pm\gamma b^2=0\), with \(\gamma\ne0\) and \(q\) nondegenerate. Each conic is smooth by nondegeneracy of its ternary quadratic form. They meet only at the two points with \(b=q=0\). At each, in a chart on the plane, the simple zero of the binary quadratic permits \(q\) and \(b\) as local analytic coordinates. The union has equation \(q^2-\gamma^2 b^4=0\), giving one \(A_3\) tacnode at each point.

The parameters in the two singular cases are disjoint and distinct because \(t\ne0,1\). All remaining fibers are smooth plane quartics and have genus three by the plane genus formula.

**Euler characteristics.** Four projective lines meeting only at a common point have \(e=4\cdot2-3=5\). Two smooth conics meeting at two distinct points have \(e=2\cdot2-2=2\). The smooth fibers have \(e=2-2\cdot3=-4\), so additivity over the base and local triviality over the smooth-fiber stratum give
\[
e(X_t)=2(-4)+5(5+4)+3(2+4)=55.
\]
Independently \(c_2(TX_t)=11H^2\) by the hypersurface Chern-class formula, with \(\int_{X_t}H^2=5\).

## Verification

The argument is uniform in \(t\); in particular the finite line-star parameters follow from the **zero set** of \(r(1-tr^3)\), not from a finite sample. The accompanying symbolic checks cover the binary-quartic identities and the Euler arithmetic. The proof gives the exhaustive singularity criterion and the analytic types.

## Relationship to prior work

Yu and Zhu [1, §3.2] already determined the five completely split residual quartic sections when counting lines meeting \(L\). Their finite plane parameter \(\lambda\) is defined by \(\lambda a=b\), so their equation \(\lambda^3=t\) agrees with \(r^3=t^{-1}\) in the reciprocal chart used here. The all-parameter classification above adds the three conic pairs, determines their local singularities, and rules out further singular fibers. For \(t=-1/8\), [1, §4] also describes the singular Kodaira fibers \(5I_0^*+I_4+2I_1\) of the elliptic surface obtained from the order-four quotient of **this same pencil** and resolution. That special-member quotient calculation does not describe the conic components and tacnodes of the original plane quartics for the family. These comparisons do not claim publication priority outside the work examined.

## Limitations

This is a classification over \(\mathbb C\) for \(t\ne0,1\) of one pencil on \(X_t\). It does not determine stable reductions, monodromy, or the elliptic quotient fibers in the varying family.

## Reference

[1] X. Yu and Z. Zhu, *A smooth quintic surface with 85 lines and Picard number 43*, [arXiv:2609.26862v1](https://arxiv.org/abs/2609.26862), Theorem 1.1, Lemma 3.1, §§3.2 and 4.
