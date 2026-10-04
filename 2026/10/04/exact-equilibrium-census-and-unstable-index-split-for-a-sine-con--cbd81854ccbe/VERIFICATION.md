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

The proof uses exact rational arithmetic for the printed coefficient matrix and standard one-variable convexity. The reduced equilibrium equation is \(t+B\sin t=0\) with \(B=231898/2735\). Rational bounds on \(\pi\) establish \(26\pi<B<27\pi\); each relevant negative-sine lobe is strictly convex and has a negative midpoint value, giving exactly two roots.

For the stability classification, the Jacobian depends on an equilibrium only through \(q=(1551/100)\cos t\). Exact determinant expansion yields the cubic in `RESULT.md`, and the Routh first column has the two finite thresholds stated there. The root equation plus \(|t|<26\pi\) implies \(|\cos t|>1/4\), which places every nonzero equilibrium strictly away from both Routh thresholds.

`verify_equilibria.py` checks the rational matrix identities, all threshold inequalities, and a numerical bisection sanity check that finds exactly two roots in each of the 13 positive lobes. The floating-point bisection is supplementary; the root count and hyperbolicity are proved analytically.

No independent audit has been performed.
