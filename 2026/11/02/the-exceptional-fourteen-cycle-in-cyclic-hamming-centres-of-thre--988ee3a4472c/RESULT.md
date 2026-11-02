# The exceptional fourteen-cycle in cyclic-Hamming centres of three-one necklaces

## Finding

**Theorem (exact one-centre phase diagram).** For each integer \(n\ge 3\), let \(\mathcal N_{n,3}\) be the set of cyclic-rotation orbits of binary words of length \(n\) with exactly three ones. For two orbits, set
\[
d([u],[v])=\min_{s\in\mathbb Z_n}d_H(u,\operatorname{rot}_s(v)),
\qquad
R_n=\min_{[u]\in\mathcal N_{n,3}}\ \max_{[v]\in\mathcal N_{n,3}}d([u],[v]).
\]
Then the exact optimal radius for **every** \(n\ge3\) is
\[
R_n=\begin{cases}
0,&n\in\{3,4\},\\
2,&5\le n\le12\ \text{or}\ n=14,\\
4,&n=13\ \text{or}\ n\ge15.
\end{cases}
\]
At \(n=14\) the complete set of optimal centre orbits comprises exactly two, represented by the three-one support sets \(\{0,2,6\}\) and \(\{0,2,10\}\) in \(\mathbb Z_{14}\). These representatives are reversals but **not rotations** of each other. For \(n=13\) and all \(n\ge15\), every orbit is an optimal centre. The number of orbits, hence the number of optimal centres in those cases, is
\[
N(n)=\frac{1}{n}\left[\binom n3+\frac{2n}{3}\mathbf1_{3\mid n}\right]
=\frac{(n-1)(n-2)}6+\frac23\mathbf1_{3\mid n}.
\]
For completeness the numbers of optimal centres, in ascending order \(n=3,4,\ldots,14\), are
\[
1,\ 1,\ 2,\ 4,\ 5,\ 7,\ 6,\ 10,\ 10,\ 2,\ 22,\ 2.
\]
These finite multiplicities are certified by the exhaustive standalone verifier; the all-length radius theorem and the exact two-centre classification at fourteen have the proofs below.

## Assumptions and scope

Positions are indexed by \(\mathbb Z_n\). A word of weight three is identified with the unordered three-subset \(T\subset\mathbb Z_n\) of its one-positions. Only translations \(T\mapsto T+s\) define the necklace equivalence; reflection, bit complementation, and arbitrary coordinate permutations are **not** allowed equivalences. Both candidate centres and adversarial inputs belong to the **same fixed-weight-three layer**. The distance is ordinary binary Hamming distance minimized over translations (not the subword-multiset overlap distance used in some other necklace-centre literature). All maxima and minima are over finite nonempty sets, and the theorem ranges over every integer \(n\ge3\).

Write the undirected cyclic separation profile as
\[
D_n(T)=\left\{\min((a-b)\bmod n,(b-a)\bmod n):\{a,b\}\subset T\right\}\subseteq\{1,\ldots,\lfloor n/2\rfloor\}.
\]
It has at most three entries, possibly fewer. For \(n\ge5\), distinct necklace classes have distance \(2\) if their separation profiles intersect, and \(4\) otherwise. The distance is zero exactly for the same class.

## Proof

**1. Three possible distance levels.** Any two three-sets can be translated to share one point; their symmetric-difference size is at most four. A shared translated pair exists precisely when one of their unordered cyclic pair separations agrees: translate one member of the pair, choosing the order or its reverse. Such an alignment gives Hamming distance at most two, and for distinct classes the distance cannot be zero. If no pair can be shared then every shift intersects in at most one point, so the minimum Hamming distance is four. This proves the separation-profile criterion, with the zero case handled separately. For \(n=3,4\) the three-sets form one orbit, hence radius zero.

**2. Explicit centres through length twelve.** In every three-set of an \(n\)-cycle, one of the three positive consecutive cyclic gaps is at most \(\lfloor n/3\rfloor\). For \(5\le n\le8\) this is at most two, so its profile meets \(D_n(\{0,1,2\})=\{1,2\}\). For \(9\le n\le11\) it is at most three, so its profile meets \(D_n(\{0,1,3\})=\{1,2,3\}\). At \(n=12\), every three-set includes two vertices of the same parity; their cyclic separation is one of \(\{2,4,6\}=D_{12}(\{0,2,6\})\). These give radius at most two. In every \(n\ge5\) there are at least two necklace classes, so the radius cannot be zero; hence all these radii equal two.

**3. The exceptional fourteen-cycle (existence).** For \(n=14\), every three-set similarly contains two vertices of the same parity, hence one cyclic separation in \(\{2,4,6\}=D_{14}(\{0,2,6\})\). Thus there is a centre of radius two.

**4. The prime thirteen-cycle (impossibility).** Fix any candidate three-set \(T\subset\mathbb Z_{13}\). Let \(A\) be the subset of nonzero residues whose undirected separation is absent from \(D_{13}(T)\). There are six distinct nonzero undirected separation classes and at most three are forbidden, so \(|A|\ge6\); moreover \(A=-A\). A triangle in the graph on \(\mathbb Z_{13}\) whose edges have differences in \(A\) produces a three-set \(U\) whose profile is disjoint from \(D_{13}(T)\), forcing distance four. Supposing there is no triangle gives \((A+A)\cap A=\varnothing\): for \(x,y,x+y\in A\), the vertices \(0,x,x+y\) would form a triangle, and the nonzero/symmetric conditions ensure distinct vertices. Cauchy–Davenport for the prime group \(\mathbb Z_{13}\) gives \(|A+A|\ge\min(13,2|A|-1)\ge11\), which cannot be disjoint from a set \(A\) of size at least six. Thus every centre has a distance-four adversary and \(R_{13}=4\).

**5. All lengths at least fifteen (impossibility).** For arbitrary \(n\ge15\), form the graph \(G_T\) on the \(n\) positions, connecting two vertices exactly when their undirected cyclic separation is **not** in \(D_n(T)\). Every separation class contributes at most \(n\) undirected edges; thus \(G_T\) has at least
\[
\binom n2-3n=\frac{n(n-7)}2>\frac{n^2}{4}\quad(n\ge15)
\]
edges. By Mantel's theorem, this graph contains a triangle. Its vertices are a three-set \(U\) with \(D_n(T)\cap D_n(U)=\varnothing\), hence at distance four. Since four is already a universal upper bound, all centres have radius four and \(R_n=4\) for every \(n\ge15\).

**6. Uniqueness of the two fourteen-cycle centres.** For \(n=14\), the graph \(G_T\) has at least \(\binom{14}{2}-3\cdot14=49=14^2/4\) edges. If \(T\) has radius two, then \(G_T\) has no triangle. Equality in Mantel's theorem forces \(G_T\cong K_{7,7}\), with its two colour classes uniquely determined. Translation by one is an automorphism of the circulant graph and must permute these classes. It cannot preserve both classes, since its action is transitive on all fourteen vertices; hence translation by one swaps the classes. The classes therefore are the even and odd residues. Consequently the missing edges, namely the forbidden separations \(D_{14}(T)\), must comprise **all** even differences and none of the odd differences, so exactly \(D_{14}(T)=\{2,4,6\}\). Thus all three vertices of \(T\) share parity. Dividing by two identifies a three-set in \(\mathbb Z_7\) whose three undirected separations are exactly \(\{1,2,3\}\). The three positive cyclic gaps between consecutive points must, up to cyclic order, be \((1,2,4)\), because each gap's undirected residue is a distinct value \(1,2,3\) and their sum is seven; direct inspection of the possibilities \(1,2,3,4,5,6\) gives this unique unordered gap multiset. There are two cyclic orders of \((1,2,4)\) up to cyclic permutation, namely \((1,2,4)\) and \((1,4,2)\). Under doubling, they give precisely the two supports stated in the theorem. Both have the parity property of Step 3, so they are exactly all optimal centres.

**7. Counting every centre in the radius-four regimes.** Burnside's lemma for the translation action on \(\binom{\mathbb Z_n}{3}\) gives \(\binom n3/n\) from the identity. A nonidentity rotation can fix a three-set only when it has order three; this requires \(3\mid n\) and the two order-three rotations each fix exactly \(n/3\) triples. This proves the stated expression for \(N(n)\). It applies as the optimal-centre count at \(n=13\) and at every \(n\ge15\).

## Verification

Run `python3 verify.py` with Python 3.9+ and no third-party modules. It prints `VERIFY_OK` after exhaustive canonical-rotation necklace enumeration through length 26 and direct rotation-Hamming cross-checks through length 17. The exact centre multiplicities for lengths 3–14 and both optimal supports at lengths 12 and 14 are checked. The script also checks the arithmetic thresholds used for lengths 13 and at least 15. These finite tests are supplementary; the Cauchy–Davenport, Mantel, and explicit-centre proofs establish the all-length theorem independently of any finite cutoff.

## Relationship to prior work

Adamson–Deligkas–Gusev–Potapov (2020, arXiv:2005.10095) and its 2023 conference treatment study the necklace \(k\)-centre framework with **subword-overlap distance** and approximation algorithms, not fixed-weight-three one-centres under minimum-rotation Hamming distance. Their distance does not imply the values above. Adamson and coauthors (arXiv:2108.01990, especially sections 4.2 and 8.1–8.2) supply general fixed-content necklace counting and the overlap-distance setting; applying the counting formula gives only \(N(n)\), not the min–max radius or the exceptional optimal-centre classification. The result here uses the precise Hamming quotient metric and ties the exact radius threshold to triangle-free circulant graphs. Primary-source comparisons and residual originality risk are detailed in the accompanying review.

## Limitations

No claim is made for weights other than exactly three, centre sets larger than one, edit distance, overlap distance, or centres drawn from unrestricted binary words. The small exceptional centre-count sequence has a finite exact enumeration certificate, not an independent symbolic closed form; the infinite all-length radius claim has a separate analytic proof. Equivalent specialized results may exist outside the checked literature and database, so originality remains a best-knowledge assessment rather than a priority guarantee. Independent scientific review has not been performed.

## References

1. D. Adamson, A. Deligkas, V. V. Gusev, I. Potapov, *The K-Centre Problem for Necklaces*, arXiv:2005.10095, first posted 2020-05-20. https://arxiv.org/abs/2005.10095
2. D. Adamson et al., *Combinatorial Algorithms for Multidimensional Necklaces*, arXiv:2108.01990, 2021, sections 4.2, 8.1–8.2. https://arxiv.org/html/2108.01990v2
3. D. Adamson, A. Deligkas, V. V. Gusev, I. Potapov, *The k-centre Problem for Classes of Cyclic Words*, 2023, DOI:10.1007/978-3-031-23101-8_26. Open-access full text: https://pure.royalholloway.ac.uk/ws/files/47364733/The_k_Centre_Problem_for_Classes_of_Cyclic_Words.pdf
4. A.-L. Cauchy and H. Davenport, the classical Cauchy–Davenport sumset inequality on groups of prime order.
5. W. Mantel, the classical maximum-edge theorem for triangle-free simple graphs (1907).
