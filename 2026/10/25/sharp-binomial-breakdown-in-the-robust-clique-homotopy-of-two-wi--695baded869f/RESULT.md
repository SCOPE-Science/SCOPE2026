# Sharp binomial breakdown in the robust-clique homotopy of two width-three grids

## Finding

Let \(P_a\) denote a path on \(a\) vertices and define the rectangular grid \(G_n=P_3\square P_n\). For \(k\ge2\), set
\[
R_k(G_n)=\{W\subseteq V(G_n):\alpha(G_n[W])<k\},
\]
where \(\alpha\) is graph independence number. Each \(R_k\) is an abstract simplicial complex. For each of the two widths \(n\in\{5,6\}\), all homotopy types are as follows (a zero sphere count means a point):

| \(k\) | \(G_5\) sphere multiplicity | \(G_6\) sphere multiplicity | Sphere dimension |
|---|---:|---:|---:|
| 2 | 8 | 10 | 1 |
| 3 | 28 | 45 | 3 |
| 4 | 56 | 120 | 5 |
| 5 | 67 | 206 | 7 |
| 6 | 42 | 225 | 9 |
| 7 | 7 | 139 | 11 |
| 8 | 0 | 33 | 13 |
| 9 | 0 | 1 | 15 |
| \(\ge10\) | 0 | 0 | — |

More precisely, the realization is homotopy equivalent to \(\bigvee^{b_{n,k}}S^{2k-3}\) whenever the multiplicity \(b_{n,k}>0\), and is contractible otherwise. The precise new cases beyond existing general small-parameter theorems are \(n=5\), \(4\le k\le7\), and \(n=6\), \(4\le k\le8\). The top thresholds follow from the known maximum-independent-set structure but are included to complete both phase diagrams.

A structural comparison is the **first failure of the low-parameter binomial multiplicity**: the expression \(\binom{2(n-1)}{k-1}\) is exact at \(k=2,3,4\) for both grids, but at \(k=5\) the actual ranks are \(67<70\) and \(206<210\) for \(n=5,6\), respectively.

## Assumptions and scope

All graphs are finite simple undirected graphs, all complexes consist of subsets of the stated vertex sets, and all homotopy equivalences and homology groups are integral. The dimensions \(n=5,6\) are fixed; no conclusion is asserted for every \(n\). For the empty complex at \(k=1\), no claim is made. For \(n=5\) the graph independence number is \(8\) and for \(n=6\) it is \(9\); hence the complex is the full simplex for \(k>\alpha(G_n)\). The single \(n=5\), \(k=8\) contractible result is also checked explicitly.

## Proof

**Graph and face predicate.** Number vertices \(v=rn+c\), with \(0\le r<3\) and \(0\le c<n\). Two distinct vertices are adjacent precisely when their Manhattan coordinate distance equals one. For a vertex mask \(s\), denote the induced maximum independent-set size by \(a(s)\). If \(v\) is the least numbered vertex of \(s\), write \(b\) for its singleton bit and \(N(v)\) for its neighbor bitmask. Then
\[
a(0)=0,\qquad a(s)=\max\bigl(a(s\setminus\{v\}),\ 1+a(s\setminus(\{v\}\cup N(v)))\bigr).
\]
Consequently the exact set of nonempty faces of \(R_k(G_n)\) is \(\{s\ne0:a(s)<k\}\). The verifier independently reconstructs \(a(s)\) a second way: enumerate independent masks by testing their least bit, initialize their cardinalities, and take maximum over all submasks by a Boolean-lattice zeta transform. These two calculations agree on every one of the \(2^{3n}\) masks, so the face predicate has an independent check.

**Explicit finite Morse matching.** For each \(k\) separately, begin with all nonempty faces unmatched. Traverse pivot vertices in increasing order \(v=0,\ldots,3n-1\). At pivot \(v\), traverse mask integers \(s=1,\ldots,2^{3n}-1\), and if both \(s\) and \(s\cup\{v\}\) are presently unmatched faces and \(v\notin s\), pair them and remove them from further consideration. This constructs a partial matching on codimension-one incidences of the full nonempty face poset, without modifying the complex.

**Exhaustive acyclicity certificate.** Orient every cover incidence from larger face to smaller face, except reverse each matched incidence. In this finite directed graph, a gradient cycle exists exactly when there is a directed cycle. The accompanying standalone `verify.py` builds the in-degree of every nonempty face by visiting *every* codimension-one incidence and then performs Kahn's topological-sort algorithm, recomputing all outgoing incidences. The number removed equals the complete number of faces for every listed parameter, so every matching is acyclic; no sampling or probabilistic argument is involved. The certificate also checks the critical-cell vector, verifies matched-pair accounting, independently counts the alternating Euler sum, and independently checks the face predicate as described above.

**Critical-cell counts and conclusion.** The critical counts consist of exactly one zero-cell and \(b_{n,k}\) cells in dimension \(2k-3\) when \(b_{n,k}>0\), with no other critical cells; when \(b_{n,k}=0\), only one zero-cell remains. The exact vectors, face counts, matching counts and complete directed-cycle checks are recomputed by the included program and stated in `CHECK_RESULTS.txt`. Forman's discrete Morse theorem gives a CW model of the same homotopy type with exactly these cells. Since the only positive-dimensional cells occur in one dimension, every attaching map has target the single point in the preceding skeleton. Therefore this CW model is the asserted wedge of spheres (or a point). This argument works integrally, not merely over a coefficient field.

## Verification

Run `python3 verify.py` using the standard Python library. A successful execution ends in `GRID_3x5_PASS`, `GRID_3x6_PASS`, and `VERIFY_OK`. All \(2^{15}=32768\) and \(2^{18}=262144\) vertex masks are covered by the face checks, and each parameter's complete nonempty face-poset Hasse digraph is topologically sorted. The exact observed counts are preserved in `CHECK_RESULTS.txt`. This is a finite exhaustive proof certificate for exactly two finite graphs, not a numerical extrapolation to other strip lengths.

## Relationship to prior work

Filakovský's 2026 primary paper [1] introduces the square-sequence framework, proves the rectangular-grid homotopy formulas for \(k=2,3\) and the pure-edge-gluing case for all \(k\), and states a general higher-parameter sphere-wedge conjecture; its explicit 2026 version identifies corner gluing at \(k>3\) as an obstruction to the available proof. Both \(3\times5\) and \(3\times6\) grids have corner gluings, so that edge-only theorem does not imply the present larger-parameter cases. Chandrakar and collaborators [2] determine the total \(k\)-cut complexes of \(2\times n\) grids and total \(3\)-cut complexes of \(3\times n\) grids; Alexander duality alone transports homology, not the missing higher-parameter homotopy types. The results for two new strip lengths are distinct from the previous \(4\times4\) rectangular-grid classification and the at-most-four-square sequences. The newly determined \(k=4\) and above cases supply additional finite evidence for the sphere-dimension conjecture and exact counterexamples to extending the naive binomial count.

## Limitations

The theorem is restricted to \(n=5,6\), and does not prove the global square-sequence conjecture. Computations are exhaustive only for the explicitly defined finite cases, and a separate independent external mathematical audit has not been performed. Bibliographic priority remains uncertain for possibly unindexed computations, inaccessible appendices, and the 2024/2026 grid literature beyond inspected material. The theorem makes no claim about torsion in complexes outside these two graphs.

## References

1. Marek Filakovský, *The Topology of k-Robust Clique Complexes in Grid-like Graphs*, arXiv:2602.11365, first posted 2026-02-11; version 4 (2026-08-10), especially Theorems 1–3, Example 10, Conjecture 5 and their proofs. https://arxiv.org/html/2602.11365
2. Himanshu Chandrakar, Nisith Ranjan Hazra, Debotosh Rout and Anurag Singh, *Topology of Total Cut and Cut Complexes of Grid Graphs*, arXiv:2408.07646, first posted 2024-08-14; author-uploaded preprint text and Theorems 1.1, 3.2, 4.2. https://arxiv.org/abs/2408.07646
3. Margaret Bayer, Mark Denker, Marija Jelić Milutinović, Rowan Rowlands, Sheila Sundaram and Lei Xue, *Total Cut Complexes of Graphs*, arXiv:2209.13503, first posted 2022-09-27. https://arxiv.org/abs/2209.13503
4. Andrés Carnero Bravo, *Total Cut Complexes and Their Duals*, arXiv:2602.21427, first posted 2026-02-24 (abstract inspected). https://arxiv.org/abs/2602.21427
