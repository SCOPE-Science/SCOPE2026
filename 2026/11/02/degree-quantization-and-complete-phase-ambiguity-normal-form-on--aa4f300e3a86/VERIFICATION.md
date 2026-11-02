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

# Reproducibility and limits

The algebraic reasoning is reproduced step by step in `RESULT.md`. In particular, the key source-independent identities are rational Schwarz reflection, cyclic fixed-field invariance \(\mathbb C(w)^{\langle\zeta\rangle}=\mathbb C(w^q)\), rational-map degree multiplicativity, and conjugate zero/pole symmetry on the real line.

Run `python3 CHECK.py` to reproduce the finite consistency experiment. The checker ran successfully and produced 11,544 assertions for rational-angle denominators from \(2\) through \(9\), with maximum relative squared-magnitude discrepancy approximately \(2.05\cdot10^{-15}\). These floating-point evaluations are illustrations, not an exhaustive or independent proof. The theorem's quantifiers are justified analytically in `RESULT.md`.

The generality is limited to nonzero univariate complex polynomials and two full Euclidean circles. Neither optimal sample count nor numerical stability in the presence of noise is claimed. Independent validation has not been performed.
