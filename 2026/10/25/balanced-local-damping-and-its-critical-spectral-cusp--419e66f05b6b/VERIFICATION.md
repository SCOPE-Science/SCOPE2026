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

# Reproducibility and verification

The file `check.py` uses Python 3, NumPy and SymPy. Run `python3 check.py` in a directory containing it. It evaluates six exact polynomial identities, 1,200 independently computed quartic-root comparisons under nonnegative fixed-budget local dampers, and eight small-imbalance asymptotic comparisons. The included program passed those tests when run with the packaged contents.

The proof in `RESULT.md` is the evidence for the quantified conclusions over all positive masses-normalized parameters. Finite random numerical tests are neither an exhaustive search nor a proof. The uniqueness arguments use the four-root sum and an explicitly nonzero translated odd coefficient for \(G\le4\sqrt a\), and a strict intermediate-value root obstruction when \(G>4\sqrt a\). The critical cusp is obtained by balancing terms at a double characteristic root. No claim is made about an independently verified formal proof, transient operator-norm optimality, or behavior outside the stated linear mechanical model.
