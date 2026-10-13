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

# Reproducible mathematical checks

The exact rational reconstruction requires Python 3 and SymPy. Run `python3 verify_hamming.py` from the directory containing this document and the script. The checker forms every distinct-eigenvalue adjacency projector for the test product, computes \(\sum_\theta E_\theta\circ E_\theta\), independently forms the tensor-sector Laurent-coefficient expression, and asserts exact matrix equality and stochasticity. It checks the three-factor rank formula on four parameter pairs and includes positive and zero sectors. A successful run emits:

```
VERIFY_OK exact_profiles=12 exact_entries=9218 special=[(3, 3, 18, 9), (3, 4, 24, 12), (3, 5, 30, 23), (4, 6, 48, 39)]
```

All computations are finite and use exact rational arithmetic; the unrestricted theorem and positivity claims follow from the displayed tensor and sign-balance proof. The check does not certify bibliographic novelty or independently audit the finding.
