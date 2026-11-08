---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Polar-area reduction gives t=|z|² and Gamma densities f_j(t)=e^{-t}t^j/j!. For m≥2 the strictly unique maximizer of t^m/(e^t−1) is t_m∈(m−1,m); the dual convex combination α_m f0+(1−α_m)fm≤α_m has only equality radii t=0,t_m, proving all-area upper bound. Two disjoint radial bands with prescribed area weights match α_m A+O_m(A²); single-annulus uniform Lipschitz estimates give e^{−(m!)^(1/m)}A+O_m(A²), strictly worse. Positive strict dual slack implies near-optimal squared-radius area measures weakly converge to p_mδ0+(1−p_m)δ_t_m. At m=1, first-excited Gamma bathtub + f1’=f0−f1 proves exact unique annulus. Independent numerical dual-inequality testing at 5 excitation indices corroborated the analytic argument.

## originality

PASS

Best-of-knowledge: joint fixed-mode small-area minimax and two-radii rigidity, not known individual Fock/Gamma concentration, are the distinct contribution.

## value

PASS

The simultaneous detection of two pure Fock number states is a motivated aperture-design problem. Exact adjacent-vs-nonadjacent support threshold, optimal two-radius split, rigidity of nearly optimal masks and exponentially increasing one-annulus loss are strong nontrivial structural consequences.

The dated certificate retains the supplied scientific assessment, sources and limitations.
