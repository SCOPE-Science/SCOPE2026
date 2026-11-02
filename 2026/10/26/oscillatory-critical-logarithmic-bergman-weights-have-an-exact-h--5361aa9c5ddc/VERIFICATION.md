---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Reconstructed input monomial moments v_n=int_0^1 t^n w(t)dt and orthonormal-coordinate operator K_{mn}=1/[(m+n+1)sqrt((m+1)v_n)]. Laplace substitution gives v_n=(log n)^2 a(loglog n)^2/n (1+O(1/log n)), using bounded positive a and bounded derivative; tail effects integrated against e^-y. The low triangular m>n and upper m<=n error squared sums between K and P_d, P_{mn}=1_(n>=m)/(sqrt(mn) log n), d_n=1/a(loglog n), are finite since sum 1/(n log²n)<infty. A Schur weight h_n=(n log n)^(-1/2) gives essential norm <=2 for P; weakly null loglog coordinate windows produce lower norm approaching 2. For P_d upper <=2 limsup d and lower use a_prime->0 to keep d nearly constant over each fixed additive u-window, then send window width to infinity. The example has liminf a=3/4 and derivative tending to zero, giving 8/3. Independent approximate finite-window Copson integral singular values for lengths 4,8,16,32 approached 2 with expected coarse-grid bias; not cited as proof of infinite essential norm.

## originality

PASS

Norrbo 2026 establishes critical logarithmic boundedness, while a published same-weight coefficient-space Copson model gives exact unmodulated essential norm 2, and a separate published one-space generalized ℓp Hilbert matrix theorem gives limsup under slow oscillation. These substantially motivate the claimed formula but are different operators/weight placements. Exact nonconvergent multiplier at a double-log scale in two-weight analytic Bergman mapping is not supplied by the inspected theorems; possible limit-operator/Hardy general result dominating the formula remains a concrete risk.

## value

PASS

The critical logarithmic Bergman mapping is a natural operator-theoretic endpoint; the exact essential norm for every admissible *nonconvergent* double-log slow multiplier describes persistent noncompactness and distinguishes liminf envelope from an average. It is an infinite-family exact essential invariant, not a known-table recomputation or a numerical perturbation; existing coefficient model supplies a starting lemma but does not state the oscillatory formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
