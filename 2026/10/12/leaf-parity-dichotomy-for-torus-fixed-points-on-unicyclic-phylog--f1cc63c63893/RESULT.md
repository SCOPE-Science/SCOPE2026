# Leaf-parity dichotomy for torus fixed points on unicyclic phylogenetic toric models

## Finding

Let \(G\) be a connected simple graph in which every vertex has degree \(1\) or \(3\), with exactly one cycle and \(n\ge 3\) leaves. For the projective phylogenetic toric variety \(X(G)\) of Buczyńska's binary symmetric graph construction, the torus-fixed points are naturally indexed by precisely two types of vertices of its rational polytope \(P_G\):

1. Exactly \(2^n\) vertices are \(0/1\)-valued network labelings; their induced assignments on the leaves have even parity, with **two** vertices above every such leaf assignment.
2. Exactly \(2^{n-1}\) vertices have value \(1/2\) on **every** edge of the unique cycle and value \(0\) or \(1\) on every other edge; their leaf assignments have odd parity, with **one** vertex above every such assignment.

No other vertices occur. Thus the total number of torus fixed points, and the ordinary complex topological Euler characteristic, are

\[
\#X(G)^{T}=f_0(P_G)=\chi_{\mathrm{top}}(X(G))=3\cdot 2^{n-1}.
\]

In particular the Euler characteristic is independent of the unique cycle's length and of the attached trivalent trees.

## Assumptions and scope

The graph is finite, connected, simple, unicyclic, and its vertices have degree \(1\) or \(3\); \(n\) is the number of degree-one vertices. The unique cycle has length at least three. There are \(n\) internal vertices and \(2n\) edges. All varieties are over \(\mathbb C\), and the Euler characteristic is that of the underlying complex analytic space, not the coherent-sheaf or orbifold Euler characteristic.

Write \(E(G)\) for the edges and identify its real edge-labeling space with \(\mathbb R^{E(G)}\). At each trivalent vertex with incident edge coordinates \((a,b,c)\), impose

\[
(a,b,c)\in T:=\operatorname{conv}\{(0,0,0),(1,1,0),(1,0,1),(0,1,1)\}.
\]

Equivalently, the three triangle inequalities \(a+b\ge c\), \(a+c\ge b\), \(b+c\ge a\), together with \(a+b+c\le2\), hold. Define \(P_G\) as the simultaneous intersection of these local constraints. This is the degree-one real slice of the saturated graded cone defining \(X(G)=\operatorname{Proj}\mathbb C[\tau(G)]\) in Buczyńska's construction; its lattice may be a finite-index sublattice of the standard edge lattice. The rational vertices and the normal fan, rather than the degree-one integral lattice points, determine the torus fixed points. Taking a suitable Veronese multiple makes the polytope integral without changing \(X(G)\).

## Proof

**Full dimension and coordinate bounds.** Each tripod tetrahedron \(T\) lies in the unit cube and contains \((1/2,1/2,1/2)\) in its interior. Consequently \(P_G\) is full dimensional in \(\mathbb R^{E(G)}\) and every coordinate lies in \([0,1]\). Its vertices can therefore be tested by the active equations of the displayed tripod inequalities.

**Fractional support.** Given \(x\in P_G\), let \(F\subset E(G)\) be those edges with labels strictly between \(0\) and \(1\). A tripod cannot have exactly one edge in \(F\): if two coordinates are binary, the local convex hull forces the third to be binary. When exactly two coordinates are fractional and the third is \(0\), the sole independent active relation between the two fractional coordinates is their equality. If the binary coordinate is \(1\), it is that their sum equals \(1\). When all three are fractional, at most one independent defining facet of \(T\) is active: two different triangle equalities would force a zero coordinate, and a triangle equality combined with the sum-equals-two equality would force a unit coordinate. Thus each internal vertex incident with \(F\) supplies at most one independent active linear equation on the fractional coordinates. At such an internal vertex the degree within \(F\) is at least two.

**Elimination of other fractional supports.** Let \(H\) be a connected component of the subgraph whose edge set is \(F\), and denote by \(I\) and \(L\) the numbers of its internal vertices and original leaves. Every internal vertex of \(H\) has degree at least two in \(H\). Since \(G\) is unicyclic, \(H\) is either a tree or contains its unique cycle. If \(H\) is a tree, it has at least two degree-one vertices, which must be original leaves: hence \(L\ge2\), and \(|E(H)|=I+L-1>I\). If \(H\) contains the full cycle and at least one other edge, an off-cycle fractional branch must end at an original leaf, so \(L\ge1\) and \(|E(H)|=I+L>I\). In either case there are more fractional variables in \(H\) than potentially independent active equations. A nonzero infinitesimal perturbation supported on \(H\) preserves all active equalities; choosing its size sufficiently small in both directions also preserves strict inactive inequalities and the bounds \(0<x_e<1\). Such an \(x\) is not extreme. Therefore a vertex of \(P_G\) has either no fractional edges or fractional-edge set *exactly the entire unique cycle*.

**Cycle parity.** In the second case, let \(u_1,\ldots,u_c\) denote the cyclic edge labels and \(y_1,\ldots,y_c\in\{0,1\}\) the side-branch labels attached to its cycle vertices. The tripod constraints imply

\[
u_{i-1}=u_i\ \text{if }y_i=0,\qquad
u_{i-1}+u_i=1\ \text{if }y_i=1,
\]

with cyclic indices. An even number of \(y_i=1\) leaves one free parameter and therefore gives a positive-dimensional segment, not a vertex with fractional edges. An odd number forces \(u_i=1/2\) for all \(i\). Conversely, every such odd-parity configuration gives a vertex: in a convex decomposition all off-cycle binary coordinates must stay fixed, and the cycle equations then have a unique solution. Every feasible wholly binary labeling is likewise a vertex, since a nontrivial convex decomposition cannot change any binary coordinate of a point in the unit cube.

**Counting with leaf parity.** Remove the unique cycle. The remainder consists of rooted trees, one attached to each cycle vertex. A binary assignment to all \(n\) leaf edges uniquely propagates along each rooted tree by the local even-parity condition: an inner edge receives the sum modulo two of the labels of the leaves below it. Therefore the branch label \(y_i\) equals the sum modulo two of the leaf labels in its rooted tree, and the parity of \(\sum_i y_i\) is the parity of all \(n\) leaf labels. Exactly \(2^{n-1}\) leaf assignments have even parity and exactly \(2^{n-1}\) have odd parity. For each even assignment the cycle equations modulo two admit exactly two binary solutions; for each odd assignment they admit no binary solution, but admit exactly one all-half cycle solution over the reals. This yields \(2^n\) binary vertices and \(2^{n-1}\) half-cycle vertices, exhaustively.

**Topological conclusion.** The complete toric variety associated with \(P_G\) is stratified into torus orbits \((\mathbb C^*)^d\), one for each face with the corresponding orbit dimension. The topological Euler characteristic of an orbit is zero for \(d>0\) and one for \(d=0\). Thus the Euler characteristic equals the number of zero-dimensional torus orbits, equivalently vertices of \(P_G\), giving the stated formula.

## Verification

A companion `check_vertices.py` enumerates independent active-facet systems for three concrete simple unicyclic trivalent graphs. It reconstructs rational candidates, checks the tripod inequalities exactly, confirms full active-facet rank in rational arithmetic, and compares the resulting complete finite vertex sets with the parity classification. Run `python3 check_vertices.py` after installing `numpy` and `sympy`. The checked graphs are the three-cycle (\(n=3\)), four-cycle (\(n=4\)), and three-cycle with a pendant trivalent branch (\(n=4\)). They have respectively \((8,4)\), \((16,8)\), and \((16,8)\) integral/half-cycle vertices. These finite computations are consistency checks, **not** the proof for arbitrary \(n\).

## Relationship to prior work

Buczyńska's *Phylogenetic toric varieties on graphs* (arXiv:1004.1183, first public posting 2010-04-07; journal DOI below) supplies exactly the graded cone, local tripod inequalities, and underlying projective toric construction used here. Its Theorem 2.33 already identifies an **odd-parity condition on cycle legs for the degree-two minimal semigroup generators**; that condition is acknowledged as prior art, not claimed here. The paper also establishes deformation equivalence and shape-independent Hilbert functions. The present finding instead separates the **extreme vertices of the real polytope** from other semigroup generators (including possible nonextreme degree-two generators), proves that an extreme half-cycle labeling must be binary off the cycle, counts its fibers over actual leaf assignments, and derives the fixed-point/Euler count. A Hilbert polynomial or its invariance under a flat deformation does not, in general, determine the number of vertices of a toric polytope. For an explicit comparison, the unit square and the lattice triangle with vertices \((0,0),(2,0),(0,1)\) both have Ehrhart polynomial \((k+1)^2\), but have respectively four and three polytope vertices. Buczyńska–Wiśniewski's earlier work treats trees, not unicyclic models. Buczyńska–Buczyński–Kubjas–Michałek later gave general degree bounds for phylogenetic-semigroup generators; those bounds do not specify this face-vector entry.

## Limitations

The theorem is restricted to simple trivalent connected graphs with precisely one cycle; no assertion is made for two or more cycles, for non-trivalent graphs, or for the higher Betti numbers or singularity types of \(X(G)\). The topological conclusion is over \(\mathbb C\). This derivation uses known cone equations and elementary polytope and toric facts. The literature comparison is necessarily nonexhaustive; unindexed or unpublished formulations could overlap. No independent audit has been carried out.

## References

- W. Buczyńska, *Phylogenetic toric varieties on graphs*, arXiv:1004.1183 (2010), *Journal of Algebraic Combinatorics* **35** (2012), 421–460, DOI: 10.1007/s10801-011-0308-2. Primary MSC 14M25; see Definition 2.22, Theorems 2.24, 2.33, 3.5 and Section 4.3. https://arxiv.org/abs/1004.1183
- W. Buczyńska and J. A. Wiśniewski, *On the geometry of binary symmetric models of phylogenetic trees*, *J. Eur. Math. Soc.* **9** (2007), 609–635, DOI: 10.4171/JEMS/90. https://ems.press/journals/jems/articles/1138
- W. Buczyńska, J. Buczyński, K. Kubjas and M. Michałek, *On the graph labellings arising from phylogenetics*, arXiv:1105.5382 (2011), *Open Mathematics* **11** (2013), 1577–1592. https://arxiv.org/abs/1105.5382
