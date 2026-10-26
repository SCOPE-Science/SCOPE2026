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

# Verification and limitations

`verify.py` and `verification_output.txt` accompany this record and are self-contained apart from Python 3, NumPy and SciPy. The recorded successful execution checked 1,960 full matrix-strang composites, 280 energy/phase comparisons and 4,800 scalar iterates. The exact Laplacian is assembled for a one-edge graph and the 4-, 6-, and 8-cycles. Independent numerical matrix exponentials are compared with the analytic scalar formula, and direct energy evaluations with the closed energy identity.

The nonstandard derivations in the proof are the Möbius denominators \(\beta_{\mathrm{DRD}}\) and \(\beta_{\mathrm{RDR}}\), their positive fixed-point hyperbolic-sine representations, the monotonicity of \(\sinh z/z\), and the original-energy factorization. They are verified symbolically in RESULT.md; the program is supplementary finite reproducibility, not an exhaustive parameter scan or proof of novelty. No full-state stability, continuous-domain PDE nonconstant equilibrium, or monotonicity of modified energy was checked or claimed. Originality comparisons are source-limited. Independent audit has not been performed.
