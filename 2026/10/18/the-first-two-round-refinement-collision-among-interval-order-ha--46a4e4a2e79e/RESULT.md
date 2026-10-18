# The first two-round refinement collision among interval-order Hasse diagrams

## Finding

A finite **interval order** is a strict partially ordered set with no induced \((2+2)\), equivalently a poset representable by closed intervals with \(x<y\) exactly when the right endpoint of \(x\)'s interval is smaller than the left endpoint of \(y\)'s interval. Its **oriented Hasse diagram** has an arc \(x\to y\) exactly when \(y\) covers \(x\). Only these cover arcs, not the entire strict order relation, are supplied to colour refinement.

Start all vertices in the same colour. In each synchronous directed counting-refinement round, recolour each vertex according to its previous colour and the two multisets of colours on its in-neighbours and out-neighbours, retaining edge direction. Two diagrams have the same \(r\)-round fingerprint when the multisets of their vertex colours after round \(r\) agree under a common canonical colour naming.

**Finite classification.** For each \(1\le n\le7\), no two nonisomorphic \(n\)-element interval orders have the same two-round fingerprint of their oriented Hasse diagrams. At \(n=8\), among all \(5335\) interval-order isomorphism types, exactly **two unordered pairs** of nonisomorphic types share a two-round fingerprint. Each pair is distinguished by a third refinement round. The two exceptional pairs are dual to one another, so there is just one exceptional pair up to simultaneous order reversal. In particular, all \(5335\) eight-element interval-order types are distinguished by three rounds.

The exact exhaustive census is:

| Number of elements | Interval-order types | Distinct two-round fingerprints | Colliding unordered pairs |
| ---: | ---: | ---: | ---: |
| 1 | 1 | 1 | 0 |
| 2 | 2 | 2 | 0 |
| 3 | 5 | 5 | 0 |
| 4 | 15 | 15 | 0 |
| 5 | 53 | 53 | 0 |
| 6 | 217 | 217 | 0 |
| 7 | 1014 | 1014 | 0 |
| 8 | 5335 | 5333 | 2 |

## Assumptions and scope

Every structure is a **nonempty, unlabeled, finite interval order**, represented for the refinement procedure by its sole named irreflexive directed **cover** relation. The domain has \(n\in\{1,\ldots,8\}\) elements. Distinctness is order isomorphism, not merely a difference in interval drawings or an orientation change. Opposite orders are regarded as distinct unless isomorphic. The two-round fingerprint records counts of complete vertex-colour types and uses a common colour vocabulary across compared structures.

A Fishburn matrix of magnitude \(m\) and weight \(n\) is an upper-triangular \(m\times m\) matrix of nonnegative integers with positive total in every row and column and total sum \(n\). Its cell \((i,j)\), \(i\le j\), represents exactly as many intervals \([i,j]\) as the matrix entry specifies. The classical Fishburn correspondence is a bijection between these matrices and interval-order isomorphism types. In particular, \(1\le m\le n\).

## Proof

**Complete finite search space.** Use the Fishburn correspondence [1,2]. For each \(n\in\{1,\ldots,8\}\) and \(1\le m\le n\), generate every upper-triangular nonnegative integer matrix of weight \(n\) by assigning a positive row sum to each of the \(m\) rows, then enumerating every weak composition of that sum into the \(m-i\) available entries of row \(i\), for \(i=0,\ldots,m-1\). Reject a matrix if any column is zero. During generation, one can also reject a partial matrix when any column with index at most the current row index is still empty, since no later row can fill it. Every admissible matrix is generated exactly once: its dimension, row sums, and within-row compositions are unique. No isomorphism pruning or random sampling is needed.

**Exact conversion to cover arcs.** Expand every matrix entry into its number of intervals. For two resulting objects \(a,b\) with intervals \([i_a,j_a]\) and \([i_b,j_b]\), define \(a<b\) if and only if \(j_a<i_b\). The cover relation is

\[
a\prec b\quad\Longleftrightarrow\quad a<b\ \land\ \neg\exists c\,(a<c\land c<b).
\]

The test for an intermediate \(c\) ranges over **all** objects, so the construction is the exact transitive reduction of the finite strict partial order, not an approximation from interval endpoint gaps.

**Exact two-round invariant.** Define \(c_0(v)=0\), and for \(r\ge0\) let

\[
c_{r+1}(v)=\Bigl(c_r(v),\ \operatorname{multiset}\{c_r(w):w\prec v\},\ \operatorname{multiset}\{c_r(w):v\prec w\}\Bigr).
\]

Each nested tuple is a canonical type, so comparing the multisets \(\{\!\{c_2(v):v\in P\}\!\}\) across two posets is exact. In particular, comparing the two-round signatures computed by `verify_fishburn.py` does not risk false equality from colour-hash collisions. Grouping all admissible matrices of a fixed weight by these signatures gives the table above.

**Exceptional cases.** The four nonisomorphic eight-element matrices consist of the following upper-triangular rows. Each row is written as its tail beginning at the diagonal, with entries in increasing column order. The two indistinguishable pairs are \((A,B)\) and \((A^*,B^*)\), where \(*\) denotes poset duality.

```text
A  = ((1,0,0,0,0,0), (1,0,0,0,0), (1,0,1,0), (2,0,0), (1,0), (1,))
B  = ((1,0,0,0,0,0), (1,0,0,0,0), (1,1,0,0), (1,1,0), (1,0), (1,))
A* = ((1,0,0,0,0,0), (1,0,1,0,0), (2,0,0,0), (1,0,0), (1,0), (1,))
B* = ((1,0,0,0,0,0), (1,1,0,0,0), (1,1,0,0), (1,0,0), (1,0), (1,))
```

Each has six rows, weight eight, and no empty row or column. Reversing interval order acts on a matrix by reflecting its nonzero entries across the anti-diagonal: \(M^*_{i,j}=M_{m+1-j,m+1-i}\). The code checks that the multisets of second-round vertex colours agree for \(A\) and \(B\), and likewise for the duals; it finds that the third-round fingerprints differ within each pair. Distinct third-round fingerprints rule out graph isomorphism, and a separate exhaustive permutation test on the four explicit eight-vertex orders independently confirms nonisomorphism. The two exceptional pairs are the only nonsingleton classes in the complete weight-eight table. These checks establish the classification, including its minimality at eight vertices.

## Verification

Three dependency-free Python 3 programs and their actual output records accompany this result. Execute them from the same directory as the document:

```sh
python3 verify_fishburn.py
python3 verify_extensions.py
python3 verify_witnesses.py
```

`verify_fishburn.py` uses the Fishburn-matrix bijection, exact cover computation, nested directed colour signatures, and full enumeration through weight eight. `verify_extensions.py` separately generates unlabeled interval orders by adjoining a maximal element above every order ideal, tests nested principal strict downsets, and uses a degree-pair normal form to remove isomorphic duplicates; it reproduces the entire table. The normal form is valid because the lower sets of an interval order are nested, as are its upper sets, so equal in/out strict-order degree pairs specify identical lower and upper sets and thus interchangeable elements. `verify_witnesses.py` reconstructs all four exceptional orders from explicit matrices, checks second- and third-round fingerprints, checks nonisomorphism by inspecting all eight-vertex permutations, and checks the order-duality pairing. The matrix class counts match the independently published Fishburn sequence [4].

## Relationship to prior work

The bijection between unlabeled interval orders, ascent sequences, and Fishburn matrices, and the characterization by nested principal downsets, are established in [1]. The precise canonical minimal interval representation and duality for Fishburn matrices are discussed in [2]. Connections between iterative counting refinement and two-variable counting logic appear in [3]. None of the inspected statements gives the rank-two cover-graph fingerprint census or the complete first eight-vertex ambiguity layer. Here the new statement concerns **two refinement rounds on directed cover relations**, not the Fishburn-count sequence, the classical interval-order characterization, or a reconstruction result using the **full** strict relation.

## Limitations

The classification is finite: it makes no assertion of two- or three-round identification for larger interval orders, and does not identify a global upper bound on refinement depth. It concerns edge directions and Hasse covers specifically; it does not apply verbatim to an undirected cover graph or to the full transitive order predicate. The finite classification has been verified through two independent exhaustive generation methods and direct witness checking, but has not undergone independent external audit or publication-priority verification. Specialized prior tabulations of cover-graph refinement could exist.

## References

[1] M. Dukes, S. Kitaev, J. Remmel, and E. Steingrímsson, *Enumerating (2+2)-free posets by indistinguishable elements*, arXiv:1006.2696, first posted 2010-06-14; Journal of Combinatorics 2 (2011), 139–163.

[2] V. Jelínek, *Catalan pairs and Fishburn triples*, arXiv:1501.05157, first posted 2015-01-21; Advances in Applied Mathematics 70 (2015), 1–31.

[3] A. Krebs and O. Verbitsky, *Universal covers, color refinement, and two-variable counting logic: Lower bounds for the depth*, arXiv:1407.3175, first posted 2014-07-11.

[4] OEIS A022493, *Fishburn numbers: number of nonisomorphic interval orders* (enumeration benchmark only).
