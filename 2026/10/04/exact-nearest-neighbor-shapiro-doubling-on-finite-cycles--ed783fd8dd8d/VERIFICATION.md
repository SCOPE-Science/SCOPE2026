---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

With \(c_n=1\) for even \(n\) and \(c_n=\cos(\pi/n)\) for odd \(n\), set \(C_n=4c_n-1\) and \(h=C_n1_U-1_{2U}\). The decomposition used in the package is exact: the pointwise nonnegative measure \(\sigma=(6c_n-4)(\delta_1+\delta_{-1})\) has nonnegative coefficient because \(n\ge5\), and the remainder \(	au=h-\sigma\) has Fourier transform \(4(1-x_k)(x_k+c_n)\), where \(x_k=\cos(2\pi k/n)\). The smallest sampled cosine is \(-c_n\), so \(	au\) is of positive type. Pairing an admissible nonnegative positive-definite \(f\) with \(\sigma\) and \(	au\) proves the upper bound. The explicit witness \(f_*(j)=(c_n+\cos(2\pi\lfloor n/2floor j/n))/(1+c_n)\) has nonnegative Fourier coefficients and is pointwise nonnegative; it vanishes at the two neighbors and takes value \(2c_n-1\) at distance two, attaining \(C_n\). This gives three on even cycles and \(4\cos(\pi/n)-1\) on odd cycles. The verifier checks the primal and dual formulas through \(n=400\), but the closed dual certificate proves every \(n\ge5\).

## originality

PASS

Gaál and Révész define exactly the Shapiro-type extremal quantity \(Q(U,k)=S(U,kU)\) for doubly positive functions on general LCA groups and prove a general dual decomposition theorem. Their full primary text develops the abstract cone duality and variants of the extremal problem but does not state the nearest-neighbor finite-cycle parity formula. The audited result is an explicit primal/dual solution of one natural finite-group instance; the general dual theorem provides the framework but not the optimal coefficient. The classical Lovász theta value for odd cycles concerns an edge-zero semidefinite optimization and does not imply this local five-point/three-point mass ratio. Current Resultary search returns the assigned record as the exact leading same-object result and no independent stronger finite-cycle formula.

## value

PASS

The nearest-neighbor ball is the canonical local set on a finite cycle, and two-fold Shapiro doubling is a standard extremal invariant in the Gaál--Révész framework. The exact parity split, sharp witness and explicit positive-type dual certificate give a useful solvable finite-group benchmark and expose a genuine \(n^{-2}\) odd-cycle defect, rather than merely evaluating a random small instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
