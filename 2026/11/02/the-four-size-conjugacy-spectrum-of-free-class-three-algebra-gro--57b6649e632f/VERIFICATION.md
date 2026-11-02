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

# Reproduction and limits

Run `python3 verify.py` with Python 3's standard library. The checker represents the original positive-degree free words of lengths one, two, and three. It constructs all degree-two and degree-three commutator coefficients from concatenation and applies exact Gaussian elimination in finite fields, including arithmetic of \(\mathbb F_4=\mathbb F_2[t]/(t^2+t+1)\).

It exhausts all \(q^{d+d^2}\) degree-one and degree-two inputs for the five listed \((d,q)\) configurations; because degree-three inputs are central, multiplying the counts by \(q^{d^3}\) gives exact exhaustive element counts for each listed finite group. It does not enumerate every full-group element explicitly or prove arbitrary-rank identities computationally. The general theorem follows from the free-word proof in RESULT.md. Compare the output to VERIFICATION_OUTPUT.txt, including the final marker.

Every asserted finite-field enumeration was run from the standalone original code; no proprietary dependencies, remote certificates or external auditing were used. Independent audit: not performed.
