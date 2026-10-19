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

# Reproduction and proof dependencies

The standalone standard-library Python file `verify.py` was run as `python3 verify.py` against the actual files packaged with this finding. Its observed terminal result was `VERIFY_OK 37958`. The program needs only Python 3 with `math`, `random`, and `fractions` from the standard library.

The script tests exact rational identities for the maximizing derivative of \(g_c(s)=\sin s+c\sin^3s\), including \(c=1\), \(u_c=2/3\), \(q(c)=16/9\), and the exact three-edge-star critical-step Jacobian \(I-K_*/4\) with spectrum \((0,3/4,3/4)\). It also tests the scalar global derivative bound and sign on 801 phases per parameter across eight coefficients, numerical potential-derivative consistency, the quartic contact at \(c=1/6\), and thousands of sampled finite-step potential-descent and invariant-slab inequalities for two diagonally dominant matrices.

These finite checks do not establish that every stable/unstable intersection is transverse, do not exhaust all torus configurations and dimensions, and do not prove priority. Universal assertions rely on the explicit analytic chain in RESULT.md: derivative maximization; symmetric-Jacobian local invertibility; strict Lyapunov descent; the signed-diagonal-dominance invariant slab; the two-sided adjoint maximum contradiction; and the exact semidefinite equality characterization of the first singular Jacobians. No external proof assistant, independent validation, or external audit has been performed.
