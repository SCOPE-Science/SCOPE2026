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

The proof uses the exact integral ray/divisor matrix \(M_m\), whose determinant is identically one; the four Cox equations reduce to two affine-plane graph equations. Distinct roots of \(h_m(x)=x^m+(1-x)^m\) are counted by the substitution \(z=x/(1-x)\), which excludes exactly \(z=-1\) for odd \(m\). The four transverse nodes and compactly supported cohomology yield the integral Betti numbers. Eliminating the \(y\)-critical equation produces a polynomial of generic degree \(r_m+1\); an explicit discriminant-nonvanishing specialization proves generic simplicity.

Run `python verify.py` with standard-library Python; it checks the polynomial identities, squarefreeness and forbidden-root arithmetic for each \(0\le m\le12\). Finite tests do not prove any statement for all \(m\). No independent audit or independent validation was performed.
