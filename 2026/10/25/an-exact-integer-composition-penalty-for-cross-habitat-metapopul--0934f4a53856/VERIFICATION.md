---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For every integer N>=2 and 1<=k<N under δ>max{a(N−1),b(N−1)}, the positive Perron eigenvalue belongs to the symmetric 2×2 quotient T_k, and δ above both diagonals makes det(δI−T_k)<0 equivalent to c²>R(k). The ratio s=k/(N−k) yields R=(UC/s+BVs+UV+BC)/N², unique s0=sqrt(UC/BV), R0=(sqrt(UV)+sqrt(BC))²/N²; square completion gives exact penalty sqrt(UBVC)*(k−k0)²/[k k0 (N−k)(N−k0)]. Floor/ceiling restrict all integer minimizers, including N=2 boundary; equality c=c_crit is not strictly supercritical. Independent 1,595 rational-parameter checks plus N=5 exact fractions confirm, not replace, the proof.

## originality

PASS

Classical metapopulation-capacity thresholds and equitable partitions determine fixed-composition spectra but do not, in the inspected literature, give the all-integer optimum and exact positive rounding penalty. The algebra is elementary once the block model is chosen, so historical implicit-derivation overlap is a genuine risk; best-of-knowledge not absolute priority.

## value

PASS

Finite habitat counts are inherently integer and can create strict false-positive capacity windows under continuous relaxation; the exact rounding cost and two-candidate criterion provide a motivated resource-allocation boundary even though this deliberately idealized model is not a stochastic survival theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
