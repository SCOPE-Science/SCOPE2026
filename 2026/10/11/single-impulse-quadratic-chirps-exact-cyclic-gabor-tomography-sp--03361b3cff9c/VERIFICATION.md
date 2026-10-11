---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
The proof is algebraic and applies to all integers \(N\ge3\), all integer chirp parameters and all positive real defect amplitudes. The finite checker directly evaluates both definitions of every ambiguity entry for orders \(3\) through \(28\), checks the rank-zero count, smallest positive and largest entry modulus, and checks strict optimality away from \(t=\sqrt N\) over a finite parameter grid. Its tests are corroboration, not exhaustive validation across infinite parameter sets.

An independent matrix assembly and numerical singular-value decomposition for cyclic orders \(3\) through \(8\) agreed with the full predicted singular-value multisets. The Weyl-basis orthogonality in the proof gives the exact general identity, independent of floating-point calculations. The arithmetic count uses only congruences and Euler's totient function; the optimizer uses the exact inequality \(N/t+t\ge2\sqrt N\).

Boundary checks: cyclic order \(N=3\) is included; even orders begin at \(N=4\). The even-order kernel is a linear-lifting obstruction only. No independent mathematical audit or certification has been performed.
