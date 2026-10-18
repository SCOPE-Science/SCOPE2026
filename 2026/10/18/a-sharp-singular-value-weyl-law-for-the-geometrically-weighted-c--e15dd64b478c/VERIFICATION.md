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

# Verification of the geometric Cesàro singular-value law

The proof is mathematical: a unitary conjugation, a finite-band Toeplitz block counting lemma, singular-value rank/norm perturbation estimates, passage through uniformly convergent analytic symbols, and count inversion. Each argument applies to every fixed parameter \(0<r<1\), not merely tested values.

The accompanying `verify.py` uses NumPy to construct \(320\)-coordinate truncated matrices and numerically integrates the characteristic symbol. The checks run for \(t=0.4\) and \(t=0.7\) (where \(t=\sqrt r\)); each tests diagonal normalization, descending singular values, four indices \(40,60,80,100\), and the positive coefficient. It also checks the degenerate symbolic limit \(t=0\). Running `python verify.py` returned **PASS: 15 deterministic checks**, including the numerical coefficients \(1.044056341290\) and \(1.175005293106\).

Finite-section singular values approximate but cannot certify the infinite asymptotic, uniqueness of a closed form, or bibliographic novelty. No machine formal proof or external independent audit was performed.
