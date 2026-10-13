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

The universal proof in `RESULT.md` is algebraic and does not depend on bounded enumeration.

The attached checker builds a smallest-prime-factor table through
\[
10^6+1
\]
and evaluates the unitary totient from exact prime-power blocks.

It records every consecutive collision below one million for which both members have exactly two distinct prime factors. For each hit it reconstructs the even member as
\[
2^aB
\]
and the odd member as
\[
CD,
\qquad C<D,
\]
then verifies the appropriate factorization
\[
uv=2^a-1
\]
and one of the three theorem branches.

The complete observed list is
\[
20,\ 35,\ 143,\ 208,\ 2623,\ 5183.
\]
Their reconstructed branch data are also asserted exactly.

The checker independently generates all parameter tuples with relevant powers of two and confirms that every tuple whose three odd blocks are prime powers with the required support conditions gives consecutive integers with equal unitary totients.

Finally, among the direct two-support collisions in the tested range satisfying
\[
\Omega(n),\Omega(n+1)\le3,
\]
it asserts that only
\[
(20,21)
\]
occurs.

These finite checks are corroborative. The infinite completeness follows from the difference-of-squares identities and their algebraic converses.
