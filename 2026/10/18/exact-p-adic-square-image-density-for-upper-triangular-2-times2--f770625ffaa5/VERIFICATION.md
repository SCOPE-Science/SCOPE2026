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

# Verification of local triangular square-image density

The mathematical proof is in `RESULT.md` and establishes the theorem at every prime and every lifting depth. The following finite computations are supplemental and independently reproducible by invoking `python verify.py` with standard Python 3, without external packages.

The verifier enumerates squares of every scalar residue modulo \(p^k\), then for each ordered diagonal-image pair enumerates all possible root-sign sums and counts the **union** of possible upper-right residues using the least gcd with the modulus. It therefore counts distinct matrix squares rather than square-root multiplicity. It also independently evaluates a long truncated rational valuation series and compares it against the derived exact formulas.

Exhaustive finite ranges are \(p=2,1\le k\le8\); \(p=3,1\le k\le5\); \(p=5,1\le k\le3\); and \(p=7,1\le k\le2\). Final checks are:

- \(p=2,k=8\): finite image proportion \(10647/524288\), compared with limiting \(7/372\).
- \(p=3,k=5\): finite image proportion \(226324/1594323\), compared with limiting \(135/968\).
- \(p=5,k=3\): finite image proportion \(70041/390625\), compared with limiting \(1625/9372\).
- \(p=7,k=2\): finite image proportion \(3382/16807\), compared with limiting \(8575/44816\).

For every tested prime, finite proportions form a nonincreasing sequence bounded below by the closed form, as required by the compactness argument. The rational truncated series agrees with the closed form numerically to \(10^{-12}\). Execution of the verifier returns `VERIFY_OK`.

The finite checks do not establish the infinite formula, rule out earlier equivalent results or certify global integer-matrix solvability. Independent audit is not performed.
