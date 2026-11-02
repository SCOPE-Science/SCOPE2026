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

For n>=3 in ordinary one-line form, contracted partial-permutation paths give E[C|three assigned images]=H_(n-3)+number of completed cycles (1,2,3) in the partial assignment; counting loops, two-cycles and two possible three-cycles over all C(n,3) image sets yields t_123=3n-2, t_132=-12a+9n-14, t_213=12a-3n-2, t_231=12a-9n+10, t_312=-12a+3n-2, t_321=-3n+10, each divided by 36*C(n,3). All numerators are 1 modulo 3; endpoint sign switches and total-pattern covariances follow by summing. Independent exact n=3..7 full permutation enumeration checked each covariance and global count; the infinite proof is the contracted-path lemma and symbolic count, not enumeration.

## originality

PASS

The statistic is one-line consecutive triple pattern jointly with cycle count, unlike cycle-word patterns. Published pair-inversion covariance does not determine the intersection events for a triple; surveyed consecutive pattern enumerations alone do not give joint cycle covariance. No equivalent six-function positional formula located, with bounded bibliographic priority risk.

## value

PASS

A complete six-pattern positional mixed-moment table reveals nonzero covariance and sharp within-permutation sign switches at positions depending on the pattern. This resolves a motivated natural joint statistic rather than merely a generic binomial identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
