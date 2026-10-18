---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For n>=2, a vertex of Hamming radius w>=1 first becomes reachable in exactly w steps. Each shortest direction word is a permutation of w distinct flipped coordinates. Uniform coin is a +1 Grover eigenvector, so first-step amplitude 1/sqrt(n) and each subsequent distinct-direction transition amplitude 2/n; (w-1)! same-sign words end in each of w orthogonal coin channels. Squaring gives Pq=w!(w-1)!4^{w-1}/n^{2w-1}; classic Pcl=w!/n^w; ratio=4^{w-1}(w-1)!/n^{w-1}. Stirling for w/n->rho>0 yields exponent rho log(4rho/e), exact sign crossover e/4. At w=n the antipodal asymptotic follows from two-term Stirling. Independent full coined-walk unitary evolution for every w in n=2..6 matched the exact first-arrival probability. This does not infer the all-n theorem from finite evolution tests.

## originality

PASS

The closest paper Kokainis et al 2022 analyzes time-dependent dispersion and Hamming-shell recurrences of the same Grover walk, but not the all-Hamming-weight ballistic first-arrival probability or its exponential comparison to the simple classical coordinate walk. Kempe provides late-time antipodal hitting results, not this frontier profile. The e/4 crossover is specific to comparing first-arrival point mass at linear Hamming distance, with no later-time or hitting-time claim.

## value

PASS

A sharp position-dependent quantum-versus-classical exponential crossover at rho=e/4 across the entire earliest-accessible hypercube shell provides a natural interpretation of shortest-path coherent interference, including a closed antipodal boundary. It is nontrivial despite the short path-counting proof and differs from known later-time quantum advantage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
