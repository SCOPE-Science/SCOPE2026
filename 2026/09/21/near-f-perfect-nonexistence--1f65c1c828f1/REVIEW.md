# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.

The reciprocal identity was rederived directly from the involution on divisors:
\[
\sigma_2(n)/n^2=\sum_{e\mid n}e^{-2}.
\]
If \(d\) is the redundant divisor and \(q=n/d\), subtracting the terms corresponding to \(n^2\) and \(d^2\) gives exactly
\[
\sum_{e\mid n,\ e>1,\ e\ne q}e^{-2}=3/n.
\]
Every subsequent inequality uses only positive terms of this equality.

The odd case was checked carefully. Parity forces \(\tau(n)\) odd and hence \(n\) square. With two distinct primes, at least one of their reciprocal-square terms survives and already exceeds \(3/n\). For an odd prime power, the only residual exponents after the same comparison are \(p^2\) and \(p^4\), and both are ruled out by the displayed exact equations.

For \(v_2(n)=1\), the term \(1/4\) forces \(q=2\) once \(n>12\). If the odd part has two distinct prime factors, the inequality
\[
1/p^2+1/r^2\le3/(2pr)
\]
contradicts \(p^2+r^2\ge2pr\). If it is a prime power, the \(1/p^2\) term forces exponent at most two, and both exponents give impossible exact equations. The three small cases \(2,6,10\) were evaluated directly.

For \(4\mid n\), either the \(1/4\) term survives and \(n\le12\), or \(q=2\) and the \(1/16\) term survives, giving \(n\le48\). The twelve multiples of four through 48 were then checked exactly. The standalone artifact reproduces this finite table and additionally scans every \(n\le10^6\) by exact integer arithmetic, finding zero hits.

No step assumes unique factorization beyond ordinary integer factorization, and the proof includes \(d=1\) because that case corresponds to \(q=n\) in the reciprocal formulation.

## Originality

PASS, qualified as to the best of our knowledge.

The older source of the \(F\)-perfect equation, Cai--Chen--Zhang, was inspected in its full arXiv version. It defines \(F\)-perfect numbers and classifies solutions of \(\sigma_2(n)-n^2=3n\), but does not study deletion of one proper-divisor square.

The full 2025 INTEGERS paper that introduces near \(F\)-perfect and \([k,\ell]\)-near-perfect numbers was inspected. It proves numerous family-specific nonexistence results: in particular prime powers, \(2^a p\), \(2p^a\), \(2^a p^b\) for even \(b\), selected odd two-prime forms, and squarefree odd forms. Its concluding section says that further work may characterize \([k,\ell]\)-near/deficient-perfect numbers with more than two prime factors. No global nonexistence theorem for near \(F\)-perfect numbers is stated there.

The 2023 conference abstract by the same line of work was checked as a precursor. Current-status searches used the exact equation and the terms “near F-perfect”, “near F_k-perfect”, “[2,3]-near-perfect”, “redundant divisor”, and synonymous square-divisor deletion descriptions; searches also targeted stronger nonexistence statements and later work by the authors. No source giving an equivalent or stronger theorem was located. The SCOPE archive was searched immediately before publication for the same object and claim family, with no overlap found.

Residual originality risk remains because the proof is elementary and an equivalent observation could be buried in older divisor-sum literature under terminology unrelated to near \(F\)-perfect numbers. No concrete source pointing to such coverage was found. The most relevant primary sources were accessible and inspected; no inaccessible paper was identified whose known statement creates a material coverage concern.

## Value

PASS.

The result settles the entire existence problem for the newly defined \([2,3]\)-near-perfect class, rather than another bounded or fixed-factor slice. It subsumes the prior near-\(F\) nonexistence theorems for special factorization patterns and replaces many case-specific calculations by a short reciprocal-divisor obstruction. The same identity also yields the useful general bound \(n\le16\ell\) for every \([2,\ell]\)-near-perfect number divisible by four.

## Limitations

The theorem is only for the square-sum exponent \(k=2\) with \(\ell=3\); it does not assert nonexistence for general near \(F_k\)-perfect or \([k,\ell]\)-near-perfect numbers. The bibliographic originality assessment is to the best of our knowledge, not an exhaustive proof that no differently named older source contains the same elementary argument.
