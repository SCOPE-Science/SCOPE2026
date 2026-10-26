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
# Reproducibility and limitations

Run `python3 verify.py` in a directory containing the accompanying script. The script uses only Python's standard library. It constructs exact finite fields as polynomial quotients, enumerates all distinct projective quadruples, tests each four-by-four rank, and compares dependence to the affine-subline criterion after a projective change of coordinates. It also checks the number of minimum-size repair sets through each coordinate. The script's recorded output is stored in `verification_output.txt`.

The verified parameter triples are \((p,m,s)=(3,2,1),(5,2,1),(3,3,1),(3,3,2)\), with \(210\), \(14{,}950\), \(20{,}475\) and \(20{,}475\) tested quadruples respectively. Every check matched, and the final output was `SUBLINE_REPAIR_CENSUS_OK`. In characteristic three, its affine-line partitions give \(q/3\) disjoint recovery triples in the tested fields. For nonternary fields no optimum disjoint-availability claim is made.

The all-parameter theorem rests on the projective evaluation equivalence, fixed-field Frobenius criterion, three-column independence, trace-span comparison and affine parallelism argument in `RESULT.md`, not the finite census. The independent mathematical audit remains unperformed.
