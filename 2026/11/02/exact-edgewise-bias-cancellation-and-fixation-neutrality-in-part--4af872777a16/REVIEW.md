# Scientific review

## Correctness

PASS. The oriented-update contribution of each discordant undirected edge equals its weight times the sum of endpoint preferences divided by \(2nD\), regardless of which opinion is on which endpoint. Vanishing cut sums for every initial configuration force the coefficient of each edge to vanish using a singleton/singleton/pair identity; connectedness then gives the bipartite alternating classification. Strictly positive copying probabilities make absorption almost sure in the finite connected system. A bounded stopped martingale yields the exact fixation probability. The two-sided weighted-degree identity gives the polarized half probability and a geometric first-change time with mean \(2/(1-h)\). Exact finite Markov checks supplement, but do not replace, the general proof.

## Originality

PASS, subject to normal bibliographic uncertainty. The originating source analyzes the fixed-preference microscopic rule but emphasizes mean-field phase portraits, modular network approximations, and simulation; its full text and appendices do not establish the weighted finite-chain martingale characterization or sharp first-flip delay. Sood–Redner (2005) already proves the **unbiased** degree-weighted law and the complete-bipartite 50-50 case, neither of which is asserted to be novel here. Masuda–Gibert–Redner (2010) studies a different conserved quantity for rate heterogeneity and mean-field partisan voting, and Masuda–Redner (2011) and Borile–Maritan–Muñoz (2013) address partisan and quenched-field effects in other graph/limit regimes. The crucial distinction is exact, nonzero, edge-alternating preference in the finite stochastic copying chain. Database and related-claim searches yielded no result that implies the full theorem; inaccessible or unindexed equivalent statements remain a risk.

## Mathematical value

PASS. This is a complete graph-theoretic classification of when conflicting fixed preferences preserve fixation odds in a natural voter process, not an isolated special example. It gives a sharp quantitative contrast between preference-independent consensus probabilities and an expected first-change time that diverges as the agents approach unwavering partisanship. The weighted version covers heterogeneous contact intensity and the necessity statement detects precisely why a single same-sign edge or odd cycle breaks neutrality. These properties provide exact boundary cases against which modular approximate dynamics can be compared.

## Limitations and closest literature

The result concerns strictly finite connected **undirected weighted** networks, \(|b_u|<1\), a particular asynchronous copying rule, and two opinions. It does not identify the full mean consensus time on general graphs and does not apply at the zealot endpoint. The nearest explicit prior fixation theorem is Sood and Redner's unbiased complete-bipartite result. A possible same-result treatment under unsearched terminology remains the principal originality risk. The finite verification checked 456 drift identities and solved 292 finite-chain transient equations; it is not an infinite proof.

Self-review: passed. Independent audit: not yet performed.
