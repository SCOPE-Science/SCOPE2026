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

Run `python3 checker.py` using a standard Python 3 interpreter. No packages beyond its standard library are needed. The file `checker_output.txt` records the successful check; the final line is `CHECK_PASS 330 quartets, four affine orbits, eight exact quartic profiles and root-separation certificates`.

The checker constructs the genuine 11-dimensional harmonic isometries for both quintic-character classes and compares 242 gauged Gram blocks to the proposed expression using a floating-point tolerance of \(5\times10^{-14}\). This is an independent *diagnostic* of the input normalization, not an exact proof.

The decisive spectral computation is exact: every coefficient of every orbit representative's \(8\times8\) characteristic polynomial is obtained from integer cyclotomic arithmetic and Newton identities. All 330 quartets are partitioned into disjoint affine orbits by exhaustive enumeration; no assumptions about generic quartets are used. The root-separation stage works in \(\mathbb Q(\sqrt5)\) with rational sign comparisons, never floating-point approximations. A negative lower-end polynomial value and strict positivity of all upper-shift polynomial coefficients isolate the largest real root sufficiently to distinguish the unique extremal orbit for each class.

Limits: the exhaustive computation applies only to the finite 11-point field. The source-dependent Gauss-sum identity and the antiunitary spectral symmetry are proved in the accompanying mathematical text; numerical samples are not used to infer an infinite-family theorem. This is self-review, not independent audit.
