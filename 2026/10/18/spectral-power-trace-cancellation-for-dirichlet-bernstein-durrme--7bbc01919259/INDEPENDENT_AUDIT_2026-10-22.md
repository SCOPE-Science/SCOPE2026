# Independent mathematical audit

## correctness

PASS

Using Dirichlet posterior moments, the operator preserves polynomial degree, is selfadjoint for its actual weighted measure, and acts on top degree j by lambda_(n,j)=∏_{r=0}^{j-1}(n-r)/(n+A+r). Orthogonalized degree-j subspaces therefore carry this eigenvalue with dimension binom(j+d-1,d-1), yielding exact power trace over 0≤j≤n for every s>0, independent of individual shapes θ_i except A=Σθ_i. On j=t√n, a log-product expansion gives -t²-(A-1)t/√n+(A t²/2-t⁴/6)/n plus controlled remainder; Gaussian domination and exponentially small tails beyond j>n^(1/2+1/32) justify termwise summation, and polynomial multiplicities yield n^(d/2) and n^((d-1)/2) coefficients. Gaussian integrals give second coefficient (d+1-A)Γ((d-1)/2)/(4(d-2)!s^((d-1)/2)), cancelling iff A=d+1. For d=2, explicit h² correction plus two half-line Euler–Maclaurin endpoint terms yields (3A²-12A+14)/12 + A/(4s)-1/(6s²). At A=3, the λ product is a central binomial ratio and telescopes at s=1,2 to (n+2)/2 and (n+2)²/[4(n+1)]. Independently calculated exact rational traces for all n=1..23 and triangle asymptotic residuals at n=10k/40k/100k decreasing like O(1/n) in tested critical case, but analytic tail bounds establish the infinite limit.

## originality

PASS

Finite Bernstein–Durrmeyer eigenvalues and multiplicities are established prior art; fixed-function multivariate operator asymptotics and finite composition kernel formulas do not automatically determine traces over a growing number of polynomial eigenspaces for arbitrary real positive s. Independent searches found no direct theorem giving the n^((d-1)/2) cancellation hyperplane and d=2 constant. Abel–Berdysheva (2010) is a highly plausible full-text inaccessible source (authorized Oxford VPN disconnected), so this is a best-of-knowledge PASS with explicit substantial historical priority risk rather than an assertion that the inaccessible whole paper is negative.

## value

PASS

Growing-rank spectral trace of a natural positive simplex averaging operator probes global spectral concentration, unlike fixed-function approximation estimates. The dimension-uniform cancellation precisely at total Dirichlet shape A=d+1 identifies a sharp structural critical surface, with an explicit all-real-power triangle order-one invariant and exact s=1,2 checks. The invariant is motivated by spectral statistics and critical Lebesgue shape rather than arbitrary coefficient bookkeeping.

The dated certificate retains the supplied scientific assessment, sources and limitations.
