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

# Reproducibility and mathematical verification

Execute `python3 verify.py` using Python 3.8+ and only the standard library. The program performs a direct propagation simulation for every ordered candidate ignition tuple for \(k=2,3,4\) on both labelled paths and cycles, at both orders \(k^2\) and \(k^2-1\). Its separate constructive generator produces the interval tilings, one-overlap arrangements and endpoint truncations, then checks uniqueness and legality under the original propagation rule.

Direct counts by \(k=2,3,4\) for the one-defect path are \(4,20,108\), with redundant-last subcounts \(2,8,36\). The corresponding cycle counts are \(6,48,360\), with redundant-last subcounts \(6,32,180\). At the square order the corresponding path totals are \(2,6,24\), and cycle totals \(4,18,96\), all with zero redundant last ignitions. The generator additionally checks the four claimed families at \(k=5,6\), without attempting an infeasible exhaustive direct search there. Success terminates in `VERIFY_OK`.

The infinite theorem is proved in `RESULT.md`: nonnegative counting of total interval-capacity defect, elimination of an interior singleton overlap using the legal-source distance condition, uniqueness of the induced interval order, and enumeration of the two permissible defect types. Finite checks alone would not prove that classification for arbitrary \(k\). Neither output from other runs nor external computational certificates are required.
