---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-21.md",
      "INDEPENDENT_AUDIT_2026-10-21.json"
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

PASS: The generalized Vandermonde determinant factors as the nonzero Vandermonde product times h₂(z₁,…,z₄)=Σ_{i≤j}z_i z_j. Write a primitive 3p-th root as ωζ with ω primitive third and ζ primitive p-th; collecting pair-sum residues gives coefficients B_b=n_{0,b}+n_{1,b}ω+n_{2,b}ω². Since [Q(ω,ζ):Q(ω)]=p−1, vanishing forces all B_b equal, hence n_{a,b}=v_a+t_b with min(v_a)=0 and 10=p|v|+3T. The only possible cases are p≥11 (impossible divisibility), p=7 (histogram (8,1,1), excluded by the exhaustive fifteen ternary histograms), and p=5 (histogram (10,0,0), forcing all columns into one mod-3 class). For p=5, the four distinct p-residues are four of five fifth roots and h₂=0 by the omitted-root generating identity; the first three Vandermonde rows give rank exactly 3. The saved checker output is an exact finite corroboration (p=5,7,11,13), not the infinite proof; the symbolic proof covers all primes.

## originality

PASS

Best-of-knowledge comparison supports non-coverage by inspected sources; source-specific evidence, implications and residual risks are recorded below. This is not a certification of independent priority.

## value

PASS

PASS: Full spark is a natural erasure-robustness invariant for harmonic frames. The theorem resolves an infinite squarefree-composite family for a concrete four-row pattern, including the exact exceptional order and all 15 rank-three bad minors. It fills a genuine gap between the prime-power theorem and composite counterexamples; it is not a known-table recomputation or a finite census extrapolated to all primes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
