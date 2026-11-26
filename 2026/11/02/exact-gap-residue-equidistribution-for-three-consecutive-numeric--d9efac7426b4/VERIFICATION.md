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

For each nonzero residue r modulo n, the increments from n+1 and n+2 must sum to at least r, so at least ceil(r/2) such generators are needed; that many attain the increment r. The resulting genus is h^2 for n=2h and h(h+1) for n=2h+1. In the even case, for any prime p dividing an admissible modulus, p divides h, and the gap polynomial at a primitive p-th root is nonzero (including p=2). In the odd case I checked the finite geometric sums, their factorization under genus divisibility, and the unit-circle nonvanishing of the remaining quadratic. The separately grouped sum at order three is nonzero when 3 divides h. Testing all nonidentity roots, rather than only a primitive root, gives exactly the claimed exclusion when m divides h and 3 divides m. The n=3 endpoint is included. An independent direct-membership dynamic program agreed for 2,242 pairs, 3 <= n <= 40 and 2 <= m <= 60; this is corroboration, not the proof. The supplied verifier was inspected but not run.

## originality

PASS

The all-moduli classification beyond the known parity slice and n=3 survives the inspected comparisons. Neither the Apéry calculation nor the roots-of-unity criterion is new. The strongest distinct indexed match directly covers m=2, not the full theorem; the same record date does not establish ordering.

## value

PASS

A natural family of width-two semigroups has a complete modular gap classification beyond parity. It tells a reader exactly which divisors of the genus give equality, including the nontrivial obstruction at order three and the failure of mixed factors from consecutive h and h+1. These are useful distinctions not read off from the genus or the generator parity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
