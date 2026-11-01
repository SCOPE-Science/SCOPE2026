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

# Reproducible checks and scope

Run `python3 verify.py` using Python 3.9 or later; only standard-library imports are required. Successful output ends in `C7_KN_UNIFORM_MORSE_CERTIFICATE_OK` and is reproduced in `verification_output.txt`.

The checker exhaustively lists all \(2^7\) and \(3^7\) seven-row words and filters total domination, correct adjacency colors, and exact occupied-color support, producing 29 and 28 fixed-sector faces. It performs full directed-Hasse acyclicity checks and signed Morse-boundary reduction; the two-color top boundary is exactly \([0]\), with no modular approximation.

Independent full-face enumerations for four distinct color counts \(n=2,3,4,5\) produce augmented face counts 843, 5,282, 36,069 and 262,884. All cover incidences and full matching acyclicity are checked (3,262; 25,242; 218,036; 1,961,820 incidences). Every full-complex top integral Morse matrix vanishes, with dimensions \(0\times1\), \(1\times3\), \(3\times6\), \(6\times10\).

The infinite-parameter conclusion is **not** inferred from those four samples. It follows from the proof that first-color matching leaves an upper filter whose face-poset cover incidences preserve color support and in which every face uses at most two nonzero colors; all surviving sectors are exact copies of the two fully enumerated finite models. Thus the finite sector computation verifies all possible remaining local cases for every \(n\ge2\).

This is an ordinary reproducible computational and mathematical check, not independent external validation. No machine-assisted proof beyond the given explicit mathematical reduction is claimed.
