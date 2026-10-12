# Scientific review: exact prime-power binomial progression gcd

## Correctness — PASS

The new result follows from four validated steps: the interpolation identity \(D(k)\mid k+1\), the published local prime-divisibility result for vanishing exponents, a uniform Kummer carry lower bound when \(a>t\), and explicit choice of a binomial coefficient attaining the lower bound. The high carry boundaries \(a+t+1\le j\le a+s\) are distinct from the low carry boundaries, and the witness digit-sum identities also hold in the boundary cases \(p=2\), \(b=1\), and \(t=0\). Exact finite integer arithmetic verifies the defining gcd for every \(2\le k\le160\), all component minima for \(3\le n\le1200\), and every witness through \(n=12000\). The proof, not the finite run, establishes the infinite result.

## Originality — PASS

The closest primary source is Guo et al., arXiv:2606.22997v1. Its Theorem 1 determines exactly when \(D(k)=1\), while Lemma 9 determines which primes divide \(D(k)\); these do not determine the exponent of a dividing prime. Exact-source, parameter, equivalent-form, stronger-coverage, OEIS, published-finding corpus, and comparisons with related mathematical claims found no full valuation formula. The previous same-source counting result determines an asymptotic frequency of nontrivial gcds, not their pointwise prime-adic orders. Unindexed equivalent literature remains possible.

## Value — PASS

The complete factorization is a natural missing quantitative invariant of the precise gcd studied in the source. It distinguishes higher prime powers hidden by a unit/nonunit test and gives witnesses realizing every exponent. The structural high/low carry argument explains the result uniformly for all integers, so the work is neither an unmotivated slice nor a routine table recomputation.

## Closest literature and limitations

The primary same-object paper is arXiv:2606.22997v1; the corresponding OEIS entry records only zero-versus-nonzero indices. The result applies to the full progression \(2\le q\le k+1\), and no claim is made for other ranges or independently established precedence.

Self-review: passed. Independent audit: not yet performed.
