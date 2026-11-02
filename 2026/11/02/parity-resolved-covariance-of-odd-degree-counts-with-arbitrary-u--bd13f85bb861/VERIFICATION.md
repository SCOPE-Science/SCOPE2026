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

# Verification details

Use Python 3 (standard library only):

```bash
python parity_motif_verify.py
```

The verified run printed `PASS 338 exact-rational identities and sign checks`. Independent enumeration uses probabilities \(1/4,2/5,1/2,3/5,3/4\), graph orders \(2\) through \(5\), and eight template graphs (when the template fits); every ambient edge configuration is weighted exactly using rational arithmetic. A separate exact-arithmetic pass checks the edge and triangle closed forms for orders up to \(30\) and three edge probabilities. The proof in RESULT.md, rather than finite enumeration, provides the infinite generality and exact midpoint multiplicity. No independent audit has been performed, and priority beyond inspected sources remains uncertain.
