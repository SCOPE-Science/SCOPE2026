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
The verification artifact uses exact rational arithmetic and the Python standard library.

For normalized \(2\times2\) Stieltjes matrices it reconstructs forward SOR directly from the sequential update equations. On multiple rational pairs \((\rho,\omega)\), it verifies that the response to the two coordinate basis right-hand sides equals the closed first- and second-iterate matrices in RESULT.md.

It verifies the exact witness
\[
\rho=\frac15,\qquad \omega=\frac53,\qquad g=(1,1/10)^{\mathsf T},
\]
obtaining
\[
y^{(1)}=(5/3,13/18)^{\mathsf T},
\qquad
y^{(2)}=(43/54,-4/81)^{\mathsf T},
\]
and
\[
\widehat A^{-1}g=(17/16,5/16)^{\mathsf T}.
\]

The infinite phase diagram is not inferred from the finite test set. Its proof is the exact quadratic sign analysis of
\[
3-2\omega+\omega^2\rho^2
\]
given in RESULT.md.
