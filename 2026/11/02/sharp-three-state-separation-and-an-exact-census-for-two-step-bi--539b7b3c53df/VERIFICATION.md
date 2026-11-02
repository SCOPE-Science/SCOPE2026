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

Run `python3 verify.py` in a directory containing `verify.py` and `certificate.tsv`. The script requires only the standard Python library and checks all 62 certificate rows, consisting of 31 reachable states for each alternating two-symbol prefix. It reconstructs both three-state maps, the pair-state evolution, the regular-language phase recognizer and every outgoing transition, then checks the comparison Boolean against the language phase. This exhaustively proves the finite commutation lemma for arbitrary-length suffixes. It does not rely on previously produced output.

As an independent diagnostic, it enumerates all 16 complete two-state binary transition tables, all words of lengths three through fourteen, and four explicit three-state machines, checking the analytic two-state criterion and exact count formula. A total of 32,724 unequal rotation pairs were tested. The output in `verification_output.txt` is a record of a successful actual replay, not a substitute for the finite-closure proof.

The theorem concerns arbitrary finite input length but only a binary alphabet and a two-position cyclic shift. Related publication priority has not been independently certified; no external audit has been performed.
