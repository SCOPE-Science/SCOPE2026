# Independent mathematical audit

## correctness

PASS

Let Y_t be number absent, start Y_0=0. Inclusion-expansion over selected coupon types gives exact return probability u_t=sum_{j=0}^m binom(m,j)q^(m-j)p^j(1-j/m)^t and Green function R(z)=sum_j w_j/(1-z(1-j/m)). Full-state holding rounds are geometric(p), and entrance-to-entrance generating function obeys R(z)=1/((1-qz)(1-F(z))). Laurent expansion R(z)=q^m/(1-z)+m sum_{j>=1}w_j/j +O(1-z) gives mean 1/(p q^m) and exact squared CV (2-p)q^m+2mp sum_j w_j/j -1. Under p=c/m the bounded binomial reciprocal converges to Poisson expectation, giving V(c)=2e^-c(1+cA(c))-1 where A(c)=sum c^j/(j j!). Its derivative has sign g(c)=-1+2c-sum_{j>=2} c^j/(j(j-1)j!), with g strictly concave, g(0)=-1,g(1)=e-2>0,g(infinity)<0. Therefore exactly two positive g roots, global min and max, and endpoint expansions V=1-2c+O(c²) as c down 0 and V=1+2/c+O(c^-2) as c tends infinity force exactly one V=1 crossing on rising branch. Independent exact one-coupon renewal computations agree, and inspected source checker independently solves finite rational hitting-time systems; numeric root brackets are illustrative. Renewal counting Fano limit takes time first, system size second.

## originality

PASS

Published primary results on the same subject and Resultary related findings were compared at the level of claimed mathematical implication; strongest already-covered components are credited and excluded from the novelty claim. The remaining specific classification appears new in actually inspected material, subject to listed source-access and indexing risks.

## value

PASS

A natural nonmonotone coupon model has an exactly classified critical entrance-cycle dispersion profile with two extrema and a unique Poisson crossing. This mathematically distinguishes sub- and super-Poisson coverage counts even though both endpoint regimes approach dispersion one, not just rederives the known stationary flux or generic renewal formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
