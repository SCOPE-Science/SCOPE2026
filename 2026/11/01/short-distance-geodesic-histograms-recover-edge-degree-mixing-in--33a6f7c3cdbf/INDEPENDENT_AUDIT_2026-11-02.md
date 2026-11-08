# Independent mathematical audit

## correctness

PASS

Decompose ordered edge pairs: same-edge region area 2r-r² through 1; shared-vertex direct corner r²/2 or 1-(2-r)²/2; for r<=3/2 every other shortest admissible route can use at most one complete intervening edge. The additional one-bridge corner triangle contributes (r-1)²/2, counted twice for each middle-edge configuration. For this radius range corner triangles have disjoint positive-area interiors, including in triangle graphs, and route-count coefficient Q=sum_uv(d_u-1)(d_v-1), with m-S+Q=H-2S. Thus the CDF spline, one-sided derivative reconstruction m=2/F’(0+), S=m² F’’(0+)+2m, H=2S+(m²/2)(F’’(1+)-F’’(1-)). For explicit graphs E1={04,12,13,23,34}, E2={01,13,14,23,24}, m=5,S=12,H=24 versus23, giving same degree sequence and first separation just above r=1. Independently computed exact rational shortest-route polygon areas for 24 graph/radius cases, including triangle, 5-path, star, square cycle and both witnesses; all agreed. Finite checks do not replace proof for arbitrary graph size.

## originality

PASS

Wei-Walteros-Batta (2019/2020) give a strictly broader forward distance-distribution framework for arbitrary edge-weighted networks; the general piecewise-linear PDF and any forward CDF special case are entirely prior. The assessed claim is the inverse recovery from local derivatives and its sharp degree-sequence indistinguishability threshold; their inspected Theorem 4/5 and applications do not state this inverse proposition. Best-of-knowledge original only as that nontrivial inverse classification, residual risk of being an immediate corollary or known graph reconstruction result.

## value

PASS

Recovering endpoint-degree mixing from local metric-graph geodesic histograms is a motivated network inverse problem: it identifies degree-correlation information genuinely invisible to vertex-degree multiset and to all shorter-radius observations, with a sharp explicit witness. Forward spline alone would be an unoriginal application; value is the precise inverse and sharp first-onset result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
