---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For p>=5, f_p(pt)=p^2(-t+p^(p-2)t^p) has bijective inner map by Hensel. On each unit ball x=zeta+pt, the critical derivative vanishes and expansion yields (1-p)zeta+p^3 u_zeta t^2 U(t), with U(t) in 1+pZ_p[[t]]; t sqrt(U(t)) is a p-adic bijection, giving disjoint square cylinders. Counting p^m quadratic residues by valuations gives S_p(m) and image density. At p=3, explicit cubic t^2(t+/-1) on the two unit balls has two full residue-output classes each, yielding exactly 13 classes mod81 and all higher lifts. Independent direct value-set enumeration for 20 prime/exponent levels matches formulas and the ternary T list. C holds for all odd p by the analytic Hensel argument, not by finite enumeration.

## originality

PASS

The all-prime p-adic exact image and densities are not implied by finite-field value-set rank results or generic nonpermutation upper bounds. p=3 is the Dickson cubic X^3-3X, so Bremser–Gomez-Calderon 1991 Galois-ring source is the closest possible coverage; its abstract/metadata were inspected but full text inaccessible after OA/arXiv search and Oxford VPN disconnected. This is an explicit priority risk, not scientific failure or proof of noncoverage. For p>=5 the specified X^p-pX is not the standard Dickson polynomial.

## value

PASS

The polynomial x^p-px has systematic critical points; its p-adic value image is a natural arithmetic object. All-level exact image cardinals, exceptional cubic branch, and a uniform density across odd primes are not routine field-level counts and provide precise local data for arithmetic dynamics/value-set questions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
