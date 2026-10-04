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

The unrestricted theorem is proved symbolically in `RESULT.md`.

The packaged checker verifies exact rational versions of the three abundancy
obstructions
\[
I(4\cdot3^2)>2,
\qquad
I(4\cdot5^2)>2,
\qquad
I(4\cdot7^2)>2,
\]
and the power-of-two obstructions for least primes \(3,7,31\). It also checks
that every other odd prime below \(37\) has \(p+1\) divisible by one of
\(3,5,7\).

As a separate finite corroboration, it computes \(\Omega(n)\), \(\sigma(n)\),
and \(\sigma(\sigma(n))\) exactly for all \(n\le200000\) with
\(\Omega(n)\le2\). In this interval the only solutions are the Mersenne primes
\[
3,7,31,127,8191,131071,
\]
and there is no composite solution.

The finite sweep is not used to prove the theorem or to infer nonexistence
outside the tested range.
