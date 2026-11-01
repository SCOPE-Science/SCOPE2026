# Sharp two-disk covering of all well-rounded flat tori

## Finding
Let \(\Lambda\subset\mathbb R^2\) be a full lattice whose shortest nonzero vectors span \(\mathbb R^2\), and write \(T=\mathbb R^2/\Lambda\), with its intrinsic flat distance \(d_T\). Put
\[
L=\min_{v\in\Lambda\setminus\{0\}}|v|,\qquad
\rho_2(T)=\inf_{p,q\in T}\max_{x\in T}\min\{d_T(x,p),d_T(x,q)\}.
\]
Then **the exact unrestricted two-center covering radius** is
\[
\boxed{\rho_2(T)=L/2.}
\]
For any independent shortest lattice vectors \(a,b\), the sites \([0]\) and \([(a+b)/2]\) attain the radius, and their only farthest torus points are \([a/2]\) and \([b/2]\).

The independent shortest vectors form a basis and meet at an angle \(\theta\in[\pi/3,2\pi/3]\). For the optimal configuration, the dimensionless multiplicity-counting disk covering density is
\[
\delta_2(T)=\frac{2\pi(L/2)^2}{\operatorname{area}(T)}
=\frac{\pi}{2\sin\theta},\qquad
\boxed{\frac\pi2\le\delta_2(T)\le\frac\pi{\sqrt3}}.
\]
The lower density equality holds only for the square shape, while the upper equality holds only for the hexagonal shape (similarity classes).

The same equality has an intrinsic quotient interpretation. For the central-inversion flat pillowcase \(P=T/(x\sim-x)\), equipped with the quotient length metric,
\[
\operatorname{rad}(P)=\min_{y\in P}\max_{z\in P}d_P(y,z)=L/2.
\]
An attaining point is represented by \((a+b)/4\). Its unique farthest inversion orbit is represented by \((a-b)/4\).

## Assumptions and scope
All lattices are two-dimensional, Euclidean, and of full rank. “Well-rounded” means that shortest nonzero lattice vectors span the ambient plane. Sites may be placed anywhere on the torus; no symmetry or lattice-coset constraint is imposed in the minimization. Geodesic disks are closed for the covering problem, and their areas are Euclidean disk areas up to radius \(L/2\) (boundary self-contacts have zero area). The angle range includes the square and both equivalent hexagonal endpoints.

## Proof
**1. A shortest-vector basis.** Choose independent shortest vectors \(a,b\), both of length \(L\). The inequalities \(|a+b|\ge L\) and \(|a-b|\ge L\) imply
\[
-\tfrac12\le \frac{a\cdot b}{L^2}\le\tfrac12,
\qquad \theta\in[\pi/3,2\pi/3].
\]
If their integer span were a proper sublattice of \(\Lambda\), choose a nonzero coset representative \(z=s a+t b\in\Lambda\) with \(|s|,|t|\le1/2\). Then
\[
0<|z|^2=L^2(s^2+t^2+2st\cos\theta)
\le L^2\bigl(\tfrac12+\tfrac12|\cos\theta|\bigr)
\le\tfrac34L^2,
\]
contrary to minimality of \(L\). Hence \(a,b\) form a lattice basis. Conversely, two equal-length basis vectors with \(|\cos\theta|\le1/2\) are shortest: for integers \((m,n)\ne(0,0)\),
\[
|ma+nb|^2\ge L^2(m^2+n^2-|mn|)\ge L^2.
\]

**2. Construct a sharp two-site cover.** Let \(t=(a+b)/2\), and set
\[
u=(a+b)/2,\qquad v=(a-b)/2.
\]
The union of the two site lifts is exactly
\[
\Lambda\cup(t+\Lambda)=\Lambda' :=\mathbb Zu+\mathbb Zv,
\]
because \(a=u+v\), \(b=u-v\), and \(2u=a+b\). Moreover,
\[
u\cdot v=\frac{|a|^2-|b|^2}{4}=0,
\qquad |u|^2+|v|^2=L^2.
\]
Thus \(\Lambda'\) is rectangular. Every plane point can be translated by an element of \(\Lambda'\) into its centered Voronoi rectangle
\[
\{su+tv:|s|\le1/2,\ |t|\le1/2\},
\]
and has distance at most \(\tfrac12\sqrt{|u|^2+|v|^2}=L/2\) to \(\Lambda'\). This proves \(\rho_2(T)\le L/2\). Equality for the constructed configuration occurs precisely at the rectangle's corners \((\pm u\pm v)/2\). Modulo \(\Lambda\), these four points give exactly the distinct torus points \([a/2]\) and \([b/2]\), proving the farthest-set assertion.

**3. Unrestricted lower bound.** More generally, any Euclidean flat two-torus with shortest lattice-vector length \(L\) satisfies \(\rho_2(T)\ge L/2\). Suppose a pair of closed radius-\(R\) metric disks covered it for some \(R<L/2\). Select \(r\) with \(R<r<L/2\). The two open radius-\(r\) balls still cover \(T\), and each is an embedded Euclidean open disk: two points within distance \(<r\) of one lift cannot differ by a nonzero lattice vector, because such a vector has length \(\ge L>2r\).

But a two-torus cannot be covered by two contractible open sets. Indeed, its two degree-one integral cohomology generators \(\alpha,\beta\) have \(\alpha\smile\beta\ne0\) in \(H^2(T;\mathbb Z)\). If \(T=U\cup V\) and both are contractible, \(\alpha\) lifts to \(H^1(T,U;\mathbb Z)\) and \(\beta\) lifts to \(H^1(T,V;\mathbb Z)\). Their relative cup product lies in \(H^2(T,U\cup V;\mathbb Z)=0\), so its image \(\alpha\smile\beta\) vanishes, a contradiction. This proves the lower bound and therefore the exact radius.

**4. Density and equality shapes.** Since \(\operatorname{area}(T)=|\det(a,b)|=L^2\sin\theta\), the two radius-\(L/2\) disks have multiplicity-counted total area \(\pi L^2/2\), hence \(\delta_2=\pi/(2\sin\theta)\). On \([\pi/3,2\pi/3]\), \(\sin\theta\) is maximal only at \(\pi/2\) and minimal only at the endpoints. The corresponding lattices are respectively square and hexagonal, establishing both sharp density extrema.

**5. Pillowcase equivalence.** A quotient point \([p]\in P\) has distance to \([x]\in P\) equal to
\[
d_P([p],[x])=\min\{d_T(p,x),d_T(-p,x)\}.
\]
Every two-site pair \(\{p,q\}\) on the torus can be translated to a symmetric pair \(\{z,-z\}\), because the torus group is divisible. Translation preserves the torus covering radius. Therefore the minimum quotient eccentricity equals the unrestricted torus two-site radius. With \(z=(a+b)/4\), its two lifts become the constructed sites after translation by \(z\). The torus farthest points \([a/2]\), \([b/2]\) translate back to \([(a-b)/4]\) and its negative, which constitute a single inversion orbit. This proves the quotient statements.

## Verification
The analytic proof is complete without enumeration. An independent standalone exact-rational checker (`checker.py`) uses Gram-form arithmetic to verify the orthogonal-index-two identities, minimum-vector bounds on a finite integer window, and the covering inequality on finite coordinate grids for seven rational cosine values including both endpoints and the square. It reports **5,607 successful exact-rational assertions**. It also checks that the two stated farthest points achieve squared distance \(1/4\) after normalizing \(L=1\). No finite grid is asserted to prove a universal covering statement; the geometric Voronoi rectangle and cohomological argument do that.

## Relationship to prior work
Musin and Nikitenko's study of congruent-circle packings on the square flat torus (arXiv:1212.0649, 2012) and Brandt et al.'s solutions of packings of two to four circles on arbitrary flat tori (arXiv:1708.05395, 2017) optimize pairwise separation with **nonoverlapping disks**, not full-area geodesic covering. Baake, Scharlau, and Zeiner (arXiv:1311.6306, Section 2) classify reduced planar lattices and identify the rhombic/square/hexagonal well-rounded family; their work does not give this two-disk metric-covering invariant. Protasov, Tolmachev, and Voronov (arXiv:2402.03997, Theorem 2) optimize diameters of arbitrary partition sets for the square torus, a different functional from covering by two equal metric disks. The present equality is for the **complete one-parameter family of well-rounded tori**, and its proof uses an orthogonal index-two *superlattice* of site lifts together with the two-dimensional cup-product obstruction.

## Limitations
This does not determine the optimal two-center radius for every non-well-rounded flat torus, nor classify every optimal pair on the well-rounded locus. It identifies one optimal pair, its complete farthest-point set, and a sharp density profile. The quotient statement specifies a minimizing pillowcase point and its farthest orbit but does not claim all minimizing points. Historical priority outside the inspected literature, particularly unindexed periodic-covering sources, remains a risk. The exact algebraic and topological argument is independent of numerical spot checks.

## References
1. O. R. Musin and A. V. Nikitenko, *Optimal packings of congruent circles on a square flat torus*, arXiv:1212.0649 (first posted 2012-12-04), https://arxiv.org/abs/1212.0649.
2. M. Baake, R. Scharlau, and P. Zeiner, *Well-rounded sublattices of planar lattices*, arXiv:1311.6306 (first posted 2013-11-25), https://arxiv.org/abs/1311.6306.
3. M. Brandt, W. Dickinson, A. Ellsworth, J. Kenkel, and H. Smith, *Optimal Packings of Two to Four Equal Circles on Any Flat Torus*, arXiv:1708.05395 (first posted 2017-08-17), https://arxiv.org/abs/1708.05395.
4. D. Protasov, A. Tolmachev, and V. Voronov, *Optimal partitions of the flat torus into parts of smaller diameter*, arXiv:2402.03997 (first posted 2024-02-06), https://arxiv.org/abs/2402.03997.
