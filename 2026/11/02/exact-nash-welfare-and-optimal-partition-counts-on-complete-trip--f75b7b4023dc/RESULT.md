# Exact Nash welfare and optimal-partition counts on complete tripartite friendship graphs

## Finding
Let \(a\ge b\ge c\ge0\) be integers with \(n=a+b+c\ge2\). In the symmetric aversion-to-enemies hedonic game whose mutual-friendship graph is the complete tripartite graph with class sizes \((a,b,c)\), assign value \(+1\) across classes and value \(-n\) within a class. Nash welfare is the geometric mean of agents' coalition utilities, optimized over individually rational partitions.

**Theorem.** If \(a>b+c\), the maximum Nash welfare is \(0\). Otherwise, put \(t=b+c-a\). The exact maximum Nash welfare is
\[
\operatorname{NW}^{\star}=2^{3t/n}.
\]
Every Nash-optimal partition contains exactly \(a\) coalitions: precisely \(t\) three-agent coalitions (one agent from each class), \(a-c\) two-agent coalitions joining the largest class to the second class, and \(a-b\) two-agent coalitions joining the largest class to the third. Conversely, every partition with this composition is optimal. For distinctly labeled agents, the **exact number** of optimal partitions is
\[
\frac{a!\,b!\,c!}{(b+c-a)!\,(a-c)!\,(a-b)!}.
\]
This counting formula is asserted only in the positive-welfare regime \(a\le b+c\); when the optimum is zero, many individually rational partitions can be optimal and they are not enumerated here. By symmetry, the class labels can be permuted before applying the theorem.

In particular, for three roles the positive optimum depends only on the population \(n\) and largest role size \(a\), whereas the number of optimal partitions depends on all three sizes. The majority threshold \(2a>n\) forces the welfare to collapse to zero.

## Assumptions and scope
A finite set of \(n\) distinct agents is divided into three possibly empty role classes. Pairwise valuations are symmetric. Each agent values another agent at \(1\) if their roles differ and at \(-n\) if their roles coincide. Agent \(i\)'s utility is the sum of the values it assigns to its fellow coalition members; singleton utility is \(0\). Only partitions where every agent has nonnegative utility are admissible for Nash welfare, in line with the geometric-mean convention in Pagano–Schlenga. No bound is imposed on the number of coalitions. Factorials include \(0!=1\).

## Proof
**1. Individually rational coalitions are cliques.** If a coalition contains two agents of the same class, each of them receives at most \(n-2\) positive contributions and one contribution of \(-n\), hence utility at most \(-2\). Such a coalition cannot occur in an individually rational partition. Conversely, a coalition with no repeated class gives every member utility equal to its size minus one. Thus all individually rational coalitions have size at most three, and positive Nash welfare requires a partition entirely into mixed-class pairs and triplets, with no singleton.

**2. Necessity of the majority threshold.** The largest class has \(a\) agents, at most one per positive-welfare coalition. Every one of those coalitions requires at least one agent outside that class. Thus \(b+c\ge a\) is necessary. When \(a>b+c\), every individually rational partition has a singleton, and consequently its Nash welfare is zero.

**3. Upper bound on three-agent coalitions.** In a positive-welfare partition, let \(T\) be the number of triplets, \(P\) the number of pairs and \(q=P+T\) the total number of coalitions. Then \(n=2P+3T=2q+T\). As every coalition contains at most one member of the largest class, \(q\ge a\), hence \(T\le n-2a=b+c-a=t\). Members of pairs have utility \(1\), members of triplets utility \(2\), so the Nash welfare is exactly \(2^{3T/n}\). It is strictly increasing in \(T\); therefore \(2^{3t/n}\) is an upper bound.

**4. Matching construction and equality classification.** Suppose \(a\le b+c\). Since \(a\ge b\ge c\), the numbers \(t=b+c-a\), \(a-c\), and \(a-b\) are all nonnegative and sum to \(a\). Partition the agents of the largest class into groups of those three cardinalities. Give each of the \(t\) agents in the first group a distinct partner from each smaller class, forming triplets. Give each of the \(a-c\) agents in the second group a distinct partner from the class of size \(b\), forming pairs. Give each of the \(a-b\) agents in the third group a distinct partner from the class of size \(c\), also forming pairs. The required partner totals are \(t+(a-c)=b\) and \(t+(a-b)=c\), so every agent is used exactly once. This produces positive Nash welfare \(2^{3t/n}\). Since a positive optimum must have \(T=t\), it must also have \(q=(n-t)/2=a\). All its coalitions therefore contain exactly one largest-class agent, and the stated pair/triplet counts are forced. This proves both optimality and the converse.

**5. Counting all optimizers.** First partition the \(a\) labeled largest-class agents into the triplet positions, size-\(b\)-class pair positions, and size-\(c\)-class pair positions. There are \(a!/[t!(a-c)!(a-b)!]\) choices. The \(b\) labeled agents from the second class can then be assigned bijectively to their \(b\) specified positions in \(b!\) ways; the \(c\) labeled agents from the third class can similarly be assigned in \(c!\) ways. Every optimal unordered coalition partition is obtained once, since every coalition has a unique largest-class member. Multiplying the factors yields the counting formula.

## Verification
A standalone standard-library Python checker, `verify.py`, independently enumerates every partition into admissible mixed-class pairs or triplets by recursively fixing a labeled agent and choosing its partners. It compares the maximum triplet count and the optimizer multiplicity to the closed formula on \(715\) class-size profiles (each class at most eight, total population between two and twenty-one). A separate literal-payoff enumeration examines \(224{,}935\) unrestricted set partitions across \(161\) labeled class-size profiles of total population at most eight, checking the nonnegative-utility condition and the exact Nash product. Both checks pass. Invoke `python3 verify.py` from the directory containing this file.

For example, the population sizes \((5,4,4)\) give \(t=3\), maximum welfare \(2^{9/13}\), and exactly \(11{,}520\) optimal labeled coalition partitions. By contrast, the utilitarian maximization criterion can favor four disjoint triplets plus one singleton, which has zero Nash welfare: the two objectives need not choose the same partitions.

## Relationship to prior work
Pagano and Schlenga (2026) introduce Nash welfare for additively separable hedonic games, prove general NP-hardness even for symmetric aversion-to-enemies games, identify the clique-partition condition for individual rationality and positivity, and give an \((n-1)\)-approximation. Those theorems do not state the exact positive Nash welfare or the number of optimal partitions for arbitrary complete tripartite class sizes. The proof here uses the model and its known clique interpretation but establishes the exact tripartite specialization and its optimizer census.

Bullinger, Chatziafratis, and Shahkar (2025, Section 5.2) study *utilitarian* welfare on random multipartite friendship networks and describe a trivial unperturbed multipartite welfare maximizer. Utilitarian maximizers can contain singleton agents, making their Nash welfare zero; hence the utilitarian statement does not imply the positive Nash optimum and its count proved here. The OEIS sequence A297527 counts maximum graph-theoretic matchings in balanced complete tripartite graphs, a different object from partitions into two- and three-agent coalitions: for class sizes \((2,2,2)\), that sequence's count is \(8\), while the present optimal-coalition count is \(4\).

## Limitations
The formula assumes three role classes, complete friendship across distinct classes, uniform unit friendships, and the strong negative value \(-n\) within a class. It does not characterize optimal-partition counts when maximum Nash welfare is zero, does not extend automatically to four or more role classes or missing cross-class friendships, and does not establish publication priority. Its verification exhausts specified finite parameter ranges; the all-size conclusion rests on the analytical proof.

## References
1. Marta Pagano and Alexander Schlenga, *Nash Welfare in Additively Separable Hedonic Games*, arXiv:2605.19030v1, first posted May 18, 2026. https://arxiv.org/html/2605.19030v1
2. Martin Bullinger, Vaggos Chatziafratis and Parnian Shahkar, *Welfare Approximation in Additively Separable Hedonic Games*, arXiv:2503.06017v1, March 8, 2025. https://arxiv.org/html/2503.06017v1
3. OEIS A297527, *Number of maximum matchings in the complete tripartite graph \(K_{n,n,n}\)*. https://oeis.org/A297527
