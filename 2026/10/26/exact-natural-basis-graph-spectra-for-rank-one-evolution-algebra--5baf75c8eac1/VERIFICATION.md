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

The zero-annihilator hypothesis makes B nondegenerate. Over F_(2^e) the square map is bijective, so each natural frame normalizes uniquely for the chosen generator; all normalized frames form a torsor for O(B), and reordering acts freely. The normalized dot product satisfies B(x,x)=B(x,t)^2, so every isometry fixes t. In odd dimension t splits off an alternating complement: the orbit is ct plus either {0} or all nonzero complement vectors. In even dimension with B(s,t)=1, s=e1, the span of s,t is nondegenerate and its alternating complement H gives all isometries by a symplectic map S on H and arbitrary z in H and a in the field. The coefficient B(z,Sx) in g(x) is forced by orthogonality to g(s) and imposes no other constraint; the images preserve all pairings. This gives G_d and the three even-dimensional orbit cases, including the fixed line and the impossibility of a moving zero-sum vector in d=2. The nonzero-coordinate sum recursion gives A_k. Deleting ct or the fixed line from the relevant hyperplane gives exactly the displayed corrections, with the zero vector irrelevant to positive weights. Orbit–stabilizer and free reordering give G_d H_k/(d! T). Equal pairs and a nonzero triple show positivity at the claimed supports, and the full-support constructions avoid the deleted scalar points. A generator change multiplies the normalized coordinates by a common nonzero square root and preserves all cases. Replay: python /workspace/checks/3-4.py directly counts unordered projective-line cliques in F4^4 and gives (10,30,70,50), (0,48,64,48), and (0,0,0,160). Frozen verify.py and supporting notes were inspected, not executed. Counts concern basis classes of a fixed algebra for q≥4, not binary parity or algebra isomorphism classes.

## originality

PASS

The supported distinct result is the coupled extension-field classification of graph support and exact quotient-frame multiplicities in all dimensions, not the separate orthogonal and symplectic group facts. The inspected earlier binary result is a close conceptual antecedent with a different support law, and the indexed all-field dimension-two formula is slice-level overlap only.

## value

PASS

Enumeration modulo scaling and reordering is a natural question about natural bases, and graph support is intrinsic to the variability across those bases. The result gives all attainable graph types and exact counts rather than just the group order, explains why the fixed characteristic line is exceptional, and quantifies the disappearance of binary parity restrictions in extension fields. This is a complete classification for a defined algebra family, not a claim to solve the general survey questions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
