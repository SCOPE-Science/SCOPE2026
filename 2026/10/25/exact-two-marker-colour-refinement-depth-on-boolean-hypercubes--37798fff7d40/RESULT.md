# Exact two-marker colour-refinement depth on Boolean hypercubes

## Finding

Let \(d\ge 1\), let \(Q_d\) be the graph on \(\{0,1\}^d\) with an edge between words that differ in exactly one coordinate, and let \(a\ne b\) be an ordered pair of marked vertices. Set \(t=d_H(a,b)\), so \(1\le t\le d\). Initially give \(a\) and \(b\) distinct singleton colours, and give every other vertex a third colour. Apply synchronous one-dimensional counting colour refinement, retaining the old colour at each update. Write \(\equiv_r\) for equality of colours after exactly \(r\ge0\) updates.

**Round-by-round normal form.** For every \(r\ge0\) and vertices \(x,y\),
\[
 x\equiv_r y\quad\Longleftrightarrow\quad
 \bigl(\min\{d_H(x,a),r+1\},\min\{d_H(x,b),r+1\}\bigr)
 =\bigl(\min\{d_H(y,a),r+1\},\min\{d_H(y,b),r+1\}\bigr).
\]

**Sharp first stable round.** The least \(r\ge0\) for which the partition no longer changes is
\[
 \rho(d,t)=
 \begin{cases}
 d-1,&t=1,\\
 d-2,&2\le t<d,\\
 \lfloor(d-1)/2\rfloor,&t=d.
 \end{cases}
\]
The cases apply only when their displayed parameter ranges are nonempty. In particular, two adjacent marked vertices do not improve the one-marker depth, intermediate separations reduce it by exactly one round, and antipodal markers nearly halve it.

**Stable orbit census.** The stable classes are exactly the orbits of the pointwise stabilizer of the ordered pair \((a,b)\) in \(\operatorname{Aut}(Q_d)\). There are precisely
\[
 (t+1)(d-t+1)
\]
classes. Index them by integers \(0\le i\le t\), \(0\le j\le d-t\); the corresponding class contains
\[
 \binom{t}{i}\binom{d-t}{j}
\]
vertices. Equivalently, a feasible *full* pair of distances \((p,q)\) determines \(i=(p-q+t)/2\) and \(j=(p+q-t)/2\).

## Assumptions and scope

Here \(Q_d\) is the simple, undirected, loopless binary Hamming graph; no colours are attached to coordinate positions. The two marked vertices receive *different* colours at round zero, and the remaining vertices (if any) share a third colour. The update key is the ordered pair consisting of the old colour and the multiset of neighbour colours. A round is counted only when such an update is applied, so a partition already stable at initialization has depth zero. Nothing is claimed about isomorphism testing outside this marked hypercube family, or higher-dimensional Weisfeiler--Leman refinement.

By translating and permuting binary coordinates we may assume \(a=0^d\), \(b=1^t0^{d-t}\). Put \(u=d-t\). A vertex \(x\) has \(i\) ones among the first \(t\) coordinates and \(j\) ones among the last \(u\) coordinates. Its two distances are
\[
 p=i+j,\qquad q=t-i+j.
\]
The admissible \((i,j)\) form the rectangular integer grid \([0,t]\times[0,u]\).

## Proof

**1. Initial colours and inductive propagation.** For an integer \(R\ge1\), define the truncated-distance signature \(F_R(x)=(\min\{p,R\},\min\{q,R\})\). The three initial colours coincide exactly with the \(F_1\)-classes: the two marked points have respective signatures \((0,1)\) and \((1,0)\), and all other points have \((1,1)\).

Suppose the current colour classes are the \(F_R\)-classes. We show one update produces exactly the \(F_{R+1}\)-classes.

To prove that an update distinguishes every newly different truncated signature, retain the previous colour. If two vertices previously had the same signature but differ in the first coordinate of \(F_{R+1}\), one has \(p=R\) and the other has \(p\ge R+1\). A vertex at distance \(p=R\) from \(a\) has exactly \(R\) neighbours at distance \(R-1\) from \(a\), whereas a vertex at distance at least \(R+1\) has none. Since \(R-1<R\), the union of the preceding colour classes with truncated first coordinate \(R-1\) is recognisable. Their neighbour counts therefore differ. The same argument applies to the second coordinate and \(b\). Thus the new partition refines the \(F_{R+1}\)-partition.

Conversely, suppose \(F_{R+1}(x)=F_{R+1}(y)\). If both true distances \(p,q\) are at most \(R\), they are individually known. The numbers of neighbour transitions of the full distance-pair depend only on \(p,q,t,d\), because \(i=(p-q+t)/2\), \(j=(p+q-t)/2\), and the four transition types, with multiplicities, are
\[
 (i,j)\to(i-1,j):i,\quad(i+1,j):t-i,\quad
 (i,j-1):j,\quad(i,j+1):u-j.
\]
Therefore the previous-colour neighbour multisets agree. If \(p\le R\) but \(q\ge R+1\), every neighbour has second truncated distance \(R\), while the numbers of neighbours with first distances \(p-1\) and \(p+1\) are respectively \(p\) and \(d-p\), independent of \(q\). Thus the previous-colour neighbour multisets again agree. The case \(q\le R<p\) is symmetric. If both distances are at least \(R+1\), every neighbour has preceding signature \((R,R)\). Hence no \(F_{R+1}\)-class is split by the update. Induction proves the round-by-round formula for all \(r\).

**2. Full-distance orbits.** The automorphisms fixing \(a,b\) may permute the \(t\) coordinates on which the markers differ and independently permute the remaining \(u\) coordinates. Conversely, the distances \((p,q)\) recover \((i,j)\) via the displayed inverse formulas. This proves both the orbit claim and its count and binomial class sizes. The \(F_R\)-partition is stable exactly when its truncation is injective on this \((t+1)(u+1)\)-element orbit grid; after that point it agrees with the orbit partition, which is equitable and therefore cannot split further.

**3. Exact saturation thresholds.** When \(t=1\), the two words with \((i,j)=(0,d-1)\) and \((1,d-1)\) have distance pairs \((d-1,d)\) and \((d,d-1)\); these collide under \(F_{d-1}\), while \(F_d\) retains all distances. Hence \(\rho=d-1\) (including the evident \(d=1\) boundary).

Suppose \(2\le t<d\), so \(u\ge1\). The grid points \((t,u)\) and \((t-1,u-1)\) have distance pairs \((d,u)\) and \((d-2,u)\), and therefore collide under \(F_{d-2}\). On the other hand, \(F_{d-1}\) is injective. Indeed, the only vertex at distance \(d\) from \(a\) has full distance pair \((d,u)\), and the two vertices at distance \(d-1\) from \(a\) in orbit coordinates have second distances \(u-1\) and \(u+1\), never \(u\). The analogous statement holds with the markers exchanged. Every other full distance pair has both entries at most \(d-1\), so cannot produce a new collision on truncating at \(d-1\). Therefore \(\rho=d-2\).

Finally, if \(t=d\), then \(u=0\) and the feasible full pairs are exactly \((i,d-i)\) for \(0\le i\le d\). Their truncations are distinct once \(R=\lceil d/2\rceil\), since at most one pair can have both entries at least \(R\). At \(R=\lceil d/2\rceil-1\), two consecutive central pairs have both coordinates at least \(R\) and collide (with the \(d=1,2\) initial-round boundaries immediate). Therefore \(\rho=\lceil d/2\rceil-1=\lfloor(d-1)/2\rfloor\). This exhausts all cases.

## Verification

The supplementary standard-library Python program `check.py` implements ordinary refinement directly on all vertices for each \(1\le d\le9\) and \(1\le t\le d\). It verifies every intermediate truncated-distance partition, the first stable round, the final orbit count, and all class sizes. Separately, it builds the four-transition weighted quotient directly from binary-coordinate flips and repeats the refinement for every \(1\le d\le40\), \(1\le t\le d\). The recorded run checks 45 full-graph and 820 quotient instances and terminates with `ALL_PASS`. Execute `python check.py` with a recent Python 3 interpreter; no additional packages or input files are required. These finite checks corroborate but do not prove the unrestricted statements.

## Relationship to prior work

The basic colour-refinement algorithm, equitable-partition interpretation, and uses in graph isomorphism and symmetry reduction are established; see Grohe--Kersting--Mladenov--Selman [1] and Kersting--Mladenov--Garnett--Grohe [2]. Structural research on equitable Hamming-graph partitions, including perfect two-colourings, also predates this statement [3]. Those works study general algorithmic or partition properties rather than an exact two-distinguished-vertex, round-by-round refinement profile of the binary cube.

Previously established one-root analyses of Cartesian products of complete graphs determine a one-root refinement depth, and separate multi-marker results address ternary and quaternary Hamming graphs. The present theorem is not a claim of a new graph family or a new refinement algorithm: its distinguishing content is the exact two-root truncation law and its sharp separation-dependent stabilization thresholds in the binary case.

## Limitations

The result requires two *distinctly coloured* marked points. Identically coloured marker points, larger marker sets, nonbinary Hamming graphs, and other message-passing models need not obey the displayed law. The exact first stable round is measured for the synchronous partition sequence, not running time in bit operations. A literature comparison cannot establish global uniqueness: the result may be implicit in previously studied pair-distance equitable partitions or literature not indexed in the searches.

## References

[1] M. Grohe, K. Kersting, M. Mladenov, E. Selman, *Dimension Reduction via Colour Refinement*, arXiv:1307.5697, first version 22 July 2013, https://arxiv.org/abs/1307.5697 .

[2] K. Kersting, M. Mladenov, R. Garnett, M. Grohe, *Power Iterated Color Refinement*, AAAI 2014, published 21 June 2014, DOI:10.1609/aaai.v28i1.8992 .

[3] E. A. Bespalov, D. S. Krotov, A. A. Matiushev, A. A. Taranenko, K. V. Vorob'ev, *Perfect 2-colorings of Hamming graphs*, arXiv:1911.13151, first version 29 November 2019, https://arxiv.org/abs/1911.13151 .
