---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The analytic argument conditions on the edges of an arbitrary specified non-induced copy and sums the resulting binomial degree probabilities. The complete finite-size parameter range, including the zero and maximum degree boundary classes, is covered algebraically. The strict monotonicity of the normalized factor establishes the unique sign roots and their ordering. Locally uniform falling-factorial expansions and a nonzero derivative at the limiting root establish the sparse-scale second-order term.

The included standalone verifier `verify_degree_motif.py` was executed under Python 3 with no third-party dependencies and reported `PASS: 3299 exact-enumeration and threshold-order checks`. It enumerates every labeled graph through six vertices for eight applicable named motifs and verifies exact rational covariances at three rational probabilities. It also checks the numerical root ordering through ambient order 29. Finite checks are auxiliary evidence, not an infinite proof.

The sparse-scale expression and root correction were also compared independently using numerical root solving for a triangle, a three-vertex path, and a four-vertex star. This checks examples but does not certify historical priority. The external independent audit has not been performed.
