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

# Exact verification instructions

The included `certificate.json` contains 471 integer row/column operations on a 23-by-23 reduced Laplacian. The script `verify_certificate.py` constructs the McGee graph using its LCF sequence, confirms cubic degree, connectivity and girth seven, replays every elementary unimodular operation and checks the final complete Smith diagonal and its product.

The script `verify_independent.py` starts instead from a separately indexed 36-edge description. It constructs the reduced Laplacian, evaluates the determinant with fraction-free Bareiss elimination and computes the entire primary Smith exponent lists modulo prime powers using ring-unit pivots.

Execute from the artifact directory:

```
python3 verify_certificate.py
python3 verify_independent.py
```

Observed exact completion markers:

```
INTEGER_SMITH_CERTIFICATE_PASS
INDEPENDENT_MODULAR_PASS
```

The first checker returns invariant factors 11, 44, 132, 2640 and determinant 168664320. The second returns prime-power exponent lists 2:(2,2,4), 3:(1,1), 5:(1), 11:(1,1,1,1), and the same determinant. This verifies the specified finite graph and integer arithmetic; it neither certifies historical novelty nor extends the result to other cages.
