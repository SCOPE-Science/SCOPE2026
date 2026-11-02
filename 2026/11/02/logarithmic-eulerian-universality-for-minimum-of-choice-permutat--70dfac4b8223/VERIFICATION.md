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

# Verification and scope

Execute `python3 checker.py` with Python 3 and no third-party packages. The standalone checker is an independent exact-rational finite experiment using full permutation enumeration and explicit weights from sequential choice. The actual execution returned `PASS` and counted 24,443 checks, including direct weighted enumeration of all permutations of sizes \(2\) through \(7\) for choice parameters \(1\) through \(4\), comparison with independently computed moment formulas, and one-step checks for sizes \(2\) through \(34\) and choice parameters \(1\) through \(7\).

The unbounded parameter domain and asymptotic estimates are supported by the analytic rank representation, telescoping and power-sum proofs and the explicit continuous coupling in `RESULT.md`, not by finite enumeration. The coupling uses \(k\) independent draws **with replacement** per stage. The proof establishes only fixed-\(k\) asymptotics; no uniform growing-\(k\) statement or historical-priority certification is provided.
