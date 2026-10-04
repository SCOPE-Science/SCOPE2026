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

The construction was checked symbolically. For a word of length \(n\) containing \(m\) zeros, direct multiplication gives the exponent parameter \(t(m-\varphi(n-m))\). Irrationality of \(1/\varphi\) proves this is nonzero for every periodic word. The Bernoulli average at zero-symbol frequency \(1/\varphi\) vanishes exactly because \(\varphi-1=1/\varphi\).

The strong-bunching check uses the source definition specialized to dimension two: strong bunching equals fiber bunching, and the largest one-step bolicity is \(e^{2\varphi t}\). The stated bound on \(t\) makes its product with \(\theta^\alpha\) strictly less than one.

No numerical experiment or finite enumeration is used. The result does not address strong irreducibility, and it makes no classification claim beyond the explicit family.
