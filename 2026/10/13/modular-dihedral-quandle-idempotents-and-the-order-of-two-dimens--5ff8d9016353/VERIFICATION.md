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

# Reproducibility of algebraic and finite checks

The algebraic proof works with the ordinary associative algebra \(K[X]/(X^p-1)\) and the nonassociative quandle multiplication separately. A verifier with the standard Python library is included as `verify.py`. Run `python verify.py`.

The verifier exhaustively checked all \(3^3\) elements for quandle order \(3\) and all \(5^5\) elements for quandle order \(5\). It found exactly four and six idempotents respectively. It generated and directly multiplied further solutions for primes \(7,11,17,31\), using fixed random seeds, and checked additional random elements for the augmentation constraint. It printed `VERIFY_OK` on the packaged execution.

The general proof is analytic and finite-algebraic: nilpotence of the augmentation ideal excludes its nonzero idempotents, truncated exponential/logarithm identify the augmentation-one part with a linear eigenspace, and the multiplicative order of \(2\) determines the dimension. Random tests do not establish exhaustive classification at larger primes.

No independent audit or external verification has been performed.
