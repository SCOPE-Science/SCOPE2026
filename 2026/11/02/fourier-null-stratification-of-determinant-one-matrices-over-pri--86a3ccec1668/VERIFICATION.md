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
Run `python3 check.py` using the Python 3 standard library. The checker tests the primitive \(p^2\)-th root-of-unity zero criterion using integer counts, and directly enumerates \(\operatorname{SL}_2(\mathbb Z/p^2\mathbb Z)\). Exact exhaustive validation is over all \(9^4=6561\) frequencies at \(p=3\); an additional reproducible 400-frequency sample is checked at \(p=5\). The proof in RESULT.md independently covers every odd prime, including infinitely many primes beyond the verified examples. These tests do not establish source originality or independent mathematical certification.
