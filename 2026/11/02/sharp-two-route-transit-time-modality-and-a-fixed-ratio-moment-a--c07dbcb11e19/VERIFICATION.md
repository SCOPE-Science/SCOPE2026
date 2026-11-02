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

# Reproduction and verification

Execute `python3 proof_check.py` from the extracted package directory with the Python standard library. It verifies both exact rational moment identities; a rational lower bound on \(e^{16/5}\); critical-weight inequalities for the moment-aliased pair; the \(k=3,R=3\) critical point; and 800 sampled mode predictions versus the sign pattern of the full derivative. All checks executed successfully for the packaged source. No third-party data are required.

The universal proof is the monotonicity of \((k-2)/s-1/(k-1-s)+R-1\) for \(k\ge3\), and the explicit unique maximum of \((1-s)e^{(R-1)s}\) for \(k=2\). Finite numerical sampling cannot verify the continuum of parameter values and is not relied upon for those assertions. Exact moments concern the mathematical idealization, and statistical identifiability under noise is unproved. Historical originality is reviewed within accessible primary literature but not externally certified; one relevant 1990 density-shape study could not be inspected in full.
