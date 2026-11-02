# Scientific review

## Correctness

PASS. The arrow-cycle exclusion gives an if-and-only-if cut characterization: the only valid edge-choice strings are a block of left arrows followed by a block of right arrows. The rank-two cost is exactly a constant plus a simple symmetric random walk. The first-minimum count factors into independently reflected strict/weak positive ballot paths, including all \(n\ge1\) and the endpoint cases. An exact reflection identity and binomial expectation establish the mean-cost formula. Donsker's theorem, almost-sure uniqueness of a Brownian minimum, the continuous mapping theorem, and Lévy's classical arcsine law justify the arbitrary-tie-break limit. The BFD median tie is resolved by the immediate edge rank, including the odd-size correction. The included standalone checker exhaustively tests 65,534 finite rankings and independently traces 4,096 branching/profile pairs; finite computation is corroboration, not a proof of the infinite statement.

## Originality

PASS under inspected-evidence priority. The 2022 initiating paper defines minimum-cost BordaBranching and observes an empirical rank-versus-weight tension but does not state the two-guru path's optimal-cut correspondence or any random-preference arcsine law. The closely relevant 2023 successor studies random walks and **uniform mixtures over optimal branchings for a fixed preference graph**, which is mathematically different from random independently assigned preference ranks and the resulting distribution of a deterministic optimizing cut. The standard random-walk arcsine theorem itself is not new, but neither paper supplies the application, the exact finite first-minimum formula, or the comparison with BFD. Search for aliases and equivalent minimum-cost rooted forests did not reveal a dominating prior theorem. Residual risk: specialist literature on random optimal-rooted forests and image-segmentation watersheds may contain a related law not captured by the reviewed sources.

## Mathematical value

PASS. Minimum local-rank cost and balanced representation are competing social-choice objectives identified by the primary paper. Here a natural, parameter-free path family exhibits a sharp and unexpected effect: although global optimization saves only order \(\sqrt n\) second-choice assignments in expectation, the resulting guru representation can be unbalanced on order \(n\) with a precisely quantified probability \(2/3\). The full finite distribution, exact expected cost, and tie-break-independent limiting concentration law make the tradeoff reproducible and robust within the specified model; it is more than a one-off negative example or a restatement of the arcsine law.

## Sources and residual scope

Primary literature: Brill et al., *Liquid Democracy with Ranked Delegations*, arXiv:2112.07509v1, AAAI 2022 §§2, 3.3, 5, 6; Utke and Schmidt-Kraepelin, *Anonymous and Copy-Robust Delegations for Liquid Democracy*, arXiv:2307.01174, NeurIPS 2023 §§1–6. Classical: Feller's reflection and fluctuation identities; Lévy/Doney on the arcsine law. Other related research on popular branchings was compared at abstract level, not asserted to have been completely ruled out. The claim is only for fair, independent local rankings on a two-guru path, with finite exact law for the earliest minimizer. No independent scientific audit has been conducted.

Self-review: passed. Independent audit: not yet performed.
