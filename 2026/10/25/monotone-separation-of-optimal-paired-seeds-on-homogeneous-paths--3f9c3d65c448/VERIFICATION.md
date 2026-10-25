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

Execute `python3 verify_pair_influence.py` (Python standard library only) and compare stdout to `certificate.json` (one JSON object followed by a newline). The program independently checks exact live-edge state enumeration against the derived two-seed expectation polynomial for 495 cases on paths of orders two through ten; tests 408 exact balanced-pair polynomial identities and 7,153 exact rational balancing comparisons; compares optimum seed gaps for 1,428 rational test configurations through 69 vertices; and verifies 47,838 exact adjacent-gap expectation differences. It also directly asserts the four-vertex \(p=1/2\) threshold.

The unlimited-\(n\), every-real-\(p\) theorem does **not** rest on these finite checks: its proof is the exact live-edge probability formula, a fixed-gap tail exchange, a strict adjacent-gap ratio inequality, and a logarithmic strict-concavity threshold argument. Root locations and monotonicity are symbolic; numerical sampling is not treated as exhaustive. The corresponding assumptions, equations, and boundary exclusions are given in `RESULT.md`. The calculations do not establish any theorem for heterogeneous or correlated transmissions. The package does not constitute an independent audit.
