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

# Reproducing the finite-field incidence census

Use Python 3 (standard library only). From the directory containing the companion program run:

```
python3 verify_lines.py
```

The program checks all five-coordinate cube classes modulo coordinate scalings, common scalar and permutation, establishing seven projective coefficient orbits. It enumerates each of the \(140050\) two-dimensional subspaces of \(\mathbf F_7^5\) using unique echelon representatives, checks vanishing of the restricted binary cubic's four coefficients, and counts the eight projective points on each accepted line. Independently it enumerates all \(2801\) projective rational points, computes the two mixed cubic polar expressions for every distinct pair of points on the threefold, and divides each point's eligible partner count by seven. The resulting point-wise line incidences agree exactly with the echelon method for each of the seven forms, not just in aggregate.

The program asserts the complete seven-row incidence table, total line counts, two incidence double-counting identities, and then prints `PASS`. The code was executed successfully on the actual included program. No floating-point operations, randomization, external data files, or network access are required.

These checks establish a finite exhaustive result only. This verification does not constitute a formal proof assistant certificate, an independent scientific audit, or a claim concerning arbitrary cubics over the field.
