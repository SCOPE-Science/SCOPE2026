---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Direct substitution of the fifth-root cosine values on the tenth-order grid yields contributions at indices 0–5 of −26, 0, 11+3√5, 0, 7−5√5, 0; reflection gives exactly 1−2/√5. For F(w)=|w|³ the derivative of the Hessian is the sum of four terms of norm at most 3 in unit directions, yielding the stated weak third-derivative bound; the Hessian extends Lipschitz through zero. The chain rule gives 3684 for each polynomial's cubed modulus, hence Fourier coefficient bound 7368/|k|³ for the difference. Absolute convergence and root-grid orthogonality give |Δ_N−I|<18420/N³. Independently certified all 124 required orders and the order-1000 proxy using Machin intervals, a degree-24 rational cosine polynomial and exact lower/upper endpoint propagation through integer square roots. The smallest resulting lower bound among 5–129 excluding ten was 648213509486681/6000000000000000 at N=6. The proxy exceeded 11554/100000, giving a bound 11769045563/109850000000 > 107/1000 for every N≥130. Both ranges therefore strictly exceed Δ_10. Replay: python3 /workspace/branches/reproduce_majorant.py, with outputs in /workspace/branches/majorant_reproduction.txt. The theorem concerns cubed norms of one fixed pair on complete uniform grids only.

## originality

PASS

The reversal, an order-independent positive bound, and order ten as candidate were already published in the exact same finite-grid setting. The supported distinct result is the sharp all-order value and its unique attainment, not the sign or the candidate. The predecessor's stated lower endpoint at order ten and weaker bound for L≥200 do not establish either the algebraic equality or a global sharp minimum. Inspectable continuous-circle results likewise do not give finite-grid extremality.

## value

PASS

The uniform margin is a quantitative stability threshold for the classical signed trinomial tested over all cyclic orders where reversal occurs. The result replaces a much smaller safe bound with the largest admissible one and identifies its sole bottleneck order; neither is interchangeable with observing positivity or a likely minimum on a finite grid.

The dated certificate retains the supplied scientific assessment, sources and limitations.
