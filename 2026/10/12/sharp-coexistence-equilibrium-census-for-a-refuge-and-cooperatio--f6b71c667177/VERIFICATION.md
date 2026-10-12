---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Mathematical verification

The exact fixed-point equations reduce to \(R q(y)=1\) with \(R=\beta b\) and positive prey coordinate \(x(y)=1+r^{-1}\log(1-bs(y))\). The proof differentiates \(G(s)=s[r+\log(1-bs)]\) three times and \(Q(y)=s''(y)/[s'(y)]^2\) once. Each sign is strict on the stated domain, and the endpoint argument forces a single maximum or strict decrease. This establishes the infinite-domain equilibrium-count result analytically.

`verify.py` reproduces the derivative identities with exact symbolic simplification and independently computes the illustrative example's peak and the two root locations at high precision. Its numerical roots are corroboration for that example, **not** a proof that all parameter sets have at most two equilibria.

The source's stated case \(r=1\), \(b=0.49\), \(c=3\), \(\beta=2\) lies strictly inside the two-equilibrium window. Its approximate coexistence equilibria are \((0.9947339,0.0104492)\) and \((0.6968123,0.3644879)\).

No finite parameter enumeration, dynamical stability test, or independent audit is claimed. See `RESULT.md` for the quantifiers, curvature sign argument and limitations.
