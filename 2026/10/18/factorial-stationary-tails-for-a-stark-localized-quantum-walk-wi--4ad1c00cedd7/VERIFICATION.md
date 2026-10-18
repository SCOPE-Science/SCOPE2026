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

# Verification checks and scope

Execute `python verify.py` with the dependencies in `requirements.txt`. The verifier checks three independent finite-lattice propagators against Bessel-square transition probabilities, three families of high-precision one-period integrals against the exact finite-product identity, and their approach to the sharp factorial asymptotic. Expected output contains `VERIFY_OK`. These are finite numerical checks, not proofs of a uniform or infinite-lattice theorem. The analytical proof uses an exact renewal representation, uniformly bounded Bessel-series remainder, a closed recurrence for weighted sine powers, Stirling's formula and the Euler product for \(\sinh\).

The exact asymptotic requires \(h\ne0\), \(F\ne0\) and \(r>0\) fixed. It is not uniform as \(F\to0\), or in the infinite-site limit of the finite truncation used for the numerical propagator. No independent review or certification has been performed.
