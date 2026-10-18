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

# Reproducibility

Run `python verify.py` with standard Python 3. The program enumerates each image assignment for the \(m\) one-letter generators from every element of \(A_m\), for \(m=1,2,3,4\). Because every interval is a product of its consecutive one-letter generators, these assignments include every homomorphism candidate. The program separately checks all pairs for preservation of both operations and tests idempotence by direct composition, not by using the closed-form classification. It compares the idempotent maps to the explicitly constructed deletion maps and compares their rank counts to the independent run-length recurrence. The complete counts of endomorphisms are \(2,12,148,3320\); idempotent counts are \(2,4,8,16\). The \(m=4\) nonzero-image-rank polynomial is \(1+4z+3z^2+3z^3+2z^4+2z^6+z^{10}\).

The computations exhaust only the four listed finite cases. Correctness for arbitrary \(m\) is furnished by the mathematical proof, and no independent audit has taken place.
