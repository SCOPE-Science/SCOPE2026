---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Direct exact-rational differentiation at (u,v)=(1/10,6/5) yields J=[[31/144,-1/24],[45/16,-15/64]], tr=-11/576, determinant 205/3072. Modal trace stays negative; sign of Delta-(a d2+d d1)q+d1 d2 q^2 is the precise strict-linear-instability criterion. For any q0>0, choose d2/d1 just above r_c=((sqrt(Delta)+sqrt(-bc))/a)^2 and set d1=(a r+d)/(2r q0); the negative determinant interval shrinks continuously to q0. Finite spectrum separation proves iff equality of positive support. Exact rational prism and K3,3 Laplacian spectra and both rate-pair signs independently checked; elementary regular graph classification for n<6 proves minimality. Band endpoints with zero determinant are not unstable, and multiplicities are undetectable.

## originality

PASS

Standard graph-Laplacian Turing modal dispersion and influence of topology are known. The additional theorem treats the entire yes/no response as inverse spectral data, constructs arbitrarily narrow positive-diffusivity selectors, and proves a sharp bidirectional same-degree graph-order witness. Ye–Zhou 2023 full primary sections on network dispersion and experiments discuss dependence on eigenmodes and average degree but do not state this response equivalence. Hütt–Armbruster–Lesne 2022 remains a related partially inaccessible comparison. Best-of-knowledge PASS with explicit residual risk.

## value

PASS

Recovering spectral support from a binary response is a meaningful inverse problem and sharply identifies what information cannot be recovered (multiplicities). The minimal six-node cubic witness shows identical degree/order does not control which network is unstable, and positive diffusion controls make the spectral selector constructive. This is not a claim about nonlinear pattern persistence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
