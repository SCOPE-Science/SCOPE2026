---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

On the orthogonal complement of constants the objective is N times trace of the inverse. Its Hessian is strictly positive in every nonzero symmetric direction, and the simple-graph off-diagonals make edge-to-Laplacian injective. On the compact budget simplex the objective diverges at disconnected limits. Hence a unique minimizer exists, invariant under cube translations and ordinary-coordinate permutations. Each class must be positive, since omitting either class disconnects even in dimension two. The Walsh mode with k ordinary bits and distinguished bit ε has eigenvalue 2b(k+εx), with multiplicity binomial(n,k) for each ε, n=d−1. This gives precisely 2^(2d−2)F_n(x); F_n=(n+tx)(A_n+B_n). The class budget fraction tx/(n+tx) is a strictly increasing coordinate in which the conductances are affine, giving exactly one stationary root. At t=1 all directions are interchangeable. Independently differentiating gives F_n'=tA_n+Σ_{k=0}^n binomial(n,k)(tk−n)/(k+x)^2. The normalized binomial concentrates at k/n=1/2; lower-tail exponential bounds control inverse powers for k≥1. For x=ny, y>0, nF_n'/2^n tends to the derivative of f_t(y)=(1+ty)(2+1/(y+1/2)). At t<1 its derivative changes sign only at the asserted positive y_t, so fixed y on either side brackets the root and the normalized value tends to f_t(y_t)=2+2√(t(2−t)). At t>1 fixed positive x has positive derivative eventually, while the k=0 term forces negative derivative near zero. At the resulting x→0 root the k≥1 terms plus tA_n are (4(t−1)+o(1))2^n/n; the term n/x² balances this, giving the stated asymptotic. It also gives n/(2^n x)→0, so the zero-index contribution to F_n/2^n vanishes, yielding 4, the same limit as t=1. The constant conversion is N³/8=2^(3d−3). No varying-price or finite deletion claim follows. The exact small-cube inverse and eigenpair checks and bounded scalar diagnostics in verify_hypercube.py were inspected, not rerun; the independent argument supports the unrestricted and asymptotic claims.

## originality

PASS

Credit prior strict convexity and equal-price cube symmetry, as well as the routine Walsh diagonalization. The supported distinct claim is the one-direction-priced Kirchhoff optimizer and its fixed-price asymptotic split and normalized cost. The closest catalogue matches change the graph, objective, or both; they were compared mathematically, not excluded by date.

## value

PASS

The priced direction is required to keep the two halves connected. Finite positivity alone would not distinguish an order-one direction from a ratio shrinking exponentially. The exact exponent and constant, together with the cheap-side linear growth and the different limiting objective below unit price, quantify a real optimizer sensitivity in a symmetric standard network.

The dated certificate retains the supplied scientific assessment, sources and limitations.
