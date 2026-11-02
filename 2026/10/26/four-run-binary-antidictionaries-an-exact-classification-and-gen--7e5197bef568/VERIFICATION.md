---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For all a,b,c,d>=1 on binary linear word 0^a1^b0^c1^d, a minimal absent contiguous word x is exactly a missing factor with both length-|x|-1 prefix and suffix present; this implies every proper factor present. Reconstruct one-run forbidden powers and two-run downward-closed factor rectangles, the forced full inner exponents in three-run factors, and the two possible four-run shapes. Five or more-run candidates fail a boundary deletion condition. Each of the displayed ten disjoint word families follows by these necessary-and-sufficient tests. Counting yields |A(T)|=b+c+(1+[a>c])(1+[d>b]); the two comparison flags factor as independent weighted pair generating functions F0=uz²/((1-uz)(1-uz²)), F1=uz³/((1-z)(1-uz²)), giving uF0²+2u²F0F1+u⁴F1². At fixed length n, n-1 is the maximum except the unique n=6 word (2,1,1,2) up to alphabet exchange attains n. Independently programmed all factors and every minimality test (NOT using submitted verify.py), obtaining exact set equality for 1,090 positive quadruples with length <=17, including equal-run and extreme comparisons; finite test corroborates the proof but is not proof of all positive lengths.

## originality

PASS

Fresh best-of-knowledge statement-and-implication comparison across standard aliases, general theorems and exact tables. Inspected primary material does not establish the same final claim at the assessed level, although stated full-text access gaps and unindexed equivalences leave explicit priority risks. A general algorithm can *in principle* output any individual instance, but does not mechanically imply a closed formal generating series across all lengths without the four-run factor-region analysis. The precisely bounded contribution survives.

## value

PASS

This is a complete natural subfamily classification of a canonical string-combinatorics invariant: exact antidictionaries encode forbidden factors used in compression and pattern matching. The multiplicative correction to baseline b+c, the two-parameter length/count spectrum, and unique length-six extremum are independently useful exact facts not stated by general output-sensitive RLE-MAW algorithms. It does not claim a faster general MAW algorithm or a theorem for arbitrary run count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
