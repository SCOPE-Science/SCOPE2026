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

# Verification and reproducibility

Run `python verify_unicyclic_leaves.py` using Python 3.10 or later. It needs only Python standard-library modules.

The checker implements two logically distinct exact finite enumerations: labelled cycle/rooted-map inclusion–exclusion and formal-power-series coefficient arithmetic. It additionally scans all \(n\)-edge labelled simple graphs for \(4\le n\le7\), finds connected unicyclic examples by connectivity and leaf-pruning, and compares every joint \((K,L)\) cell against the formula. It returned: `PASS: 455 exact formula/closed-case checks, 34 independent raw graph-enumeration checks (n=4..7).`

The infinite-size theorem additionally requires the explicit determinant reduction and uniform fixed-degree coefficient expansion given in `RESULT.md`; the finite program does not certify any asymptotic conclusion on its own. The checker is neither an independent mathematical audit nor a third-party certificate. No external validation has been performed.
