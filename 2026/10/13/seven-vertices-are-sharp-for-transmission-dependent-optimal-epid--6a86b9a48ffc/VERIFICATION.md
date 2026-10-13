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

# Verification record

The finite theorem is checked by `python3 check.py`, included beside this document. A successful execution yields `VERIFY_OK` and the exact class counts. The standalone program uses only the Python standard library and recomputes all tree representatives from Prüfer encodings, not from a supplied table. It performs rational Bernstein coefficient comparisons on vertex distance polynomials for each class.

The proof also contains analytic identities: for the broom candidates the score gap is \(p(1-p)(1-p-p^2)\), and for the joined-claw candidates it is \(p(1-p)(1-2p)\). The checker verifies the integer polynomial coefficients directly. These identities, plus exact sign arguments and candidate exclusion, prove statements for every real \(0<p<1\); selecting finitely many floating-point transmissibilities would not suffice.

The enumeration ends at tree order seven, as required by the claim. It is not a classification for larger trees, irregular rates, multiseed epidemics, or arbitrary graphs. No external audit or independent scientific validation has been performed.
