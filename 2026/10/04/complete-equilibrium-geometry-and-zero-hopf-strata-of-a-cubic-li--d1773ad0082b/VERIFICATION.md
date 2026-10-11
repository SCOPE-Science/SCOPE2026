---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

The equilibrium equations split exhaustively into \(x=0\) and \(x\ne0\). The first gives the three real roots of \(F(y)=0\) with free \(z\); the second forces \(z=0\), \(x=-a_6y/a_7\), and a quadratic with negative constant term, hence exactly two nonzero real roots. Independent symbolic reconstruction gives \(\det(\lambda I-J)=\lambda(\lambda^2+a_5zF'(r))\) on every line. Since \(F'(0)<0\) and \(F'(r_\pm)>0\), the stated zero-Hopf and saddle-normal half-lines follow exactly.

## originality

PASS

The introducing paper studies the same equations but prints an equilibrium-line discriminant incompatible with its own positive-parameter example and gives a zero-Hopf proposition that is not the linewise sign classification obtained from the actual Jacobian. No checked source supplies the corrected three-line/two-point census together with the exact zero-Hopf strata.

## value

PASS

The result repairs the complete equilibrium geometry and identifies the exact zero-Hopf submanifolds of a published chaotic oscillator. That is a motivated correction because the source uses the equilibrium geometry for stability and bifurcation discussion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
