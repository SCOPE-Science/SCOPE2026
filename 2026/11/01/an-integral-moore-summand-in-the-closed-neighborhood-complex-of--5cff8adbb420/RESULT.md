# An integral Moore summand in the closed-neighborhood complex of the Paley graph of order 13

## Finding

Write \(P_{13}\) for the graph on \(\mathbb Z/13\mathbb Z\) in which distinct residues \(a,b\) are adjacent precisely when \(b-a\in\{\pm1,\pm3,\pm4\}\). The closed-neighborhood complex \(K=\mathcal N[P_{13}]\) consists of all vertex sets contained in \(\{a\}\cup N(a)\) for some residue \(a\). Then there is an ordinary integral homotopy equivalence

\[
|K|\simeq M(\mathbb Z/2\mathbb Z,2)\vee S^2\vee S^3\vee S^3,
\]

where \(M(\mathbb Z/2\mathbb Z,2)\) is the simply connected Moore space formed by attaching a three-cell to a two-sphere with degree two. In particular,

\[
\widetilde H_2(K;\mathbb Z)\cong\mathbb Z\oplus\mathbb Z/2\mathbb Z,
\qquad
\widetilde H_3(K;\mathbb Z)\cong\mathbb Z^2,
\]

and all other reduced integral homology vanishes. The complex is pure six-dimensional and not shellable.

## Assumptions and scope

The graph is the undirected thirteen-vertex quadratic-residue Paley graph, equivalently the circulant graph with steps \(1,3,4\). No vertex loops are inserted. The closed neighborhood of \(a\) **does** contain \(a\), in contrast to the ordinary open Lovász neighborhood complex. The simplicial realization is finite; the assertion concerns this one graph and its ordinary, not equivariant, homotopy type. This is also the vertex-centered intrinsic Čech complex of \(P_{13}\) at inclusive graph-distance radius one.

Each of the thirteen closed neighborhoods is a distinct seven-vertex subset. Each generates a maximal six-simplex; their subfaces comprise exactly \(1171\) faces including the empty face, with face counts by cardinality

```text
cardinality: 0   1   2   3   4   5   6  7
count:       1  13  78 286 416 273  91 13
```

## Proof

**Finite combinatorial reduction.** Encode a simplex \(F\) by the integer \(m(F)=\sum_{a\in F}2^a\). For each \(a\in\{0,\ldots,12\}\), let \(B_a=\{a,a\pm1,a\pm3,a\pm4\}\), with arithmetic modulo thirteen. Construct the face set as \(\bigcup_a2^{B_a}\). The complete construction is performed from these definitions in `verify.py` without external tables.

Apply the following deterministic repeated-toggle matching to the face poset, initially including the empty face. At each stage select the unused vertex \(v\) with the most available pairs \((F,F\cup\{v\})\) in the current unmatched face set, breaking ties toward the larger label; pair all such faces and remove both. The complete pivot order is

```text
12, 10, 5, 7, 2, 4, 11, 6, 9, 3, 0, 8, 1
```

There are \(579\) matched pairs and thirteen unmatched simplices: six of dimension two and seven of dimension three. The empty face is paired with the vertex \(12\), so ignoring the empty face produces one additional critical zero-cell. This matching is globally acyclic: orient every unmatched Hasse incidence downward and every matched incidence upward; a full topological sort exhausts all \(1171\) faces and all \(4693\) incidences. Forman's theorem therefore yields a CW model with one zero-cell, six two-cells, and seven three-cells, with no one-cells or cells in larger dimensions. It is simply connected.

**Signed integral attaching degrees.** Orient every simplex by increasing vertex labels. The critical two-simplices, encoded as decimal bitmasks, are

```text
1044, 1060, 1064, 1072, 1184, 3136
```

and the critical three-simplices are

```text
58, 294, 297, 368, 610, 1176, 3585
```

For each matched lower face \(L\) with upper mate \(U\), the signed cellular boundary identity \(\partial U=0\) eliminates \(L\) with coefficient \(-\langle\partial U,L\rangle^{-1}\) times the other facets. Recursive substitution along ascending gradient paths gives the integral Morse boundary from critical three-cells to critical two-cells:

\[
\partial_3=\begin{pmatrix}
0&0&0&-1&0&0&-1\\
0&0&-1&0&1&0&0\\
0&1&0&0&0&-1&0\\
-1&1&-1&-1&-1&1&0\\
-1&0&0&0&0&0&-1\\
0&0&1&0&-1&0&0
\end{pmatrix}.
\]

All signs and entries are reconstructed in the standalone checker, not supplied as unexplained numerical output. Its Smith diagonal is \(\operatorname{diag}(1,1,1,1,2,0)\), with one extra zero column. Thus integral elementary basis changes on the two- and three-cells yield four degree-one attaching maps, one degree-two map, and two zero maps, with one unused two-cell.

**From the chain matrix to homotopy.** Since the CW model has no one-cells, its two-skeleton is \(\bigvee^6S^2\). The Hurewicz map \(\pi_2(\bigvee^6S^2)\to H_2(\bigvee^6S^2;\mathbb Z)\) is an isomorphism. Accordingly each three-cell attaching map is determined, up to homotopy, by its integral degree vector. Elementary integer row and column operations are realized by homotopy self-equivalences of the two-sphere wedge and by three-cell slides. The four degree-one attachments cancel, a degree-two attachment creates the Moore space \(M(\mathbb Z/2\mathbb Z,2)\), the unused two-cell contributes one \(S^2\), and the two zero attaching maps contribute two \(S^3\). This proves the displayed homotopy equivalence.

Finally the thirteen seven-vertex balls are distinct and all maximal, so \(K\) is pure six-dimensional. A pure shellable six-complex is homotopy equivalent to a wedge of six-spheres or is contractible; the nonzero two-torsion in degree two rules out shellability.

## Verification

Run `python verify.py` with `sympy` installed as specified by `requirements.txt`. The script independently enumerates all faces, recomputes the deterministic toggle matching, proves global acyclicity of the directed Hasse graph, reconstructs the exact signed Morse boundary, obtains its integer Smith form, and computes the original simplicial boundary ranks over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_5\).

The complete original boundary ranks in dimensions one through seven are \((1,12,66,218,195,78,13)\) in characteristic two and \((1,12,66,219,195,78,13)\) in characteristics three and five, using the augmented chain complex. These yield respectively \((\widetilde\beta_2,\widetilde\beta_3)=(2,3)\) and \((1,2)\), as required by the displayed integral decomposition and universal coefficients. Field calculations alone would not prove the integral or homotopy statements; the exact Morse boundary and the attaching-map argument supply that proof.

## Relationship to prior work

Matsushita's *Closed neighborhood complexes of graphs* (arXiv:2511.12608v1, first posted 2025-11-16) defines the closed-neighborhood construction and gives general equivalences with canonical-double-cover independence complexes, plus examples for products of complete graphs. The paper's relevant theorems and examples do not give a calculation for the Paley graph of order thirteen. Its general suspension equivalence alone does not yield the integer attaching matrix above.

The published indexed classification of the **open** Lovász neighborhood complex of the Paley graph of order seventeen concerns another graph and a different construction. Existing indexed Paley-29 independence and Rips calculations also concern different complexes and parameters. The closed-neighborhood complex here is not the ordinary flag clique complex of the Paley graph: its simplices need only lie inside a single closed neighborhood, not be pairwise adjacent. These distinctions matter for both comparisons and the proof.

## Limitations

This theorem does not classify closed-neighborhood complexes of all Paley graphs, the automorphism action on integral homology, other Čech radii, or persistent homology. Unindexed equivalent calculations remain a possible originality risk. The executed certificate proves the specified finite claim only, not an infinite-family extrapolation.

## References

1. Takahiro Matsushita, *Closed neighborhood complexes of graphs*, arXiv:2511.12608v1 (2025-11-16), https://arxiv.org/html/2511.12608v1 . Relevant definitions, Theorem 1.2, and examples in Sections 3–5.
2. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145. Discrete Morse equivalence and reduced cellular chain complexes.
3. Indexed mathematical finding, *Three-torsion in the neighborhood complex of the Paley graph of order seventeen*, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-three-torsion-in-the-neighborhood-complex-of-the-paley-graph-of--3bbd3a54ace8 (different graph and open-neighborhood operation; indexed abstract checked).
