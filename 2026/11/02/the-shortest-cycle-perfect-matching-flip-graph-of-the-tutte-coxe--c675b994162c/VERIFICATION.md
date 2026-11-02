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

# Reproduction of the finite proof

The two checkers require only Python 3 standard-library modules and are executable independently:

```
python3 verify_duads.py
python3 verify_symplectic.py
```

`verify_duads.py` enumerates incidence-preserving bijections of 15 duads with 15 synthemes, checks every pair's four-coordinate difference, computes all eccentricities by BFS, and calculates the \(S_6\)-orbit partition under adjacent transpositions. It verifies the even and odd permutation-class metric profiles and the exact quadrilateral count.

`verify_symplectic.py` constructs a separate classical model from 15 nonzero four-bit symplectic vectors and 15 isotropic lines. It enumerates every perfect matching by graph-edge recursion, verifies the absence of 4- and 6-cycles and the existence of exactly 90 eight-cycles, performs every alternating flip directly by edge-set XOR, and checks all-source distance vectors and 4-cycle counts. It also checks that each short cycle is alternating in 32 states.

`certificate.json` supplies the complete state encodings and adjacency lists; it is not used as an input to either checker. The certificate and programs together permit regeneration of every finite count without relying on logs. Both independent programs were executed successfully. Their exhaustive finite search establishes exactly the stated result on this single labelled graph; it supplies no infinite-family theorem and is not an independent scholarly review.
