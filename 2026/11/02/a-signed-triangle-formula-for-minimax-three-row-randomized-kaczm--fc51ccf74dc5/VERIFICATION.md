---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For invertible real unit-row A, maximizing lambda_min(A^T diag(p) A) is exactly minimizing T=sum w_i subject to diag(w)-C PSD with C=(AA^T)^-1 and p_i=w_i/T. On separating diagonal entries, minimization of sum q_i is dual to elliptope maximization 2sum c_ij X_ij. Balanced sign product yields weighted graph Laplacian primal with rank-one sign-vector dual; frustrated strict triangle uses a rank-one primal vv^T and rank-two correlation Gram of unit vectors whose weighted sum vanishes; frustrated weak reciprocal edge uses a signed Laplacian with PSD Schur complement. Matching certificates prove global optimality; dual complementary nullspaces fix all q_i and guarantee uniqueness, including equality boundary. Inverse Gram gives positive weights; explicit G(t) substitution yields kink at t=2/5 and minimum eigenspace dimension 1 before, 2 after. Independently checked five rational G(t) values using exact PSD principal minors/eigenvalues and branch weights. Finite SDP experiments are only corroboration.

## originality

PASS

Dai–Soltanalian–Pelckmans established general row-probability SDP; Saunderson et al established minimum-trace diagonal PSD and elliptope framework, not new here. The specific inverse-Gram sign/reciprocal-triangle formula, uniqueness and 2/5 phase transition are not stated in these inspected primary sources. General elliptope/optimal-design literature could implicitly specialize to the formula; priority remains qualified.

## value

PASS

A complete closed-form minimax sampling law for all real invertible three-row normalized systems, with unique optimizer, distinct frustration geometry and a natural multiplicity-changing nonsmooth Gram family; more informative than a generic numerical three-variable SDP. This is a natural complete small-dimensional classification, not a one-point example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
