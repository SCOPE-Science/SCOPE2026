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

The analytic theorem follows from an exact ordered-pair overlap decomposition, strict derivative negativity, endpoint limits, and a Taylor expansion in the overlap ratios. Its hypotheses include \(r\ge3\), \(n\ge r+1\), and \(0<p<1\).

Run `python verify.py` in the directory containing the extracted file. The script uses only the Python standard library and independently enumerates every graph with four, five, or six vertices for selected parameters; it also performs exact-rational comparisons and numerical zero/asymptotic checks. Finite computations corroborate but cannot certify all integer orders or all real edge probabilities. Source comparisons are summarized in REVIEW.md and AUDIT.json; complete inspection of every historical treatment remains outside the available evidence.
