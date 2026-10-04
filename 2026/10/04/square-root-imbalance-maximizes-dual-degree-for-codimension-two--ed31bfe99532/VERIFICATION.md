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

The proof was reconstructed from the conormal-bundle formula for projective-dual degree. For \(X_{d,e}\subset\mathbb P^5\), the only source-dependent input is
\[
\deg X^\vee=\int_X\frac1{c(N^*(1))},
\]
together with the fact that a nonlinear smooth complete intersection has dual hypersurface. Both were checked in the cited full texts.

With \(x=d-1\), \(y=e-1\), the coefficient extraction was replayed directly:
\[
[H^3]\frac1{(1-xH)(1-yH)}=x^3+x^2y+xy^2+y^3,
\]
and \(\int_XH^3=de\). Substituting \(q=x+y\) and \(s=y-x\) gives the factored formula and then the completed-square identity used for optimization.

The tie analysis was checked symbolically: adjacent parity-lattice values \(s,s+2\) tie exactly when \(2q=s(s+2)\), hence \(s=2k\) and \(q=2k(k+1)\); both candidates are admissible precisely for \(k\ge2\). The asymptotic uses only that the fixed-parity lattice has mesh two near \(\sqrt{2(q+1)}\).

The standalone program `artifacts/verify_dual_degree_mode.py` was executed from its packaged path and returned:

`VERIFY_OK q=2..2000 admissible_pairs=1000000 first_tie_q=12`

It checks every admissible pair in that range, formula equality, exact maximizers, the tie classification, and stated small examples. The program is a regression check and does not certify cases beyond its finite range; the infinite statement rests on the algebraic proof.
