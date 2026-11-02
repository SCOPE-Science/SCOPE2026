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

# Verification of the mathematical claim

The companion `verify.py` is a standalone Python 3 script using only the standard library. Executed against its actual packaged path, it builds the adjacency matrix of \(J(n,2)\), the two-orbit antisymmetric potential, and the full skew-symmetric commutator. For every integer \(5\le n\le10\) and each of nine exact rational potential parameters, it computes the Gram matrix on the complete minus-parity basis directly from the actual graph. It checks every entry against the closed formula; it checks the projected two-dimensional block, the repeated eigenvalue, strict block domination, skew symmetry, and parity anticommutation. The recorded output is:

`CHECK_OK: exact rational Gram blocks, parity, and norm domination; 89685 assertions across 54 graph/parameter cases`

The calculation uses `fractions.Fraction`; it is not a floating-point fit. The unrestricted statement additionally requires the exact group-average reduction, parity completeness, and analytic large-parameter argument given in RESULT.md. Those are mathematical proof steps, not computationally certified over infinitely many graphs. Numerical approximations and the finite test neither establish historical originality nor count as independent validation.
