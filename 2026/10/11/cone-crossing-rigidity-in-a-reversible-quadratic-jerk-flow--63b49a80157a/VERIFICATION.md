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

The standalone `verify.py` checks the unrestricted-parameter Lie derivative of \(P=z+xy\), the polynomial derivative of \(Q\), and the two cone-branch substitutions \(y=\varepsilon sx\), \(z=\varepsilon x/s\), \(a=s^2-1\) for \(\varepsilon\in\{-1,1\}\). Both branches give \(\dot z=-2x^2\) from the system but \(\dot z=x/s^2\) from tangency. The only possible constant nonzero \(x\) violates \(\dot x=z\); the unique cone-bound complete orbit is the origin.

To reproduce, run `python3 verify.py` with SymPy installed. The script prints `PASS` only after every asserted exact expression evaluates to zero. The analytical convergence and invariant-measure arguments appear in RESULT.md, and are not replaced by the finite symbolic check. No independent external validation or audit has been performed.
