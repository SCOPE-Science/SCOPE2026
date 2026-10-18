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

Run `python3 verify.py` in the directory containing this document, using Python 3 and no third-party packages. Expected terminal text:

```
VERIFY_OK: 95 moduli; all prime-divisor/cardinality/residue counts; positivity; odd-modulus nonempty subset contrast
```

The verifier takes each integer modulus \(2\le N\le96\), enumerates the unit residues, independently computes the subset-size and sum-residue counts by descending dynamic programming, and checks the stated integer formulas and strict biases for every divisor prime, cardinality and residue. It separately counts all nonempty subsets modulo each odd \(N\) to verify the pooled-cardinality contrast in the finite range. These checks are exhaustive over that explicitly bounded range, not an infinite proof or an independent mathematical audit.

The infinite conclusion uses the surjective reduction homomorphism and uniform fibers, the exact product of all nontrivial \(p\)-th roots, character orthogonality, and positivity of every coefficient of the bounded-composition polynomial. No external computational certificate is required by the proof.
