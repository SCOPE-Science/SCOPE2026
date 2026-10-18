---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Read full RESULT.md, verification-code symbolic identities and PSD trace dual construction. Reflection decomposition gives one centered eigenvalue in each parity sector at Λ, with other eigenvalues >Λ certified by explicit positive Bernstein coefficients; F(u) strictly decreases from 16 to 0 on (sqrt(2/5),4/5) by six-coefficient Bernstein negativity. Independently checked in SymPy the exact derivative factorization F′ and F(sqrt(2/5))=16, F(4/5)=0; the source verifier further supplies all eigenvector/distance/endpoint symbolic identities and the displayed proof derives arbitrary (not just symmetric) global upper bound from PSD X and uniqueness by equality conditions. For t>=16 Rayleigh centered v=(-2,-1,0,1,2) gives λ2<=1/10 with deletion for >16 and explicit q-family at equality t=16; endpoint polynomial determines precise allowed q range. This is an all-real-price analytical proof, not a numerical search.

## originality

PASS

The 2006 Sun–Boyd–Xiao–Diaconis primary paper §5.3 explicitly covers cycles with EQUAL costs and the general SDP/dual, §5.2 covers paths with arbitrary costs, not the globally all-t solution for a cycle having exactly one exceptional price and its nonunique critical continuum t=16. Boyd–Diaconis–Parrilo–Xiao (2009) optimizes discrete-time SLEM and symmetry reductions; cannot imply this continuous-time weighted price transition. The submitted global trace-dual and all-optima classification add nontrivial exact parametric information, originality PASS with a narrow undiscovered priced C5 risk.

## value

PASS

A sharp price-induced nonuniqueness and edge-deletion transition with all optimal conductances in a minimal nontrivial odd cycle is a motivated spectral optimization classification. The exact critical 16 and continuum of optimizers supply useful structural boundary data beyond merely computing a numerical SDP.

The dated certificate retains the supplied scientific assessment, sources and limitations.
