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

The standalone `checker.py` was executed from its package path using Python 3. It enumerates all \(131068\) binary words of lengths \(2\)–\(16\), identifies \(8798\) Lyndon words and verifies exact Witt–Möbius counts, correct initial maximal zero-run, and last-letter \(1\). It reports terminal tables for \(12\) lengths and samples \(15000\) uniformly random words at each of lengths \(128\), \(512\), and \(2048\) after canonical rotation. The observed four-letter suffix frequencies approach \(1/8\). These checks are finite; the convergence rate, switching lemma, logic locality reduction, and exact infinite spectrum follow from the proof in `RESULT.md`, not the experiment.

Reproduce with `python3 checker.py`. No external dependencies. The formal use of effective Hanf locality is a standard theorem stated with precise degree and language assumptions in the result. Independent external validation has not occurred.
