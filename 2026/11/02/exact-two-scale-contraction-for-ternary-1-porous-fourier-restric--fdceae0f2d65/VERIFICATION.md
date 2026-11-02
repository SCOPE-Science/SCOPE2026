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

# Reproducibility

Execute `python CHECK.py` using Python 3 and only the standard library. It computes all four-by-four Gram characteristic polynomials exactly in the cyclotomic integer ring, checks the exact list of 27 maximal one-step porous supports, the six-unit nine-translation affine orbit, and the decomposition into three nine-element translation orbits. This is an exact algebraic reproduction of the finite input, with no floating-point threshold decision.

The mathematical proof establishes the real-root ordering using inequalities for \(\cos(2\pi/9)\), \(\cos(4\pi/9)\) and \(\cos(8\pi/9)\). Submultiplicativity beyond length two is taken from Lemma 3.1 of Badalucco and Franchi, arXiv:2607.11534, rather than asserted as a new lemma. Finite verification does not establish infinite results on its own. The exact constant is local to one-step porosity in the ternary case, and the resulting uniform exponent is not claimed optimal.
