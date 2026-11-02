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

# Reproducibility and limitations

Run from the directory containing these files:

```bash
python3 verify.py certificate.json
python3 crosscheck.py certificate.json
```

The first program regenerates all 640 balanced five-mers, obtains the 320 reverse-complement orbits and the 120 internally non-overlapping orbits, checks every same-class incompatible pair across the 12 classes, and checks every ordered prefix/suffix test for the 24-word witness. The second program independently encodes DNA as two-bit numbers, recalculates all admissible pairs, and checks the class-clique and witness conditions using bit-masked equality. Both are self-contained, require no optimizer or external library, and run on standard-library Python 3.

Observed results:

```text
VERIFY_OK: balanced=640, initial_orbits=320, admissible_orbits=120, classes=12, witness=24
class_sizes=[10, 10, 7, 8, 6, 8, 7, 12, 12, 12, 14, 14]
CROSSCHECK_OK: numeric masks, 120 valid orbits, 12 incompatibility cliques, 24-word witness
```

The complete finite checks prove the stated length-five extremum. They do not establish an all-length bound, enumerate all optimum codes, guarantee biochemical suitability, or certify historical priority. The two checkers use separate arithmetic representations, but this is not an independent external scientific audit.
