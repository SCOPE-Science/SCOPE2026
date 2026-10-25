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

# Computational and analytical verification

Run `python check_switching_gates.py` with standard Python 3 (no third-party packages). The actual packaged program was executed successfully and printed: `PASS: 160 checks; two independently assembled Markov generators agree exactly.` It independently builds two continuous-time Markov-chain generators from first principles, performs absorbing hitting-time solves using exact fractions, compares them to the closed Fourier expression, and tests derivative sign boundaries and scaling. The algebraic Fourier proof in `RESULT.md` establishes the result for every positive integer \(k\); the finite tests alone do not certify an infinite theorem. The originality comparison is literature-bounded; independent scientific audit has not been performed.
