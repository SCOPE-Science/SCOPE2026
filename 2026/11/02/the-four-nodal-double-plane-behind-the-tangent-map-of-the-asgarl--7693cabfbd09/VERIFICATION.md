---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

The seven simple common zeros of yz(3x-s),xz(3y-s),xy(3z-s), s=x+y+z, are precisely three coordinate vertices, three points on a coordinate line with s=0, and [1:1:1]. The seven-point cubic evaluation matrix has rank 7; the three cubics give the complete base-point-free anticanonical net on the blowup. The generic inverse λ obeys abc λ²-2(ab+ac+bc)λ+3(a+b+c)=0 after removal of the base-point root. Its discriminant B=(ab+ac+bc)²-3abc(a+b+c) factors over roots of unity into two nonsingular conics meeting transversely at the four explicit rational points, hence precisely four A1 surface singularities. Strict transforms of x=0,y=0,z=0,s=0 have self-intersection -2 and resolve them. Frobenius either fixes both conics (2q-2 branch points if q≡1 mod3) or exchanges them (4 if q≡2 mod3), for finite fields char>3. Verified factorization symbolically, all cubic base equations and rank, and branch counts q=5,7,11,13; these finite checks are not the proof for arbitrary q.

## originality

PASS

PASS, best-of-knowledge: special four-node split-conic discriminant, explicit seven-point anticanonical resolution and Frobenius branch counts are not covered by the already published tangent-filling theorem or the known contact/deck-involution calculation. Classical Geiser geometry is prior framework, not a tabulation of this special net; an equivalent classical explicit Geiser computation remains possible.

## value

PASS

The map is canonical for a published finite-field tangent problem, and the complete branch configuration, ADE degeneration, exceptional -2 curves and Frobenius splitting provide natural geometric/arithmetic invariants unavailable from mere tangent contact counts. This is a structural classification of a particular nonarbitrarily chosen map, not a one-off unmotivated polynomial expansion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
