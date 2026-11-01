---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Consistent periodic P1 assembly gives H=4I+S+S^-1, A=(4+6r)I+(1-3r)(S+S^-1), and P=2A^-1 H-I. At r=0 identity, r=1/3 nonnegative, at n>=4 and 0<r<1/3 the signed cyclic inverse yields positive G_02 and P_02=-36rG_02/(1-3r)<0. At r>1/3 inverse is positive Stieltjes, so offdiagonals >0 and diagonal f_n(r) strictly decreases, with unique zero rho_n. Exact positive finite-size Green correction decreases in n and proves rho_n↓(5+sqrt(33))/12; n=3 direct eigenmode formula gives r<=1. Independent full P matrices and Fourier sums in 99 n/r cases, roots for n3..13, corroborate.

## originality

PASS

Best-of-knowledge PASS: the closest general P1 FEM papers provide sufficient bounds or Dirichlet problems; the exact FD Dirichlet Crank--Nicolson results and published filtered lattice / reversible Markov generator positivity laws have different operators or premises. Thus no inspected source directly implies the exact periodic consistent-mass all-n window, monotone upper roots, and limiting radical. A general cyclic-tridiagonal literature specialization is a residual possibility.

## value

PASS

The natural periodic consistent-mass heat discretization has a nontrivial *nonmonotone* allowed timestep set: no small positive step, then a precisely quantified positivity window. Identifies the sharp finite-grid endpoint, its strict mesh monotonicity and limit, improving a conventional sufficient 2/3 limit. This is useful for rigorous numerical maximum-principle design, not a trivial substitution of Dirichlet results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
