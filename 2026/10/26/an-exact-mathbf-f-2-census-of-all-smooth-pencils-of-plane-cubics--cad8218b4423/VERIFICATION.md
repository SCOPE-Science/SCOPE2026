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

# Reproducibility checks

All four files below are complete standalone source/output pairs. `verify_pencils.py` requires Python 3 and SymPy; its printed certificate enumerates the \(336\) smooth cubics, \(5544\) pencils, \(37\) projective orbits, \(4508\) reduced bases and \(1036\) nonreduced bases. It uses Groebner unit-ideal tests in all three affine charts so its geometric decisions do not depend on a finite extension cutoff. `verify_base_splitting.cpp` can be compiled with a standard C++17 compiler and independently enumerates projective base-support points over extensions through degree \(9\), recovering the Frobenius support partitions of all \(37\) orbit representatives.

The two recorded output files are from executing their corresponding packaged scripts, not extrapolations or externally supplied transcripts. A complete reproducibility check consists of running both as specified in `RESULT.md`, byte-comparing their stdout against their respective outputs, confirming there are exactly \(37\) representatives, and summing the orbit sizes and reducedness labels. The support-degree calculation is a cross-check of the geometric reducedness test, not an alternate method of proving full scheme multiplicities. Independent audit: not performed.
