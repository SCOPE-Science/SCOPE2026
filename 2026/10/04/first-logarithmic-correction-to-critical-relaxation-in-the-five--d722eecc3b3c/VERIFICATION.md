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

At r=1 the linearization has one zero eigenvalue and four strictly negative eigenvalues, so the local one-dimensional center manifold is legitimate. Independent symbolic solution of the invariance equations reproduced all submitted coefficients A,B,C,D,F,G,H exactly, including q=sigma B. For W=xi^{-2}, the reduced equation gives W'=2c-2q/W+O(W^{-2}); using W=2ct+O(log t) and integrating the corrected derivative yields W=2ct-(q/c)log t+C+o(1). The standard-parameter rational specialization is consistent with the formulas. The full Zhang--Deng paper confirms that its first-transition reduction stops at beta_1 x_1+H x_1^3+o(x_1^3), while its later fifth-order calculations concern the distinct second/Hopf transition.

## originality

PASS

The complete Zhang--Deng article was inspected. At the first transition it derives only the cubic center-manifold equation (3.18) and global stability at r=1; it gives no quintic first-transition coefficient and no critical time-decay expansion. Its fifth-order normal-form work later in the paper belongs to the separate Hopf transition near the nonzero equilibrium. The audited result computes the missing quintic coefficient in the physical x-amplitude and converts it to the first logarithmic relaxation correction, where the higher-mode damping d enters for the first time. Targeted Resultary and literature searches did not locate an equivalent same-model formula.

## value

PASS

At a critical nonhyperbolic equilibrium, the first correction beyond the leading algebraic decay is a natural quantitative invariant of relaxation. Here it reveals a structural feature invisible at cubic order: the added-mode damping d enters the dynamics first through the logarithmic term. The calculation therefore sharpens a published first-transition normal form in a mathematically motivated way rather than adding an arbitrary higher-order coefficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
