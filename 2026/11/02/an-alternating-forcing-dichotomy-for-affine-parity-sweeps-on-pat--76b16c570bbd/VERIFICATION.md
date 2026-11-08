---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

The linear map x↦Σ_i x_i(e_{i-1}+e_i) identifies F_q^n with the zero-sum hyperplane in F_q^{n+1}; each local update conjugates to adjacent swap plus b_i root translation. Any order of the n edge-transpositions along the path is one (n+1)-cycle. A global translation puts the affine map on constant-sum hyperplane H_c, whose c=0 is equivalent to solvability of A(P_n)x=b; the odd-n kernel is the alternating vector. P^t fixes gcd(t,n+1) cycles and one affine sum constraint yields the displayed counts; primitive period witnesses and Möbius inversion establish support and exact order. Independent exhaustive GF2/GF4 checks covered 4696 offset/order instances, not the all-n proof.

## originality

PASS

Coxeter elements of type A and general sequential linear-system matrices are classical. The finite-field affine constant-sum representation plus arbitrary-schedule path-specific offset obstruction and complete orbit census are the surviving contributions. Defant’s closely related affine rule 150/105 work studies cycles with more restricted update settings rather than the exact asserted path theorem.

## value

PASS

An all-schedule complete periodic-orbit classification for a natural reversible affine local-update system is a structural theorem, including a sharp forcing dichotomy and exact primitive period support beyond elementary matrix invertibility.

The dated certificate retains the supplied scientific assessment, sources and limitations.
