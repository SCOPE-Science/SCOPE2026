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

With \(\operatorname{col}(X)=v^\perp\), the full-model residual is exactly \(Zv\), while the null observed coefficient is \(U=q^\top\varepsilon\); Gaussian orthogonality makes \(U,Z\) independent standard normals. For a uniform observation permutation, \(q^\top Pv\) has values \(-\sqrt{2/n},0,\sqrt{2/n}\) with the stated masses, so conditional rejection reduces exactly to binomial tail counts in four angular wedges. Including the observed statistic in the source empirical distribution gives the stated order index \(k\). The Gaussian wedge probabilities, law-of-large-numbers limit for fixed \(\alpha<1/4\), and final \(n\)-limit follow directly. An independent recomputation reproduced the reported \(n=20,m=1000,\alpha=0.05\) size to machine precision.

## originality

PASS

Toulis Equation (17) was inspected in the full PDF and matches the audited full-model residual randomization construction; Theorem 4 gives asymptotic validity under exchangeability when \(p/n=o(1)\), not an exact saturated counterexample. Wen--Wang--Wang later address proportional dimension with a different projected RPT and prove validity only for \(p<n/2\). Neither inspected source states the rank-one three-point law, finite-\(m\) exact size formula, or the \(1/2\) saturation limit. Resultary search returned no covering exact residual-permutation record.

## value

PASS

The theorem gives an explicit Gaussian boundary family where a widely motivated residual-permutation construction has severe size inflation despite ideal iid errors, with an exact finite-randomization formula and limiting size approaching one half. That sharply delineates the low-dimensional validity theory and is a substantive failure mechanism rather than a numerical anomaly.

The dated certificate retains the supplied scientific assessment, sources and limitations.
