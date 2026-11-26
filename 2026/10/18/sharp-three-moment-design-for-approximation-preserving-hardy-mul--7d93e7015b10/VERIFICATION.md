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

In the moment matrix, the index groups {0,1,2} and {n+1,n+2,n+3} give identity diagonal blocks and the stated triangular cross-block; any indices from 3 to n have only zero cross-moments. Schur complement and the truncated trigonometric moment theorem prove both directions. In the Herglotz Cayley transform the first correction beyond its linear term is of order 2(n+1)>n+3, so the shifted Schur function has coefficients a,b,c. Set r=|a| and s=|b|. Schwarz–Pick on the next Schur parameter gives the envelope 1+r−r²+s−s²/(1+r) with 0≤s≤1−r². Its unconstrained vertex gives at most 13/8 up through r=1/2; thereafter the endpoint gives 1+2r−r²−r³, uniquely optimized at (√7−1)/3. Saturation forces the next parameter to be a unimodular constant, uniquely prescribing the Schur function. The degree-n+2 Blaschke product has strictly positive boundary angular derivative, so its level-one roots are distinct and the Herglotz masses are precisely the reciprocal angular derivatives. Subtracting the corresponding point kernels cancels all poles and leaves zero real part on the circle, excluding another measure component; Herglotz uniqueness and the two moment phases give the full equality family. The Hardy transfer matches Theorem 2.1 of arXiv:2206.11841v1.

## originality

PASS

Credit the sharp aggregate coefficient-modulus optimization with complete equality and its all-degree optimal moment measures, not the classical feasibility criteria or the existing Hardy kernel characterization. The strongest inspected coefficient paper explicitly separates segment supremum norm from the modulus sum and gives 13/8 only as an example for the latter; it neither proves the global upper bound nor classifies its equality. The closest inspected catalogue result likewise solves the section-norm problem instead. No covering claim was established in the inspected sources; historical priority is not certified.

## value

PASS

The joint objective answers how large the first three deviations from uniform moments can be in aggregate while preserving exact cancellation at all preceding orders. Beyond the sharp number, the phase classification gives every optimal positive quadrature explicitly and proves the exact minimum node count for optimality. Separate one-coefficient bounds or a nonsharp example cannot supply that design information.

The dated certificate retains the supplied scientific assessment, sources and limitations.
