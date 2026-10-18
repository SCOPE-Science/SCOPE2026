# Left-endpoint anchoring makes colour refinement exactly the true-twin partition of proper interval graphs

## Finding
Let \(G\) be a finite, connected, nonempty proper interval graph (equivalently, a unit interval graph). Fix a proper interval ordering \(v_1,\ldots,v_n\), and distinguish just the leftmost vertex \(v_1\) by one unary root predicate. Start ordinary one-dimensional colour refinement with this root as one colour and every other vertex in a second colour.

**Theorem.** The stable colour classes are precisely \(\{v_1\}\) and the true-twin classes among the non-root vertices; two vertices are true twins when their closed neighbourhoods coincide. Consequently:

1. The rooted structure is identified, *among all finite rooted simple graphs*, by two-variable first-order logic with counting, \(C^2\).
2. If \(B\) ranges over the non-root true-twin classes, the root-preserving automorphism group is \(\prod_B \mathfrak S_{|B|}\).
3. The polytope of doubly stochastic root-fixing matrices commuting with the adjacency matrix is affinely \(\prod_B\mathcal B_{|B|}\), the product of Birkhoff polytopes. In particular it has only integral vertices.
4. If \(D=\max_{v\in V(G)}\operatorname{dist}(v_1,v)\), then refinement stabilizes after at most \(D+1\) rounds, with initial colouring round zero.

The endpoint condition is substantive: for the three-vertex path, marking its centre instead leaves the two nonadjacent, hence non-true-twin, endpoints in one stable class.

## Assumptions and scope
Graphs are finite simple undirected graphs. Proper interval means having a representation by closed intervals with no interval strictly containing another, or equivalently a representation by equal-length intervals. A *proper interval ordering* has the umbrella property: for all \(i<j<k\), the edge \(v_iv_k\) implies both \(v_iv_j\) and \(v_jv_k\). Such an ordering exists for every proper interval graph; ties in a proper interval representation may be ordered consistently. Connectivity is required. A true-twin class means an equivalence class under equality of closed neighborhoods \(N_G[u]=N_G[v]\).

A colour-refinement round replaces a vertex colour by the pair consisting of its old colour and the multiset of neighbours' old colours. We use canonical equality of these pairs, not arbitrary numerical labels. An equitable partition means that each vertex in a cell has the same number of neighbours in any other given cell.

## Proof
**1. Consecutive adjacency and distance layers.** In the fixed order define \(r_i\) as the largest index in \(N_G[v_i]\), and \(\ell_i\) as the smallest. The umbrella property implies \(N_G[v_i]=\{v_{\ell_i},\ldots,v_{r_i}\}\); both sequences \((\ell_i)\) and \((r_i)\) are nondecreasing. In particular \(r_i\ge i\), and connectivity forces \(r_i\ge i+1\) when \(i<n\): otherwise the initial segment through \(i\) would have no edges to the remaining vertices.

Put \(b_0=1\) and iteratively \(b_{k+1}=r_{b_k}\) until \(b_D=n\), with the smallest such \(D\). The vertices at distance exactly \(k\) from \(v_1\) are
\[
L_0=\{v_1\},\qquad L_k=\{v_{b_{k-1}+1},\ldots,v_{b_k}\}\quad(1\le k\le D).
\]
Indeed, if the root's vertices within distance \(k\) form precisely the initial segment through \(b_k\), their neighbours extend this segment precisely to \(r_{b_k}\), by monotonicity of \((r_i)\). All the layers \(L_k\), for \(k\ge1\), are cliques: if \(b_{k-1}<i<j\le b_k\), monotonicity gives \(r_i\ge r_{b_{k-1}}=b_k\ge j\).

**2. Recovering the two ends of a closed neighbourhood.** Fix \(1\le k\le D\) and \(v_i\in L_k\). No edge can skip a distance layer. The neighbours of \(v_i\) in \(L_{k-1}\) are exactly those vertices indexed from \(\ell_i\) through \(b_{k-1}\), so
\[
|N_G(v_i)\cap L_{k-1}|=b_{k-1}-\ell_i+1.
\]
For \(k<D\), its neighbours in \(L_{k+1}\) are indexed from \(b_k+1\) through \(r_i\), and hence
\[
|N_G(v_i)\cap L_{k+1}|=r_i-b_k.
\]
For \(k=D\), monotonicity and \(r_{b_{D-1}}=n\) force \(r_i=n\). Therefore the ordered pair of the previous-layer and next-layer neighbour counts determines both \(\ell_i\) and \(r_i\) uniquely for every vertex within a fixed non-root layer. For the root itself, its distinguished unary colour already isolates it.

**3. Exact stable colour classes.** At stabilization, the root's colour is unique and each root-distance layer is a union of colour classes: inductively, the root neighbourhood and then each successive layer can be distinguished by their adjacency counts to already separated preceding layers. In an equitable stable partition, two vertices of the same colour thus belong to the same layer and have identical counts into its predecessor and successor layers. By step 2, they have the same \(\ell_i,r_i\), and consequently the same closed neighbourhood. Conversely, any two non-root vertices with equal closed neighbourhoods can be transposed by a root-fixing graph automorphism and must receive the same colour at every refinement round. The claimed stable partition follows.

For the round bound, after at most \(D\) rounds the distance layers are separated (one new layer can be distinguished at each round). One further round records their adjacent-layer neighbour counts; step 2 then makes every distinct pair of non-root true-twin blocks different. Thus there are at most \(D+1\) rounds, including the cases \(D=0\) and \(D=1\).

**4. Identification by counting logic.** Every stable class is a clique, and any two distinct stable classes are either completely adjacent or completely nonadjacent: equality of closed neighbourhoods makes adjacency constant on each pair of classes. Consider an arbitrary finite rooted graph \(H\) that is equivalent to \((G,v_1)\) by colour refinement, or equivalently by \(C^2\). Use the canonical joint refinement colours of the disjoint union to match corresponding stable cells. They have the same sizes and the same per-cell neighbour counts. As the counts in \(G\) are respectively \(0\) or the entire other-cell size, every corresponding pair of cells of \(H\) is also empty or complete; and the internal count \(|B|-1\) forces each corresponding cell to be a clique. Thus the cell bijection extends to a root-preserving graph isomorphism, proving identification even outside the proper interval class.

**5. Integral fractional symmetries.** Each root-fixing automorphism necessarily preserves each stable colour cell; conversely, independent permutations inside true-twin blocks preserve every edge and the root. This gives the group formula. For fractional automorphisms, a nonnegative doubly stochastic matrix \(X\) with \(XA=AX\) and \(Xe_{v_1}=e_{v_1}\) preserves the colour-refinement cells: initially it fixes the root indicator and the all-ones vector, and inductively it fixes each stable colour-class indicator because commuting with \(A\) fixes neighbour-count vectors, while a doubly stochastic map that fixes a vector cannot mix distinct coordinate levels (strict Jensen equality). Hence \(X\) is block diagonal on the true-twin cells. Every doubly stochastic block matrix on such a cell commutes with the complete or empty adjacency blocks, and with the internal block \(J-I\). Thus all such \(X\) are exactly the Cartesian product of the \(\mathcal B_{|B|}\), whose vertices are permutation matrices by Birkhoff–von Neumann.

## Verification
Two standalone Python 3 scripts corroborate the structural result, using exhaustive right-endpoint encodings of connected proper interval orderings for every order from \(1\) through \(12\). Each encoding is a nondecreasing sequence \((r_i)\) with \(r_i\ge i+1\) for \(i<n\) and \(r_n=n\); its induced edges satisfy \(v_iv_j\in E\) for \(i<j\) precisely when \(j\le r_i\). In the converse direction every connected proper interval ordering has such an encoding.

`rooted_unit_check.py` independently runs actual iterative colour refinement and compares stable-colour equality to true-twin equality; `rooted_unit_layers.py` instead performs breadth-first search and checks clique layers and equality of predecessor/successor neighbour counts. Running `python3 rooted_unit_check.py 12` and `python3 rooted_unit_layers.py 12` gives the accompanying `.out` files. Their per-order encoding counts are \(1,1,2,5,14,42,132,429,1430,4862,16796,58786\). These are finite stress tests, **not** an exhaustive proof for unbounded graph orders. The proof in steps 1–5 establishes the all-size statements.

## Relationship to prior work
Proper/unit interval representations and their canonical vertex orderings are classical. Köbler–Kuhnert–Laubner–Verbitsky (2010), and Klavík and coauthors (2012), supply the relevant established representation setting. Arvind–Köbler–Rattan–Verbitsky (2015) develop the general relationship between colour refinement, graph identification, and compactness, including preservation of stable colour classes by fractional automorphisms. Kiefer–Schweitzer–Selman (2015) classify graphs identified by two-variable counting logic more generally.

The present claim is **not** an assertion that these foundational notions are new. Its specific all-size step is that *one distinguished geometric endpoint* of a connected proper interval graph forces every stable colour cell to be exactly a true-twin block; the resulting logical identification and fractional-symmetry formulas are consequences. The inspected primary treatments did not state this endpoint-marked class theorem or an equivalent immediate specialisation. General identification/compactness results can still imply portions once the new structural step is supplied; this is a remaining priority risk.

## Limitations
The root must be a geometric extreme of an appropriate proper interval ordering. The theorem does not claim the same stable partition for arbitrary roots, unmarked proper interval graphs, disconnected graphs, or interval graphs permitting proper containment. The ten- to twelve-vertex finite verifications alone would not establish the theorem for all orders. No claim of independent certification or exhaustive priority search is made.

## References
1. J. Köbler, S. Kuhnert, B. Laubner, O. Verbitsky, *Interval Graphs: Canonical Representations in Logspace*, ECCC TR10-043, revision 1, 19 July 2010.
2. P. Klavík and collaborators, *Extending Partial Representations of Proper and Unit Interval Graphs*, arXiv:1207.6960, 30 July 2012.
3. V. Arvind, J. Köbler, G. Rattan, O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255, 4 February 2015.
4. S. Kiefer, P. Schweitzer, E. Selman, *Graphs Identified by Logics with Counting*, arXiv:1503.08792, 30 March 2015.
