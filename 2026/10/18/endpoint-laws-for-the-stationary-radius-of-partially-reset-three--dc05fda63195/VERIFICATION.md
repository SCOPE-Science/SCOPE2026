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

The stationary law is obtained as a norm of a convergent three-dimensional random-vector series, not a sum of its termwise norms. Fourier inversion is justified by the first two resolvent factors, which give an integrable order-four bound in three dimensions. The strong-contraction endpoint uses the change of variables \(s=ct\) and domination by \((1+s^2)^{-1}\). The weak-contraction endpoint uses Fourier normalization by the exact coordinate standard deviation, a pointwise Gaussian limit, and an integrable uniform fourth-power envelope.

To rerun computational cross-checks, install the packages in `requirements.txt` and execute `python verify.py` from this document's directory. The script evaluates the stationary integral at several contraction parameters, checks the two predicted limiting scalings to numerical tolerance, verifies moment formulas, and tests finite products. Numeric checks do not establish limits or mathematical priority; the proof is in RESULT.md.

The source comparison relied on the accessible full text of Kolb--Wübker (2026), notably Proposition 10, Corollary 11 and Lemma 12, and on Grzywny et al. arXiv:2412.15626, notably Theorem A, Proposition 2.22 and the Brownian space-time sections. No independent audit has been performed.
