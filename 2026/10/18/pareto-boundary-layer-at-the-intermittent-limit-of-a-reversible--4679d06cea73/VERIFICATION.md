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

Run `python verify.py` using Python 3 and only its standard library; the embedded program returned `VERIFY_OK` on the source material accompanying this theorem. The program checks exact rational reverse-branch identities and the transformed recurrence and evaluates rigorous CDF brackets from exact cylinder masses at several finite parameters. These checks do not constitute an exhaustive verification of the infinite limit.

The proof verifies the necessary infinite claims directly: contraction defines the canonical conditional; a length-\(n\) leftmost cylinder has conditional mass \(\lambda^n\); reciprocal rescaling has a uniform harmonic-series error estimate; and deterministic bracketing yields convergence at every continuity point of the limiting CDF. The boundary conditional at \(x=0\) is specified by the backward kernel, avoiding any ambiguity from conditioning on a Lebesgue-null singleton. The theorem does not assert a joint planar density or convergence of moments.

No independent audit has been performed.
