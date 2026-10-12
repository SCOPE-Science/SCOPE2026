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

The proof is symbolic and exhaustive. For
\[
n\ge5,
\]
the even member of a consecutive pair with \(\Omega\le2\) must be
\[
2r
\]
with \(r\) an odd prime. The odd neighbor has exactly one of the forms
\[
s,\qquad s^2,\qquad ab
\]
with \(s,a,b\) odd primes and \(a<b\). Substitution into the equality of totients produces contradictions in all cases.

The packaged checker independently sieves Euler totients and prime-factor multiplicities through \(2{,}000{,}000\). It confirms that the only solution in the tested range with both multiplicities at most \(2\) is
\[
n=3.
\]

The finite computation is corroborative only and is not used to establish the unrestricted theorem.
