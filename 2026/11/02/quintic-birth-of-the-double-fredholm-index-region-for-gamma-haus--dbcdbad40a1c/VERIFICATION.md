---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Galanopoulos et al. root-count theorem gives Fredholm index as count of preimages of (s/(s−1+z))^α in Re(z)>0, assumed as a published input. The substitution w=s/(s−1+z) maps this half-plane onto |w−R/2|<R/2 with R=s/(s−1), so polar preimages φ_k=(θ+2πk)/α satisfy |φ_k|<π/2 and r<R^α cos^αφ_k. For 2<α<4 a second branch only near negative ray θ0=π(2−α/2)<|θ|≤π; its radial cap is smaller. Two sector area integral is α R^(2α)∫_(π/α)^(π/2) cos^(2α)u du. At α=3 the trigonometric integral yields (5π−9√3)R^6/32. With ε=α−2 and δ=π ε/(2α), sin(v)~v uniformly near zero yields area/ε^5→π^5 R^4/2560. Independently integrated α=3 (R=1), obtaining 0.0037345624946584647 versus exact 0.0037345624946584777, and checked numeric ratios for ε .03, .01, .003. The finite checks do not prove the operator theorem.

## originality

PASS

The 2026 Galanopoulos–Mahillo–Oliva-Maza–Siskakis theorem already gives complete spectral and index root count for these operators; no new spectral theorem is claimed. The assessed contribution is the full 2<α<4 double-index planar domain, its area and the sharp fifth-order onset. Searches found no exact area law; this is a quantitatively computed natural invariant, although a geometric special case of the general source formula and possibly known earlier as tangent-disk power image. Full recent primary source could not be downloaded in this run; qualified PASS based on available statements and direct derivation rather than assertion of absolute priority.

## value

PASS

Measuring the planar region with an extra Fredholm defect near the first parameter where it exists is a natural phase-transition invariant for the given Gamma Hausdorff family. The all-order interval, precise α=3 value and fifth-order onset distinguish it from a single arbitrary sample, despite reliance on the prior root-count theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
