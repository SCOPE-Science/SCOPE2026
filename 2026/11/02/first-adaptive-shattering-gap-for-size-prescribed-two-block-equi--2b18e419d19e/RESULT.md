# First adaptive-shattering gap for size-prescribed two-block equivalence relations

## Finding

Let \(V\) be a finite labeled set, and let \(\mathcal B(V;a,b)\) be the Boolean concept class of **unlabeled** partitions \(\{A,B\}\) of \(V\) with \(|A|=a\), \(|B|=b\), where \(1\le a\le b\) and \(a+b=|V|\). Its query domain consists of the unordered pairs \(\{u,v\}\subseteq V\); the answer is one precisely when \(u\) and \(v\) belong to the same block. Identical partitions under exchange of their blocks count as one hypothesis.

The first strict separation between ordinary VC dimension and deterministic realizable Littlestone dimension, over **every** prescribed positive two-block size profile on at most five vertices, occurs at the unique five-vertex profile \((a,b)=(2,3)\). Precisely,
\[
\operatorname{VCdim}(\mathcal B([5];2,3))=2,\qquad
\operatorname{Ldim}(\mathcal B([5];2,3))=3.
\]
All two-block profiles on two, three, or four vertices have equal VC and Littlestone dimensions. The remaining five-vertex profile \((1,4)\) also has equal dimensions, both two.

For every \(s\ge1\), partition \(5s\) labeled vertices into \(s\) **known** disjoint groups of five. Let \(\mathcal H_s\) consist of equivalence relations which, independently in each group, have precisely two blocks of sizes two and three, and whose equivalence classes never cross the known groups. On the entire pair-query domain, including cross-group pairs, one has
\[
\operatorname{VCdim}(\mathcal H_s)=2s,\qquad
\operatorname{Ldim}(\mathcal H_s)=3s.
\]
Consequently the static-versus-online shattering gap is exactly \(s\), despite a uniform bound of five on the prescribed group sizes. Cross-group queries are identically false and contribute zero to either dimension.

## Assumptions and scope

All sets and concept classes are finite; the two blocks of each partition are unordered. Queries are binary equality-of-class tests, not exact-recovery queries and not cluster-center queries. A depth-\(d\) complete binary mistake tree has one pair query at each internal node, with both answer branches realized by some hypotheses on every path. VC shattering uses one fixed query support for all labelings. The case \(s=0\) is excluded.

## Proof

**Local five-vertex upper VC bound.** Label the vertices \(0,1,2,3,4\), and represent a hypothesis by its unique smaller (two-element) block. There are \(\binom52=10\) hypotheses. Any three-edge query support is, up to vertex relabeling, one of exactly four types: a triangle with two isolated vertices; a three-edge star with one isolated vertex; a four-vertex path with one isolated vertex; or a three-vertex path disjoint from an edge. This classification exhausts all three-edge simple graphs on five vertices. The triangle is not shattered because two positive (same-block) edges and one negative edge contradict transitivity. In either the star or the four-vertex path, labeling all three edges positive would force four vertices into one block, exceeding the maximum allowed block size three. In the path-plus-edge case, labeling the two path edges positive and the disjoint edge negative would force the three path vertices to be the full size-three block and the remaining two vertices to be the full size-two block, contradicting the negative edge. Hence no three-edge support is shattered. A larger shattered support would contain a shattered triple, so the VC dimension is at most two.

**Local VC lower bound.** The queries \(\{0,1\}\) and \(\{0,2\}\) realize all four pairs of answers: \((0,0)\) with small block \(\{0,4\}\); \((0,1)\) with \(\{1,4\}\); \((1,0)\) with \(\{2,4\}\); and \((1,1)\) with \(\{3,4\}\). Thus VC dimension is two.

**Local online lower bound.** The following is an explicit complete depth-three binary query tree. Its root queries \(\{0,1\}\). If the answer is zero, next query \(\{0,2\}\); for either answer, the third query is \(\{0,3\}\). The four answer leaves \((0,0,0)\), \((0,0,1)\), \((0,1,0)\), \((0,1,1)\) are witnessed respectively by small blocks \(\{0,4\}\), \(\{0,3\}\), \(\{0,2\}\), \(\{1,4\}\). If the root answer is one, next query \(\{2,3\}\); when its answer is zero, query \(\{0,2\}\) and use witnesses \(\{2,4\}\) and \(\{3,4\}\) for final answers zero and one. When its answer is one, query \(\{0,4\}\) and use witnesses \(\{0,1\}\) and \(\{2,3\}\) for final answers zero and one. Direct substitution verifies every leaf. Therefore the Littlestone dimension is at least three. A complete tree of depth four would require at least sixteen distinct hypotheses, whereas there are ten; hence Littlestone dimension is exactly three.

**Sharp minimality across smaller profiles.** For \(|V|=2\), profile \((1,1)\) has one hypothesis and both dimensions zero. For \(|V|=3\), profile \((1,2)\) has three hypotheses, at least two distinct, so both dimensions are one. On four vertices the \((2,2)\) profile has three hypotheses and both dimensions one. The \((1,3)\) profile has four hypotheses and the two queries \(\{0,1\},\{0,2\}\) realize all four labels by choosing the singleton block in turn as \(\{0\},\{1\},\{2\},\{3\}\), so both dimensions are two. On five vertices \((1,4)\) has five hypotheses and the same two queries are shattered; the hypothesis-count upper bound shows its Littlestone dimension at most two. Thus the first separation occurs only at \((2,3)\) on five vertices.

**Exact amplification.** For concept classes on disjoint nonconstant query domains with independent choices of hypotheses, VC dimension is additive: the intersection of any shattered support with each query domain is shattered locally; conversely unions of local shattered supports are shattered. Littlestone dimension is also additive: concatenating complete local mistake trees gives the lower bound, while separately running an optimal realizable online predictor for each factor yields the upper bound, since its local mistake count is at most the factor's Littlestone dimension. Applying these facts to \(s\) five-vertex factors gives dimensions \(2s\) and \(3s\). Cross-group pair queries are constants and cannot occur in a shattered tree or support.

## Verification

Run \(\texttt{python3 check\_balanced\_partitions.py}\) in the directory containing the supplied certificate files. The standard-library-only program enumerates all allowed two-block partitions on at most five labeled vertices and computes both dimensions from the definitions. It checks each of the \(\binom{10}{3}=120\) possible three-query supports for the \((2,3)\) profile, classifies them into the four graph types, constructs a full depth-three adaptive tree, verifies its eight leaves, and writes a reproducible JSON certificate. The companion recorded stdout supplies an exact expected result and certificate digest. The unrestricted amplification rests on the proof above, not on extrapolation from finite enumeration.

## Relationship to prior work

Li, Song, and Zhang (2021) study clustering with same-cluster queries, particularly identifying large clusters under learning assumptions. DePavia, Medrano Martín del Campo, and Tani (2023) analyze exact partition recovery with bounded adversarial oracle errors and total query complexity; their paper also discusses balanced target partitions in expected-query analysis. Chase, Freitag, and Reyzin (2023) study general applications of Littlestone dimension to query-learning and compression. Those investigations use different objectives from the **realizable online mistake-tree dimension of the prescribed \((2,3)\) partition class**. The comparison is by statement and implication, not just title. A complete negative historical-priority claim is not made.

## Limitations

The finite classification is for two nonempty blocks on at most five points. The all-\(s\) formulas apply only when the five-point supergroups are prescribed and their choices independent, not to arbitrary unlabeled decompositions of \(5s\) points into blocks of sizes two and three. The work does not give a closed formula for general larger prescribed block-size profiles, nor an exact-recovery query bound. No independent mathematical audit has been performed.

## References

- Y. Li, Y. Song, Q. Zhang, *Learning to Cluster via Same-Cluster Queries*, arXiv:2108.07383v1, first public August 17, 2021. https://arxiv.org/abs/2108.07383
- A. F. DePavia, O. Medrano Martín del Campo, E. Tani, *Error-Tolerant Exact Query Learning of Finite Set Partitions with Same-Cluster Oracle*, arXiv:2305.13402v1, first public May 22, 2023. https://arxiv.org/abs/2305.13402
- H. Chase, J. Freitag, L. Reyzin, *Applications of Littlestone Dimension to Query Learning and to Compression*, arXiv:2310.04812v1, first public October 7, 2023. https://arxiv.org/abs/2310.04812
