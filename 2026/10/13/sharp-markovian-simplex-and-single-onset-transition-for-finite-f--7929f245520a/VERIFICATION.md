---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Scope is the q+1 F_q-linear lines in F_q², not every maximal isotropic additive subgroup in composite prime-power dimension. Each line is its own field symplectic perpendicular; for a Weyl label off the line the symplectic pairing runs through F_q, so the nontrivial trace character averages to zero. This yields the stated T_j eigenspaces and positive finite-time λ_j=x_j+(1−x_j)y with y=e^(−ct), including zero weights. Independently invert the generator in T_j−Id: its coefficient b_j must satisfy Σ_i b_i−b_j=g_j=−(d/dt)log λ_j on sector j. Summing gives Σ_i b_i=Σ_i g_i/q, and T_j−Id is the sum of the q−1 nonidentity Weyl conjugation differences divided by q. Hence γ_j=(Σ_i g_i−qg_j)/q². Nonnegative Weyl coefficients yield a GKLS generator; a negative one has a negative first-order Choi expectation along its orthogonal nonidentity Bell vector for a short propagator. Finite-time invertibility makes this propagator the unique intermediate map. In the simplex interior a least rate always corresponds to m=max_j a_j. Its exact expression is cyF(y)/[q²(1+my)], where F is the displayed root function. (Dividing by cyφ_y(m)/q² gives F/m, not F itself; the proof only uses the sign.) F(0)=A−qm and F(1)=q; F is nondecreasing, with strictly positive derivative unless all a_j=m. Thus A≥qm is necessary and sufficient, and A<qm gives exactly one crossing in (0,1) and local CP-indivisibility at every later time, with inclusive endpoint on the initial interval. At equality A=qm the leading term is c(qm²−Σ_j a_j²)y²/q², positive because all a_j>0 and not all equal. On a proper face with 2≤s≤q active weights, each active g_j<c(1−x_j) for t>0 and each absent g_j=c, so γ_k<0 in every absent direction; a vertex is the original semigroup. Substitution of qutrit weights (1/10,3/10,3/10,3/10) gives exactly y*=11/21. Inspected, did not run, the frozen finite numerical diagnostic. Its reported 182400 counts nonidentity-label units over the main test cases; the actual rate assertions there are made for one representative per direction, not 182400 distinct rate-to-formula comparisons. The continuous proof and all prime powers do not depend on that reporting convention.

## originality

PASS

The evaluated interior simplex condition together with the exact global single-onset structure is the supported distinction. Existing generalized-Pauli formulas already give the same mixture and pointwise rate sign test, even in the complete-MUB prime-power setting, and substantial proper-face behavior was known; neither derivation of the instantaneous rates nor mere extension using prime powers is the new result. The inspected sources do not evaluate the general all-time sign problem into the stated weight-only condition and monotone crossing classification.

## value

PASS

For a natural equal-rate mixture of mutually unbiased pinchings, a weight-only rule is useful in place of testing every time instance. The evaluated classification establishes a sharp distinction between immediate, delayed and absent loss of CP-divisibility, including a permanent-onset theorem and the critical tail behavior. The contribution is not the existing pointwise generator formula or a one-weight example; scope remains fixed weights, a common decay rate and the complete field-line family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
