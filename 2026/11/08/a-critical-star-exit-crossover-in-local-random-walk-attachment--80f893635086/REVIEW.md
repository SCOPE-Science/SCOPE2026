# Review: star-exit crossover in local attachment

## Correctness
The claim is confined to one-edge per arrival, independent uniform starting vertices and independently selected walk lengths in \(\{0,1\}\). The exact conditional stay-star probability equals \(((1-q)j+q)/(j+1)\); the product, gamma conversion, tail-sum comparison and two scaling limits follow by the displayed identities. The proof explicitly handles \(q=0\), \(q=1\), \(s\ge2\), integer times and moving parameters. A separate graph-transition checker executed 4694 exact assertions. Finite verification is not used to claim the infinite proofs.

## Originality
Three model-defining works were materially examined: Saramäki–Kaski (2004), Evans–Saramäki (2004), and Cannings–Jordan (2013). The last explicitly states that stars are eventually left but does not quantify the delay; its mixture section does not provide star-exit distributions. The original model papers emphasize degree distributions and growth rather than first-exit lifetimes. Searches for the first nonstar time, its heavy-tailed mean, and the perturbative crossover yielded no dominating explicit published statement. This is evidence of a distinction, not a guarantee that no general-purpose renewal or network-growth formula contains an implicit corollary. Related random-walk hitting-time and redirection literature is a residual priority risk.

## Value
The relevant 2013 result skips a star initial graph by conditioning on eventual escape. Almost-sure escape can be misleading as a finite-time surrogate: the exact mean is infinite for pure one-step walks. A small zero-step perturbation regularizes that mean only logarithmically, while the precise noise–initial-size scale separates Lomax-like and exponential waiting. This gives a concrete, natural finite-time boundary for an established stochastic network-growth theorem rather than an arbitrary statistic or an unrelated finite enumeration. It does not claim a new general theorem on arbitrary evolving graphs.

## Source and proof limitations
No post-exit growth law or quantitative global degree profile is proved; the critical weak limits do not transfer moments. The first model preprint and the 2013 full journal article were inspected in substantial relevant portions, but all possible historical sources cannot be exhausted.

Self-review: passed. Independent audit: not yet performed.
