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

The proof establishes the exact component decomposition of each finite compression, a convergent component-count formula, an independent matching recursion for the kernel, and the closed second-moment identity. To reproduce the finite tests, index basis words of length at most \(N\) in lexicographic order and place a unit entry between each word \(w\) and \(1w\), or \(22w\), when both lengths are at most \(N\). Separately construct \(\mathcal T_h\) by the stated root recursion; compare the two spectra after applying the precise multiplicities in the proof. Direct comparisons covered \(d=2\), \(2\le N\le6\), and \(d=3\), \(2\le N\le4\), with error less than \(6\times10^{-15}\). No finite computation is presented as a proof for all \(N\). The infinite limit follows from the generating-function summability. Publication priority and independent audit are not certified.

The self-contained finite check is included as `check_finite_blocks.py`; it requires Python 3 and NumPy, uses no external datasets, and prints each tested spectral discrepancy.
