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

# Reproducibility and scientific limits

Run `python3 verify.py` with Python 3 and the standard library. The program constructs all weight-four reduced Świątkowski basis states for \(K_{5,5}\), exhaustively builds and reduces each boundary, and asserts both the boundary ranks and the Betti vector. It repeats the calculation under two independently chosen local reference-edge conventions. The expected terminal marker is `VERIFY_OK`.

The chain dimensions are \((20475,117000,234000,192000,53760)\); the four differential ranks are \((20474,96509,136963,53759)\). The program independently verifies the Euler-characteristic identity \([t^4](1-4t)^{10}/(1-t)^{25}=-765\) and tests sampled compositions of successive differentials. The full differential-square identity follows algebraically from the reduced local differential and the characteristic-two cancellations, not from those samples.

The computation proves dimensions over \(\mathbb F_2\) for exactly four unordered particles on \(K_{5,5}\). It does not determine integral torsion factors, integral free ranks, or the homology for larger families. External independent audit has not been performed.
