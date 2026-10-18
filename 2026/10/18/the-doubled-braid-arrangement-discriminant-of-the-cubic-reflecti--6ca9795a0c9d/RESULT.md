# The doubled braid-arrangement discriminant of the cubic reflection net

## Finding

Consider the plane cubic net over \(\mathbb C\)
\[
G_{a,b,c}(x,y,z)=a yz(y-z)+b xz(z-x)+c xy(x-y),
\quad [a:b:c]\in\mathbb P^2.
\]
Its scheme-theoretic discriminant (the pullback of the ternary-cubic discriminant) is the nonzero-scalar multiple
\[
\operatorname{Disc}(G_{a,b,c})\doteq
\bigl[abc(a-b)(a-c)(b-c)\bigr]^2.
\]
The six discriminant lines form the projectivized braid arrangement of type \(A_3\), each with scheme multiplicity two. Consequently, \(G_{a,b,c}=0\) is smooth exactly when \(a,b,c\) are all nonzero and pairwise distinct.

The entire geometric fiber classification is as follows. At a parameter lying on one discriminant line but no others, the cubic is a smooth conic plus a transverse line, with exactly two ordinary nodes. At one of the three double crossings \([1:1:0]\), \([1:0:1]\), or \([0:1:1]\), it is three nonconcurrent lines (a triangle), with three ordinary nodes. At one of the four triple crossings \([1:0:0]\), \([0:1:0]\), \([0:0:1]\), or \([1:1:1]\), it is three concurrent lines, with a unique ordinary triple point. Every parameter outside this arrangement yields a smooth, geometrically integral cubic of genus one.

## Assumptions and scope

All geometry and discriminants are over the complex numbers (more generally the argument applies in characteristic zero). Parameter triples are homogeneous nonzero triples. The discriminant is the classical homogeneous degree-twelve polynomial in the ten coefficients of a ternary cubic, specialized to the three-dimensional linear system displayed above; its nonzero multiplicative normalization is not specified. A fiber is the *reduced geometric plane curve* at its parameter; the scheme-theoretic multiplicity two refers to the parameter discriminant divisor, not to components of the plane cubic.

The net is the \(n=1\) case of the reflection-arrangement net in Di Gennaro–Ilardi–Miró-Roig–Schenck–Vallès, Section 5: the original reflection divisor is \(xyz(x-y)(x-z)(y-z)=0\), and the paper's three generators are precisely the three summands without parameter coefficients.

## Proof

**Step 1: Exact location of the singular-parameter set.** Let \(G=G_{a,b,c}\). Direct differentiation of the three displayed cubic generators gives
\[
\det\bigl(\nabla(yz(y-z)),\nabla(xz(z-x)),\nabla(xy(x-y))\bigr)
=-6xyz(x-y)(x-z)(y-z),
\]
up to an immaterial overall sign. If \(G\) has a projective singular point, then \(\nabla G=0\), so it lies on one of the six coordinate/diagonal lines in the \((x,y,z)\)-plane. Simultaneous permutation of \(x,y,z\) induces a permutation of \(a,b,c\), up to an overall sign. It suffices to inspect \(x=0\) and \(x=y\).

On \(x=0\), differentiation gives
\[
(G_x,G_y,G_z)=(b z^2-c y^2,\ a z(2y-z),\ a y(y-2z)).
\]
If \(a\ne0\), the last two entries have no common zero for \([y:z]\in\mathbb P^1\): if either coordinate vanishes, so must the other; otherwise \(2y=z\) and \(y=2z\) would force \(3y=0\). Hence singularities on \(x=0\) imply \(a=0\).

On \(x=y=t\), the derivatives are
\[
(G_x,G_y,G_z)=(-2btz+bz^2+ct^2,\ 2atz-az^2-ct^2,\ (a-b)t(t-2z)).
\]
If \(a\ne b\), the last derivative forces \(t=0\) or \(t=2z\). In the first case the first two derivatives force \(a=b=0\), a contradiction. In the second, they give \(3a=4c=3b\), again a contradiction. Thus a singular point on \(x=y\) implies \(a=b\). By permutation symmetry, the singular parameter locus is contained in the six lines \(a=0,b=0,c=0,a=b,b=c,a=c\).

Conversely, on \(a=0\) and \(a=b\), we have the exact factorizations
\[
G_{0,b,c}=x\bigl(bz(z-x)+cy(x-y)\bigr),
\qquad
G_{u,u,v}=(x-y)\bigl(vxy-uz(x+y)+uz^2\bigr).
\]
Each is a reducible cubic and hence singular. Permuting coordinates covers all six parameter lines. This proves the equality of the *reduced* discriminant with the six-line arrangement.

**Step 2: Geometric fiber types.** In the first factorization, the determinant of the symmetric matrix of the residual conic is \(bc(b-c)/4\); on the component line \(x=0\) its equation becomes \(bz^2-cy^2\). If \(bc(b-c)\ne0\), the conic is nonsingular and meets its line in two distinct points, producing two ordinary nodes and no other singularities. In the second factorization, the residual conic has symmetric-matrix determinant \(uv(u-v)/4\) and restricts on \(x=y=t\) to \(vt^2-2utz+uz^2\), with binary discriminant \(4u(u-v)\). Thus if \(uv(u-v)\ne0\), its two intersections are similarly transverse nodes. Symmetry gives the one-line stratum.

The six lines in parameter space meet in exactly three double points and four triple points. At \([a:b:c]=[1:1:0]\) the cubic is \(-z(x-y)(x+y-z)\), three nonconcurrent lines; the other double points are permutations. At \([a:b:c]=[0:0:1]\) the cubic is \(xy(x-y)\), three lines through one point; the other two coordinate vertices are analogous. Finally \(G_{1,1,1}=(x-y)(x-z)(y-z)\), another concurrent triple of lines. These exhaust the parameter intersections and establish the complete fiber stratification.

**Step 3: Scheme-theoretic multiplicities.** Write \(\Delta(a,b,c)\) for the specialized ternary-cubic discriminant, a homogeneous polynomial of degree twelve. It is nonzero because Step 1 proves there are smooth members, such as \(G_{1,2,3}\). A generic parameter on *each* of the six lines has two distinct ordinary nodes, by Step 2. The standard local deformation description of a plane curve with two ordinary nodes says that near its point in the full space of cubic equations, the universal discriminant is locally the product of the two independent node-smoothing equations, up to a unit. Each of these two equations vanishes identically along the chosen line of parameters (both nodes persist there), so the pullback \(\Delta\) vanishes at least to second order along that line. Equivalently, both distinct ordinary-double-point branches of the universal discriminant contribute one order of vanishing.

Consequently the product of the squares of all six defining linear forms divides \(\Delta\). This product already has degree twelve, the full degree of \(\Delta\). Since \(\Delta\ne0\), its quotient is a nonzero scalar. This proves the claimed *scheme-theoretic* discriminant identity and rules out every additional singular fiber.

## Verification

A standalone exact-symbolic checker, `verify.py`, checks the source net identity, the representative factorizations, the conic determinant calculations, the two reflection-line gradient restrictions, all seven special intersection representatives, and the absence of singular points for the smooth representative \([1:2:3]\) by Gröbner bases in the three standard affine charts. The polynomial discriminant identity is proven above using its classical degree and the local two-node deformation property; finite/sample calculations are only supplementary checks.

## Relationship to prior work

Di Gennaro, Ilardi, Miró-Roig, Schenck and Vallès define the reflection-arrangement net for all \(n\ge1\) and establish freeness results for general members and associated unions (their Section 5 and Theorem 5.2). The present conclusion instead classifies every singular fiber of the special \(n=1\) net, including all intersection strata, and determines the full scheme multiplicity of its discriminant. Those conclusions are not stated in the inspected source. Literature and mathematical-record checks were made under discriminant, dual variety, braid-arrangement, cubic net, and nodal degeneration formulations. The nearby discriminant computations found concern different families and do not logically imply this exact parameter-space identity.

## Limitations

This is a characteristic-zero classification, not a uniform result in small positive characteristics. It does not determine the modular invariant of the smooth elliptic fibers, the global monodromy representation, or freeness for every special union with the original reflection arrangement. The originality conclusion is subject to possible unindexed classical discriminant identities or equivalent parameterizations; no claim of independent scholarly audit is made.

## References

1. R. Di Gennaro, G. Ilardi, R. M. Miró-Roig, H. Schenck and J. Vallès, *Free curves, Eigenschemes and Pencils of curves*, arXiv:2306.09443 (first posted 2023-06-15), Section 5 and Theorem 5.2; Bulletin of the London Mathematical Society **56** (2024), 2424–2440, DOI:10.1112/blms.13063.
2. Classical discriminant theory of ternary cubics: the discriminant is a homogeneous polynomial of degree twelve and its local branches at ordinary nodes are given by independent node-smoothing parameters. Only these standard facts are used; the specialized factorization is proved in this note.
