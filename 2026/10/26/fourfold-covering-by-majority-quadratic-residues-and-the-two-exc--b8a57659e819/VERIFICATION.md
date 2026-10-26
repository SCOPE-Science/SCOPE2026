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

The six-item scientific package contains a self-contained prime-field proof and the standalone Python script `verify_prime_majority.py`.

Run `python3 verify_prime_majority.py`. It exhaustively checks all qualifying strict-majority residue subsets for \(p\in\{7,11,13,17,19,23,29,31\}\); it also verifies the exceptional obstruction witnesses, both constant-character-sign triple counts for \(7\le p\le127\) with \(p\equiv3\pmod4\), and the absence of critical-length progressions in the nonzero squares for \(19\le p\le127\) with \(p\equiv3\pmod4\).

Observed output: `CERTIFICATE_OK exhaustive_majority_subsets=24275 character_sign_checks=30`.

The infinite proof separately derives the exact triple-sign count and applies Cauchy--Davenport and Vosper; finite tests cannot verify all primes. Independent scientific review is not performed.
