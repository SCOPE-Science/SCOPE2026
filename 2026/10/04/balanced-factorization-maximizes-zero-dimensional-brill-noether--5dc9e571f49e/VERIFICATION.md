---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The proof has two independent layers.

First, the infinite argument is symbolic. The Brill--Noether condition \(\rho=0\) is converted exactly to \(ab=g\). The classical formula is converted exactly to the hook-length formula for an \(a\times b\) rectangle. For two fixed-area rectangles \(a\times b\) and \(c\times e\) with \(a<c\le e<b\), the cumulative hook counts are compared on every threshold interval. The only non-linear interval is handled by a concave quadratic in the tail parameter, whose two endpoint inequalities follow from \(ab=ce\), \(c>a\), and \(e\ge c\). The final tail comparison uses \(a+b>c+e\). This gives coordinatewise dominance of sorted hook lengths and therefore strict hook-product decrease under balancing.

Second, `artifacts/verify.py` is an exact-integer regression checker. It checks all genera \(2\le g\le300\), all divisor rectangles with first factor at most \(\sqrt g\), every pairwise cumulative-hook comparison, equality between factorial and hook-product forms of the Castelnuovo count, transposition symmetry, and the Serre-dual degree identity. The executed package-path checker returned:

`VERIFY_OK`

`genera_checked=299`

`factor_pair_comparisons=1407`

`max_genus=300`

The finite range is not extrapolated. It is only a regression test for the exact formulas used in the proof.
