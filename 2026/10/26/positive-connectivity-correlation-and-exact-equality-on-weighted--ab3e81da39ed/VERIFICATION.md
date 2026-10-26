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
# Verification of mathematical calculations

The proof reduces the universal result to independent cactus blocks. On each cycle, four disjoint missing-edge cells yield exact unnormalized masses `Z`, `R`, `S`, `H`, so that `Z*H-R*S` is a polynomial in four nonnegative variables. Direct expansion yields the explicit positive decomposition shown in `RESULT.md`. Its strictness criterion is exact because all missing-edge weights are positive.

Reproduce the finite checks with `python3 verify.py`; the program uses only the Python standard library and exact `fractions.Fraction` arithmetic. It checks all ordered combinations of two marked vertex pairs on nine weighted cactus examples and evaluates the polynomial identity and its strictness condition at 256 four-tuples. Observed result: PASS, 256 polynomial evaluations, 9 graphs, 701 acyclic edge subsets, 2145 ordered pair-pair covariance checks.

These finite tests do not establish universal graph claims; the steps in `RESULT.md` supply that proof. The literature review is not a guarantee of global novelty. Independent validation and independent audit have not been performed.
