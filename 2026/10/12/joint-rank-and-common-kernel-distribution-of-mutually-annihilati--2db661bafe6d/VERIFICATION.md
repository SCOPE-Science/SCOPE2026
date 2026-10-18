---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For each common kernel K of dimension k, X and Y factor uniquely through V/K to K. Four zero-product relations hold, and exact joint kernel K is equivalent to injectivity of (f,g):V/K→K⊕K. Rank-r map counts are Gaussian coefficients times |GL_r(q)|. Subspace Möbius inversion gives the displayed joint (r,s,k) sum. Summing ranks yields [n choose k]_q∏_(i=0)^(n-k-1)(q^(2k)-q^i), nonzero iff k≥ceil(n/3); polynomial leading degree 3floor(n²/4) and parity-dependent coefficient follow by maximizing 3k(n−k). Independently enumerated actual square-zero matrices and rank/kernel strata at (n,q)=(2,2),(2,3),(3,2): total ordered pairs 10,33,148 with 4,4,5 strata respectively. Proof establishes all finite fields; tests do not.

## originality

PASS

The geometric classification of two-loop radical-square-zero representations and the general total count of annihilating matrices are prior. Neither inspected primary treatment specifies the joint finite-field (rank X,rank Y,dim common kernel) point counts; total sums and component/orbit data do not invert to these multiplicities. Resultary semantic search returned related rank/representation results but no mathematical implication supplying the full refinement. Best-of-knowledge PASS with historical representation-count risk.

## value

PASS

The complete labeled finite-field rank/socle spectrum is a natural structural enumerative invariant of the radical-square-zero two-loop algebra, significantly finer than known component or total pair counts. A representation or probability researcher can directly use these exact strata and support thresholds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
