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

The full proof and definitions are in `RESULT.md`. Run `python3 mus_checker.py` using a standard Python 3 interpreter in the same directory. The checker uses brute-force occurrence multiplicities to obtain all minimal unique substrings, compares their exact sets with the structural theorem for every nonnegative gap triple of total at most 35, and checks rational generating-function coefficients independently by convolution. The run checked 8436 gap triples and reported success. It also tests both length-five four-factor examples.

The finite test does not prove the theorem for unbounded gap lengths. The all-length result depends on the factor-type exhaustion, the flank uniqueness argument, the run uniqueness exception and the rational generating-function case split detailed in `RESULT.md`. No third-party certification or independent audit has been performed.
