# The optimal four-multiset deletion codes as graph pairings over quadruple packings

## Finding
Let \(V\) be a labeled alphabet of cardinality \(q\ge2\). A word is a multiplicity vector \(x\in\mathbb Z_{\ge0}^{V}\) satisfying \(\sum_{i\in V}x_i=4\), and deleting one symbol produces \(x-e_i\) for any \(i\) with \(x_i>0\). The code corrects one unordered deletion when deletion-output sets of distinct codewords are disjoint. Write \(D(q,4,3)\) for the largest family of four-subsets of \(V\) in which no triple occurs in two blocks, taking \(D(q,4,3)=0\) when \(q<4\).

**Complete optimizer parameterization.** Every maximum one-deletion code, and no other code, is obtained uniquely from the following data:

1. A maximum \(3\)-\((q,4,1)\) packing \(\mathcal B\) of \(D(q,4,3)\) four-subsets of \(V\).
2. A simple graph \(H\) on \(V\), all of whose vertex degrees are even (isolated vertices are allowed).
3. For each vertex \(i\), a partition \(\pi_i\) of its neighbor set \(N_H(i)\) into unordered pairs \(\{j,k\}\). Every triple \(\{i,j,k\}\) assigned this way must be **uncovered** by \(\mathcal B\), and no such triple may be assigned more than once globally.

The corresponding code is exactly
\[
\begin{split}
C(\mathcal B,H,\pi)={}&\{4e_i:i\in V\}\\
&\cup\{2e_i+2e_j:\{i,j\}\notin E(H),\ i\ne j\}\\
&\cup\{2e_i+e_j+e_k:\{j,k\}\in\pi_i\}\\
&\cup\left\{\sum_{i\in B}e_i:B\in\mathcal B\right\}.
\end{split}
\]
In the second set each unordered pair \(\{i,j\}\) is used once. Every such code has the **previously established** optimal size
\[
|C|=q+\binom q2+D(q,4,3).
\]
The finding is the full necessary-and-sufficient description of **all** optimizers, not this previously established numerical identity.

**Steiner rigidity.** If \(q\ge4\) and \(q\equiv2,4\pmod6\), or if \(q\ge3\) and \(q\equiv1,3\pmod6\), then every optimal code has \(H=\varnothing\). In these four congruence classes, its sole freedom is the maximum quadruple packing \(\mathcal B\): this is a Steiner quadruple system on \(q\) points in the even cases, and the blocks not involving one distinguished point of a Steiner quadruple system on \(q+1\) points in the odd cases. All codewords of multiplicity type \((2,1,1)\) are excluded in these families. For \(q=2\), the same canonical code is uniquely optimal directly.

The graph condition is genuinely needed outside these families: at \(q=6\), a six-cycle \(H=(0,2,4,1,3,5,0)\) and the three blocks complementary to the pairs \(\{0,1\},\{2,3\},\{4,5\}\) give an optimal code with six words of type \((2,1,1)\). It differs from the canonical all-pair-square construction.

## Assumptions and scope
The alphabet is labeled, with \(q\) any integer at least two; it need not be a prime power. Codewords are **unordered multisets**, not sequences. The deletion channel removes exactly one occurrence of a present symbol and does not alter the remaining multiplicities. A four-block packing means a simple family of distinct four-subsets with no repeated three-subset. The classification concerns **all maximum** one-deletion codes in this model, not merely linear/congruence codes. A perfect partition of the empty neighbor set is empty.

For the congruence-class classification we use the classical existence theorem for Steiner quadruple systems: a system of four-blocks containing every triple exactly once exists whenever the order is at least four and congruent to two or four modulo six. The cases of orders two and three are handled directly.

## Proof
**Deletion resources and the known maximum.** Partition any code by multiplicity type \((4),(3,1),(2,2),(2,1,1),(1,1,1,1)\), with cardinalities \(a,b,c,d,f\). Deleting from a word of these five types yields, respectively, one triple of type \((3)\); one each of types \((3)\) and \((2,1)\); two triples of type \((2,1)\); two of type \((2,1)\) plus one of type \((1,1,1)\); and four triples of type \((1,1,1)\). (The word “triple” here means a size-three multiset, not necessarily three distinct symbols.) No deletion output can be used by two codewords.

There are \(q\) outputs of type \((3)\), and exactly \(q(q-1)\) outputs of type \((2,1)\): the latter correspond to ordered arcs \((i,j)\), meaning two copies of \(i\) and one of \(j\). Hence
\[
a+b\le q,\qquad b+2c+2d\le q(q-1).\]
The squarefree codeword supports form a quadruple packing, so \(f\le D(q,4,3)\). Consequently
\[
|C|=a+b+c+d+f\le q+\frac{q(q-1)-b}{2}+D(q,4,3)
\le q+\binom q2+D(q,4,3).
\]
This sharp cardinality identity is Chen–Ma–Zhang's weight-four, distance-four constant-\(\ell_1\)-weight result (Theorem III.2), translated to unordered deletions. It is attained by taking every \(4e_i\), every \(2e_i+2e_j\) with \(i<j\), and the squarefree words of a maximum quadruple packing: their shadows have disjoint multiplicity types, with disjoint shadows within each type.

**Necessity of the graph-pairing data.** Equality in the preceding sharp bound forces \(b=0\), \(a=q\), \(f=D(q,4,3)\), \(c+d=\binom q2\), and equality in \(2c+2d\le q(q-1)\). Thus every pure word occurs, no \((3,1)\) word occurs, and **every oriented arc** \((i,j)\) belongs to the deletion shadow of exactly one word of type \((2,2)\) or \((2,1,1)\).

Let \(\mathcal B\) consist of the squarefree supports. Define \(H\) to contain precisely those unordered edges \(\{i,j\}\) for which the pair-square \(2e_i+2e_j\) is absent. An absent pair-square leaves both oriented arcs \((i,j)\) and \((j,i)\) to be used by words of type \((2,1,1)\). At vertex \(i\), each such word doubled at \(i\) uses **exactly two** arcs \((i,j),(i,k)\), and uniqueness of arc use partitions \(N_H(i)\) into pairs \(\{j,k\}\). Thus \(\deg_H(i)\) is even and the pairings \(\pi_i\) are forced. Each corresponding support \(\{i,j,k\}\) must be uncovered by \(\mathcal B\), or its deletion to three distinct symbols would collide with the squarefree word on that block. Two different centered words with the **same** three-point support would collide on that three-distinct-symbol deletion, so all assigned triples are distinct. These data can be recovered uniquely from the code.

**Sufficiency.** Given data satisfying the three stated requirements, the displayed family contains \(q\) pure words, \(\binom q2-|E(H)|\) pair-square words, \(\sum_i\deg_H(i)/2=|E(H)|\) mixed doubled words, and \(D(q,4,3)\) squarefree words, hence has the claimed maximum size. For correctness, classify possible deletion outputs as follows. Type \((3)\) comes from only one pure word per symbol. Every arc \((i,j)\) of type \((2,1)\) is used either by the present pair-square on \(\{i,j\}\), or, if that edge is in \(H\), by the unique wedge pair at center \(i\). Finally a three-distinct-symbol output belongs either to a unique squarefree block of the packing or to a unique assigned wedge triple; the uncovered-triple and distinctness conditions exclude any collision. Thus all deletion shadows are disjoint.

**Rigidity from Steiner designs.** If \(q\equiv2,4\pmod6\) with \(q\ge4\), an optimal quadruple packing is a Steiner quadruple system, since its size is the trivial triple-counting maximum \(\binom q3/4\) attained by Hanani's existence theorem. No triple is uncovered, so no wedge can be assigned and \(H=\varnothing\).

If \(q\equiv1,3\pmod6\) with \(q\ge3\), then \(q\) is odd. Every pair of vertices lies in \(q-2\) distinct triples, an odd number, whereas each selected four-block covering that pair accounts for two of those triples. Hence at least one triple containing each pair remains uncovered. The number of uncovered triples is at least \(\binom q2/3\). Adding a new point to a Steiner quadruple system of order \(q+1\), then retaining only blocks not containing that point, attains this lower bound; its uncovered triples form a Steiner triple system. Therefore, in **every** maximum quadruple packing on \(q\) vertices, the uncovered triples form a Steiner triple system \(\mathcal L\), with exactly one uncovered triple through each pair.

Suppose \(H\) had edge \(\{i,j\}\). The required wedge at \(i\) using neighbor \(j\) would assign some uncovered triple \(\{i,j,k\}\). The required wedge at \(j\) using neighbor \(i\) would assign another uncovered triple \(\{i,j,\ell\}\). By uniqueness of the \(\mathcal L\)-triple through \(\{i,j\}\), these triples coincide, contradicting the global nonrepetition requirement. Hence \(H\) is empty. Conversely, adjoining a distinguished new point to every uncovered triple of \(\mathcal L\) recovers a Steiner quadruple system on \(q+1\) points, proving the asserted bijection. For \(q=3\) the packing is empty and the same argument applies to its single uncovered three-set. For \(q=2\), neither a quadruple block nor a positive-degree even graph exists, so the canonical three-word code is the unique optimum.

**A noncanonical optimizer at \(q=6\).** Take the three four-blocks complementary to \(01,23,45\). They form a maximum packing: complements of any two four-blocks must be disjoint for their original blocks to meet in at most two points, so there can be at most three on six points. Let \(H\) be the six-cycle \((0,2,4,1,3,5,0)\), and at each cycle vertex pair its two neighbors. The six wedge triples, centered in cycle order, are \(\{0,2,5\},\{0,2,4\},\{1,2,4\},\{1,3,4\},\{1,3,5\},\{0,3,5\}\). All are distinct and uncovered by the three four-blocks. The parameterization therefore produces \(6+9+6+3=24\) compatible words, six of which have type \((2,1,1)\), proving that the mixed layer need not vanish in other congruence classes.

## Verification
Run `python3 verify.py` using Python's standard library. The checker reconstructs optimal canonical codes for \(2\le q\le8\) from explicit maximum packings, checks every deletion shadow directly, verifies all five multiplicity-type resource counts for every size-four profile, and separately constructs and directly checks the six-symbol noncanonical optimal code with its six-cycle wedge data. It also checks that its assigned triples are distinct and uncovered. The run returned `VERIFY_OK`. These finite checks are regression tests; the universal theorem is proved by the preceding resource and graph arguments, and the infinite Steiner corollaries invoke Hanani's published existence theorem.

## Relationship to prior work
Chen, Ma and Zhang (2020), Theorem III.2, **already proved** the exact optimal cardinality \(D(q,4,3)+\binom q2+q\) in equivalent constant-weight \(\ell_1\) terminology and exhibited the canonical construction. Neither that cardinality result nor the canonical construction is asserted as new here. The distinction is the complete necessary-and-sufficient classification of **all** equality cases, including the compatible even-degree graph and local neighbor pairings, global Steiner rigidity in four residue classes, and a concrete mixed optimum at six symbols. Kreindel, Essayag and Zabokritskiy (2026) review multiset-deletion codes and give general bounds and exact small-alphabet results; their weight-four results do not supply this optimizer parameterization. Kovačević and Tan (2018) develop the underlying unordered multiset channel and general packing bounds. The design-existence input is Hanani's classical Steiner quadruple system theorem, also discussed by Horan and Hurlbert (2012). Zabokritskiy (2026) determines exact independent-set sizes for five and seven alphabet symbols in every weight; its complete manuscript was not available for equality-case comparison here, so its potential implication is a residual risk.

## Limitations
This is a structural classification, not an enumeration of the number of optimal codes for every alphabet size. Outside the four indicated congruence classes, classifying all admissible packings and compatible graph pairings can still be difficult. The known value formula is not new; the newly asserted contribution is the all-optimizer characterization and its rigidity and mixed-family consequences. The finite checker does not prove the theorem for arbitrarily large alphabets, and an earlier unindexed equality-case classification remains possible.

## References
1. T. Chen, Y. Ma and X. Zhang, *Optimal codes with small constant weight in \(\ell_1\)-metric*, arXiv:2003.00483 (2020), Theorem III.2, https://arxiv.org/pdf/2003.00483.
2. A. Kreindel, I. B. Essayag and A. L. Zabokritskiy, *Multiset Deletion Codes: Cyclic Constructions, Bounds, and Exact Results*, arXiv:2601.05636 (first posted January 9, 2026), https://arxiv.org/pdf/2601.05636.
3. A. Kreindel, I. B. Essayag and A. L. Zabokritskiy, *Polynomial Constructions and Deletion-Ball Geometry for Multiset Deletion Codes*, arXiv:2603.18322 (2026), https://arxiv.org/pdf/2603.18322.
4. M. Kovačević and V. Y. F. Tan, *Codes in the Space of Multisets—Coding for Permutation Channels With Impairments*, IEEE Transactions on Information Theory (2018), https://doi.org/10.1109/TIT.2017.2760279.
5. H. Hanani, *On quadruple systems*, Canadian Journal of Mathematics 12 (1960), 145–157; V. Horan and G. Hurlbert, *Overlap Cycles for Steiner Quadruple Systems*, arXiv:1204.3215 (2012), https://arxiv.org/abs/1204.3215.
6. A. L. Zabokritskiy, *Independent Sets in Multiset Profile Graphs via Weighted Local Covers*, arXiv:2607.13733 (2026), https://arxiv.org/abs/2607.13733.
