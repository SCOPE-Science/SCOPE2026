# Independent mathematical audit

## correctness

PASS

For iid Bernoulli(p), 0<p<1, the transfer matrix for occurrences of 10 has trace 1 and determinant p(1-p)(1-z). Its n-step generating polynomial is R_n(u)=sum_{k=0}^{floor(n/2)}(-u)^k binom(n-k,k). The Chebyshev recurrence factors R_n(pq(1-z)) as a product of 1-4pq cos^2(jπ/(n+1))(1-z), showing a genuine independent-Bernoulli law with parameters in (0,1). Reversal gives 01. For 11 the leading masses are p^n, 2p^(n-1)q, and (n-2)p^(n-1)q+3p^(n-2)q² for n>=4, violating Newton a_(d-1)^2 >= (2d/(d-1))a_d a_(d-2). At n=3 the generating quadratic has discriminant -4p³q<0. Swapping 0 and 1 gives 00. At n=1 each count is zero and at n=2 each count Bernoulli; p=0,1 excluded from dichotomy.

## originality

PASS

Best-of-knowledge PASS: published general rise/fall enumerators and real-root tests are related but their inspected statements do not provide the sharp cosine PB vs repeated-letter non-PB four-pattern classification. Chebyshev factorization as such is classical, not credited as novel; historical motif/run factorization remains a residual risk.

## value

PASS

This is a natural complete classification of four adjacent binary motifs for all iid interior biases and all lengths, sharply separating dependent indicator sums whose laws nevertheless are PB from those that cannot be PB. Explicit cosine parameters allow probability calculations without numerical root solving; this is more than a random small enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
