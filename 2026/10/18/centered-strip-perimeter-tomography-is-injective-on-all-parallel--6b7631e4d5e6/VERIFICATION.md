---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The strict disk condition is t<min(C/A,C/B), which gives U+V>t everywhere and open pure chambers at directions perpendicular to each half-edge. In the first pure chamber the full coordinate interval in the a direction remains, and the interval across the strip gives two half-edge lengths C/V and tB/V; the other pure chamber interchanges a and b. In the mixed chamber each of two opposite corner cuts replaces lengths δA/U and δB/V by δC/(UV), with δ=U+V−t: the difference vector has zero projection on u and determinant magnitude δC after multiplication by UV. This verifies the perimeter formula independently of clipping. For continued signed forms X,Y, the sum of the mixed expression at u and −u is 4[(X−Y)(AY−BX)−Ct]/(XY). A pure expression H/L is odd on continuation, and agreement on a nonempty open arc gives a global identity after clearing linear factors. Evaluating the resulting oddness at X=Y≠0 contradicts Ct>0; this argument remains valid when L vanishes there, by continuity of the mixed expression there. Removing finitely many walls and dot-product zeros gives a comparison arc in each pure neighborhood. Linear denominator comparison recovers one edge direction and its support distance C/B, and the other neighborhood recovers the distinct direction and C/A. The intersection of those centered half-plane pairs is exactly the original parallelogram.

## originality

PASS

The closest published theorem is for slab area, and its author explicitly leaves the corresponding perimeter question unanswered by that method. The closest indexed parallelogram reconstructions use distinct observables and often identify only up to similarity or congruence. The checked evidence does not cover the frozen fixed-width Euclidean perimeter theorem. The conclusion is bounded to all parallelograms satisfying the stated strict interior condition and does not assert historical priority or the arbitrary-polygon theorem.

## value

PASS

This resolves the full four-vertex case of a naturally posed perimeter question, including skew parallelograms and unrestricted side ratios. It distinguishes two geometrically different cutting regimes by exact analytic continuation and extracts both edge directions and support distances from a single fixed-width data family, rather than assuming axes known or importing area data. That is substantive even without a stability estimate or a theorem for larger polygons.

The dated certificate retains the supplied scientific assessment, sources and limitations.
