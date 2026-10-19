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

# Reproducible exact checks

Run `python verify_quorum.py` using Python 3.9+ standard library. The program verifies the realized-group payoff subtraction against the model's algebraic gain formula, the Bernstein-to-power polynomial expansion, the four alternating rational signs, three separate isolating intervals, and the inequalities for transverse and homogeneous-vertex eigenvalues. It makes no numerical root count assumption. The source equations are [1, Eqs. (2), (7)–(10), (14)–(17)] as cited in RESULT.md.

The analytic proof in RESULT.md covers every integer group size \(N\ge3\) and every admissible quorum \(2\le M\le N-1\); finite code does not certify this universal quantification. Exact stability claims are local, not global. The closest earlier mathematical principle—the Bernstein polynomial sign-variation bound—is expressly attributed to Peña, Lehmann, and Nöldeke. Independent external validation has not been performed.
