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

# Verification of weighted-wheel projection threshold theorem

The analytical proof is in `RESULT.md`. Its critical independently checkable identities are the grounded Green recurrence \((tI+L(C_n))g=e_0\); the cyclic variation \(\sum_k|g_k-g_{k+1}|=2(g_0-g_{\lfloor n/2\rfloor})\); the complementary spoke/rim absolute column sums \(A_{n,t}\) and \(B_{n,t}\); and the strict-monotonic Fourier expression for \(tg_0\).

The executable `wheel_verification.py` requires Python 3.10 or newer and SymPy. Execute `python wheel_verification.py` from the directory containing that file. The actual execution reported `PASS: 63 exact-rational parameter instances, 882 edge columns, 18 radical Green checks`. The checker constructs the grounded incidence matrix from the wheel's edges, recomputes the weighted Laplacian inverse, builds \(Q_{n,t}\) and \(C_{n,t}\) in edge coordinates, checks their projection and symmetry identities, checks both norms for every edge column, and checks the radical Green formula against the defining linear system.

The rational tests use \(3\le n\le11\) and conductances \(1/10,1/2,1,4/3,2,5,50\), yielding 63 instances and 882 total columns. An additional 18 tests independently substitute the radical Green formula for \(3\le n\le8\) with conductances \(1/2,1,2\). These checks do **not** quantify over every real conductance, prove the asymptotic in isolation, or certify literature uniqueness; those parts rely on the written mathematical arguments and the separately documented source comparison. Independent audit remains unperformed.
