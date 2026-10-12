# Self-review

## Correctness
**PASS.** For a committee \(W_c=C\setminus\{c\}\), every voter either loses no approved candidate or loses exactly \(c\). In the second case, both SAV and PAV lose exactly \(1/|A_i|\) relative to their respective voter-specific baselines. Summation gives
\[
\operatorname{SAV}(W_c)=n-s(c)
\]
and
\[
\operatorname{PAV}(W_c)=\sum_i H_{|A_i|}-s(c).
\]
Thus the complete score vectors differ by a committee-independent constant. The packaged exact-arithmetic verifier independently checks the identities and \(57160\) small profiles.

Risk: the equivalence is only for one-vacancy committees.

## Originality
**PASS.** The inspected primary full text defines SAV and PAV together and proves general PAV winner determination NP-hard, but does not state the one-vacancy identity. Targeted searches using \(m-1\), all-but-one, near-full committee, and exact SAV/PAV winner-equivalence formulations did not locate equivalent coverage. The claim is not the generic observation that the rules can sometimes agree; it gives an exact profile-independent equality of all pairwise committee-score differences.

Risk: failed search does not prove bibliographic uniqueness. A handbook exercise, implementation optimization, or unindexed note could contain the same algebraic simplification.

## Value
**PASS.** SAV and PAV are prominent approval-based committee rules with different general objectives and very different winner-determination complexity. The theorem identifies a natural nontrivial boundary regime—electing everyone except one candidate—where PAV collapses exactly to the polynomial SAV ranking. This gives both an interpretive simplification and a direct tractable winner rule, rather than an arbitrary finite coincidence.

Self-review: passed. Independent audit: not yet performed.
