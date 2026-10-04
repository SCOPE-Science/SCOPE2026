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

The exact proof has two parts. Necessity is symbolic: the two projective reversal equations imply \(\mu'=1-\mu\), and full support forces \(s=1/2\). Sufficiency is replayed by `verify.py` in \(\mathbb Q(\sqrt2)\): the two stated weights are swapped exactly by the normalized \(j=2\) fourth-power weight map and have common normalization \(Z=1/64\).

The checker also verifies exact positivity of the smaller extreme weight and confirms that the general radial expression specializes to \(Q=1/49\) at \(\kappa=3\). The radial formula for arbitrary \(m>h>0\) is proved algebraically in `RESULT.md` by multiplying the two cycle polynomials; the checker is not used as a substitute for that infinite-parameter proof.

No claim is made about arbitrary exceptional cycles, their measure, or their stability. The closest Li--Wang full text was not available for line-by-line originality comparison; that is an access limitation, not evidence of absence.
