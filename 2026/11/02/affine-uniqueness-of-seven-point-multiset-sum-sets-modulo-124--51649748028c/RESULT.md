# Affine uniqueness of seven-point multiset-sum sets modulo 124

## Finding
Let \(A\) be a seven-element subset of \(\mathbb Z/124\mathbb Z\). Call \(A\) *valid* if among the nonnegative integer multiplicity vectors \((m_a)_{a\in A}\) with \(\sum_{a\in A}m_a=7\), precisely the all-ones vector satisfies
\[
\sum_{a\in A}m_a a\equiv\sum_{a\in A}a\pmod{124}.
\]
Then \(A\) is valid **if and only if**
\[
A=\{u c+b\pmod{124}:c\in\{0,1,3,7,15,31,63\}\},
\quad \gcd(u,124)=1.
\]
Consequently exactly \(7440\) distinct seven-element subsets are valid, constituting one orbit under the affine unit group. Among sets containing \(0\) and \(1\), precisely ten are valid; all ten are in `normalized_valid.txt`.

## Assumptions and scope
All residues, subsets, congruences, and affine actions in this theorem are in the cyclic additive group \(\mathbb Z/124\mathbb Z\), and elements within \(A\) are distinct. Repetition is allowed only in the candidate seven-term multisets. Two subsets are affinely equivalent when one is the image of the other under \(x\mapsto ux+b\) with \(u\) invertible modulo \(124\). No assertion about different moduli, other cardinalities, or absolute minimum modulus among arbitrary seven-point subsets is made here.

## Proof
**1. The dissociation obstruction.** Affine translation of all seven distinct residues does not change validity: both the target sum and every seven-term candidate sum increase by \(7b\). Similarly scaling by a unit preserves equality of such sums. Translate a given valid set to contain \(0\). Its other six members have \(2^6=64\) distinct subset sums modulo \(124\). Indeed, if different subsets have equal sums, delete their intersection to find disjoint subsets \(P,Q\), not both empty, with equal sums; interchange them so that \(|P|\le |Q|\). In the all-ones seven-term multiset, remove one occurrence of each member of \(Q\), insert an additional occurrence of each member of \(P\), and insert \(|Q|-|P|\) further zeroes. The resulting seven-term multiset is not the all-ones multiset, but has the same sum. This contradicts validity.

**2. A unit difference is mandatory.** Suppose no difference between two elements of \(A\) is a unit modulo \(124=4\cdot31\). If all seven have the same parity, translate one member to zero. Every subset sum of the remaining six belongs to the subgroup of even residues, which has size \(62<64\), contradicting step 1. Otherwise there are elements of both parities. Every cross-parity difference is odd and, by assumption, a nonunit; hence every such difference is divisible by \(31\). Fix one element of either parity to conclude every element of \(A\) is congruent to the same residue modulo \(31\). There are only four residues in \(\mathbb Z/124\mathbb Z\) with a given value modulo \(31\), contradicting \(|A|=7\). Therefore \(A\) has a pair with unit difference. Translate the first element to \(0\) and multiply by the inverse difference to send the second to \(1\).

**3. Complete normalized census.** Every valid set is consequently affine-equivalent to exactly one of the candidates
\[
\{0,1,b,c,d,e,f\},\qquad 2\le b<c<d<e<f\le123.
\]
There are \(\binom{122}{5}=207288004\) candidates. The standalone file `enumerate_direct.cpp` iterates through all of them with explicit strictly increasing loops, creates all \(64\) subset sums of the six nonzero members using integer arithmetic modulo \(124\), discards any set with repeated subset sums, then enumerates the \(\binom{13}{6}=1716\) nonnegative seven-coordinate vectors of sum seven (apart from the all-ones vector) and tests equality to the target. This exhaustive finite loop finds \(5192384\) subset-sum-injective sets and precisely ten valid sets. Their exact, sorted coordinates are:
\[
\begin{gathered}
(0,1,3,7,15,31,63),\quad(0,1,5,21,83,85,93),\\
(0,1,9,71,73,89,93),\quad(0,1,17,25,29,91,93),\\
(0,1,32,34,96,100,108),\quad(0,1,32,36,52,54,116),\\
(0,1,32,40,42,104,120),\quad(0,1,32,48,56,60,62),\\
(0,1,62,94,110,118,122),\quad(0,1,63,65,69,77,93).
\end{gathered}
\]
A second implementation in `enumerate_pruned.cpp` uses a \(124\)-bit cyclic subset-sum recurrence to reject collisions during construction and independently rechecks the full seven-multiset condition. It yields precisely the same ten lines. The pruning condition is necessary by step 1; no candidate failing it can be valid.

**4. Orbit exhaustion.** The group of affine units modulo \(124\) has order \(124\varphi(124)=124\cdot60=7440\). `verify_affine.py` independently enumerates all \(7440\) transformations of the canonical set \(C=\{0,1,3,7,15,31,63\}\), finding \(7440\) distinct images (trivial set stabilizer). Exactly ten orbit images contain \(0\) and \(1\), and their complete coordinate list equals the ten normalized valid sets from step 3. The program also directly verifies the multiset condition for all ten. Since validity is affine-invariant, every orbit image is valid. Conversely, every valid set normalizes to one of these orbit members by steps 1–3, completing both directions and the cardinality formula.

## Verification
The package contains `enumerate_direct.cpp` (an exhaustive independent direct implementation), `enumerate_pruned.cpp` (a cyclic-bitset filtered implementation), `normalized_valid.txt` (the ten normalized subsets), and `verify_affine.py` (orbit enumeration and an independent seven-multiset check). Compile each C++ file with g++ in C++17 mode (the fast enumerator uses a 128-bit integer extension), run both, compare their standard-output lists to `normalized_valid.txt`, and run `python3 verify_affine.py` in the same directory. The direct program reports `all_combinations=207288004 subset_distinct=5192384 valid=10`; the pruned program reports `leaf=5192384 valid=10`; the orbit checker reports `ORBIT_OK orbit=7440 normalized=10 canonical_stabilizer=1`. These are exhaustive computations over a *fixed finite domain*, not sampled evidence or an assertion about unbounded moduli.

## Relationship to prior work
Fonollosa introduced the unique multiset-sum condition and proved that the canonical superincreasing set first works at modulus \(2^n-2^{\lfloor\log_2 n\rfloor}\). For \(n=7\) this is \(124\). The source discusses computational observations about equivalence of optimal sets, without providing a complete certification of all valid seven-subsets at \(124\). The present classification proves that equivalence and gives the exact number of subsets for this specified modulus. Inal's later finite-abelian-group minimum-order result concerns the smaller unrestricted group-order threshold and does not classify all valid seven-subsets in the cyclic group of order \(124\). The classical two-summand unique-sum problem of Bedert uses a distinct representation condition.

## Limitations
The proof of normalized uniqueness includes two reproducible finite exhaustive enumerations over \(207288004\) candidates; it does not replace them with a closed-form structural classification. It establishes no analogous statement for \(n>7\) or any other modulus. Prior work may contain an unindexed implicit proof of this particular affine uniqueness result; independent priority review remains appropriate. The companion Fourier/permanent paper was identified but its entire body was not available for inspection, leaving a bounded literature-comparison risk.

## References
1. José A. R. Fonollosa, *Minimum modulus for the unique multiset-sum problem*, arXiv:2607.08366v1 (first public July 9, 2026), revised v2 July 14, 2026, https://arxiv.org/abs/2607.08366.
2. José A. R. Fonollosa, companion paper on permanent evaluation by Fourier transforms, arXiv:2607.09949, https://arxiv.org/abs/2607.09949 (abstract-level relevance; body not fully inspected).
3. Michael Inal, *The Exact Minimum Order for Unique Multiset Sums in Finite Abelian Groups* (2026), described in https://github.com/jarfo/min-modulus.
4. Benjamin Bedert, *On Unique Sums in Abelian Groups*, Combinatorica 44 (2024), 269–298, https://doi.org/10.1007/s00493-023-00069-w.
