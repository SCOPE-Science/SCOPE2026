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

Execute `python3 verification/check.py` from the directory containing this file. The program uses only Python 3 standard-library modules and terminates on a failed assertion.

It constructs \(S_3\) explicitly as six permutations, independently builds the multiplication table of all \(144\) equivariant endomorphisms on two free orbits, and determines natural conjugacy by searching witnesses for **all four defining equations**. It separately enumerates equivariant conjugacies of image restrictions and compares them across all \(10{,}296\) distinct unordered element pairs. The complete agreement yields \(12\) natural-conjugacy classes, with sizes \(1,4,4,6,6,9,12,12,12,18,24,36\).

A different exhaustive calculation examines all transformations on \(m\) points for \(1\le m\le5\) when the group is trivial, canonicalizes the maps induced on their images, and compares class counts with the formal Euler-product coefficients. Expected counts are \(1,3,7,15,30\). The series routine additionally tests the first six counts for the trivial group and for a group with three conjugacy classes: respectively \(1,3,7,15,30,61\) and \(3,12,37,103,268,675\).

These are exhaustive only in the stated finite test ranges. They are not a substitute for the proof of the image-extension lemma, the nonabelian cycle-product gauge classification, the \(r+s\) realization condition, or the formal cycle-index identity. No independent mathematical audit or external certification has been performed.
