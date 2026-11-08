---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

The first successful A at part i leaves exactly two irreversible possibilities: an opposite B in the same part before any accepted A outside i permanently blocks every other part, so all of i eventually fills; an A outside i first bans all B thereafter and eventually fills N vertices. For a=n_i and b=N-a the full-coverage probability conditional on the first A is bp∫_0^∞exp(-bpt)(p+q exp(-t))^(a-1)dt; binomial expansion gives F_i^(A) and the B-symmetry gives F_i^(B), whence w_i=(a/N)(p(1-F_A)+q(1-F_B)). Finite support is only n_i and N (aggregate equal part sizes). Rescale the exponential race by N and apply bounded convergence for fixed positive limiting proportions: part-only limiting mass α_i²pq[( (1-α_i)p+α_i q)^(-1)+((1-α_i)q+α_i p)^(-1)]. At p=1/2, balanced r parts give masses 1/r at 1/r and 1-1/r at full coverage with positive variance (r-1)^3/r^4. For K_(n,n), J~Bin(n-1,1/2) and F_n=E[n/(n+2J)]; centered fourth-moment expansion yields 1/2+3/(8n)+O(n^-2). Endpoints p∈{0,1} separately yield complete coverage; r>=2 and n_i>=1 essential. Independently coded exact absorbing-state recursion matched exact formula in independently selected small multipartite graphs; only proof covers arbitrary sizes.

## originality

PASS

Best-of-knowledge PASS for complete finite-jamming distribution, growing multipartite mixture and balanced 3/(8n) correction. The exact same repeated-attempt antagonistic species dynamics are known from Martins–Dickman–Ziff, but their published 1D/2D lattice jamming/percolation results do not logically determine this all-part-size finite absorption law. One-species greedy RSA and equilibrium Widom–Rowlinson partition functions use different dynamics or statistics. Classical exponential race techniques are not credited as new. General unlocated absorbing-rate formula remains possible.

## value

PASS

Exact law for a physically defined nonequilibrium irreversible process across a canonical dense graph family, including a nontrivial non-self-averaging limit and sharp finite-size bias; not merely a numerically observed phase or a formula for a contrived small graph.

The dated certificate retains the supplied scientific assessment, sources and limitations.
