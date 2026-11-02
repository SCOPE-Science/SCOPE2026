---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For finite k-committees with candidate qualities h_c in [q,1], reciprocal affordability sum_{c in X}1/h_c<=k implies t=|X|<=k and B=h(X)>=max(qt,t²/k) by the floor and Cauchy–Schwarz. After factoring common optimal and affordable members, quality-greedy completion of X has ratio >=1-z+max(qz,z²), z=t/k. Direct piecewise minimization gives inf 3/4 for q<=1/2 and 1-q+q² for q>=1/2. In matching party-list instances with n=rk<k voters, n-1 private voters force quality-r singleton candidates by reciprocal JR while a remaining voter supports k quality-one public candidates; optimum constrained retention tends to 1-r+r². Rational r approximates irrational q, and q=1 is equality. The proof imports from Boehmer et al. the nontrivial axiom-satisfying greedy completion existence for reciprocal EJR, threshold-PJR+ and value-EJR, which was not independently re-proved; the analytical envelope and rational witnesses were independently checked across a rational grid. This conditional reliance is stated, not disguised as a self-contained proof.

## originality

PASS

The originating Boehmer–Dong–Kreisel–Utke paper gives the unconstrained sharp 3/4 price and affordable greedy completion constructions for reciprocal axioms, and its welfare appendix has a different objective. The additional quality-floor parameter q changes the worst-case domain and yields strictly improved sharp 1−q+q² for q>1/2, beyond the unconditional theorem. The full primary text could not be fetched this run; a detailed independent reviewer synopsis of its Theorem 5.5 and Appendix G was materially read; prior Resultary floor-frontier search found no exact statement. Priority remains qualified.

## value

PASS

The formula is an exact conditional price of proportional representation under a natural exogenous quality floor, revealing a genuine plateau-to-curved frontier at q=1/2. Exact finite-instance infimum and matching extremal families quantify an important fairness/quality tradeoff across four axioms; the improvement for q>1/2 is not a textbook restatement of the known global 3/4.

The dated certificate retains the supplied scientific assessment, sources and limitations.
