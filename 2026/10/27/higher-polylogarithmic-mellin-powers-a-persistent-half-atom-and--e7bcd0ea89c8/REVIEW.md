# Scientific review: higher polylogarithmic Mellin powers

## Correctness — PASS

The order-two Dirichlet mean of equal-weight binary input is uniform; multiplicative Markov–Krein closure [1, Theorem 1.4(ii)] yields the k-fold product-uniform image. The second generalized Cauchy transform is z-inverse times a polylogarithm, and the order-two logarithmic derivative identity [1, Proposition 1.2] gives the claimed ordinary Cauchy transform. The polylogarithm cut discontinuity gives the continuous density; the endpoint residue limits give mass 1/2 at zero and none at one. Local Stieltjes inversion rules out extra singular mass. Leading large-argument and near-one polylogarithm expansions prove both asymptotic formulas for every integer k>=3. The embedded program passed 45 numerical checks; the infinite claims do not depend on enumeration.

## Originality — PASS, qualified

The main motivating theorem [1] proves existence/uniqueness and a general transform mechanism, **not** this explicit all-higher-power density and endpoint classification. The most consequential broader prior coverage is Mergny [2, Eq. (12)]: its additive Bernoulli self-convolution, after squaring and halving, exactly yields the k=2 logistic–Cauchy benchmark. Thus k=2 is excluded from the assessed original claim. For k>=3, the polylogarithmic quotients, fixed half atom, and order-varying endpoint exponents were not found in inspected primary sources, targeted published mathematical-record searches. James [3] gives beta-scaling representations with a different constraint on Dirichlet concentrations, not these explicit all-k densities. Equivalent results in older Dirichlet-mean or special-function literature remain possible, and the Lijoi–Regazzini [4] full text was not materially inspected.

## Mathematical value — PASS

The higher powers are a canonical, newly defined multiplicative semigroup arising from the first nontrivial two-atom law. Exact inverse base measures are substantially more informative than closure alone. The theorem classifies an infinite, natural family: a persistent atom of mass 1/2 despite vanishing mean, universal logarithmic left singularities whose prefactor grows linearly with power, and a strict right-edge hierarchy (finite positive density for k=3, vanishing with successively higher orders for k>=4). These are structural probabilistic facts not implied by the published two-fold additive density or an unexplained numerical transform.

## Closest literature and limitations

[1] P. Mergny, *Stability of the Markov-Krein Transform Under Classical Convolutions*, arXiv:2610.18436v1. General theorem includes closure and derivative formula. [2] P. Mergny, *An explicit example for the high temperature convolution*, arXiv:2204.07744, Eq. (12): known squared-pushforward k=2 benchmark. [3] L. F. James, *Dirichlet mean identities and laws of a class of subordinators*, arXiv:1010.1639: beta scaling identities. [4] A. Lijoi and E. Regazzini, *Means of a Dirichlet process and multiple hypergeometric functions*, arXiv:math/0410151: general inversion methods. Restricted to c=2 and integer k>=3; no arbitrary Bernoulli parameters, general parameters, or random-matrix realization.

Self-review: passed. Independent audit: not yet performed.
