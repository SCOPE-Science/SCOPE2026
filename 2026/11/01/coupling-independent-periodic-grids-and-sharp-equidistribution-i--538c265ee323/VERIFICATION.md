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

# Verification record

The analytical proof in `RESULT.md` is the evidence for statements quantified over all positive integers and all Borel couplings. Its critical modular congruence lemma and the conditional offset-grid quadrature bound are explicitly proved. Their assumptions include strictly positive integer expansion factors \(A,C,E\ge2\), deterministic real shift and canonical half-open remainder. The sharp lower bound requires \(r=0\) and uses the ordinary unwrapped coordinate observable \(h(x,y,z)=z\).

Run `python3 verify_periodic_grid.py` in a directory containing the standalone companion file. The checker uses `fractions.Fraction` throughout, builds the entire fixed-point set by the nested congruence equations, and checks direct returns under the original map for the polynomial forcing \(\Phi=b y^\gamma\), \(\Psi=d z^\gamma\). It tests three distinct parameter cases: slopes \((2,3,2)\), \((3,2,2)\) and \((2,2,3)\); widths \(1\), \(5/3\) and \(7/4\); exponents \(2\) or \(3\); nonzero and zero shifts. In each case the numbers of fixed points at periods \(1,2,3\) are \(2,72,1274\). It additionally checks the coordinatewise mean inequality and exact sharp \(z\)-mean discrepancy at width \(7/4\), zero shift and period \(3\). A separate discontinuous Borel forcing case (piecewise-constant rational shifts in the first two coordinates) is checked at the same three periods, returning exact counts \(1,27,343\) and direct periodic returns. All checks passed with exact rational arithmetic.

The checker samples finitely many smooth polynomial and discontinuous Borel couplings. It does not exhaust all Borel functions, all periods, all observables or all numerical properties; those infinite assertions rest on the stated proof. No independent audit or certification has been carried out. Publication-priority uncertainty persists because some relevant classical full texts were not read.
