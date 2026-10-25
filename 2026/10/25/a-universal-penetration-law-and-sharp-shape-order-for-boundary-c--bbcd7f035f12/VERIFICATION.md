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

# Verification details
The mathematical proof is complete in `RESULT.md`; finite numerical experiments are checks rather than proof. Run `python verify.py` with a standard Python 3 interpreter. The script calculates endpoints from actual Euclidean arclength weights and clips the resulting segment by three independent barycentric inequalities. Three example triangles (equilateral, scalene and thin), five thresholds each, 35,000 pairs per triangle: all 15 mixture comparisons have absolute normal deviations under 1.1. A separate conditional simulation of 100,000 pairs verifies five universal-law probabilities, each within 0.7 standard deviations.

The second failure integral, with \(b=1-2a\), is over intervals \(b/(1-a)<u<1-a\) and \(1-a<u<1\); these bounds were also algebraically simplified independently. No infinite enumeration, externally certified proof, or independent audit is asserted.
