---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The finite cyclic stage embedding and Feynman–Kac give the simple Perron eigenvalue for every initial phase. Multiplying the positive eigenvector ratios gives A_+^p A_-^q = λ_+^p λ_-^q with A_± positive; the product increases from zero to infinity above the larger diagonal threshold. Implicit logarithmic differentiation gives Λ′ = v(p/A_+ − q/A_-)/(p/A_+ + q/A_-) and Λ″(p/A_+ + q/A_-) = p(Λ′−v)^2/A_+^2 + q(Λ′+v)^2/A_-^2 > 0. At positive tilt A_- = A_+ + 2vθ + λ_-−λ_+, so A_+ tends to zero with the stated positive coefficient and power −q/p; swapping signs gives −p/q. These also yield the slopes ±v, intercepts −λ_±, and θ(v−Λ′)→0 at the positive edge (with the sign-reversed counterpart). Thus the Legendre rate has the stated endpoint limits; exponential tightness and Gärtner–Ellis on the interior give the full LDP, including open neighborhoods of the endpoints. Taking the positive p-th root when p=q gives the Markov quadratic, whose Legendre transform gives the displayed rate. Conversely the conjugate rate determines the pressure; the intercepts fix the comparator rates and its inverse-first-power edge law forces p=q. The ballistic atom for a fresh plus run is the Erlang survivor. Line 4's phrase 'family of unequal Erlang stage counts' is infelicitous; the explicit quantifiers in line 6 and classification in line 23 include equal counts and are consistent.

## originality

PASS

Pass the complete two-sided Erlang classification and edge-ratio discrimination, not the underlying model, classical Markov rate or symmetric Erlang-2 example as separate contributions. The strongest inspected catalogue overlap is an exact special case, not a dominating result; accessible literature evidence does not establish earlier equivalent or stronger coverage of the boundary. This is not a priority finding.

## value

PASS

The pressure is a natural observable for discriminating holding-time models from displacement. An exact alias/no-alias boundary and a positive, reciprocal-power signature of the directional shape ratio give a usable identifiability result, in contrast to a comparison of a few cumulants or examples. The ballistic atom shows what the rate discards.

The dated certificate retains the supplied scientific assessment, sources and limitations.
