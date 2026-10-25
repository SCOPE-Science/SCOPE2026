---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

With L_j=|j+1><j| and L=gamma(J-I), the exact-integral FREE step of Chen et al. is Phi=q I+(1-q) J, q=e^(-gamma tau), whereas the exact channel is e^(x(J-I)). The superoperator J is normal: it cyclically permutes diagonal populations and kills all off-diagonal coherences. Its only fixed matrix is scalar identity. The full Hilbert–Schmidt contraction thus has alpha_n=max(q,sqrt(1-2a_n q(1-q))) and beta_n=e^(-x min(1,a_n)) with a_n=1-cos(2pi/n). Exact n=2,3 factorizations show equality only x<=ln3 or x<=ln2 respectively; for n>=4 the displayed scalar derivative inequality gives strict alpha>beta for all x>0. As q->0, alpha=1-a_n q+O(q^2) and e^(x(J-I))->depolarizing Pi while Phi->J; the maximal density-state trace-norm distance tends 2(1-1/n). Independent finite-dimensional full-superoperator singular-value checks for n=2,3,4,6 corroborate. They do not prove universal dimensions or steps.

## originality

PASS

The full-rank FREE update and its positivity/consistency are already in Chen et al.; Fourier modes of cycles and lazy Markov chains are classical. The submitted result isolates their exact full density-matrix spectral norm comparison, sharp dimension-two and -three equality windows, and strong-step trace-distance limit. No inspected primary theorem makes this full-matrix quantitative classification. There is genuine risk of an equivalent earlier Poissonized/lazy-walk computation.

## value

PASS

A numerical Lindblad integrator can be completely positive, trace preserving and stationary-state exact yet nearly cease mixing in the stiff regime while the true dynamics relaxes rapidly. The exact dimension-dependent thresholds identify when coherence modes conceal population failure, giving a mathematically sharp warning rather than simply a tiny numerical error demonstration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
