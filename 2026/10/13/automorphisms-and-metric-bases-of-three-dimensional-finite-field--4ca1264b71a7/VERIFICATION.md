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

The standalone `verify.py` artifact was read from its actual packaged path before replay.

For \(q=3\) and \(q=5\), it independently constructs the projective quotient of \(TD(\mathbb F_q,3)\), checks the isotropic/anisotropic degree split, and exhaustively enumerates all quotient graph automorphisms. The counts are \(24\) and \(120\), matching the prime-field values \(q(q^2-1)\).

It then constructs the full vector graph, recovers exactly \(q^2+q+1\) maximal twin classes of size \(q-1\), confirms diameter two, and verifies that selecting all but one vector from every class gives a resolving set of size \((q^2+q+1)(q-2)\).

The checker also verifies the closed determining/metric cardinality identity and minimum-set count algebra for \(q=3,5,7,11\).

Exact replay output:

```text
p=3: quotient_vertices=13, quotient_aut=24, twin_classes=13, determining_metric=13, canonical_basis=OK
p=5: quotient_vertices=31, quotient_aut=120, twin_classes=31, determining_metric=93, canonical_basis=OK
symbolic count checks OK
VERIFY_OK
```

The finite calculations corroborate the proof. The arbitrary odd prime-power statement rests on the projective-polarity reconstruction and the semilinear fundamental theorem, not on finite enumeration.
