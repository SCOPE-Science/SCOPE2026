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

# Analytical and computational verification

The exact moment sequence of the claimed two-initial-weight unilateral shift is \(\gamma_0=1\), \(\gamma_1=c/2+d\), and \(\gamma_r=c/(r+1)\) for \(r\ge2\). The proof reconstructs both nonautomatic shifted Hankel matrices and evaluates the relevant inverse Gram entries directly. A positive-real two-by-two Schur complement determines the second condition without extrapolating from finite sections. At each order \(n\ge1\), the two nonautomatic Agler defects are exact alternating binomial sums; all later defects are positive Beta integrals. The subnormal locus has the explicitly specified representing probability measure.

To replay the finite checks, run `python weighted_shift_checker.py` with Python 3 and SymPy. The checker reconstructs exact rational Hilbert and shifted Hilbert inverses for matrix sizes two through eight, evaluates principal minors independently of the closed inequalities at representative rational parameters, checks Agler sums for orders one through nine, and confirms the published special case with the first squared weight fixed at one half and second-order hyponormality. It also tests asymptotic coefficients at increasing finite orders. The completed run returned `PASS: 315 exact or finite consistency assertions`.

The finite checker does not prove universal positivity, infinite-dimensional equivalence, priority, or the asymptotics by enumeration. Those claims rest on the derivations in RESULT.md. Possible equivalent earlier formulae and nonuniformity in parameters approaching the critical mass remain limitations. There is no external or independent scientific audit.
