---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For any reversible edge-flow matrix F on K_{p,q}, total T≤a, the bipartition cut contrast Rayleigh quotient is 1−T/(ab). Compression to the q−1 zero-sum subspace of larger-mass part has average 1−T/b, hence SLEM ≥max(1−T/b,|1−T/(ab)|). Uniform F_ij=T/(pq) exactly attains bound: eigenvalues 1, 1−T/a (p−1), 1−T/b (q−1), 1−T/(ab). Scalar minimax uniquely gives T*=a for a≤1/3 or 2ab/(1+a) for a≥1/3. Equality of the W_B average with spectral maximum makes every vector W_B an eigenvector, forcing rowwise equal F; when T*=a row capacities force equal row sums, and when T*<a the negative cut eigenvector forces equal row sums. Therefore unique kernel even without symmetry assumptions; MH T=a optimal iff a≤1/3. Independent rational and numerical eigenvalue checks corroborate.

## originality

PASS

PASS for explicit all-two-mass SLEM and global uniqueness among arbitrary nonsymmetric feasible reversible kernels; uniform-stationary case is previously known.

## value

PASS

A closed-form optimum and unique kernel for a natural nonuniform reversible network design problem, including a sharp Metropolis threshold, are directly useful in spectral Markov-chain optimization; the all-asymmetric rigidity is mathematically substantive.

The dated certificate retains the supplied scientific assessment, sources and limitations.
