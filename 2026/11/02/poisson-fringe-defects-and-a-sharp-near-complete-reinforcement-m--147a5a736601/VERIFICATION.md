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
# Computational and analytical verification

The proof in `RESULT.md` reconstructs the exact recursive-tree growth expectation, second-moment concentration, Poisson thinning, negligibility of nested cut edges, count-sequence tightness, compound-Poisson root deficit, and the walk's binary Fourier/parity identity. It applies to \(Nq_N\to\lambda\in[0,\infty)\). No finite computation is substituted for convergence of infinite distributions.

The complete standalone Python 3 file `verification/check.py` uses only standard-library exact fractions. Executing `python verification/check.py` produced the saved `verification/check_output.txt` with 63 passing exact-rational assertions. It independently enumerates all parent-choice arrays through order 7 to check the fringe-frequency identity, and compares the exact walk Markov recursion with the separately enumerated cut-forest parity probability for orders 2 through 6 at three rational cut probabilities per order.

Limitations: these checks are finite and do not certify asymptotic uniqueness, historical originality, analytical tightness, or statistical sampling; those statements are argued in `RESULT.md`. The asymptotic theorem does not assert convergence rates and no independent audit has been performed.
