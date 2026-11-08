---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For the signed Schur multiplier M_(n,k) with negative first k diagonal entries, an explicit nonnegative vector u gives trace-norm lower bound ||diag(u) M diag(u)||_1, and positive semidefinite P±M with diagonal T gives factorization upper bound T. The fully flipped k-core has eigenvalues (k−2)/k once and −2/k repeated k−1. With one additional unflipped coordinate, explicit maximizer a_k and 2x2 Gram block determinants yield T=1+k/(1+sqrt(2k)) for 1<=k<=5, versus 3−4/k for k>=6. Replication of the unflipped Gram vectors proves no dependence on further n. Checked n=k=1 and k=0 separately; independently recomputed eigenvalue/witness and PSD certificates for k=1..30, including transition at six. Infinite proof is symbolic positive semidefiniteness, not those finite checks.

## originality

PASS

Mathias circulant formula covers the n=k fully flipped symbol, and general Schur factorization/SDP methods are classical. Holbrook–Johnston–Schoch publish several small corresponding numerical Schur values. The asserted new contribution is an all-size evaluation, one-coordinate effect and exact k=6 stabilization; no inspected broader theorem states that specialization explicitly.

## value

PASS

Analytically solves a natural one-parameter symmetry reduction of a nontrivial operator multiplier-norm problem and identifies a sharp qualitative cutoff where one unflipped coordinate ceases to increase the norm, with constructive lower contractions and PSD upper witnesses.

The dated certificate retains the supplied scientific assessment, sources and limitations.
