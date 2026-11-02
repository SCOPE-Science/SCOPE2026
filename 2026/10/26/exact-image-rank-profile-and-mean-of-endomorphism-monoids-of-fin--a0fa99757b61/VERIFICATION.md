---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Every edge-map of C_n (n>=3) has a unique ±1 increment sequence with total 0 or ±n. For odd n only ±n and 2n dihedral endomorphisms; for even 2m, 2m times binom(2m,m) zero-sum bridges plus 4m automorphisms. A zero-sum bridge of span h, 1<=h<=m, has image rank h+1. For s-vertex path traces T_s=sum_{h<s}(s-h)b_h; second differences recover b_h and prove every coefficient. Reflection at first level a yields Pr(max>=a)=binom(2m,m+a)/binom(2m,m), so mean span=4^m/binom(2m,m)-1 and stated mean follows, with central-binomial asymptotics. Independent brute increments for n=3..12 and independent path-walk trace matrix counts for even n=4..12 matched all histograms. No claim for weak endomorphisms.

## originality

PASS

PASS, qualified. The distribution by image CARDINALITY and its exact mean are not the previously published total count or the semigroup minimal generating-set rank; reflection is classical and not new. Primary published total/structure result read; 2009 congruence paper is plausibly relevant but its full text not inspected, residual priority risk.

## value

PASS

The complete rank histogram and mean of *all* endomorphisms of a canonical graph family are natural and useful refinements of its known total count. A path-trace expression with all noninvertible ranks and exact bridge mean is substantively more informative than a recomputed total, without claiming a wider graph classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
