---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For exponential age T the complex conditional Gaussian moment is (2n-1)!! (4Delta)^n exp(2in theta0) I_T^n. Ordered times in I_T^n and Brownian independent increments yield n!/product_{j=1}^n(r+4gamma j^2); the independent stationary generator recursion (r+4gamma k^2)F_{n,k}=4n(2n-1)Delta F_{n-1,k+1} confirms this without using a log. m2=4Delta exp(2i theta0)/(r+4gamma), m4=96Delta^2 exp(4i theta0)/((r+4gamma)(r+16gamma)); Q decreases 6 to 3/2, giving the inverse gamma/r=(6-Q)/(16Q-24), S=4barD/r and strict A/S<(4Q-6)/(3Q). Boundary gamma=0 is included, infinite gamma excluded; isotropy and common-rate scaling are true degeneracies. Independent rational diagnostic compared the generator product for eight even orders.

## originality

PASS

Qualified PASS: Chaki–Olsen–Löwen 2024 supplies this very reset model and renewal/second-order equations, but no inspected fourth complex-moment ratio inversion or feasible region; generic Fourier propagators may encode ingredients implicitly rather than assert the claimed identifiability theorem.

## value

PASS

Exact population-moment identifiability and the complete attainable set in the exact motivating stochastic model are natural inverse-problem invariants; the sharp second-order obstruction explains why fourth-order measurements are necessary. Not an estimator or a discovery of renewal theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
