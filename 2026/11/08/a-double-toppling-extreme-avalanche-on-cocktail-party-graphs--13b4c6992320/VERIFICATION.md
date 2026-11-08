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

# Verification of the cocktail-party extreme-avalanche theorem

## Analytic certificate

The proof in `RESULT.md` supplies (i) the upper odometer \(q=(2,1,\ldots,1)\), (ii) an if-and-only-if burning bijection with the vertex-deleted graph, (iii) both closed matrix-tree determinants, (iv) the stationary Green-function mean, and (v) the \(e^{-1}\) limiting activity share. The comparison vector's putative terminal heights can be negative at the drive; the first-illegal-excess argument explicitly verifies why the odometer bound remains valid.

## Reproducible computation

From the same directory as the included scripts:

```bash
python verify_exhaustive.py
python verify_reduction.py
```

The first script uses direct stable-height enumeration, Dhar recurrence testing, and an explicit legal-toppling stabilizer for \(m=2,3,4\), giving respectively \(4,384,82944\) recurrent states and \(1,45,6125\) maximizing states. It separately checks the exact means \(2,3/2,4/3\), the maximal odometer pattern, and the universal toppling bounds.

The second independently evaluates reduced Laplacian determinants exactly for every \(m\) from 2 to 10, verifies the Green-function linear system, explicitly enumerates recurrent states of the smaller graph for \(m=2,3,4\), and checks the corresponding maximizing configurations in the original graph. It also prints finite approximations to the proven \(e^{-1}\) limit; numerical approximation is not used as a proof of the limit.

The scripts require Python 3; the second also requires SymPy. All checked cases passed. Results for unbounded \(m\) rest on the analytic proof, not on extrapolation from finite tests. No independent scientific audit was performed.
