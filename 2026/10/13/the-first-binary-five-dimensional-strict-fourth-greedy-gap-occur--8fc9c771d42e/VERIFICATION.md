---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Represent every nondegenerate binary [n,5] generator by a multiplicity function on the 31 points PG(4,2). For maximum point mass M, maximum line mass L, and maximum point mass B lying on an L-line, subspace duality gives d3=n-L, d4=n-M, g4=n-B. A strict gap B<M forces a multiplicity-M point p off every maximum line. With max-mass line ℓ and its largest point mass b, L<=3b, while the line pq for q∈ℓ attaining b cannot be L and has mass ≥M+b, giving L>=M+b+1; b<=M-1 implies M>=3, b>=2, L>=6. Rank 5 requires ≥2 additional support points outside span(ℓ,p), hence n>=M+L+2>=11. Witness columns 3e1,2e2,2e3,2(e2+e3),e4,e5 have rank5; independent enumeration of all 155 PG(4,2) lines establishes M=3,L=6,B=2 with one maximally massive line, so d4=8 and g4=9. Inspecting subspaces confirms claimed full generalized hierarchy in package. The universal lower bound is symbolic, not inferred from finite enumerations.

## originality

PASS

Bose–Wei complete 21-page primary paper online September 2026 gives projective formulas and upper bounds on g4-d4 for prescribed (n,d1,d2,d3) and constructions; it does not state a universal smallest binary dimension-five length with strict g4>d4 or this eleven-column witness. Its p.3 Eq.(3) accidentally exchanges alpha and beta but p.2 defines d4 and g4 correctly; the proof here uses correct point/line correspondence directly. Johnsen–Verdure develops matroid greedy weights, not the special sharp cutoff. Thus the natural first-occurrence theorem is neither a mere relabeling nor a directly covered corollary of published maximal-gap bounds.

## value

PASS

The smallest block length admitting divergence of generalized and greedy weight is a natural coding-theoretic threshold; sharp n=11 with a complete rank-independent obstruction for all n≤10 informs structural limits of greedy support chains, regardless of a larger downstream theorem. The witness has d1=1, which is explicitly disclosed, and no higher-min-distance optimality is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
