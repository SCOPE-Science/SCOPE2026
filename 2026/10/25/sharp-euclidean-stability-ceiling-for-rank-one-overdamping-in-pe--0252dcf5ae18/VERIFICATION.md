---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For real finite-dimensional SPD A and B, C=I+hB/2 and T=I-h A C^-1, direct noncommutative expansion gives C(I-T^T T)C=h(2A+hK), K=(A(B-A)+(B-A)A)/2. Thus Euclidean nonexpansivity is equivalent to 2A+hK positive semidefinite; no commutativity is presumed. When B=A+vv^T, S=A^-1/2 K A^-1/2=(ab^T+ba^T)/2 with a=A^1/2 v,b=A^-1/2 v has nonzero eigenvalues (s ± sqrt(alpha beta))/2. Strict Cauchy-Schwarz gives delta=sqrt(alpha beta)-s>0 iff Av is not parallel to v, so h*=4/delta is the inclusive sharp one-step norm boundary. Alignment gives positive definite 2A+hK for all h>0. A second exact congruence C(A^-1-T^T A^-1 T)C=h(2I+h vv^T) is positive definite, and h C^-1/2 A C^-1/2 has eigenvalues in (0,2) because B>=A>0, establishing weighted strict contraction and spectrum in (-1,1) even for h>h*. Exact rational witness A=diag(1,4), v=(1,1) has h*=8 and h=16 ratio 1557/1301; independent exact congruences checked 12 matrix cases.

## originality

PASS

Qualified PASS only for the sharp rank-one Loewner-larger stage-generator Euclidean one-step ceiling with simultaneous weighted/spectral stability. Original perturbed midpoint scheme and mixed-precision perturbation bounds, elementary Jordan-product eigenvalues, and ordinary B-stability were already established; their implications do not give this necessary-and-sufficient rank-one threshold. Older matrix norm contractivity results may formulate the same criterion.

## value

PASS

The exact permissible timestep under a common stage-surrogate error model is a concrete numerical design question: a more strongly damped SPD stage can exhibit Euclidean transient amplification. Separating all-step weighted stability from Euclidean norm loss and identifying the eigenvector exception supplies a useful sharp mechanism rather than a routine consistency estimate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
