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

# Verification procedure and scope

Run `python verify.py` with Python \(3\) and no third-party packages. The program has three separate mathematical checks: direct evaluation of every \(\pm1\) signing and every ordered index triple on each support for \(3\le n\le41\); an independent three-pair geometric condition for those same inputs; and evaluation of the all-length counting sum, cubic residues, and floor expressions on finite test ranges up to \(n=1000\). The direct checker never assumes the structural pair criterion. It prints `ALL_CHECKS_PASS` on success.

Expected examples are \(G_3(6)=18\), \(G_3(10)=92\), \(G_3(20)=770\), \(G_3(32)=3220\), \(G_3(40)=6336\), and \(G_3(41)=6818\). The full reproducible table for lengths \(3\) through \(60\) is in `weight3_counts.tsv`.

The finite tests are deliberately not presented as proof for every length. The general proof in `RESULT.md` derives the pair criterion from the constraint, classifies the exceptional cases, and counts all supports algebraically. Independent external audit has not been performed.
