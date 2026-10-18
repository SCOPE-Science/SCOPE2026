---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Armijo on SPD quadratic is alpha q<=2(1-sigma), q=(g^TAg)/(||g||²). Define t=alpha q. Exact squared gradient factor 1-2t+K t², K=(||g||² g^TA²g)/(g^TAg)². Spectral scalar bound lambda²<=(mu+L)lambda-mu L and optimizing over q yields sharp Kmax=(kappa+1)²/(4kappa), with endpoint eigenmode weights. Convexity in t makes supremum maximum of 1 (t to0) and 1-4(1-sigma)+4(1-sigma)² Kmax. Solving endpoint<=1 yields sigma>=((kappa-1)/(kappa+1))². Scaling diag(1,kappa) realizes Armijo equality on any first trial s0; exact Fraction witness sigma=1/4,kappa=4 has g=(2,1), new g=(1/8,-11/4), norm squared ratio 97/64>1 and f decreases 34/15 to61/60. Endpoint attained on unsafe branch; value 1 only supremum at alpha downarrow0 in safe branch.

## originality

PASS

Nocedal-Sartenaer-Zhu 2002 primary full 31-page text was accessed via lawful institutional publisher service and Section 4 Theorem 4.1 explicitly concerns exact-line-search steepest descent with classical threshold 3+2sqrt2; equation and theorem pages 12-14 inspected. It does not impose Armijo-only admissibility, sigma-dependent endpoint, or arbitrary first-trial scaling witness. Classical Kantorovich spectral bound supplies an ingredient but alone does not state the sharp accepted-step frontier. Armijo 2014 work gives sufficient objective decrease, not this independent gradient-norm diagnostic. Related Resultary steepest-descent records compare exact line search and other objectives, no stronger implication located.

## value

PASS

Practical monotone Armijo line searches guarantee objective descent yet may accept gradient-norm-amplifying first trials. The sharp condition-number/Armijo parameter phase frontier makes this distinction quantitative, in all dimensions, and the explicit first-trial counterexample rules out interpreting the failure as an implausible abstract stepsize. A motivated optimization stability boundary, not merely a demonstration that gradients oscillate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
