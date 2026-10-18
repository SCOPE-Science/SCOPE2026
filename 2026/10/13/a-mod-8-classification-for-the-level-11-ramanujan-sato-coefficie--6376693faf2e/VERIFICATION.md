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

The full statement is for n>=1 and exactly the c11(n) coefficients defined by Campbell’s published double-binomial formula, not another level-11 normalization. Split the summation into a=0 and a>0. In the a=0 slice the central binomial factors have exact valuation 3[s_2(b)+s_2(n-b)]-2s_2(n); Kummer/Lucas show its mod-8 contribution is 4 precisely for n a power of two. For a>0, the summand is divisible by 4: when the squared middle binomial is odd, its Lucas-disjoint supports force the bit nu_2(a) of the relevant w to vanish, and two carries give 4|C(2w,w-a); when even, its square already supplies 4. The exact involution b -> n-3a-b preserves the summand, so nonfixed terms cancel modulo 8. At a fixed point 2b=n-3a, direct bit parity reduces the unique possible nonzero class to a=2^k,b=0,n=3*2^k. Thus c11(n) mod 8 is 4 exactly at 2^k and 3*2^k, zero otherwise. Independently reconstructed Campbell’s sum and checked all n=1..37 and separate Kummer two-carry instances; finite examples corroborate the unrestricted digit proof.

## originality

PASS

Campbell 2026 gives the exact double sum and the known modular recurrence but not its uniform mod-eight index classification. OEIS A284756 lists recurrence, initial values and references without a dyadic-index theorem. Caruso–Fürnsinn–Vargas-Montoya–Zudilin 2025 has the same sequence in the level-11 row of its Apéry-like mod-prime Galois table, but the reported mod-prime reductions do not furnish mod 8 or the exact two exceptional binary rays. Published mathematical record searches and targeted exact-congruence searches revealed no covering equivalent or stronger law. Novelty is only best-of-knowledge; same sequence and strongest nearby papers were examined rather than comparing titles.

## value

PASS

The minimum dyadic valuation of a fixed classical Ramanujan–Sato coefficient sequence is a natural uniform arithmetic invariant. The exact two-ray index classification explains a nontrivial 2-adic pattern for an infinite modular sequence using a reusable involution-and-carry mechanism. It is neither a recurrence restatement nor a finite tabulation and is motivated by Campbell’s newly established closed binomial formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
