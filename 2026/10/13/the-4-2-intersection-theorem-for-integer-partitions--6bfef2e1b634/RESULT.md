# The \((4,2)\) intersection theorem for integer partitions

## Finding
Let \(P_{n,4}\) be the set of all partitions of an integer \(n\ge4\) into exactly four positive parts. Write \(M_{4,2}(n)\) for the largest cardinality of a subfamily in which any two distinct partitions have at least two common parts, counting multiplicity. Then, for every integer \(n\ge4\),
\[
M_{4,2}(n)=\left\lfloor\frac{n-2}{2}\right\rfloor+\begin{cases}1,&n=9,\\0,&n\ne9.\end{cases}
\]
For \(n\ge30\), every maximum family is a full two-star of maximum cardinality. The center is \(\{1,1\}\), or, when \(n\) is odd, it may instead be \(\{1,2\}\). The four-member counterexample at \(n=9\) was already exhibited by Borg; it is included here as a necessary known exception, not claimed as new.

## Assumptions and scope
Partitions are unordered multisets, represented by their unique nondecreasing sequences \((a_1,a_2,a_3,a_4)\) of positive integers with \(a_1+a_2+a_3+a_4=n\). For partitions \(\lambda\) and \(\mu\), their intersection multiplicity is \(\sum_{a\ge1}\min(m_\lambda(a),m_\mu(a))\). A *full two-star* consists of all partitions containing one prescribed multiset of two parts. A family is *trivial* if its members have two common parts across the entire family, and *nontrivial* otherwise.

Use occurrence labels \(S_\lambda=\{(a,j):1\le j\le m_\lambda(a)\}\). Each \(S_\lambda\) has four elements, and \(|S_\lambda\cap S_\mu|\) equals the number of common parts counted with multiplicity. In this fixed-sum four-part universe, any three occurrence labels extend to **at most one** valid partition: the fourth part value is forced by the sum, and the canonical occurrence-label rule can only discard that candidate.

## Proof
**Full stars.** Fix positive parts \(a\le b\). If \(n-a-b\ge2\), deletion of these two prescribed parts gives a bijection to partitions of \(n-a-b\) into two positive parts. Hence the corresponding two-star has size \(\lfloor(n-a-b)/2\rfloor\), and otherwise it is empty. The largest size is therefore \(s(n)=\lfloor(n-2)/2\rfloor\), attained for \(\{1,1\}\). Equality also holds for \(\{1,2\}\) when \(n\) is odd; no other center is largest.

**Nontrivial-family cap.** Let \(\mathcal F\) be a nontrivial two-intersecting family. If every two of its members have at least three common occurrence labels, fix one member \(L\). Each other member contains at least one of the four triples of labels of \(L\), and each triple extends to at most one partition. Consequently \(|\mathcal F|\le4\).

Otherwise choose \(L,N\in\mathcal F\) with precisely two common occurrence labels. Write \(L=I\cup A\) and \(N=I\cup B\), where \(|I|=|A|=|B|=2\) and \(I,A,B\) are pairwise disjoint. As \(\mathcal F\) is nontrivial, some \(E\in\mathcal F\) does not contain all of \(I\). Partition the family into members containing both labels of \(I\) and members containing at most one.

A member containing \(I\) must, by intersection with \(E\), also contain at least one label of \(E\setminus I\). There are at most four choices of this third label, and each triple \(I\cup\{e\}\) extends to at most one partition. Thus at most four members contain \(I\).

A member containing exactly one label from \(I\) must contain at least one label from each of \(A\) and \(B\), to two-intersect both \(L\) and \(N\). There are at most \(2\cdot2\cdot2=8\) ways to choose such a triple, each with at most one completion. A member containing no label from \(I\) must contain all four labels of \(A\cup B\); hence there is at most one. Summing gives the **universal bound** \(|\mathcal F|\le4+8+1=13\). This is a specialized instance of the nontrivial-intersection bounds from Borg's earlier work, and the bound is not asserted to be original.

**Large orders.** For \(n\ge30\), the largest star has size \(s(n)\ge14>13\). Every maximizing two-intersecting family must therefore be trivial, and maximal cardinality forces it to be a full largest two-star. This proves both the formula and the extremizer statement for all \(n\ge30\).

**Remaining orders.** For each of the 26 integers \(4\le n\le29\), the accompanying standard-library program generates every nondecreasing four-part partition. It forms a graph with one vertex per partition and an edge between pairs sharing at least two parts. It calculates the exact maximum clique size by exhaustive branching, pruning only when the greedy-coloring bound on a remaining induced graph proves that a branch cannot improve the incumbent. Thus no candidates are dropped without a valid upper bound. A separate subset census matches all cases through \(n=13\). The resulting maximum sizes equal \(s(n)\) except at \(n=9\), where the maximum is four rather than three. A four-member witness is
\[
\{(1,1,2,5),(1,1,3,4),(1,2,2,4),(1,2,3,3)\}.
\]
All four partitions sum to nine and any two share at least two parts. The upper bound of four at this order follows from the exhaustive finite clique computation. Together with the large-order argument this establishes the theorem for every \(n\ge4\).

## Verification
Run `python3 verify_four_parts.py` from the directory containing this document. The program has no third-party dependencies. It constructs all 26 finite compatibility graphs, verifies partition counts by an independent partition-number recurrence, compares multiset intersection against occurrence-label intersection, and evaluates each exact maximum clique. A second standard-library program, `verify_bk.py`, independently enumerates **all maximal cliques** via Bron--Kerbosch pivot recursion for every order \(4\le n\le29\), using a separately implemented partition generator. Direct exhaustive subset scans additionally confirm clique maxima through \(n=13\). The recorded outputs `verify_output.txt` and `verify_bk_output.txt` end in `ALL_CHECKS_PASSED` and `INDEPENDENT_ALL_MAXIMAL_CLIQUES_PASS n=4..29`, respectively. Computation is used only for the finite range \(4\le n\le29\), never to infer an unbounded result.

## Relationship to prior work
Borg's *Intersecting integer partitions* (2016, Conjecture 1.6 and Remark 1.5) proposes the canonical maximum two-star bound outside the exceptional parameters and already gives the counterexample at \(n=9\). Its Proposition 1.7 handles small orders and Theorem 1.8 handles orders \(n\ge3tk^5\), which at the parameters of this theorem only yields an extremely remote range. Borg's general Lemma 3.1 also contains a stronger structural bound that specializes to the thirteen-member nontrivial cap proved above; this auxiliary cap is not a novelty claim.

Person and Schweser (arXiv:2610.01747v1, published online 1 October 2026) prove star optimality when the number of parts is sufficiently large and the total grows cubically with that number, and exhibit further counterexamples as the part number grows. Their statements do not yield a bound valid for fixed four parts at every order. The contribution here is the exact **all-order fixed-parameter classification**, including finite intermediate orders not implied by the cited asymptotic and large-order theorems. The exceptional four-member family itself was previously known.

## Limitations
The result is specific to four parts and required pairwise intersection multiplicity two; no claim is made for other numbers of parts, other intersection thresholds, all extremizers at \(n<30\), or general set partitions. The bounded computation covers every needed small order because the analytic nontrivial bound closes the remainder; it is not an infinite exhaustive search. Although the cited sources and indexed prior findings were compared, an unindexed equivalent classification cannot be ruled out. Independent external validation is not asserted.

## References
1. P. Borg, *Intersecting integer partitions*, Australasian Journal of Combinatorics 66(2) (2016), 265–275, Conjecture 1.6, Remark 1.5, Lemma 3.1, Theorem 1.8. Public repository: https://www.um.edu.mt/library/oar/handle/123456789/75639 . Earlier preprint: arXiv:1304.6563.
2. Y. Person and T. Schweser, *Intersecting integer partitions: star bounds and counterexamples at every scale*, arXiv:2610.01747v1 (1 October 2026), Theorems 1.1 and 1.2, Sections 2 and 5. https://arxiv.org/abs/2610.01747 .
