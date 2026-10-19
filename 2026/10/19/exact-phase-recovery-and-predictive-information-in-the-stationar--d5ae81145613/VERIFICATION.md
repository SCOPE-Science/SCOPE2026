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

# Reproducibility of the finite-word information law

The proof uses exact phase-conditioned uniform word counts, including the two-word compatibility intersection, and the Shannon entropy chain rule. This supplies an all-length proof independently of finite computation.

Execute `python3 verify.py` in the extracted directory. It enumerates all binary sign words of lengths 1 through 12 and computes conditional phase likelihoods as reduced rational numbers. It checks full normalization, support cardinalities, optimal Bayesian risks, alternating-word masses, and double-precision evaluations of the exact entropy identities. No third-party packages are required.

Observed output: `VERIFY_OK: 606 positive exact phase-conditioned cylinders; 12 exact support, Bayes-risk and alternating-mass identities; 12 Shannon entropy comparisons`.

Computational limitation: these are finite checks only; they do not establish unrestricted formulas, historical novelty, or independent audit. Those mathematical claims are established by the counting argument in RESULT.md and the source comparison in REVIEW.md.
