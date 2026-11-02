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

The scientific proof is in `RESULT.md`, with the independently enumerating exact-rational verifier in `verify.py`. Running `python3 verify.py` from the extracted artifact directory returns `PASS: 2777 exact assertions, including complete parent-history enumeration for n<=8.` All parent histories through eight vertices are enumerated with their exact affine probabilities for four reinforcement parameters; five parameters are also checked against telescoping and closed-form identities through size 59.

The exact assertions check normalization, individual birth indicators, full covariance, strict reinforcement boundary, complete sum across birth dates, and the plane-tree central-binomial special case. These are finite consistency checks, not exhaustive verification over all real parameters or all sizes. The all-size and all-real-parameter claims rest on the symbolic derivations in `RESULT.md`. Independent audit was not performed.
