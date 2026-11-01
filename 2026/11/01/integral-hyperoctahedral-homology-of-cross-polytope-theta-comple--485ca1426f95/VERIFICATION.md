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

The uniform proof is recorded in `RESULT.md`; no finite test is used to infer the all-parameter statement. Two standard-library-only programs provide independent finite consistency checks.

Run `python verification/verify_crosspoly.py`. This enumerates the actual theta-complex simplices of seven small cases, computes every signed fixed-face contribution to the reduced Lefschetz character for every signed permutation, and compares with the claimed exterior-power character. It checks \(8+48+48+384+384+384+3840=5096\) group-element/case combinations.

Run `python verification/check_lattices.py`. This constructs explicit adjacent-transposition matrices for the augmentation kernel and its dual over the prime field of a prime divisor of \(n\), and checks fixed-space dimensions for \(3\le n\le10\).

The exact recorded output is `verification/verification_output.txt`. Both scripts terminated with their respective success markers, `VERIFY_OK` and `MODULAR_VERIFY_OK`. The tests verify rational characters and sample modular invariant dimensions; they do not directly certify an infinite family, all integral attaching maps, or uniqueness in the literature. The full proof uses integral chain complexes, a simplicial contiguity equivalence, orientation-aware combinatorial Alexander duality, and a uniform modular obstruction.
