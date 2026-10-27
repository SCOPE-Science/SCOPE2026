# Scientific review

## Correctness — PASS

The carry-state derivation accounts for every base-four choice of both summands and both possible carries, including the final no-carry condition and \(k=0\). Boolean determinization leaves exactly two accepting reachable states and a dead state, yielding an exact second-order recurrence for coverage. A bounded indicator invariant proves the unique-representation count without relying on empirical patterns. A sorted-coordinate Fibonacci induction, together with explicitly constructed digit words, proves both sides of the sharp maximum. A standalone verifier independently enumerates all representations for \(k\le7\) and checks state recurrences for \(k\le14\). The infinite proof does not rely on those cutoffs.

## Originality — PASS within inspected literature

OEIS A000695 records the familiar unique \(\mathcal M+2\mathcal M\) basis. The inspected text of Dekking's *Sumsets and fixed points of substitutions* (arXiv:2105.04959) proves sumset statements for other substitution-fixed sets but does not state the arithmetic theorem for \(\mathcal M+3\mathcal M\). The numerical coverage sequence is **not new**: OEIS A007052 contains the same recurrence and values in other combinatorial settings. That table does not identify the set \(\mathcal M+3\mathcal M\), the \(3^k\) unique-representation count, or the sharp Fibonacci maximum. Targeted digital-sumset literature searches and four relevant semantic record searches revealed no equivalent joint theorem; their top unrelated records do not themselves establish novelty. The strongest residual risk is an earlier unindexed dilation-three argument or an unstated corollary of a broader automatic-set theorem.

## Mathematical value — PASS

The classical set \(\mathcal M\) is a sparse exact additive basis after dilation by two. Replacing that coefficient with three destroys universal coverage and uniqueness in a precise, nontrivial way: the support grows at sharp exponent \(\log_4(2+\sqrt2)\), uniquely represented values grow at the smaller exponent \(\log_4 3\), and the maximum multiplicity grows at the Fibonacci rate. These three complementary invariants characterize the resulting arithmetic coverage/ambiguity transition rather than just identifying a familiar integer sequence. The result does not classify all dilations, and arbitrary cutoff asymptotic constants are not claimed.

## Closest literature and remaining risks

- Dekking, arXiv:2105.04959 (11 May 2021), discusses substitution sumsets, but not the specific dilation-three claims.
- OEIS A000695 records the Moser–de Bruijn digits and its unique dilation-two representation.
- OEIS A007052 records the already-known numerical coverage recurrence, but not its present interpretation or the two multiplicity laws.
- Some general carry-automaton treatment may implicitly subsume the calculations; priority needs human verification. No independent mathematical audit has been conducted.

Self-review: passed. Independent audit: not yet performed.
