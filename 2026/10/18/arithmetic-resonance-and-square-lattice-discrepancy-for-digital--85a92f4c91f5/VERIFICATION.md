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

# Verification of the rational-angle resonance law

The standalone `verify.py` runs with a Python 3.9+ standard-library installation. It tests 110 ordered primitive Pythagorean triples produced by the Euclidean parametrization and verifies, using exact modular arithmetic, the relation \(h^2\equiv-1\pmod q\), the parity identity \(H=V+1\), and complete \(q\times q\) source-period collision counts. Exact integer floor division then measures the zero/one/two preimage frequencies in finite target windows for four independent triples, including both orientations of the \((3,4,5)\) triangle. An additional floating-point diagnostic checks two irrational angles against the published generic benchmark.

Command: `python verify.py`. Observed outcome: `PASS: 110 ordered primitive triples, exact modular-period counts, exact finite target counts, discrepancy bounds, and irrational diagnostics.`

The proof in `RESULT.md`, not the finite tests, supplies the universal identities, exact limiting frequencies and all-denominator discrepancy bound. Rounding in the irrational diagnostic does not constitute a certified infinite-time argument. The benchmark nonresonant formula is credited to the earlier literature. There is no independent audit.
