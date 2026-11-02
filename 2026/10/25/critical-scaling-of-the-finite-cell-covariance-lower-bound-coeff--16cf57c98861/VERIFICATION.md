---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

FINAL REPAIRED claim: cell Taylor parity gives for each fixed beta>0 S_M=C_E(beta)/M^2+O_beta(M^-4), C_E=(pi beta^2/12) integral Eprime^2 sech^2(beta E); endpoint rescaling under unique zero E(pi-s)=v s^z + O(s^(z+1)), derivative expansion, proves C_E~K_z(beta v)^(1/z). Reconstructed exact counterexample E(k)=pi-k: at fixed M, S_M(beta)->log(2)/(2M) although C_E~pi beta/12. Thus original unconditional necessary M~sqrt(beta) claim is FALSE and removed from full corrected RESULT, REVIEW, AUDIT, METADATA. Independently integrated z=1,2, beta=2, M=10,20,40, matching fixed-beta coefficient; analytic calculation proves limits and counterexample, not these tests.

## originality

PASS

Statement-level search and implication audit, not a novelty proof from a failed search. Fixed-beta covariance expansion is classical midpoint quadrature, not a novel method. Shirai has the particular lower-bound functional and z=1 Ising case but not the general K_z coefficient in inspected text. Source M^-2 observation and order-one critical endpoint do not alone imply a uniform joint-beta/M necessity; repaired result explicitly excludes that false inference; earlier work is explicitly credited. Best-of-knowledge originality survives with the stated residual risk.

## value

PASS

The corrected, fixed-temperature exact coefficient and arbitrary endpoint-order low-temperature exponent are motivated by a concrete finite-cell lower-bound functional; their precise constants distinguish critical dispersion orders. The explicit counterexample protects this result against an invalid uniform-resolution interpretation. No physical complexity or new Hamiltonian is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
