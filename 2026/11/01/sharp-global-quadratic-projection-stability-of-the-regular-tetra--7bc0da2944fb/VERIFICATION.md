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

# Verification of the tetrahedral projection constant

The proof uses the exact normal/facet-area calculation giving \(A(u)=\frac12\sum_i|u_i|\), the full maximizing orbit of six vectors, and a two-case sign-chamber argument. The critical inequality is
\[
\frac{1-A(u)}{\operatorname{dist}(u,\mathcal E)^2}\ge\frac{1-a}{2(1-2a/3)}\ge\frac{3-\sqrt3}{8},
\]
for the one-positive chamber, with \(a\le\sqrt3/2\). This holds everywhere in that chamber, not just at tested directions.

Run `python3 verify.py` from the extracted package directory. The script uses only the standard library. The strict bound is analytically certified by the proof, not the randomized experiment. The test compares the exact nonmaximizing equality normal and samples 200,000 additional normalized zero-sum normals (seed 236). Numerical tolerances only monitor floating-point calculations. No external verification or independent audit is claimed.
