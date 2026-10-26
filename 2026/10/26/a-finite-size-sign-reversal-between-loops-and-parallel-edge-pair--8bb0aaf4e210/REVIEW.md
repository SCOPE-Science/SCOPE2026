# Scientific review

## Correctness — PASS

For a uniform perfect matching of \(q\) labeled half-edges, any \(k\) prescribed disjoint pairing edges appear with probability \(1/[(q-1)(q-3)\cdots(q-2k+1)]\). The proof counts single internal edges, two-edge cross-group witnesses, and the compatible three-edge unions. It derives \(\mathbb E L=S/(q-1)\), \(\mathbb E P=B/[(q-1)(q-3)]\), and \(\mathbb E LP=(BS-T)/[(q-1)(q-3)(q-5)]\), hence the exact covariance. Substitution of regular degrees gives its factorized sign law. The four-half-edge boundary case is enumerated separately. A standalone exact-arithmetic program checks 2,223 independent moment/formula/sign identities, including all 701 weak group-size profiles at total half-edge counts 6, 8, and 10. The unrestricted proof is combinatorial rather than experimental.

## Originality — PASS, provisional

Wormald's survey (Theorem 2.6), Janson (2006, Section 7), and Angel–van der Hofstad–Holmgren (2016, Theorem 1.4 and Section 3) treat self-loops and multiple-edge pairs through Poisson approximation and, in the last paper, indicator-pair covariance bounds. The inspected texts do not state the precise signed finite covariance or the degree-two versus higher-degree reversal. The exact formula does not follow solely from asymptotic independence. A residual priority risk remains because prior indicator expansions might implicitly recover the result after unsupplied algebra; source material has not been exhaustively surveyed over all historical literature.

## Mathematical value — PASS

The configuration model is a standard random-graph comparison object. Although loop and parallel-pair counts become asymptotically independent in fixed-degree models, their finite covariances have a structurally opposite sign depending on degree, with a sharp boundary and distinct decay rates. The classification explains two natural regimes of interaction invisible to limiting independence; it holds for every admissible regular parameter, and the irregular-profile identity provides a tool for degree-heterogeneous applications. This is a distributional distinction about standard graph defects, not a numerically isolated curiosity.

## Scope and limitations

No claims concern simple graphs, connected graphs, or uniform unlabeled multigraphs. For irregular profiles the formula is exact but its signs are not classified. The analytical proof handles the entire specified parameter domain. No independent audit or guaranteed historical-priority certification has been carried out.

Self-review: passed. Independent audit: not yet performed.
