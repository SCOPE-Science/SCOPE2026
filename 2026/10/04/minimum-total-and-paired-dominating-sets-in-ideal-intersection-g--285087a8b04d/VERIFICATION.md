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

The standalone `verify.py` artifact encodes each nonzero proper ideal of a product of \(r\) fields by a nonzero, non-full \(r\)-bit support mask. Distinct vertices are adjacent exactly when the masks have nonzero bitwise intersection.

For every
\[
2\le r\le7,
\]
the verifier exhaustively enumerates all two-vertex total dominating sets and all two-vertex paired dominating sets. It checks that the two families coincide, that each pair satisfies
\[
A\cap B\ne\varnothing,
\qquad
A\cup B=[r],
\]
and that their number equals
\[
\frac{3^r-3\cdot2^r+3}{2}
\]
for \(r\ge3\), with zero such pairs at \(r=2\).

Exact replay output:

```text
r=2 vertices=2 minimum_total_pairs=0 minimum_paired_pairs=0 formula=0
r=3 vertices=6 minimum_total_pairs=3 minimum_paired_pairs=3 formula=3
r=4 vertices=14 minimum_total_pairs=18 minimum_paired_pairs=18 formula=18
r=5 vertices=30 minimum_total_pairs=75 minimum_paired_pairs=75 formula=75
r=6 vertices=62 minimum_total_pairs=270 minimum_paired_pairs=270 formula=270
r=7 vertices=126 minimum_total_pairs=903 minimum_paired_pairs=903 formula=903
VERIFY_OK
```

The finite replay is corroborative only. The general proof is the support argument in `RESULT.md`.
