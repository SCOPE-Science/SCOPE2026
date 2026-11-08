---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

Companion matrix C sends (a_n,a_(n+1),a_(n+2)) by recurrence, and exact C^28=I+8E with E as displayed. Uniform binomial interpolation F_r(z)=e C^r sum_{j≥0}8^j E^j binom(z,j)v extends all residue subsequences 2-adically. Residues R0,R1,R2 determined uniformly mod8; r14 remains ≡8 mod16; r=20,25,27 each has F_r(−1)=0 and an odd unit bracket, giving 3+nu2(m+1). For r0=0, F_0(z)=32z h(z) with odd linear coefficient 12899489 and Lipschitz remainder contracting by >=8, so h is an exact Z_2 isometry with unique odd root theta. Thus nu2(a_(28m))=5+nu2(m)+nu2(m−theta) for m>=1. Congruence classes count densities p_t and at most 16 progression discrepancies for each level uniformly in X,t. Independent exact SymPy C^28 identity and direct recurrence valuations for n=1..29999 matched the classification using theta ≡698045 mod2^22. Checks are finite, full law follows from the analytic isometry and progression argument.

## originality

PASS

The complete p=2 law, unique exceptional 2-adic root, 28-residue partition, exact density and uniform discrepancy are different from the published p=3 Narayana valuation theorem by Guadalupe. General third-order recurrence valuation frameworks and generalized Fibonacci 2-adic results do not visibly instantiate all these precise formulas. Best-of-knowledge originality retains risk of unindexed older p=2 specialization or hidden corollary.

## value

PASS

Narayana numbers are a standard recurrence with published valuations at prime 3; full prime-2 divisibility is a motivated complementary arithmetic invariant. A complete 28-residue law, unique 2-adic root, every valuation density and uniform |C_t(X)−p_tX|≤16 are useful exact quantitative information about all positive indices, beyond known small tables or routine periodicity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
