# Independent mathematical audit

## correctness

PASS

On complex ℓ²(Z^d), for each coordinate one may choose I or (1−θ)I+θS_j, 0<θ<1, independently. With c=θ/(2−θ) the universal scalar identity |u|²+c|v|²−|(1−θ)u+θv|²=c|(2−θ)u−(1−θ)v|² holds for complex u,v. Consequently |u|²+c|v|²−max{|u|²,|(1−θ)u+θv|²}=c min{|v|²,|(2−θ)u−(1−θ)v|²}≥0; summing with u=f(n),v=f(n−1) yields the exact ℓ² deficit and the 1D norm sqrt(2/(2−θ)). Equality forces at each n either f(n−1)=0 or f(n)=ρ f(n−1), ρ=(1−θ)/(2−θ)∈(0,1); an ℓ² nonzero solution has a leftmost nonzero index and thereafter a single nonvanishing geometric ray. Every such translated scaled ray attains the bound, so rigidity is complete in dimension one. For d≥1 positive averaging and commutation imply pointwise |R_{θ,d}f|≤M_d…M_1|f|; Fubini and the 1D estimate give upper norm (2/(2−θ))^{d/2}, while tensor products of 1D rays attain it. Independent exact SymPy expansion at θ=2/5 verified the scalar polynomial identity, squared norm 5/4, and the published package checker contains additional rational-weight checks; no finite trial is used to prove the all-weight/all-d conclusion.

## originality

PASS

Best-of-knowledge originality judgment for the exact scoped final claim, after mathematical prior-work implication comparison. Existing discrete centered synchronous cube and continuous symmetric semigroup maximal theorems have different kernels, scopes and quantifiers; no covering sharp weighted two-choice norm theorem was retrieved.

## value

PASS

Independent coordinate selection is the simplest nontrivial strong rectangular discrete maximal family. The exact exponentially growing dimension dependence, all-parameter weight profile and complete one-dimensional geometric optimizer/deficit identity provide a reusable benchmark distinguishing strong rectangular from synchronous cube maximal behavior; the result is an infinite-dimensional sharp inequality, not a trivial finite case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
