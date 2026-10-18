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

# Reproduction and limits

The mathematical statement is proved in `RESULT.md`. The following code independently tests key finite consequences; it is not an all-dimensions proof or a substitute for reviewing the adapted-basis transitivity argument.

Run from the directory containing all files:

```bash
python3 check_flag_refinement.py
python3 check_flag_orbits.py
```

`check_flag_refinement.py` enumerates row-reduced-echelon subspaces over \(\mathbb F_2\) and \(\mathbb F_3\), enumerates compatible nested flags, performs directed strict-containment colour refinement, and compares round-two cells with intersection-vector cells. It also asserts that the two specified two-dimensional subspaces of \(\mathbb F_2^4\) collide at round one and split at round two.

`check_flag_orbits.py` independently constructs all binary subspaces by repeated linear spans, enumerates all invertible binary matrices in dimensions two, three, and four, filters matrices fixing the given flag, and checks exact group orbits, Gaussian cell sizes, and round-two refinement partitions. The dimension-four group has \(20{,}160\) matrices; the one-marked-two-plane stabilizer has \(576\).

`checks_output.txt` records the observed standard runs and additional selected higher-dimensional cases. Standard refinement tests cover \(q=2\), \(n=2,3,4\), and \(q=3\), \(n=2,3\), over multiple flags. Additional selected tests cover \(q=3,n=4\) and \(q=2,n=5\), but not every flag. The group-orbit tests are exhaustive only for the listed binary flags.

The general field-size and ambient-dimension result follows from the proof's dimension-counting and adapted-basis lemmas. The software does not prove uniqueness among other posets, nor exhaust the scientific literature. External independent audit is not performed.
