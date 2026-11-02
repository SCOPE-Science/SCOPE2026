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

# Reproducibility

Execute `python3 verify_hopf_criticality.py`. The program requires only a Python 3 standard-library installation. It independently computes the Hopf cubic coefficient (a) from the planar derivative formula and (b) from a normalized complex-eigenvector Kuznetsov multilinear contraction, and compares both to the closed payoff expression. It also checks the Hopf trace condition and verifies that the equilibrium is interior.

For the original paper's plotted parameters \((\theta,R,s,T,P,\varepsilon)=(0.8,1.5,0.5,0.5,0.25,0.5)\), the calculated \(\beta_h\) is about \(5.676683215269\) and \(\ell_1\) is about \(-0.618878506352\).

For the positive-payoff witness \((0.1,2,0.5,0.5,50)\), the calculated critical environmental speed is \(\varepsilon_c\approx23.607116993784\). The coefficient is approximately \(-5.560417137554\) at speed 1 and \(+1.572385202232\) at speed 30. The program additionally performs 100 reproducible randomized parameter checks, with a fixed seed.

These finite checks are not a proof of claims quantified over all real parameters, nor are they an independent scientific audit. The full analytical reduction, positivity inequalities, exact assumptions and boundary cases appear in RESULT.md. The sign of the first coefficient classifies local nondegenerate Hopf orbits only, not global recurrence or the degenerate equality.
