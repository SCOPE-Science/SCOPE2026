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

# Verification of the affine class-group theorem

The exact finite checker `verify_wu_local_groups.py` was run on the files in this package, using Python 3 and SymPy. It independently enumerates all distinct vertices of each box-slice coordinate facet by assigning \(n-1\) boundary coordinates, verifies that the resulting rays are primitive, forms the integer ray matrix in an integral trace-zero basis, and computes its Smith normal form. It compares the result to the closed \((r,D)\) formulas in the theorem, including the degenerate endpoint's missing facet.

Observed run:

`VERIFY_OK checked_parameter_triples=105 n_range=2..6 Liu_Zhu_specialization=matched`

A separate hand-check of the general proof verifies: (i) the vertex configurations exhaust all vertices; (ii) pairwise differences generate exactly \(D\) times the root lattice, not merely a finite-index subgroup; (iii) the primitive reference vector makes the determinantal divisors of the presentation matrix equal to \(D^{j-1}\); (iv) the toric class-group exact sequence supplies free rank \(r-n\). These steps prove the assertion for all permissible dimensions and coprime parameters; the bounded tests alone would not suffice.

The proof does not compute singular local rings at non-fixed points, global class groups, or a full singular-locus stratification. Original Wu full-text access remained unavailable, which affects historical priority assessment, not the stated self-contained lattice computation. No external or independent audit is reported.
