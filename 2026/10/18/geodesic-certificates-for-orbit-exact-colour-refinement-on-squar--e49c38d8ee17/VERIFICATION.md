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

Run all three standalone Python 3 scripts from a directory containing the extracted files:

```sh
python3 verify_direct.py
python3 verify_certificate.py
python3 verify_automorphisms.py
```

The outputs in `direct_output.txt`, `certificate_output.txt`, and `automorphisms_output.txt` were obtained from these exact scripts. `verify_direct.py` checks 66 orders and 116765 aggregate vertices. `verify_certificate.py` checks 496 orders for algebraic injectivity and separately 9425 vertices with BFS. `verify_automorphisms.py` enumerates rooted automorphisms in orders \(n=5,6,7\) via NetworkX (a separately installed Python dependency).

The theoretical claim for all \(n\ge5\) is proved symbolically in `RESULT.md`: verification ranges are finite checks, not exhaustive proofs over an infinite parameter. No independent scientific audit has been performed.
