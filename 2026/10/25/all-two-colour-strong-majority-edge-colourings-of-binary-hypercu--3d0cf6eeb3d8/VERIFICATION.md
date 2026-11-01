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

For each edge uv of sign s=+1(red)/-1(blue), exactly d-1 adjacent red edges is equivalent to R(u)+R(v)-d=s, i.e. f(u)+f(v)=s for f=R-d/2. Summing over incident edges yields Af=-(d-2)f. Walsh diagonalization of Q_d confines f to co-singleton characters, and the unit edge signs force each coefficient to be epsilon_i/2. Thus every colouring has the unique asserted direction-parity form; conversely, toggling direction i reverses the two adjacent direction-j edge signs for each j!=i, proving sufficiency. Exactly 2^d named assignments, 2^(d-1) up to colour exchange; index 2, for all d>=4. Independently enumerated all 2^4 and 2^12 candidate edge assignments in dimensions 2 and 3 and recovered 4 and 8 legal assignments; the general proof is spectral, not enumeration.

## originality

PASS

Comparison is by exact mathematical statements, quantifiers and implications, with strong prior premises acknowledged; best-of-knowledge historical priority subject to the explicit unread-paper and alias risks.

## value

PASS

Exact classification and unique sign-parameterization of every optimal two-colour assignment on fundamental unbounded-degree cubes, including the exponential 2^d count, is a motivated structural graph-colouring result, not simply a prior existence bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
