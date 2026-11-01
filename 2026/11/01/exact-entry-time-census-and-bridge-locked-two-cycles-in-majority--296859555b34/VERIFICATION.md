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

The proof is algebraic/combinatorial and covers every integer clique size \(m\ge2\). The script `verify.py` independently simulates all \(349520\) binary states for \(2\le m\le9\), recording first periodic entry and orbit size. Its output is in `verification_output.txt`. It checks the exact finite histograms, cycle counts, absence of nonperiodic period-two basins and size-total identities. The integer count identities are also tested for \(2\le m<300\); those checks supplement but do not replace the proof.

Run with `python3 verify.py` from the containing directory; standard Python 3.8 or newer is sufficient. No external dependencies, downloads, or probabilistic tests are required. The script directly builds the graph's neighbor masks and does not invoke the analytical local-case recurrence.

Self-review of definitions, exceptional small cases, finite checks and written proof was performed. Independent audit: not yet performed.
