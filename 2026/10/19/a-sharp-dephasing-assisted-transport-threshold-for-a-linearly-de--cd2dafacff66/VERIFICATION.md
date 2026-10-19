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

# Reproducibility and limitations

Run `python check_three_site.py` with Python 3 and SymPy, NumPy, SciPy. The included program regenerates the expected absorption time from the exact nine-dimensional Lindblad superoperator and checks the independent rational formula. It then checks the derivative polynomial's first three coefficients, the two sign identities, positivity of every coefficient of degrees \(3\) through \(8\), and the exact large-gradient subleading term.

The program runs 48 separately implemented numeric Kronecker-resolvent comparisons on a Cartesian grid of rate, detuning, and dephasing values, as well as sampled polynomial root counts. These numerical samples are sanity checks, not a proof for all rates. The all-parameter theorem is proved using exact polynomial coefficient signs and Descartes' rule in the RESULT.md proof. The critical constant at \(k=1\) is a numerical evaluation of the rigorously unique positive root of an exact cubic, not an independent numerical discovery.

Actual checker execution for this package reported `83 symbolic, coefficient, and independent matrix checks passed`. Independent assessment of mathematical priority, particularly examination of the potentially related 2004 paper, has not been performed.
