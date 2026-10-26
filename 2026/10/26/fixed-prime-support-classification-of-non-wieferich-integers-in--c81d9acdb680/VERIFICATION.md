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

# Verification and limitations
The exact congruence test is implemented in `verify.py`: compute \(L_b(n)\) by Euler-totient factor reduction, then independently check \(b^{L_b(n)}\not\equiv1\pmod{p^{a_p+1}}\) for each prime-power divisor \(p^{a_p}\) of \(n\). Compare that boolean with the explicit threshold criterion. This verifies selected finite cases, not every \(b,S\).

The unrestricted universal result is proved by lifted orders and \(2\)-adic valuation identities in RESULT.md. The counting error comes from a fixed-dimensional simplex boundary argument. A future independent review can audit the reference comparison and infinite proof.
