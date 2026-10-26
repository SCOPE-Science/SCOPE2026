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

Run `python3 verify_phase_means.py` from the same directory. Its output must match `checker_output.txt`. The script uses the Python 3 standard library, exact rational arithmetic for the cubic identities, deterministic Fourier quadratures and finite phase meshes for numerical cross-checks. The theoretical proof in `RESULT.md` supplies the infinite-domain maximizer classification and the existence of smooth dynamical realizations. No computation is presented as a certificate of an unbounded theorem.

All checks returned successfully on the packaged source. Important checks are normalized Fourier-correlation identities, critical polynomial identities, a finite two-lobe phase scan, the high-frequency local-instability sign and inequivalence of supercritical mean classes. Critical scientific restrictions: no arc-length quotient, no ambient rigid rotations, no claim about general ensembles or unique real-valued parameter estimation.
