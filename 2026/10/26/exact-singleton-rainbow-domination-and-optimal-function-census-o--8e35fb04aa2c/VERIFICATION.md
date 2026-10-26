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

The self-contained `verify.py` independently enumerates all assignments of zero or one named colour to each vertex for 29 small triples of parameters. Every zero vertex is checked using its literal graph-neighbourhood list, without invoking the mathematical proof. The exact minimum weight and number of minimum functions are compared with a separate implementation of the stated combinatorial sums.

Run: `python verify.py`. Recorded result: `VERIFY_OK cases=29 exhaustive_labelings=2921552`. In particular, the direct nine-vertex test at \(r=3,m=3,k=4\) yields weight \(5\) and \(648\) minimum functions. Four additional formula-only examples are reported in `verify_output.txt`.

This is not an exhaustive census of the infinite family. It provides finite corroboration and a reproducible check; the mathematical proof relies on the two-support lemma, the full-part lower bound, and equality-case analysis in `RESULT.md`. No independent mathematical audit has occurred.
