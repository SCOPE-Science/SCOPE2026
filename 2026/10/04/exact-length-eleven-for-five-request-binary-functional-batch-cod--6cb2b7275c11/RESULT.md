# Exact length eleven for five-request binary functional batch codes with locality two
## Finding
For binary three-dimensional functional batch codes in which every request in every five-request multiset has a pairwise-disjoint recovery set of size at most two, the minimum length is exactly \(11\). Equivalently, a \([11,3,5,2]\) code exists and no \([n,3,5,2]\) code exists for \(n\le 10\).

A concrete optimal generator matrix has columns
\[
(1,0,0),(0,1,0),(1,1,0),(0,0,1),(0,0,1),(1,0,1),(1,0,1),(0,1,1),(0,1,1),(1,1,1),(1,1,1).
\]
Thus the seven nonzero vectors of \(\mathbb F_2^3\) occur with multiplicities \((1,1,1,2,2,2,2)\).

## Assumptions and scope
An \([n,k,t,r]\) binary functional batch code is a binary \(k\times n\) generator matrix such that every multiset of \(t\) nonzero query vectors can be assigned pairwise-disjoint recovery sets, one for each query, with every recovery set containing at most \(r\) columns whose span contains that query. Only linear binary codes, dimension \(3\), five simultaneous functional queries, and locality \(2\) are claimed here. Zero columns are irrelevant and can be deleted.

Identify the seven nonzero vectors of \(\mathbb F_2^3\) with labels \(1,\ldots,7\), using bitwise addition. Let \(c_v\) be the number of columns of type \(v\), so \(n=\sum_v c_v\).

## Proof
Fix a nonzero query \(q\) and ask for five copies of \(q\). Any recovery set of size at most two can be shrunk to a minimal one without destroying disjointness. A minimal recovery set is either a singleton column of type \(q\), or two distinct non-\(q\) column types \(u,v\) satisfying \(u+v=q\). The six types other than \(q\) split into three complementary pairs \(\{u,u+q\}\). Hence the maximum number of pairwise-disjoint locality-two recoveries for five equal queries is
\[
A_q=c_q+\sum_{\{u,v\}:u+v=q}\min(c_u,c_v).
\]
A five-request code must satisfy \(A_q\ge5\) for all seven nonzero \(q\). Summing over \(q\), every unordered pair of distinct nonzero types appears exactly once, so
\[
35\le \sum_q A_q=n+\sum_{u<v}\min(c_u,c_v).
\]

Suppose \(n\le10\). Adding arbitrary nonzero columns cannot decrease any \(A_q\), so it suffices to consider total multiplicity exactly \(10\). For seven nonnegative integer multiplicities summing to \(10\),
\[
\sum_{u<v}\min(c_u,c_v)\le24.
\]
One proof is by balancing: if two multiplicities differ by at least two, moving one unit from a larger coordinate to a smaller coordinate cannot decrease the sum of pairwise minima. Iterating reaches the balanced multiset \((1,1,1,1,2,2,2)\), where the sum is \(24\). Therefore \(\sum_q A_q\le10+24=34\), contradicting the required lower bound \(35\). Thus \(n\ge11\).

For the matching upper bound, take multiplicities \((1,1,1,2,2,2,2)\). For a query \(q\), the only minimal recovery choices of size at most two are the singleton \(\{q\}\) and the three complementary pairs summing to \(q\). The supplied exact verifier enumerates every multiset of five queries from the seven nonzero vectors and finds a capacity-respecting choice of five pairwise-disjoint recovery sets. There are exactly \(\binom{11}{5}=462\) such query multisets, so this is exhaustive. The displayed columns contain \((1,0,0),(0,1,0),(0,0,1)\), hence have rank three. Therefore an \([11,3,5,2]\) code exists, completing the proof.

## Verification
Run `python3 verify.py`. The verifier reconstructs the four minimal locality-two recovery options for every nonzero query, checks all \(462\) five-query multisets against the length-eleven witness, and independently enumerates all \(8008\) seven-part nonnegative integer compositions of \(10\). It confirms that the maximum pair-minimum sum at total \(10\) is \(24\), the maximum \(\sum_q A_q\) is \(34\), and no total-ten multiplicity vector passes all seven repeated-query necessities. As a supplemental check, it finds exactly \(77\) total-eleven multiplicity vectors passing the repeated-query test and verifies all \(77\) against all \(462\) query multisets.

## Relationship to prior work
Kılıç, Ravagnani, and Salizzoni study the unrestricted minimum length of functional batch and PIR codes, where recovery-set size is not capped. Tars's 2025 thesis reports by exhaustive search that the unrestricted binary functional-batch minimum at dimension \(3\) and five requests is \(10\). The present claim is therefore not a reformulation of that value: it shows that imposing locality two costs exactly one additional column at this parameter.

Oksner, Hollmann, Riet, and Skachek explicitly introduce \([n,k,t,r]\) functional batch codes with bounded recovery-set size and develop lower bounds for their minimum length. Their locality-two framework contains the present problem, but the inspected paper does not state the exact dimension-three, five-request value proved here. Its simplex discussion gives the dimension-three four-request locality-two construction of length seven and the doubled-simplex eight-request construction of length fourteen, making five requests the first intermediate request count beyond the simplex point.

## Limitations
The theorem is only for binary linear codes with dimension \(3\), five requests, and locality \(2\). It does not determine neighboring dimensions, larger locality, or the complete equivalence classification of optimal generator matrices. The exhaustive computation is finite and complete for the stated witness and total-ten multiplicity obstruction; it is not used to infer any unbounded family statement.

## References
1. A. B. Kılıç, A. Ravagnani, F. Salizzoni, “The Length of Functional Batch and PIR Codes,” arXiv:2508.02586, first public version 2025-08-04.
2. T. Tars, “Asymptotic Bounds on the Length of Functional Batch and PIR Codes,” University of Tartu bachelor's thesis, 2025, repository handle 10062/117012; repository availability 2025-10-23.
3. K. Oksner, H. D. L. Hollmann, A.-E. Riet, V. Skachek, “On the Minimum Length of Functional Batch Codes with Small Recovery Sets,” arXiv:2601.12302, first public version 2026-01-18.
