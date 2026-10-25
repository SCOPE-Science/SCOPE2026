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

# Verification scope

The mathematical proof is self-contained in `RESULT.md`. The algebra uses positive consecutive gaps, explicitly enumerates every possible omitted agent, computes exact subset-normalization and expected cost, and proves an inequality for all integer facility counts and all positive real gaps. A limiting family proves that the upper constant is the sharp supremum.

The program `VERIFY.py` uses Python standard-library fractions and enumeration of all possible chosen facility sets. It checks the exact expectation formula, the strict sharp bound, and the equality characterization for all \(2\le k\le6\) with gap entries \(1,2,3,4\), plus four sharp-family rational identities per \(k\). Command: `python3 VERIFY.py`. Observed output: `PASS: 21844 exact-rational assertions; k=2..6, integer gaps 1..4; sharp families T=2,5,20,100.`

The finite tests do not establish the theorem by exhaustion; its unbounded facility count and arbitrary real gaps follow from the proof. No independent external audit, higher-dimensional extension, or incentive-property proof is asserted.
