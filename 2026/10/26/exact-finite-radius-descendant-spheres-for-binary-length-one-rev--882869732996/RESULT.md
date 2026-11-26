# Exact finite-radius descendant spheres for binary length-one reverse-complement duplication

## Finding

Let \(x\) be a nonempty binary word of length \(n\) with initial constant-run length \(r\). One operation inserts the binary complement of a chosen letter immediately after that letter. The set \(D_t(x)\) of distinct outputs after exactly \(t\) operations satisfies
\[
|D_t(x)|=\sum_{j=0}^t\binom{n+t-1}{j}-\sum_{j=0}^{t-1}\binom{n+t-r-1}{j}\qquad(n\ge1,\ t\ge0),
\]
where the second sum is empty when \(t=0\). A word \(y\) is reachable exactly when it begins with the same bit as \(x\), contains \(x\) as a scattered subsequence, and its initial constant run is no longer than that of \(x\). The subsequence condition entails \(|y|\ge n\); the number of operations is then \(|y|-n\).

In particular, \(|D_1(x)|=n\) and \(|D_2(x)|=n(n+1)/2+r\). For \(t\ge2\) the size increases strictly with \(r\) at fixed \(n,t\). Thus constant seeds maximize it, and seeds beginning with unequal bits minimize it for \(n\ge2\). For each fixed \(x\),
\[
\lim_{t\to\infty}\frac{|D_t(x)|}{2^{n+t}}=\frac{1-2^{-r}}{2}.
\]

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\), complementation interchanges the symbols, the seed is nonempty, and different histories with the same output count only once. The result does not address longer duplication blocks, larger alphabets, inverse parent multiplicities, or optimal codes.

## Proof

**Reachability.** An insertion cannot change the first bit, destroy the old word as a subsequence, or lengthen its initial constant run. Conversely, assume the three claimed conditions, and use induction on \(|y|-n\), with equality of lengths forcing \(y=x\). Choose a subsequence embedding that uses every letter of the first run of \(y\). This can be done by moving the first \(r(y)\) matches to the first \(r(y)\) positions: these have the right value because \(r(y)\le r\) and the first bits agree. Within every later run, right-justify the matches in that run, preserving their order and all matches in other runs.

If \(|y|>n\), let the rightmost run with an unmatched letter be the chosen run. It is not the first run. By right justification its first letter is unmatched, so it may be deleted: it immediately follows its complement. The original embedding survives. The only deletion that could increase the initial run length is deletion of the singleton second run when a third run exists. In this case all positions in the first and third runs are matched, and their matches form an initial constant block in \(x\); their combined length is at most \(r\). The shorter word therefore still meets all the conditions. Applying the induction and reversing the deletion gives the desired insertion sequence.

**Counting.** Let \(S(M,H)\) be the number of binary words of length \(M\) containing any fixed target of length \(H\) as a subsequence. Then \(S(M,H)=\sum_{j=H}^M\binom Mj\), with \(S(M,0)=2^M\). Extend the target by an arbitrary infinite binary tail and greedily match its symbols while scanning independent fair bits. Each new greedy match indicator is a fair coin conditionally on all preceding bits, so the indicators are independent; the first \(H\) symbols are matched exactly when there are at least \(H\) successes.

Write \(m=n+t\). Fixing and using the first letter of \(y\) leaves \(S(m-1,n-1)\) candidates. For \(t\ge1\), a forbidden candidate has at least \(r+1\) copies of the first bit at the start. With those \(r+1\) letters fixed, greedy embedding matches the initial \(r\) seed bits there; if \(r<n\), the extra letter cannot match the next seed bit. The suffix therefore contributes \(S(m-r-1,n-r)\), including the empty-target case \(r=n\). For \(t=0\) the only candidate is \(x\), which is allowed. Subtracting and using binomial symmetry gives the two sums in the finding.

**Consequences.** Evaluating at \(t=1,2\) gives the stated expressions. When both \(r\) and \(r+1\) are admissible and \(t\ge2\), Pascal's identity shows that the forbidden sum decreases by \(\sum_{j=0}^{t-2}\binom{n+t-r-2}{j}>0\). For the limit use the complementary tails, valid for \(t\ge1\):
\[
|D_t(x)|=2^{m-1}-2^{m-r-1}-\sum_{j=0}^{n-2}\binom{m-1}{j}+\sum_{j=0}^{n-r-1}\binom{m-r-1}{j}.
\]
Empty tails are zero. The tails are polynomials of bounded degree in \(m\) for fixed \(n,r\) and vanish after division by \(2^m\) in the limit. The powers of two give \((1-2^{-r})/2\).

## Verification

Run `python verify.py` with Python 3.9 or later and the standard library. It directly enumerates distinct descendants for all binary seeds of lengths 1 through 8 and exact radii 0 through 4, and tests the inverse-deletion property for all admissible pairs of target length at most 10. The documented markers are `RC1_DESCENDANTS_PASS seed_radius_cases=2550 candidate_targets=2708780` and `RC1_INVERSE_LEMMA_PASS admissible_pairs=84490`. These finite checks supplement the proof.

## Relationship to prior work and limitations

Ben-Tolila and Schwartz [1, Theorem 4 and proof] give a per-letter language factorization of the unbounded descendant cone and show full expressiveness for the binary channel. The factorization already characterizes reachable words and is not claimed as new here. The contribution is the explicit distinct per-seed cardinality for every exact radius, not a count of factorizations or insertion histories. Yohananov and Schwartz [2, Lemma 2 and Corollary 3] give an unbounded common-descendant criterion rather than this per-seed fixed-length count. Neither the standard binary supersequence count nor separate low-radius evaluations are claimed as new. An equivalent all-radius enumeration elsewhere remains possible.

## References

1. E. Ben-Tolila and M. Schwartz, *On the Reverse-Complement String-Duplication System*, arXiv:2112.11811v1.
2. L. Yohananov and M. Schwartz, *Optimal Reverse-Complement-Duplication Error-Correcting Codes*, arXiv:2312.00394v1 (later title: *On the Coding Capacity of Reverse-Complement and Palindromic Duplication-Correcting Codes*).
