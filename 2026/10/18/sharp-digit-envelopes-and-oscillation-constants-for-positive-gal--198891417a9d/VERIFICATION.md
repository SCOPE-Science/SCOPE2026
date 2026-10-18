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

# Mathematical checks and limits
The accompanying `verify.py` runs with the Python standard library and requires no external data. Its checks are: (i) exact digit and reflected-digit values of the two explicitly constructed positive sequences for every \(2\le k\le17\) and \(1\le n\le2000\), including the dilation identity and pointwise order; (ii) integer-power coefficient inequalities at bases for which \(\log_2 k\) is integral; and (iii) exhaustive finite-horizon enumeration of all positive sibling splits for three small settings. The recorded execution printed `deterministic envelope tests: 32000`, `all-positive-split prefix tests: 54300`, and `verification: PASS`.

The infinite conclusions are justified by the proof in `RESULT.md`, not by any finite check. No formal prover or independent scientific audit was performed. Earlier foundational source texts may contain additional unstated relevant results and were not fully accessible.
