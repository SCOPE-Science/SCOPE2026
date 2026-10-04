# Review

## Correctness

PASS. Pairwise independence and fairness determine the first two moments of the
Hamming weight exactly. Confining that weight to one residue class converts the
problem to the existence of an integer-valued variable \(J\) on a finite
interval with prescribed mean and variance. The lower variance
\(\delta(1-\delta)\) follows from the nearest-lattice inequality, while the
upper variance \(m(N-m)\) is the finite-interval variance bound. Sufficiency is
constructive: the nearest-lattice law and endpoint law have the same mean and
span the entire admissible variance interval by convex mixing. Conditional
uniformization over \(K\)-subsets then gives the Bernoulli vector and verifies
pairwise independence exactly.

The threshold proof separately verifies all four feasibility components and
identifies an explicit residue that fails at \(n=q^2-2\).

## Originality

PASS, with a residual coding-literature risk. The 2012 Benjamini--Gurel-
Gurevich--Peled paper was inspected in full where it develops the limited-
independence extremal framework and classical moment-problem method. It
contains the familiar binary XOR phenomenon and discusses integer-support
sharpness, but no arbitrary-modulus residue-simplex criterion or \(q^2-1\)
threshold was found.

The full Ramachandra--Natarajan preprint was also inspected. It formulates
pairwise-independent Bernoulli-sum optimization using fixed univariate and
bivariate marginals and first-two-moment bounds, but its objectives are tail,
union, and intersection probabilities. No finite-\(n\) Hamming-weight
congruence theorem matching the present statement was located.

Targeted semantic searches over the published result database found related
moment reductions for pairwise-independent occupancy statistics and rare
Bernoulli sums, but no implication of the modular threshold.

## Value

PASS. Modular counting is a basic nonmonotone Boolean statistic. The theorem
gives an exact and sharp answer to when pairwise independence can make that
statistic completely arbitrary: not merely one extreme event, but the full
simplex of residue laws. The threshold \(q^2-1\) quantifies precisely how much
finite length is needed before second-order information imposes no restriction
at all on the modular output.

Same-model review: passed. Independent audit: not yet performed.
