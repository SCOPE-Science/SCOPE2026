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

# Reproducible verification

The included source files are self-contained except for the explicitly optional SymPy algebraic-chart check. Compile the three C programs with a standard C11 compiler, generate the five projective-substitution matrices with the Python standard library, and execute them as described in `RESULT.md`.

The primary program exhausts exactly 2441406 scalar-normalized cubic equations and writes the 186000 maximizing coefficient indices to `maximizers.bin`. The flag-restriction program has an independently computed same-domain histogram. Their histograms agree in every cell. The orbit program consumes only that freshly generated maximizing set and the five independently regenerated substitution matrices, finds two disjoint 93000-element orbits and confirms that each generator maps every maximizing equation to another maximum. The group generation and order are explained in the proof.

The representative check verifies all three projective affine gradient charts in characteristic five via exact Gröbner bases, plus independent rational-point and tangent incidence counts for each representative. The two representatives have exactly 10 and 8 rational points, respectively, each covering 29 of the 31 ambient points. A symbolic derivative contradiction in the proof is independent of the Gröbner library.

The outputs to compare are in `EXPECTED_OUTPUT.txt`. These computations are finite and exhaustive within the stated cubic coefficient space. They do not prove an analogous theorem in other fields. The check is an internal reproducibility review, not independent external auditing.
