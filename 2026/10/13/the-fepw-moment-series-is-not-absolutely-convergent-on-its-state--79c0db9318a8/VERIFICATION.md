---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

From the source-given survival S(x)=e exp(-exp((tau*x)^eta)) exp(-(kappa*x)^phi), the nonnegative-variable moment formula r∫x^(r-1)S(x)dx is finite for every positive integer r by exp[-(kappa*x)^phi] domination. Substitution in the published Eq.(3.2) coefficient yields at all-one parameters a_(i,j)=e(-1)^i i^j/i! and hence exactly a_(1,j)=-e for every j. This fixed-row term test refutes convergence, a fortiori absolute double convergence, without any truncation. Substitution z=exp((tau*x)^p) yields r e/(p tau^r)∫_1^∞ (log z)^(r/p-1)z^(-c-1)e^(-z)dz with c=(kappa/tau)^p. At r=p this is e tau^(-p)Gamma(-c,1); mpmath quadrature independently equals e Gamma(-1,1)≈0.4036526376768059 at the all-one point and verifies a second shape slice. This does not imply the distribution lacks moments or all related series are invalid.

## originality

PASS

The 2026 publisher primary identifies the FEPW model and Theorem 1 Eq.(3.2); indexed full-text excerpts from its published remarks claim absolute convergence of infinite representations across admissible parameters, and searches for DOI and corrigendum found no published correction. The exact interior-row obstruction with a corrected equal-shape representation is not a general Weibull fact or a title match. Full publisher text could not be retrieved from arXiv/OA and protected Oxford returned vpn_disconnected; novelty is assessed best-of-knowledge with this genuine primary-source access risk, not automatically failed.

## value

PASS

The claimed divergent expression purports to compute fundamental raw moments and is used to justify truncation; an interior exact counterexample changes the rigor of statistical inference and numerics. This is an impactful, motivated type of negative correction, not an arbitrary boundary check. The convergent equal-shape formula is useful replacement for a natural model slice; the paper-wide scope is expressly limited.

The dated certificate retains the supplied scientific assessment, sources and limitations.
