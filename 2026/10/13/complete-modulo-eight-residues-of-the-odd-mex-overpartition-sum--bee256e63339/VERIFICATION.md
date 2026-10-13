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

# Verification of modulo-eight odd-mex residues

Run `python3 verification/verify.py` using Python 3 standard library only. The verifier constructs the residues from the forced/unrestricted overpartition part factors for every odd minimal excludant with smallest possible size at most 400. Separately, it enumerates ordinary partitions of every index through 24, weighting each part-support set by the number of possible overlinings, and compares with the independently computed closed formula. It also confirms the exact positive-square zero locus and the exclusion of all but residues 0, 2, and 6 in the tested range. Actual recorded standard output is in `verification/check_output.txt`.

The proof is not based on numerical extrapolation. Its decisive infinite checks are: the terms indexed by \(j\ge2\) vanish modulo \(8\); the \(j=1\) term reduces to a rational series modulo \(8\); the inverse theta factor has precisely three terms modulo \(8\); every square coefficient cancels; and nonsquares are twice an odd number modulo \(8\). Direct enumeration and coefficient tests are finite consistency checks only.

Scope: coefficients for every positive integer, modulo eight. Higher-power divisibility, closed exact integer values, and external/independent review are not claimed.
