---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For w_j=1+α/j+c_j/√j with 0≤α≤1 and bounded zero-mean periodic |c_j|≤1/2, weights are positive. Taylor expansion gives log w_j=c_j j^{−1/2}+(α−c_j²/2)/j+O(j^{−3/2}) uniformly in j large. Periodicity and zero mean make the c and c²−v partial sums uniformly bounded, so Abel summation yields uniform all-start/all-length log product δ log((k+n)/k)+O(k^{−1/2}), δ=α−v/2, plus finite positive correction limit L_k. The orbit identity ||Tⁿx||²=Σ|x_k|²P_{k,n}² and dominated convergence give δ>0 divergence of every nonzero orbit, δ<0 strong convergence to 0 but failure of uniform decay on any fixed bounded-orbit ball by far-out e_k, and δ=0 strictly positive finite norms. T is a compact perturbation of the unilateral shift; Fredholm index −1 inside the disk, absence of eigenvectors, growth-bound spectral radius 1 and long approximate unit-circle blocks give σ=closed disk, σ_point=∅, σ_approx=unit circle. Independently recomputed logarithmic drift/residual stabilization for alternating perturbations across δ signs; these finite diagnostics are not proofs. Exact comparison of imported named strong/super asymptotic definitions limited by inaccessible Bag–Mandal–Das full text.

## originality

PASS

Bernardes et al. establish positive expansivity iff unbounded forward weight products; the δ>0 implication is an application once the new uniform product law is known. Bag–Mandal–Das introduce the refined definitions, equivalence of super asymptotic expansivity and hyperbolicity, and a spectrum-blind pair of examples, but no documented all-period critical j^−1/2 perturbation law. The distinct mean-square correction and quantitative uniform estimate create the new three-branch phase portrait; O best-of-knowledge with source full-text access residual risk.

## value

PASS

Periodic zero-mean fluctuations at the critical j^−1/2 scale produce a deterministic variance correction of −mean(c²)/2, changing orbital stability and sharp phase boundaries while spectrum stays fixed. The quantified all-start/all-time product bound and three distinct dynamical outcomes provide a meaningful perturbation threshold, not a routine positive-expansivity criterion alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
