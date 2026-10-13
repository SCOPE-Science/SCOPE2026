# Outer-Galois quartic quotients are sixteen-point grid blow-ups
## Finding
Let \(S\subset\mathbf P^3_{\mathbb C}\) be a smooth quartic
\[
X^4+Y^4+F_4(Z,W)=0,
\]
where \(F_4\) has four distinct zeros, and let
\[
\sigma[X:Y:Z:W]=[iX:iY:Z:W].
\]
This is the order-four automorphism attached to the two-outer-Galois-point family of Miura--Taki. Let \(U\subset\mathbf P^1_{[X:Y]}\) be the four zeros of \(X^4+Y^4\), and let \(V\subset\mathbf P^1_{[Z:W]}\) be the four zeros of \(F_4\).

The quotient \(Y=S/\langle\sigma\rangle\) has exactly eight singularities, all of type \(\frac14(1,1)\). If \(R\to Y\) is the minimal resolution, then
\[
R\cong \operatorname{Bl}_{U\times V}(\mathbf P^1\times\mathbf P^1).
\]
The eight exceptional \((-4)\)-curves over the quotient singularities are the strict transforms of the four vertical and four horizontal fibers through the \(4\times4\) grid. The sixteen lines on \(S\) joining a point of \(U\) on \(\{Z=W=0\}\) to a point of \(V\) on \(\{X=Y=0\}\) descend to the sixteen \((-1)\)-curves exceptional over the grid points. Thus these twenty-four curves have the incidence graph obtained by subdividing every edge of \(K_{4,4}\).

If \(D\) denotes the sum of the eight \((-4)\)-curves, then
\[
D=-2K_R,
\]
while \(|-K_R|=\varnothing\). Consequently \(R\) is a Coble surface. In addition,
\[
K_R^2=-8,\qquad \rho(R)=18,\qquad e(R)=20.
\]

## Assumptions and scope
The ground field is \(\mathbb C\). The binary quartic \(F_4\) is assumed squarefree; this is the smooth two-outer-Galois-point case in the cited source. The statement concerns the quotient by the simultaneous order-four scaling of \(X\) and \(Y\). It does not classify quotients by other subgroups or compactifications of unrelated affine charts.

## Proof
A point fixed by \(\sigma\) must have either \(Z=W=0\) or \(X=Y=0\). Intersecting with \(S\) gives four points on each coordinate line, hence eight in total. The same two coordinate lines contain the fixed locus of \(\sigma^2\), so there are no further points with nontrivial stabilizer.

At a fixed point on \(\{Z=W=0\}\), use a chart in which one of \(X,Y\) is nonzero. Since a root of \(X^4+Y^4\) is simple, the surface equation eliminates the remaining coordinate in the \([X:Y]\)-pair, and the tangent coordinates coming from \((Z,W)\) are both multiplied by \(-i\). Thus the quotient germ is \(\frac14(1,1)\). At a fixed point on \(\{X=Y=0\}\), squarefreeness of \(F_4\) similarly eliminates one of \((Z,W)\), while the tangent coordinates \((X,Y)\) are both multiplied by \(i\), giving the same quotient type. Its minimal resolution has one exceptional \((-4)\)-curve.

Consider the invariant rational map
\[
\phi:S\dashrightarrow \mathbf P^1\times\mathbf P^1,
\qquad [X:Y:Z:W]\longmapsto([X:Y],[Z:W]).
\]
On the affine chart \(Y W\ne0\), put \(r=X/Y\), \(z=Z/W\), and \(t=Y/W\). Then
\[
t^4(r^4+1)+F_4(z,1)=0.
\]
The automorphism fixes \(r,z\) and sends \(t\) to \(it\). Therefore
\[
\mathbb C(S)^{\langle\sigma\rangle}=\mathbb C(r,z),
\]
so \(\phi\) induces a birational map from the quotient to \(\mathbf P^1\times\mathbf P^1\).

The only indeterminacy points of \(\phi\) on \(S\) are the eight fixed points. Locally, the resolution of the scalar quotient \(\mathbb C^2/\mu_4\) is the total space of \(\mathcal O_{\mathbf P^1}(-4)\), whose exceptional \(\mathbf P^1\) records tangent directions. Hence the induced map from \(R\) extends regularly: an exceptional curve over a point of \(U\) maps isomorphically to the corresponding vertical fiber, and an exceptional curve over a point of \(V\) maps isomorphically to the corresponding horizontal fiber.

For every \((u_i,v_j)\in U\times V\), the line \(L_{ij}\) joining the corresponding two fixed points lies on \(S\), because both quartic summands vanish identically along that line. Away from its endpoints, \(L_{ij}\) is mapped by \(\phi\) to the single grid point \((u_i,v_j)\). These are exactly the positive-dimensional fibers of the resolved birational morphism \(R\to\mathbf P^1\times\mathbf P^1\): if one of the two quartic factors is nonzero, the displayed affine equation fixes the relative fourth power and the fiber is finite. The sixteen strict transforms are mutually disjoint after resolving their distinct tangent directions at the fixed endpoints. A birational morphism between smooth surfaces with one irreducible exceptional curve over each of sixteen distinct smooth points is the blow-up of those points. This proves the claimed model.

Let \(A,B\) be the two ruling classes on \(\mathbf P^1\times\mathbf P^1\), and let \(E_{ij}\) be the sixteen exceptional curves. The four vertical boundary curves have classes \(A-\sum_jE_{ij}\), and the four horizontal boundary curves have classes \(B-\sum_iE_{ij}\). Therefore their sum is
\[
D=4A+4B-2\sum_{i,j}E_{ij}=-2K_R.
\]
Each has self-intersection \(-4\). To see that \(|-K_R|\) is empty, an anticanonical divisor would push forward to a bidegree \((2,2)\) curve through all sixteen grid points. Restricting its equation to any one of the four vertical fibers gives a degree-two polynomial with four distinct zeros, so that fiber must be a component; doing this for all four vertical fibers is impossible for bidegree \((2,2)\). Hence no such divisor exists. The Coble assertion follows. Finally, blowing up sixteen points of \(\mathbf P^1\times\mathbf P^1\) gives \(K_R^2=8-16=-8\), \(\rho(R)=2+16=18\), and \(e(R)=4+16=20\).

## Verification
The accompanying verifier reconstructs the intersection lattice of the sixteen-point grid blow-up, checks the eight \((-4)\)-boundary classes, the sixteen \((-1)\)-classes and their incidence, verifies \(D=-2K_R\), and recomputes \(K_R^2\), \(\rho(R)\), and \(e(R)\). The quotient-field and local cyclic-quotient arguments are symbolic and are given explicitly in the proof; no finite experiment is used to infer an infinite statement.

## Relationship to prior work
Miura--Taki give the exact quartic normal form with two outer Galois points and identify the order-four automorphism and its eight fixed points. Artebani--Sarti had earlier exhibited the broader family \(f(x_0,x_1)+g(x_2,x_3)=0\) with the same type of order-four symmetry and eight fixed points. Neither inspected source identifies the quotient resolution with a blow-up of \(\mathbf P^1\times\mathbf P^1\), the sixteen grid centers, the sixteen descended line curves, or the resulting Coble boundary. Dolgachev--Zhang supplies the standard definition and general theory of Coble rational surfaces; the Coble designation here is a consequence of the explicit quotient model, not a claim that Coble surfaces themselves are new.

## Limitations
The result is for the smooth squarefree two-outer-Galois-point family and for the indicated order-four automorphism. It does not assert that every type \((10,4,8)\) order-four K3 quotient has this grid blow-up model. The originality comparison is strongest against the exact lead source and the standard order-four K3 classification; an older treatment in different coordinates could in principle contain an equivalent explicit quotient model.

## References
1. K. Miura and S. Taki, *Quartic surfaces with an outer Galois point and K3 surfaces with an automorphism of order 4*, arXiv:2408.04137v1 (2024), especially Proposition 2.1 and the two-Galois-point case.
2. M. Artebani and A. Sarti, *Symmetries of order four on K3 surfaces*, J. Math. Soc. Japan 67 (2015), 503--533, especially Proposition 2 and the separable quartic family following it.
3. I. Dolgachev and D.-Q. Zhang, *Coble Rational Surfaces*, arXiv:math/9909135v1 (1999).
