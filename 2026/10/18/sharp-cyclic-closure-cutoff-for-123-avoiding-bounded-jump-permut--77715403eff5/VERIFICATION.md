---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

Classical 123 avoidance with linear jumps |π_(i+1)-π_i|≤m implies π_1≥n−m: the first subsequent term above π_1 must be n, and its predecessor is at most π_1 but within m of n. Applying reverse-complement gives π_n≤m+1. The cyclic closing jump then imposes n−2m−1≤π_1−π_n≤m, hence n≤3m+1; m=1 cannot host an n≥3 simple Hamiltonian cycle. For m≥2 the displayed five-block witness W_m at n=3m+1 is a permutation, 123-avoiding, has maximal edge jump m including its closing edge. For 5≤n<3m+1 choose r=ceil((n−1)/3)≤m and delete 0,1,2 largest entries from W_r; new jumps stay ≤r; n=3,4 use explicit tuples. At equality all endpoint inequalities are equalities; the first exceeding n−m is n immediately after π_1, and reversed complement forces π_(n−1)=1. This proves every claimed quantifier and boundary. Independent direct permutation enumeration compared all 24 pairs (n=3..8,m=1..4), forced endpoints and exact existence, with no counterexample. These tests are finite; the all-parameter proof is the endpoint argument and construction.

## originality

PASS

Nadler 2026 treats 123 avoidance with linear bounded adjacent jumps and Hamiltonian paths, and obtains reverse-diagonal localization, but not adding the cyclic closing edge, the sharp n=3m+1 cutoff or all four forced positions. Novelty is the exact cycle closure, not the known linear localization.

## value

PASS

Adds a natural Hamiltonian-cycle extremal property to a studied family of pattern-constrained Hamiltonian paths and establishes the exact maximum feasible length with a rigid four-position boundary. The all-n construction and sharp boundary are useful combinatorial structure, not an arbitrary short census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
