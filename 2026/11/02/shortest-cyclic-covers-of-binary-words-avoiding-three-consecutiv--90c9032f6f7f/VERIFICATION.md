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

# Exact certificate replay

Run `python3 verify.py` with `CERT.json` in the same directory; no package installation is needed. The reported `VERIFY_OK` means that every one of the fourteen cases has passed the following checks: complete regeneration of every linear binary input word avoiding \(000\), exact nonnegative augmentation multiplicities, de Bruijn conservation at each vertex, the full-graph dual potential inequalities, exact equality between primal augmentation cost and its dual lower bound, and an explicit cyclic word realizing the complete required-plus-extra window multiset. Orders three and four have an additional exhaustive direct search for all shorter binary circles.

The certificate contains finite integer data, rather than floating-point solver logs. Thus the proof does not depend on how the optimal primal and dual solutions were originally discovered. For reproducibility, `CERT.json` stores unsigned byte augmentation arrays in ascending arc index and signed little-endian 16-bit potentials in ascending vertex index, both compressed with zlib and encoded in base64. The exact cyclic witness for every order is plain binary text in the same JSON object. File-local loading prevents accidental use of another directory's certificate.

The logical lower-bound argument and its limits are specified in `RESULT.md`. The certificate proves the values only through order sixteen. A finite successful replay does not assert any general all-order law, and external independent audit has not been performed.
