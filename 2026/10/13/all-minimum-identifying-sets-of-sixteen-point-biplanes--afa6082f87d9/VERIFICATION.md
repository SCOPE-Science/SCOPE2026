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

# Reproducible scientific checks

Execute `python verify.py` with Python 3 and no external dependencies. The checker builds the five-regular Clebsch graph on four-bit binary labels with XOR step set \(\{1,2,4,8,15\}\). It checks the symmetric design incidence conditions: \(16\) blocks of size \(6\), each pair of distinct blocks meeting in \(2\) points, each point in \(6\) blocks, and every two points in exactly \(2\) blocks. It generates all \(96\) distinct punctured blocks and verifies their signature patterns.

The checker then tests all \(2^{16}=65,536\) vertex subsets directly against the definition of an identifying code; the smallest feasible size is \(5\), its feasible sets exactly match the \(96\) punctured blocks, and they partition into \(16\) independent open neighborhoods and \(80\) induced four-leaf stars. As a strengthened finite consistency check, the program compares the full identifying-code size distribution with independently fixed exact counts.

This is a finite exhaustive confirmation of the **graph** specialization only. The statement for every symmetric \(2\!-(16,6,2)\) design follows from the universal point-pair incidence proof in `RESULT.md`; scanning one graph does not prove it. No independent mathematical audit has been performed.
