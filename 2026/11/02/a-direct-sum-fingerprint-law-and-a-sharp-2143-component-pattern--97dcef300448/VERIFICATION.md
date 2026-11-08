---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

The inversion-graph components equal 1 plus the number of proper direct-sum cuts J_k. Conditioned on J_k, left and right position blocks are independently uniform permutations of their respective value intervals. Cross-block pattern probability is 1_{j in D(tau)}/(j!(m-j)!) instead of 1/m!, and weighting by Pr(J_k)=1/binom(n,k) proves the universal finite sum. For 2143 only j=2 is a cut, giving (-1,5,-1)/24 coefficients. Independent brute force of uniform permutations n=4..7 and exact rational evaluation of n=4..39 verified the coefficients and sign. For n>=40 the proof preserves negative endpoint terms giving -D_n and bounds interior positive B_k by binomial estimates; D_n>=n²/100 dominates 5n/48 for n>=40, so all n proved. Finite enumeration alone is not used to infer the infinite sign.

## originality

PASS

Acan–Pittel state the graph-connected iff direct-sum-indecomposable characterization, and Janson–Nakamura–Zeilberger analyze the covariance of pairs of pattern occurrence counts. Neither paper treats this component-versus-pattern mixed statistic or direct-sum-cut fingerprint. The role of 2143 in skew-merged pattern classes is preexisting; no novelty asserted for its definition. Best-knowledge PASS for the full mixed covariance and sharp reversal.

## value

PASS

The statistic couples global inversion-graph block structure with local pattern counts and reveals a surprising all-size sign reversal at a sharp finite boundary. The universal dependency only on a pattern direct-sum fingerprint is a nontrivial structural classification relevant to random permutation statistics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
