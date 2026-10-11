---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

Every dual cross-Gramian is precisely an idempotent projection onto \(W=\operatorname{ran}F^*=z^\perp\), hence has the unique form \(G=I-qz^*\) with \(z^*q=1\). Its off-diagonal objective is \(\max_i b_i|q_i|\). The inequality \(1=|z^*q|\le\sum_i|z_i||q_i|\le\mu\sum_i a_i/b_i\) gives the stated lower bound. Equality forces every \(b_i|q_i|\) to equal \(\mu_*\) and all \(\overline z_iq_i\) to have common nonnegative phase, yielding the unique optimizer. The canonical projection is \(I-zz^*/\|z\|^2\), so equality with the optimizer is equivalent to constant \(a_i b_i\). The exact-rational verifier independently confirms the displayed counterexample, both dual identities and coherences \(2/5<3/7\).

## originality

PASS

Aceska--Kaczanowski explicitly conjecture that an exclusive Grassmannian dual must be canonical. The audited excess-one reduction produces a complete fixed-frame minimizer and a concrete strict counterexample to that conjecture. The earlier Welch-type dual-pair result assumes constant diagonal pairings and therefore does not optimize over the unrestricted dual set here; the finite-dual-pair characterization likewise does not solve this off-diagonal minimax problem. Targeted Resultary search found no earlier excess-one formula or noncanonical exclusive counterexample.

## value

PASS

The result gives a complete sharp solution in the first redundant frame regime and supplies a concrete counterexample to a published structural conjecture. The optimizer formula also identifies exactly when the canonical dual survives, making the result reusable rather than an isolated example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
