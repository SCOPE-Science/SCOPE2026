# Eleven rank-three theories of finite cycle powers

## Finding

Let \(k\ge1\) and \(n\ge2k+1\) be integers. Let \(G_{n,k}=C_n^k\) be the finite simple graph on \(\mathbb Z/n\mathbb Z\) in which distinct vertices are adjacent exactly when their cyclic distance is at most \(k\). Consider first-order logic in the language consisting of equality and one undirected adjacency relation, with no named vertices, ordering, or distance predicate. Write \(G\equiv_3 H\) when the graphs satisfy the same sentences of quantifier rank at most three.

**Theorem.** The complete equivalence classification comprises precisely the following eleven cases, with each row one equivalence class. No two different rows are equivalent.

| Class | Exact parameter condition | Smallest representative | Order |
|---|---|---|---:|
| A | \(n=2k+1\) | \(G_{3,1}\) | 3 |
| B | \(k=1,\ n=4\) | \(G_{4,1}\) | 4 |
| C | \(k=1,\ n=5\) | \(G_{5,1}\) | 5 |
| D | \(k=1,\ n=6\) | \(G_{6,1}\) | 6 |
| E | \(k=1,\ n\ge7\) | \(G_{7,1}\) | 7 |
| F | \(k\ge2,\ n=2k+2\) | \(G_{6,2}\) | 6 |
| G | \(k\ge2,\ 2k+3\le n\le3k+1\) | \(G_{7,2}\) | 7 |
| H | \(k\ge2,\ n=3k+2\) | \(G_{8,2}\) | 8 |
| I | \(k\ge2,\ 3k+3\le n\le4k+1\) | \(G_{9,2}\) | 9 |
| J | \(k\ge2,\ n=4k+2\) | \(G_{10,2}\) | 10 |
| K | \(k\ge2,\ n\ge4k+3\) | \(G_{11,2}\) | 11 |

Thus every finite cycle power has a rank-three-equivalent cycle power on at most eleven vertices. This bound is **sharp within this family**: class K has no representative of order below eleven. In particular, all cycle powers satisfying \(k\ge2\) and \(n\ge4k+3\) have one common rank-three theory, though their graph orders and degrees are unbounded.

## Assumptions and scope

The cycle order is \(n\ge3\); the power is an integer \(k\ge1\); and the restriction \(n\ge2k+1\) avoids duplicate descriptions of the same complete graph obtained with greater exponents. The boundary \(n=2k+1\) is included. All graphs are finite, simple, undirected and uncoloured. Rank means **quantifier rank**, not the number of variables, counting-logic rank, or graph-theoretic rank. The theorem neither describes higher quantifier ranks nor arbitrary circulant graphs.

## Proof

**1. Exact three-round invariant for a vertex-transitive graph.** For a fixed ordered pair \((x,y)\), its rank-one first-order type is exactly its atomic diagram (whether \(x=y\) and whether \(E(x,y)\)) together with the *set*, not multiset, of atomic diagrams attained by the triples \((x,y,z)\) for all vertices \(z\). This follows by the definition of rank-one formulas: one additional existential choice can test every atomic triple configuration, while Boolean combinations detect the set of possible configurations. The recursive Ehrenfeucht–Fraïssé characterization then says that the rank-two type of a selected vertex \(x\) is determined by the set of all such ordered-pair rank-one types, as \(y\) varies. The rank-three theory of the unpointed graph is determined by the collection of these rank-two pointed types as \(x\) varies. Since \(G_{n,k}\) is vertex-transitive, this last collection contains only one type. Consequently **two cycle powers are rank-three equivalent if and only if their fixed-vertex sets of ordered-pair rank-one types coincide**.

For \(x=y\), the third vertex has either an edge or a nonedge to \(x\), or equals \(x\). For \(x\ne y\), the two equality cases \(z=x\) and \(z=y\) are determined by the adjacency of the pair. The only remaining data are which of the four patterns \((E(x,z),E(y,z))\in\{(0,0),(0,1),(1,0),(1,1)\}\) occur with \(z\ne x,y\). The dihedral symmetry interchanging \(x,y\) makes the two mixed patterns simultaneously present or absent. Thus the claimed rank-three invariant is completely encoded by the diagonal pattern, and the sets of patterns for adjacent and nonadjacent distinct pairs.

**2. Exact overlap counts.** Write \(L=2k+1\), \(s=n-L\ge0\), fix \(x=0\), and take \(y=d\) at circular distance \(1\le d\le\lfloor n/2\rfloor\). Put \(a=1\) when \(d\le k\), and \(a=0\) otherwise. The two closed cyclic \(k\)-balls, each of length \(L\), have intersection size

\[
 t(d)=\max(0,L-d)+\max(0,d-s).
\]

This identity follows by intersecting the two length-\(L\) circular intervals along the two complementary arcs of lengths \(d\) and \(n-d\). Removing the selected endpoints gives the following *exact numbers* of third vertices in the both-adjacent, each exclusive-adjacent, and neither-adjacent patterns:

\[
 c(d)=t(d)-2a,\qquad
 u(d)=2k+a-t(d),\qquad
 w(d)=s-L+t(d).
\]

The two exclusive-adjacent counts are equal by the reflection exchanging the endpoints. Every count is nonnegative. To encode the presence pattern, use the mask \(1\) for neither-adjacent, \(2\) and \(4\) for the two mixed orientations, and \(8\) for both-adjacent. Therefore the mask at distance \(d\) is

\[
 M(d)=8\,[c(d)>0]+6\,[u(d)>0]+[w(d)>0],
\]

where brackets are truth-value indicators. For the diagonal pair \(x=y\), the mask is \(8\) in a complete graph and \(9\) otherwise.

**3. Uniform sign analysis and exhaustive classification.** The following table lists the complete diagonal mask and all realized masks for *adjacent* and *nonadjacent* distinct pairs. Empty entries mean no pair of that kind exists. These are sets, not counts of pairs.

| Class | Diagonal | Adjacent masks | Nonadjacent masks |
|---|---:|---|---|
| A | 8 | 8 | — |
| B | 9 | 6 | 8 |
| C | 9 | 7 | 14 |
| D | 9 | 7 | 6, 15 |
| E | 9 | 7 | 7, 15 |
| F | 9 | 14 | 8 |
| G | 9 | 14, 15 | 14 |
| H | 9 | 15 | 14 |
| I | 9 | 15 | 14, 15 |
| J | 9 | 15 | 6, 15 |
| K | 9 | 15 | 7, 15 |

Here is an algebraic verification of the table, valid for **all integers** in the stated ranges. For \(k\ge2\), first take \(s=0\) (A) and \(s=1\) (F), which follow immediately by inserting the two values into the displayed formulas. When \(2\le s\le k\) (G), on adjacent distances \(d\le k\), the neither-adjacent count is positive for \(d<s\) and zero for \(d\ge s\); both cases occur, and the other two counts are positive. Every nonadjacent distance has both-adjacent and mixed counts positive but neither-adjacent count zero. At \(s=k+1\) (H), the same argument makes every adjacent pair realize mask 15 and every nonadjacent pair mask 14. For \(k+2\le s\le2k\) (I), all adjacent pairs realize 15, whereas the available nonadjacent distances include both \(d=k+1<s\) (mask 15) and \(d=s\le\lfloor n/2\rfloor\) (mask 14). At \(s=2k+1=L\) (J), \(d=L\) is an attainable nonadjacent distance with \(t=0=w\), while smaller nonadjacent distances have positive common-neighbor and neither-neighbor counts. For \(s\ge L+1\) (K), \(d=L\) is again attainable, now with \(t=0<w\), while \(d=k+1<L\) realizes positive counts of all three kinds. At all these cases, the stated strict inequalities follow directly from \(t(d)=(L-d)_++(d-s)_+\); no computational extrapolation is used. Finally, \(k=1\) has \(n=3,4,5,6\) or \(n\ge7\). Checking the possible distances \(d\) in the same formulas gives rows A–E; the last row stabilizes because \(d=2\) realizes the common-neighbor pattern and \(d\ge3\) realizes its absence.

Each row has a distinct encoded fixed-vertex rank-three type, so the first step proves both that all members of a row are equivalent and that no two rows are equivalent. The given smallest representatives follow by minimizing \(n\) subject to each nonempty parameter range. In particular the first member of K is \(n=11,k=2\), establishing sharpness.

## Verification

Run `python3 verify.py` from a directory containing this file and the standalone program. It requires only the Python standard library. The program (i) recomputes the closed-neighborhood overlap formulas across 34,268 parameter pairs, (ii) independently builds actual adjacency matrices and compares every third-vertex pattern in 132 graphs, (iii) calculates complete ordered atomic-triple extension types without using the overlap formulas and distinguishes all eleven canonical classes, and (iv) checks their least-order representatives. The supplied `verification_output.txt` records the successful run. All finite calculations corroborate the algebraic sign analysis above; **the proof for unbounded parameters is the displayed interval-count argument**, not these finite tests.

## Relationship to prior work

Brown and Hoshino (2007) completely classify Ehrenfeucht–Fraïssé games on *ordinary paths and cycles*. Their three-round cycle cutoff accounts for the \(k=1\) portion of this table; that portion is not claimed as novel. Lin, Rautenbach, Soulignac and Szwarcfiter (2010, journal 2011) provide structural and recognition characterizations of powers of cycles and explain their relation to regular unit circular-arc graphs. Their characterization does not determine three-round first-order equivalence. Existing work on rooted counting colour-refinement of cycle powers concerns a distinct, stronger-signature/rooted counting-refinement process and does not imply the unrooted rank-three classification here. The contribution asserted here is the complete unmarked two-parameter **power** classification, its collision pattern across different exponents, and its sharp eleven-vertex representative bound.

## Limitations

The theorem is specific to pure adjacency first-order sentences of rank at most three and to the entire family \(n\ge2k+1\), \(k\ge1\). It gives a sharp representative bound only **within this family**, not among arbitrary graphs. The exact table is established mathematically but has not undergone independent scientific audit. The originality comparison uses the identified primary literature and searchable records; equivalent unindexed work remains a residual possibility.

## References

1. J. I. Brown and R. Hoshino, “The Ehrenfeucht–Fraïssé Game for Paths and Cycles,” *Ars Combinatoria* **83** (2007), 193–212, published April 30, 2007. https://combinatorialpress.com/article/ars/Volume%20083/volume-83-paper-13.pdf
2. M. C. Lin, D. Rautenbach, F. J. Soulignac and J. L. Szwarcfiter, “Powers of cycles, powers of paths, and distance graphs,” *Discrete Applied Mathematics* **159** (2011), 621–627, first available online April 21, 2010, DOI 10.1016/j.dam.2010.03.012. https://bibliotecadigital.exactas.uba.ar/download/paper/paper_0166218X_v159_n7_p621_Lin.pdf
3. L. Libkin, *Elements of Finite Model Theory*, Springer, 2004, Chapter 3 (standard quantifier-rank Ehrenfeucht–Fraïssé recursion).
