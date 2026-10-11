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

The conditional identities follow by applying invariance to arbitrary smooth antiderivatives of \(x\) and \(z\): \(L\Phi(x)=a\Phi'(x)(y-x)\) and \(L\Psi(z)=\Psi'(z)(hx^2-cz)\). An independent symbolic calculation verified that for \(F=-hxy+(h/2)x^2+bz-(k/2)z^2\), \(LF=kc z^2-bc z-ah(y-x)^2\), giving the exact completed-square identity. Equality forces \(y=x\) and \(z\in\{0,b/k\}\) almost surely; invariance then restricts support to \((0,0,0)\) and \((\pm\sqrt{bc/(hk)},\pm\sqrt{bc/(hk)},b/k)\). The strict excursion and sign-change consequences follow because a non-equilibrium invariant measure makes the nonnegative defect term positive while the invariant mean of \(y-x\) is zero.

## originality

PASS

The full primary Liu-system treatment inspected here gives the exact equations, equilibria, classical parameters, frozen-z threshold \(b/k\), and Hopf analysis but no invariant-measure conditional expectations, stationary square identity, or equality classification. Targeted searches for Liu stationary moments/invariant measures found dynamical/bifurcation papers but no equivalent law.

## value

PASS

The theorem gives exact global stationary constraints, a sharp equilibrium-height defect, and a rigidity/equilibrium classification for an established chaotic model. These are structurally motivated observables and turn a local threshold \(b/k\) into a necessary excursion law for every non-equilibrium compact invariant measure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
