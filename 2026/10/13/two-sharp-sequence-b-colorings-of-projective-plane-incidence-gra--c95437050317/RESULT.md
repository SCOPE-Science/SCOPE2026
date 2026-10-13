# Two sharp sequence b-colorings of projective-plane incidence graphs

## Finding

For \(q\in\{3,4\}\), let \(L_q\) denote the point-line incidence (Levi) graph of the Desarguesian plane \(\mathrm{PG}(2,q)\). Define \(\beta_2(G)\) to be the largest integer \(k\) for which \(G\) has a **proper** vertex coloring with \(k\) nonempty color classes, each containing at least two color-dominating vertices. A vertex is color-dominating if its neighborhood contains at least one vertex of every other color.

**Finite theorem.** In both specified projective planes,

\[
\boxed{\beta_2(L_3)=5,\qquad\beta_2(L_4)=6.}
\]

In fact, there is a coloring with **exactly** two color-dominating vertices of each color in each case. Both graphs are regular of degree \(q+1\), have girth six and order \(2(q^2+q+1)\). They are natural smallest-order degree-four and degree-five examples at the girth-six boundary of the sequence b-coloring conjecture described in [1]. This theorem addresses only these two finite instances.

## Assumptions and scope

The field \(\mathbb F_3\) has ordinary arithmetic modulo three. The field \(\mathbb F_4\) is \(\mathbb F_2[t]/(t^2+t+1)\), encoded by the two-bit integers 0, 1, 2 and 3. A projective point is a one-dimensional subspace of \(\mathbb F_q^3\), represented by its unique vector with first nonzero coordinate equal to one; lines are represented analogously by nonzero coefficient triples up to scalar. A point \([x]\) is incident with a line \([a]\) exactly when \(a_0x_0+a_1x_1+a_2x_2=0\). There are \(N=q^2+q+1\) points and \(N\) lines; the graph has vertices indexed by 0 through \(N-1\) for points, then \(N\) through \(2N-1\) for lines. The order of the normalized triples is fixed by the array `points` in `certificates.json`.

Each color list in `certificates.json` assigns colors to *all* \(2N\) vertices, in that exact order, using color names 0 through \(q+1\). Thus the certificate does not require an external optimization program or any unpublished computation. The theorem is limited to \(q=3,4\); checking finitely many examples makes no assertion about further \(q\).

## Proof

**Degree upper bound.** If a graph of maximum degree \(\Delta\) admits a proper \(k\)-coloring having a color-dominating vertex, that vertex must have neighbors of the other \(k-1\) colors. Therefore \(k-1\leq\Delta\). Applied to \(L_q\), where \(\Delta=q+1\), this proves \(\beta_2(L_q)\leq q+2\), for either specified \(q\).

**Finite lower-bound certificates.** The complete arrays in `certificates.json` encode one \((q+2)\)-coloring per plane. The supplied independent checker `verify.py` reconstructs every field operation directly from the defining polynomial, generates the \(q^2+q+1\) normalized projective representatives, and recomputes the entire incidence graph by the vanishing bilinear pairing. It first asserts that the certificate's point set is exactly the normalized representatives and that each vertex has degree \(q+1\). For *each of the \(N(q+1)\) incidences*, it asserts that the endpoint colors are distinct. For *every vertex* it computes the set of colors on all of its neighbors, and counts vertices whose neighbor-color set is exactly the complement of their own color. Its resulting vectors of dominating-vertex counts are

\[
q=3:\quad (2,2,2,2,2), \qquad q=4:\quad (2,2,2,2,2,2).
\]

These are complete finite checks over precisely specified finite sets, not samples of an infinite domain. Together with the upper bound they prove both equalities. The checker's construction verifies the projective-plane incidence properties, connectedness, absence of quadrilaterals and existence of a six-cycle. Since the graph is bipartite and has no four-cycle, its girth is six. The source code and data are entirely present here and require only a standard Python interpreter.

For reference, the checker prints two distinct color-dominating vertices for each color, using the vertex indexes defined above:

- \(q=3\): 0: [0,1]; 1: [8,10]; 2: [19,20]; 3: [13,23]; 4: [5,12].
- \(q=4\): 0: [24,25]; 1: [11,17]; 2: [15,18]; 3: [7,21]; 4: [6,23]; 5: [26,28].

These index pairs merely identify witnesses; the *complete arrays and every graph edge* are checked by the executable certificate.

## Verification

In the same directory as this document, run `python3 verify.py`. This reads the complete witness `certificates.json` and prints `verification_output.txt` exactly; the recorded output can be compared byte-for-byte. Checks cover all 26 and all 42 graph vertices, all 52 and all 105 edges respectively, all vertex degree and coloring constraints, and every possible color-dominating vertex. The program also reconstructs arithmetic in both finite fields and all normalized point and line labels. Its output includes the dominating-vertex counts and the girth-six checks. No MILP solver, graph database, or external package is needed for reproduction.

## Relationship to prior work

Jakovac and Lang [1] introduced sequence b-colorings, giving the relevant definition and their conjectured extension to regular graphs of girth at least six. Their reported results establish degree-plus-one colorings with two dominating vertices of every color for arbitrary sufficiently high-girth regular graphs (girth at least seven), and separately for cubic graphs of girth six. The present examples have girth **exactly six** and degrees four and five, so these reported theorems do not imply the two instances here. Ordinary b-coloring (one dominating vertex per color) is weaker and does not imply the two-vertex condition. Standard finite-projective-plane incidence graph facts appear in [2] and are used only for the graph construction and its degree and girth.

The abstract, author and conjecture descriptions of [1] were inspected via public scholarly indexes, but the complete primary text was not obtained. Therefore absence of equivalent constructions from its full text, appendices or from unindexed literature is **not independently established**. The mathematical certificates remain verifiable regardless of priority.

## Limitations

This is a two-instance finite theorem, **not** a proof of the general girth-six regular-graph conjecture, nor a classification of all possible colorings. The proof is a reproducible exhaustive verification of two explicit complete certificates, coupled with the universal degree upper bound. The field and incidence representation, enumeration, all edge checks and the color-dominating condition are verified from actual included source and data. Independent external audit has not been performed. Published-equivalence risk remains because the full motivating preprint was inaccessible.

## References

[1] M. Jakovac and M. S. Lang, *Sequence b-colorings in graphs*, arXiv:2609.08484, first public 2026-09-08. Public summaries and conjecture description at https://www.emergentmind.com/open-problems/girth-six-regular-graphs-sequence-two and https://www.arxiv-vanity.com/papers/2609.08484/ (where accessible).

[2] C. Godsil and G. Royle, *Algebraic Graph Theory*, Springer (2001), projective geometries and incidence graphs. Bibliographic or online text available at https://djvu.online/file/xLrm4thdjUfDN.
