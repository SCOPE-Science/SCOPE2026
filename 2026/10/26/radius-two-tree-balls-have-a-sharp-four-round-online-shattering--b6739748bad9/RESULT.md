# Radius-two tree balls have a sharp four-round online-shattering ceiling

## Finding
For every finite nonempty simple undirected tree \(T=(V,E)\), let
\[
\mathscr B_2(T)=\{B_2(v):v\in V\},\qquad
B_2(v)=\{x\in V:d_T(v,x)\le2\},
\]
where repeated sets are identified. A complete binary decision tree of depth \(d\), whose internal nodes query membership of a vertex in the unknown ball, is **shattered** if every binary root-to-leaf answer string is realized by at least one ball in the family. Write \(\operatorname{Ldim}\) for the largest such depth.

**Theorem.** Every finite tree satisfies \(\operatorname{Ldim}(\mathscr B_2(T))\le4\). Moreover, for each integer \(n\ge1\), the exact extremal dimension over all trees of order \(n\) is
\[
\max_{|V(T)|=n}\operatorname{Ldim}(\mathscr B_2(T))=
\begin{cases}
0,&1\le n\le3,\\
1,&n=4,\\
2,&5\le n\le7,\\
3,&8\le n\le15,\\
4,&n\ge16.
\end{cases}
\]
The first four-round examples have exactly sixteen vertices. Among the \(19{,}320\) isomorphism classes of unlabelled sixteen-vertex trees, exactly \(569\) have dimension four. The complete dimension distribution at that order is:

| Littlestone dimension | Number of isomorphism classes |
| ---: | ---: |
| 0 | 1 |
| 1 | 7 |
| 2 | 227 |
| 3 | 18,516 |
| 4 | 569 |

## Assumptions and scope
Trees are finite, unweighted, simple, connected, and nonempty. The radius is fixed at **exactly two edges**, including the center and vertices at distance one. Queries can name any vertex of the same tree. No empty-ball hypothesis is adjoined. Distinct centers may define the same ball; the hypothesis family is a set of distinct vertex subsets. The assertion concerns ordinary binary Littlestone dimension, not static VC dimension, teaching dimension, compression size, randomized Littlestone dimension, or balls of arbitrary radii.

## Proof
**1. Recursion and information bound.** For a finite family \(\mathcal F\) of distinct Boolean functions on a domain \(X\), let \(\mathcal F_{x,b}\) be the version space of functions with value \(b\) at \(x\). Then
\[
\operatorname{Ldim}(\mathcal F)=
\max_{x:\mathcal F_{x,0},\mathcal F_{x,1}\ne\varnothing}
\left(1+\min_{b\in\{0,1\}}\operatorname{Ldim}(\mathcal F_{x,b})\right),
\]
with value zero if there is no nontrivial split. This follows by choosing the root of a complete shattered tree, and conversely adjoining shattered subtrees to a splitting root. The \(2^d\) terminal answer strings require distinct hypotheses, so \(\operatorname{Ldim}(\mathcal F)\le\lfloor\log_2|\mathcal F|\rfloor\).

**2. A center-star lemma.** Fix a vertex \(a\), and restrict centers to \(B_1(a)\). The corresponding family of radius-two balls has dimension at most two. Indeed, a vertex query \(x\) at distance at most one from \(a\) is positive for every candidate center. At distance two, at most two candidate centers answer positively: \(a\) and the neighbor of \(a\) on the unique \(a\)-to-\(x\) path. At distance three, at most one center answers positively; beyond that no center does. Thus every nontrivial split has a positive child containing at most two hypotheses, whose dimension is at most one. The split recurrence gives the bound two. The same conclusion holds when the candidate centers form any subset of \(B_1(a)\).

**3. A grandchild-family lemma.** Fix adjacent vertices \(p,y\), and let \(C\) be the set of centers at distance exactly two from \(p\) whose path from \(p\) does **not** start with \(y\). Divide \(C\) into groups \(C_u\) by their common first neighbor \(u\) of \(p\). Within one group, all candidates are distinct neighbors of \(u\), different from \(p\). Every radius-two membership query is either constant on \(C_u\) or positive for exactly one member. Therefore the radius-two-ball family restricted to \(C_u\) has dimension at most one. For an arbitrary query \(z\), if \(d(p,z)=0\), all centers of \(C\) answer positively; if \(d(p,z)\in\{1,2\}\), the positive candidates lie in at most one group \(C_u\); if \(d(p,z)\in\{3,4\}\), at most one center answers positively; and if \(d(p,z)\ge5\), no center does. Every nontrivial split consequently has a positive child of dimension at most one. Hence the entire family restricted to \(C\) has dimension at most two. This includes empty groups and all degenerate cases.

**4. A positive-branch lemma.** Fix \(p\), and consider the radius-two balls with centers in \(B_2(p)\). To rule out depth four for this restricted family, examine any proposed first query \(y\):

- If \(d(p,y)=0\), its negative branch is empty.
- If \(d(p,y)=1\), centers answering zero are exactly the grandchildren from Step 3, so this branch has dimension at most two.
- If \(d(p,y)=2\), let \(a\) be the midpoint of the unique length-two path. Centers answering one are exactly \(B_2(p)\cap B_2(y)=B_1(a)\), so Step 2 bounds this branch by two.
- If \(d(p,y)=3\), the positive centers are exactly the two middle vertices of the length-three path. If \(d(p,y)=4\), only its midpoint can answer positively. If \(d(p,y)\ge5\), none can answer positively. All these positive branches have dimension at most one.

Thus every nontrivial query has a child of dimension at most two. The restricted family has dimension at most three, for every finite tree and every \(p\).

**5. Universal bound and extremizers.** In a hypothetical depth-five shattered tree for \(\mathscr B_2(T)\), its root query \(p\) would have a positive child of depth four. Every ball in that child has center in \(B_2(p)\), contradicting Step 4. Hence the dimension is at most four for **every** tree, independently of its size or degree.

For any \(n\), there are at most \(n\) hypotheses, so Step 1 gives the information bound. For \(n\le3\), the diameter of every tree is at most two and every radius-two ball is the entire vertex set, yielding dimension zero. For \(n=4\), the path has a nontrivial split, while every radius-two ball contains at least three of four vertices; a depth-two tree would require a first query splitting four distinct hypotheses into two-and-two, but the only four-vertex tree with multiple distinct balls is the path, which has just three distinct balls. Therefore the maximum is one. The path on five vertices has depth two and the path on eight vertices has depth three, witnessed by the complete answer trees in `WITNESS.json`; their paths are verified independently by `verify_pure.py`.

The tree on vertices \(0,\ldots,15\) with edges

```
(0,1) (0,2) (0,4) (1,6) (1,11) (2,3) (4,5)
(6,7) (6,9) (7,8) (9,10) (11,12) (11,14) (12,13) (14,15)
```

has a complete depth-four shattered tree, explicitly given in `WITNESS.json`. Every one of its sixteen binary paths is realized by its listed distinct center, and `verify_pure.py` checks each membership directly from the edges. Finally, adjoining a new leaf to an existing tree never changes distances among old vertices, so the restrictions of the old centers' radius-two balls to old query vertices remain unchanged. Each certificate persists when arbitrarily many leaves are adjoined. The cited lower witnesses, the information bound below sixteen, and the universal bound four establish the displayed extremal formula for all \(n\).

**6. Exact first-layer census.** The attached `verify_pure.py` constructs **every** unlabeled tree through order sixteen: from each representative of order \(n-1\), it adds a new leaf at every vertex and retains one representative per center-rooted AHU tree code. Completeness holds inductively because every tree with more than one vertex has a leaf; the center-rooted AHU code is a complete invariant under tree isomorphism. On each of the resulting \(19{,}320\) nonisomorphic trees of order sixteen, it enumerates the (possibly repeated) radius-two balls, deduplicates them, and applies the exact finite shattering recurrence of Step 1. The census gives the five counts in the Finding section. A second program, `verify_networkx.py`, independently generates unlabelled trees using a different generator and recomputes dimensions by a separately written recurrence using shortest-path distances. It reproduces every count.

## Verification
With Python 3.11 or later, run `python verify_pure.py` in the directory containing `WITNESS.json`. It requires only the Python standard library and regenerates all 19,320 unlabelled sixteen-vertex trees. For an independent generator and recurrence, install NetworkX 3.x and run `python verify_networkx.py`. Both programs assert the exact distribution and output their completion markers. The pure verifier additionally checks the depth-one, depth-two, depth-three, and depth-four certificates against their explicit edge lists. `CHECKS.txt` records successful outputs of both programs. The unrestricted radius-two upper bound follows from Steps 2–5, not from the finite enumeration.

## Relationship to prior work
Chalopin, Chepoi, Mc Inerney, Ratel and Vaxès [1] study metric balls in graphs and establish size-two compression schemes for families of balls of fixed radius in trees. Their result addresses reconstructing hypotheses from samples, not the maximum depth of complete adaptively shattered binary trees; neither a four-round radius-two ceiling nor the order-sixteen census follows from the stated compression theorem. Chalopin, Chepoi, Mc Inerney and Ratel [2] study non-clashing teaching maps of ball families and give bounds in terms of VC dimension, again for a different learning invariant. Filmus, Hanneke, Mehalel and Moran [3] establish general optimal-prediction characterizations in terms of Littlestone dimensions; these do not evaluate the ball classes for trees of radius two. The present argument uses the geometric structure of center intersections with tree balls, and the extremal order/census is specifically about adaptive shattering.

## Limitations
The radius must be exactly two and distances must be unweighted tree-graph distances. The theorem does not bound Littlestone dimension for variable-radius balls, graph classes containing cycles, or arbitrary radius three or larger. The census is exhaustive only at sixteen vertices and is not a shape-by-shape classification for larger trees. Though two independent computations corroborate the census, their correctness ultimately relies on the stated canonicalization and recurrence algorithms. No independent mathematical audit or absolute historical-priority certification is claimed.

## References
1. J. Chalopin, V. Chepoi, F. Mc Inerney, S. Ratel, Y. Vaxès, *Sample compression schemes for balls in graphs*, arXiv:2206.13254, first posted June 27, 2022. https://arxiv.org/abs/2206.13254 (journal version: *SIAM Journal on Discrete Mathematics* 37 (2023), 2585–2616).
2. J. Chalopin, V. Chepoi, F. Mc Inerney, S. Ratel, *Non-Clashing Teaching Maps for Balls in Graphs*, COLT 2024, PMLR volume 247, https://proceedings.mlr.press/v247/chalopin24a.html.
3. Y. Filmus, S. Hanneke, I. Mehalel, S. Moran, *Optimal Prediction Using Expert Advice and Randomized Littlestone Dimension*, COLT 2023, PMLR volume 195, https://proceedings.mlr.press/v195/filmus23a.html.
