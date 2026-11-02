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

# Verification record

The included standard-library Python program `check_growth_k2n.py` was executed from its actual packaged content and returned `PASS: 2541 exact/computational assertions`. For each \(1\le n\le8\), a separately programmed boundary-edge Markov enumeration with exact rational arithmetic agrees with the bridge/binomial formula for every root degree. The code also checks the exact mean/variance decomposition, the birthday tail for \(1\le n\le69\), and finite stochastic dominance for every possible degree cutoff for the tested small graphs. Numerical scaling checks at \(n=100,1000,10000\) are only diagnostics.

The all-size and limit statements follow from the explicit proof in `RESULT.md`; no finite computation is being used to extrapolate an infinite theorem. An independent mathematical audit has not been performed. Historical priority, other root positions, and graphs beyond \(K_{2,n}\) are not certified.
