# A canonical Cartier phase transition in sparse-paving matroid toric varieties

## Finding

Let \(M\) be a rank-\(r\) sparse-paving matroid on \(n\) elements, with \(r\ge3\) and \(n-r\ge3\). Write \(\mathcal H\) for its circuit-hyperplanes, \(h=|\mathcal H|\), and \(X_M\) for the normal projective toric variety of the **normal fan** of its base polytope. For a basis \(B\), put \(t(B)=|\{H\in\mathcal H:|B\cap H|=r-1\}|\), and let \(U_B\) be the torus-fixed affine chart.

All \(2n+h\) torus-invariant prime divisors give a torsion-free global Weil class group
\[
\operatorname{Cl}(X_M)\simeq\mathbb Z^{n+h+1},
\qquad
\operatorname{Cl}(U_B)\simeq\mathbb Z^{1+t(B)}.
\]
In particular **every torus-fixed point is singular and non-\(\mathbb Q\)-factorial**. More sharply, \(U_B\) is \(\mathbb Q\)-Gorenstein precisely when it is already Gorenstein, and this happens precisely when
\[
n=2r\quad\text{and}\quad(t(B)=0\ \text{or}\ r=3).
\]
Thus **\(X_M\) is Gorenstein if and only if \(n=2r\) and either \(r=3\) or \(h=0\)**. Otherwise it is not \(\mathbb Q\)-Gorenstein. There are no nontrivial finite local canonical Cartier indices.

For the rank-four eight-element Vámos matroid, take the circuit-hyperplanes
\[
1234,\ 1256,\ 3456,\ 3478,\ 5678.
\]
Its seven-dimensional toric variety has \(65\) torus-fixed points and \(\operatorname{Cl}(X_M)\simeq\mathbb Z^{14}\). The local divisor-class ranks \(1,2,3\) occur respectively at \(17,16,32\) points. Exactly the \(17\) rank-one points are Gorenstein, and the remaining \(48\) points are not \(\mathbb Q\)-Gorenstein. Under the matroid automorphism group the \(65\) points split into six orbits, of sizes \(1,16,16,8,8,16\), whose associated \(t(B)\)-values are respectively \(0,0,1,2,2,2\).

## Assumptions and scope

Sparse-paving means that the matroid and its dual are paving, equivalently that its nonbases are exactly a family \(\mathcal H\) of \(r\)-subsets with pairwise intersections at most \(r-2\). All base polytopes are considered in their affine lattice of integer vectors with coordinate sum \(r\); the saturated normal-fan lattice is \(N=\mathbb Z^n/\mathbb Z(1,\ldots,1)\), dual to \(M_N=\{(a_i)\in\mathbb Z^n:\sum_i a_i=0\}\). All claims hold over an algebraically closed field of arbitrary characteristic. The toric variety is the *normal-fan projective toric variety*, not the potentially different projective embedding or affine semigroup ring defined by lattice points of the matroid polytope.

## Proof

**1. Facet classification.** The matroid is connected, and every deletion and contraction by a single element is connected. To see the connectivity statement, first note that paving in rank at least three forbids circuits of size below \(r\), and dual paving of corank at least three forbids cocircuits of size below \(n-r\). Hence there are no loops, coloops, parallel pairs, series pairs, or two-element cocircuits. A disconnected loopless, coloopless rank-\(s\) matroid with two components has a component of rank at most \(\lfloor s/2\rfloor\) supporting a circuit of size at most \(\lfloor s/2\rfloor+1\); this is too short when applied to \(M\), to a deletion of rank \(r\), or dually to a deletion of \(M^*\). Thus coordinate deletion and contraction remain connected, and each coordinate inequality \(x_i\ge0\), \(x_i\le1\) defines a facet. For every circuit-hyperplane \(H\), the inequality \(x(H)\le r-1\) is also a facet: \(M|H=U_{r-1,r}\) and \(M/H=U_{1,n-r}\) are connected. Conversely, any proper flat of rank at most \(r-2\) is independent, so its rank inequality follows from coordinate upper bounds. A proper rank-\(r-1\) flat is either independent, or exactly one of the \(r\)-element circuit-hyperplanes (a larger such flat would contain two overlapping circuit-hyperplanes). The standard connected-flat facet criterion therefore gives precisely the \(2n+h\) facets claimed.

**2. Primitive rays and class groups.** At the vertex corresponding to a basis \(B\), precisely one coordinate facet for each \(i\) is active, with primitive outward normals \([e_i]\) for \(i\in B\) and \([-e_i]\) for \(i\notin B\). The additional active facets are exactly \(H\in\mathcal H\) with \(|B\cap H|=r-1\), with primitive normal \([\sum_{i\in H}e_i]\). All the normals are primitive in \(N\) because their \(0/1\) representative has both values present, hence coefficient differences of greatest common divisor one. The \(n\) coordinate normals span \(N\) as a saturated lattice, since they are signed images of all standard basis vectors of \(\mathbb Z^n\). The affine toric divisor sequence \(M_N\to\mathbb Z^{n+t(B)}\to\operatorname{Cl}(U_B)\to0\) therefore has torsion-free cokernel of rank \((n+t(B))-(n-1)=1+t(B)\). Similarly, all \(2n+h\) global rays span \(N\), and the complete fan's divisor sequence gives \(\operatorname{Cl}(X_M)\simeq\mathbb Z^{(2n+h)-(n-1)}\). Since \(n>n-1\) ray generators occur at every maximal cone, none is simplicial; toric \(\mathbb Q\)-factoriality and smoothness therefore fail at every fixed point.

**3. Canonical Cartier criterion.** The toric canonical divisor is \(K_{X_M}=-\sum_{\rho}D_\rho\). A local rational Cartier support vector must take value \(1\) on each primitive ray. The coordinate rays force a uniquely determined vector \((a_i)\in\mathbb Q^n\), with \(a_i=1\) for \(i\in B\) and \(a_i=-1\) for \(i\notin B\). It descends to the dual of \(N\) exactly when \(\sum_i a_i=2r-n=0\), i.e. \(n=2r\). Once this holds, the candidate is integral, and for every active circuit-hyperplane \(H\) its value is
\[
\sum_{i\in H}a_i=|B\cap H|-|H\setminus B|=(r-1)-1=r-2.
\]
Therefore all extra ray constraints hold exactly when \(t(B)=0\) or \(r=3\). If a rational support vector exists it is this integral one: \(\mathbb Q\)-Gorenstein and Gorenstein are equivalent locally, with no index greater than one. If \(h>0\), for each circuit-hyperplane \(H\) replacing one element by any element outside \(H\) produces a basis \(B\) with \(t(B)>0\): no second circuit-hyperplane can share \(r-1\) elements with \(H\). This proves the global criterion.

**4. Vámos specialization.** The five prescribed circuit-hyperplanes pairwise intersect in at most two points and define the standard Vámos sparse-paving matroid. There are \(\binom84-5=65\) bases. An exact exhaustive partition of these bases by \(t(B)\) yields \(17,16,32\) for \(t=0,1,2\) (and zero at higher values). The four permutations \((12)\), \((17)(28)\), \((34)\), \((35)(46)\), preserving these five hyperplanes, generate its automorphism group and yield six basis orbits with representative, orbit size and \(t\): \((1278,1,0)\), \((1357,16,0)\), \((1237,16,1)\), \((1235,8,2)\), \((1347,8,2)\), \((1345,16,2)\). The preceding universal formulas now give the asserted toric invariants.

## Verification

Run `python verify_vamos.py` with Python 3 and the standard library; it must print `VERIFY_OK`. The checker enumerates Vámos bases and four permutation-generated orbits, verifies exact counts, tests facet affine ranks and the canonical-support equations over rational numbers, and repeats for selected uniform and one-circuit-hyperplane examples in ranks three through five. It independently forms ray normal vectors in a quotient-lattice basis and solves their Cartier equations. Finite checker runs support the concrete counts and catch sign/lattice mistakes; the infinite-family conclusions follow from the preceding proof, not from numerical extrapolation.

## Relationship to prior work

Feichtner–Sturmfels and Joswig–Schröter provide the matroid-polytope and sparse-paving facet frameworks used in Step 1. Karn–Nasr–Proudfoot–Vecchi identify and study the Vámos circuit-hyperplanes and automorphisms, but their computed invariants are Kazhdan–Lusztig-theoretic, not the normal-fan canonical Cartier status or local divisor class-group distribution. Hibi–Lasoń–Matsuda–Michałek–Vodička study *Gorenstein matroid semigroup rings* in a graphic setting, which must not be conflated with the normal-fan toric variety here. Earlier singular-stratum calculations for a one-circuit-hyperplane matroid are compatible special cases, not a covering result for arbitrary sparse-paving matroids or Vámos. The contribution is the uniform local-to-global canonical Cartier dichotomy with integral class-group formula and its non-representable eight-element example.

## Limitations

The conclusion describes class groups of torus-fixed affine charts, local canonical Cartier properties at torus-fixed points, and global Gorensteinness. It does not classify all positive-dimensional singular strata, the scheme structure of the singular locus, or local singularities away from fixed charts. A uniqueness or independent literature-completeness claim is not made; differently worded or unindexed results might overlap. The Vámos basis counts were finite and exhaustively verified; no external independent audit has been carried out.

## References

1. E. M. Feichtner and B. Sturmfels, *Matroid polytopes, nested sets and Bergman fans*, arXiv:math/0411260, first version 11 November 2004, https://arxiv.org/abs/math/0411260.
2. M. Joswig and B. Schröter, *Matroids from hypersimplex splits*, arXiv:1607.06291, https://arxiv.org/abs/1607.06291.
3. T. Karn, G. Nasr, N. Proudfoot and L. Vecchi, *Equivariant Kazhdan–Lusztig theory of paving matroids*, arXiv:2202.06938, especially the Vámos example, https://arxiv.org/abs/2202.06938.
4. T. Hibi, M. Lasoń, K. Matsuda, M. Michałek and J. Vodička, *Gorenstein graphic matroids*, arXiv:1905.05418, https://arxiv.org/abs/1905.05418.
5. W. Fulton, *Introduction to Toric Varieties*, Princeton University Press, 1993 (standard toric divisor sequences and Cartier criteria).
