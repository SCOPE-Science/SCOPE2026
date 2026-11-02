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

# Verification performed

The two bundled Python 3 programs were executed directly and their exact printed results captured in `CHECK.out` and `CHECK_INVERSION.out`. Each program exited successfully and printed `VERIFY_OK`.

`CHECK.py` constructs multiplication in five finite rings without relying on the probability formula: a radical extension, two semisimple examples, a noncommutative upper-triangular ring, and a mixed-characteristic product of fields. Complete multiplication distributions were evolved exactly for every word length from one through six and nilpotent outputs were counted. The resulting rational probabilities match the formula at every tested length. It also verifies the published \(15/64\) two-factor collision and its length-three separation.

`CHECK_INVERSION.py` expands the exact finite exponential spectrum of \(1-P_k\), checks dominant-base inversion on 329 field-factor multisets with up to four factors, and checks a finite Vandermonde horizon in all pairwise comparisons among 28 two-factor samples. It also checks the sharpness example \(\mathbb F_4\) versus \(\mathbb F_2^2\).

# Mathematical limits

The tests are exhaustive only for the specific finite rings and field-size multisets identified. The general theorem, the asymptotic reconstruction step, and the universal finite bounds rely on the complete algebraic proofs in `RESULT.md`; experimental agreement is not used as an infinite proof. Exact asymptotic limits are mathematical, not noise-stable numerical methods. No independent mathematical review or external certification has been performed.
