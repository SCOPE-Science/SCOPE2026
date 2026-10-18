---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

The exact resultant of T^3-2 against (u-v)^2-T^2 w(u+v)-2T w^2 is (u-v)^6-16w^3(u^3+v^3+w^3), independently verified over Z. Applying coordinate permutations and v->omega^j v produces nine distinct block sextics. The coefficient of u^5 v is -6 omega^j, so exactly three equations are rational; each rational sextic has three distinct smooth conjugate conic factors transitively permuted by the cubic Galois subgroup, hence irreducible over Q. The full splitting field Q(cuberoot2,omega) is S3 of degree6; explicitly enumerated its action on 27 labeled components giving orbit sizes 3,3,3,6,6,6 and block orbits 1,1,1,2,2,2. The existing geometric freeness claim is credited to the published original, not independently reproved.

## originality

PASS

Dimca–Ilardi–Malara–Pokora already construct the 27 hyperosculating conics, nine same-block triples and free degree-nine curves; those are explicitly prior. The independently reconstructed exact arithmetic sextic products, minimal coefficient fields, rational irreducibility and six-component Galois orbit census are not given as such in inspected geometric theorems. Moe–Toft has general conic formulas but no compared explicit full descent. The result is an arithmetic characterization of an existing finite natural configuration, not freeness novelty.

## value

PASS

Field of definition, arithmetic irreducibility and Galois orbit types are natural invariants of the complete distinguished 27-conic/9-block Fermat cubic configuration. The exact split into three Q-defined sextic products and six quadratic-field-defined products matters for rational plane geometry and arithmetic descent; computing the entire configuration is more than renaming the known freeness theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
