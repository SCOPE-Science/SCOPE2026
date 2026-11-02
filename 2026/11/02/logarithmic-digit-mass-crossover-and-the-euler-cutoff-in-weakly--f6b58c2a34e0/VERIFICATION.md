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

# Reproducible checks and their limits

The proof is analytical: exact similarity pressure roots, a uniform monotone integral comparison, the Riemann-zeta pole, a generalized-harmonic partial-sum CDF, and the harmonic-number constant. These apply for every stated fixed \(q>1\), \(\tau>0\), and sufficiently small \(c>0\). A finite computation cannot certify limits or historical originality.

From this package, run `python verify_crossover.py` after installing `mpmath` (tested with 1.3.0). The script completed **162 sample consistency assertions** on the finite and infinite pressure roots, probability distribution, physical branch separation, and harmonic cutoff. For \(q=2\), its continuum scaled root values at \(\tau=1/2,1,2\) are approximately \(-2.51286241725234\), \(0\), \(0.79681213002002\). At \(\tau=1\), the distribution tends to the uniform law on \([0,1]\). For the full alphabet the scaled dimension excess approaches one and the rescaled digit approaches a unit-rate exponential.

The script uses Hurwitz-zeta subtraction for huge integer cutoffs rather than claiming exhaustive iteration over exponential alphabets. Errors decrease across the tested scales, but the program does not provide computer-assisted rigorous error bounds and is not an independent audit.
