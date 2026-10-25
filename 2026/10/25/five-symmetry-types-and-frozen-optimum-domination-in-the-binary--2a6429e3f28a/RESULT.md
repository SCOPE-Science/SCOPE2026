# Five symmetry types and frozen optimum domination in the binary five-cube

## Finding

Let \(Q_5\) be the graph on \(\mathbb F_2^5\) with two vertices adjacent precisely when their Hamming distance is one. A *total dominating set* \(S\) has an adjacent member of \(S\) at every vertex, including vertices of \(S\). A *paired dominating set* is a total dominating set whose induced graph admits a perfect matching. The reconfiguration graph for either optimum family joins sets \(S,T\) of minimum cardinality when \(|S\setminus T|=|T\setminus S|=1\).

**Theorem.** Both optimum cardinalities equal eight: \(\gamma_t(Q_5)=\gamma_{\mathrm{pr}}(Q_5)=8\). There are exactly \(1600\) labeled minimum total dominating sets, of which exactly \(1120\) are paired dominating and \(480\) are not. Every minimum total dominating set is isolated under single-vertex exchanges; consequently the minimum paired-domination exchange graph consists of \(1120\) isolated vertices.

More precisely, under all coordinate permutations and binary translations, the \(1600\) minimum total dominating sets fall into precisely five symmetry orbits. Their sizes, selected induced graph types, and paired status are:

| Orbit size | Induced graph on the eight selected vertices | Paired? |
|---:|---|---|
| 40 | \(2C_4\) | yes |
| 120 | \(4K_2\), affine span dimension three | yes |
| 480 | \(4K_2\), affine span dimension four | yes |
| 480 | \(2P_4\) | yes |
| 480 | \(2P_3\sqcup K_2\) | no |

Here \(P_r\) denotes a path on \(r\) vertices and \(\sqcup\) denotes disjoint union. The five orbit sizes add to \(1600\); the four paired orbit sizes add to \(1120\).

## Assumptions and scope

All sets are subsets of the 32 *labeled* binary length-five vertices. The parity classes \(E,O\) consist of vectors having respectively even and odd Hamming weight, with \(|E|=|O|=16\). In bit-mask examples, integer \(v\in\{0,\ldots,31\}\) denotes the vector whose coordinate \(i\) is bit \(i\), starting at zero. No conclusion about higher-dimensional cubes, near-optimal sets, or exchanges allowing temporary nonoptimal configurations is claimed.

## Proof

**1. The optimum is eight.** Because \(Q_5\) is bipartite, each selected even vertex can totally dominate only five odd vertices. Thus any total dominating set must contain at least four even vertices to dominate all 16 odd vertices. Likewise it must contain at least four odd vertices. Hence every total dominating set has size at least eight. The eight-vertex set \(\{0,1,2,3,28,29,30,31\}\) is total dominating; its induced graph is \(2C_4\), which has a perfect matching. Therefore both minimum cardinalities are eight.

**2. Exact characterization of the 40 feasible four-point parity blocks.** Write \(\mathbf1=(1,1,1,1,1)\), and let \(e_i\) be the \(i\)-th unit vector. For each unordered coordinate pair \(\{i,j\}\), put
\[
U_{ij}=\{0,e_i+e_j,\mathbf1+e_i,\mathbf1+e_j\}\subset E,
\]
where addition is in \(\mathbb F_2^5\). This is a two-dimensional vector subspace.

We claim that a four-point set \(A\subseteq E\) totally dominates every odd vertex if and only if \(A=x+U_{ij}\) for some \(x\in E\) and some \(i<j\). Translation by a chosen member of \(A\) allows us to assume \(0\in A\). Every nonzero even vector then has weight two or four. To dominate the all-one (weight-five) odd vertex, at least one of the other three members has weight four. A weight-four selected vector omitting coordinate \(k\) is adjacent to the four weight-three vectors whose supports omit \(k\), and a weight-two selected vector is adjacent to exactly three weight-three vectors.

If exactly one selected vector has weight four and omits \(k\), the six weight-three vectors containing \(k\) must be covered by the other two weight-two vectors. Each weight-two vector containing \(k\) reaches three of these six, and two distinct such vectors have one of these neighbors in common; a weight-two vector not containing \(k\) reaches only one. Two weight-two vectors therefore cannot cover all six. If all three nonzero selected vectors have weight four, the weight-three vector supported on their three distinct omitted coordinates is uncovered. Hence exactly two have weight four. Suppose their omitted coordinates are \(i\) and \(j\). The three weight-three vectors containing both \(i\) and \(j\) are untouched by either weight-four vector, so the remaining weight-two vector must be \(e_i+e_j\). This forces \(A=U_{ij}\).

Conversely, \(U_{ij}\) reaches every odd vertex: all weight-one vectors are adjacent to zero; the weight-five vector is adjacent to each weight-four member; a weight-three vector either omits \(i\) or \(j\) and meets the corresponding weight-four member, or contains both and meets \(e_i+e_j\). Translation preserves this property. There are ten distinct subspaces \(U_{ij}\), each with exactly four cosets in the sixteen-point even class. Distinct cosets belonging to distinct direction subspaces cannot coincide. Thus exactly \(10\cdot4=40\) possible even blocks occur. Odd translates yield exactly 40 possible odd blocks.

**3. Factorization and exchange isolation.** A minimum total dominating set \(S\) must contain exactly four vertices of each parity. It is total dominating if and only if its even four-set belongs to the 40 allowable even blocks and its odd four-set belongs independently to the 40 allowable odd blocks. This gives \(40^2=1600\) configurations.

An exchange between parity classes changes the \(4+4\) split to \(3+5\) or \(5+3\), contradicting the parity lower bound. An exchange within one parity class would produce two distinct affine two-planes of four points having three points in common. This is impossible in \(\mathbb F_2^5\): any three distinct points uniquely determine the fourth point of the affine two-plane, namely their vector sum. Thus the total-domination exchange graph has no edges. Its paired-domination subgraph has no edges either.

**4. Five-orbit matching classification.** It remains to classify the perfect-matching condition. Fix the even block \(A=\{0,3,29,30\}=U_{01}\), using integer bit masks. The subgroup of binary translations and coordinate permutations preserving parity and fixing \(A\) setwise has exactly 48 elements. It partitions the 40 allowable odd blocks into five orbits of sizes \(1,3,12,12,12\). Representatives \(B\), in that order, may be chosen as
\[
\begin{aligned}
&\{1,2,28,31\},\quad \{4,7,25,26\},\\
&\{1,4,26,31\},\quad \{4,11,21,26\},\quad \{1,13,22,26\}.
\end{aligned}
\]
For these pairs \(A\cup B\), their induced graph types are respectively \(2C_4\), \(4K_2\) (affine rank three), \(2P_4\), \(4K_2\) (affine rank four), and \(2P_3\sqcup K_2\). The first four admit perfect matchings, whereas the fifth has two odd-order components and does not. Translations and coordinate permutations act transitively on the 40 even blocks, so multiplying the local orbit sizes by 40 gives the five global orbit sizes \(40,120,480,480,480\). Consequently \(40(1+3+12+12)=1120\) total-dominating sets are paired, and \(40\cdot12=480\) are not.

The stabilizer order, orbit partition and induced graph types can be verified by direct evaluation of only the 48 stabilizer transformations on the 40 odd blocks. The accompanying standalone `verify.py` performs precisely these exhaustive finite group checks, independently enumerates all 40 blocks of each parity from the neighborhood definition, constructs all 1600 optimum total dominating sets, checks perfect matching, and also includes an optional direct enumeration of all \(\binom{32}{8}\) eight-vertex subsets. This finishes the proof.

## Verification

Running `python3 verify.py --exhaustive` uses only Python's standard library and prints `ALL_VERIFY_OK`. It independently checks the affine-plane characterization against all \(\binom{16}{4}=1820\) choices in each parity class; validates orbit sizes under all \(32\cdot5!=3840\) cube symmetries and, separately, under the 48-element stabilizer; checks perfect matchings via the full \(4!\) bipartite assignments; checks all optimum exchanges; and directly enumerates all \(\binom{32}{8}=10{,}518{,}300\) eight-vertex subsets when the `--exhaustive` flag is supplied. Both default and exhaustive modes completed successfully in the packaged check. The classification is exact at dimension five; there is no extrapolation to untested dimensions.

## Relationship to prior work

Paired domination was introduced by Haynes and Slater (1998). Brešar, Henning and Rall (2007) investigated general paired-domination bounds for Cartesian products. Gorzkowska, Henning, Pilśniak and Tumidajewicz (2023, open author PDF inspected through the hypercube subsection and adjacent definitions) explicitly give \(\gamma_{\mathrm{pr}}(Q_5)=8\) in their Table 2, as part of a study of stability after vertex deletion. Thus the optimum cardinality **is known and is not claimed as new**. The claim here concerns all labeled optimum configurations, the distinction between total and paired optima, the complete symmetry classification, and the absence of optimum-preserving single-vertex exchanges. The cited works do not state this combined classification in their inspected available material. Search and access limitations are recorded in the accompanying review; absence from an index does not establish priority.

## Limitations

This is a finite, exact result about \(Q_5\), not a theorem about all cubes. The completeness of the orbit calculations is checkable using the packaged finite verifier, but independent human review has not been performed. The 1998 and 2007 articles were accessible only through abstracts/bibliographic material; the 2023 article's hypercube section and definitions were read in full. There remains a risk of an earlier, unindexed statement giving the same configuration classification.

## References

1. T. W. Haynes and P. J. Slater, *Paired-domination in graphs*, Networks 32 (1998), 199–206, DOI: 10.1002/(SICI)1097-0037(199810)32:3<199::AID-NET4>3.0.CO;2-F (explicit first-public date 1998-12-07).
2. B. Brešar, M. A. Henning, and D. F. Rall, *Paired-domination of Cartesian products of graphs*, Utilitas Mathematica 73 (2007), 255–265, https://utilitasmathematica.com/index.php/Index/article/view/485.
3. A. Gorzkowska, M. A. Henning, M. Pilśniak, and E. Tumidajewicz, *Total and paired domination stability in prisms*, Discussiones Mathematicae Graph Theory 43 (2023), 1147–1169, DOI: 10.7151/dmgt.2421, accessible author manuscript https://galaxy.agh.edu.pl/~pilsniak/51.pdf.
