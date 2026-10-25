# Scientific review

## Correctness — PASS

The source's BDF1 half-step and doubly stabilized Crank–Nicolson endpoint reduce exactly to the two rational expressions stated in the finding. The positive-domain factorization gives a strictly increasing ratio \(R(u)\), showing that the upper interval boundary is the worst-case input; oddness gives the lower boundary. Multiplication by a positive denominator yields the exact cubic \(Q_{s,v}(h)\). Strict negativity creates actual overshoot near \(u=1\), not merely failure of a sufficient bound. The phase diagram follows from the unique maximum of a rational function whose derivative numerator is strictly decreasing. Both boundary equalities and \(v=0\) are included. The independent direct-equation rational verifier ran successfully. The theorem is mathematical and not based on extrapolation from its finite tests.

## Originality — PASS, best-knowledge

The 2023 primary source, arXiv:2310.19663v1, was examined in full around its method and maximum-bound proof, and its sufficient gridwise conditions do not imply the exact homogeneous if-and-only-if polynomial or its reentrant phase diagram. The related stabilized CN/AB literature involves different stages and recurrence laws; a published mathematical result on that method's reversal threshold does not cover this map. Semantic searches of public research records and the accessible earlier claim collection did not identify the same polynomial, an equivalent classification, or a broader theorem that implies it. This is a best-knowledge assessment, not a guarantee of global uniqueness. A re-expression in classic invariant-domain or SSP literature is a residual risk.

## Value — PASS

The question is intrinsic to maximum-bound preservation of a named numerical method, not an arbitrary invariant. The result identifies a sharp obstruction inherited by every periodic/Neumann spatial implementation from its homogeneous modes. The unexpectedly disconnected safe-step set at intermediate second stabilization explains why a step-size restriction need not be monotone and why asymptotically large steps can regain positivity. The exact \(4+2\sqrt2\) first-stabilization boundary and \(v_*(2)=1/4\) give usable analytic benchmarks that are not visible from sufficient meshwise stability estimates.

## Closest literature and limitations

The exact algorithm and prior sufficient bounds are due to Hou, Ju, and Qiao (arXiv:2310.19663v1, equations (2.11a)–(2.11b), Theorem 2.1). Hou and Leng (2020) and Feng, Tang, and Yang (2013) analyze stabilized CN/AB methods, not this BDF1 midpoint construction. The analyzed invariant-interval improvement is **not** a sufficient theorem for nonconstant spatial states, and does not establish convergence or energy stability for the PDE method. Independent mathematical assessment has not occurred.

Self-review: passed. Independent audit: not yet performed.
