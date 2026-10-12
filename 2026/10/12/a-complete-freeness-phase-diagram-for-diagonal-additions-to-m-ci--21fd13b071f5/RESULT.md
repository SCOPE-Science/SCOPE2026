# A complete freeness phase diagram for diagonal additions to Măcinic’s Example 4.1
## Finding
Let
\[
B:\ (x-y)(x+y)(x^2+y^2-z^2)(2y^2-z^2)(2x^2-z^2)=0.
\]
Măcinic’s Example 4.1 proves that \(B\) is free with exponents \((2,5)\). Consider the full projective plane of diagonal conics
\[
C_{[a:b:c]}:\ ax^2+by^2+cz^2=0.
\]
Restrict to \(abc\neq0\), which is exactly the smooth locus of this diagonal family, and remove \([1:1:-1]\), the parameter of the conic \(x^2+y^2-z^2=0\) already contained in \(B\).

Define
\[
F=a+b+2c,
\qquad
\Delta=(a+b)(a-b)(a+c)(b+c)(a+2c)(b+2c).
\]
Then the complete freeness-type stratification of this smooth diagonal family is as follows.

If \(F=0\), then \(|B\cap C_{[a:b:c]}|=4\) and \(B\cup C_{[a:b:c]}\) is free with exponents \((2,7)\).

Assume \(F\neq0\), and let \(r\) be the number of the six linear factors in \(\Delta\) that vanish at \([a:b:c]\). Then
\[
|B\cap C_{[a:b:c]}|=16-2r.
\]
The only admissible point with \(r=3\) is
\[
[2:2:-1],
\]
and there \(B\cup C_{[a:b:c]}\) is free with exponents \((4,5)\). The admissible points with \(r=2\) are exactly
\[
[1:-1:-1],\ [1:-1:1],\ [1:2:-1],\ [2:-2:-1],\ [2:-2:1],\ [2:1:-1],
\]
and precisely at these six parameters the union is plus-one generated with exponents \((4,6)\) and level \(7\). If \(r=1\), the union is neither free nor plus-one generated and
\[
0\longrightarrow S(-9)\longrightarrow S(-7)\oplus S(-7)\oplus S(-4)\longrightarrow D_0\longrightarrow0.
\]
If \(r=0\), the union is neither free nor plus-one generated and
\[
0\longrightarrow S(-10)\longrightarrow S(-8)\oplus S(-7)\oplus S(-4)\longrightarrow D_0\longrightarrow0.
\]

Thus the symmetry-adapted diagonal parameter plane has a one-dimensional free locus \(F=0\) (after deleting the singular and already-present members), one additional isolated free point, six isolated plus-one generated points, and two complementary neither-free-nor-plus-one-generated strata.

## Assumptions and scope
All curves are over \(\mathbb C\). The parameter \([a:b:c]\) is projective. The condition \(abc\neq0\) is necessary and sufficient for the diagonal quadratic form to have rank three, hence for \(C_{[a:b:c]}\) to be smooth. The point \([1:1:-1]\) is excluded because it gives an existing component of \(B\). No claim is made about non-diagonal conics.

The diagonal family is intrinsic to the example: it is exactly the space of conics invariant under the coordinate sign-change subgroup of \(\operatorname{PGL}_3\). It contains both diagonal conics singled out in Măcinic’s Example 4.1.

## Proof
Use squared coordinates
\[
\pi:\mathbb P^2_{x,y,z}\longrightarrow\mathbb P^2_{X,Y,Z},
\qquad
[x:y:z]\longmapsto[x^2:y^2:z^2].
\]
The four sign-orbits of components of \(B\) map to the four lines
\[
H_0:X-Y=0,\quad
H_1:X+Y-Z=0,\quad
H_2:2Y-Z=0,\quad
H_3:2X-Z=0.
\]
All four pass through
\[
P=[1:1:2].
\]
The conic \(C_{[a:b:c]}\) maps to the line
\[
L_{a,b,c}:aX+bY+cZ=0.
\]
Therefore \(L_{a,b,c}\) passes through \(P\) exactly when \(F=a+b+2c=0\).

Suppose first that \(F\neq0\). Then the four points \(L_{a,b,c}\cap H_i\) are distinct. A generic point of any \(H_i\) has four projective lifts under \(\pi\), while a point with exactly one zero coordinate has two. Direct cross products give
\[
L\cap H_0=[c:c:-(a+b)],
\]
so its lift count drops exactly when \(a+b=0\). For \(H_1\), the three coordinates of \(L\cap H_1\) are proportional to
\[
-(b+c),\quad a+c,\quad a-b,
\]
so the three branch conditions are \(b+c=0\), \(a+c=0\), and \(a-b=0\). For \(H_2\), the only admissible branch condition is \(b+2c=0\), and for \(H_3\) it is \(a+2c=0\). Hence the six factors of \(\Delta\) are exactly the six branch conditions. Smoothness excludes the coordinate vertices, so every such event changes a four-lift intersection to a two-lift intersection and nothing further degenerates. Consequently
\[
|B\cap C_{[a:b:c]}|=4(4-r)+2r=16-2r.
\]

Each branch event is a simple tangency. For instance, on either line \(x=\pm y\), the restriction of \(C_{[a:b:c]}\) under \(a+b=0\) is a nonzero multiple of \(z^2\). On either line \(z=\pm\sqrt2\,y\), the condition \(b+2c=0\) makes the restriction a nonzero multiple of \(x^2\), and similarly for \(z=\pm\sqrt2\,x\). On \(x^2+y^2-z^2=0\), subtracting a scalar multiple of that conic shows respectively that the conditions \(a+c=0\), \(b+c=0\), and \(a-b=0\) make the restriction a nonzero square of \(y\), \(x\), or \(z\). Hence all new two-branch singularities are \(A_3\) tacnodes and are quasihomogeneous.

Now suppose \(F=0\). The four conics
\[
x^2-y^2=0,\qquad x^2+y^2-z^2=0,\qquad 2y^2-z^2=0,\qquad 2x^2-z^2=0
\]
are members of the same pencil \(a+b+2c=0\), and every admissible \(C_{[a:b:c]}\) with \(F=0\) is another member. The pencil has exactly the four base points above \(P\), and two generators have independent gradients at each base point. They therefore form local analytic coordinates. Locally the five pencil members become five distinct linear forms in those coordinates, so the union has an ordinary homogeneous five-branch singularity at each base point. Thus the triple is quasihomogeneous and \(|B\cap C_{[a:b:c]}|=4\).

It remains only to classify intersections of the six lines in the parameter divisor \(\Delta=0\). Pairwise exact projective intersections show that the sole admissible triple point is \([2:2:-1]\), and the six admissible double points are exactly the six points listed in the Finding. All other admissible points on \(\Delta\) have \(r=1\), while points off \(\Delta\) have \(r=0\).

Măcinic’s addition theorem applies because \(B\) is free with exponents \((2,5)\) and all the triples above are quasihomogeneous. If \(k=|B\cap C|=2m\), the source theorem says that the union is free exactly for \(m\in\{2,5}\), plus-one generated exactly for \(m=6\), and neither for \(m\ge7\). Thus \(k=4,10,12,14,16\) give exactly the stated five cases. The source’s resolution corollary gives the displayed minimal resolutions for \(m=7\) and \(m=8\).

## Verification
The accompanying `verify.py` uses exact integer projective arithmetic. It verifies that the four quotient lines are concurrent at \([1:1:2]\), derives the six coordinate-branch forms from cross products, enumerates every pairwise intersection of the six parameter lines, confirms the unique admissible triple point and the six admissible double points, checks that the free line meets the branch divisor only at singular or already-present conics, and verifies the values \(k=4,10,12,14,16\) and their freeness-type consequences. It also checks that the two diagonal conics printed in Example 4.1 land in the predicted free and plus-one generated strata.

The checker certifies the finite algebra used in the parameter stratification. The application of the addition theorem and the local analytic pencil argument are proved above rather than delegated to finite computation.

## Relationship to prior work
Măcinic’s Example 4.1 supplies the base free arrangement and exhibits three individual additions: the diagonal conic \(x^2+3y^2-2z^2=0\), which is free after addition; the diagonal conic \(x^2+2y^2-z^2=0\), which is plus-one generated after addition; and a non-diagonal conic yielding neither outcome. Theorem 3.7 gives the general addition criterion once the intersection cardinality is known, and Corollary 3.17 gives the minimal resolution in the neither case.

The present result does not strengthen that general theorem. It instead computes, for the natural full invariant plane of diagonal conics, the exact parameter discriminant controlling the intersection cardinality and then pushes the general theorem through that discriminant. In particular, it identifies the additional free conic \(2x^2+2y^2-z^2=0\), proves that the plus-one generated locus in the smooth diagonal family consists of exactly six points, and determines the two complementary minimal-resolution strata. Exact-equation and parameter-stratification searches did not locate this phase diagram in the inspected literature.

## Limitations
The result is confined to smooth diagonal conics and does not classify arbitrary smooth conics added to \(B\). The general addition theorem is taken from the cited source; the new work is the exact geometric computation of the diagonal parameter strata and the resulting specialization. The literature search cannot exclude an equivalent computation hidden under unrelated terminology, so originality carries the residual risk typical of a narrowly explicit classification.

## References
1. A. Măcinic, *Deletion-addition of a smooth conic for free curves*, arXiv:2408.11714, first public version 21 August 2024; especially Theorem 3.7, Corollary 3.17, and Example 4.1.
2. H. Schenck and Ş. O. Tohăneanu, *Freeness of conic-line arrangements in \(\mathbb P^2\)*, the predecessor addition/deletion framework cited and extended by Măcinic.
