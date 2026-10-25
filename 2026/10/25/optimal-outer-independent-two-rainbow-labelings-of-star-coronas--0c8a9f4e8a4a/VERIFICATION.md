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

## Reproducibility

Run `python3 verify.py` in the extracted artifact directory; the script depends only on the standard library. It constructs the full graph with named original and leaf vertices and tests each proposed labeling directly for independent empty-label vertices and two-color neighbor coverage.

The verifier exhaustively considers every labeling for every graph on \(1\), \(2\), and \(3\) original vertices with two private leaves. For five four-vertex graphs it examines all labelings of the proved optimal weight \(2n\), rather than relying on the structural form of minimizers. The test also checks all optimal-weight candidate labelings on bases of up to three vertices for three leaves and up to two vertices for four leaves. An independent vertex-subset computation supplies the predicted independent-set polynomial, and separate blow-up tests validate the interpolation identity for three clone multiplicities.

**Observed execution:** `VERIFICATION_OK graphs= 30 plus_three_blowup_identities`.

The infinite identities are justified by the proof's per-block equality characterization. Exhaustive finite checking is not an infinite proof. The \(\#\mathrm P\)-hardness consequence uses Provan–Ball's established counting theorem and the explicitly described polynomial-time interpolation reduction; this external premise was checked bibliographically, not re-proved by enumeration.

## Scope limits

No claim is made about all nonminimum labelings, the single-leaf corona case, parsimonious completeness, or bounded-degree hardness. No independent scientific audit has been performed.
