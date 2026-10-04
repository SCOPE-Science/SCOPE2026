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

The finite verifier checks the weighted Euler-map arithmetic used in the proof.

For a weight quadruple
\[
a_0\le a_1\le a_2\le a_3,
\]
it builds the weighted monomial spaces \(P_k\) of the polynomial ring in four variables and the exact linear map
\[
\bigoplus_{i=0}^3P_{t-a_i}\longrightarrow P_t,
\qquad
(f_i)\longmapsto\sum_{i=0}^3 a_ix_if_i.
\]
Over the rationals it computes the kernel dimension.

For every nondecreasing quadruple with entries in \(\{1,\ldots,6\}\), the script verifies that the kernel is zero for every nonnegative
\[
t<a_0+a_1
\]
and is nonzero at
\[
t=a_0+a_1.
\]
This is a bounded consistency check. The proof for arbitrary positive weights is the regular-sequence/Koszul argument in `RESULT.md`.

For the explicit weights \((2,3,5,7)\), the script verifies kernel dimension zero in twists \(0\) through \(4\) and positive kernel in twist \(5\). It also checks that
\[
210>2+3+5+7
\]
and that the exponents \(105,70,42,30\) all give weighted degree \(210\).

The script does not replace the geometric inputs: the weighted Euler and conormal exact sequences, line-bundle cohomology on the quasi-smooth hypersurface stack, or the stack-to-coarse identification of reflexive differentials.

The saved replay output ends in `VERIFY_OK`.
