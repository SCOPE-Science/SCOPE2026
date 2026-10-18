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

The finite checks were run with Python 3 and use only standard-library modules. Place `affine_refinement_check.py` and `affine_generation_check.py` in the same directory and execute:

```sh
python affine_refinement_check.py
python affine_generation_check.py
```

The first program constructs explicit affine incidence graphs over polynomial-basis fields of orders \(2,3,4,5,7,8,9,16,25\), runs iterative neighbour-multiset colour refinement, and compares the *exact sets* of singleton point and line vertices with the rational subplane \(\mathbb F_p\). For all extension fields, it also checks that a fourth marked point whose coordinate generates the full field yields a discrete partition. Two additional markings within \(\mathbb F_{16}\) whose marked-coordinate subfield is \(\mathbb F_4\) are checked against the exact intermediate counts \(16\) and \(20\). Its recorded output is `affine_refinement_check_output.txt` and ends in `ALL_CASES_PASS`.

The second program independently closes the marked points under geometric joins, line intersections and parallels. It checks all nine cases and, for extension fields, the four-point generating set. Its recorded output is `affine_generation_check_output.txt` and ends in `GEOMETRY_CLOSURE_PASS`. This second implementation shares only finite-field arithmetic with the first program.

These checks do not exhaust all prime powers or all marking configurations. The infinite statement is justified by the displayed geometric reconstruction and relative Frobenius obstruction, each of which has a separate argument. The tests supply finite corroboration, not independent scientific audit or a priority certificate.
