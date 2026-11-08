# Independent mathematical audit

## correctness

PASS

For q>=3 pairwise distinct cyclic run letters, each directed boundary a_i a_(i+1) occurs at one phase modulo p, fixing start phase of any factor containing a boundary. Closed factors split into disjoint constant words a_i^s (p types), complete first returns with constant frontier B_(i,s)=a_i^s full intermediate runs a_i^s (p types), and mixed-frontier returns of length p+m indexed by phases t in [0,h_k(m)-1] where first m letters cross a boundary. These mixed returns have exactly two occurrences of their length-m prefix, at offsets 0 and p; constant prefixes excluded in count sum_i(r_i-m+1)_+. The sum of h_k(m) for 1<=m<=(k-1)p is (k-2)p^2+p(p+1)/2, and the exclusions sum_i r_i(r_i+1)/2. Thus all length coefficients and C_+(W)=(k-2)p^2+(p^2-sum r_i^2)/2+2p. Independently enumerated literal proper-border closed factors for all 27 3-run vectors in {1,2,3}^3 at k=2 and 3; every factor set and total agreed. Source checker covers 4032 cases but was inspected, not blindly used as infinite proof.

## originality

PASS

Parshina–Puzynina provides general closed-factor upper bounds for primitive cyclic squares, while Parshina–Zamboni addresses aperiodic Arnoux–Rauzy words. This restricted periodic root with all distinct run labels has an exact disjoint type classification and length polynomial, not just general bounds; direct Resultary search found a binary closed-rich-maxima record but not this theorem. Best-of-knowledge originality with residual equivalence risk.

## value

PASS

Exact distinct closed-factor length spectrum is a standard string-combinatorics invariant. The result characterizes a natural structured class of periodic words and gives the exact p^2 gain from another period, plus a second-moment dependence on run sizes. It is not known table recomputation or arbitrary finite parameters; it proves an all-length combinatorial pattern.

The dated certificate retains the supplied scientific assessment, sources and limitations.
