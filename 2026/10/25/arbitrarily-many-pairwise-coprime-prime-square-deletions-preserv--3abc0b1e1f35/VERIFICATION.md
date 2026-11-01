---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Inductively choose p_i ≡1 mod4 larger than twice the previous square scale, using two new distinct auxiliary splitting primes ell_ij,m_ij ≡1 mod4 for each prior p_j. Hensel gives unit roots of -p_j² modulo each auxiliary prime square; CRT joins them with p_i≡1 mod4 and Dirichlet supplies arbitrarily large primes in that coprime progression. Hence every cross sum p_i²+p_j² has two distinct 1 mod4 squared prime divisors, forcing r_2≥36 by Jacobi; a deleted unordered positive distinct pair accounts for at most eight. Diagonal 2p_i² has r_2=12 while its diagonal pair accounts for four. Growth p_i²>2p_(i-1)² makes distinct unordered deleted-root pairs have distinct sums; an alternative representation cannot have both roots deleted. Every finite prefix preserves the full set S+S. Independently verified finite tuple {5,37,89} for all sums ≤15842; no finite test establishes the Dirichlet construction.

## originality

PASS

Comparison is by exact mathematical statements, quantifiers and implications, with strong prior premises acknowledged; best-of-knowledge historical priority subject to the explicit unread-paper and alias risks.

## value

PASS

Unbounded removal from a natural additive two-square basis when deleted roots are distinct primes (hence pairwise coprime) answers a structural arithmetic-support question not met by the earlier all-common-factor construction. The infinite CRT–Dirichlet induction is mathematically substantive rather than a recomputed finite example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
