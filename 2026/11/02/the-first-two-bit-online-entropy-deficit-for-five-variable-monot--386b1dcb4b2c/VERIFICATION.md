---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

The concept class J_n is all order ideals of Boolean lattice B_n. Static shattering supports are exactly antichains, so VCdim=binomial(n,floor(n/2)); an unchanging sequence of shattered support points proves Ldim≥VCdim. Exhaustive generation by ideal pairs (A,C) of B_{n−1} with C⊆A yields exact Dedekind counts (3,6,20,168,7581). For Ldim upper bound the exact decision-tree recursion R(F,d) iff some query x admits R(F_x,0,d−1) and R(F_x,1,d−1), with pruning only when |F|<2^d, exhaustively excludes depth width+1 for n≤4. For n5 root ranks 0,1,4,5 have smaller branch <1024; only ranks 2 and 3 remain, whose 2008-concept smaller branches respectively fail depth 10 (independent memoized counts 23644 and 6666 states). Thus Ldim=(1,2,3,6,10), entropy floor(log₂|J_n|)=(1,2,4,7,12), first deficit 2 at n5. I independently ran a complete finite recurrence, not a sampled search.

## originality

PASS

PASS best knowledge: Sperner widths and Dedekind numbers are classical; the exact Littlestone upper bound n=5 is a different adaptive-tree invariant not implied by static VC or counts. No covering complete adaptive calculation found in the inspected learning or published census records; equivalent older online learning table remains possible.

## value

PASS

Boolean monotone-function concepts form the canonical Dedekind-number class. Quantifying the first instance where an adaptive complete query-tree dimension is two below the information-theoretic concept-count bound is a natural benchmark for online learnability; the exact critical branches are not a trivial static antichain count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
