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

The proof is an exact case analysis over arbitrary nonzero complex vectors of length four. It uses only the four-character Fourier transform and the fact that a one-frequency inverse transform is nonzero everywhere; the key nonstandard assertion, the shift-two ratio classification, is derived algebraically in the proof rather than delegated to testing.

Run `python verify_z4.py` from the directory containing this file. The recorded deterministic output is `verification_output.txt`. The implementation uses exact Gaussian integer operations for the sample alphabet \(\{0,1,2,-1\}\); the finite check covers 65,025 pairs and reproduces the sharp example and all enumerated support-six equivalences. It does not test arbitrary complex phases and is not substituted for the universal proof.

No external certification, independent replication or full higher-order support classification is asserted.
