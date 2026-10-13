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

# Reproducible checks
Run `python3 VERIFY.py` with `CERTIFICATE.tsv` in the same directory. The script checks the complete list of nineteen odd primes not exceeding \(71\), and all three essential truncations \(t=3,4,5\). It recomputes exact signed integer binomial sums, their prime-adic orders and normalized residues; independently checks each result by products of p-free factorial factors modulo \(p^4\); and validates the full table.

The infinite step uses the elementary exact identity \(j\binom{p^5h}{j}=p^5h\binom{p^5h-1}{j-1}\), followed by Vandermonde. It is not tested computationally for every truncation and is not asserted on the basis of numerical samples.

Unproved limits: nothing here classifies prime exceptions above \(71\), higher digit depth, or Gaussian q-polynomial valuations. No external or independent audit has been performed.
