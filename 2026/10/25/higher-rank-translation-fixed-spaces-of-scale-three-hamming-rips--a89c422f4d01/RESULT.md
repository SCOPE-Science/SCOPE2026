# Higher-rank translation-fixed spaces of scale-three Hamming Rips complexes

## Finding

Let \(n\geq2\), let \(Q_n=(\mathbf F_2)^n\) carry Hamming distance, and let \(X_n=\operatorname{VR}_{\leq3}(Q_n)\) denote its *inclusive* scale-three Vietoris--Rips simplicial complex. The additive translation group \(Q_n\) acts simplicially. For every linear subgroup \(H\leq Q_n\) of rank \(r\geq2\), put \(w(H)=\max_{h\in H}\operatorname{wt}(h)\), where \(\operatorname{wt}\) is Hamming weight.

The *geometric* fixed-point space (not the fixed-vertex subcomplex and not a homotopy-fixed-point space) has the following complete PL homeomorphism classification:

\[
|X_n|^H\cong_{\mathrm{PL}}
\begin{cases}
\varnothing,&w(H)\geq4,\\
|Q_{n-2}|,&r=2,\ w(H)\leq3,\ \{\operatorname{wt}(h):h\in H\setminus\{0\}\}\ne\{2,3,3\},\\
\displaystyle\bigsqcup^{2^{n-4}} S^1,&r=2,\ \{\operatorname{wt}(h):h\in H\setminus\{0\}\}=\{2,3,3\},\\
\displaystyle\bigsqcup^{2^{n-3}}\{\mathrm{pt}\},&r=3,\ w(H)\leq3.
\end{cases}
\]

In the second line, \(Q_{n-2}\) means the one-dimensional **cube graph**, not a full cubical cell complex; \(Q_0\) is one point. In the third line, each circle can be taken to be a four-cycle. Every rank-two subgroup with \(w(H)\leq3\) has precisely one of the nonzero weight multisets \(\{1,1,2\},\{1,2,3\},\{2,2,2\},\{2,3,3\}\). Every subgroup of rank at least four satisfies \(w(H)\geq4\).

Consequently, the connected rank-two cases have first Betti number \((n-4)2^{n-3}+1\) for \(n\geq3\); the exceptional rank-two case has \(2^{n-4}\) circular components, and an admissible rank-three fixed space is discrete. All fixed spaces in the theorem have dimension at most one.

## Assumptions and scope

The coefficient field is \(\mathbf F_2\) only for the ambient translation vector space. The PL and homotopy classifications hold integrally and do not depend on homology coefficients. A subgroup has rank at least two, so no claim is made here about the rank-one fixed spaces. The fixed-point action on the geometric realization uses the natural permutation of the \(2^n\) binary vertices. In every formula, \(n\) is the number of binary coordinates and the threshold is inclusive Hamming distance three. An empty geometric fixed space has no points; a one-point graph is contractible.

## Proof

**1. Orbit-complex description.** The translation action of \(H\) on \(Q_n\) is free; its vertex orbits are precisely its affine cosets. A geometric point is fixed by \(H\) exactly when its barycentric coordinates are constant on each coset. Thus it is a convex combination of uniform coset barycenters, and a collection of coset barycenters spans a simplex exactly when the union of those cosets is a Rips face. This gives a PL homeomorphism of the geometric fixed space with the orbit simplicial complex. A coset is itself a Rips face exactly when \(w(H)\leq3\). If that fails, there is no possible support for a fixed point, proving the empty case.

If \(w(H)\leq3\), the orbit complex is flag because the Rips condition is pairwise. For two distinct cosets \(x+H\) and \(y+H\), its graph contains an edge exactly when
\[
M_H(x+y):=\max_{h\in H}\operatorname{wt}(x+y+h)\leq3.
\]
Its one-skeleton is therefore the Cayley graph on \(Q_n/H\) with generator set
\[
S_H=\{z+H\ne H:M_H(z)\leq3\}.
\]

**2. Classification of admissible ranks.** Suppose \(H\) has rank \(r\) and is supported on exactly \(s\) coordinates. Across the \(2^r\) codewords, each active coordinate is one in exactly \(2^{r-1}\) words. Hence, under \(w(H)\leq3\),
\[
 s\,2^{r-1}=\sum_{h\in H}\operatorname{wt}(h)\leq3(2^r-1).
\]
For rank four this gives \(s\leq5\). If \(s=4\), the code is the whole \(\mathbf F_2^4\) and contains a weight-four word. If \(s=5\), the rank-four code is a hyperplane \(\{x:\sum_{i\in T}x_i=0\}\) for a nonempty parity set \(T\subseteq[5]\). Full support forces \(|T|\geq2\). It contains a vector of weight four: for odd \(|T|\), set to zero a coordinate in \(T\); for even \(|T|\), set to zero one outside \(T\). Every rank at least four contains a rank-four subgroup, so no such admissible group exists.

For rank three, the bound gives \(s\leq5\). If \(s=5\), the seven nonzero weights total \(4s=20\), and since each weight is at most three, six must have weight three and the seventh weight two. Any two of the six distinct weight-three codewords have XOR weight two (the XOR has positive even weight at most three), so their three-element supports intersect in exactly two points. Their complementary two-subsets of the five support coordinates therefore form six pairwise intersecting edges in a five-vertex complete graph. Such an edge family has at most four members (it is either a star or a triangle), contradiction. Thus \(s=3\) or \(s=4\). With \(s=3\), \(H=\mathbf F_2^3\) on its support. With \(s=4\), \(H\) is a hyperplane of \(\mathbf F_2^4\) with parity-check set \(T\); excluding the all-ones vector forces \(|T|\) odd, and full support forces \(|T|\geq2\), so \(|T|=3\). Up to a coordinate permutation, \(H=\langle e_1,e_2+e_3,e_2+e_4\rangle\), i.e. a free coordinate plus the even-weight plane on the other three.

For rank two, let \(u,v,u+v\) be the three nonzero elements. Each active coordinate occurs in precisely two of them, so the sum of their weights is twice the support size. With weights in \(\{1,2,3\}\) and the XOR relations, their unordered weights are exactly \(\{1,1,2\},\{1,2,3\},\{2,2,2\}\), or \(\{2,3,3\}\). Coordinate permutations put them respectively in the following forms:
\[
\begin{aligned}
&\langle e_1,e_2\rangle,\\
&\langle e_1,e_2+e_3\rangle,\\
&\langle e_1+e_2,e_2+e_3\rangle,\\
&\langle e_1+e_2,e_2+e_3+e_4\rangle.
\end{aligned}
\]

**3. Computing the fixed graphs.** For the first rank-two form, the quotient cosets are indexed by the \(n-2\) outside coordinates. Each candidate edge has maximum coset difference weight \(2+j\), where \(j\) is the outside difference weight; it is allowed precisely when \(j=1\). The graph is \(Q_{n-2}\).

For the third form, index quotient cosets by the parity of the first three support coordinates and \(m=n-3\) outside bits. A difference with even support parity and outside weight \(j\) has maximum weight \(2+j\); one with odd parity has maximum \(3+j\). The nonzero allowed differences are \((0,e_i)\) for \(1\leq i\leq m\) and \((1,0)\). These are \(m+1=n-2\) independent elements, so their Cayley graph is \(Q_{n-2}\).

For the second form, index quotient cosets by the parity of the coordinates \(2,3\) and the \(m=n-3\) outside bits. The corresponding maxima are \(3+j\) for parity zero and \(2+j\) for parity one. The allowed nonzero differences are \((1,0)\) and \((1,e_i)\), \(1\leq i\leq m\). They too form a basis of the quotient, so the graph is \(Q_{n-2}\).

For the fourth form, the support size is four. On its four-dimensional support, the quotient has four cosets; the three nontrivial cosets have maximum weights \(4,3,3\). No difference involving a nonzero outside coordinate is allowed, since \(H\) already has a weight-three element. For each assignment of its \(n-4\) outside coordinates, the two permitted support generators give a four-cycle; distinct assignments do not interact. This gives \(2^{n-4}\) disjoint four-cycles.

For an admissible rank-three group, an outside-coordinate difference is impossible because \(H\) has a weight-three element. In the support-three case the quotient has no nontrivial support difference. In the support-four case its one nontrivial support coset contains a weight-four vector. Thus there are no edges, and the \(2^{n-3}\) affine cosets give isolated points. These graphs have no triangles, so their flag complexes are exactly the graphs stated. This finishes the PL classification.

## Verification

The included `verify.py` constructs translation-orbit cosets directly and checks every rank-two, rank-three, and rank-four subgroup of \(\mathbf F_2^n\) for \(2\leq n\leq6\). For each admissible subgroup it builds the orbit compatibility graph from the maximum pairwise Hamming distance, checks graph isomorphism with the claimed model, and verifies that no triangles are present. It also checks that the rank and weight patterns exhaust the possibilities in this finite range. Execute `python verify.py` with Python 3; no external packages are required. The observed terminal marker is `HYPERCUBE_SCALE3_HIGHER_RANK_FIXED_VERIFIED`, followed by 3098 examined subgroups and 420 admissible subgroups. The proof above, not the finite experiment, establishes the result for unbounded \(n\).

## Relationship to prior work

Adamaszek--Adams (2021) classify small-scale ambient cube Rips homotopy; Shukla (2022) identifies scale-three ambient homology dimensions and collapsibility; and Feng (2023), especially Theorem 24, establishes the scale-three ambient wedge decomposition. These nonequivariant results do **not** give the geometric fixed spaces of higher-rank translation subgroups. Galetto--Montaño--Wellner (2026) concerns the ordinary homology representation under cube symmetries, a different invariant; its full text was not accessible in this review, so an incidental overlapping statement cannot be definitively excluded. The present classification is about geometric, simultaneous subgroup fixed sets rather than ordinary invariant homology or a rank-one fixed set.

## Limitations

This theorem does not classify rank-one subgroup fixed spaces, arbitrary nonlinear isometry subgroups, higher Rips scales, or the equivariant homotopy type of the ambient Rips complex. It gives PL models of geometric fixed-point spaces and their immediate homotopy consequences, not a classification of homotopy fixed points. The one-dimensional cube graph \(Q_{n-2}\) is not the full cubical \((n-2)\)-ball. The inability to inspect the entire 2026 group-action preprint leaves a specifically identified literature-overlap risk despite the different invariant in its abstract.

## References

1. M. Adamaszek and H. Adams, *On Vietoris--Rips complexes of hypercube graphs*, first arXiv posting 2021-03-01, https://arxiv.org/abs/2103.01040.
2. S. Shukla, *On Vietoris--Rips complexes (with scale 3) of hypercube graphs*, first arXiv posting 2022-02-06, https://arxiv.org/abs/2202.02756.
3. Z. Feng, *Homotopy types of Vietoris--Rips complexes of Hypercube Graphs*, first arXiv posting 2023-05-11, https://arxiv.org/abs/2305.07084.
4. F. Galetto, J. Montaño and Z. Wellner, *Homology of Vietoris--Rips complexes of hypercube graphs via group actions*, first arXiv posting 2026-06-18, https://arxiv.org/abs/2606.20784.
