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

The rational-symbol proof is analytic. Its critical steps are the rational reflected adjoint, the polynomial spectral projection onto the maximal Hermitian eigenspace, the positive-semidefinite kernel construction at each exposed-face endpoint, and Gaussian elimination over \(\mathbb C(z)\) followed by denominator clearing. No finite sampling substitutes for these steps.

The nonrational counterexample uses uniqueness of Laurent boundary coefficients on an outer annulus and the impossibility of cancelling \(\exp(-1/z)\)'s essential singularity with a nonzero analytic germ. Vector reproducing kernels give arbitrarily close endpoint expectations but not attainment.

The standalone `verify.py` checks a rational two-by-two polynomial witness and a real-analytic rank-one projection's sampled algebraic identities. Execute with Python 3 standard library. It does not verify all matrix dimensions or mathematical originality, and the independent audit is not yet performed.
