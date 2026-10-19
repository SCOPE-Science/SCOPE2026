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

The proof is analytic. The standalone standard-library program `verify.py` reproduces supporting arithmetic and numerical checks by running `python verify.py` with Python 3.9 or newer. No external files, web access, random data sets or nonstandard dependencies are needed.

The program checks the exact rational witness \(\kappa=2\), \(h=2\), \(q_0=(1,1/2)\), for which the midpoint predictor is \((-3,-11/2)\) and the minimum along the prescribed correction line is \(9801/1945\), strictly above the target energy \(2\). It separately evaluates matrix-map energy amplification, direct minimization against its closed expression, maximal phase constructions across the threshold, and numerical phase-arc integrations. Finally, it tests the critical square-root asymptotic and the large-step inverse-square phase law over several anisotropy values.

The recorded output, in `verification_output.txt`, reports `PASS: 6563 exact/numerical assertions`. The phase integrals are approximated by 300,000 deterministic midpoint samples for each of five parameter choices, with a stated numerical tolerance. The infinitely many steps and continuum of phases are handled by the algebraic proof, **not** established by these finite grids. The asymptotic formulas are also established symbolically in the proof; finite evaluations only check their normalization.

No external independent scientific audit has been performed.
