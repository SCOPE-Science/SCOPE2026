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
# Reproducibility and mathematical limits

The proof certificate is the complete list of the \(21\) invariant center-and-support states in `RESULT.md`. For each state, check the displayed successor by the original synchronous update rule; the listed hitting times follow recursively, except that \((2,\{0,1,2\})\) is permanently nonsynchronous and the three monochromatic states cycle together. Multiply the \(|S|=1,2,3\) populations by \(1\), \(2^r-2\), and \(3^r-3\cdot2^r+3\), respectively.

Execute `python3 verify.py` to reproduce the direct labelled-state exhaustive comparison over all \(3^{r+1}\) configurations for each \(1\le r\le9\). Expected output is retained in `verify_output.txt`, ending `ALL NINE SIZES EXACT`. The verifier uses an update on full labelled vertex arrays rather than the support quotient, and detects repeated configurations before declaring nonsynchrony. Its agreement is an independent computational implementation, **not** an independent mathematical audit and not a replacement for the all-size proof.

The scope is the deterministic synchronous three-color inhibitory rule on stars only. No stochastic or other-color theorem has been checked.
