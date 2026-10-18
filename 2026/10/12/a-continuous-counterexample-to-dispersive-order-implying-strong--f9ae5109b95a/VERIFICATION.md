---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

PASS: Reconstructed two strictly increasing piecewise-linear quantiles; their difference is 0, then increases with slope 8, then remains 8/5, proving X<=disp Y for every pair of quantile levels. Independently integrated quantile pieces to get tau_X=(25p²+143)/(2(25p²-25p+86)) and tau_Y=(25p²+183)/(2(25p²-25p+106)) on [3/5,4/5]. At u=24/25 and v=159/164, with u<v, differences are 174/115 and (1411-sqrt(62841))/770 respectively; 62841*23²-5657²=1241240>0 verifies reversed required strong expectile gap. Exact algebra checks the single witness; no finite enumeration used as a universal proof.

## originality

PASS

PASS (best of knowledge): New example establishes Q_Y-Q_X nondecreasing, a property not guaranteed by earlier dilation witnesses, and demonstrates reversed same-side expectile spacings. A counterexample under dilation alone does not refute an implication with the strictly stronger classical dispersive premise. No inspected broader theorem implies the present pair. Residual literature/access risks are explicitly recorded.

## value

PASS

PASS: A fully explicit atomless compactly supported witness resolves an explicit open implication in stochastic order theory with the very strong classical dispersive premise, distinguishing it from older dilation/weak expectile counterexamples. The upper-tail all-level failure has conceptual mathematical significance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
