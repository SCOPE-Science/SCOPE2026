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
# Reproducible checks

Run `python3 verify.py` with Python 3 standard library from the directory containing the supplied `verify.py`. The script derives the actual polygon side counts by crossing each of the twelve box edges as eight vertex heights are swept, then compares with the independently specified analytical offset-length expressions. It checks 25,000 deterministic pseudo-random oriented normals for each of five positive box aspect ratios, producing 125,000 configurations and 875,000 independent interval classifications. It also compares the exact formula to sphere averages. Recorded output ends in `VERIFY_OK configurations= 125000 independent_edge_counts= 875000`.

The proof in RESULT.md separately gives all-parameter symbolic expressions from spherical boundary integration; no finite sample is asserted to prove an identity over infinitely many real parameters. The universal parallelotope identity is a pointwise signed-height argument. The 1991 historical source cited there was not available as full text and is a priority limitation; no independent mathematical audit has been conducted.
