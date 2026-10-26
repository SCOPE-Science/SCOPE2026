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

# Reproduction and verification scope

Extract `verify.py` and `requirements.txt` into the same directory, install the declared NumPy/SciPy dependencies, and run `python verify.py`. The program should print `PASS: 57 numerical comparisons` followed by a table of approximate lowest positive eigenvalues for selected \(q\) values.

The two independent eigenproblems are (i) weighted odd Legendre–Galerkin discretization on \((-1,1)\) and (ii) finite elements after the coordinate substitution \(x=\tanh y\). The explicit energy and mass forms are derived in RESULT.md rather than being inferred from observed numbers. The checks include the exactly known \(q=0\) Legendre normalization, monotonicity samples, Hardy bounds, the one-dimensional trial-function Rayleigh upper bound, the \(3/10\) perturbation coefficient, and cross-method comparison.

The limiting relation \(\mu(q)/(1+q^2)\to1/16\) is **not** numerically certified at any finite maximum \(q\): approach is slow, and a finite cutoff can miss the Hardy threshold. Its proof is the analytical lower/upper argument in RESULT.md. Likewise, sampled monotonicity does not certify an uncountable parameter family. No spectral claim for the full finite-spin quantum generator near the critical boundary is verified or asserted.
