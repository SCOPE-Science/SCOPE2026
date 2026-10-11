---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

The boundary-one length-two symmetry follows directly from the published triangle relation: on three consecutive vertices all four boundary factors are \(1\), forcing \(c_{i,i+2}=c_{i+2,i}\). Applying the two oriented published exchange relations to four consecutive vertices of the pentagon gives \(q_i=q_{i+1}^{-1}+q_{i+1}^{-1}q_{i+3}\) and \(q_i=q_{i+1}^{-1}+q_{i+3}q_{i+1}^{-1}\); multiplying on the appropriate side yields \(q_iq_{i+1}=q_{i+1}q_i=1+q_{i+3}\). Thus adjacent quiddity entries commute. Since \(q_i\) also commutes with \(q_{i+4}\) and \(q_{i+4}=q_{i+1}q_{i+2}-1\), cancellation by the unit \(q_{i+1}\) gives \(q_iq_{i+2}=q_{i+2}q_i\). Every pair on five indices has cyclic distance one or two, so all pentagon values commute. The height-one relation \(ab=2\) makes its two internal units commute, while the cited quaternionic height-three example contains noncommuting quaternion units, proving sharpness of the height threshold.

## originality

PASS

Best-of-knowledge originality survives. The 2025 foundational paper supplies the general noncommutative triangle/exchange calculus, and the 2026 division-ring paper studies finiteness and explicit quaternionic behavior, but targeted searches found no theorem stating that every boundary-one pentagon is forced commutative or that height three is the sharp first possible noncommutative height. The submitted result is not a title-level restatement: it extracts a rigid low-height consequence by using both orientations of the exchange relation and a nontrivial cyclic cancellation.

## value

PASS

The theorem identifies a sharp structural threshold: boundary-one noncommutativity is impossible for quadrilateral and pentagon friezes over any division ring, while a quaternionic height-three example exists. That is a natural complete low-height classification and explains where genuinely noncommutative behavior can first occur; it is more than a tiny numerical instance or arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
