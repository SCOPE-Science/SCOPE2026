# Independent mathematical audit

## correctness

PASS

For compact stationary measures contained in 0<X<Y<m/n, the invariant generators of Y, Y²/2 and log X yield n meanY+meanX=m, Cov(X,Y)=-n Var(Y), and E[(1+εX)(Y-X)]=(n+1)/k. Algebra gives (m-(n+1)meanX)(1+ε meanX)/n=(n+1)/k+ε[Var(X)+nVar(Y)]. The equilibrium quadratic has leading coefficient -ε(n+1)/n, so if its two distinct physical roots x_-<x_+, factorization gives Var(X)+nVar(Y)=(n+1)/n(x_+-meanX)(meanX-x_-). Both variances zero only for an equilibrium atom, making the mean bounds strict for non-Dirac measures. Independent SymPy rational expansion for m=2,n=1/3,ε=5/4,k=41/200 gave polynomial -(1230x²-861x+124)/246 and exact roots 7/20±sqrt(131241)/2460 (0.202734960462713...,0.497265039537287...). The numerical example is supplementary; the proof is all-parameter under the stated hypotheses.

## originality

PASS

The Zeng–Yu full author-hosted 17-page source studies the EXACT normalized epidemic model, the quadratic endemic branches and Hopf/bistable examples, but its theorems concern equilibria and bifurcation parameters, not the invariant-measure covariance and exact mean–variance factorization. Its PDF contains neither 'variance' nor 'average'. A positive cycle example is not a statement about every compact interior stationary distribution. Resultary returns the assessed result and different epidemic models, no same-model dominating moment theorem. The 2007 introduction of the identical incidence model was accessible only in abstract, so older equivalent averaging identities remain possible; assessment is best-of-knowledge, not certified priority.

## value

PASS

The model's published bistable Hopf cycles make finite-amplitude averages of infected population a natural exact invariant. The formula pins a weighted fluctuation magnitude to the distance of the true cycle mean from the two endemic branches, with a strict global mean trap not obtainable from local Hopf linearization; it is useful for simulations and epidemiological interpretation. Limited to compact interior invariant measures and not an existence claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
