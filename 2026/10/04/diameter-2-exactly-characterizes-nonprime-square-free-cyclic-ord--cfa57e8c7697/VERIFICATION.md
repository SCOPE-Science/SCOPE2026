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
The symbolic proof was reconstructed from the definitions and checked for all containment orientations of a possible common neighbor.

Key exact checks:
- For \(\alpha=2,3,4\), the choices \(t=2,2,3\) satisfy that \(2t+1\) is prime and \(\alpha<3t-2\).
- For \(\alpha\ge5\), Bertrand's postulate applied to \(\alpha+1\) gives a prime \(2t+1\) with \(t>\alpha/2\), which implies \(\alpha<3t-2\).
- A lower common neighbor would force a nontrivial proper divisor of the prime \(2t+1\).
- An upper common neighbor would force \(2t-1\mid2s+1\), hence \(s\ge3t-2>\alpha\).

`artifacts/verify.py` performs an independent exact-integer replay on a finite range, including graph construction from subgroup orders and direct distance calculations. The computation is not used to justify the infinite theorem.
