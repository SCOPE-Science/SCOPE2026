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

The standalone `checker.py` independently performs literal permutation enumeration for every \(1\le n\le8\) and computes the weighted-run formula from compositions and set partitions. All 36 exact count comparisons agree. Sixteen additional parity-scaled probability calculations for \(n\in\{12,20,30,50\}\) and \(d\in\{0,1,2,3\}\) passed, totaling 52 checks. Run `python3 checker.py` from this directory; it uses only the Python standard library.

Representative scaled values for \(n=50\), in order \(d=0,1,2,3\), are \(1.000000,2.085272,1.002264,5.317244\), compared with analytic limits \(1,2,1,4\). These finite checks do not establish asymptotic statements; their proof is the factorial bound and unique dominant-cycle analysis in `RESULT.md`. Independent audit has not been performed.
