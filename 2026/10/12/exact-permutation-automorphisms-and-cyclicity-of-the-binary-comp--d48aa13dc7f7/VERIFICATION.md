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

# Computational verification

Run `python3 verify.py` with Python 3.10+ and no third-party dependencies. The script reconstructs every length-\(2k\) codeword by the stated generator for \(k=2,4,6,8,10\). It verifies the minimum-support description and intrinsic coordinate-pair signatures for \(k=6,8,10\), exhaustively enumerates all \(46080\) pair-preserving permutations for \(k=6\), and checks all coordinate permutations at \(k=2\) and \(k=4\). In the \(k=6\) case it independently confirms that exactly \(23040\) pair-preserving permutations are automorphisms and exactly \(23040\) are not, and checks full-length cycles in the small boundary cases. Expected final line: `VERIFY_OK`.

These are finite independent checks of the formulas, not a substitute for the proof for all even \(k\). The infinite result follows from the support reconstruction and swap-parity calculation in `RESULT.md`. Literature originality remains subject to unindexed equivalent results, and independent audit has not been performed.
