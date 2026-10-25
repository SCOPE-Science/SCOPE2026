---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

Reconstructed barycentric Reeve-prism horizontal fiber: only one horizontal lattice translate contributes a.e. and vertical interval length 1+mT with T=min(x,1−x,y,1−y). For independent uniform x,y, P(T>t)=(1−2t)^2 on [0,1/2]; a random vertical shift rounds interval occupancy to floor/ceil. Integration gives exact cubic positive-part tails P(N>=k)=(m/6)[(1−2(k−2)/m)_+^3−(1−2(k−1)/m)_+^3], correct support, P(N=1)=2/m−4/(3m²), mean 1+m/6, variance m²/72+1/6−(1−(−1)^m)/(48m²). Independent Fraction integration of tails and moment identities was exact for m=2..35; general proof is integral, not extrapolation. Orbit-volume counting yields unique coverage fraction 4(3m−2)/(m²(m+6)); |N/m−T|<=2/m a.e. proves limit law.

## originality

PASS

The original Lian–Xue paper owns the minimal eight-vertex Reeve-prism construction, fiber bounds and volume. Its inspected §4.2 does not calculate the entire integer-translate occupancy distribution or parity-sensitive second moment. The exact cubic-tail distribution with attainable multiplicities up to order m/2 and essential coverage fraction is a separate explicit natural classification; known octahedral optimal lattice profile concerns a different convex body and lattice.

## value

PASS

A natural distributional invariant of a canonical minimal lattice covering family is determined for all m>=2, not merely a selected height. Its exact limit law, parity variance and decay ~12/m² of the genuinely essential fraction contrast irredundancy with growing multiplicity. The calculations materially refine understanding of the already-known construction, despite using its public fiber formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
