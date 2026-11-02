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

# Verification and reproducibility

Run `python check.py` with Python 3 and SymPy; the supplementary numerical corroboration uses mpmath. The script checks the exact Chebyshev reduction, the strict-concavity derivative polynomial, the Bernstein positivity certificate for the negative-cosine half-cycle, two closed-form parameter examples, and seven illustrative numerical grids. The algebraic proof in `RESULT.md` is required for the continuous all-parameter theorem; sampled grids do not establish global optimality.

The exact illustrative optimizer has \(E=5/6\), \(a=1/2\), \(b=2/3\), \(\cos\theta=1/2\), and splitting excess \(19/12\). Another exact example has \(a=1/20\), \(b=1/10\), with each overtide below its separate Doodson threshold but a strictly positive joint excess.

Assumptions: phase locking at the nominal crest, unit primary amplitude, nonnegative overtide amplitudes, fixed squared-amplitude sum, and a continuous full-period maximization. Reproducing the script or the symbolic identities does not certify ecological or coastal realism, historical priority, or independent mathematical validation.
