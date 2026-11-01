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

The exact rational checker compares the monic three-term recurrence with the coefficient representation for degrees zero through twenty and \(q\in\{1/2,2/3,3/4\}\), verifies the endpoint identity, and checks finite weight-product factorizations. Numerical calculations compare the scale \(N\max_x E_{q,N}(x)\) and the maximizing location with their derived limits for \(q\in\{0.2,0.5,0.8,0.9\}\) and \(N\in\{75,150,300\}\). All 198 specified assertions passed when `python CHECK.py` was executed in the delivered directory. The numerical optimization is an approximate bounded-window golden-section search and is not a proof of global optimality; the proof in RESULT.md is analytical.

All statements about derivatives and exponentially small errors use fixed \(0<q<1\); the same argument does not claim estimates uniform as \(q\uparrow1\). No third-party review or independent validation has been carried out.
