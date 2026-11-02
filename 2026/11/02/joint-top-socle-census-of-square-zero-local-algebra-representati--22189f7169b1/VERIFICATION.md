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

Run `python3 verify.py` with Python 3 and the standard library. The executable source is embedded alongside this file.

The checker separately enumerates all labeled tuples satisfying all pairwise products zero and computes their joint horizontal-block and vertical-block ranks. It evaluates a **two-sided** subspace Möbius formula, algebraically equivalent to but computationally distinct from the **single** Möbius formula displayed in the proof. The following thirteen complete finite configurations were checked: \((d,r,q)=(1,1,2),(2,1,2),(3,1,2),(4,1,2),(2,2,2),(3,2,2),(2,3,2),(2,2,3),(2,2,4),(3,2,3),(2,3,3),(2,2,5),(3,2,4)\), where \(\mathbb F_4=\mathbb F_2[u]/(u^2+u+1)\). The full joint distributions agreed in every configuration.

For \((d,r,q)=(3,2,2)\), the nonzero cells \((a,c):\mathrm{count}\) are \((0,0):1\), \((1,1):63\), \((1,2):42\), \((2,1):42\), totaling \(148\). The checker terminates with the marker `RADICAL_SQUARE_ZERO_TOP_SOC_CENSUS_OK 13`.

The finite computations do not verify every prime power or dimension and are not treated as proof of the general theorem. The proof instead uses exact flags, Möbius inversion, a basis construction and geometric vector bundles. No independent mathematical audit has been performed; historical originality remains provisional.
