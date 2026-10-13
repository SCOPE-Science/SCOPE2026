# Exact reset thresholds for cyclic automata with a successor-chain letter

## Finding
For every pair of integers \(n\ge3\) and \(2\le k\le n-1\), let \(\mathcal A_{n,k}\) be the deterministic two-letter automaton on \(Q=\{0,1,\ldots,n-1\}\) with
\[
a(i)=i+1\pmod n,\qquad
b(i)=\begin{cases}i+1,&0\le i<k,\\i,&k\le i<n.\end{cases}
\]
Here \(b\) has rank \(n-1\), with a transient successor chain \(0\to1\to\cdots\to k\) and fixed points \(k,\ldots,n-1\). The least length \(R(n,k)\) of a word mapping every state to a single state is exactly
\[
\boxed{R(n,k)=n\left(\left\lceil\frac{n-1}{k}\right\rceil-1\right)+k.}
\]
Writing \(n-1=qk+r\), with \(q\ge1\) and \(0\le r<k\), a shortest reset word is
\[
w=\begin{cases}
(b^k a^{n-k})^{q-1}b^k,&r=0,\\
b^r a^{n-r}(b^k a^{n-k})^{q-1}b^k,&1\le r<k.
\end{cases}
\]
Powers denote repetitions of letters, products act on states from left to right, and the exponent zero means the empty word. For each fixed \(k\), \(R(n,k)=n^2/k+O_k(n)\). For \(k\) proportional to \(n\), the threshold is linear in \(n\).

## Assumptions and scope
All states and transitions above are total and deterministic. A reset word is measured in individual occurrences of \(a\) and \(b\), not in grouped powers. The complete arithmetic formula applies to all specified integers, including \(k=n-1\), when \(b^{n-1}\) is a reset word. The excluded endpoint \(k=1\) recovers the classical Černý threshold \((n-1)^2\), so no novelty is asserted at that endpoint. Only the explicitly defined two-parameter family is classified, not all rank-\(n-1\) cyclic automata.

## Proof
**1. Inverse images remain cyclic intervals.** Read a reset word backward, starting from its final singleton \(\{j\}\). Write \(A(I)=a^{-1}(I)\), \(B(I)=b^{-1}(I)\). A *cyclic interval* is a set \(\{s,s+1,\ldots,s+h-1\}\pmod n\), where \(1\le h\le n\). Clearly \(A(I)=I-1\) is a cyclic interval. The map \(b\), represented on the line \(0,\ldots,n-1\), is nondecreasing: it sends \(0,\ldots,k-1\) to \(1,\ldots,k\), fixes \(k,\ldots,n-1\), and never outputs \(0\). Therefore the inverse image of any ordinary interval is an ordinary interval or empty, and the inverse image of a cyclic interval, which is an initial segment united with a terminal segment or an ordinary segment, is again a cyclic interval or empty. Empty sets cannot lead to a full preimage.

**2. Exact dominance of the two inverse moves.** For a nonempty proper cyclic interval \(I\), if \(k\in I\) and \(0\notin I\), it has the ordinary form \(I=[L,R]\) with \(1\le L\le k\le R<n\), whence direct calculation gives
\[
A(I)=[L-1,R-1]\subseteq [L-1,R]=B(I).
\]
In every other case, \(B(I)=I\) or \(B(I)\subseteq A(I)\). Indeed, for \(i<k\), \(a(i)=b(i)=i+1\). A point of \(B(I)\setminus A(I)\), if any, must consequently be an \(i\ge k\) belonging to \(I\) whose successor is outside \(I\). It is the unique terminal point of the cyclic interval. If that terminal point is \(\ge k\) while \(I\) is not of the preceding ordinary form, then either \(I\) avoids \(\{0,\ldots,k\}\), or \(I\) contains the whole set \(\{0,\ldots,k\}\); in either case, no change occurs under \(B\), so \(B(I)=I\). When its terminal point is below \(k\), every point of \(B(I)\) is in \(A(I)\), proving the assertion.

Preimages preserve inclusion: \(I\subseteq J\) implies \(v^{-1}(I)\subseteq v^{-1}(J)\) for every word \(v\). Consequently, when \(k\in I\) and \(0\notin I\), choosing \(B\) is never worse than choosing \(A\); otherwise, choosing \(A\) is never worse than \(B\), unless \(B(I)=I\), in which case a \(B\)-step is idle and cannot occur in a shortest expansion. Replacing the first inverse operation of any successful expansion by the indicated move preserves eventual coverage in the same number of steps; induction proves the *greedy inverse rule* gives a shortest expansion from each cyclic interval:
\[
\text{apply }B\text{ iff }k\in I\text{ and }0\notin I;\quad\text{otherwise apply }A.
\]

**3. The best initial singleton.** If \(j\ne k\), inverse \(B\) on \(\{j\}\) is either unchanged, empty, or equal to inverse \(A\); it never increases cardinality. Any successful expansion must first reach \(\{k\}\) by inverse rotations, after a positive number of steps. The singleton \(\{k\}\) therefore minimizes expansion length. At \(\{k\}\), exactly \(k\) consecutive greedy \(B\)-steps produce \([0,k]\). If \(k=n-1\), this already is the whole state set.

**4. Every later greedy phase.** Suppose the current set is \([0,m]\) with \(k\le m\le n-2\). It does not trigger \(B\). After \(t\) inverse \(A\)-steps, the first occasion on which \(0\notin I\) and \(k\in I\) is
\[
t=\max\{m+1,n-k\}.
\]
Indeed, \(t>m\) is required for the rotated interval to exclude zero, while \(t\ge n-k\) is required for its left endpoint to be at most \(k\); these conditions suffice and produce the interval \([n-t,n-t+m]\). Each following inverse \(B\)-step extends its left endpoint by one until the endpoint becomes zero (or all \(n\) states have been reached).

Write \(n-1=qk+r\), \(0\le r<k\). From \([0,k]\), the first \(q-1\) full phases have \(m=jk\), \(1\le j\le q-1\); here \(\max\{jk+1,n-k\}=n-k\), yielding the chain
\[
[0,jk]\ \xrightarrow{A^{n-k}}\ [k,(j+1)k]\ \xrightarrow{B^k}\ [0,(j+1)k].
\]
If \(r=0\), the set is full after the last full phase. If \(r>0\), a final phase starts at \([0,qk]=[0,n-r-1]\); it uses \(n-r\) inverse rotations and then \(r\) inverse \(B\)-steps:
\[
[0,n-r-1]\xrightarrow{A^{n-r}}[r,n-1]\xrightarrow{B^r}Q.
\]
Thus the minimal inverse length is
\[
k+(q-1)n+\begin{cases}0,&r=0,\\n,&r>0,\end{cases}
=n\left(\left\lceil\frac{n-1}{k}\right\rceil-1\right)+k.
\]
Reading the inverse-operation sequence in reverse order produces the forward reset word stated in the finding. Every shorter forward reset word would reverse to a shorter expansion of some singleton, contradicting Steps 2–4. This proves equality.

## Verification
The included standalone standard-library program `verify.py` computes exact shortest reset lengths by forward-subset breadth-first search for all \(3\le n\le16\), \(2\le k<n\), checks every nonempty proper cyclic interval and the dominance law for \(3\le n\le22\), and replays the explicit witnesses for \(17\le n\le60\). Running `python verify.py` returned:

`VERIFY_OK bfs_cases=105 bfs_states=1622619 interval_cases=53130 large_witnesses=1606`

These finite checks are independent corroboration only; the proof above supplies the infinite assertion. Counts are of tested parameter pairs, explored BFS subsets, tested inverse-interval cases, and larger witnesses respectively.

## Relationship to prior work
Rystsov and Szykuła (arXiv:2307.01302, §§3–4) study primitivity versus synchronizability, including semiconstant letters, but the present letter \(b\) is nonidempotent when \(k\ge2\), and their statements do not determine shortest reset words for this family. Zhu (arXiv:2407.08135, Theorem 1.4) proves the general bound \(2n^2-7n+7\) for synchronizing automata whose nonpermutation letters have rank at least \(n-1\) and whose permutation subgroup is transitive; those hypotheses hold here, but that upper bound is not the exact family-specific equality. Grech and Kisielewicz (arXiv:1207.2556, §4) cover orientable automata by the Černý bound, likewise without the present arithmetic equality. Don (2016, Proposition 15) gives synchronizability and a \((n-1)^2\) bound for circular one-deficient automata under a coprimality hypothesis, again not the present exact shortest-word length. The classical \(k=1\) specialization, and generic Černý upper bounds, are not claimed as original. Identically valued isolated parameters in other cyclic families do not imply identity of transformation maps or the two-parameter conclusion.

## Limitations
No general reset threshold is asserted for arbitrary automata containing a cyclic permutation and a rank-\(n-1\) letter. The formula does not classify all shortest words or all possible reset target states; it supplies a shortest witness and exact minimum length. A complete comparison with unindexed or unpublished literature is impossible, so an equivalent earlier presentation remains a priority risk. Verification over finitely many parameters is not an infinite proof.

## References
1. I. Rystsov and M. Szykuła, *Primitive Automata that are Synchronizing*, arXiv:2307.01302, first posted July 3, 2023; https://arxiv.org/pdf/2307.01302.
2. Y. Zhu, *A Quadratic Upper Bound on the Reset Thresholds of Synchronizing Automata Containing a Transitive Permutation Group*, arXiv:2407.08135, first posted July 11, 2024; https://arxiv.org/pdf/2407.08135.
3. M. Grech and A. Kisielewicz, *The Černý conjecture for automata respecting intervals of a directed graph*, arXiv:1207.2556, first posted July 11, 2012; https://arxiv.org/pdf/1207.2556.
4. H. Don, *The Černý conjecture and 1-contracting automata*, Electronic Journal of Combinatorics 23(3) (2016), P3.12; https://www.combinatorics.org/ojs/index.php/eljc/article/download/v23i3p12/pdf/.
5. J. Černý, *Poznámka k homogénnym experimentom s konečnými automatami*, Matematicko-fyzikálny Časopis 14 (1964), 208–216.
