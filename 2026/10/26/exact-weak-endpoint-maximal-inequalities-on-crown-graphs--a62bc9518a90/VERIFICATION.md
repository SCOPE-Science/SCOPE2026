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

Reconstructed ball sizes 1,n,2n-1,2n and the four explicit means at each A_i,B_i; for threshold <=T/(2n-1), cardinality suffices. For higher thresholds, classify self-covered vs radius-one-only. Mixed-side centers force X,Y>(n-1)t and the n=3,k=6 matched-pair argument gives contradiction. The RESULT.md mass-moving assertion for arbitrary destinations is not justified as written; a direct inequality closes the same one-sided case without transport: each B_i in H obeys X-x_i+y_i>=nt, hence T>=nt+x_i+(Y-y_i). For k<=2n-2 this gives the target; for k=2n-1 either a self-covered B contributes >=t in Y-y_i, or an intersection U∩H supplies x_i>=t, giving T>=(n+1)t; for k=2n and b>=1 both contributions give T>=(n+2)t; when k=2n,b=0 summing all H gives (n-1)X+Y>=n²t, implying T>=n²t/(n-1). Restored K_(n,n) proper ball sizes 1,n+1,2n yield 2n/(n+1). Independent BFS balls and exact weak-ratio enumeration checked 1584 rational integer-mass vectors on n=3,4, plus uniform extremizers. This independently supplies a valid proof of the unchanged theorem, while the original exposition should be corrected before publication.

## originality

PASS

Qualified PASS: Soria–Tradacete (arXiv:1410.6204) defines the centered graph maximal operator and proves general weak-type bounds (Section 4, Theorem 4.9) but not the sharp all-n crown constant; González-Riquelme–Madrid arXiv:2005.03146 and 2011.02630 concern variation, strong p norms and complete/star graphs, not the crown weak endpoint. Crown n=3 is C6 but no inspected result gives the entire n-family. Broader graph-ball overlap theory may still yield an unrecognized corollary.

## value

PASS

Weak (1,1) amplification for graph balls is a natural endpoint stability invariant. The exact all-order crown constant, its extremizer and strictly quantified difference from the intact balanced biclique determine how deleting a perfect matching changes this nonlinear operator, beyond a trivial graph-cardinality upper bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
