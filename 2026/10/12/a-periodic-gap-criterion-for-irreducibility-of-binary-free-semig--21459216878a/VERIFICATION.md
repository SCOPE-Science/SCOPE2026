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

# Computational and mathematical verification

The mathematical proof is an explicit normalization and two-way construction of free-semigroup factorisations; no finite computation is used to infer the infinite theorem. The normalization handles the intermediate-letter swap when a factor sends \(b\) to \(a\), so an enumeration restricted to normalized factors is complete for the finite tests.

Run `python3 verify.py` in a directory containing that standalone file. It enumerates all normalized non-automorphism pairs \((u,v)\) that can produce an output word of length at most nine; it does not use the divisor condition to generate witnesses. For every tested word containing \(a\), existence of such a pair agrees with the criterion. The tests cover 1,013 words over lengths 1–9; the per-length reducible counts are respectively 0, 0, 5, 12, 24, 50, 100, 201, and 398. It also checks the \(m=4\) count for \(0\leq\beta\leq9\), prime-\(m\) counting for \(m=2,3,5,7\) and \(0\leq\beta\leq6\), and irreducibility of \(aba^{m-1}\) for \(2\leq m\leq20\). The final line is `VERIFY_OK`.

Limits: the finite tests are exhaustive only for the stated word-length bound and tested families, not for all words. The proof establishes the general claim. A separate, independent audit has not been performed.
