---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Every automorphism of C_p⊕C_(p^b), b≥2, has unique constrained mixed-modulus matrix [[a,u],[p^(b-1)v,d]] with a, d mod p nonzero. Multiplication modulo p and p^b gives three necessary and sufficient commutation equations xu’=x’u, xv’=x’v and vu’=v’u, x=a-d mod p. Cases x≠0, x=0 with (u,v)≠0, and x=u=v=0 give respectively centralizer sizes (p-1)²p^(b-1), (p-1)p^b and |G|=(p-1)²p^(b+1). Counting elements and dividing by class sizes yields exactly the table 1:(p-1)p^(b-1), p(p-1):(p²-1)p^(b-2), p²:(p-1)(p-2)p^(b-1). Then k=(p-1)(p²+1)p^(b-2) and cp=k/|G|=(p²+1)/(p³(p-1)), independent b. The last class type correctly vanishes for p=2. Independent exhaustive pair commutation tests on four small groups (p,b)=(2,2),(2,3),(3,2),(5,2) confirmed the element distributions; the all-parameter classification rests on the three equations.

## originality

PASS

Qualified best-of-knowledge finding after an actual Resultary query, targeted primary-literature comparison, and an implication-level review of the submitted theorem. Specific same-object access restrictions and broader historical-priority risks remain in source_inspections and residual_risks. No failed search alone is treated as proof of novelty.

## value

PASS

A complete conjugacy-class size and multiplicity distribution is a standard natural group invariant. The stable commuting probability across increasing cyclic exponents captures a non-obvious feature of an infinite automorphism-group family, beyond the already known group order and fixed-point enumerations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
