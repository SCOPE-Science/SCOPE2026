---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

The published complete parity-resolved Parikh spectrum gives j=#1 every integer in [p_n,q_n] and c=#0−#2 equal 0 when n−j even or both ±1 when odd. It also gives p_{4n−1}=n+p_n−1, q_{4n−1}=n+q_n, so q_{n_k}−p_{n_k}=k+1. For an allowed (j,c), total weight is ((a0+a2)n−Aj+Ec)/2. Equal weight requires AΔj=EΔc, with parity Δj≡Δc mod 2 and |Δc|≤2. If A≠0 and A∤E this forces Δj=Δc=0. If A=0, at most three weighted sums occur vs at least k+2 Parikh vectors. If A divides E, h=E/A, disjoint c=+1 at j versus c=−1 at j−2h pairs yield at least max(0,floor((k+2−2|h|)/2)) collisions, diverging. This is an actual infinite proof conditional on the published full-spectrum theorem; the finite verifier is not its replacement.

## originality

PASS

The 2014 result already provides the full ternary Thue Parikh spectrum and is credited as the nonstandard premise. The 2024 additive-word paper proves only the special sufficiently separated weight ray (0,1,λ), λ≥5. Applying parity/congruence arithmetic to classify every integer triple, including zero and negative weights, and proving an unbounded deficit on an explicit subsequence was not stated in the inspected sources; the earlier special theorem follows as a proper corollary.

## value

PASS

Integer valuation preserving abelian distinction is a natural combinatorics-on-words question explicitly posed through prior special rays. The complete necessary/sufficient arithmetic phase diagram and quantitative divergence for all excluded weights settle the motivated projection question on this canonical ternary word; not a narrow brute-force table or a weight-relabeling alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
