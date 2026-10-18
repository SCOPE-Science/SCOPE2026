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

Run `python3 verify.py > reproduced.json` with Python 3.8 or later. The generated UTF-8 file should match the supplied `census.json` exactly (including final newline). The script depends only on the Python standard library.

The computation is exact: coefficients of \(\zeta_8\) are tested using \(c_j=c_{j+4}\), not numerical complex roots; all orthogonality and tiling tests reduce to bit masks. The script counts all \(65535\) nonempty subsets and every cardinality, checks the complete multiplicity distributions, enumerates all \(256\) affine maps, and provides \(43\) representative records. As a cross-check it enumerates proposed spectra directly for every actually spectral two-, four- and eight-point set, without using subset-zeta sums to count those bases.

The certificate is finite and exhaustive for \(\mathbb Z_8\times\mathbb Z_2\) only. No general claim for larger groups or independent audit is asserted.
