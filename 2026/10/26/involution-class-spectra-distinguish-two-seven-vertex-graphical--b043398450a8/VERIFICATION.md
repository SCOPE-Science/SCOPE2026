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

# Verification evidence

Run `python3 verify.py` in this directory. The standalone script independently enumerates every subset of each of the two named seven-vertex graphs and recomputes the complete ordinary and independent-support histograms from the edge sets. It checks their formal difference as a polynomial, not merely at sampled field orders, and compares the stored `CERTIFICATE.json` with direct enumeration. It also executes literal group multiplication, squares, and centralizers over the finite fields of orders two and four for small graphs, and computes the full seven-vertex square-one conjugacy-class counts over the binary field. The observed binary distributions are \( (256,256,256,416,112,16) \) and \( (256,256,320,320,160,8) \), with exactly \(7424\) square-one elements in each group. The program returned `VERIFY_OK_GRAPHICAL_INVOLUTION_CLASS_TWINS`.

This finite exhaustive certificate is valid only for the displayed pair; the universal group-theoretic involution formula is proved separately in `RESULT.md`. Verification does not constitute independent review. The subgroup- and support-count operations are explicit, and no unidentified computations or inaccessible paths are needed.
