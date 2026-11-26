# Independent mathematical audit

## correctness

PASS

A neighbor shore with j ones makes a current zero flip iff j>=k and a current one flip iff d-j>=k. This gives exactly the four stated actions, with the central class either all retain, all complement, or empty at d=2k-1. For two active shores, two central words stay central and repeat by the second update; a nonempty complemented word is never fixed. With no central word the first update is periodic, and with exactly one central word the second update is uniform. In the latter case the first update is nonperiodic exactly when the outer-class word was nonuniform, yielding Q2. Its central action decides whether the outer word's orientation agrees with the uniform word forced on the other shore, giving the basin coefficients. For s<k<=d the d-word is frozen; each of its outer words gives one fixed state, while each central word gives 2^s fixed or period-two states. This also supplies the uniform-basin counts implicit, not separately displayed, in this branch: each global constant has basin 2^s, since the frozen word must already equal that constant; there is no opposite uniform cycle. For k>max(a,b) all basins are singletons. Direct independent vertex-update replay gives (N1,N2;Q0,Q1,Q2)=(2,38;40,120,96) for (4,4,2), including 36 middle/middle states with both words complemented, and (2,2502;2504,392,1200) for (6,6,2). The replay also checks two one-inactive-shore examples and relevant basins.

## originality

PASS

The general period-at-most-two conclusion is already known. The distinct mathematical content is the sharp uniform two-update entry bound on these bicliques together with the labelled orbit, depth and basin census. None of the inspected prior statements covers that combination or implies it directly.

## value

PASS

Complete bipartite graphs are a natural dense test family for reversible synchronous dynamics. The explicit maximal depth and exactly which labelled states realize it, together with the division between uniform basins and isolated central attractors, answer more than the known general period bound. The exact classification distinguishes the degree regimes and includes a sharp witness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
