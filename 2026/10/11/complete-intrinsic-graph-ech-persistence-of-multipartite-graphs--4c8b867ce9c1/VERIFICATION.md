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
# Reproducibility and verification

The standalone file `verify_cech_multipartite.py` contains an independently stated finite implementation of the graph Čech nerve. It constructs the scale-\(0\) vertex sets, scale-\(1\) edge sets, scale-\(2\) closed-neighborhood facets, and scale-\(3\) adjacent-pair closed-neighborhood unions, then enumerates **all** subsets of these generators. The program computes exact boundary ranks over \(\mathbb F_2\) by bitset Gaussian elimination, giving reduced Betti numbers in all dimensions. It also tests the full scale-two face criterion on **every** nonempty vertex subset for each of eight small input tuples.

Command: `python3 verify_cech_multipartite.py`. Observed successful termination: `VERIFY_OK`, with the eight parameter-by-parameter counts printed beforehand. No nonstandard dependencies, external datasets, network access or custom binaries are needed.

A separate unrestricted proof is supplied in `RESULT.md`: the Čech facet theorem gives the exact complex; the decomposition into two contractible subcomplexes at each induction stage yields a suspension of their intersection; iterated join identifies the sphere wedge and integral augmentation module; and endpoint complexes determine the barcode. Computational checks do not certify arbitrary parameters, integral torsion, or module structure; these come from the mathematical proof. The proof does not address automorphisms permuting equal-size parts or alternative metric/nerve conventions.
