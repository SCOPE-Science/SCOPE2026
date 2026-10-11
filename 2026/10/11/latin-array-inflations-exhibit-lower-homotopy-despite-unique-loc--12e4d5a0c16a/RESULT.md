# Latin-array inflations exhibit lower homotopy despite unique local lifting
## Finding
Let \(n\ge3\) and \(q\ge2\). Let \(A_1,\ldots,A_n\) be sets of cardinality \(q\), and let \(T\subseteq A_1\times\cdots\times A_n\) project **bijectively** to every product of \(n-1\) coordinate sets. Such a set is an orthogonal array of strength \(n-1\) and index one, also called an \(n\)-ary quasigroup graph or Latin hypercube.

Form the simplicial complex \(K(T)\) with vertices \((i,a)\), where \(1\le i\le n\) and \(a\in A_i\). A face is a partial assignment of at most one value per coordinate; all assignments supported on fewer than \(n\) coordinates are faces, while full-support assignments are faces exactly when they belong to \(T\).

**Theorem.** The diagram over the nonempty faces of the \((n-1)\)-simplex whose value at a face is its set of allowed assignments has surjective restriction maps between **every pair of comparable faces**. Each restriction from a full-support face to a codimension-one face is bijective. Nevertheless, the corresponding finite-set-valued sheaf is **not flabby**. The associated simplicial inflation has homotopy type
\[
 |K(T)|\simeq \bigvee^{B(n,q)} S^{n-2},\qquad
 B(n,q)=(q-1)\bigl(q^{n-1}-(q-1)^{n-1}\bigr)>0.
\]
Thus even uniquely solvable codimension-one local lifting does not replace the global open-set extension hypothesis of the flabby-sheaf wedge theorem.

## Assumptions and scope
The array property means precisely that for every \(j\in\{1,\ldots,n\}\), the coordinate-forgetting map \(T\to\prod_{i\ne j}A_i\) is bijective. In particular, \(|T|=q^{n-1}\). Every \(n\ge3\) and \(q\ge2\) is realized: set \(A_i=\mathbb Z/q\mathbb Z\) and require \(a_1+\cdots+a_n=0\). The theorem is not limited to this additive array; no group structure is needed.

A diagram section over a subcomplex means compatible values on all its faces. For any nonempty coordinate subset \(I\) with \(|I|<n\), its assigned set is \(\prod_{i\in I}A_i\); for the full subset \([n]\), its set is \(T\). Restriction means dropping coordinates. The inflation is the face poset of \(K(T)\); its order complex is the barycentric subdivision of \(K(T)\), with the same homotopy type. "Flabby" uses surjectivity for restrictions of sections between **arbitrary nested open sets**, not merely face stalks.

## Proof
**1. Exact local lifting but not flabbiness.** If the target face uses fewer than \(n\) coordinates, any partial assignment can be extended to an \(n-1\)-coordinate assignment by freely choosing values on further coordinates, then to an element of \(T\) using bijectivity of one omitted-coordinate projection. This proves surjectivity for every comparable-face restriction and bijectivity for full-to-codimension-one restrictions. An open set of the dual face poset is equivalently a lower order ideal in the original face poset, hence a subcomplex. Let \(U\) be the full simplex and \(V\) its boundary. Global compatible sections on \(U\) correspond exactly to \(T\), whereas sections on \(V\) correspond to the full product \(\prod_i A_i\): every proper-face assignment must be the restriction of the chosen vertex values, and no full-face condition occurs on \(V\). Thus the restriction map has image \(T\subsetneq\prod_i A_i\), of sizes \(q^{n-1}\) and \(q^n\); it is not onto. Hence the sheaf is not flabby.

**2. Simultaneous simplicial collapses.** Let \(X=A_1*\cdots*A_n\) be the join of the discrete vertex sets. Its facets are all \(q^n\) full words and its entire \((n-2)\)-skeleton is contained in \(K(T)\). Each facet \(t\in T\) has a codimension-one face obtained by omitting coordinate \(n\). Bijectivity of the projection \(T\to A_1\times\cdots\times A_{n-1}\) ensures that this face belongs to exactly one facet. It is a free face. Distinct facets have distinct chosen free faces. Collapse all \(q^{n-1}\) pairs, in any order. The result is an \((n-2)\)-dimensional simplicial complex \(L\) homotopy equivalent to \(K(T)\).

**3. Connectivity.** A discrete set of \(q\ge2\) points has the homotopy type of a wedge of \(q-1\) zero-spheres. The join formula implies \(X\simeq\bigvee^{(q-1)^n}S^{n-1}\), hence \(X\) is \((n-2)\)-connected. Since \(K(T)\) contains the entire \((n-2)\)-skeleton of \(X\), and the only cells of \(X\) missing from \(K(T)\) have dimension \(n-1\), cellular approximation gives \(\pi_i(K(T))\cong\pi_i(X)=0\) for \(i\le n-3\), with \(\pi_0\) interpreted as connectedness. Thus \(L\) is \((n-3)\)-connected.

**4. Exact wedge multiplicity.** For \(1\le k<n\), \(K(T)\) has exactly \(\binom nk q^k\) faces with \(k\) vertices, and it has \(q^{n-1}\) faces with \(n\) vertices. The identity \(\sum_{k=0}^n(-1)^k\binom nk q^k=(1-q)^n\) gives
\[
 \widetilde\chi(K(T))=(-1)^{n-2}(q-1)\bigl(q^{n-1}-(q-1)^{n-1}\bigr).
\]
The collapse makes the dimension at most \(n-2\) while connectivity excludes homology in degrees below \(n-2\), so its sole possibly nonzero reduced integral homology group is free of rank \(B(n,q)\) in degree \(n-2\). For \(n=3\), \(L\) is a connected graph and thus a wedge of \(B(3,q)\) circles. For \(n\ge4\), \(L\) is simply connected and \((n-3)\)-connected, so the Hurewicz theorem identifies \(\pi_{n-2}(L)\) with \(H_{n-2}(L;\mathbb Z)\). Choose maps representing a homology basis to obtain \(\bigvee^{B(n,q)}S^{n-2}\to L\); it is a homology equivalence between simply connected CW complexes and hence a homotopy equivalence by Whitehead's theorem.

## Verification
The accompanying self-contained `verify.py` constructs the zero-sum arrays on \(\mathbb Z/q\mathbb Z\), checks unique codimension-one completion by exact enumeration, constructs all faces, computes exact binary boundary ranks, and checks the displayed homology formula for \(q\in\{2,3,4\}\), \(2\le n\le5\), omitting \((n,q)=(5,4)\). There are eleven tested pairs. Run `python3 verify.py` and require `VERIFY_OK 11`. These finite computations test examples; the proof above covers every orthogonal array of the stated kind, including nonlinear examples.

## Relationship to prior work
Ayzenberg--Khoroshavkina [1, Theorem 5.1 and Definition 2.20] prove a wedge of \((n-1)\)-spheres for the inflation of a simplex when the associated finite-set sheaf is inhabited and **flabby**. The present arrays deliberately violate that hypothesis despite surjectivity of every comparable-face restriction; their nonzero \((n-2)\)-homology demonstrates why the weaker condition is insufficient. The earlier vertex/edge inflation theory [2] treats flabby diagrams built by independent coordinate choices, not this globally constrained top-facet construction. The full all-array wedge computation and this local-versus-global boundary were not found in the inspected comparison sources.

## Limitations
This is an ordinary, nonequivariant homotopy-type theorem. It does not compute automorphism actions, identify individual quasigroup isomorphism classes, or classify arbitrary diagrams with nonsurjective open-set restrictions. The novelty assessment cannot rule out independent unindexed or older equivalent statements. The proof does not invoke the recent flabby theorem to establish its homotopy conclusion: that theorem's hypotheses intentionally fail here.

## References
[1] A. Ayzenberg and N. Khoroshavkina, *Homotopy types of finite étale spaces and generalized inflations*, arXiv:2602.08694v1 (first public version, 2026-02-09), https://arxiv.org/html/2602.08694v1 . Theorem 5.1, Definition 2.20, Remark 6.2, and Sections 6–7.

[2] A. Ayzenberg and V. Rukhovich, *Clique complexes of multigraphs, edge inflations, and tournaplexes*, arXiv:2012.07600v1 (2020-12-14), https://arxiv.org/html/2012.07600v1 . Background on flabby edge inflations.
