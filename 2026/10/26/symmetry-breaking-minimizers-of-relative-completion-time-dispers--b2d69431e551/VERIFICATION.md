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

Independently derived the PGF from the three first-step equations: set b=1−a, q=1−p, w=ab, c=2p−1, and let s mark steps. The PGF from 00 is U(s)/D(s), where U=wq²s²(2−s) and D=(1−sp)[1−s+(pq+c²w)s²]−s²pq[1−2w−s(p−(2p+c)w)]. Derivation: from 10 the PGF is s(ap F00+bq)/(1−s(1−ap−bq)); swap a,b for 01 and substitute into the 00 equation. Each transient state has a uniformly positive probability (for the fixed parameters) of absorption in at most two steps, so the PGF is analytic near 1. Differentiating gives E[T]=(log F00)'(1) and Var(T)=(log F00)''(1)+(log F00)'(1); independent symbolic simplification confirms both moments, the derivative at RESULT.md:40–43, and the variance difference at 50–55. The affine bracket in the derivative starts at 1−p²>0 and ends at (6p²−19p+11)/4 at w=1/4. It is positive throughout the interior for p≤p_star, including at equality in p, and crosses exactly once inside the interval for p>p_star. The sign of the derivative therefore identifies the unique optimal w, and the two weights above threshold are precisely the two preimages of that w. The endpoint w→0 is not a missing minimizer; the mean and variance strictly favor w=1/4. Static inspection of clumsy_two_type_checker.py:15–31 and the recorded output shows 361 parameter pairs, two moment equalities and one positivity assertion per pair; that script does not test optimization. No archived code was needed for the independent PGF check.

## originality

PASS

The supported distinct contribution is the exact global optimizer and loss threshold for the squared CV, not the first-passage law, moment method or mean balancing. The earlier October 18 Resultary theorem covers the whole distribution for nonuniform weights and the exact mean optimizer. Its m=2 PGF determines both moment inputs of this record; passing originality does not credit those inputs. The sharp normalized-dispersion reversal requires a new global comparison of the ratio of moments over weights, not a specialization of that earlier balancing theorem. No compared statement supplies this optimization or an order theorem implying it.

## value

PASS

The sharp boundary answers a natural design question in the smallest model where a relative criterion can disagree with absolute completion-time dispersion. It predicts exactly when and by how much type probabilities must be unbalanced to minimize relative uncertainty, despite strict balancing of both absolute moments. That is materially different from recomputing moments from a known transform.

The dated certificate retains the supplied scientific assessment, sources and limitations.
