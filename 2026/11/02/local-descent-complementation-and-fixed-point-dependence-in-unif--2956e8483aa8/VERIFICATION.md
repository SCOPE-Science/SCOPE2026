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

For n>=3 uniform involutions, the adjacent-label map that exchanges two fixed singleton cycles with their transposition, otherwise conjugates by (j,j+1), is a genuine involution. Case analysis shows that it toggles D_j while preserving the entire remote fixed-indicator vector, proving joint (not just pairwise) independence within every admissible fiber. Conditioning on a local fixed site counts (j-1)T_(n-3) or (n-j-1)T_(n-3) favorable pairings; the telephone recurrence gives the exact two-diagonal covariance matrix, Cov(F,D_j)=-T_(n-2)/T_n, and endpoint/interior distinctions, with interior n=3 equality. Verified independently by exhaustive enumeration of every involution n=3..8, fiber by fiber and rational covariance entry by entry; finite tests support but do not replace the bijection.

## originality

PASS

The novelty assessed is the remote-FIXED-LOCATION joint independence and complete site-specific covariance matrix, not classical univariate involution Eulerian numbers or aggregate fixed-count/descents identities. Chow's 2008 involution Eulerian enumerators retain total fixed counts, not the vector of named fixed statuses. The nearest published result for uniform *permutations* has a different law and Cov(F,D)=-1/n, and does not cover the involution conditional fibers. Relevant older descent-set/cycle-type algebra is a residual potential for an implicit positional specialization.

## value

PASS

The fiberwise independence is a nontrivial local-symmetry classification for an important restricted permutation measure, strictly stronger than zero covariance. The exact mixed covariance matrix and its surprising interior negative total-descents correlations are natural statistics for random involutions, with potentially reusable local-complementation map.

The dated certificate retains the supplied scientific assessment, sources and limitations.
