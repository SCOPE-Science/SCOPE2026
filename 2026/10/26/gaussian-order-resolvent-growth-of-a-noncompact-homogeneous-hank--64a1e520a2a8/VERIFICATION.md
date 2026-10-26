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
The proof uses a normalized unitary Mellin transform, Euler's beta integral, Gamma reflection and recurrence, strict convexity of the hyperbolic cosine, and a disjoint-support localization of the Neumann resolvent series. The localization is decisive for a phase-uniform lower bound: independent testing of a power alone would not rule out cancellation in the resolvent series.

The finite Python checks use only the standard library; they reproduce weighted-translation product maxima, numerical reflection-constant checks through a separate finite integral if available, and the quadratic saddle-point coefficient. Finite tests do not establish the infinite-dimensional limit. The operator-norm proof and the comparison with the available literature are self-contained in RESULT.md, subject to the acknowledged publication-priority risk.
