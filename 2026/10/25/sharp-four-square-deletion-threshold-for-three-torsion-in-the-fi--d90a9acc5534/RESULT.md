# Sharp four-square deletion threshold for three-torsion in the five-by-five chessboard complex

## Finding
Let \(B=[5]\times[5]\). For \(F\subseteq B\), write \(\Delta_F\) for the simplicial complex whose vertices are allowed board cells \(B\setminus F\) and whose simplices are sets of cells no two sharing a row or a column. For every forbidden set with \(|F|\le4\),

\[
H_2(\Delta_F;\mathbb Z)\cong
\begin{cases}
\mathbb Z^8,& |F|=4\text{ and all four forbidden cells lie in one row or column},\\
\mathbb Z^7,& F=\{r_1,r_2\}\times\{c_1,c_2\},\\
\mathbb Z/3\mathbb Z,&\text{otherwise}.
\end{cases}
\]

In particular, no set of at most three forbidden squares removes three-torsion. The first possible deletion cardinality is four; among the \(\binom{25}{4}=12650\) choices of four squares, exactly \(50\) single-row/column four-stars and \(100\) full two-by-two rectangles remove it. The remaining \(12500\) four-square deletions preserve precisely one \(\mathbb Z/3\mathbb Z\) factor in second integral homology.

## Assumptions and scope
The board consists of five labeled rows and five labeled columns; forbidden squares are removed as vertices of the usual chessboard/matching complex \(\Delta_{5,5}\). The homology groups are unreduced integral simplicial homology, with conventional signed boundary maps on oriented faces. Every statement quantifies over **all** subsets \(F\subseteq [5]\times[5]\) of cardinality zero through four. No assertion is made about larger deletion sets, homotopy types of the subcomplexes, or maps induced on homology by inclusion.

## Proof
**1. Orbit completeness.** Two forbidden sets yield isomorphic complexes when related by independent permutations of the five rows and five columns, or by transposition. The self-contained verifier constructs all orbit representatives inductively: start from the empty set and add one cell to representatives at the preceding cardinality, canonically relabeling the occupied row and column indices and allowing transposition. This procedure is complete because deleting a cell from any size-\(k\) set produces some size-\((k-1)\) set, which can be moved to the previously enumerated representative before re-adding a cell. There are respectively \(1,1,2,4,10\) orbits at cardinalities \(k=0,1,2,3,4\). A second computation independently applies all \(5!\) row and \(5!\) column permutations and transpose to each representative; the orbit sizes sum to \(\binom{25}{k}\) at each \(k\). Thus there are no omitted deletion patterns.

**2. Signed chain complexes.** The verifier enumerates, for each representative, every nonattacking rook configuration of cardinality one through five, orienting each face by increasing row index. For a \(d\)-face \([v_0,\ldots,v_d]\), the boundary is \(\partial_d[v_0,\ldots,v_d]=\sum_{i=0}^d(-1)^i[v_0,\ldots,\widehat v_i,\ldots,v_d]\). It constructs sparse integer matrices \(\partial_1,\partial_2,\partial_3\). Since no row or column permutation alters the integral isomorphism type of homology, it suffices to compute these for the complete orbit list.

**3. Exact integral reduction, not a modular approximation.** For each boundary matrix, the verifier repeatedly uses a coefficient \(\pm1\) as an integral Smith pivot: subtract integer multiples of the pivot row or column to clear the corresponding column and row, then discard this unit direct summand. All operations are invertible over \(\mathbb Z\), so the result is integrally equivalent to \(\operatorname{diag}(I_p,R)\). For both \(\partial_1\) and \(\partial_2\), this procedure leaves the zero matrix, establishing ranks \(f_0-1\) and \(f_1-f_0+1\), respectively (here \(f_i\) counts \(i\)-faces). For \(\partial_3\), the residual is either zero or rank one over \(\mathbb Q\). Rank-one status is checked **exactly** by verifying all two-by-two minors vanish, including those involving zero entries. In the latter case the greatest common divisor of *all* residual entries is exactly three; thus its Smith form has a single nonunit invariant factor three. A zero residual has none. No finite-field rank estimate is substituted for these integral certificates.

**4. Recovering second homology.** The integral chain sequence implies \(\operatorname{Tor}(H_2)\cong\operatorname{Tor}(\operatorname{coker}\partial_3)\), because the quotient by \(H_2\) inside \(\operatorname{coker}\partial_3\) identifies with the free abelian group \(\operatorname{im}\partial_2\). Therefore a rank-one residual with gcd three yields exactly \(\mathbb Z/3\mathbb Z\) torsion; a zero residual yields torsion-free \(H_2\). The free rank is calculated, without dimension shifting, from
\[
\operatorname{rank}H_2=f_2-\operatorname{rank}\partial_2-\operatorname{rank}\partial_3.
\]
The verifier confirms zero free rank in all sixteen nonexceptional orbits and free rank eight or seven in the two exceptional orbits.

**5. Enumeration of the two exceptional patterns.** The four-star orbit consists of \(5\binom54\) row-star sets and the same number of column-star sets, altogether \(50\). A full two-by-two rectangle is chosen in \(\binom52^2=100\) ways. These families are disjoint. All other four-cell configurations form eight orbits totaling \(12500\) labeled sets and have exactly the three-torsion asserted. The counts also independently total \(12650\).

For a compressed reproduction of the orbit certificate, a forbidden cell \((r,c)\) is indexed by \(5r+c\) in zero-based coordinates. For \(k=4\), the ten canonical orbit keys and sizes are

| Canonical key | Orbit size | Exact second homology |
| --- | ---: | --- |
| `(0,1,2,3)` | 50 | \(\mathbb Z^8\) |
| `(0,1,2,5)` | 1200 | \(\mathbb Z/3\mathbb Z\) |
| `(0,1,2,8)` | 800 | \(\mathbb Z/3\mathbb Z\) |
| `(0,1,5,6)` | 100 | \(\mathbb Z^7\) |
| `(0,1,5,7)` | 1200 | \(\mathbb Z/3\mathbb Z\) |
| `(0,1,5,12)` | 3600 | \(\mathbb Z/3\mathbb Z\) |
| `(0,1,7,8)` | 600 | \(\mathbb Z/3\mathbb Z\) |
| `(0,1,7,12)` | 900 | \(\mathbb Z/3\mathbb Z\) |
| `(0,1,7,13)` | 3600 | \(\mathbb Z/3\mathbb Z\) |
| `(0,6,12,18)` | 600 | \(\mathbb Z/3\mathbb Z\) |

## Verification
Run `python3 verify.py` using Python 3.10 or newer, with the standard library only. It enumerates complete orbit representatives, compares independent orbit-size counts with all \(\binom{25}{k}\) labelings, generates signed simplicial chain matrices, runs exact integral unimodular reductions, checks every two-by-two residual minor and gcd, and asserts the complete torsion and free-rank classification. `verify_output.txt` contains the output of this exact program, ending in `VERIFY_OK_CHESSBOARD_FOUR_DELETION_TORSION_THRESHOLD`. Neither the log nor a finite-field probe is used as a substitute for the executable exact certificate.

## Relationship to prior work
Shareshian and Wachs, *Torsion in the Matching Complex and Chessboard Complex*, first available as arXiv:math/0409054v1 on 2004-09-03, establishes the classical \(\mathbb Z/3\mathbb Z\) second homology of the full five-by-five board and treats separately a board with its full diagonal removed. Those statements do **not** classify the effect of deleting zero through four arbitrary squares. Jonsson's *On the 3-torsion Part of the Homology of the Chessboard Complex* (arXiv:1203.5644) develops other chessboard subcomplexes, notably restrictions at a selected row/column, but does not determine these ten low-deletion orbits and their sharp threshold. Clark and Zeckner's *Simplicial Complexes of Triangular Ferrers Boards* (arXiv:1008.4525) addresses a restricted board shape; it does not cover the full arbitrary-forbidden-cell classification. These are comparisons of mathematical implications rather than titles. General matching-complex torsion and rook-graph topology results were also searched; no identified statement implies this complete classification.

## Limitations
The theorem applies only to second integral homology and at most four missing cells on the five-by-five square board. It does not classify the full homotopy type or all other homology degrees. A torsion-free subcomplex can map onto torsion in a larger complex under inclusion, so absence of torsion in the two exceptional subcomplexes does **not** prove vanishing of the induced inclusion map to the full board's second homology. Orbit completeness and Smith factors are established by an executable finite integer certificate, not by a shorter symbolic closed-form classification. Equivalent work in a nonindexed board-homology table remains an originality risk; no claim of globally proven novelty is made.

## References
1. J. Shareshian and M. Wachs, *Torsion in the Matching Complex and Chessboard Complex*, arXiv:math/0409054v1, 2004-09-03. https://arxiv.org/abs/math/0409054
2. J. Jonsson, *On the 3-torsion Part of the Homology of the Chessboard Complex*, arXiv:1203.5644v1 (2012). https://arxiv.org/abs/1203.5644
3. R. Clark and A. Zeckner, *Simplicial Complexes of Triangular Ferrers Boards*, arXiv:1008.4525 (2010). https://arxiv.org/abs/1008.4525
