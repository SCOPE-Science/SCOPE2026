---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

For tent Q2=(1-|x|)_+ and ab=3/4 with b in [11/4,13/4], rational Zibulski–Zeevi p x q =3x4 fiber at x=t=0 evaluates exactly to [[c0,c,c,c],[c,c,c,c],[c,c,c,c]], c=2-3/b, c0=1 when b<=3 and 3-6/b otherwise. All eight lower-row arguments modulo 3 belong to [1/4,11/4] and only two nearest integer-period translates survive, endpoints included; c0-c=|b-3|/b. Rank is exactly 2 except b=3 rank1. Since Q2 is continuous in M1 and fiber continuous, rank defect at point excludes positive lower frame bound. Exact rational checks at five selected b corroborate, but distance argument establishes continuum.

## originality

PASS

Theorem 7 of Lemvig–Nielsen arXiv:1507.03982 gives only [23/8,25/8] at ab=3/4; their Theorem 8 uses ab=5/6. Ghosh–Selvan arXiv:2310.01141 provides fiber matrix and a different family of exclusions; Lemvig arXiv:2601.07642 requires q>=6. The present full [11/4,13/4] interval is not implied by inspected theorem hypotheses. An earlier thesis may contain the identical row-equality trick; priority remains qualified.

## value

PASS

Exact frame-set boundaries for compactly supported B-splines are motivated problems. The explicit second-order rational-density row-deficiency mechanism expands a general nonframe slit from width 1/4 to width 1/2; this is meaningful and not a numerical sample. No global optimal interval claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
