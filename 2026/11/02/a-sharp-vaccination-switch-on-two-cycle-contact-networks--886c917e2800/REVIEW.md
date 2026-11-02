# Scientific review: A sharp vaccination switch on two-cycle contact networks

## Correctness — PASS

In the specified one-seed Reed–Frost/independent-bond process, the expected final infected count is \(1+S_v(q)/r\), where \(S_v\) sums unordered residual-graph pair-connectivity probabilities. The two arc events of each cycle are independent; they yield the displayed exact cycle, path and rooted-connection polynomials. Deleting the intermediary or a portal gives precisely the two closed forms; nonportal deletions contain the portal-deletion graph as a proper spanning subgraph and increase the objective strictly. The score difference \(D_r(q)\) has one physical zero: Descartes' bound of at most two positive roots is exhausted by sign changes in \((0,1)\) and \((1,\infty)\). The derivative at one and the uniform second-derivative estimate give the sharp \(r^3(1-q_r)\to6\) boundary. An independent exact-rational finite-state program corroborated 231 checks, but is not substituted for the general proof.

## Originality — PASS, with residual uncertainty

The closest epidemiological motivation is Li, Zhao and Zhang, *Site-bond percolation model of epidemic spreading with vaccination in complex networks* (2022), DOI:10.1007/s00285-022-01816-1. Its accessible abstract and first-page preview use generating functions for vaccination probabilities and epidemic thresholds on random network ensembles. Its full text could not be obtained, so this is a meaningful residual priority risk rather than a certified whole-document exclusion. Becchetti et al. (arXiv:2205.08774), full text inspected in its model and appendix, prove related independent-bond epidemic methods on small-world random graphs but do not imply the exact optimal vertex and switching root on two fixed cycles. Chatterjee and Zehmakan (arXiv:2305.16458), full text inspected in its vaccination/model sections, treat degree-normalized epidemic dynamics, not this homogeneous independent-edge law. Published mathematical-record searches for two-cycle vaccination crossover, bridge-versus-portal optimization, and percolation containment revealed no result implying this stated classification and cubic threshold. Failed search is not proof of novelty, and a specialist unindexed result remains possible.

## Mathematical value — PASS

A decision-maker vaccinating one person faces a genuine exact intervention reversal as transmission changes: a degree-three portal is best at low transmission but a degree-two intermediary is best at high transmission. The graph motif is a natural two-community contact network, the switch occurs for every cycle length, and the sharp window \(1-q_r\asymp r^{-3}\) quantifies the asymptotic scale at which this reversal is confined. The theorem is an explicit complete classification rather than a generic monotonicity or a trivial single-parameter substitution. Its small full-transmission benefit \(1/r\) is also quantified.

## Closest literature and limitations

Primary references: Li–Zhao–Zhang (2022), DOI:10.1007/s00285-022-01816-1; Becchetti et al. (2022), arXiv:2205.08774; Chatterjee–Zehmakan (2023), arXiv:2305.16458; Kenah–Robins (2007), DOI:10.1103/PhysRevE.76.036113. The homogeneous independent-bond model must not be silently extended to general SIR processes with shared infectious-period randomness. Source inspection uncertainty is recorded in AUDIT.json. Independent external validation has not occurred.

Self-review: passed. Independent audit: not yet performed.
