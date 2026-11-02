---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

Pick gives L_P(n)=(I+B/2-1)n^2+(B/2)n+1 and L_{P×[0,k]}(n)=(kn+1)L_P(n), yielding exactly the stated cubic h* numerator 1+((k+1)(I+B)-4)t+(4kI+(2k-1)B-6k+3)t²+(k-1)It³. Independently expanded the exact cubic discriminant over disjoint chambers I=1+a,B=3+b,k=1+s and I=0,B=4+b,k=1+s. Obtained respectively 72 and 25 nonzero positive-coefficient monomials, constants 0 and 12; first chamber has coefficients 192b,288s,64a² so discriminant vanishes only at a=b=s=0 (the lone I=1,B=3,k=1 double root). The I=0,B=3 case is a simple linear polynomial. In all other degree2/3 cases discriminant is strictly positive and positive coefficients preclude nonnegative real zeros, so all zeros are simple strictly negative. Exact symbolic identities, not the 1848 sampled triples, prove the universal quantified result.

## originality

PASS

Universal real-rootedness for polygon-by-segment prisms is stronger than the prior log-concavity-only segment-factor theorem. Full primary text of Liu 2026, Section 2 Theorem 2.2(i), now read from arXiv article HTML, requires BOTH input h* polynomials to be real-rooted; a polygon with I=1,B=3 has h*(t)=1+t+t², not real-rooted, so that theorem does not subsume this unrestricted claim. Large-width results similarly exclude width-one prisms. Prior Wagner result under real-rooted inputs is credited.

## value

PASS

Real-rooted Ehrhart numerators are a strong algebraic/geometric property. Showing this for every 3D polygon-by-segment lattice prism, including thin prisms with nonreal-rooted 2D base numerator, is a genuine boundary strengthening beyond conditional product-preservation theorems. The all-I,B,k formula, unique double root and complete discriminant classification are independently reusable exact invariants, not an arbitrary enumerated range.

The dated certificate retains the supplied scientific assessment, sources and limitations.
