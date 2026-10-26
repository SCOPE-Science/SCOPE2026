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
# Reproducibility of the all-run-limit law

Run `python3 verify.py` with Python 3.10 or newer. No third-party dependencies are needed. The checker performs the following independent finite tasks: (i) greedy-arch versus defining all-subsequences tests on all binary words through length 10; (ii) direct word enumeration for each run ceiling from 1 through 8 and lengths 0 through 14; (iii) an arch-mask/zero-run DFA dynamic program and a separate coefficient recurrence derived from the rational identity for each run ceiling 1 through 8 and lengths 0 through 125; (iv) a separate ordinary run-limited word-count recurrence; and (v) unrestricted reductions when the forbidden run exceeds the word length.

Expected success line: `RUN_LIMIT_ARCH_LAW_PASS r=1..8 lengths=0..125 direct_lengths=0..14 arch_definition=0..10 histogram_compared=1008`.

These checks do **not** exhaust all run limits, lengths, or universality levels; the general proof is the finite-state formal-series derivation in RESULT.md. The asymptotic comparison is justified by the analytic dominant root and the exact signed derivative identity, not by numerical tests. No outside certification or independent audit is claimed.
