# Scientific review

## Correctness — PASS

The key identity is an explicit stochastic channel \(G\) that maps the rare-start Bernoulli transition law to the common-start law at every correlation, independent of that correlation. Its entries are nonnegative for each \(0<a\le1/2\). Tensorization proves the all-bias rare-vertex inequality; weighted transpose symmetry under detailed balance gives equality of the \(L^1\) and \(L^\infty\) operator norms even for complex parameter mixtures. The exact homogeneous formulas are verified by differentiating a binomial probability generating function; the single-mode first derivative follows from unimodality and telescoping. Gaussian-Hermite limits follow by coefficientwise convergence of score generating functions and an exact uniform second-moment identity. The Poisson scaling follows from a moving binomial mode. Every limiting statement is analytically proved; finite tests are only corroboration.

## Originality — PASS with residual bibliographic risk

The closest established work on biased Walsh noise (Keller 2010, Definition 1.1 and Proposition 1.3) provides the multiplier and hypercontractive setting but not maximal endpoint row variation of all derivatives. Pisier 2007, Theorem 1 treats holomorphic semigroup factorization, without the parameter-independent stochastic garbling or binomial derivative norm profile. O'Donnell 2014, the bias and noise-operator chapters, supplies the standard kernels, not the exact derivative norms. A previously described first-chaos rare-vertex principle overlaps the special first derivative at correlation zero; that special case is **not** asserted to be newly discovered. Complete texts of published homogeneous second-Walsh and general q-ary second-Hamming projection results were inspected: each treats only a fixed degree-two projector, not parameter-uniform full semigroup derivatives. Targeted semantic and bibliographic searches did not reveal a theorem implying the full statement. Possible older unindexed Markov-chain or coupling literature remains a priority risk; negative searches alone do not establish novelty.

## Mathematical value — PASS

The result replaces an exponential maximum over kernel rows by a single explicit row for every product bias and every derivative order. Its fixed independent Markov factorization works not only for one derivative but for signed spectral superpositions. The exact binomial answer and the Gaussian-Hermite versus Poisson critical-time scaling quantify finite-time endpoint regularity with full constants. This is a structurally motivated semigroup norm problem, not an arbitrary finite-dimensional calculation.

## Evidence and limits

The analytic argument is in RESULT.md. The exact rational finite checker check.py performed 1,698 comparisons at explicitly encoded cases, including heterogeneous biases and orders; the results do not certify the asymptotic statements. The literature comparison is strong for inspected operator-semigroup and biased Boolean Fourier sources but not exhaustive. No independent review has been performed.

Self-review: passed. Independent audit: not yet performed.
