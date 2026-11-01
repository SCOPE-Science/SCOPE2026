# Independent mathematical audit

## correctness

PASS

For a fixed convex polygon with all side lengths positive, on the event every side receives a sampled point the missing hull area is exactly sum of disjoint vertex triangles 1/2 sin(alpha_i) X_i Y_i. Their joint tail is (1-(x+y)/P)^N on two disjoint adjacent boundary arcs; integrate to obtain E(X_i Y_i)=P²/[(N+1)(N+2)] times four exponential edge truncation factors. The empty-edge probability is at most sum_i(1-l_i/P)^N, and the total error is uniformly bounded by a geometric constant times that probability. Thus the universal coefficient P²/2 sum_i sin(alpha_i) and exponential remainder are exact. Joint binomial void probabilities of all 2m rescaled endpoint gaps converge to independent exponentials; continuous mapping and uniform exponential tail bounds imply convergence of ALL fixed positive moments, variance 3 sum w_i² and the product E1 Laplace formula. No approximation by a smooth boundary or a growing number of polygon sides is used.

## originality

PASS

The same boundary-random-polytope sampling model is studied in primary prior literature, including local corner Poisson limits. Prochno–Schütt–Sonnleitner–Werner provide the asymptotic independence mechanism and a Hausdorff-distance result; Reitzner–Schütt–Werner derive volume deficit leading exponents for broader polytopes. Neither inspected primary text supplies the exact two-dimensional rational denominator with error exponentially small for every fixed polygon, nor the angle-sine coefficient. Novelty is restricted primarily to that finite-N perimeter–angle mean law; the exponential-product limiting law is an interpreted consequence of already-known local Poisson behavior.

## value

PASS

The result exposes an exact algebraic cancellation of all higher 1/N corrections in a classic random-polytope observable, and shows that leading mean/limiting distribution are insensitive to individual side lengths beyond perimeter and angle data. It is motivated by the polygonal boundary sampling problem and has useful explicit finite-sample and limit formulas.

The dated certificate retains the supplied scientific assessment, sources and limitations.
