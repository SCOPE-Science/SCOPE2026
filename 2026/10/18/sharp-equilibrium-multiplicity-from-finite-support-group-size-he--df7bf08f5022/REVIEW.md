# Independent mathematical audit

## correctness

PASS

For experienced group sizes n_j>=3, payoff difference is B*x*sum_j w_j(n_j-1)(1-x)^(n_j-2)-c. In z=1-x the polynomial -c/B+sum a_j(z^(n_j-2)-z^(n_j-1)) has at most 2m+1 nonzero monomials, hence at most 2m positive roots with multiplicities by Descartes, so <=2m interior equilibria. For all m>=1, explicit L=16m,R=L^2,n_j=R^j+1,w_j=1/m,c/B=1/(4m) have peaks p_i=R^-i with G(p_i)>=1/(em)>lambda and valleys q_i=(LR^i)^-1 with G(q_i)<1/L<lambda. The alternating 2m disjoint sign intervals force 2m simple roots; exactly m attract. Checked m=1 endpoint case; numerical evaluations for m=1..5 confirmed all peak/valley inequalities but prove no infinite statement.

## originality

PASS

The exogenous group-size replicator payoff and nonlinear pivotality are known, but the exact support-size root bound plus all-m explicit multi-attractor realization was not implied by the inspected comparisons. This is best-of-knowledge novelty with fixed-size/game-definition and unindexed-equivalent risks.

## value

PASS

A natural support-complexity parameter controls attainable equilibrium multiplicity exactly, and its sharp construction exhibits arbitrarily many stable population frequencies in a fixed quorum-two game; this is meaningful nontrivial qualitative game dynamics, not a routine numerical case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
