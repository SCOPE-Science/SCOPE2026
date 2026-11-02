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
# Verification of the coexistence theorem

Run `python3 check.py` in a directory containing the standalone checker. Its exact output is embedded as `check_output.txt`. The checker recomputes the rational inequality \(M_{1/10000}(2)>1/(1-2m_{1/10000})\) using finite Taylor lower sums, and verifies the negative-slope and factorial coefficient certificates.

The analytic proof in `RESULT.md` independently supplies the infinite coefficient induction, tail cutoff \(\Phi_p(t)<1/t\), compactness, continuity, and transition-existence argument. A finite check cannot establish existence of \(p_*\) on its own. There is no independent audit, no symbolic black-box certificate, and no claim of exact threshold localization.
