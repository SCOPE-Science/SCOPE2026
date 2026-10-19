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

# Reproducibility of the finite checks

The proof of the all-multiplicity theorem is contained in `RESULT.md`. Its decisive infinite-dimensional step is the unique minimal exterior minor: order \(r^2\), nonzero coefficient \(D_{m,r}\), all others at least one order higher with square-summable Fock expansions.

Execute `python verify.py` with Python 3 and `mpmath`. The script runs 139 assertions: exact rational reciprocal-factorial determinant identities through exterior order seven; sharp final-channel factorial identities through multiplicity six; and independent high-precision overlap and truncated leakage-tail matrices for multiplicities one through six at three small displacements. Every channel is checked for the predicted leading term. A 48-term Fock tail is used only for corroborating finite tests; no claim about an infinite matrix is inferred from truncation. `verification_output.txt` records the actual output. All theorem error terms remain \(O_m(|w|^2)\) for fixed \(m\), not uniform in \(m\).
