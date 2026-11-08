---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For n>=3 triangular cylinder C3 square Cn, every vertex has 4 distinct neighbors; strict best response active exactly for 0 or 2 active neighbors. Ordered pairs of three-bit columns (p,c) define 64 transfer states with (p,c)->(c,q) allowed exactly when all 3 row constraints are met. Closed walks biject to labeled equilibrium profiles; E_n=tr(M^n), no rotation quotient. Independent SymPy exact 64x64 charpoly equals z^25(z-1)^10(z+1)^5(z²+z+1)^4(z³-z²-1)(z³-z²+1)(z^5+z³-z²+z-1)^2. Dominant SCC has 18 states, contains 3- and 8-cycles, hence primitive; its unique PF eigenvalue is positive root λ≈1.465571231876768 of z³-z²-1. All other recurrent blocks have roots of unity, so E_n~λ^n; per-player entropy log(λ)/3. Direct brute equilibrium counts agree n=3..5; exact trace list n=3..12 21,9,3,45,3,33,75,39,69,153.

## originality

PASS

Gilboa/Nisan and Klimm/Stahlberg establish existence/decision complexity of picky zero-or-two-neighbor best-response patterns on arbitrary graphs and describe active components, NOT the full 64-state spectral enumeration for labeled C3 square Cn. A finite-state transfer is standard, but its computed factored characteristic, exact counts and entropy in this natural first 4-regular strip are not direct corollaries of those complexity theorems. Unlocated tabulations of periodic Boolean network configurations are a residual risk.

## value

PASS

The choice C3 square Cn is mathematically structural: at degree <=3, the zero-or-two rule equals parity of neighboring actives and equilibria become linear over F2; at degree 4, neighbor count 4 breaks that linearity. The full exact strip entropy and spectral factorization provide a nontrivial benchmark beyond the parity-solvable degree cutoff, not an arbitrary size slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
