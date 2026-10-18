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

For M=2^e, e>=2, pairing i and M-i gives P_e(A)=G(M^2 A(A+1)), with m=2^(e-2) odd pair-constants c_r=i_r(M-i_r). A dyadic congruence f(r+2^k)=f(r) mod 2^(k+2) for f=c_r^(-1) yields v2(sum_r 1/c_r)=e-2. Consequently v2(G' (0))=e-2 and the divided-difference quotient at T_A,T_B in 2^(2e+1)Z has that exact valuation. Factoring T_A-T_B proves v2(P_e(A)-P_e(B))=3e-2+v2((A-B)(A+B+1)); the zero factors are actual equalities. The two factors have odd sum, so modulo 2^s they give exactly distinct reflected two-point fibers; odd products congruent modulo 4 give exactly +j valuation on 2^j powers. Independently computed 384 nontrivial exact pairs at e=2..7 and shifts -4..4; finite checks do not prove the universal law.

## originality

PASS

Davis 2026 Theorem 3.1 and Corollary 3.2 cover a universal lower-bound congruence but not the exact pair-dependent valuation or two-element fiber theorem. The new result is a natural sharp strengthening despite relying on closely related earlier reciprocal/coefficient lemmas. Actual Resultary semantic and published-literature comparisons found no stated stronger same-block identity. The proximity of Davis Lemma 3.3 means derivability by adaptation remains a priority risk, not a claim of independent discovery.

## value

PASS

A complete ultrametric distance and exact all-precision quotient/fiber classification for a standard full odd-factorial block directly answers how much information any shifted product comparison retains. These uniform all-shift congruence budgets and sharp powered lifts add useful structure beyond a one-instance numerical modulus; they are motivated by Davis's factorial-unit stabilization problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
