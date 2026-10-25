# Independent mathematical audit

## correctness

PASS

For the matching-deleted graphical zonotope of K_n with n>=3 and 0<=k<=floor(n/2), maximizing segment endpoints under an isotropic zero-sum Gaussian gives each of n! coordinate orders probability 1/n!. In a fixed orientation class, precisely the deleted-matching pairs that are consecutive in one linear extension may swap, independently; other unmatched vertex pairs are graph-comparable, so class size is exactly 2^J, J the number of consecutive deleted pairs. For t prescribed pairs, 2^t(n−t)! permutations contain all t as blocks. Binomial inversion gives A_s=Σ_{t=s}^k (−1)^(t−s) binom(t,s)binom(k,t)2^t(n−t)!, and vertex angle multiplicity N_s=A_s/2^s. Collision C=(1/n!²)Σ binom(k,t)2^t(n−t)! and v=Σ(−1)^t binom(k,t)(n−t)!. The generating function E[a^J]=Σ binom(k,t)2^t(n−t)!/n! (a−1)^t converges via the coefficient bound (2k/n)^t/t!<=1/t! to exp(2ρ(a−1)) if k/n→ρ; Gaussian S→Pois(2ρ), while reweighting each class by 2^(−S) gives uniformly selected vertex S→Pois(ρ). I independently exhaustively grouped orientation signatures for n=4..7 and every admissible k and verified that all sizes equal 2^J, separately from the packaged n<=8 verifier; the all-n statements use the proved swap and exponential-series lemmas, not small enumeration.

## originality

PASS

Best-of-knowledge novelty is the specific fully quantified invariant, not the underlying classical method or any known special-case total count. The old acyclic-orientation/ordered-partition picture gives the correct equivalent formulation but not, in sources inspected, the specific matching-specialization 2^s angle spectrum or two differently sampled Poisson laws. Comparing mathematical implications rather than titles: old counts cannot determine second moments or size-biased versus unweighted sampling limits.

## value

PASS

Normal-cone angles determine how likely different exposed vertices are under random optimization, which cannot be inferred from the number of vertices of a graphical zonotope. The exact factorial spectrum yields collision probabilities and reveals that Haar-direction-selected and uniformly selected vertices have asymptotically DIFFERENT Poisson parameters, a structural bias persisting in a dense natural graph family. These concrete invariants are useful to random optimization, graphical zonotope geometry and asymptotic combinatorics, not just a known orientation count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
