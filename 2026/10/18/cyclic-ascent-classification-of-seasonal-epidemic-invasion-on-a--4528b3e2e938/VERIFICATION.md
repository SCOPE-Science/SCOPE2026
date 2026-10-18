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

# Verification of the claim

The included `check_cycle.py` is an executable, standard-library Python script. Its path is relative to this package and it has no external dependencies. The script constructs exact rational shear products for all chronological permutations in dimensions \(2\) through \(5\), checks their full characteristic polynomials by Faddeev–LeVerrier, and checks the three-season threshold inequalities with \(P=8/27\). Execute with `python check_cycle.py`.

Recorded replay result:

```
PASS: 152 exact permutation characteristic-polynomial checks, n=2..5
PASS: 3-season example, P=8/27 between 1/4 and 1/2
```

The theorem for every integer \(n\ge2\), arbitrary real positive exposures, and all season orders is established analytically in `RESULT.md`. The checker covers finite rational cases only. The analytic averaged-system inequality is \(\log2>2/3\) by a positive series, not by relying on approximate floating-point evaluation.

No independent audit, external formal proof certificate, empirical disease observation or stochastic validation has been carried out. For parameter equality the result identifies a simple unit Floquet multiplier but makes no nonlinear stability claim.
