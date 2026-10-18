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

For binary weight-two cyclic words, distinct disjoint supports produce a four-element symmetric difference with at least six affected windows for n>=6. Supports sharing one endpoint leave two differing coordinate positions; their triple-window supports are disjoint iff their cyclic distance is >=3. Thus feasible codes equal edge sets whose every vertex neighborhood is 3-separated on C_n. Handshake gives |E|<=floor(n floor(n/3)/2). When n=3m, a degree-m neighborhood is one residue class mod3; three fully saturated residue classes would force a fixed-point-free involution on three labels, impossible, forcing at least m missing degree units. K_{m,m} disjoint K_m attains m(3m-1)/2. Explicit circulants +/- (3j-1) with optional antipodal edges or Hamilton cycle matching attain floor(nm/2) for other residues. Independent constructed graph checks n=6..45, direct triple-read pair distances through n=22, and independent exhaustive maximum independent sets n=6..9 (5,7,8,12). The infinite result depends on the proof, not tests.

## originality

PASS

A fixed-Hamming-weight-two optimum in the cyclic three-symbol read metric, equivalently alpha(F_2(C_n²)), is not supplied by published ordinary-cycle token graph independence nor by b-symbol-weight bounds/linear codes. Exact divisible-by-three degree deficit is an additional nonstandard combinatorial argument; historical equivalent token graph results remain possible.

## value

PASS

Determines a natural exact constrained coding capacity at every length, with a sharp arithmetic obstruction (m/2 loss when n divisible by three) and constructive optimal configurations. Fixed-weight layers are relevant to constrained read-channel design; all lengths rather than an arbitrary small tabulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
