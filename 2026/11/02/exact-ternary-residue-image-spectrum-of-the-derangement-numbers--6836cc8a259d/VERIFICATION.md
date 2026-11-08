---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

The actual RESULT.md interpolates (-1)^n D_n by restricted integral F(x)=sum (-1)^j falling_factorial(x,j). Interleaving parity in each mod 3^a class makes derangement image F(Z3) union -F(Z3). Coefficientwise F(3t)=1+6t mod9 gives a contraction bijection onto 1+3Z3 and its sign supplies all units. For x=1+3t, F=9A(t); the exact mod9 expansion and A'(t) congruent 2t mod3 give a unique critical point and p-adic Morse coordinate with image A(Z3)=c+Sq, v3(c)=2, c/9=2 mod3. Partition unit square classes and divisible arguments gives I_m and 725/972. Critically checked the actual falling-factorial polynomial reductions and normal-form steps, not only finite period logs. Independently enumerated D_n mod 3^a for a<=8 and signed shifted-square images m<=7: all match. Infinite conclusion relies on the complete analytic normal form.

## originality

PASS

Known derangement p-adic interpolation, modular periodicity, and p-adic valuation/Hensel methods are prior mathematics (Miska, O'Desky–Richman, Barsky). Read O'Desky–Richman preprint in full: it gives p-adic interpolations and distribution/zeros but no formula for this all-a residue IMAGE cardinality; this distinction is stronger than merely a different index frequency. No equivalent Resultary finding returned for the query.

## value

PASS

Image density is a natural congruence invariant of the classical derangement sequence. The exact p-adic normal form and all-exponent image count solve a nontrivial distinction between periodicity/zero valuations and total residue occupancy, yielding an independent exact rational limiting density.

The dated certificate retains the supplied scientific assessment, sources and limitations.
