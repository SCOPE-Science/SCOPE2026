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

`verify.py` performs an exhaustive exact enumeration for \(2\le a<b<c\le1215\). It factors integers through \(1216\), maps them to prime-exponent vectors, assigns every multiplicatively independent pair a primitive Pluecker key for its rational two-plane, enumerates all monochromatic triangles, and then applies the same rank-two test to the translated triple.

The finite completeness argument is exact: every maximal-rank dependent triple has three independent pair edges spanning one common rational two-plane, and every triangle with a common primitive Pluecker key has three exponent vectors of rank two. No relation-exponent cutoff is introduced.

The program asserts that there are 15 unordered consecutive maximal-rank triples through \(1215\), 13 through \(1000\), and exactly two above \(1000\), both at \(1215\). It also checks the explicit multiplicative identities for the boundary witnesses and the ordered counts \(M(1214)=78\), \(M(1215)=90\).

Expected output:

`VERIFY_OK H=1215 total_unordered=15 le1000=13 new_at_1215=2 M1214=78 M1215=90`

This verifies only the stated finite range. It does not establish any claim for \(H>1215\).
