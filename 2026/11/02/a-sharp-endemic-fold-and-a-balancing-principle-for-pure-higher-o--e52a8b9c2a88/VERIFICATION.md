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

# Verification and reproducibility

The proof in `RESULT.md` is the basis for all infinite and arbitrary-size statements. The accompanying `verify_tripartite.py` independently evaluates its key identities at exact rational parameter choices and checks its numerical consequences on a bounded sample of size vectors. From the directory containing the extracted files, install the dependencies in `requirements.txt` and execute `python verify_tripartite.py`.

The checker performs exact-rational equilibrium and Jacobian checks for the balanced three-group example of group sizes \((2,2,2)\): at \(\lambda=1\) the endemic equilibrium is \(x=1/2\) and the class Jacobian has eigenvalues \(0,-3,-3\); at \(\lambda=9/8\) the equilibria \(x=1/3\) and \(x=2/3\) have respectively one and zero unstable directions. It checks an unbalanced rational stable equilibrium \((n_1,n_2,n_3)=(72,27,16)\), \((x_1,x_2,x_3)=(1/2,2/3,3/4)\), \(\lambda=1/216\), including the positive-definite sign condition for the stability transform. It numerically minimizes the exact scalar curve and compares balanced versus every other integer partition of totals from 3 through 18 into three positive parts. This enumeration checks 3-partite instances only; it is not a proof for general \(m\) or unbounded sizes.

The static full-node Jacobian's transverse-mode argument and the analytic concavity inequality are proved in `RESULT.md`. No finite computation or approximate minimizer is used in place of these proofs. Scientific limitations, uncertainty about equivalent prior results, and the deterministic-versus-stochastic distinction are stated in `RESULT.md`.
