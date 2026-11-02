# The first adaptive two-round excess for regular tournament orientations

## Finding
Let \(\mathcal R_n\) be the class of all orientations of the edges of the complete graph on a fixed labeled set of odd size \(n\), with every vertex having outdegree \((n-1)/2\). A query specifies an unordered pair of vertices and asks which vertex wins its directed edge. Then
\[
\operatorname{VCdim}(\mathcal R_7)=9,\qquad
\operatorname{Ldim}(\mathcal R_7)=11.
\]
The smaller nontrivial cases have \((\operatorname{VCdim},\operatorname{Ldim})=(1,1)\) at \(n=3\) and \((4,4)\) at \(n=5\). Thus seven vertices is the first odd order at which these static and adaptive shattering dimensions differ, and the first gap is two.

The complete seven-vertex shattered-support polynomial, where the coefficient of \(z^j\) counts labeled sets of \(j\) queried edges shattered by \(\mathcal R_7\), is
\[
1+21z+210z^2+1330z^3+5880z^4+18732z^5
+40502z^6+32490z^7+315z^8+35z^9.
\]
The nine-edge shattered sets are exactly the disjoint unions of the edge sets of a four-clique and a three-clique, hence there are \(\binom74=35\) of them. The general static VC formula and this extremal-support characterization were established separately; the new results here are the exact seven-vertex adaptive dimension, the first strict-gap conclusion, and the intermediate support census.

## Assumptions and scope
All tournaments are labeled, without loops or ties. For every \(u<v\), its edge is encoded by bit \(1\) if \(u\) defeats \(v\), and bit \(0\) otherwise. Each query is one edge direction; a complete depth-\(d\) binary mistake tree is shattered when every root-to-leaf answer sequence is realized by a (possibly different) regular tournament. The VC dimension is the maximum number of fixed edge queries whose every answer assignment is realizable. The result concerns precisely these membership/query semantics, not comparison queries between permutations or a single unlabeled tournament.

## Proof
**Orientation feasibility and static traces.** Let \(n=2m+1\), and let \(E\) be a set of queried unordered edges. An assignment of directions to \(E\) extends to a regular tournament precisely when the remaining graph \(F=K_n\setminus E\) admits an orientation with residual outdegree \(m-d_E^+(v)\) at every vertex. By the integer-valued orientation criterion (a form of Hakimi's theorem, or the partial-tournament completion criterion), this holds if and only if, for every vertex set \(S\),
\[
\sum_{v\in S}\bigl(m-d_E^+(v)\bigr)\ge |F[S]|.
\]
The left side equals \(m|S|-|E[S]|-d_E^+(S,\overline S)\), and \(|F[S]|=\binom{|S|}{2}-|E[S]|\). Thus the condition is \(d_E^+(S,\overline S)\le |S|(n-|S|)/2\). It must hold for every orientation of the queried edges. Maximizing the left side over those orientations gives the exact, previously available cut criterion
\[
E\text{ is shattered}\quad\Longleftrightarrow\quad
|\delta_E(S)|\le\frac{|S|(n-|S|)}2\quad\text{for every }S\subseteq[n].
\]
The orientation criterion's sufficiency follows from integral network flow: represent each edge of \(F\) by a unit supply that must be assigned to one endpoint, with endpoint quotas \(m-d_E^+(v)\); the min-cut inequalities are exactly the displayed inequalities. This proof requires no approximation or relaxation of integer orientations.

**Static dimension at seven.** A singleton cut forces maximum query-graph degree three. For two nonadjacent vertices of degree three, the cut around those two has size six, exceeding the allowed five. Hence all degree-three vertices of a shattered support are adjacent. A query graph with at least ten edges has degree sum at least twenty, and since every degree is at most three, it has at least six degree-three vertices. Those six would form a clique and therefore have degree at least five, a contradiction. Thus VC dimension is at most nine. The disjoint union \(K_4\sqcup K_3\) satisfies every cut inequality: if \(S\) contains \(a\) vertices from the four-clique and \(b\) from the three-clique, the difference between the number of cut edges inside the cliques and the number between them is \((a-b)(1-a+b)\le0\), since \(a-b\) is an integer. Thus nine is attained. In any shattered nine-edge graph, degree-sum counting forces exactly four degree-three vertices, which form a four-clique; the other three form a three-clique. This also proves the thirty-five-extremizer assertion.

**Exact adaptive dimension.** There are exactly \(2640\) regular labeled seven-vertex tournaments. The verifier computes this integer by exhausting the \(2^{21}\) complete edge orientations and checking all seven outdegrees; equivalently it is the coefficient of \(\prod_{v=1}^7 x_v^3\) in \(\prod_{u<v}(x_u+x_v)\). Any shattered depth-twelve binary tree needs \(4096\) distinct terminal hypotheses, so \(\operatorname{Ldim}(\mathcal R_7)\le11\).

The accompanying `depth11_tree.json` supplies an explicit complete depth-eleven tree with \(2047\) internal pair queries and \(2048\) leaves. Each leaf contains the bit mask of a regular tournament realizing its complete root-to-leaf answers. `verify.py` exhaustively reconstructs the hypothesis family and checks every query, branch, leaf outdegree, and uniqueness of the \(2048\) terminal witnesses. This gives the reverse inequality \(\operatorname{Ldim}(\mathcal R_7)\ge11\), without assuming that the computer search is itself a proof. The finite witness is a complete certificate whose local verification checks are explicit.

For \(n=3,5\), the counts of regular tournaments are respectively \(2\) and \(24\), so the binary-tree counting upper bounds are one and four. The cut criterion certifies matching shattered edge supports \(K_2\sqcup K_1\) and \(K_3\sqcup K_2\); hence the static and adaptive dimensions match at those orders.

**Full static support census.** The standalone `census.cpp` exhaustively visits all \(2^{21}=2097152\) edge subsets, tests every cut up to complementation, and accumulates the displayed support counts. Its test is exact integer arithmetic. At nine edges, it additionally checks the forced degree profile. These computations establish the polynomial exactly, using the preceding all-orientations cut equivalence.

## Verification
Reproducibility from this package: put `depth11_tree.json`, `verify.py`, `census.cpp` and optionally `make_witness.py` in the same directory. Run `python3 verify.py`; compile the independent support-census program using `g++ -O3 -std=c++17 census.cpp -o census`, then run `./census`. The first program independently enumerates all regular tournaments, replays the depth-eleven tree, and compares direct shattering against the cut criterion for every support at orders three and five and for all thirty-five nine-edge witnesses at order seven. The second program independently checks every seven-vertex support. The provided tree can also be regenerated using `python3 make_witness.py`.

The complete output of the replay is included in `verification_output.txt`. It is corroborating evidence, not a substitute for the definitions and proof above.

## Relationship to prior work
Brualdi and Kiernan (2009), Theorem 3.1, provide a general criterion for completing partial tournaments to prescribed score vectors. Sanchez and Kolesnik (first public 2020) present the relevant graphic-zonotope and integral-orientation framework. Kozma and Moran (2013) explicitly develop shattering theory for graph orientations, but their results concern connectivity and related orientation properties. Guingona, Kolesnikov, Nierwinski and Soucy (first public 2021) develop exact VC/Littlestone dimensions for families of zero sets rather than score-constrained tournaments. Earlier mathematical work already gives the static VC value and the extremal nine-edge supports for all odd orders, and those statements are not asserted as new here. None of the inspected covering candidates gives the eleven-round adaptive value or the full seven-vertex intermediate support polynomial.

## Limitations
The exact adaptive calculation is confined to seven vertices (with smaller-order comparisons). No formula for the Littlestone dimension at every odd order is proved. This is a finite classification rather than a general proof of an unbounded static-adaptive gap. Full historical priority cannot be guaranteed by database searches; the analogous online parameter may occur under different learning-theory terminology. No independent scientific audit has been performed.

## References
- R. A. Brualdi and K. Kiernan, *Landau's and Rado's Theorems and Partial Tournaments*, Electronic Journal of Combinatorics **16** (2009), N2, Theorem 3.1. DOI: 10.37236/240.
- M. Sanchez and B. Kolesnik, *The geometry of random tournaments*, arXiv:2009.09322 (first submitted 19 September 2020); subsequently Discrete & Computational Geometry **71** (2024), 1343–1351.
- L. Kozma and S. Moran, *Shattering, Graph Orientations, and Connectivity*, arXiv:1211.1319 (first submitted 6 November 2012); Electronic Journal of Combinatorics **20** (2013), P44.
- V. Guingona, A. Kolesnikov, J. Nierwinski, and R. Soucy, *Littlestone and VC-dimension of families of zero sets*, arXiv:2109.04805 (first submitted 10 September 2021).
