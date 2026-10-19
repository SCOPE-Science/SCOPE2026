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

`verify.py` constructs all \(3^{2e}\) parameter pairs for each \(e\in\{1,2,3,4\}\), computes actual matrix orders by successive multiplication up to \(2\cdot3^e\), and compares them against the closed-form ternary valuation law. It also compares the observed multiplicity of each \((r,s)\) stratum with the analytical exact count and verifies that the strata partition all pairs.

Executed from the embedded source with Python 3; result: `VERIFY_OK`.

Observed period histograms: \(e=1\): \(1:1,3:4,4:2,6:2\). \(e=2\): \(1:1,3:20,4:6,6:6,9:24,12:12,18:12\). The larger tests for \(e=3,4\) also passed.

These are finite diagnostic calculations. The proof for all \(e\ge1\) relies on the integer matrix Cayley–Hamilton identity, a ternary binomial lifting lemma, and exact valuation-shell counting. The checker does not certify the historical absence of earlier equivalent results and does not constitute an independent mathematical review.
