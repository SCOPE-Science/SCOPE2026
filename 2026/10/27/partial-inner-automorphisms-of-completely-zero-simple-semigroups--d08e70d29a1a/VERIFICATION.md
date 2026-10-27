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
# Direct mathematical checks

The supplied `verify_rees_inner.py` constructs finite groups, Rees zero-matrix semigroups, all generating maps \(\phi_{g,h}\) (including pairs involving the adjoined identity), and the exact partial-map domains directly from multiplication. It checks closure of the obtained map family under all possible compositions, verifies the global identity and the zero partial map, and compares the number of distinct maps with the predicted Brandt formula.

Recorded execution: cases using the trivial group, \(C_2\), \(C_3\), and \(S_3\), crossed with one-by-one, two-by-two diagonal, two-by-two triangular, and two-by-two full matrices; also two regular two-by-three matrices with nonidentity coefficients. In every case the predicted count agreed and closure held. The direct checker printed `VERIFY_OK`.

Coverage limits: the program is finite and does not check arbitrary groups or index sets; those are handled by the abstract calculation of both-sided fixed-point domains and explicit group conjugations in `RESULT.md`. A later independent mathematical audit has not been performed.
