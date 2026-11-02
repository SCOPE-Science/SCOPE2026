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

# Verification of the negative-type threshold

The proof is in `RESULT.md`. The embedded Python file `gq_negative_type_check.py` uses the standard library only and was executed on the package copy with `python gq_negative_type_check.py`.

Observed output:

```text
GQ(2,2): 30 vertices, p-critical=0.345784723476, recurrence_checks=1800
GQ(3,3): 80 vertices, p-critical=0.137565128845, recurrence_checks=12800
GQ(5,5): 312 vertices, p-critical=0.032764105998, recurrence_checks=194688
CHECK_OK exact_graph_recurrence_entries=209288 scalar_orders=2..199
```

For the three explicit symplectic quadrangles, the script constructs projective points and isotropic lines over prime fields from a nondegenerate alternating bilinear form. It then performs all-pairs breadth-first searches, checks every layer count, and verifies \(AA_2=qA_1+A_3\) and \(AA_3=qA_2+(q+1)A_4\) for every ordered vertex pair. The recurrence assertions are exact integer comparisons. It also checks the bipartition witness against the entire powered distance matrix, computes approximate roots, and tests scalar sign inequalities for orders \(2\) through \(199\).

The universal spectral derivation, strict sign inequalities, uniqueness of the positive root, and the asymptotic expansion are proved symbolically in `RESULT.md`, not by the finite checks. Numerical root values are approximations, and the checker is not a symbolic or independent verification of every analytic lemma. The nonclassical cases are covered by the incidence-axiom proof, not by constructing those geometries.
