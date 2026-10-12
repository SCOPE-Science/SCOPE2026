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

Proof checks: \(H^2=Kz\) and \(\operatorname{Ann}(H)=Kz\) force the block form, and the multiplication preservation equation is both necessary and sufficient. The singular rank split is governed by whether \(f|_{\ker A}\) vanishes. The isotropic subspace count was derived from ordered isotropic flags, with no characteristic restriction. All rank multiplicities add to \(q^{2m}G_m(q)+q^{2m}\sum_r N_{m,r}(q)\); the leading degrees yield the stated limits.

Reproducible finite tests: run `python3 checker.py` using the standalone script bundled with this result. The script directly constructs and checks all \(3\times3\) linear matrices over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\) and independently enumerates \(4\times4\) degree-one blocks plus central functionals over \(\mathbb F_2\). All cases returned `VERIFY_OK`. Examples: \(\mathcal R_{1,2}(T)=1+21T+18T^2+24T^3\) and \(\mathcal R_{2,2}(T)=1+465T+15750T^2+37800T^3+11520T^5\).

Limits: finite checks alone do not establish the theorem for all fields and all \(m\). An independent scientific audit and exhaustive bibliography-level priority determination are not part of this verification.
