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

# Verification of cyclic-minimum coincidence formulas

Run `python3 verify.py` using Python 3.9 or later; no additional libraries are required. The program enumerates primitive necklaces for \(2\le n\le24\) and \(1\le k\le5\), computes both canonical rotations directly, compares the counts for \(k=1,2,3\) with the proved formulas, and checks every uniquely odd-minimal-gap count against the coefficient formula for \(k=2,3,4,5\). It also separately enumerates indexed circular words without adjacent zeroes for \(3\le n\le16\), comparing the standard closed expression. The output is `VERIFY_OK` followed by the number of primitive-necklace cases examined and the parameter scope.

The program's finite checks are supporting reproducibility evidence. The structural gap-parity argument, orbit enumeration, singularity estimate, and dense-regime entropy bound in `RESULT.md` constitute the proofs of the infinite statements. No independent audit or infinite machine certification is claimed.
