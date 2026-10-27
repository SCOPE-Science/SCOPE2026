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
# Computational verification and limitations

The standalone `verify.py` script computes positive solutions to the linear resonance equation and compares them to the directly evaluated phase-speed function. It checks the monotone high-harmonic short-wave sequence, fixed-tension cubic correction, critical-tension harmonic uniformity at multiple orders, and weak-tension crossover across varying harmonic indices. A local execution returned `VERIFICATION_OK 329` (329 successful assertions). The numerical checks use IEEE double precision and fixed tested parameters; they **do not** constitute exhaustive verification of any infinite-order uniform asymptotic statement. The analytical proof in `RESULT.md` addresses those statements.

Command: `python3 verify.py`. Python standard library only; no network, nonstandard packages or datasets are needed.

The underlying phase-speed formula and resonance uniqueness are established in the references. The separate originality and mathematical-value assessments are documented in `REVIEW.md` and `AUDIT.json`. No independent scientific audit has been performed.
