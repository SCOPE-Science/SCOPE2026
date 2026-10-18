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

The finite verification can be reproduced with Python 3.10+ from the two files `verify.py` and `certificate.json`:

```
python verify.py > reproduced.json
cmp reproduced.json certificate.json
```

The program works with exact integer subset counts, rational expectations and Python's standard library. It checks all nonempty-row three-site incidence matrices with at most five species for binomial inversion across all available factorial moment orders (94,773 instances), and exhausts all 2,800 three-site matrices with at most four species for first-two-moment profile identifiability. It verifies both extremal communities directly and exhausts the 35 sorted triples with entries in 0 through 4 for the only ambiguous mean/variance triple pair.

The unrestricted inversion is proved symbolically using finite double counting and the alternating binomial identity. The impossibility claims for at most two sites or two species, and the separate three-site four-species argument, are also mathematical proofs. The code is corroborative rather than a substitute for an infinite proof. No sampling-error or stability estimates were obtained.
