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

The embedded `verification/verify.py` uses SymPy exact rational arithmetic. It reconstructs the mean and variance of the two possible ambiguous media payoffs at \(y=0\), differentiates the payoff-consistent two-strategy replicator with respect to \(\lambda\), and checks
\[
\partial_{\lambda}\dot z_{\mathrm{util}}
=x(1-x)z(1-z)^3(F_m-F'_m)^2.
\]
For the source's fine rates \(F_m=7/2\) and \(F'_m=4/5\), at \(x=z=1/2\), it obtains the exact rational \(729/6400\). The separate \(\lambda\) coefficient printed in Equation (18) gives \(729/3200\) on the same face.

The final media drift of Equation (21) reduces on this face to
\[
F_z=z[-C_m-R_m+(1-z)(xF_m+(1-x)F'_m)],
\]
which has identically zero \(\lambda\) derivative. Equations (19)–(24) and updates (42)–(44) were also manually checked for absence of \(\lambda\).

The observed absence of a parameter from a complete published vector field is the mathematical proof of nonidentifiability for its well-posed solution law; symbolic tests independently check the nonzero risk effects of the original payoff game. No finite simulation is used to certify an infinite-time property. The interpretation or validity of unpublished numerical code is unproved.
