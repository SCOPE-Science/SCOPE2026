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
# Reproducibility and verification
The standalone `verify_cycle.py` script uses Python standard-library exact `Fraction` arithmetic for rational instances, and elementary floating-point bisection and Fourier-limit checks for the limiting constant. Run `python3 verify_cycle.py`. The expected completed output is `PASS 112 rational/numerical assertions`; an exception or assertion failure is a failed check.

The exact rational witness with \(n=4\), \(h=50\), and \(s=1\) was recomputed from the Padé factor and matched the negative numerator \(-9599175\) over the positive denominator \(309830404\). The symbolic arguments requiring independent reading are the resolvent identity, the cyclic group-inverse coefficient formula, uniform Fourier-logarithm expansions, and the uniqueness of the scalar critical root. Finite sample checking does not prove the infinite-step or dimension-uniform statements. Numerical values are illustrative evaluations of exact characterizations, not certificates of publication priority or external validation.
