---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For the directed finite ring, each feasible predecessor feeding site i has stationary weight ratio a_i/a_(i-1), so after multiplying by the predecessor jump rate its incoming flux divided by the proposed weight is a_i, exactly the total-outflow contribution indexed by a nonempty site i. Irreducibility gives uniqueness. Summing ordinary-site occupations at fixed slow vector k gives binom(L+N-|k|-1,N-|k|); the proposed negative-binomial identity follows after multiplying by the common factor q^N(1-q)^L. The geometric summands have span one, mean rho_c and variance v, so the lattice local CLT gives the uniform compact approximation, including the boundary k_j=0; the floor changes the scaled displacement by O(L^-1/2). For a uniform tail proof use the mode m=floor(t) with t=q(L-1)/(1-q). Below it, mass(b-1)/mass(b)=b/[q(L+b-1)] decreases when stepping down, and 1-ratio is at least c(t-b)/L for 1<=b<=m. Multiply the ratios using log x<=-(1-x), sum the linear deficits, and use the local-CLT supremum O(L^-1/2) at the mode and globally. Since t differs from rho_c L by O(1), this yields the stated one-sided Gaussian envelope. Counting r-tuples with total s and multiplying the envelope by the weak tilt and any fixed polynomial gives an integrable polynomial times a Gaussian in s/sqrt(L). Compact Riemann sums with this tail control give the positive finite normalizer, weak limit and polynomial moment convergence. The s/share Jacobian is s^(r-1), so zero shift and tilt give the normalized chi_r and independent uniform Dirichlet shares; for r=2 integration over the second site's mass gives the stated h_theta and conditional law for either tilt sign and continuously at zero. The frozen checker was inspected, not executed: its scaling samples use round rather than the theorem's floor (a bounded displacement), and its balance and finite comparisons are corroboration, not the limit proof.

## originality

PASS

The supported distinct result is the joint canonical critical-window law for an arbitrary fixed finite set of slow sites with separate weak splittings, moment control, and its chi_r/share consequence. Prior canonical product weights, fixed-total two-site sharing and single-defect finite-size analyses are not new here. The closest indexed two-site result is exactly overlapping at r=2 after reparametrization but dated later and does not supply the arbitrary fixed-r family. A plausible 2014 many-defect paper remains an access risk, not verified coverage.

## value

PASS

A fixed degeneracy changes the critical bulk deficit law from a truncated Gaussian into a chi family, with an independent share vector only in the symmetric case described. The full finite-dimensional weak-splitting window quantifies competition on the scale where the macroscopic background still fluctuates. The moment conclusion and arbitrary fixed number of competing sites make this a useful equilibrium benchmark beyond a two-site computation or a restatement of product stationarity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
