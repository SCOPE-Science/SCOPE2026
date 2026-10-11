# Independent mathematical audit

## correctness

PASS

The proof reconstructs. After the stated inner multiplicity limit, total-rate-k Poissonization gives independent direct marks of rate a per vertex and edge-support arrivals of rate 2(1-a)/(k-1). Recovery completeness implies that a target is unrecovered exactly when its support component is a simple tree with no direct mark: a mark or cycle recovers and propagates, while an unmarked tree has an explicit nonzero dual witness. Cayley's formula then gives the finite-k survival sum. For fixed component size the terms converge to the rooted-tree series; components larger than J while unmarked are bounded by exp(-ar(J+1)), and U_k(r) is bounded by exp(-ar), yielding both pointwise and dominated convergence. The tree equation gives u=exp(-ar-2(1-a)r(1-u)); setting t=1-u and integrating by parts yields the claimed integral. A fresh independent numerical integration at the stated optimum gives 0.793933444596334, consistent with the source optimum but not used as proof.

## originality

PASS

Originality passes. The full Hofmeister--Bitar--Yaakobi primary PDF gives the degree-two LT/peeling optimum p1 approximately 0.15547, p2 approximately 0.84453 with objective approximately 0.7939, and explicitly conjectures that the ideal weight-one/weight-two ratios in the Boruchovsky et al. construction and the corresponding normalized expectation converge to those values. The full Boruchovsky et al. PDF defines recovery completeness and G_k(x,y), supplies the cycle/repeated-support recovery mechanism, but does not prove this large-k asymmetric limit. The audited marked-random-graph argument proves precisely the conjectured missing implication.

## value

PASS

The theorem resolves an explicit recent conjecture linking an ideal-decoding construction to the degree-two LT peeling optimum. It also explains structurally why the ideal decoder's finite-size cycle advantage disappears at first order when direct marks have positive density. This is a motivated probabilistic/coding-theoretic gap, not merely recomputation of the numerical optimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
