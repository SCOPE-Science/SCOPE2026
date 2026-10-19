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

# Verification details

Run `python check.py` with Python 3.10 or later; no external packages are needed. The program directly constructs every binary lower mechanical word of coprime parameters \(2\le n\le80\), cycles through all \(n\) rotations, computes complete length-\(\ell\) prefix and suffix Parikh counts for \(1\le\ell<n\), and compares each individual border decision with the independent modular-residue formula. It also checks the distribution of border-count values, the exact multiplicity of unbordered rotations, and the parity-dependent maximum.

Observed output:

`PASS_CHRISTOFFEL_ABELIAN_BORDER n=2..80 coprime_length_slope_pairs=1965 rotations=105388 border_decisions=6250510`

The unrestricted conclusion is furnished by the telescoping-floor proof in `RESULT.md`; finite testing is not treated as an infinite certificate. The test does not establish novelty in the literature. Independent audit: not performed.
