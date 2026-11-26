---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For positive data T² applies g in each coordinate and T⁴ applies h=g∘g. The scalar h is increasing and maps into a bounded interval away from zero, so its trajectories converge monotonically to roots and it has no other periods. For m>1, the Schwarzian of g follows from writing it as a fractional-linear map of z^m; it is −(m²−1)/(2z²). The Schwarzian chain rule implies strict convexity of (h′)^(−1/2), so Rolle permits at most three roots; at criticality h′(w)=1 already, so two additional roots are impossible. Above threshold the signs at 0, w±ε and infinity give both outer roots and their signs; the paired-root multiplier q=(m sinh(t)/sinh(mt))²<1 also rules out a pair below threshold (two downcrossings would require an upcrossing at w). For m≤1 use the strict logarithmic contraction after entry into [g(b),b]. The product grid splits into the claimed cycles, with the two lines precisely the union of the saddle stable set and the central fixed point and the boundaries between the return phases; the diagonal derivative supplies the stated multipliers. Recomputed the critical cubic coefficient c=(m²−1)/(6w_*²) and the derivative K=(m−1)²/(m w_*) of h_b′(w(b)). Reciprocal squares give the signed limit 1/sqrt(2c) for four-step return times; dividing the fixed-point expansion by the nonzero phase offset gives s²/(b−b_*)→K/c, with the claimed square-root amplitude. The exact m=2 equations force uv=1 and u+v=b for the nontrivial pair. No numerical premise is used in these arguments.

## originality

PASS

Credit the exact map, known numerical m=2 orbit structure, and standard scalar dynamics and normal-form methods to prior work. The supported distinction is a proved all-real-exponent global basin/period result with exact critical-time and parameter amplitudes for the exact infinite-step Hill map. A later indexed record supplies equivalent coverage of the main mathematics, including the split amplitude by direct expansion; it is not evidence of earlier coverage. The inaccessible 2015 full text leaves a named residual risk.

## value

PASS

The exact tau→infinity model was already used to interpret numerical stable and unstable cycles; this proof identifies all positive basins and exclusion of other periods, including the exceptional separatrices invisible to generic sampling. The two sharp constants quantify distinct slow-relaxation and orbit-birth phenomena near a natural threshold, beyond establishing a local flip or sampling a representative exponent.

The dated certificate retains the supplied scientific assessment, sources and limitations.
