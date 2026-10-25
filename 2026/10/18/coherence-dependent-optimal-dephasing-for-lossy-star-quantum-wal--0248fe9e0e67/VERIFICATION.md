---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

For m>=2, J,kappa>0, gamma>0, and any leaf-supported density matrix rho, the site-projector Lindblad dephasing term damps each off-diagonal entry at rate gamma. Hilbert–Schmidt dissipation excludes imaginary-axis eigenvectors: they would be diagonal with zero hub entry; the hub-leaf commutator forces zero. Hence all integrals converge. Writing x=rho00,p=sum leaf diagonals,B=sum leaf entries,eta=Im(sum hub-leaf entries), the four closed linear equations integrate to tau=(m+1)/kappa+kappa/(4J²)+gamma/(2J²)+(m-s)/gamma, s=B(0)=m<b|rho|b> in [0,m]. Completing a square uniquely minimizes at gamma*=J sqrt[2(m-s)] if s<m; if s=m, positive-gamma infimum is not attained and exact gamma=0 bright mean 2/kappa+kappa/(4mJ²), strictly smaller than lim positive gamma; a dark component at gamma=0 gives infinite unconditional mean. Independently checked exact formula against full matrix Liouvillian resolvent in six cases, including coherent inputs; finite checks do not replace analytic integrability and boundary proof.

## originality

PASS

Best-of-knowledge statement-and-implication comparison; not a priority certificate. A full paper and targeted Resultary search were inspected as described below.

## value

PASS

For a natural star transport architecture, dephasing optimization depends on a single physically measurable bright-state overlap and is independent of trap strength. The singular discontinuity for exactly bright preparation distinguishes the zero-noise and long-time limits. This is a motivated full-state exact mean-trapping invariant and optimizer, not a numerical convenience.

The dated certificate retains the supplied scientific assessment, sources and limitations.
