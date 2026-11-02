---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For every D,E>=1 over F_2, Frobenius gives T^(2^r)-I multiplication by u^a+v^a+u^av^a on F_2[u,v]/(u^D,v^E), a=2^(r+1). Splitting by exponents mod a produces truncated chain pairs. The automorphism Y->(1+X)Y sends X+Y to X+Y+XY, and the quotient by X+Y has length min(d_i,e_j). Summing chain survival indicators gives exactly K_r and #Fix=2^K_r. Distinct monomials show exact operator order 2^R, and nested fixed-point counts yield least periods, cycle counts and zeta. For dyadic windows with max>=4, K_(R-1)=DE/2 proves full-period proportion 1-2^(-DE/2). Reviewed actual RESULT.md and artifacts/verify_corner.py at pinned tree; independent constructed bitwise operator and 405 exact rank checks, including K(5,7)=(10,19,35). One-sided D=1 or E=1 handled by vanishing truncated shifts. No assumption that short finite checks establish the universal formula.

## originality

PASS

Originality is the full all-rectangle distribution of binary moving-corner periods and cycles, not the underlying unipotent tensor-block nullity or moving-corner factorization. Direct comparison with closest square-window source finds an exact operator order, not fixed-state counts. Literature/index overlap remains possible for equivalent dynamical formulations.

## value

PASS

The moving-corner local rule defines a natural finite-state dynamical system studied for Frobenius revivals. The theorem resolves the entire period spectrum, all exact multiplicities, dynamical zeta and a sharp generic-period probability for every rectangle; these are nontrivial seed-level invariants not implied by operator order alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
