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

# Reproducibility and limits

Run `python3 verify_fano.py` using the Python standard library. The checker performs arithmetic in \(\mathbb F_2\), rather than using numerical approximations. It checks seven binary forms, their cubic sum, the characteristic-two Moore determinant, and direct syzygy identities at five odd degrees \(d=1,3,5,7,9\). The theorem is stated for odd \(d\ge3\); the degree-one test is merely a base-case consistency test. The final success marker is `FANO_FERMAT_CHAR2_GENERAL_IDENTITIES_AND_FIVE_EXACT_INSTANCES_PASS`.

The universal assertion uses the hand-proved identities \(D_j(\ell)=\ell^{2^j}\), the seven-form parity cancellations, the degree-four determinant factorization and the logarithmic determinant criterion. The experiments do not independently prove the infinite family. The local singularity scheme calculations are supplied algebraically in `RESULT.md`, not inferred from sample enumeration. Neither an independent external audit nor independent validation has been performed.
