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

# Finite checks and their logical limits

The self-contained script `verify.py` requires only Python 3 standard-library modules. It was executed as `python verify.py`; the captured output is in `verify_output.txt`.

The program computes each vertex update directly from the sign of the current difference across each edge; this is independent of the algebraic residue-class calculation. For each \(1\le r\le5\), center value zero and every leaf gap in \([-r-2,r+2]\), it checks whether the direct fixed/two-step return agrees with the claimed gap-based classification, totaling 789,355 configurations. Translation invariance in the center explains why using center zero is sufficient for these local comparisons, but finite gap bounds do not prove all-size correctness.

It then enumerates all \(r^r\) canonical gap tuples for each \(1\le r\le7\) and checks the modular count formula across 35 residue classes. Finally, it enumerates positive-gap tuples and independently computes a polynomial convolution times a geometric-series sum across 340 nonnegative graph-size/total pairs for \(1\le r\le6\). All checks passed, ending with `STAR_DIFFUSION_CENSUS_VERIFIED`.

The infinite all-integer and all-star statements are justified by the written potential, sign-reversal argument, quotient-ring identity, and canonical nonnegative phase proof, not by finite enumeration. There has been no independent external audit or validation.
