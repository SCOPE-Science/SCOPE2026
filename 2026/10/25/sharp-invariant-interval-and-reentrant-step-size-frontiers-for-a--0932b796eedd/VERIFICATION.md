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
# Verification and boundaries

The proof identifies the precise numerical method, all hypotheses, and the worst-case invariant-interval input analytically. In particular, the inequality \(Q_{s,v}(h)\ge0\) is both necessary and sufficient in the scalar domain, with a genuinely violating open interval of positive initial values when it fails. The monotonic ratio lemma and the uniqueness of the positive critical root provide the infinite-parameter certificates. The analytical result includes \(s=2\), \(v=0\), both equality boundaries, and every finite positive time step.

Running `python3 verify.py` from the same directory performs 1200 exact-rational checks of the original half-step and endpoint equations, cubic equivalence and symmetry, plus 9999 exact-rational critical-boundary checks. It also verifies the explicit rational overshoot witness and tests opposite sides of the reentrant interval. The program requires Python 3 and no third-party packages. These finite checks corroborate, but do not replace, the proof of the continuum statement.

Scientific limits: this is the homogeneous scalar subsystem of a particular Allen–Cahn discretization. Spatially varying solutions, other mobility functions, general meshwise sufficiency, energy estimates and error convergence are outside the claim. An equivalent result elsewhere in numerical invariant-domain literature has not been definitively excluded. Independent audit is not performed.
