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

- Reconstructed the universal lower bound from the encoding formula: \(|\sigma_T|\ge2L+4s\), \(n\le kL\), hence \(|\sigma_T|+k\ge2\sqrt{2n}+4s\).
- Checked the witness transducer: one state, self-loop outputs \(0^a\) and \(arepsilon\), input \(0^{2a}\); output is \(0^{2a^2}\) and total description length is \(4a+4\).
- Equality characterization: the real lower-bound value \(2\sqrt{2n}+4\) can be an integer only if \(2n\) is a square; this forces \(n=2a^2\). The witness attains equality for each such \(n\).
- Scope limitation: no exact formula is claimed for the other values of \(n\).
- The related 2011 journal article was not inspected in full; literature-overlap risk remains.
- Independent audit and independent validation have not been performed.
