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
# Reproducible verification

Run `python verify.py` using Python 3.10 or newer; there are no third-party dependencies. The script checks four different small graph classes by two exact rational recursions (one on physical labeled vertex subsets, one on coarse vacancy counts), the generator inequalities for integer class totals 10 through 1999 together with their factored identities, and independently integrates the limiting martingale variance using midpoint quadrature. It also runs two seeded finite-size simulations solely as sanity checks.

The exact terminal distributions for \((|A|,|B|,|C|)=(2,2,2)\), \((2,2,4)\), and \((3,3,2)\) assign respectively \(8/65\), \(96/1183\), and \(1644/7865\) probability to two unmatched vertices. The limiting variance values computed by both the formula and quadrature are approximately \(0.005316274621\), \(0.045661088368\), and \(0.087538396729\) for \(\alpha=0.2,0.3,0.4\).

The symbolic rational identities printed in RESULT.md establish the generator bounds for all integer \(L\ge10\); the loop is an additional consistency check, not their infinite proof. Finite recursions and Monte Carlo cannot establish the asymptotic central limit theorem. The latter follows from the stopped-martingale argument and its explicit all-time tail control.
