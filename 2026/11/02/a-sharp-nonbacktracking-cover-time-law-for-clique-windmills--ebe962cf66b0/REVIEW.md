# Scientific review: a sharp nonbacktracking cover-time law for clique windmills

## Correctness (C): PASS

The asserted objects are the genuine uniform-neighbor nonbacktracking walk and the standard simple walk on \(K_1\vee(nK_m)\), with fixed \(m\ge3\). The proof derives the per-excursion avoidance probabilities exactly from absorbing races, including the prohibited immediate return after entering a petal. It treats nonbacktracking hub memory explicitly rather than pretending that excursions are independent. For any fixed marked set its conditional hit hazard differs from \(\sum_i h(s_i)/n\) by \(O(n^{-2})\), uniformly in the number of previous unsuccessful excursions; factorial moments then show a Poisson law for uncovered vertices. Independent exponential-tailed excursion lengths justify moving from excursion counts to edge-step cover times; a union bound and Wald's identity give the mean asymptotics. The exact-rational finite-state checker passes 114 assertions for both walks on all petal sizes 2 through 7. The full asymptotic proof is analytic, not inferred from those finite tests.

## Originality (O): PASS, with residual historical risk

The closest full-text primary comparison is Tishby–Biham–Katzav (2021, arXiv:2110.13592): its random regular graph models and associated nonbacktracking cover-time calculations do not include clique windmills with a hub whose degree is \(nm\), and its regular-network Gumbel constants cannot be substituted into the displayed windmill law. Breen et al. (2022, arXiv:2203.12049) treat nonbacktracking Kemeny constants, not full vertex-cover times. Sylvester (2021, arXiv:2102.12356) proves rationality of finite Markov-chain cover-time means, which is weaker in a different direction. The separately known triangle-bouquet nonbacktracking calculation treats \(m=2\), whereas this finding requires \(m\ge3\), for which an excursion need not cover an entire petal. The new comparison also distinguishes the sharp leading mean-ratio \((m+1)/(m+2)\) from a generic Gumbel-class statement. Searches for clique-windmill, bouquet, nonbacktracking and marked-excursion formulations revealed no equivalent theorem; search failure alone is not a proof of priority. Specialized nonindexed graph-cover calculations are a residual risk.

## Value (V): PASS

A bouquet of cliques is a canonical highly inhomogeneous graph with a single high-degree bottleneck. Its cover time probes a meaningful algorithmic distinction: the two walk rules have exactly the same mean duration per hub excursion, yet excluding immediate backtracking produces a measurable strict asymptotic reduction in total exploration time. The result gives exact petal-hit probabilities, identifies why the hub memory does not destroy the uncovered-vertex Poisson limit, and quantifies the speedup sharply for every fixed clique size at least three. This is not an arbitrary parameter slice or a mere textbook coupon-collector substitution, because in the genuine nonbacktracking process excursions are dependent and a petal may be only partially explored.

## Limits and independent status

The result is not uniform when \(m\) grows, and it makes no finite-size stochastic ordering claim. Independent validation and independent historical priority verification have not occurred.

Self-review: passed. Independent audit: not yet performed.
