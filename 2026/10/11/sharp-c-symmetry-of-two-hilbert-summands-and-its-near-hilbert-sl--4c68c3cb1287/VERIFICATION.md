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
The theorem was verified analytically using the unique Hilbert-sum support functional and exact optimization of the block mass:
\[
\omega_*=(1+\tau)^{-1}.
\]
The one-sided derivatives of the two smooth branches of the envelope have strictly positive and strictly negative signs, respectively, for every \(1<p<\infty\). The constructed unit pair has opposite-sign collinear blocks and exact forward functional value zero; its reverse functional has the claimed equality value. Boundary configurations with a vanishing block have reverse residual zero.

The global near-Hilbert coefficient is justified by a uniform estimate (not by checking finitely many exponents): for \(7/4\le p\le9/4\), putting \(\delta=|p-2|\),
\[
0\le D_p(e^{2z})/\delta\le2z e^{-9z/14}\qquad(z\ge0).
\]
The limiting scalar profile \(z/\cosh z\) has its unique maximizer at the solution of \(z\tanh z=1\).

The bundled `verify.py` uses the standard Python library to check the hyperbolic conversion, conjugate-exponent identity, positivity of branch derivative numerators, sharp explicitly constructed pairs in Hilbert blocks of several dimensions, noncollinear Birkhoff pairs and the near-Hilbert coefficient. It must be run as `python verify.py` from its actual extracted path. Finitely many floating-point tests are not a continuum or infinite-dimensional proof.

No independent audit or independent validation has been performed.
