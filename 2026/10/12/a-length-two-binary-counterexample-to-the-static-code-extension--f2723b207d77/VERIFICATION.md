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

The claim has a complete symbolic proof over \(\mathbb F_2\). The defining staticity evaluation maps are isomorphisms because all relevant modules are one-dimensional over \(\mathbb F_2\). The displayed embedding is injective but changes Hamming weight from \(1\) to \(2\), while every monomial transformation preserves Hamming weight.

`artifacts/verify.py` supplies an exact finite replay. It checks linearity and injectivity, enumerates every nonzero possible image of the generator, enumerates the binary length-two monomial restrictions, and confirms that \((1,1)\) is the unique non-isometric embedding image. Successful execution prints `VERIFY_OK`.

The computation is only a consistency check; no unbounded or probabilistic step is used. The result does not determine whether the later Morita-invariance theorem has a different proof, and no independent audit has been performed.
