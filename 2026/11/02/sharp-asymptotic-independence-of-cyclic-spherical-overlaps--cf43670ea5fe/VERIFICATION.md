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

Leaf integration gives the exact product law on each forest. With normalized sphere measure the kernel Q_l is the degree-l harmonic projector divided by its rank D_l, and cyclic contraction gives mixed moments zero unless all degrees agree, then D_l^(1-m). In the one-edge inner-product measure, the Q_l have squared norm 1/D_l, by the same projector norm identity. Thus the proposed summands have squared product-space norms D_l^(2-m), summable since (m-2)(d-2)>=2. Their L2 limit defines a finite signed measure matching the joint law on tensor polynomials, which are uniformly dense on the compact cube. Equality of measures also proves positivity; no pointwise convergence is needed. The test product of the edges has mean d^(1-m), not zero. Parseval yields the divergence; the tail starting at l=2 is at most D_2^(4-m) times the convergent sum of D_l^(-2) over l>=2. The reverse L1 triangle inequality and L2 bound give the TV error about the degree-one term (d/2)a_d^m. For both parities D_2 a_d^2>1: it is 5/4 and 16/pi^2 for d=3,4, and the ratio at d+2 versus d is d^2(d+4)/[(d-1)(d+1)(d+2)]>1. Hence the error is smaller order, for each fixed d. The bijective Bloch change of variables gives a_3=1/2 and exactly the indicated TV prefactor. The general-m moment comparison in Step 5 should cite Zhang Proposition 6.8, not Theorem 6.7 (the latter is for triples); this is a citation-locator error and the mathematical identity is independently proved. Frozen scripts and finite checks were inspected, not executed.

## originality

PASS

The forest and cyclic trace mechanisms are established prior techniques, and the cited qubit product moment is already known. Neither the scalar product or cumulant results nor the inspected kernel-cycle work provides the claimed sharp fixed-dimensional TV asymptotic for the full continuously valued edge vector, including its prefactor and smaller-order error. Credit is for that joint-law result, not for inventing harmonic trace identities or for global priority.

## value

PASS

The cycle is the first obstruction to exact forest independence. A vector-law error with a sharp coefficient quantifies that obstruction in a way that a single cycle moment or chi-square upper bound does not. The fixed-d TV rate a_d^m is strictly smaller than the scale d^(-m/2) from chi-square alone, since |Z| is nonconstant. The qubit result is a useful interpretation of the real theorem, not a separate source of novelty.

The dated certificate retains the supplied scientific assessment, sources and limitations.
