---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

The energy difference on flipping site i is 2J sigma_i(sigma_{i-1}+sigma_{i+1}-kappa(sigma_{i-2}+sigma_{i+2})). This five-spin condition gives an exact 16-state quadruple de Bruijn transfer-matrix trace for all n>=5; only threshold kappa=1 can change allowed transitions. Independently constructed all 3 integer 16x16 matrices and used exact SymPy determinants to reproduce source characteristic factorization in each phase. Brute full spin enumeration for each n=5..9 matched trace(T^n) in all 15 cases. Verified exact Collatz–Wielandt component inequalities for both 14-state Perron vectors: the critical lambda lies in (1.665,1.668) and high lambda in (1.554,1.557), separated from phi in (1.618,1.619). The source checks strongly connected primitive components; Perron–Frobenius then yields the exponential limit, not just finite trace data. At kappa=1 neutral flips satisfy >=0, and the statement does not equate weak minima with dynamically absorbing states.

## originality

PASS

Earlier Redner–Krapivsky and Sen–Dasgupta papers analyze dynamical coarsening/persistence in ANNNI chains; Dhar–Shastry–Dasgupta study equilibrium degeneracy at distinct kappa=1/2. The exact all-weakly-one-spin-blocked configuration characteristic polynomials and the marginal-vs-strong entropy comparison were not identified in read source portions. The golden-ratio weak branch is explicitly credited as pre-existing, as are physical transition locations.

## value

PASS

Exact entropy of all non-strict local-energy minima is a motivated, distinct combinatorial invariant of the competing-interaction chain. The sharp marginal spike and three algebraic rates classify how neutral-energy motifs affect the entire locally stable configuration space, rather than just typical Glauber trajectories or equilibrium ground states.

The dated certificate retains the supplied scientific assessment, sources and limitations.
