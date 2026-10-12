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

For even \(k\ge4\) and \(m=k/2+1\), division of the two positive source equations gives
\[
\frac{z_1}{(1+z_1)^2}=\frac{z_2}{(1+z_2)^2},
\]
so a non-symmetric solution must satisfy \(z_1z_2=1\). Substitution gives
\[
\lambda=\frac{(z^2+1)^k}{z^{k/2}(z+1)^k}.
\]
With \(u=z+z^{-1}\), this is exactly
\[
\lambda^{2/k}=\frac{u^2}{u+2}.
\]
The right side has derivative \(u(u+4)/(u+2)^2>0\) for \(u\ge2\), proving the global threshold and uniqueness of the non-symmetric branch pair.

The bundled `verify.py` checks the source equations exactly over rational reciprocal pairs for several even orders and checks the radical reconstruction numerically for representative activities. These finite checks are corroborative only; they are not used to infer the all-order theorem.

The 2025 same-object Bulletin article was not available in full text, so equivalence with that later source remains an explicit originality risk.
