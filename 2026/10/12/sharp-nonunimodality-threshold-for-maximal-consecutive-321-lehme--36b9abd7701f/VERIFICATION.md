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

The published block encoding of maximal consecutive-321 avoiding Lehmer codes has endpoint lengths {1,2} and interior lengths {2,3}; defect contributions are C(b,2). Setting e endpoint excess 0,1,2, u=#interior2, v=#interior3 gives n=2+e+2u+3v, d=e+u+3v. Hence u=n-2-d, e congruent 2d-n+2 mod 3, v=(2d-n+2-e)/3; nonnegative solutions have coefficient C(2,e)C(u+v,v), proving generating function (x+qx²)²/(1-qx²-q³x³). For n=2r+1, r>=5, consecutive coefficient triple (r-1,r-2,(r-2)(r-3)) has a strict valley. For n=2r, r>=7, triple (C(r-2,2),C(r-3,2),2C(r-3,3)) has a strict valley. Remaining n=2..10 and 12 are directly checked via exact formula, so unimodality iff 2<=n<=10 or n=12. Independently generated all binomial-formula coefficients for n=2..15 and checked each profile; inspected full source RESULT.md and its cited structural proof. Finite checks corroborate while valley families prove infinite n.

## originality

PASS

Beveridge–Hu–Liu (arXiv:2609.33137) already proves the block encoding, Padovan total count and maximum inversion weight. These are explicitly treated as prior. The new mathematical finding is all-length coefficient-sequence unimodality classification, including a nonmonotone revival at n=12; source did not state such threshold in inspected original text.

## value

PASS

Unimodality of an inversion-rank polynomial is a natural finer invariant of a pattern-avoidance poset than its size or extremal weight. A complete sharp all-length threshold, proved by two infinite strict-valley families and one small exception, is an independently useful structural classification rather than a routine table lookup.

The dated certificate retains the supplied scientific assessment, sources and limitations.
