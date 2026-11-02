# Five symbol-pair spectra of coordinate-ordered extended Hamming codes

## Finding

Fix eight cyclically indexed coordinate positions. Across all coordinate permutations of the binary extended Hamming code of parameters \([8,4,4]_2\), there are exactly **30 distinct labeled codebooks** and precisely **five** symbol-pair weight enumerators. Exactly **ten** of these thirty have symbol-pair minimum distance \(6\), meeting the symbol-pair Singleton bound \(d_2\le 8-4+2=6\); the other twenty have minimum pair distance \(5\). All thirty share the ordinary Hamming weight enumerator \(1+14z^4+z^8\).

For an arbitrary bijection \(v:\mathbb Z_8\to\mathbb F_2^3\), set
\[
C_v=\{(a\cdot v_i+b)_{i\in\mathbb Z_8}:a\in\mathbb F_2^3,\ b\in\mathbb F_2\}.
\]
Let \(T\) count those four blocks \(\{v_i,v_{i+1},v_{i+2},v_{i+3}\}\), for \(0\le i\le3\), which are affine planes, and let \(Z=1\) if the four even-indexed points \(\{v_0,v_2,v_4,v_6\}\) form an affine plane and \(Z=0\) otherwise. Here an affine plane is a four-element coset of a two-dimensional subspace of \(\mathbb F_2^3\). For every such ordering,
\[
W_{C_v}(z)=1+2Tz^5+(10-4T+2Z)z^6+(4+2T-4Z)z^7+(1+2Z)z^8.
\]
The complete classification is:

| \(T\) | \(Z\) | Distinct labeled codes | \(W_{C_v}(z)\) |
|---:|---:|---:|---|
| 0 | 0 | 10 | \(1+10z^6+4z^7+z^8\) |
| 1 | 0 | 12 | \(1+2z^5+6z^6+6z^7+z^8\) |
| 1 | 1 | 4 | \(1+2z^5+8z^6+2z^7+3z^8\) |
| 2 | 0 | 2 | \(1+4z^5+2z^6+8z^7+z^8\) |
| 2 | 1 | 2 | \(1+4z^5+4z^6+4z^7+3z^8\) |

## Assumptions and scope

The coordinate ordering is indexed, cyclic and oriented, with pairs \((c_i,c_{i+1})\), indices modulo eight. Different labeled codebooks means different subsets of \(\mathbb F_2^8\); orderings related by an affine automorphism of the eight point labels give the same codebook. No quotient by cyclic rotation, coordinate reflection or arbitrary pair-metric isometry is taken. The binary symbol-pair weight is
\[
\operatorname{wt}_2(c)=\#\{i\in\mathbb Z_8:(c_i,c_{i+1})\ne(0,0)\},
\]
and \(W_{C_v}(z)=\sum_{c\in C_v}z^{\operatorname{wt}_2(c)}\). The invariant \(Z\) is tied to even/odd coordinate parity, not to the zero vector among the affine points.

## Proof

**1. Affine support geometry.** The sixteen affine Boolean maps \(x\mapsto a\cdot x+b\) give distinct codewords: the zero word, the all-one word, and fourteen words of Hamming weight four. Their supports are exactly the fourteen affine planes in \(\mathbb F_2^3\), namely the four-subsets \(B\) with \(\bigoplus_{x\in B}x=0\). Every pair of distinct affine points lies in precisely three of these planes: the span direction between them can be completed with one of three remaining two-dimensional directions.

**2. Weight enumerator from two incidence statistics.** For a nonempty proper four-element support \(B\subset\mathbb Z_8\), let \(r(B)\) be its number of cyclic runs. A pair position is nonzero exactly when at least one endpoint lies in \(B\), whence \(\operatorname{wt}_2(B)=4+r(B)\), with \(1\le r(B)\le4\). A four-element support has one run exactly when it consists of four consecutive positions. These eight windows form four complementary pairs, so exactly \(2T\) of the fourteen plane supports have pair weight five. A four-element support has four runs exactly when it is one of the two alternating parity classes, so exactly \(2Z\) plane supports have pair weight eight.

Each of the eight cyclic coordinate edges lies inside exactly three affine-plane supports, yielding \(24\) total internal-edge incidences. Each plane support with \(r\) runs contains \(4-r\) internal edges. Writing \(A_j\) for the number of weight-four supports with symbol-pair weight \(j\), the equations
\[
A_5+A_6+A_7+A_8=14,\quad A_5=2T,\quad A_8=2Z,\quad
3A_5+2A_6+A_7=24
\]
give \(A_6=10-4T+2Z\) and \(A_7=4+2T-4Z\). The all-one word contributes one additional term \(z^8\), and zero contributes one, proving the displayed formula.

**3. Count the codebooks and the unconditional \(T\)-distribution.** The coordinate permutation stabilizer of the code is the affine group \(\operatorname{AGL}(3,2)\) of order \(8\cdot168=1344\). Indeed affine maps preserve the fourteen zero-XOR four-subsets. Conversely, a permutation preserving them, after translation to fix zero, preserves the unique fourth point \(x+y\) completing each plane \(\{0,x,y,x+y\}\), and so is linear. The number of distinct codebooks is therefore \(8!/1344=30\).

Uniformly permute the eight affine points. Let \(E_i\), for \(i=0,1,2,3\), be the event that positions \(i,i+1,i+2,i+3\) form a plane; \(T=\sum_i\mathbf1_{E_i}\). Each event has probability \(14/\binom84=1/5\). Events with adjacent indices modulo four are mutually exclusive: if \(E_0\) and \(E_1\) both held, distinct affine planes would share three points; if \(E_0\) and \(E_3\) both held, the complement of the second plane would share three points with the first. The other cases follow by cyclic symmetry. Thus \(T\le2\), and only pairs \((E_0,E_2)\) and \((E_1,E_3)\) can coexist.

Condition on \(E_0\). The two selected points at positions two and three belong to one affine plane, while positions four and five are a uniformly random unordered pair of points from its parallel complement. For their union to be an affine plane, the two pairs must have the same nonzero vector difference. Of the six pairs in the complementary affine plane, precisely two have that prescribed difference. Consequently \(\Pr(E_2\mid E_0)=1/3\). Therefore \(\Pr(T=2)=2/15\), while \(\mathbb E[T]=4/5\) yields \(\Pr(T=1)=8/15\) and \(\Pr(T=0)=1/3\). Across thirty codebooks this gives totals \(4,16,10\) for \(T=2,1,0\) respectively.

**4. Joint distribution with the alternating statistic.** The alternating four-set is a plane with probability \(1/5\), so precisely six of the thirty codebooks have \(Z=1\). Conditional on this event, the four even-indexed and the four odd-indexed points independently enumerate two parallel affine planes. Identify their common two-dimensional difference space with \(\mathbb F_2^2\). Traversing each four-point plane in its cyclic parity order gives two distinct nonzero edge directions, chosen uniformly among the three possible two-element subsets of \(\mathbb F_2^2\setminus\{0\}\). Independence holds because the two plane orders are independent after fixing their unordered point sets.

A four-consecutive-coordinate window is a plane if and only if its consecutive even-position pair and its consecutive odd-position pair have the same vector difference. For the four tested windows, the four comparisons cover all four combinations of the two even directions and two odd directions; hence \(T\) equals the cardinality of the intersection of the two chosen two-element direction sets. They always intersect, and intersect twice exactly when their omitted directions match, an event of conditional probability \(1/3\). Hence among the six codes with \(Z=1\), exactly two have \(T=2\) and four have \(T=1\). Subtracting from the unconditional totals gives all five rows of the table, with no other cases.

**5. Optimality.** The displayed enumerators have minimum nonzero pair weight \(6\) precisely when \(T=0\), otherwise \(5\). Since the code has sixteen words, the symbol-pair Singleton bound \(|C|\le2^{n-d_2+2}\) yields \(d_2\le6\). Thus exactly ten labeled codebooks are pair-MDS.

## Verification

The standalone standard-library program `verify.py` enumerates the \(7!=5040\) point orders having first point zero; this loses no distinct codebooks because translations of \(\mathbb F_2^3\) preserve the code. For each order it reconstructs the code independently by zero-XOR affine planes and by affine Boolean functions, checks agreement, records the symbol-pair enumerator and both invariants, and groups orders into distinct codebooks. It finds exactly thirty codebooks, each occurring \(168\) times among the normalized orders; all five rows match the theorem. Run `python3 verify.py`; the last line must be `VERIFY_OK`. The enumerator and multiplicities are established by the combinatorial argument above; the computation is a finite independent check, not a substitute for that proof.

## Relationship to prior work

Cassuto and Blaum introduced symbol-pair read channels and the pair metric. Chee and collaborators proved the symbol-pair Singleton bound and explicitly constructed a binary linear MDS code of length eight and pair-distance six; neither the existence of such parameters nor the Singleton inequality is new here. Hao Chen analyzed the pair-weight and covering behavior of a particular binary extended Hamming code of length eight in Example 4, without classifying all thirty labeled coordinate presentations. Saniga listed thirty labeled Fano planes and classified them using a different line-incidence invariant; that source provides underlying incidence data, not the five symbol-pair enumerators, their distribution or the interleaving criterion. The claimed contribution is the **joint structural enumerator and exact thirty-codebook spectrum for all coordinate orderings**, not the underlying code, incidence system, pair metric or MDS existence.

## Limitations

Only the length-eight binary extended Hamming code is classified, and the answer depends on the specified cyclic coordinate order. Nothing is claimed for other lengths, other alphabet sizes, arbitrary binary linear codes, list decoding, covering radius, practical storage performance or global optimization outside this fixed permutation class. Existing Fano-plane tables could in principle be postprocessed into the classification; historical priority of the exact new joint table has not been independently certified.

## References

- Y. Cassuto and M. Blaum, *Codes for Symbol-Pair Read Channels*, IEEE Transactions on Information Theory 57 (2011). DOI: https://doi.org/10.1109/TIT.2011.2164891.
- Y. M. Chee et al., *Maximum Distance Separable Codes for Symbol-Pair Read Channels*, arXiv:1211.1728, first posted November 7, 2012; especially Theorem 2.1 and Proposition 4.4, Table I. https://arxiv.org/html/1211.1728v2.
- M. Saniga, *Combinatorial Intricacies of Labeled Fano Planes*, arXiv:1509.06009, first posted September 20, 2015. https://arxiv.org/html/1509.06009v1.
- H. Chen, *Covering b-Symbol Metric Codes and the Generalized Singleton Bound*, arXiv:2206.12668, first posted June 25, 2022; especially Example 4. https://arxiv.org/html/2206.12668v3.
