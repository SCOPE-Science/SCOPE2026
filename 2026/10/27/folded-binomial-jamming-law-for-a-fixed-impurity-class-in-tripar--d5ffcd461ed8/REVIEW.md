# Independent mathematical audit

## correctness

PASS

At each accepted event the three possible types have weights ab, ac and bc, by independent equal-rate Poisson clocks and irreversible blocking. At stage j=n minus the number of AB dimers, a=j-x and b=j-y with x+y<=r; for j>=r+1 both base classes are nonempty. For a still-vacant marked C vertex, the probability of an AB event before its own match is at most q(a,b)=ab/(ab+a+b): first-step induction in c bounds continuation after any other C event by monotonicity of q, and [ab+(c-1)(a+b)q]/[ab+c(a+b)]=q. Thus it is at most j/(j+2) at stage j. Surviving to stage k (necessary for J_i<=k) yields the product (k+1)(k+2)/((n+1)(n+2)); at k=r+1 it also bounds J_i<=r. Summation by parts for 1/max(J_i,r+1) gives 1/n plus the sum of (k+2)/k over r+1<=k<n divided by (n+1)(n+2), bounded by the displayed harmonic expression. The next event's type AB vs impurity, and the identity of the chosen impurity, can be sampled before that impurity's previously unused independent uniform variable. Comparing this variable against a/(a+b) and 1/2 gives mismatch probability at most r/(2j) at early stages. Union-bounding mismatches and late/unmatched impurities gives the exact stated bound; on success the remaining bipartite imbalance is |r-2B_r|. At any terminal state at most one part survives, so the vacancy total is at most r (either vacancies lie in C or the base-part imbalance is at most r), with parity r. Thus expectation errors are bounded by r times TV. For the folded law, summing (2k-r) binom(r,k)=r[binom(r-1,k-1)-binom(r-1,k)] over k>r/2 and doubling gives the stated mean; the r=2,3 probabilities follow directly. A fresh forward rational recurrence (/workspace/branches/replay/r1_forward.py) checked the bound at n=2r+2 for r=2 through 6 and n=100 for r=2,3,4, including the supplied n=100 probabilities. These tests are corroboration only. The advertised Python 3.9 support for the supplied verifier is a minor documentation issue: int.bit_count requires 3.10; no frozen verifier was run. The proof assumes fixed r for the stated convergence, equal rates and the complete graph between distinct parts.

## originality

PASS

The supported distinct claim is the fixed-impurity folded-binomial terminal vacancy law with the explicit total-variation bound, not the general greedy edge-adsorption model or the absolute-binomial mean identity. The closest exact tripartite and fixed-impurity results inspected have materially different hypotheses and observables. Full text of the closest classical edge-adsorption paper remained unavailable; the verdict is best-of-knowledge, not historical certification.

## value

PASS

The balanced bipartite core alone is always perfectly matched at jamming. A fixed number of added vertices, despite vanishing density, produces a nontrivial microscopic residue distribution; already two yield a limiting half chance of imperfect coverage. The full law distinguishes mechanisms at a scale invisible to coverage fractions, and the explicit TV bound controls when that limit is predictive without extrapolating to a growing impurity class.

The dated certificate retains the supplied scientific assessment, sources and limitations.
