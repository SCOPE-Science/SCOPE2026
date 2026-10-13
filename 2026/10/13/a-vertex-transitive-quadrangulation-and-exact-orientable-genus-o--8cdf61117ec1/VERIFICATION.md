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

# Reproduction

Run the two included scripts in a directory containing their embedded files:

```sh
python3 verify_rotation.py
python3 verify_local.py
```

`verify_rotation.out` and `verify_local.out` contain the captured stdout of those exact source files. The first checks the graph, rotation system, connectedness, all 1120 darts and 280 simple four-faces; the second checks the ten local group-product and closure identities. The certified graph is finite and fully enumerated; there is no claim to an unbounded parameter theorem. Orientable-genus minimality additionally follows from the written Euler lower-bound argument. Independent external audit has not been performed.
