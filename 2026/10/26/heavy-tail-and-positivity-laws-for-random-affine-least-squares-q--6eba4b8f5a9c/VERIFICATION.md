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
# Reproduction and limitations

Run `python3 verification/verify_affine_ls.py` from the artifact root. The test uses only the Python standard library and deterministic random seeds. The executed program passed 3,000 sample-moment/weight identities, 350,000 independently sampled three-node cases against the exact positivity probability, a 7,200-direction evaluation of the centered-circle integral, numerical radial-tail integrals at thresholds 30, 100 and 300, and clustered-design scaling checks.

The proof, not the finite tests, establishes the universal asymptotic and integrability statements. The calculation assumes iid uniform continuous node locations, unweighted affine least squares in exact arithmetic, and independent centered, equal-variance errors when discussing noise amplification. The result does not verify other sampling distributions, higher-degree spaces, pruning, rejection or regularization. Independent review has not been performed.
