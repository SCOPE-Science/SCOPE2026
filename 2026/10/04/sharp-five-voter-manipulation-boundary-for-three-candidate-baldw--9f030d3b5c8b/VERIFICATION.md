---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The normalized witness is directly verified: truthful first-round Borda scores are \((6,4,5)\), so \(B\) is eliminated and \(C\) beats \(A\); after one \(ABC\) voter reports \(BCA\), the scores become \((4,5,6)\), so \(A\) is eliminated and \(B\) beats \(C\). The frozen verifier contains two independent Baldwin winner implementations, exhaustive anonymous enumeration for every electorate size \(1\) through \(5\), and a separate labeled replay over all \(6^5\) profiles and every distinguished voter/report. A fresh independent anonymous replay reproduced zero bad profiles through four voters, exactly six at five voters, one relabeling class and labeled weight \(180\); inspection of the labeled route verifies the factor two giving \(360\) vulnerable distinguished voter-profile pairs.

## originality

PASS

Narodytska, Walsh and Xia prove broad one-manipulator hardness for unweighted Baldwin but do not give a three-candidate minimum electorate or exact prevalence. Heilmaier's full thesis already contains the same truthful \(2,1,2\) five-voter profile as a minimal Black-versus-Baldwin difference and computes Baldwin winner \(C\), so that profile itself is prior; however, the thesis does not state the unilateral \(ABC\to BCA\) manipulation, the four-voter impossibility, the unique strategic normal form or the exact incidence counts. Resultary exact searches returned no matching strategic census.

## value

PASS

Baldwin manipulation is a standard computational-social-choice problem, and the exact first tie-independent electorate where a single voter can profit gives a natural finite strategyproofness boundary. The complete orbit, prevalence and unique normalized report make this a structural classification rather than an isolated example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
