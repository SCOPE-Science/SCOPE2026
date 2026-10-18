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

The exact mode reduction uses the normalized beta density with parameters \((m+1,\alpha+1)\). It gives the double singular value \(\sqrt{\mathbb E_m(u^2)-(\mathbb E_m u)^2}\) in each Fourier mode. The strict positive leading coefficient follows from gamma log-convexity, and the limit in sorted singular values from fourfold counting.

Run `python3 verify_radial_blocks.py`. It checks exact beta moments and positivity for three integer boundary powers at a range of degrees, and a finite-dimensional orthogonal-projection commutator matrix, with high-degree asymptotic spot checks. These computations are finite checks, not an infinite proof. The mathematical proof is supplied in RESULT.md. No external or independent validation has been performed.
