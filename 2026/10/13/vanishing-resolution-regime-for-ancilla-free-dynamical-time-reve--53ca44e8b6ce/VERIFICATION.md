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

The primary arXiv:2610.01555v1 Appendix C.4 gives explicit good-event ζ_d=o(1) independent of epsilon and base error bounds involving r~d/(ε_n² b), b=floor(log d/(4 loglog d)). With d=2^n, b∼n log 2/(4 log n), so ε_n² n/log n→∞ iff ε_n²b→∞. Exact τ=−1 null has zero false rejection; τ=+1 null error O((ε_n² b)^(−1))→0. Alternative false acceptance at most e^(−4)+ζ_d+32/((d+1)ε_n²)+128d/((d−2) ε_n²b)→e^(−4). For sufficiently large n base error <1/3; O(log1/δ) majority repetitions yield O(d log n/(ε_n² n) log1/δ) queries and o(d) for fixed δ. The primary identity 1−fτ=||ΞτUΞτ^{-1}−U†||_F²/(2d) converts ε to squared distance; δ distance threshold ω((log n/n)^(1/4)). All implications use explicit uniform published inequalities, not plugging n-dependent ε into an unquantified big-O.

## originality

PASS

Best-of-knowledge PASS for a nontrivial, motivated vanishing-resolution consequence of primary published finite-error inequalities; original stated theorem fixes ε and does not state an n-dependent promise. Does not claim a new protocol, a necessary threshold, or stronger information-theoretic lower bound.

## value

PASS

The natural experimental resolution shrinks with system size; quantifying exactly when a prescribed no-auxiliary protocol remains sub-2^n-query yields a motivated accuracy–complexity boundary. It is an achievability extension, not a paper-sized innovation or a claim of optimality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
