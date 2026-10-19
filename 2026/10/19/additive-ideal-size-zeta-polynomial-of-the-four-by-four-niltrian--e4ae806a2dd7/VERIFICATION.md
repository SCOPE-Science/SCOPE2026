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

# Verification details

The two embedded independent Python checks, `verify_gf4.py` and `verify_prime.py`, require only the standard library and are run with `python verify_gf4.py` and `python verify_prime.py` respectively. The first constructs the \(12\)-dimensional additive binary realization of the ring over \(\mathbf F_4\), builds all \(3011\) ideals from actual principal generators and their joins, independently checks each ideal's two-sided stability, and counts \(59\) \(\mathbf F_4\)-linear members. It confirms the dimensional histogram \(1,3,1,15,35,39,69,87,651,1395,651,63,1\) across dimensions zero through twelve. The second enumerates reduced-row-echelon subspaces over the prime fields of sizes \(2\) and \(3\), tests ideal closure and compares exact histograms with the theorem. Both complete with `CHECKER_OK` or explicit `MATCH True` for their cases.

The general proof, in contrast, rests on the central-socle dichotomy and counts quotient ideal graphs; no finite enumeration is used to extrapolate the universal formula. No independent third-party audit is claimed, and omitted dimensions/fields have not been exhaustively enumerated.
