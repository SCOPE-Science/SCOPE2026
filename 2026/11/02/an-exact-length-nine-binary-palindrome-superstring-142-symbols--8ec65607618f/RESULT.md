# An exact length-nine binary palindrome superstring: 142 symbols

## Finding
Let \(P_9\) be the set of all \(32\) binary palindromes of length \(9\). The minimum length of an ordinary finite linear binary word containing every member of \(P_9\) as a contiguous factor is exactly
\[
\boxed{142}.
\]
The minimum length of a circular binary word containing all those palindromes as cyclic length-nine factors is also exactly \(142\). In particular, the published candidate upper bound of \(142\) for the linear problem is sharp.

## Assumptions and scope
The alphabet is \(\{0,1\}\). Substring occurrences are exact, not approximate or scattered. Linear factors must lie entirely within the displayed finite word. Circular factors may cross its boundary and are indexed by starting positions modulo the circular length; two rotations are treated as the same circular word only for the purpose of discussing the minimum length, not as distinct occurrences. All \(32\) target palindromes are required, without allowing reversal substitution: each is already equal to its reversal. No restriction is placed on the nonpalindromic factors of the covering word.

Index the palindromes by \(i\in\{0,\ldots,31\}\): if the five-bit binary expansion of \(i\) is \(b_1b_2b_3b_4b_5\), write
\[
p_i=b_1b_2b_3b_4b_5b_4b_3b_2b_1.
\]
For distinct indices \(i,j\) define the directed overlap shift
\[
c_{ij}=\min\{s\in\{1,\ldots,9\}:p_i[s+1..9]=p_j[1..9-s]\}.
\]
An empty overlap, at \(s=9\), is permitted. Since all target words are palindromes, reversing a matching suffix-prefix overlap gives \(c_{ij}=c_{ji}\).

## Proof
**Lower bound, reduction to an overlap tour.** Suppose a circular word of length \(L\) contains all targets. Select one starting position for each of the \(32\) different palindromes and list the selected positions in cyclic order. They are necessarily distinct. If successive starts differ by a positive cyclic displacement \(\delta\), then \(c_{ij}\le\delta\): for \(\delta<9\), the two observed factors overlap consistently; for \(\delta\ge9\), the inequality follows from \(c_{ij}\le9\). The cyclic displacements sum to \(L\). Consequently \(L\) is at least the sum of the \(32\) edge costs along some Hamiltonian cycle of the complete palindrome-overlap graph.

**Integer lower-bound certificate.** Assign to indices \(0,\ldots,31\) the respective integer potentials
\[
(u_i)_{i=0}^{31}=(4,1,2,2,3,3,3,3,2,2,4,2,1,4,4,4,3,3,3,3,1,3,3,3,2,2,2,2,1,1,0,5).
\]
Direct evaluation of the \(496\) unordered costs gives \(\sum_i u_i=81\). For every unordered pair let \(e_{ij}=\max\{0,u_i+u_j-c_{ij}\}\). Only these seven \((i,j,e_{ij})\) triples have nonzero deficit:
\[
(4,17,4),\ (9,18,1),\ (10,21,6),\ (13,22,3),\ (14,27,4),\ (18,19,1),\ (19,25,1).
\]
Thus \(\sum_{i<j}e_{ij}=20\), and \(c_{ij}\ge u_i+u_j-e_{ij}\) for every distinct pair. A Hamiltonian cycle uses each vertex exactly twice and each unordered edge at most once. Its total cost is therefore at least
\[
2\sum_i u_i-\sum_{i<j} e_{ij}=2(81)-20=142.
\]
This establishes \(L\ge142\) for circular covers. A linear word containing every required factor is, when regarded as circular, also a circular cover of the same length, so the linear minimum is at least \(142\).

**Matching upper bound.** The following explicit binary word has length \(142\):

```text
0000000001000000011011000110101101101110111000001110001111100100111001010010010101000101000100010000010101010111110111111101011101010111111111
```

Directly scanning its ordinary (non-wrapping) length-nine substrings finds all \(32\) targets. It therefore proves the linear upper bound \(142\), and also proves the circular upper bound. Both minima equal \(142\).

## Verification
The standalone file `certificate.json` contains the \(32\) potentials, the seven nonzero deficits, and the construction witness. Running `python3 verify.py` reconstructs all targets, independently evaluates the \(496\) pair costs from their string overlaps, verifies the exact deficit list and lower-bound arithmetic, and checks all \(134\) ordinary length-nine windows of the witness. Running `python3 verify_independent.py` repeats the calculations using nine-bit integer shifts and a separate target enumeration. Both checks must complete successfully. These finite computations certify explicit exhaustive inequalities; no assumption about a solver's numerical optimality is needed.

## Relationship to prior work
Orenstein and Shamir (2013) optimally cover all DNA \(k\)-mers up to Watson–Crick reverse complementation. Their object is not the set of ordinary binary palindromes alone and their bounds do not imply this exact optimum. Fici et al. (2015) develop a general shortest-common-superstring method with reversal and discuss overlap graphs, but do not give the specified \(32\)-palindrome optimum. The OEIS entry A330022, introduced in 2019 and extended in 2025, lists \(142\) at order nine explicitly as a *greedy upper bound*, not a certified minimum; A390882 enumerates shortest superstrings only through order eight. The present result turns the order-nine upper bound into an equality using a small independent lower-bound certificate. The displayed \(142\) is not claimed as a newly discovered construction length.

## Limitations
Only the binary, length-nine all-palindromes instance is resolved here. No claim is made about order ten or larger, enumeration of all shortest words, or a uniform formula. The originality comparison depends on accessible indexed literature and may miss unpublished or unindexed proofs. The certificate checks a finite list of \(496\) explicit pairs and does not rely on unverified numerical optimization.

## References
- Y. Orenstein and R. Shamir, “Design of shortest double-stranded DNA sequences covering all k-mers with applications to protein-binding microarrays and synthetic enhancers,” *Bioinformatics* 29 (2013), i71–i79. https://doi.org/10.1093/bioinformatics/btt230 (first publicly verified date: 2013-06-19).
- G. Fici, T. Kociumaka, J. Radoszewski, W. Rytter, and T. Waleń, “On the Greedy Algorithm for the Shortest Common Superstring Problem with Reversals,” arXiv:1511.08431 (first submitted 2015-11-26). https://arxiv.org/abs/1511.08431.
- OEIS A330022, “Length of shortest binary string containing all palindromes of length n as substrings,” https://oeis.org/A330022 (entry introduced 2019-11-27, upper bound added 2025-11-22).
- OEIS A390882, “Number of shortest strings containing all binary palindromes of length n as substrings,” https://oeis.org/A390882 (2025-11-22; entries through order eight).
