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

For fixed n>=3, scattered three-decks recover shorter counts by combinatorial extension, including S0=c_01. For r marked ones and m=n-r zeros the eight triple counts are explicit polynomials in S0=sum z_i, S1=sum i*z_i, S2=sum z_i^2; these are both necessary and sufficient deck invariants. r<=2 yields unique zero-prefix vector; at r=3 the two linear equations leave a direction (1,-2,1), and positive quadratic norm meets this line at most twice. The explicit 7-letter pair gives equality and padding preserves it. At r=4, use x_j+y_j sqrt(-5)=(1+sqrt(-5))^j(1-sqrt(-5))^(k-j), norm 6^k and v=((x-y),(3y-x),(-x-3y),(x+y))/2. Exact integer parity, sum v=sum i*v_i=0, norm squared=6^k and B=4*6^k yield strictly increasing z_i=iB+v_i in 0..5B. The quotient of conjugate algebraic numbers has rational trace -4/3 and cannot be a root of unity; the k+1 words are distinct and deck-identical at length 20*6^k+4, with padding extending to every n>=124 and the exact floor-log bound. Independently enumerated 1,578 short words/decks and checked algebraic witnesses k=1..5; finite checks do not prove unboundedness.

## originality

PASS

The 2021 Chrisnata et al. full paper specifically counts distinct k-deck observations D_k(n), and its Section 5.3 concerns three ones, explicitly giving the two 7-letter ambiguous words. Rigo--Salimov and Lejeune--Rigo--Rosenfeld develop binomial equivalence and total number of equivalence classes, primarily two-binomial finite-word classification; neither the number of distinct observations nor a bounded weight-three fiber can imply unbounded single-deck fibers at weight four. Fresh Resultary nearest hits concern three-deletion reconstructions and alternative multispectra, not fixed-weight four-one scattered length-3 deck fibers. Norm-form infinite witness is new relative to inspected implications; unindexed older sparse-word class-size research remains risk.

## value

PASS

Fixed-deck reconstruction is a natural combinatorial inverse problem. The sharp transition from at most two reconstructions with <=3 ones to unbounded multiplicities with precisely four ones, plus an explicit arithmetic construction and bound for all sufficiently long lengths, establishes a meaningful structural threshold beyond a single counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
