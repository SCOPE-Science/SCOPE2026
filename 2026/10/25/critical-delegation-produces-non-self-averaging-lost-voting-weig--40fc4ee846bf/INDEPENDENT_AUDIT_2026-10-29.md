# Independent mathematical audit

## correctness

PASS

PASS: The exact finite first-path probability is a_(n,k)=q(1-q)^k∏_(r=1)^k (n-r)/(n-1), summing over distinct successful ancestry lengths. Conditional on a first successful path of s vertices, the second path has an exact backward recursion incorporating hits to the known successful set, newly encountered direct voters and collisions with previously exposed outside delegators. For k,s of order sqrt(n), logarithmic expansion of the no-collision product yields exp(-ct-t²/2) and the two-path success function H_c(t)=(c+t)I(c+t). Gaussian product tails justify dominated Riemann-sum convergence to P(c)=cI(c) and J(c)=∫ ce^(-ct-t²/2)H_c(t)dt. The variance is J(c)-P(c)^2=∫ce^(-ct-t²/2)(H_c(t)-P(c))dt, strictly positive because H_c is strictly increasing and equals P(c) at t=0. Monotone coupling as q rises and Markov bounds yield off-critical concentration to 0 or 1. Independently quadrature-checked P(1)=0.655679542418798472 and variance V(1)=0.0700843376534750558; these numerics corroborate, not prove, the limiting theorem.

## originality

PASS

PASS, qualified: Targeted Resultary and primary literature comparisons confirm the strongest known coverage as explicitly acknowledged in the source inspection: existing complete-digraph finite delegation partitions and mean crossover, versus the new explicit positive critical limiting variance. Full-text material read and unresolved historical-priority risks are recorded; absence from a search is not asserted as proof of novelty.

## value

PASS

PASS: A mathematically natural random functional-digraph model of delegation has a sharp participation threshold and an explicit positive limiting variance in the critical window. The result quantifies persistent fluctuations of lost voting weight that a previously available mean participation crossover and finite partition recursion cannot reveal without further asymptotic analysis. The work does not claim a full weak limit, strategic voting accuracy or alternative cycle resolution rules.

The dated certificate retains the supplied scientific assessment, sources and limitations.
