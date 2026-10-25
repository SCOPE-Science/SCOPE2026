# All-dimensional face enumerators and sharp staircase thresholds for partition-graph clique complexes

## Finding
Let \(G_n\) be the graph of integer partitions of \(n\ge1\), adjacent when one Ferrers cell is transferred between rows, and \(K_n=\operatorname{Cl}(G_n)\). Write \(c_r(n)\) for the number of \(r\)-vertex simplices (cliques) of \(K_n\), and let
\[
P(q)=\prod_{j\ge1}(1-q^j)^{-1},\qquad D_r(q)=\prod_{j=1}^{r}(1-q^j).
\]
The complete face enumerators, as formal power series in \(q\), are
\[
\boxed{\sum_{n\ge1}c_1(n)q^n=P(q)-1,\qquad
\sum_{n\ge1}c_2(n)q^n=\frac{q^2P(q)}{D_2(q)},}
\]
\[
\boxed{\sum_{n\ge1}c_r(n)q^n=
\frac{P(q)}{D_r(q)}
\left(q^{1+\binom r2}+q^{\binom{r+1}2-1}\right)
\quad(r\ge3).}
\]
In particular, for every simplex dimension \(d\ge0\), its first occurrence is at
\[
\boxed{\tau(d)=1+\frac{d(d+1)}2.}
\]
For \(d\ge2\), at that first occurrence there is exactly one \(d\)-simplex: its \(d+1\) vertices are the distinct one-cell extensions of the staircase partition \(\delta_d=(d,d-1,\ldots,1)\). Consequently the exact first-occurrence local layer consists of those same \(d+1\) partitions. Equivalently,
\[
\dim K_n=\max\left\{d\ge0:1+\frac{d(d+1)}2\le n\right\}.
\]
This proves the two staircase first-occurrence conjectures stated in the March 2026 simplex-stratification paper, while supplying the complete face-vector series previously sought in the March 2026 numerical paper.

## Assumptions and scope
Partitions are identified with left-justified, nonincreasing Ferrers diagrams. For \(\lambda\vdash n\), let \(d(\lambda)\) be its number of distinct positive part sizes, equal to the number of removable corners; it has \(d(\lambda)+1\) addable corners. An elementary transfer changes a diagram by removing one removable cell and inserting one addable cell, producing a different partition. A simplex is an unordered nonempty collection of pairwise adjacent partitions. A clique of cardinality \(r\) corresponds to dimension \(r-1\). All equalities are formal series with integer coefficients, valid without analytic convergence assumptions. The proof uses the published global star/top classification of partition-graph cliques, rather than claiming that classification as new.

## Proof
**1. Star/top uniqueness.** The published star/top theorem says every clique lies among the size-\(n\) Young-diagram successors of some \(\mu\vdash n-1\), or among the size-\(n\) predecessors of some \(\nu\vdash n+1\). These are called the lower-star and upper-top descriptions. A size-\(r\) star clique is a selection of \(r\) among the \(d(\mu)+1\) addable corners, so contributes \(\binom{d(\mu)+1}{r}\). A size-\(r\) top clique is a selection of \(r\) among the \(d(\nu)\) removable corners, contributing \(\binom{d(\nu)}r\).

For \(r\ge2\), a star's lower predecessor is the intersection of the clique's Ferrers diagrams, and therefore unique. A top's upper successor is the union of its Ferrers diagrams, likewise unique. For \(r\ge3\), a clique cannot have both descriptions: the union of \(r\) distinct one-cell extensions of a common predecessor has \(n-1+r\ge n+2\) cells, while a common upper successor would have only \(n+1\) cells. Thus every \(r\ge3\) clique is counted precisely once, in exactly one of the two families. An edge has both descriptions, but is counted exactly once by choosing only its unique lower predecessor. Hence
\[
 c_2(n)=\sum_{\mu\vdash n-1}\binom{d(\mu)+1}{2},\qquad
 c_r(n)=\sum_{\mu\vdash n-1}\binom{d(\mu)+1}{r}
       +\sum_{\nu\vdash n+1}\binom{d(\nu)}r\quad(r\ge3).
\]

**2. Corner-weighted partition series.** A positive part size \(j\) appears either zero times or at least once, so introducing an auxiliary variable \(u\) for the number of distinct sizes gives
\[
 F(q,u)=\sum_{\lambda}q^{|\lambda|}u^{d(\lambda)}
 =\prod_{j\ge1}\left(1+\frac{u q^j}{1-q^j}\right).
\]
Substituting \(u=1+x\) and simplifying factorwise yields
\[
 F(q,1+x)=P(q)\prod_{j\ge1}(1+xq^j).
\]
By the distinct-part generating identity,
\[
 E_r(q):=[x^r]\prod_{j\ge1}(1+xq^j)
 =\frac{q^{\binom{r+1}{2}}}{D_r(q)},\qquad E_0(q)=1.
\]
Therefore \(\sum_\lambda\binom{d(\lambda)}r q^{|\lambda|}=P(q)E_r(q)\). The elementary identity \(\binom{d+1}r=\binom dr+\binom d{r-1}\) and cancellation give
\[
 E_r(q)+E_{r-1}(q)=\frac{q^{\binom r2}}{D_r(q)}
 \quad(r\ge1).
\]
The lower-star series, with its shift by one in \(n\), is therefore \(qP(q)(E_r+E_{r-1})\); the upper-top series is \(q^{-1}P(q)E_r\). Applying the uniqueness from step 1 yields the displayed two-term formula for \(r\ge3\), and the lower-star term alone gives the \(r=2\) formula. For vertices \(c_1(n)=p(n)\), so the series is \(P(q)-1\).

**3. Sharp first-occurrence thresholds and their actual vertices.** For \(r\ge3\), \(P(q)/D_r(q)\) has constant term one and no negative powers. The lower-star summand begins at \(1+\binom r2\) with coefficient one; the upper-top summand begins strictly later, at \(\binom{r+1}2-1\), a difference of \(r-2>0\). Thus an \(r\)-clique first appears at \(n=1+\binom r2\), and exactly one such clique occurs then. The \(r=2\) formula gives its unique first edge at \(n=2\); \(r=1\) starts at \(n=1\). At the onset \(n=1+\binom r2\), the lower predecessor must have \(r-1\) distinct positive part sizes and minimal weight \(1+2+\cdots+(r-1)=\binom r2\). It is uniquely the staircase \(\delta_{r-1}\). Its \(r\) distinct one-cell extensions are precisely the first \(r\)-clique. Since there is no clique with more than \(r\) vertices at that \(n\), the exact top local layer is exactly these \(r\) vertices. Taking \(r=d+1\) yields both first-occurrence assertions and the dimension formula.

## Verification
The bundled standalone `verify_partition.py` computes integer partition series and exact clique counts with integer arithmetic; independently constructs complete transfer graphs and enumerates all cliques for \(1\le n\le16\) (a total of \(8{,}932\) faces); checks \(153\) corner-count identities for \(2\le n\le18\); compares clique tables for \(n=26,27,29,30\) and known Betti tables for \(1\le n\le25\) against published values; tests initial threshold values through \(r=10\); and tests a derived Euler-characteristic identity through coefficient \(65\). The latter Betti identity is a consistency check, not a novelty claim. Reproduce with `python3 verify_partition.py`; its captured output is `verification_output.txt` and finishes with `VERIFY_OK`. Exact finite checks do not replace steps 1–3 proving the all-parameter statements.

## Relationship to prior work
Lyudogovskiy's arXiv:2603.14370 (March 15, 2026) proves the star/top clique classification and wedge-of-two-spheres homotopy theorem used here. His arXiv:2603.23228 (March 24, 2026), Conjectures 5.1 and 5.2, explicitly proposes the triangular first-layer thresholds and staircase first-occurrence families; the proof above establishes both in all dimensions. His arXiv:2603.26656 (March 27, 2026) gives extensive exact tabulated clique counts but explicitly does not claim a closed family of clique-count formulas; the formula above fills this specified gap. Other available research already gives a positive partition statistic and Euler-product generating function for the sphere multiplicities \(b_n\). No novelty for those homotopy ranks, their generating function, or the underlying star/top theorem is claimed here. The new assertion is the **full face-enumerator series, jointly with the verified sharp staircase onset and uniqueness**.

## Limitations
This is an exact enumeration of all simplex dimensions, not an enumeration of maximal simplices, all local layer sizes, graph phase-boundary sizes, or attaching maps. The argument depends on the published star/top theorem and the standard distinct-parts generating identity; those are not reproved here. Bibliographic searches and primary-text inspections cannot rule out every uncatalogued simultaneous discovery. The reported review is self-review only; no independent scientific audit is claimed.

## References
1. F. B. Lyudogovskiy, *The homotopy type of the clique complex of the partition graph*, arXiv:2603.14370 (first public March 15, 2026), Section 3, especially Theorem 3.6. https://arxiv.org/html/2603.14370v1
2. F. B. Lyudogovskiy, *Simplex Stratification and Phase Boundaries in the Partition Graph*, arXiv:2603.23228 (first public March 24, 2026), Sections 3 and 5, Conjectures 5.1–5.2. https://arxiv.org/html/2603.23228v1
3. F. B. Lyudogovskiy, *Numerical topology of the clique complex of the partition graph: Euler characteristic, clique counts, and sequence data*, arXiv:2603.26656 (first public March 27, 2026). https://arxiv.org/html/2603.26656v1
4. F. B. Lyudogovskiy, *Local Morphology of the Partition Graph*, arXiv:2603.18696 (first public March 19, 2026). https://arxiv.org/abs/2603.18696
5. F. B. Lyudogovskiy, *Local Complexity, Overlap Control, and Global Simplicity in Partition Graphs*, arXiv:2606.20773 (first public June 18, 2026). https://arxiv.org/abs/2606.20773
