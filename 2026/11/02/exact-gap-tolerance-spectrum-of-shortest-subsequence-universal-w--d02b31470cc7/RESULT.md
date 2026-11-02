# Exact gap-tolerance spectrum of shortest subsequence-universal words

## Finding
Fix a labeled alphabet \(\Sigma\) of size \(q\ge2\) and a target length \(k\ge2\). A word \(w\in\Sigma^{qk}\) is *subsequence-universal* of order \(k\) if every length-\(k\) word over \(\Sigma\) occurs as a scattered subsequence. For an embedding at increasing positions \(i_1<\cdots<i_k\), its *jump* is \(\max_{1\le j<k}(i_{j+1}-i_j)\). Define the universal gap radius
\[
G_k(w)=\max_{u\in\Sigma^k}\ \min_{\substack{i_1<\cdots<i_k\\w_{i_j}=u_j}}
\max_{1\le j<k}(i_{j+1}-i_j).
\]
This quantity is defined only when \(w\) is order-\(k\) subsequence-universal. The ordinary gap length (number of skipped host positions) is the jump minus one.

Every universal host of shortest possible length \(qk\) has a unique decomposition into \(k\) consecutive permutation blocks, \(w=P_1P_2\cdots P_k\), where each \(P_i\) is a permutation of \(\Sigma\). Write \(p_i(a)\) for the position of symbol \(a\) inside block \(P_i\). Then
\[
\boxed{G_k(w)=q+\max_{\substack{1\le i<k\\a\in\Sigma}}\bigl(p_{i+1}(a)-p_i(a)\bigr).}
\]
In particular \(q\le G_k(w)\le2q-1\).

For every integer \(d\) with \(0\le d\le q-1\), the exact number of *indexed, labeled* shortest universal hosts having \(G_k(w)\le q+d\) is
\[
\boxed{N_{q,k}(d)=q!\left((d+1)!\,(d+1)^{q-d-1}\right)^{k-1}.}
\]
Consequently the number of hosts with radius exactly \(q+d\) is \(N_{q,k}(d)-N_{q,k}(d-1)\), with \(N_{q,k}(-1)=0\). The unique optimizers for the smallest radius \(q\) are the \(q!\) repeated-permutation words \(P^k\). The largest possible radius \(2q-1\) occurs in a uniformly chosen shortest universal host with exact probability
\[
\boxed{1-\left(\frac{q-1}{q}\right)^{k-1},}
\]
which approaches one exponentially for every fixed \(q\).

## Assumptions and scope
The alphabet contains \(q\ge2\) *distinct labeled symbols*; \(k\ge2\); all words are indexed and are not identified under cyclic rotation or alphabet relabeling. Only shortest-length ordinary universal hosts \(w\in\Sigma^{qk}\) are counted. Each target \(u\) may choose a different embedding. The jump constraint is *uniform across all consecutive embedded positions* and permits no restriction on the unselected prefix or suffix. A jump bound \(q+d\) corresponds to maximum skipped gap length \(q+d-1\). The case \(k=1\) is excluded because a maximum over zero consecutive gaps requires a separate convention.

## Proof
**1. Shortest universal hosts.** Universality forces all \(q\) constant words of length \(k\) to occur, hence at least \(k\) occurrences of every symbol and length at least \(qk\). The standard arch-factorization characterization of subsequence universality states that a word is order-\(k\) universal if and only if it can be partitioned into \(k\) consecutive factors each containing every alphabet symbol (see Kosche–Koß–Manea–Siemer, Theorem 13). When the total length is \(qk\), every factor has exactly \(q\) positions, so all factors are permutations and the only possible factor boundaries are at multiples of \(q\). Conversely any \(k\) permutation blocks are universal, by choosing target symbol \(j\) from block \(j\). Thus these and only these words are shortest universal hosts.

**2. Exact jump radius.** Set
\[
M=q+\max_{\substack{1\le i<k\\a\in\Sigma}}
\bigl(p_{i+1}(a)-p_i(a)\bigr).
\]
For each boundary \(i\), the sum of the \(q\) displacements \(p_{i+1}(a)-p_i(a)\) over all symbols equals zero. Thus their maximum is nonnegative; also each displacement is at most \(q-1\). Therefore \(q\le M\le2q-1\).

For the *lower bound*, the target \(u=a^k\) has only one possible embedding, since each letter occurs exactly once in each permutation block. Its consecutive jumps are precisely \(q+p_{i+1}(a)-p_i(a)\). Taking the largest of these over the symbols and boundaries proves \(G_k(w)\ge M\).

For the *upper bound*, fix an arbitrary target \(u\in\Sigma^k\), and embed it greedily, each symbol at its first occurrence following the previous chosen position. The embedding exists, since the blockwise embedding exists. If the \(j\)-th chosen position lies in block \(P_i\), then \(i\le j\): after reading \(j\) symbols a greedy embedding cannot have advanced more than \(j\) permutation blocks. Consequently, for \(j<k\) the next symbol occurs no later than block \(P_{i+1}\). Let the current offset inside \(P_i\) be \(r\), and let the next requested symbol be \(b\). If \(b\) occurs later in \(P_i\), the next jump is at most \(q-1\le M\). Otherwise the next chosen occurrence is at offset \(p_{i+1}(b)\) in \(P_{i+1}\). Since \(b\) did not occur after offset \(r\) in \(P_i\), we have \(p_i(b)\le r\), and hence the jump is
\[
q+p_{i+1}(b)-r\le q+p_{i+1}(b)-p_i(b)\le M.
\]
All consecutive jumps in this embedding are thus at most \(M\), uniformly for every target. This proves \(G_k(w)=M\).

**3. Exact enumeration.** For a fixed permutation block \(P_i\), the next block \(P_{i+1}\) is eligible for \(G_k(w)\le q+d\) precisely when every symbol obeys \(p_{i+1}(a)\le p_i(a)+d\). Reindexing symbols in order of their positions in \(P_i\) gives the permutations \(\pi\) of \(\{1,\ldots,q\}\) satisfying \(\pi(j)\le j+d\) for all \(j\).

Construct \(\pi\) in row order \(j=1,\ldots,q\). For \(1\le j\le q-d\), there are exactly \(d+1\) available values among \(1,\ldots,j+d\), because the \(j-1\) previously selected values all belong to that range. For \(j>q-d\), all remaining \(q-j+1\) values are permitted. Therefore the total number of allowed next blocks is
\[
C_{q,d}=(d+1)^{q-d}\,d!=(d+1)!\,(d+1)^{q-d-1}.
\]
This number is independent of the present permutation block. Choosing the first block in \(q!\) ways and each of the next \(k-1\) blocks in \(C_{q,d}\) ways proves the formula for \(N_{q,k}(d)\). Subtraction proves the exact-radius spectrum. At \(d=0\), the restricted permutation must be the identity, so the minimum radius is attained exactly by repeated blocks. At \(d=q-1\), all \(q!\) choices are allowed independently; at \(d=q-2\) there are \((q-1)!(q-1)\) choices. Their ratio gives the displayed largest-radius probability.

## Verification
The standalone program `verify_gap_universality.py` independently constructs embeddings by literal combinations of indices and checks all words with equal multiplicities of every symbol for \((q,k)\in\{(2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(4,2)\}\). For each host it checks whether the full set of target strings is present, the necessary permutation-block condition, and the literal worst-target minimum jump. It compares all radius distributions against the closed formula. It separately enumerates all eligible bounded-displacement permutations for every \(q\in\{2,3,4,5,6,7\}\) and every \(d\in\{0,\ldots,q-1\}\).

Successful replay reports `VERIFY_OK parameter_cases=7 balanced_hosts=4638 universal_hosts=888 exact_pattern_checks=40901`; it also reports `bounded_drop_counts=27`. These finite checks support implementation correctness and boundary handling but cannot substitute for the quantified proof above.

## Relationship to prior work
Day, Kosche, Manea, and Schmid study matching and complexity of *general* gap-constrained subsequences and their universality, including upper gap constraints (arXiv:2206.13896). Their full accessible preprint, including the analysis-problems section, treats decision algorithms and complexity bounds; it does not supply the present exact shortest-host gap-radius characterization or distribution. Kosche, Koß, Manea, and Siemer's survey (arXiv:2208.14722, Theorem 13) gives the arch characterization used in Step 1, but no uniform-jump spectrum. Chen and Chen (arXiv:1306.5428) and earlier bounded-drop literature study restricted permutations: the count in Step 3 is a classical restricted-permutation enumeration, **not** independently claimed as new. The contribution assessed here is the coupling of worst-pattern bounded-gap subsequence universality to a sharp adjacent-block statistic and the ensuing complete all-parameter host-radius distribution.

A publicly accessible result titled *Exact full-support insertion radius of subsequence universality* concerns the maximum insertion distance to universality over full-support words; its full mathematical statement does not impose embedding gaps or count shortest universal hosts by their bottleneck jump. Likewise, published binary universality-index distributions omit the gap parameter. Relevant published-record searches did not reveal an equivalent all-parameter result. There remains a risk that an equivalent specialization occurs in less-indexed literature.

## Limitations
The result covers only *minimum-length* universal hosts and \(k\ge2\); longer universal hosts, variable individual gap limits, nonuniform alphabet weights, and cyclic words are not classified. The proof uses the known arch-factorization theorem and a classical bounded-displacement permutation count. The quantitative novelty assessment is limited by discoverability of earlier results.

## References
1. J. D. Day, M. Kosche, F. Manea, and M. L. Schmid, *Subsequences With Gap Constraints: Complexity Bounds for Matching and Analysis Problems*, arXiv:2206.13896v1, first public 2022-06-28. https://arxiv.org/html/2206.13896v1
2. M. Kosche, T. Koß, F. Manea, and S. Siemer, *Combinatorial Algorithms for Subsequence Matching: A Survey*, arXiv:2208.14722, first public 2022-08-31. https://arxiv.org/abs/2208.14722
3. J. N. Chen and W. Y. C. Chen, *On Permutations with Bounded Drop Size*, arXiv:1306.5428, first public 2013-06-23. https://arxiv.org/html/1306.5428v1
4. *Exact full-support insertion radius of subsequence universality*, public mathematical record, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-full-support-insertion-radius-of-subsequence-universality--967f04fec949
