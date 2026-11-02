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

# Verification record

The exact standalone Python 3 checker is `rhombicuboctahedron_harmonic_certificate.py`. Run `python3 rhombicuboctahedron_harmonic_certificate.py` in a directory containing that file. It constructs all twelve antipodal representatives, three signed relations, six explicit invariant vectors, a universal residual quadratic identity in formal Legendre coordinates, and all degree-wise assertions for \(0\le k\le199\) in the exact field \(\mathbb Q(\sqrt2)\). Its terminal sentinel is `RHOMBICUBOCTAHEDRON_SAMPLING_CERTIFICATE_OK 200 exact degrees`.

The all-degree conclusion rests additionally on the analytic Bernstein–Gershgorin argument for \(k\ge200\), proved in RESULT.md; the finite checker does not attempt or imply exhaustive testing of infinite degrees. The exact maximum is taken only over full-rank twelve-by-twelve Gram matrices. The certificate supports a reproducible self-review, not any independent audit, machine-checked foundational certification, or publication priority determination.
