# Scientific review of the finite zero-sum transient-depth theorem

## Correctness

PASS. Every payoff ranking induces one of the \(3^6\) row-minimum/column-maximum maps, and the nine-cell linear-extension recurrence gives its exact rank multiplicity. All eight joint cycle/depth counts sum to \(9!\). A separate exhaustive permutation enumeration gives exactly the same counts and the five vertex-depth totals; both are implemented from scratch in the included `verify.py`. A second structural count checks the longest transient: \(72\) possible directed saddle-plus-chain graphs with \(96\) rank orders each. The symmetry argument verifies distribution independence under any common atomless law. No experimental extrapolation or unspecified infinite claim is involved.

## Originality

PASS, with a remaining literature-access risk. The most relevant full primary text, Karelas–Lugosi–Zhang, arXiv:2610.29153v1, Section 6, supplies a general one-cycle probability integral and asymptotic cycle statistics, not the distribution of first entry times to a recurrent class. Section 5 covers transient paths in common-interest rather than zero-sum games. Because the same four-cycle type occurs with two different maximum depths, the new entry-time law cannot be recovered from cycle-type counts alone. Heinrich et al. (2023) treat playing sequences and convergence in a random-game model with separately sampled player payoffs; their results do not establish this exact correlated-payoff finite law. Actual semantic searches found no equivalent statement among relevant published mathematical records or the accessible research ledger. Unindexed equivalent finite calculations remain possible; absence of search hits is not proof of uniqueness.

## Mathematical value

PASS. First entry into the recurrent class is the fundamental finite-time observable of deterministic best-response dynamics, distinct from the length and number of recurrent cycles. Three strategies per side are the smallest balanced zero-sum environment admitting a full four-edge transient, and the exact hitting distribution and expected time provide a natural, distribution-free benchmark at that boundary. The calculation is a complete finite classification rather than a selected incidental numerical example. It does not purport to solve the general-strategy case.

## Limits

The theorem concerns directed-graph entry times, not arbitrary update protocols or repeated-game convergence rates. No independent scientific audit has been performed.

Self-review: passed. Independent audit: not yet performed.
