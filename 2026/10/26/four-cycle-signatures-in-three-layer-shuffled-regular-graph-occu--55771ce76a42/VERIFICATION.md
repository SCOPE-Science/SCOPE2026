---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

After the first two outgoing edges, the subsequent globally uniform shuffle places two unit piles at a uniform unordered pair S of distinct vertices; no unjustified independent-ball approximation is made. Empty indicator at target v is 1[S cap N(v)=empty], giving E Z2=d*C(d-2,2)/H=mu. For a,b, k_ab=|N(a) cap N(b)| and P(both empty)=C(d-4+k_ab,2)/H. The global codegree sum over a<b is d, while k_ab=2 exactly at the two opposite pairs per C4 component, so E C(Z2,2)=(H*C(d-4,2)+d(d-4)+2q)/H. This gives variance. A fresh independent global permutation sends the two input neighbors of any target to a uniform pair, so E[Z3/d]=E C(Z2,2)/H. Simple-cycle partitions classify extremal q and first q-variation at d=7. Direct exact enumeration of all cycle partitions d=7..14 and uniform pairs corroborated 156 formulas; unrestricted conclusion follows from the codegree counting.

## originality

PASS

Qualified PASS: Chiclana's 2026 paper uses precisely the same path/pile permutations and proves asymptotic empirical Poisson universality and universal quadratic contraction identities, but the inspected theorems do not give these nonlinear exact finite-depth vacant-site variance/third-layer formulas. A standard common-neighbor 4-cycle count makes the result accessible; an unindexed finite-layer moment consequence could exist. Originality is for the motif fingerprint and first d=7 discriminating pair, not for random-permutation model or the factorial-moment identity itself.

## value

PASS

PASS: a sharp first graph-geometric signature at finite depth in an otherwise geometry-independent asymptotic occupancy model is a motivated structural counterpoint. The 4-cycle motif coefficient and all cycle-partition extremizers yield a complete natural subclass classification, including the smallest witness size d=7. Its small asymptotic magnitude is disclosed but does not remove mathematical interest.

The dated certificate retains the supplied scientific assessment, sources and limitations.
