---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

The Lindblad normalization makes hub-leaf coherence decay at s=(kappa+gamma_L+gamma_H)/2. Averaging the localized leaf by permutation covariance preserves the trace survival function. Integrating a’=-kappa a-2mJv, b’=2Jv, d’=2Jv-gamma_L d, v’=-J(b+(m-1)d-a)-sv with a(0)=d(0)=v(0)=0, b(0)=1/m yields A=1/kappa, V=-1/(2mJ), D=-1/(m gamma_L), B=1/kappa+(m-1)/(m gamma_L)+s/(2mJ^2), hence the formula. Positive leaf noise destroys every trace-preserving invariant leaf block: positivity with hub population zero forces R 1=0 and the dephased off-diagonal decay then forces the diagonal to zero. This establishes exponential absorption in finite dimension and legitimizes integration. Separate strict AM-GM inequalities give the unique joint optimum; the dark subspace perpendicular to the uniform leaf vector has initial squared weight 1-1/m when gamma_L=0, proving the discontinuity. Independent full unsymmetrized Liouvillian resolvent checks: 12 m/rate cases, error <=6.3e-15. No finite calculation is used as an infinite proof.

## originality

PASS

Best-of-knowledge comparison after fresh Resultary searches, focused primary-source proof inspection and explicit implication checks. A related method, family or parameter alone does not establish identity/coverage; historical risk remains noted.

## value

PASS

The physically natural competition between noise unlocking a dark subspace and excessive noise slowing transport is resolved by an exact all-size, all-positive-rate absorption law. The sharp global three-rate optimum and singular zero-noise boundary provide independent structural facts useful for transport design; these are not simple renamed rate constants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
