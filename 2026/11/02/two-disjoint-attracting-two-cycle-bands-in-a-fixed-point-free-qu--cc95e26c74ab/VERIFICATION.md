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
# Reproducibility of the two-cycle calculation

Run `python3 verify_period_two.py` using Python 3 and no external packages. The checker successfully executed from the packaged exact source. It uses `fractions.Fraction`, not floating-point evaluations, for the algebraic identities, orbit returns, branch Jacobians, root sign brackets and Jury witnesses. Its checks are supplemental: the proof of complete root counts comes from quadratic algebra, Descartes' rule of signs and the strict monotonicity of \(V(t)\).

The five central identities to reproduce are: the period-two scalar equation \(Lt^2-2at+K=0\); the trace \(T=290/121-(W+H)^2\); the determinant \(D=169/121-(W-H)^2\); the Schur identity \(1-T+D=11(K-at)/5\); and the polynomial numerator \(P(t)\) for \(W^2+H^2-290/121\). The exact rational root brackets isolate the two \(-1\) spectral boundaries. Two additional rational brackets isolate the solutions of \(V(t)=\pm4\sqrt3/11\), compared by squaring with controlled signs. The four resulting amplitudes are strictly ordered.

The displayed \(c\)-threshold decimals are numerical evaluations for illustration, not machine certificates. At a boundary eigenvalue of modulus one, nonlinear stability is not asserted. Neither the checker nor the analytic argument examines prime periods above two, global basins, or priority against unavailable literature. Independent mathematical audit has not been performed.
