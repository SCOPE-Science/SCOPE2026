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

# Reproducibility and limits

The standalone `verify.py` is a deterministic Python 3 program requiring only the standard library. Run `python3 verify.py` in the same directory. Expected output is:

```text
PASS: extension-amalgamation lemma: 1472 compatible ordered pairs
Exhaustive source and target sizes 1,2, plus 6000 fixed-seed trials on 3-world structures.
PASS: representative nested rank-two fluted sentence invariance.
```

The checker enumerates all structures for unary \(P\) and binary \(R\) on one- and two-world nonempty sets; checks each compatible source-target pair; additionally samples 6,000 fixed-seed ordered pairs of three-world structures. For each compatible pair it reconstructs a finite induced extension with the target's complete set of signed row descriptors. It also checks preservation of truth for a representative rank-two sentence when two structures have identical descriptors. The script is finite evidence only and does not enumerate all three-world pairs, all relational signatures, or infinite structures. The general theorem is supported by the written constructive proof, not by an extrapolation from numerical tests.

Source comparison is documented separately in the scientific review and structured report; absence of a database result is not a mathematical certificate of priority. Independent audit status remains not performed.
