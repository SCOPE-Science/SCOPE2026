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

The proof uses the exact finite-\(k\) QQ formula and the analytic QC upper bound from the cited source. The included verifier checks the following finite identities and convergence diagnostics:

- \(|1-p+pe^{2i\alpha}|^2=1-4p(1-p)\sin^2\alpha\);
- at \(p=1/2\), the QQ formula equals \(2^{-k}\) for even \(k\);
- for representative fixed \(p<1/2\), the exact QQ expression converges to \(e^{-\pi^2p(1-p)}\cos^2(\pi p)\);
- the exact QC capacity expression has \(nC_{\mathrm{QC}}\to 2\pi^2(1-2p)^2/\ln2\) in the stated resource scaling.

These checks are corroborative. The infinite-\(k\) statements follow from the displayed Taylor expansions in the proof, not from finite enumeration.
