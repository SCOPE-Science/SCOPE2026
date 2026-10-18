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
# Reproducibility and verification

From the directory containing `verify.py`, run `python3 verify.py`. It uses only the standard Python library, reconstructs the edges of both \(L_n^0\) and \(L_n^1\) directly, identifies rich edges through actual four-edge open neighbourhoods, and confirms rich-neighbor coverage for all \(996\) graph instances with \(3\le n\le500\). It also checks the four finite cyclic blocks and the six exceptional witnesses. The recorded output is in `verification_output.txt` and must end in `VERIFIER_OK`.

The four states checks are finite arithmetic checks with complete data supplied in `RESULT.md`; the concatenation lemma is the infinite proof. Testing 996 instances does not establish the theorem for larger orders. Neither the verifier nor this record certifies literature priority or constitutes an independent mathematical audit.
