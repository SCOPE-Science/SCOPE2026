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

Run `python verify.py` with Python 3. The checker is self-contained and uses exact modular integer arithmetic.

Expected checks:

- `PDS_DIFFERENCES_OK: 72 distinct nonzero residues`
- `AFFINE_ORBIT_OK: 584 distinct PDSs; stabilizer size 9`
- `SEED_CONTAINMENT_OK: 9 transformations, 1 distinct PDS`
- `FOURSET_SIGNATURE_OK: 9 of 126 subsets; all are 2^j*SEED`
- `SEED_AFFINE_STABILIZER_OK: identity only`
- `VERIFY_OK`

The checker exhausts the finite domains stated above. The claim that every perfect difference set modulo 73 belongs to this affine orbit is a literature premise, supported by Hall’s classification as reported by Niu; the checker does not replace that premise with a finite search over arbitrary nine-subsets. Independent audit has not been performed.

The trusted importer initializes absent external channels as unperformed; research never assesses or authors them or resets old evidence.
