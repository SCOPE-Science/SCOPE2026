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

PASS: Tame 4-point degree-seven Riemann–Hurwitz gives genus six; six deck-character holomorphic differentials omega_j=(x-lambda)^(j-1)dx/y^j exhaust the basis by local valuations. For s(j)=3j mod7, k(j)=(5s-j)/7, the characteristic-five coefficient selection in x^k(x-1)^k(x-lambda)^(6k+j-1) gives H=(q,1,2(lambda+2),2(lambda+2),1,q), q=lambda^2-lambda+1. Independent SymPy expansion recovered all six H scalars. Cartier maps around a 6-cycle; two zero arrows opposite at either exceptional factor give ranks 6,4,2,0 and a=2, p-rank0; otherwise bijective, p-rank6 a0. Distinct lambda3 and conjugate roots of q avoid 0,1; t identity (lambda+2)^2=4-t, q=1-t yields two labeled orbit types. Valid for all lambda in Fbar5, not inference from F5 samples.

## originality

PASS

PASS at best knowledge: Bouw and Elkin establish general p-rank/Cartier methods for cyclic covers and bounds, while Moonen studies special subvarieties from branch-varying covers. These foundations do not state the specific char5 septic (1,1,6,6) exceptional three-point polynomial, nilpotent string lengths or colored-moduli split in inspected results. A published special table or unpublished specialization of Bouw/Elkin coefficients could cover it.

## value

PASS

PASS: A natural genus-six cyclic degree-seven four-point Hurwitz family has a sharply classified ordinary-to-p-rank-zero transition, two Cartier nilpotence strings and distinct colored branch orbits; these exact invariants fill a motivated gap beyond generic p-rank bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
