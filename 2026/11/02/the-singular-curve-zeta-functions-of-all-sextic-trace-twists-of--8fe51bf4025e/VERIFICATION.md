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

Over Fq char p>=7 sextic etale E, over algebraic closure the trace-zero quartic gradient condition yields all six coordinates satisfy t^3-(s2/4)t+c=0. Distinct roots force multiplicity two each by Vandermonde, giving 15 pairing (syntheme) projective lines, and repeated roots yield precisely the 15 duad triple points. Line–point incidence has 45 branches/flags. Frobenius on six factors acts with cycle type lambda partition of 6. For each of 720 S6 permutations the cycle spectra ell_d on 15 lines, p_d on 15 duads, b_d on 45 flags yield exact normalization zeta Z= product_d (1-T^d)^(b_d-ell_d-p_d)*(1-q^d*T^d)^(-ell_d). Independently enumerated all 11 cycle types and orbit spectra, verified split Fq-point result 15q-15, type (3,1,1,1) 3 rational points, (5,1) zero, and (6) q+1. Algebraic-geometric proof plus exact finite S6 group exhaustion establishes all q and all 11 etale types; finite q sample is only corroboration.

## originality

PASS

Geometry of Igusa quartic, Cremona–Richmond 15 lines, S6 representation, and twisting are classical. Bruin–Kulkarni 2025 §2.5 explicitly covers this equation, synthemes, and arbitrary twists, but in inspected treatment does not provide the reduced singular curve normalization/branch correction and complete 11-case Frobenius-zeta table. Best-of-knowledge new complete arithmetic classification.

## value

PASS

An exact complete eleven-case zeta classification of a natural reducible singular curve under sextic trace twists, with nonobvious rational-point pathologies (e.g. 3 points but no rational component, 0 points), is a motivated arithmetic invariant, not a new claim about known fifteen-line geometry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
