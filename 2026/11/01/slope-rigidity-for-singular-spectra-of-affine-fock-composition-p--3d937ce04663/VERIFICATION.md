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

# Verification record and limits

The central identities can be checked without any numerical experiment: compute both products on kernels \(K_w(z)=e^{z\overline w}\); insert each exponential-affine symbol into the explicit unitary identity \(T=e^{\delta-E}U_pD_vU_q\), where the diagonal singular values are \(|v|^n\); and check that the associated real Hermitian quadratic-form determinant is \(-|a-c|^2\).

The supplementary program `check_singular_orientation.py` was executed with Python 3 and NumPy. It returned “PASS: 143 finite numerical/algebraic checks”. Its tests include selected complex affine pairs, the first three singular values of each finite matrix compression, two opposite orientation examples, randomly sampled algebraic identities, and the same-slope formula. The truncation checks are not a proof for infinite matrices or for all complex parameters. The theorem's exact limits are the strict-slope one-variable Gaussian Fock domain stated in `RESULT.md`.

No independent scientific validation or external certificate has been performed.
