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
# Verification scope

The analytic proof establishes the infinite family. The executable checker performs independent exact finite corroboration but does not certify the infinite argument.

Run `python3 CHECK.py` with SymPy installed. Expected completed assertions: symbolic determinant equals Vandermonde times \(h_2\); every one of sixteen signed evaluations is in \(\{2,4,10\}\); exhaustive exact-cyclotomic four-column tests for \(N=6,10,14,18,22\), with checked subset counts \(15,210,1001,3060,7315\). These tests give zero singular subsets except ten at \(N=10\).

The proof's required noncomputational premises are: a Schur quotient with integer coefficients; factorization \(N=2p^k\) into sign and \(p^k\)-root parts; minimal-polynomial divisibility of \(Q\) by \(\Phi_{p^k}\); identity \(\Phi_{p^k}(1)=p\); signed evaluation formula; and the explicit order-five counterexample. These are described in RESULT.md.

Limits: no assertion of unconditional novelty priority, no numerical conditioning estimate, and no independent audit or external certification.
