---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

In characteristic 5, f(x)=x^{2g+1}+x for g=3^r has squarefree derivative at roots because 5∤2g. The Cartier–Manin matrix from f²=x²+2x^(2g+2)+x^(4g+2) has at most one nonzero entry per row/column, following odd labels t=2i−1 under multiplication by 5 modulo 4g. Consequently stable p-rank equals number of full cycles confined to odd labels below 2g, not one-step matrix rank. For v_3(t)=k, the 5-action on units mod 3^(r−k) has full order 2·3^(r−k−1); if r−k≥2, each fixed-mod-4 orbit includes labels above the cutoff. For r−k=1 exactly two labels t=3^(r−1),5·3^(r−1) survive, and v_3(t)=r contributes t=3^r. Thus exactly three labels survive for all r≥1. Independent exact partial-permutation computations r=1..5 reproduced ranks 3 with the specified survivor sets; they corroborate rather than prove the all-r orbit calculation.

## originality

PASS

Pan introduces the underlying complex curve family; Nourozi computes a-numbers for related x^m+x models, which are not stable p-ranks. A specific complete multiply-by-5 orbit proof establishes constant rank three in all genera 3^r. Resultary same-object search did not find prior exact p-rank expression, but implicit general cyclic-cover coverage remains plausible.

## value

PASS

Geometric p-rank measures the étale p-torsion of Jacobians and is distinct from a-number. A natural exponent subfamily of known hyperelliptic curves has unbounded genus yet fixed positive p-rank three; this exact stable-Cartier classification is a motivated new arithmetic invariant, not a mere restatement of one-step Cartier ranks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
