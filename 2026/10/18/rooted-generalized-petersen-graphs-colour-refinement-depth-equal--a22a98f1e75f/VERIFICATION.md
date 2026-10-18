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

# Reproducibility

Run with Python 3 (standard library only):

```sh
python3 verify_graph.py
python3 verify_quotient.py
```

The two programs are independently written: the first constructs the full cubic graph and iterates vertex-colour signatures; the second iterates a weighted quotient of reflection orbits using the index-folding formula. The programs check exact depth, final orbit classes and root distances for every dimension parameter \(14\le n\le300\), and check wavefront, four penultimate patterns and depths for \(14\le n\le500\). The expected output is included in the two `.stdout` files. These tests are finite and do not substitute for the symbolic induction in `RESULT.md`. There is no external certification or independent audit.
