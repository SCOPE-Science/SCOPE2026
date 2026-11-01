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
# Verification

The complete proof is in `RESULT.md` and the executable finite checker is `checker.py`. Run `python3 checker.py` in their extracted directory; the program uses only Python's standard library. The checker enumerates orbit labels, computes all cross-orbit Hamming distances for ten nonbinary pairs of alphabet size and dimension, checks every integer scale, and performs complete finite mod-two simplicial homology calculations for the \(q=3,n=4\) fixed complexes at scales \(2\) and \(3\). It separately verifies the sharp binary boundary \(q=2,n=3,r=2\).

The finite checks pass, but they are not an infinite proof; the universal orbit-distance identity, geometric fixed-point triangulation and dominated-vertex collapse establish the unrestricted theorem. For integral homology and all-scale persistence the mathematical proof, not a mod-two finite computation, is decisive. No independent audit or external certification has been performed.
