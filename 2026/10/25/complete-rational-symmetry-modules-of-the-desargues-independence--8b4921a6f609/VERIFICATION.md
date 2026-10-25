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

# Reproduction and limits

Run `python3 verification/verify_desargues_character.py` using Python 3 and only standard-library modules. The code constructs the 20-vertex incidence graph from all two- and three-subsets of five labels and checks all 6,212 augmented independent faces. Its binary boundary-rank vector is `(19,141,519,991,932,383,97,18,2)`, constraining rational Betti numbers. It builds each sign-antisymmetrized rational chain orbit, checks its integral coefficients and full signed boundaries, finds exact rational boundary ranks `{3:4,4:16,5:9,9:2}`, and obtains a unique fourth-degree sign-homology generator. Complement has sign-chain alternating trace `-1`. Direct oriented-simplex traces on all fourteen conjugacy-class configurations establish the claimed full characters. The final marker is `DESARGUES_EQUIVARIANT_HOMOLOGY_VERIFIED`.

These are exhaustive finite calculations for the stated graph, not an infinite-family theorem. Rational equivariance does not classify integral representations; bibliographic searches do not prove global publication priority. The calculation has not received independent scientific audit.
