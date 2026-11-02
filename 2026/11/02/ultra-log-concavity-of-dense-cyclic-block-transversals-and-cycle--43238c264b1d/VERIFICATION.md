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

# Reproduction

Run `python3 verify.py` using Python 3.9 or later; no third-party libraries are required. The verifier tests all cyclic-block hitting-set profiles with \(2\le n\le15\) and \(q+1\le n\le2q+1\), all powers of simple cycles of order \(3\le n\le15\) in the claimed range, and a further \(13,040\) parameter pairs by exact binomial formulas. Each test checks the correct normalized inequality using integer cross products, without floating-point rounding. Expected result: `VERIFY_OK cyclic_hypergraphs=63 exhaustive_graphs=92 exact_parameter_cases=13040`.

The computational checks establish only these finite cases. The proof in `RESULT.md` supplies the infinite argument by unique long gaps, a rational identity for adjacent failure-probability ratios, and a convexity identity. Publication priority and independent audit remain unresolved.
