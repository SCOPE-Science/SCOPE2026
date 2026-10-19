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

# Reproducing the transfer calculation

Execute `python verify.py` from this directory using Python 3. No external packages, network connection, or previously saved data files are necessary. For an independent *symbolic* check of the displayed invariant matrix factorization, use `python symbolic_verify.py` (requires SymPy); it must print `SYMBOLIC_VERIFY_OK`.

The checker creates \(B_m=P_2\square K_{1,m}\) directly as an undirected graph, constructs all of its directed arcs, applies the Grover coin to degree-two wing vertices, negates the Grover coins at the two marked body vertices, and performs the flip-flop arc reversal. Computations use `fractions.Fraction` throughout the exact full-graph evolution; the initial vectors are represented without the common normalization factor, which is divided out in the overlap.

The separate symbolic checker also verifies orthogonality of the reduced walk matrix, its characteristic polynomial factorization, and agreement of all three first odd amplitudes with the cosine expression. The main rational checker compares every time step \(0\leq t\leq54\) for every integer \(0\leq m\leq15\) against the proposed cosine closed form evaluated as rational Chebyshev polynomials, for **880** comparisons. It also tests the one-step incoming-target shift identity exactly. Its output includes the exact numerator/denominator for \(F_3(31)\) and `VERIFY_OK`.

This is a finite reproducibility check, not a proof that the formula holds for arbitrary \(m\) or arbitrary \(t\). Infinite validity follows from the explicitly factored eight-dimensional characteristic polynomial and three initial values in `RESULT.md`. The no-perfect-transfer theorem depends on the rational-algebraic-integer argument and irrational rotation density, neither of which is decided by simulation. Likewise, the mean-fidelity limit uses mathematical equidistribution rather than a truncated time average.

The independent-audit channel has not been performed; all results presented here have received only the self-review documented in `REVIEW.md`.
