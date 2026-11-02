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

# Computational verification

The source equation and interval assumptions are stated in `RESULT.md`. Run the self-contained script with Python 3 and SymPy/mpmath:

```
python proofcheck/mmap_markov_check.py
```

The script checks symbolic characteristic polynomials and generating-function identities for all three interior transition matrices; checks the algebraic equivalences between the valley image and the three turning-point targets; reconstructs matrix entries directly from numerical images of the four basic intervals; and counts turning-point preimages to seven iterations independently of matrix powers. Its output was:

```
PASS: 3 characteristic polynomials, 3 rational generating functions, 3 algebraic branch identities,
       69 Markov-cell and independent inverse-image lap checks; endpoint branch values.
```

The computations use exact symbolic arithmetic for matrix and polynomial identities and 70-digit working precision for the numerical inverse-image enumeration. They do not prove an infinite entropy identity or exhaustive publication priority. Those conclusions require the analytical derivation given in `RESULT.md`. Independent mathematical audit has not been performed.
