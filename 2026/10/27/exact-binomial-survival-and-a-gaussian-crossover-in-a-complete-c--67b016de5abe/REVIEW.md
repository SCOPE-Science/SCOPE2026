# Scientific review

## Correctness — PASS

The claimed law is derived directly from the exact three-valued ecological update, not inferred from an asymptotic simulation. For an initial count \(k\) of biomass-two sites, the first update is controlled by the scalar threshold \(T_n=(n-1)(\alpha^{-1}-1)\). If the initial low sites die, exactly \(k\) sites survive; otherwise the second update decides whether the initial high sites die or all survive. The proof also handles the exceptional singleton survivor correctly: its biomass reaches a fixed point, rather than an oscillatory two-cycle. All other surviving nonempty groups of at least two enter a two-cycle. For generic finite-\(n\) parameters, the exact binomial formula follows by counting initial states. The Gaussian-window claim is proved by the binomial central limit theorem and an explicit \(O(n^{-1/2})\) bound on exceptional tie counts. The standalone rational checker passed 25,560 enumerated initial states. This finite test is a cross-check, not the infinite proof.

## Originality — PASS, with historical-priority risk

The closest primary paper, Sergo–Koller–Erba–Zdeborová (arXiv:2606.09494v1), introduces the same model and includes the fully connected limiting extinction threshold \(\alpha_c=2/3\). The claimed finite-\(n\) binomial law, exact initial-state survivor classification, and one-sided Gaussian window are distinct from simply knowing that threshold or solving infinite-degree cavity equations. Goles–Olivos (1980, 1981) gives the general period-at-most-two bound, not the ecological survival distribution. The present formula also differs from known bounded-degree cycle-graph formulas. Searches for the exact map, binomial law, complete mixing, and critical window did not identify an implication-equivalent published statement. This is best-knowledge priority, not an exhaustive proof of novelty: equivalent complete-graph threshold automaton treatments, or uninspected portions of earlier literature, remain possible.

## Mathematical value — PASS

The motivating ecological work reports a nontrivial change in the extinction threshold between finite-degree and fully mixed regimes. Exact finite-system survival counts and their critical scaling answer the natural follow-up question of how finite complete populations approach that high-degree threshold. The result characterizes all initial conditions, gives a closed survival probability rather than numerical cavity predictions, and identifies both a discontinuous limiting occupied fraction and its unusually one-sided Gaussian smoothing at the \(n^{-1/2}\) scale. It is a precise finite-population theorem for a natural model, not an arbitrary numerical slice. The contribution does not cover heterogeneous couplings, \(K>2\), or continuous dynamics.

Self-review: passed. Independent audit: not yet performed.
