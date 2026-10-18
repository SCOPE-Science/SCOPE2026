# Scientific assessment: consecutive-square prime-counting roots

## Correctness

PASS. The inequality is reduced exactly to \(n\log(B/A)<\log A\), with \(A=\pi(n^2)>1\) and \(B=\pi((n+1)^2)\). In any six integers there are at most two primes greater than three. For \(n\ge100\), this bounds the increment by \((2n+7)/3\); the classical unconditional lower estimate \(\pi(n^2)>n^2/(2\log n)\) then yields \(n\log(B/A)<(69/50)\log n<(3/2)\log n<\log A\). The last step follows from \(2\log n<\sqrt n\). Exact integer arithmetic checks all 97 remaining indices, with independently implemented primality tests. The certificate is finite only after the infinite tail is proved.

## Originality

PASS with residual literature risk. Sun (arXiv:1402.6641, Conjecture 2.14(ii)) and OEIS A038107 state precisely the theorem as a conjecture, without a proof. The closest work on prime counts between squares (Hassani, arXiv:math/0607096) addresses different bounds. The distinct fixed-\(n\) root problem Conjecture 2.7(i) does not imply this cross-index assertion by direct substitution. OEIS A014085 contains counts, not the required general root monotonicity. Searches of statement, exponentiated equivalent, and logarithmic normalized formulation found no dominating result. Undiscovered equivalences remain possible.

## Value

PASS. This is a complete all-index resolution of a specific published 2014 conjecture on the prime-counting function, not an arbitrary parameter slice or finite extension. Its normalization differs mathematically from ordinary monotonicity of prime counts and from Legendre's prime-between-squares conjecture. The quantitative division into an analytically certified tail and a small exhaustive finite range is explicit and reproducible. No claim is made about the unrelated parts of Sun's catalogue.

## Scope and limitations

The certificate verifies exactly \(3\le n\le99\), while the proof handles every \(n\ge100\). The hypothesis on the classical prime-counting bound is clearly attributed; an earlier unindexed proof could affect originality. Independent validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
