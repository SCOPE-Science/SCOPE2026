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
# Verification

The symbolic proof uses only the positive Ricker boundary recurrence and the transverse predator derivative. Summing \(\log(x_{j+1}/x_j)=r(1-x_j)\) over a full period proves the exact arithmetic-mean identity; multiplying the scalar transverse variational recurrence proves the exact Floquet multiplier.

The packaged `verify.py` checks the nontrivial period-two witness at \(r=2.2\) by bisection, verifies \(x_1+x_2=2\), recomputes the prey two-step derivative and predator transverse multiplier at \(R_0=1.1\), and confirms both lie strictly inside the unit disk while \(R_0>1\). The computation is illustrative; it is not used to certify the arbitrary-period theorem.

Limit: no claim is made about global basins or about nonperiodic/chaotic boundary invariant measures. The full body of the 2026 motivating article was not available in the accessible text view, so literature-overlap risk beyond the inspected abstract, captions, and references remains explicitly recorded.
