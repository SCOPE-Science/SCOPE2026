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

The analytic proof checks the generator normalization, exact renewal products, exchangeability, and controlled fixed-size asymptotics. Independent finite-state verification uses the original configuration-space generator, not the count-level chain: `python verify_annihilation.py`. It tested \(N=2,3,4,5,6,7\) at \(r=0.13,0.7,2.5,9.0\), making 1,008 individual state-probability comparisons and 24 covariance comparisons (absolute tolerance \(3	imes10^{-12}\)). Every test passed. The script requires NumPy and SciPy; finite testing is corroboration, not an infinite proof.

Unproved limits: no claimed unique crossing for general odd \(N\), no even-size global sign classification, no thermodynamic scaling, and no independent audit.
