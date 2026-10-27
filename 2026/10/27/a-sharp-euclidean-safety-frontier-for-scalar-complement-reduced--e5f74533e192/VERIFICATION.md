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
# Verification of the stated analytical formulas

Run `python verify.py` in the same directory with Python 3. Only the standard library is needed. The script was executed successfully and reported 12,756 exact-rational evaluations of the derived Gram determinant, 14,000 seeded numerical tests of the spectral formula and contraction interval, and separate explicit exact witness and period-two matrix identities.

The code checks the polynomial identity, spectral-optimal parameter, sample operator norms, positive safe interval, impossibility witnesses, and the unbounded-transient family. In particular, \(a=10\), \(b=1\), \(k=2\), \(t=1/5\) gives a squared operator norm of \((21+5\sqrt{17})/50<1\), whereas \(t=1\) has norm \(2\) and the smaller spectral radius \(\sqrt{2/5}\).

The proof in `RESULT.md`, not these finite checks, establishes the statements for all dimensions, parameters, and weights. No independent mathematical audit has been performed. The checker uses approximate floating-point comparisons only for supporting diagnostics, not for any universal implication.
