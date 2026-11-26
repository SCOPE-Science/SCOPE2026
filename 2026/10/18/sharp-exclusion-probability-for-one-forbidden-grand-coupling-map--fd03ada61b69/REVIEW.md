# Independent mathematical audit

## correctness

PASS

Verified the full one-map equivalence and relative asymptotic analytically. The cube cut by sum x_i <= n-1 is integral: at a vertex on the cut, at most one coordinate is not at a cube bound, and the integer right-hand side forces that coordinate to be integral too. Lifting its binary law to row marginals uses the positive 1-x_i denominators. For a=n-1 the uniform-sum density bound and ratio Jacobian give (a/n!) d^(a-1)(1-d)^(-n), with equality up to 1/2; the Dirichlet mass constant is exactly 1/(n^n(na)!). The Gamma representation implies nM and n sum d_i^2 tend to 1 and the n-scaled slack tends to 0, giving log W=n+1/2+o_P(1). For an explicit integrability check, on T>=na/2 bound exp(r nM) by exp(2r max G_i/a) for fixed r>1. On max G_i>2a, the union bound in expectation and a Gamma tilt of 1/4 give at most n exp(-a/2)(3/4-2r/a)^(-a), exponentially small for large a. The lower-Gamma-tail event T<na/2 contributes at most exp(rn+na/2)2^(-na-1). The remaining simplex corners have beta power b-n=(n-1)(n-2) and are exponentially negligible on the n^2 scale. The n=2 case needs no corner bound: continuity and row exchangeability give probability 1/2. The result is exactly for one fixed, not necessarily injective, map and normalized iid uniform rows.

## originality

PASS

The supported increment is the sharp general-n nonrepresentability probability for one preassigned map, including the e^(1/2) correction, not the sampling model, the n=2 answer, or a solution for all permitted map sets. The closest inspected full-text prior solves n=2 and gives a sufficient proper-subset obstruction, not the full simplex criterion or the asymptotic under this distribution.

## value

PASS

Resolves a natural and explicitly asked subcase of the published probability question. Separating the integral normalization from the concentrating row-normalization product produces a nontrivial sharp multiplier, not merely an order estimate or recomputation of the two-state case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
