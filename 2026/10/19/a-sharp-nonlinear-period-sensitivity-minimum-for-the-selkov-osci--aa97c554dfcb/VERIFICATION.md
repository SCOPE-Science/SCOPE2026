---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

An independent scalar harmonic calculation uses u=x+y/alpha−1−1/alpha and u'=1−y. Order-two harmonics and order-three solvability give a stable nondegenerate branch on alpha>alpha_H. If e is the u harmonic amplitude and q=gamma−1, then alpha−alpha_H=(gamma/(8q))e²+o(e²) and r²=gamma e²+o(e²). The order-three cosine forcing after subtracting the actual linear frequency gives C=(2q+1+2/q)/48. The square identity proves positivity and the unique minimum 5/48 at gamma=2. A differentiated tensor replay also reproduces the complex cubic coefficient; neither argument relies on finite-offset integration.

## originality

PASS

The same-system Hopf type is established in the literature, and an earlier fixed-determinant Selkov calculation algebraically recovers the gamma=2 coefficients at its boundary after an exact scale change. The frozen exposition overstates the separation from the polynomial variant at that exponent. Neither source computes the off-Hopf frequency correction on the real-exponent family or determines its sharp minimum over the family. The pass is for that full-exponent result, with the special case credited.

## value

PASS

A radial Hopf computation does not tell whether nonlinear oscillations run slower than the equilibrium's linear oscillatory mode at the same parameter. The substrate harmonic and physical time make this comparison operational. An exact positive correction over all real exponents and a unique minimizing exponent distinguish the nonlinear dynamical effect from the linear frequency drift, not just from another amplitude convention.

The dated certificate retains the supplied scientific assessment, sources and limitations.
