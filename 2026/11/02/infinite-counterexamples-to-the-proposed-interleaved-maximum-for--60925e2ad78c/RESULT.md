# Infinite counterexamples to the proposed interleaved maximum for consecutive-pattern packings

## Finding
For integers \(m\ge4\), let \(K=2m\). Define two permutations of \([2m]\) by concatenating the indicated increasing blocks:
\[
\begin{aligned}
\pi_m&=(1,3,4,7,9,11,\ldots,2m-1\ ;\ 2,5,6,8,10,\ldots,2m),\\
\tau_m&=(1,3,5,\ldots,2m-1\ ;\ 2,4,6,\ldots,2m).
\end{aligned}
\]
The semicolon marks the boundary after the first \(m\) entries and is not part of the permutation. At \(m=4\) these are \(\pi_4=(1,3,4,7,2,5,6,8)\) and \(\tau_4=(1,3,5,7,2,4,6,8)\).

For a length-\(2m\) permutation \(\rho\), let \(N_{\rho}^{m}(2)\) count permutations \(\sigma\) of \([3m]\) whose consecutive blocks in positions \(1,\ldots,2m\) and \(m+1,\ldots,3m\) both have relative order \(\rho\). Additional, unprescribed occurrences are allowed, exactly as in the pattern-packing convention in [1]. Then
\[
\boxed{N_{\pi_m}^{m}(2)=9\cdot2^{m-4},\qquad
N_{\tau_m}^{m}(2)=2^{m-1}.}
\]
Thus \(N_{\pi_m}^{m}(2)/N_{\tau_m}^{m}(2)=9/8>1\), for every \(m\ge4\). The family disproves the universally quantified maximizing assertion in Conjecture 7.1 of [1] in its two-occurrence case: the conjectured interleaved-minimal pattern \(\tau_m\) is not a maximizer. No claim is made here about which pattern actually maximizes the count.

## Assumptions and scope
A consecutive pattern is read in one-line notation. A word of distinct integers has relative order \(\rho\) when replacing its smallest entry by \(1\), its next smallest by \(2\), and so on yields \(\rho\). The patterns \(\pi_m\) and \(\tau_m\) are permutations of \([2m]\), and each has increasing prefix and suffix of length \(m\), so two prescribed occurrences overlapping in \(m\) positions are consistent. The result concerns labelled permutations of length \(3m\) with precisely two *prescribed* occurrences, not permutations with exactly two occurrences in total. The integer restriction is \(m\ge4\); the first counterexample has length \(K=8\) and overlap \(m=4\).

## Proof
**Two-chain interleaving lemma.** Suppose \(K=2m\), and a permutation \(\rho\in S_{2m}\) has both its first and last \(m\) entries in increasing order. Let \(P\) be its sorted prefix-value set and \(S\) its sorted suffix-value set; they partition \([2m]\). Define the gap vectors \(a=(a_0,\ldots,a_m)\) and \(b=(b_0,\ldots,b_m)\) as follows. For \(a_i\), count elements of \(P\) strictly between the \(i\)-th and \((i+1)\)-st elements of \(S\); for \(b_i\), count elements of \(S\) between the corresponding consecutive elements of \(P\). The sentinels are \(0\) and \(2m+1\), allowing \(i=0\) and \(i=m\). Then
\[
N_{\rho}^{m}(2)=\prod_{i=0}^{m}\binom{a_i+b_i}{a_i}.
\]
Indeed, the two prescribed occurrences each impose a total order on their \(2m\) positions. Their \(m\) shared positions appear in the same increasing order in both chains. Between consecutive shared positions, the first occurrence contributes a chain of \(a_i\) private positions and the second a chain of \(b_i\) private positions. There are no cross-chain comparisons within that gap, and the shared positions separate all gaps. The permissible orders in each gap are therefore exactly the \(\binom{a_i+b_i}{a_i}\) shuffles. Multiplying over the gaps counts all linear extensions of the union of the two chains. Assigning increasing labels \(1,\ldots,3m\) to a linear extension gives a unique permutation counted by \(N\), and conversely every counted permutation gives such a linear extension. This proves the lemma without invoking an enumeration theorem.

For the proposed extremal pattern \(\tau_m\), the prefix values are the odd numbers and the suffix values the even numbers. The gap vectors are
\[
a(\tau_m)=(\underbrace{1,\ldots,1}_{m},0),\qquad
b(\tau_m)=(0,\underbrace{1,\ldots,1}_{m}).
\]
The product has \(m-1\) nontrivial factors \(\binom21=2\), giving \(N_{\tau_m}^{m}(2)=2^{m-1}\).

For \(\pi_m\), the prefix-value set is \(\{1,3,4,7,9,11,\ldots,2m-1\}\) and the suffix is its complement \(\{2,5,6,8,10,\ldots,2m\}\). Directly counting between consecutive shared values yields
\[
\begin{aligned}
a(\pi_m)&=(1,2,0,\underbrace{1,\ldots,1}_{m-3},0),\\
b(\pi_m)&=(0,1,0,2,\underbrace{1,\ldots,1}_{m-3}).
\end{aligned}
\]
The only nonunit factors are \(\binom32=3\), \(\binom31=3\), and \(m-4\) copies of \(\binom21=2\). Therefore \(N_{\pi_m}^{m}(2)=9\cdot2^{m-4}\). Since \(9>8\), the displayed strict inequality holds for every \(m\ge4\). This completes the proof.

## Verification
A standalone standard-library script `verify.py` constructs each two-occurrence partial order directly from the original pattern inequalities. A memoized topological-order recurrence counts its linear extensions without using the gap factorization, while a separate implementation computes the latter formula. For each \(m\in\{4,5,6,7,8,9,10\}\), both methods return the claimed values. For \(m=4\), the script also explicitly generates all nine and eight labelled permutations, respectively, and checks both prescribed consecutive occurrences in each generated permutation. Running `python3 verify.py` prints `VERIFY_OK` on success. These finite checks corroborate the formulas but do not replace the all-\(m\) proof.

## Relationship to prior work
Blitvić, Kammoun, and Steingrímsson [1], arXiv version 1 dated October 21, 2026, define constant-overlap pattern packings and pose Conjecture 7.1: for overlap at most half the pattern length, the maximum count is attained when the prefix and suffix interleave in minimal ranks. At \(K=2m\), their proposed pattern is \(\tau_m\). Their general enumeration and poset methods provide background, but the asserted maximum is precisely what the explicit strict comparison contradicts. The present claim is **not** a denial of their general recurrences or their other results.

The authors' 2023 extended abstract [2] already developed general counting recurrences and the prefix/suffix dependence. Its accessible text states a different conjecture about moment sequences; it does not state the extremal Conjecture 7.1 addressed here. Dwyer and Elizalde [3] develop refined cluster and consecutive Wilf-equivalence theory but do not assert the maximizing claim. The independent two-chain proof above uses standard linear-extension counting and does not present that technique as new.

## Limitations
This refutes only the maximizing assertion of Conjecture 7.1, via its \(j=2\), \(K=2m\) subfamily. It does not find a true global maximizer, settle cases with more prescribed occurrences, or make any claim about the separate moment-sequence conjecture. The literature comparison is based on accessible primary relevant sections, bibliographic searches, and related full-text material; unindexed earlier counterexamples are still possible. No independent mathematical audit has been performed.

## References
1. N. Blitvić, M. S. Kammoun, and E. Steingrímsson, *Permutations, Pattern Covers, Posets and Positivity: Part I: Patterns and Posets*, arXiv:2610.29846v1, publicly posted 2026-10-21, especially Definition 2.6 and Conjecture 7.1, https://arxiv.org/html/2610.29846.
2. N. Blitvić, M. S. Kammoun, and E. Steingrímsson, *A new perspective on positivity in (consecutive) permutation patterns*, Séminaire Lotharingien de Combinatoire 89B (2023), Article 61, https://strathprints.strath.ac.uk/85045/.
3. T. Dwyer and S. Elizalde, *Wilf equivalence relations for consecutive patterns*, Advances in Applied Mathematics 99 (2018), 134–157, arXiv:1801.08262, https://arxiv.org/abs/1801.08262.
