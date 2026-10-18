# Scientific review: invariant polarization measure for predictive opinion loops

## Correctness — PASS

The full hypothesis set fixes reciprocal positive network weights, every peer susceptibility in \((0,1)\), complete peer relaxation, perfect prediction, and a common platform susceptibility \(\beta\in[0,1)\). The proof first derives the exact equilibrium as the resolvent of the stochastic Friedkin--Johnsen response matrix. It then obtains detailed balance for that matrix under the explicit normalized weights \(\nu_i\propto d_i(1-\alpha_i)/\alpha_i\). The similarity/reversibility argument is sufficient for real positive eigenvalues, and the spectral expansion gives both strict variance decay and its sharp coefficient. The two-person case follows from its one-dimensional disagreement quotient; the three-person obstruction uses exact rational inversions and a strictly positive variance difference. The standalone checker recomputes these identities rather than accepting stored answers. Infinite-network, nonreversible, and finite-peer-interval claims are not made.

## Originality — PASS, subject to historical priority

The motivating Wu--Abebe--Mendler--Dünner paper already derives the full predictive-loop equilibrium resolvent, proves Euclidean-variance monotonicity for regular networks with homogeneous peer susceptibility, and proves a general consensus limit. It does **not** give this heterogeneous stationary measure, the sharp corresponding contraction on reciprocal weighted graphs, or an explicit three-person reversal of ordinary variance. The related Boudourides work derives susceptibility-dependent response matrices and an undirected degree-weighted spectral specialization **with homogeneous susceptibility and without repeated platform feedback**; those fixed-boundary spectral claims do not imply the precise heterogeneous result without an additional detailed-balance calculation. Classical reversible-chain spectral theory is background, not itself claimed new. Targeted mathematical-record searches and accessible historical claims did not show an equivalent statement; some unexamined broad consensus literature could still dominate the theorem. A failed novelty search alone is not the justification: the comparisons here are by exact assumptions, implications, and counterexample requirements.

## Mathematical value — PASS

The motivating source's regular-graph polarization result and its numerical treatment of irregular graphs leave a practical structural question: what, precisely, remains monotone when social influence and susceptibility are heterogeneous? The theorem supplies an explicit conserved population weighting, a quantitative sharp contraction valid without regularity or homogeneous peer parameters, and a **minimal** counterexample explaining why replacing the conserved weighting by the ordinary arithmetic variance is invalid. This is a classification of the permissible disagreement metric and a mathematically meaningful boundary to extrapolating a monotonicity claim, rather than a numerical-only example or a mere textbook restatement. Its applicability remains restricted to the declared feedback and network assumptions.

## Closest primary literature and residual limitations

1. Wu, Abebe and Mendler--Dünner, *Opinion Dynamics in Learning Systems*, arXiv:2603.12137, §§3--4, Appendix A.5--A.6. General loop/resolvent, narrower regular homogeneous variance result, broad consensus limit.
2. Boudourides, *Boundary-Value Friedkin--Johnsen Dynamics and Influence-Based Centralities on Networks*, arXiv:2602.08704, §§2.2--2.6 and 4.2. Fixed-boundary Green operators, susceptibility sensitivity, homogeneous undirected spectral results; no repeated prediction loop.
3. Aldous--Fill, *Reversible Markov Chains and Random Walks on Graphs*, Chapter 3. Standard reversibility used as a tool, not novelty.

Residual scientific limits: only finite connected reciprocal weighted graphs, strictly interior peer susceptibilities, homogeneous platform susceptibility, exact predictions, and infinite peer relaxation. Other historical FJ influence and Markov chain resolvent results could subsume parts of the statement. The proof is a self-review, not an independent historical or mathematical audit.

Self-review: passed. Independent audit: not yet performed.
