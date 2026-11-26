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

Under independent fair orientations, the source probability at v is a_v=2^−d_v. Nonneighbors' events depend on disjoint edges; adjacent sources are mutually exclusive. This yields Var(S)=Σ_v(a_v−a_v²)−2Σ_uv a_u a_v, equivalently the squared edge differences plus Σ_v b(d_v). On a path the two leaf edges and degree-two terms give n/16. In a nonpath the leaf arms are edge-disjoint and their count is L=2+Σ_{d≥3}(d−2). A leaf arm contributes at least 1/16+(1/4−2^−d)², strictly more if it has length one. Subtract n/16 and use g(d)≥1/64 and δ(d)≤(d−2)/64, strictly for each d≥3: δ(3)=0<1/64 (the proof's phrase ‘equality at d=3’ is a local wording error; the next step uses the correct strict difference); d=4,5 follow by substitution and d≥6 from b(d)>0. When a degree-three vertex exists the lower bound is 2/64 plus the branching penalties and is at least 3/64, with equality requiring only that one branch and three arms of length ≥2. If no branch has degree three, g(d)≥9/256 and L≥4 give at least (5L+8)/256>3/64. Arms 2,2,n−5 attain the gap for every n≥7 and none can do so at n=4,5,6. Global reversal gives the sinks statement. In independently written finite checks, enumerating connected (n−1)-edge sets and their actual orientations at n=4,…,7 gave second gaps 15/64, 11/64, 7/64, 3/64 and confirmed the equalizer condition on that range; replay python /workspace/branches/math_checks.py 5. The frozen verifier and recorded checks were inspected, not run; the analytical bound proves the infinite claim.

## originality

PASS

The supported distinct result is the all-tree sharp variance gap, with the branching inequality excluding every profile with four or more leaves. The elementary moment formula is not counted as new. The closest exact covariance result supplies the three-leaf slice and the same equality shapes, but not the all-tree variance bound after the degree-profile correction. The comparison is of statements and their proofs, not dates or terminology.

## value

PASS

The marginal source-count variance is a natural fluctuation statistic for independently oriented fixed trees. The all-size positive gap separates the minimum path from all branched shapes, and the proof explains which number of branches and which leaf attachments control the first excess. The remaining all-branch-degree component is useful even after recognizing the three-leaf consequence of the covariance result, because the exact second minimum and complete equality classification cannot be concluded from that slice alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
