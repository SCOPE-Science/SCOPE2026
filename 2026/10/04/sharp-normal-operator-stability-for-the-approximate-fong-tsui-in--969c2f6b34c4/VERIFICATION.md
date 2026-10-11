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

For normal T=A+iB, A and B commute and continuous functional calculus reduces the hypothesis exactly to abs(z) <= abs(Re z)+epsilon on the spectrum. With r=abs(z)<=M, the cases r>=epsilon and r<=epsilon give respectively abs(Im z)^2 <= 2 r epsilon-epsilon squared <= 2 M epsilon-epsilon squared and abs(Im z)^2 <= epsilon squared <= 2 M epsilon-epsilon squared. For epsilon>=M, norm(B)<=M. The displayed scalar choices attain both branches, including endpoints. No finite experiment is needed.

## originality

PASS

The current joint primary preprint proves the exact zero-defect Fong–Tsui conjecture. The superseded quantitative preprint publicly states a general one-eighth-Hölder estimate and says its exponent is not claimed optimal; indexed discussion records only that uniform exponents above one half are impossible. No checked source states the full sharp normal-class profile. The complete superseded preprint was inaccessible and the authorized institutional attempt returned an unavailable/invalid-worker error, so this remains an explicit originality risk.

## value

PASS

Quantitative stability is the natural refinement of the resolved Fong–Tsui problem. The normal class is the canonical spectral baseline, and the theorem gives the complete optimal modulus, sharp exponent and equality family rather than merely another zero-defect subclass.

The dated certificate retains the supplied scientific assessment, sources and limitations.
