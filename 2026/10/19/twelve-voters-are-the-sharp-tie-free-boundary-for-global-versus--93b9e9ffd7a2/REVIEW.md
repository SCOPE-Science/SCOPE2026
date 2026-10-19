# Scientific review: sharp tie-free PAV divergence

## Correctness — PASS

The stated theorem is about exactly three candidates, two seats, seven nonempty ballot types, a unique global PAV committee, and unique choices in both forward greedy rounds. Direct score comparison gives the exact integer identity \(n=3a+3d_B+3d_C+4+2u+2v+3z+w\), with \(d_B,d_C\ge1\) and all remaining variables nonnegative. The remaining greedy marginal-score difference is \((v-u)/2\), so strictness demands \(u\ne v\), forcing \(n\ge12\). Equality fixes all ballot multiplicities up to relabeling; universal-approval voters extend the witness to every larger electorate. A separate direct-score enumeration verified all 50,387 anonymous profiles with up to twelve voters. The proof, not the finite program, establishes the unbounded theorem.

## Originality — PASS, with priority qualifications

The existence of PAV/seq-PAV divergence and the underlying ten-voter nonmonotonicity example are known. In particular, Lackner and Skowron's Appendix A Proposition A.2 gives precisely the earlier ten-voter pattern up to relabeling, which contains a greedy second-round tie, while their Example 2.5 illustrates a larger global/greedy difference. Janeczko and Faliszewski study ties and their computational complexity; Dong and Lederer characterize sequential rules. The assessed claim is only the **first tie-free** discrepancy at twelve voters, its complete six-profile classification, and existence at each larger size. No covering statement was identified in the inspected works or searched research records. A broader enumeration could nevertheless subsume it, so independent priority checking is still warranted.

## Mathematical value — PASS

Tie-breaking is a genuine methodological issue when comparing voting rules; a strict disagreement cannot be dismissed as an arbitrary tie resolution. The theorem supplies the sharp electorate threshold for the smallest nontrivial candidate/seat setting, identifies the entire minimal boundary and gives a compact exact regression example. Its integer normal form explains why eliminating the greedy tie necessarily costs two more voters beyond the established ten-voter example, rather than merely constructing another arbitrary profile.

## Scope and residual limitations

No conclusion is asserted for four or more candidates, other committee sizes, voter weights, blank ballots, different Thiele weights or reverse elimination. Mathematical verification of the finite example does not establish literature priority. An external independent audit has not been conducted.

Self-review: passed. Independent audit: not yet performed.
