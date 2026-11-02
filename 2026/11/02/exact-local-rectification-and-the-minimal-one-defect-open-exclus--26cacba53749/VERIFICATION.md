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

The reproducibility bundle contains `certificate.json` (integer-polynomial stationary-distribution coefficients at orders zero, one and two) and `verify.py` (standalone Python 3, standard library only). Execute `python verify.py` in the bundle directory. Its exact-integer polynomial checks reconstruct the generator from the transition rules and verify the stationary balances, normalizations, coefficient identities, and positivity certificate for every formal defect rate.

The verifier was executed against the included files and returned `PASS: exact polynomial balances at orders 0, 1, 2; normalization; exact current coefficients; positive-coefficient sign certificate.` Direct finite-rate stationary linear solves were also performed at several slow and fast defect rates; their current-even-part signs agreed with the exact formula. Numerical agreement is supplementary and is not used as an infinite-parameter proof.

The proof covers \(t>0\), reservoirs \(\rho_L=(1+\delta)/2\) and \(\rho_R=(1-\delta)/2\), and the local expansion at \(\delta=0\). It does not certify any finite nonzero driving interval uniformly in \(t\), nor all system sizes. The source-comparison limitations in the scientific result remain; no independent audit has been performed.
