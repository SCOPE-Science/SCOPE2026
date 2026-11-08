---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

PASS: Two-interval Markov model has primitive transition and T_t² uniformly expanding for every 0<t<1; its transfer-invariant density is h_A=(1+t)^{-1} and h_B=(1-t²)^{-1}. Integrating affine densities yields exact 4×4 transfer matrix with charpoly (λ−1)(λ+t)(λ²+(1−t)²λ+t²), all nontrivial spectral roots inside unit disk. Centered observable covariance is J M^n v; resolvent J(I-zM)^{-1}v reproduces stated rational function, 2G(1)−G(0) gives positive CLT variance. Quadratic discriminant (t²+1)(t²−4t+1) and nonzero numerator at z=−1/t_* establish uncancelled order-three pole; residue gives 1/4−sqrt(3)/8. Derivative q(t) strictly increases with root t_var< t_*=2−sqrt(3), entropy derivative log((1−t)²/t) gives t_ent larger. Independent exact-symbolic rational checks of transfer resolvent, variance and resonant leading term at four distinct t corroborate, not prove general theory.

## originality

PASS

Best-knowledge PASS after exact statement/implication comparison, Resultary searches and inspection of relevant primary source material. Classical ingredients, partial coverage and specific inaccessible-source risks are credited; no exhaustive historical priority claimed.

## value

PASS

PASS: For a natural tunable-mean Markov chaos family, a closed entire autocovariance spectrum and CLT variance answer genuine fluctuation questions. Third-order pole at a sharp internal parameter and strict separation of variance, correlation and entropy optima are substantive dynamical structure, not merely recomputation of stationary mean.

The dated certificate retains the supplied scientific assessment, sources and limitations.
