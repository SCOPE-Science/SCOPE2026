# Review: exact leader placement in two weighted bridge-linked cliques

## Correctness

**PASS.** The grounded inverse of a uniformly weighted clique is explicitly computed, including its diagonal and column norm. A single Sherman--Morrison identity gives all cross-clique leader pairs. The cut-edge electrical resistance series law gives same-clique pairs and proves strict inferiority of omitting a gateway when both leaders are in the same clique. Those cases exhaust all pairs. The sharp \(p>4q-2\) possibility boundary follows from a strict comparison with a split-leader competitor, with a separate large-bridge constructive sufficiency argument. The two transition points in the example are exact rational equalities and the remaining candidates are strictly dominated there as specified in the proof. No step depends on finite enumeration.

Direct reproducibility checks: 300 exact weighted graph configurations, 9000 exact rational grounded matrix inversions, 2400 strict exclusions of non-gateway same-clique pairs, and exact checks at two rational transition points. The checker outputs PASS. Finite checking is corroborative, not proof of all quantifiers.

## Originality

**PASS under bounded best-knowledge comparison, with residual priority risk.** The public full-text material inspected from Lin--Fardad--Jovanović establishes general stochastic leader-selection algorithms and convex relaxations, not the five-orbit structural reduction. Fitch--Leonard establishes a general centrality formula and explicit path/cycle conclusions; Patterson--Yi--Zhang establishes resistance methods and explicit path/cycle/tree families. A documented earlier equal-strength \(K_2\)-versus-\(K_q\) special case is subsumed, so neither that case nor general trace-inverse machinery is claimed as new. They do not imply arbitrary internal conductance scales, arbitrary orders at least three, or the sharp \(4q-2\) leader-concentration criterion without additional analysis. published-finding corpus and literature searches using bridge-barbell, weighted two-clique, grounded trace, gateway/non-gateway, and four-to-one threshold formulations did not reveal an explicitly covering claim. Search absence is not a proof of priority. Unindexed specialized work or a generic formula specialized without a printed theorem remains a possibility.

## Mathematical value

**PASS.** This is a natural noisy-consensus leader-allocation problem with two dense communities and a single bottleneck. It gives a constant-size, globally exhaustive optimizer despite quadratic growth in leader pairs, a sharp **parameter-independent** barrier to placing both leaders in one community, and a constructive sharp converse. The exact three-stage migration example, from distributed non-gateway leaders to one bridge gateway and finally both leaders in the larger internally weak community, is a genuine structural phenomenon absent from the earlier single-transition two-vertex-clique case. The family has freely varying clique sizes, internal coupling scales and bridge strength; it is not a numerical table recomputation or a one-parameter substitution.

## Closest literature and limits

Primary references: Lin, Fardad and Jovanović (arXiv:1302.0450, initially 2013); Fitch and Leonard (arXiv:1407.1569, initially 2014); Patterson, Yi and Zhang (arXiv:1708.06873, initially 2017). The latter is later supporting literature and does not set the archive anchor. The result assumes strictly positive uniform conductance within each clique, exactly one bridge, and exactly two perfect leaders. Full bibliographic exhaustion is unavailable, so publication priority remains a residual risk. The verification is self-review only and is not independent certification.

Self-review: passed. Independent audit: not yet performed.
