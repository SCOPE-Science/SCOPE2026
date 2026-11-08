---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-01.md",
      "INDEPENDENT_AUDIT_2026-11-01.json"
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

PASS: Algebraically |cosh(s)z+sinh(s)|²-|sinh(s)z-cosh(s)|²=|z|²-1+2sinh(2s)Re(z); the two coefficient vectors have determinant -cosh²(s)-sinh²(s)≠0. On the spiral this is 2exp(t)[sinh(t)+kappa cos(alpha t)]. Positive crossings lie in negative-cosine lobes before L=asinh(kappa); each lobe center c_j<L yields two sign-change roots. On later lobes log(sinh(t)/(-cos(beta t))) has second derivative beta²sec²(beta t)-csch²(t)>0, hence ≤2 crossings per lobe. Fixed finitely many early lobes contribute O_beta(1) uniformly in kappa because their ratio has finitely many critical points. The center/lobe count gives N=beta L/pi+O_beta(1), not a mere lower bound. Alternating signs at j*pi/beta produce arbitrarily many distinct adversarial sites for affine non-phase-equivalent pairs. For the full trace distinct exponents j+k+i alpha(j-k) imply equality of all coefficient Gram entries, proving continuous uniqueness. Independent finite sign and root-count diagnostics agree but do not prove the universal quantifiers.

## originality

PASS

Best-of-knowledge originality after comparing exact statements and implications; four structured comparisons and source-inspection limits are included.

## value

PASS

PASS: The quantified divergence between complete-trace uniqueness and finite arbitrary-position identification is a mathematically motivated sampling obstruction for degree-one polynomials. The sharp logarithmic collision law supplies its growth mechanism and exact rate, rather than a trivial finite bad configuration or an unsupported claim about all designed grids. The geometry can guide hypotheses on admissible sample placement and conditioning; no noise stability or optimality of this pair is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
