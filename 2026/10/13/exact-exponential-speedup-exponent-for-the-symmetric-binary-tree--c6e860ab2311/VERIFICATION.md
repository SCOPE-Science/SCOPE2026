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

The proof uses the exact generating functions in arXiv:1107.4201. The critical algebraic reductions are:

\[
q=\frac u3(1+q-2q^2),\qquad
u(q)=\frac{3q}{(1-q)(1+2q)},
\]

\[
(-2|q|^2+4\operatorname{Re}q+1)(2|q|^2+2\operatorname{Re}q-1)=0
\quad (|u|=1),
\]

and, at the maximizing branch point on the unit circle,

\[
q_*=\frac{\sqrt3-1}{2},\quad
\rho^2=\frac{2+\sqrt3}{6},\quad
\alpha_*=\sqrt3-\frac32.
\]

The standalone `verify.py` re-evaluates these constants, checks the classical first-passage mean, and performs an independent dense numerical replay of the unit-circle modulus. It prints `VERIFY_OK`.

The numerical scan is not used as proof of the sharp bound. The proof is the exact factorization of the unit-circle modulus condition plus the standard nondegenerate one-dimensional saddle calculation. The theorem establishes the exponential rate and the limiting linear optimizer location, not the full polynomial prefactor.
