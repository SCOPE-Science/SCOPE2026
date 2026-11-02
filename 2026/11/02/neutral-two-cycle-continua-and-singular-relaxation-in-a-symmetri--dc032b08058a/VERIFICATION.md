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

# Verification of the neutral two-cycle and slow-time theorem

The analytical argument in `RESULT.md` supplies the infinite-time and small-parameter proofs. `verify.py` provides independent finite consistency checks of the formulas using SymPy and SciPy; it is not an exhaustive certificate.

Run `python verify.py`. The script checks the exact identities \(J_1(s)=J_2(s)=s\); symbolic formulas for \(H_1\), \(H_2\) and their second derivatives; selected strict convex/concave cases; inverse consistency; local first-order inverse expansions at both degenerate exponents; and four first-passage computations near the degenerate parameters. The script executed successfully and reported 179 finite checks and identities.

The two exact passage-time integrals from amplitude \(1/4\) to \(3/4\) are numerically \(4.207740802102\) at \(p_0=1\) and \(7.363093797459\) at \(p_0=2\). For perturbations of size \(0.0002\), the four scaled first-passage counts differed by less than \(0.04\%\) relative error, consistent with the convergence theorem.

No finite computation establishes the global dynamical trichotomy or the uniform perturbative limit; these rest on exact convexity/concavity and the compact-time Euler argument. No independent external audit was performed.
