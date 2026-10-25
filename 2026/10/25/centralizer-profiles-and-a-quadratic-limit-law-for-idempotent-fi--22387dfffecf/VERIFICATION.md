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

# Verification record

Run `python3 check_clamp_centralizers.py` next to the standalone script. The script enumerates all nondecreasing \(1\)-Lipschitz maps via every possible zero/one increment pattern and starting value, identifies idempotents by the equation \(f\circ f=f\), and evaluates the equation \(f\circ e=e\circ f\) point by point. Every \(n=1,\ldots,10\) passed against the closed formula; the count is \(220\) idempotents tested and \(243714\) individual map-versus-idempotent pairs. It additionally verifies exact combinatorial minimum-gap counts and numerical logarithmic estimates for sizes up to \(100\). Exact output ends with `ALL_CLAMP_CENTRALIZER_TESTS_PASSED cases=220 maps=5120 commuting_pairs=243714`.

The general correctness argument is contained in RESULT.md: the binary-step enumeration is exact for all integers, and the quadratic CDF comes from an exact composition count. Finite exhaustive enumeration does not prove an infinite asymptotic. The equivalence to any unidentified prior theorem has not been independently checked, and independent mathematical audit has not been performed.
