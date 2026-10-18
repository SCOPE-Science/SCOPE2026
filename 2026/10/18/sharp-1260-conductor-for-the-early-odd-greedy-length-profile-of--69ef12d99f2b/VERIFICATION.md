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

Run `python3 verify.py` using a standard Python 3 interpreter. The program uses only the standard library, constructs all primes from 5 through 100000 by a sieve, independently iterates the odd-greedy recurrence through seven steps with exact integers, and checks the classification on all 9590 such primes. It also enumerates all 288 invertible residue classes modulo 1260, reproduces counts 144, 36, 78, and 30, and checks explicit witnesses against each maximal proper divisor of 1260. Expected output: `VERIFY_OK primes=9590 unit_classes=288 counts={2: 144, 4: 36, 6: 78, 8: 30} minimal_divisor_period=1260`.

# Limits

The numerical checks do not establish infinitely many primes in classes, prove global periodicity of all stopping times, or resolve the last category. Those claims rely only on the exact symbolic proof and the cited classical Dirichlet and prime-number theorems. No independent audit has been performed.
