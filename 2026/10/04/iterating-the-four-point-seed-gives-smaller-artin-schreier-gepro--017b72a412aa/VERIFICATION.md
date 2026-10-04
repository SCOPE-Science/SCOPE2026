---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The verifier checks the arithmetic recurrence behind both families.

For each prime
\[
3\le p\le97
\]
and each
\[
4\le n\le30,
\]
it builds the type
\[
(2,2,p,p^2,\ldots,p^{n-3}),
\]
checks that its regularity
\[
\sum(d_i-1)
\]
is at most
\[
p^{n-2}-1,
\]
and therefore that the next orbit size used in the induction satisfies the published lifting theorem's surjectivity bound. It checks the point-count identity
\[
\prod d_i=4p^{(n-3)(n-2)/2}
\]
and verifies strict coordinatewise comparison with
\[
(3,p,p^2,\ldots,p^{n-2}).
\]

For characteristic \(2\), it performs the same checks for
\[
(2,2,4,8,\ldots,2^{n-2}),
\]
including the exact regularity identity
\[
\sum(d_i-1)=2^{n-1}-n+1
\]
and the point-count formula
\[
\prod d_i=2^{(n-2)(n-1)/2+1}.
\]
It verifies strict coordinatewise comparison with
\[
(3,4,8,\ldots,2^{n-1}).
\]

The script also checks the claimed ratios between the published and new cardinalities.

These finite checks do not replace the all-dimensional induction or the geometric Artin--Schreier lifting theorem. The mathematical proof is given in `RESULT.md`.

The saved replay output ends in `VERIFY_OK`.
