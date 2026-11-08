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

For W=0^a1^b0^c1^d0^c1^b0^a with strictly positive a,b,c,d, good forbids factors u complement(u) of half-length>=2 (order-one allowed). The order-two four forbidden words force each adjacent run pair to include a singleton and no interior run of length 2, and order-three alternating antisquare excludes b=c=d=1. Consequently exactly three disjoint families survive the short filters. The imported complete minimal-antisquare classification of Baranwal et al Theorem 11 reduces all longer obstructions to rotations of 0^k101^k01 for k>=3. In family 1 all zero-runs are singleton, in family 2 all one-runs are singleton, excluding longer rotations. In family 3 the unique long 1-run must be central and a cyclic rotation fits iff d<=2a (the split long zero-run draws from two outer blocks), yielding sharp d>2a. GF follows bijective run lengths: 2*( z^10(z+z³/(1-z))/(1-z²)+z^11/(1-z²)^2+z^9/((1-z)(1-z^4)) ). Independently enumerated every quadruple 1<=a,b,c,d<=7 (2401) with literal antisquare checks; exact match. Full all-parameter proof uses imported theorem, not finite test.

## originality

PASS

Best-of-knowledge originality after checking exact formulations, stronger work, tables and implication: Good word equals binary word avoiding antisquares of order>=2. The palindrome/run restriction is strictly narrower than unrestricted avoidance, but the claimed mathematical result is an explicit exact classification and enumerator not merely forbidden-factor restatement. The general forbidden-pattern description is stronger in object scope and can mechanically decide any given W, but the exact run parameter inequalities and complete generating function require additional nontrivial derivation. Distinguish derived new specialization from claiming new minimal antisquares. An algorithm implicit in the stronger general antisquare characterization is not the explicit equality of three parameter families and rational generating function. The latter is an original worked-out natural structural specialization subject to unindexed priority risk.

## value

PASS

Natural first palindromic maximal-run stratum where long minimal antisquare rotations impose a genuinely new central-versus-boundary threshold, and a complete rational enumerator by word length. It extracts a sharp structural condition rather than merely reprinting a known forbidden-pattern table; meaningful for symmetry-restricted factor avoidance and counting.

The dated certificate retains the supplied scientific assessment, sources and limitations.
