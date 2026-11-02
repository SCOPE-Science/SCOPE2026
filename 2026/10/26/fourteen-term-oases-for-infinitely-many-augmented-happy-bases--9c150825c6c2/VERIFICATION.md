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

A three-digit fixed point is exactly a nonnegative defect D_b(x,y,z). Twelve offsets 0..13 excluding 5,8 are represented by singleton formula s²+z(z−1); special leading-digit 12 constructions represent offsets 5 and 8 exactly when the quadratic Q(u,t)=0. The Pell norm identity U²−29V²−10940=−232Q and norm-one unit (192119201,35675640) preserve the quadratic constraint; parity and positivity yield infinitely many increasing bases. Independently re-enumerated the entire 3-digit defect/mirage spectrum for all even bases 2..28, matching maxima and [8686,8699], and independently algebraically checked recurrence/norm and explicit witness sets at multiple Pell indices. The first-base upper bound uses the published JIS Theorem 10 mirage bound; odd bases L=1 and even <=20 use JIS results; the infinite family follows from algebra, not finite tests.

## originality

PASS

Baker Swart et al. 2019 introduce oasis/mirage, prove upper bounds by finite mirage and tabulate even bases through 20; these tools are prior. The arithmetic novelty assessed is first b=28 with exact L=14 and especially an explicit infinite Pell-generated family of distinct bases. The paper’s infinite translated oases within a fixed base are not the same as infinitely many bases.

## value

PASS

Oasis maximum length L(b), its first attainment base, and existence along infinitely many distinct bases are canonical quantities of augmented-happy digit dynamics. The explicit Pell family gives a nontrivial uniform construction beyond a one-off finite scan, while exact b28 resolves the natural first fourteen-term threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
