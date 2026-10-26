# Eulerian strategy thresholds and the complete minimal antichain for unanimous \(\rho\)-Naples parking

## Finding
Fix any integers \(n\ge1\) and \(1\le m\le n\). For the unanimous parking preference \(\alpha=(m,m,\ldots,m)\), the complete successful-strategy upset, its entire antichain of componentwise-minimal elements, and its cardinality admit explicit descriptions.

For any parking strategy \(\rho=(r_1,\ldots,r_n)\), with \(0\le r_i\le i-1\), set \(b_1=0\) and, for \(i\ge2\),
\[
b_i=b_{i-1}+\mathbf 1_{\{r_i\ge b_{i-1}+1\}}.
\]
The following conditions are equivalent:

1. All cars park using \(\rho\).
2. \(b_n\ge m-1\).
3. There are indices \(2\le i_1<\cdots<i_{m-1}\le n\) such that \(r_{i_j}\ge j\) for every \(1\le j\le m-1\).

For each index set \(I=\{i_1<\cdots<i_{m-1}\}\), let \(\rho^I\) have coordinate \(j\) at index \(i_j\) and zero elsewhere. **The entire set of componentwise-minimal successful strategies** is \(\{\rho^I:|I|=m-1\}\); its size is
\[
\binom{n-1}{m-1}.
\]
All these minimal strategies have the same total quota \(\binom m2\). In particular, the realized upset can have exponentially many incomparable minimal elements when \(m\) is near the middle of the allowed range.

If \(\left\langle {n\atop k}\right\rangle\) denotes the Eulerian number of permutations of \(n\) with exactly \(k\) descents, the full successful-strategy count is
\[
|\mathcal F_{n,m}|=\sum_{k=m-1}^{n-1}\left\langle {n\atop k}\right\rangle.
\]
In fact there is an explicit bijection from all \(n!\) strategy vectors to permutations under which the statistic \(b_n\) becomes the ordinary descent count. For \(n=1\), the formula gives the unique zero strategy; the empty index set is understood when \(m=1\).

## Assumptions and scope
Cars \(1,2,\ldots,n\) arrive in that order at \(n\) numbered spaces. Each car first tries space \(m\). If occupied, it checks preceding spaces \(m-1,m-2,\ldots,m-r_i\) in decreasing order, stopping at the first vacant space that is actually on the street. If none is free, it moves forward from \(m+1\) and takes the first free space. It fails only if neither search finds a space. These are the individual-quota rules in Ferrari--Verciani, arXiv:2610.20267v1. The natural strategy set is \(\Delta_n=\prod_{i=1}^n\{0,\ldots,i-1\}\), ordered coordinatewise. No extra hypothesis is imposed on \(n\), \(m\), or the strategy.

## Proof
**1. Interval invariant and exact success threshold.** Car \(1\) occupies \(m\). After any successful prefix of cars, all occupied spaces form a contiguous interval \([m-L,m+F]\), where \(L\) and \(F\) are the numbers of occupied spaces to the left and right of \(m\). Thus \(L+F=i-1\) after \(i\) successful cars. If \(L<m-1\) and another car arrives, its first free backward space is \(m-L-1\), so the car extends the interval to the left **exactly when** \(r_i\ge L+1\). Otherwise it extends the interval to the right when \(F<n-m\), and fails when the right side is already full. As long as the first \(i\) cars succeed and \(L<m-1\), the recurrence defining \(b_i\) therefore tracks the left-occupation count, until the left side is filled.

If the process succeeds completely, all \(m-1\) left spaces are filled, forcing \(b_n\ge m-1\). Conversely, suppose the first failure occurs at car \(i\), with \(L<m-1\) left spaces filled, \(F=n-m\) right spaces filled, and inadequate backward quota. Then \(i-2=L+(n-m)\), so \(n-i=m-L-2\). The greedy statistic at the failure is \(b_i=L\); even granting it one increment at every remaining index, it obeys \(b_n\le L+(n-i)=m-2\). Hence failure implies \(b_n<m-1\). This proves the first equivalence, including the boundary case \(m=1\) where success is automatic.

**2. Greedy subsequences and the complete minimal antichain.** The recurrence increments \(b_i\) whenever \(r_i\) reaches the next required threshold. If it reaches \(m-1\), record the first indices \(i_1<\cdots<i_{m-1}\) at which increments \(1,\ldots,m-1\) occur. Then \(r_{i_j}\ge j\). Conversely, given such a subsequence, the greedy counter has reached at least \(j\) by index \(i_j\), inductively: it either already exceeds \(j-1\), or the quota \(r_{i_j}\ge j\) supplies the next increment. Thus the subsequence test is equivalent to success.

Every successful strategy dominates at least one \(\rho^I\) componentwise. Conversely, every such vector meets the subsequence test, so is successful. Distinct \(\rho^I\) have different supports of the same size \(m-1\), and therefore cannot be coordinatewise comparable. The successful set is exactly their union of principal up-sets, and these vectors are exactly its minimal elements. Their count is \(\binom{n-1}{m-1}\), and their sum of quotas is \(1+\cdots+(m-1)=\binom m2\).

**3. Eulerian distribution.** Let \(f_{i,k}\) count the first \(i\) quota entries with greedy statistic equal to \(k\). Initially \(f_{1,0}=1\). Extending a length-\(i-1\) strategy with score \(k\) gives \(k+1\) admissible new quotas \(r_i\in\{0,\ldots,k\}\) that leave the score unchanged, and \(i-k-1\) quotas that increase it by one. Hence
\[
f_{i,k}=(k+1)f_{i-1,k}+(i-k)f_{i-1,k-1},
\]
with out-of-range entries zero. This is precisely the Eulerian recurrence for descents. Thus \(f_{n,k}=\left\langle {n\atop k}\right\rangle\) and summing over \(k\ge m-1\) counts all successful strategies.

For an explicit statistic-preserving bijection, begin with the permutation \([1]\). Given the permutation on \(i-1\) elements having \(k\) descents, insert the new maximum \(i\) into one of its \(i\) gaps. Exactly \(k+1\) gaps (after each descent and after the final element) preserve the number of descents, while the remaining \(i-k-1\) gaps (at the beginning and after each ascent) increase it by one. Assign quotas \(0,\ldots,k\) bijectively to the preserving gaps in left-to-right order, and the remaining quotas \(k+1,\ldots,i-1\) to the increasing gaps in left-to-right order. Removing the largest element reverses every insertion step, so this is a bijection and takes \(b_n\) exactly to the permutation's descent count.

## Verification
The accompanying standalone standard-library script `verify.py` independently simulates the physical parking process, directly enumerates all \(n!\) strategies for each \(1\le n\le8\), tests all preference positions \(m\), and checks the greedy criterion, the full componentwise-minimal antichain, Eulerian frequencies, and the insertion bijection. It also checks the Eulerian recurrence and symmetry for \(n\le100\). Its recorded output ends in `VERIFY_OK`. For example, with \(n=8\), the exact success counts for \(m=1,\ldots,8\) are \(40320,40319,40072,35779,20160,4541,248,1\). These finite checks corroborate the proof; the proof, not the enumeration, establishes all orders.

## Relationship to prior work
Ferrari and Verciani (2026, arXiv:2610.20267v1) introduce the individual-quota model and establish upward closure for every preference. Their Theorem 5.4 characterizes strategies minimizing **total** backward quota; for unanimous preferences this includes the min-total profiles identified here. The present theorem makes the stronger complete statement that there are *no other componentwise-minimal profiles* for this preference and, independently, gives the exact full successful up-set and its Eulerian-tail enumeration and permutation bijection. Their Section 8 explicitly highlights describing all minimal elements and finding permutation links as open avenues. The earlier homogeneous-backward-limit literature (Ferrari and Verciani, arXiv:2405.07522) concerns a different rule with a common bound for cars and does not give this variable-quota formula. The Eulerian recurrence itself is classical; the new statement is its application through a concrete statistic-preserving correspondence in this parking model.

## Limitations
The uniform-preference restriction is essential to this argument; no classification is asserted for arbitrary nonconstant parking preferences. The insertion bijection is a deliberately constructed encoding, not a claim about the descent statistic of a pre-existing canonical inversion-sequence encoding. Bibliographic novelty is based on the inspected accessible sources and may be affected by unindexed results. The verification is finite and not independent expert validation.

## References
1. L. Ferrari and F. Verciani, *A new generalization of parking functions: \(\rho\)-Naples parking functions*, arXiv:2610.20267v1 (first posted 2026-10-14), https://arxiv.org/html/2610.20267v1 ; sections 3--8, especially Theorem 5.4 and Section 8.
2. L. Ferrari and F. Verciani, *A new approach to Naples parking functions through complete parking preferences*, arXiv:2405.07522 (2024), https://arxiv.org/abs/2405.07522 .
3. Classical Eulerian descent recurrence, as established by insertion of the new maximum in a permutation; proved again here to identify the exact relationship.
