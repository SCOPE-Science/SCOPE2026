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

# Verification and scope

The exact argument uses one two-dimensional rank-one-projector identity, enumeration of row-label transitions, a binomial generating function, and monotone Riemann sums with a Laplace-type limit. The script `verify_pair_shuffling.py` is fully standalone using Python's standard library. Running `python3 verify_pair_shuffling.py` produced `PASS: exact enumeration paths 386 ; finite ordering cases 16 ; power-law leading-constant comparisons 12 ; total checks 414`.

The direct exact enumerations test through four epochs for overlap \(3/5\), and numerical tests evaluate the four finite formulas for heterogeneous overlaps and dimensions up to two million. The program does not prove the limits for every exponent; those follow from the argument in RESULT.md. The limits require \(t^\beta/N\to0\) and do not describe fixed finite dimension at arbitrarily late epochs.

The scientific review is not an independent audit. No claim is made about adaptive randomized solvers, floating-point stability, runtime, or mathematical universality outside this specified family.
