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

# Reproducibility and verification

The self-contained standard-library program `verify.py` constructs all directed paths of complete transitive layered digraphs and their nonregular root-of-unity boundary matrices over suitable finite fields. It independently constructs every fixed-augmentation subset block and its boundary. It checks complete Mayer homology dimensions by the identity \(\dim H_k^{N,q}=\dim C_k-\operatorname{rank}(d^q|_{C_k})-\operatorname{rank}(d^{N-q}|_{C_{k+N-q}})\), checks the canonical universal block multiplicities are constant at fixed subset size, and checks the closed three-level \(N=3\) numbers. Every sample whose chain degrees permit it is also checked for \(d^N=0\).

Run `python verify.py` using the supplied file, without external dependencies. Expected exact output: `VERIFY_OK: 41 complete direct-vs-universal Mayer homology comparisons with canonical block and low-dimensional checks`.

The test domains contain finite layered graphs with two to five levels, varying cardinalities, and parameters \(N=2,3,4,5\). Arithmetic is exact modular arithmetic in fields containing primitive \(N\)-th roots. Finite-field agreement provides an independently generated finite consistency check, not an infinite characteristic-zero proof. The all-size theorem and equivariant trace formula follow from the displayed module splitting and the explicit rescaling proof, not from computational extrapolation.

Independent audit: not performed. No independent validation is claimed.
