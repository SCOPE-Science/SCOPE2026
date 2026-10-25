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

# Verification record

The proof reduces the spherical width to an edgewise Gaussian range, proves the two-tail point-process limit with independent Bernoulli marks, calculates the Poisson void probability exactly, then upgrades to graph-quenched almost-sure weak convergence with bounded differences and a uniform radial-normalization estimate. The sharp upper tail is proved by an exponential-integral comparison with a finite-mean remainder.

The standalone `checker.py` was executed with NumPy and SciPy. It returned `EXACT_COMBINATORIAL_PASS 1024 120` after enumerating all graphs on five vertices and all coordinate permutations. It returned `FINITE_LIMIT_DIAGNOSTICS_PASS 3000 1400` after 1400 independent graph/Gaussian trials in dimension 3000 and comparisons to two independently sampled descriptions of the limit. These checks do not replace infinite-dimensional proofs, nor do they certify priority or independent verification.

Scope limits: fixed \(p\in(0,1]\), Euclidean zero-sum embedding, weak convergence over random spherical directions conditioned on almost every graph sequence. No claim covers \(p=p_n\to0\) or a deterministic graph solely from edge-density assumptions.
