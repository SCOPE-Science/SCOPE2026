---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Complementarity K_Hc(x)=-K_H(x) for x≠0 and K_Hc(0)=7-|H| reduces any cardinality m≥4 to complement size≤3 with strictly better ratio. For singletons C=2/7. For pairs, translation and nonzero rescaling reduce the denominator and show best step ±1 with exact 2sin(pi/14)cos(pi/7)<0.41. The 35 triples split exactly into affine orbits 21 arithmetic progressions and 14 translates/dilates of the Fano difference set {0,1,3}; the latter has all nonzero Fourier moduli sqrt(2) and ratio <1/4. AP triple optimal step ±1 gives stated cosine quotient. Exact real cyclotomic elimination yields 97gamma^3+44gamma^2−20gamma−8=0 with unique positive root bracket (11/25,441/1000). Independent clean Python enumerated all 127 nonempty H and found exactly seven translated AP triples with gamma=0.4402496918696975 and polynomial residual <2e−15; the mathematical partition and algebra, not floating exhaustive comparisons alone, establish exactness.

## originality

PASS

The original Bonami–Révész primary text explicitly defines gamma_p^sharp(q) via EXACT SAME finite-group normalization and notes unknown sharp constants for p≠2; its results concern uniform/asymptotic q behavior, not a q=7 table. Exact published two-frequency and three-frequency projection results do not give the all-127-support optimum or equality classification. Bounded searches found no independently covering q=7 table; retain risk of an older unindexed computation.

## value

PASS

This is a natural fixed-prime exact evaluation of the finite cyclic p=1 concentration invariant explicitly defined by Bonami–Révész, with a complete 127-support classification and exact equality orbit. The arithmetic-progression versus Fano difference-set comparison explains the extremizer mathematically; although small and self-contained, a future researcher comparing endpoint finite moduli could need the exact q=7 value rather than a numerical experiment. It is not an arbitrary unmotivated slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
