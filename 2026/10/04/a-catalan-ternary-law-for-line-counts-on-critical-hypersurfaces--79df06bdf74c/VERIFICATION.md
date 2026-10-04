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
The verification is symbolic.

For \(n=3m\), the defining product has a factor whose two coefficients are divisible by three, so the target coefficient vanishes modulo three.

For \(n=3m+1\), the factor residues occur \(2m\) times each and their product is
\[
x^{2m}y^{2m}(x+y)^{2m}.
\]
For \(n=3m+2\), the residue multiplicities are \((2m+1,2m+1,2m)\) and the product is
\[
x^{2m+1}y^{2m+1}(x+y)^{2m}.
\]
After multiplication by \(x-y\), both target coefficients are
\[
\binom{2m}{m}-\binom{2m}{m+1}=C_m.
\]

The ternary rule is exactly the known Catalan residue theorem of Deutsch--Sagan. The density count is obtained by counting allowed ternary strings and is independent of any finite computation.

The classical initial line counts \(1,27,2875,698005,305093061\) provide a low-index consistency check only.
