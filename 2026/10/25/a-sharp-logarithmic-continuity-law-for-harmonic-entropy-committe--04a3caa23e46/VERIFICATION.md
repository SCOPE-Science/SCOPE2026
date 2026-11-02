---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

From actual pinned RESULT.md: after zeros are omitted, f_l(x)=max_{1<=t<=s}S_t(x)/(l+t). The active full-support branch equals 1/(l+s) for sufficiently large l and telescopes the infinite defining series. For y=((1-e)x,e), e<=(1-e)min x, the new coordinate is last and f_l(y)=max((1-e)f_l(x),1/(l+s+1)); switching at l=M-s-1, M=floor(1/e), gives F(y)=(1-e)F(x)+e H_{M-1}+1/M with exact boundary ties. Symmetry and concavity of the original harmonic-entropy objective then imply maximum binary increment occurs from the boundary; formula valid to distance 1, and range F in [0,1] saturates for delta>=1. For d fixed, largest-partial-sum total-variation control |f_l(x)-f_l(y)|<=e/(l+1), uniform tail <=(d-1)/(L+1), choice L~(d-1)/e yields upper e log(1/e)+O_d(e). The embedded two-coordinate example attains it. Independent rational checker ran 2808 tests; these finite tests are corroboration, not the analytic argument.

## originality

PASS

Compared direct equivalences, stronger implications, exact tables, and the original papers; no decisive prior coverage identified for the same final statement. Residual priority and access risks separately recorded.

## value

PASS

The exact conditioning of a newly introduced voter payment destination is a natural, potentially practically relevant sensitivity invariant of the specific voter potential. The result gives a sharp leading logarithmic modulus, an all-distance binary extremum and a conditional exact support-opening identity, rather than a renaming of Shannon entropy. It does not assert stability of winning committees or entire election feasibility.

The dated certificate retains the supplied scientific assessment, sources and limitations.
