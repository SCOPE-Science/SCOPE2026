# A torsion-to-sphere-wedge transition for bidirected bipartite multipath complexes

## Finding
For each integer \(n\ge5\), let \(D_n\) be the loopless digraph obtained from the undirected complete bipartite graph \(K_{2,n}\) by replacing each edge with its two opposite directed arcs. Let \(X_n=X(D_n)\) be its multipath complex: the simplicial complex on all \(4n\) arcs whose faces are the sets of arcs forming vertex-disjoint directed simple paths and isolated vertices (directed cycles, including two-cycles, are forbidden).

There is an integral homotopy-type transition:
\[
|X_n|\simeq
\begin{cases}
M(\mathbb Z/2,2)\vee\bigvee^{31}S^3,&n=5,\\
\bigvee^{\mu_n}S^3,&n\ge6,
\end{cases}
\quad\text{where}\quad
\mu_n=n^4-8n^3+19n^2-14n+1.
\]
Here \(M(\mathbb Z/2,2)\) is the simply connected Moore space obtained by attaching a three-cell to a two-sphere by a map of degree two. Thus \(\widetilde H_2(X_5;\mathbb Z)=\mathbb Z/2\), \(\widetilde H_3(X_5;\mathbb Z)=\mathbb Z^{31}\), while \(\widetilde H_3(X_n;\mathbb Z)=\mathbb Z^{\mu_n}\) for every \(n\ge6\); all other reduced integral homology groups vanish. In particular, the smallest displayed complex is not shellable, since shellable complexes have torsion-free integral homology.

## Assumptions and scope
The two vertices in the small bipartition class are called hubs \(a\) and \(b\); the other \(n\) vertices are leaves numbered \(0,\ldots,n-1\). An arc is labeled by an integer: \(4j+2h\) labels the arc from hub \(h\in\{0,1\}\) to leaf \(j\), and \(4j+2h+1\) labels the reverse arc. An augmented face means a face together with the empty face, which is used only for reduced discrete Morse matching. The wedge equivalences concern geometric realizations, with no equivariance asserted. Every integer \(n\ge5\) is covered, but no statement about \(n<5\) is claimed.

## Proof
**1. Dimension and face enumeration.** In any multipath, each of the two hubs has at most one entering and one leaving arc. Consequently at most four arcs can be selected. Let \(f_k\) be the number of augmented faces containing exactly \(k\) arcs. Direct classification gives
\[
(f_0,f_1,f_2,f_3,f_4)
=\bigl(1,4n,6n^2-4n,4n(n-1)^2,n(n-1)^2(n-2)\bigr).
\]
For two arcs, either they use the same hub, contributing \(2n(n-1)\), or one uses each hub, contributing \(4n^2-2n\). For three arcs, choose the hub used twice, its distinct entering and leaving leaves, and an entering or leaving arc at the other hub avoiding the corresponding collision: \(2\,n(n-1)\,2(n-1)\) possibilities. For four arcs choose the first hub's entering leaf and distinct leaving leaf (\(n(n-1)\) choices), then the second hub's entering and leaving leaves subject to indegree/outdegree constraints and exclusion of directed four-cycles (\((n-1)(n-2)\) choices). These are all cases; higher faces cannot occur.

**2. An explicit augmented Morse matching.** Given an ordered list of arc labels \(p_1,\ldots,p_t\), begin with every augmented face unmatched. At stage \(i\), simultaneously pair each still-unmatched face \(F\) not containing \(p_i\) with \(F\cup\{p_i\}\), provided the latter is also a still-unmatched face. The pairs are disjoint within a stage. This construction is acyclic for every face complex and every pivot list. Indeed, suppose a closed gradient path existed, and choose the earliest stage \(i\) among its matched edges. An upward edge matched at stage \(i\) inserts \(p_i\), whereas upward edges from later stages do not change membership of \(p_i\). An unmatched downward edge cannot remove \(p_i\): both incident faces are matched at stages at least \(i\), so were still present at stage \(i\), at which they would necessarily have been paired if they differed only by \(p_i\). Hence a closed gradient path cannot return to its starting face after inserting \(p_i\), a contradiction. This is the sequential element-matching acyclicity argument.

**3. The uniform finite-locality certificate.** For \(n\ge6\), use only the arcs on the first six leaves and the fixed pivot sequence

`18,9,22,21,7,15,5,19,3,1,12,14,16,0,23,10,6,11,8,17,2,4,13,20`.

The standalone `verify.py` exhaustively reconstructs all faces for \(n=9\), runs these 24 stages, checks all oriented Hasse incidences for acyclicity, and verifies that **every face with at most three arcs is matched**. This finite check proves the assertion for every \(n\ge6\), not just for nine leaves: a face of at most three arcs uses at most three leaves outside the first six; injectively relabel those leaves as \(6,7,8\). Membership of any face and every toggle by one of the 24 fixed pivot arcs depends only on its selected arc endpoints and hence is invariant under this relabeling. Induction over the pivot stages shows the face has exactly the same matched/unmatched status as its image in \(D_9\). This argument covers every possible face involving any number of additional unselected leaves. Therefore the only critical faces in the augmented matching have four arcs. Their number is forced by cancellation of paired faces in the alternating augmented face count:
\[
\mu_n=f_4-f_3+f_2-f_1+f_0=n^4-8n^3+19n^2-14n+1.
\]
Discard the pair between the empty face and its singleton in the ordinary nonaugmented face poset; that singleton becomes the unique critical zero-cell and every other critical cell is unchanged. A discrete Morse CW complex for the geometric realization consequently has one base zero-cell and precisely \(\mu_n\) three-cells, with no cells in dimensions one or two. All three-cell attaching maps are constant because the two-skeleton is a point, giving \(\bigvee^{\mu_n}S^3\) **integrally and in homotopy**.

**4. The five-leaf boundary and exact integral torsion.** For \(n=5\), instead use the pivot list

`6,2,13,18,5,19,8,1,10,3,11,0,7,15,9,14,16,17,4,12`.

An exhaustive acyclic matching leaves exactly one critical two-cell, represented by arc triple `(2,5,11)`, and 32 critical three-cells; after discarding the empty/singleton pair the ordinary Morse CW has one critical zero-cell and no one-cells. Using signed simplicial boundaries and algebraic unit-incidence cancellations along the matching, the integral Morse boundary from the 32 three-cells to the single two-cell has entries \(+2\) eleven times, \(-2\) ten times, and \(0\) eleven times. The standalone program calculates this **signed integer row** by the explicit recursive elementary-cancellation formula and also verifies the full Hasse matching acyclic. Its greatest common divisor is exactly two. By an integral unimodular change of basis in the 32-dimensional domain, the attaching degrees become \((2,0,\ldots,0)\). Because \(\pi_2(S^2)\cong\mathbb Z\) and the two-skeleton is a single two-sphere, this yields one degree-two Moore summand and 31 trivially attached three-spheres, as asserted. Independent boundary-rank computations over characteristics two and three check the predicted torsion-sensitive change without being used as a substitute for the integral calculation.

## Verification
Run `python3 verify.py` with Python 3.9 or newer; no third-party modules are required. The program enumerates faces directly from indegree, outdegree and directed-acyclicity tests, checks the exact five-leaf signed Morse boundary and prime-field chain ranks, and checks the uniform six-leaf pivot matching for input sizes six through ten. For nine leaves it exhaustively verifies the finite-locality representative and the entire oriented Hasse graph. Successful output ends with `BIDIRECTED_K2N_TORSION_TO_SPHERE_WEDGE_EXACT_OK`. The infinite theorem uses the proved locality reduction, the proved universal acyclicity of sequential element matching, and elementary discrete Morse theory; checking a few parameter values alone would not suffice.

## Relationship to prior work
Caputi, Collari, Di Trani and Smith's foundational 2022 preprint defines multipath complexes and computes an Euler-characteristic formula for *one-way oriented* complete bipartite digraphs; the arrows in its bipartite family all point from one part to the other. That simplicial complex is a chessboard matching complex and is not the present bidirected complex with 2- and 4-cycles. The 2026 paper of Caputi, Collari and Smith treats bidirectional *paths* and *polygons*, not complete bipartite graphs. The published bidirected double-star multipath classification concerns a tree with adjacent branching centres and independent pendant leaves; the present digraph has two nonadjacent hubs sharing all leaves and many bidirected four-cycles, so the double-star theorem does not imply this result. Likewise, ordinary Morse matching complexes and two-matching complexes on underlying undirected bipartite graphs impose different face conditions. Searches for these mathematical aliases and the exact polynomial identified no source establishing the present theorem; this is evidence for, not proof of, originality.

## Limitations
Only fully bidirected \(K_{2,n}\) for \(n\ge5\) is treated, not arbitrary bipartite orientations or bipartition sizes. The finite-check reduction depends on the explicitly provided pivot list and on its complete exhaustive check, not on a general unverified finite pattern. No automorphism-group action is classified, and no assertion of uniqueness in all unpublished or unindexed literature is made. The scientific review associated with this result is not an independent mathematical audit.

## References
1. L. Caputi, C. Collari, S. Di Trani, J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656v1, publicly posted 2022-08-09, https://arxiv.org/abs/2208.04656 (especially Section 3.2).
2. L. Caputi, C. Collari, J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670v1, publicly posted 2026-01-09, https://arxiv.org/abs/2601.05670 (introduction, Sections 1–2).
3. *Homotopy classification of bidirected double-star multipath complexes*, published mathematical research record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-homotopy-classification-of-bidirected-double-star-multipath-comp--9525e342e100 (full RESULT.md inspected).
4. R. Forman, *Morse theory for cell complexes*, Adv. Math. 134 (1998), 90–145 (discrete Morse theory).
