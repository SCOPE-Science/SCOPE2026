# Scientific assessment: two-prime-support divisor-sum classification

## Correctness — PASS
The theorem quantifies over every positive integer with at most two **distinct** prime factors. Parity eliminates even integers; the positive integer \(1\) and all odd prime powers are excluded explicitly. Multiplicative bounds exclude two-prime supports not containing \(3\). The remaining identity
\[
(3^{a+1}-q)(q^b-1)=4(q-1)
\]
is equivalent to the original equation, without division by zero because \(q\ge5\). Its geometric-series quotient forces \(b=1\), then \(q=3^{a+1}-4\). Substitution proves the converse. All exponents are unrestricted. Exact finite verification through \(10^6\) is supplementary rather than a substitute for the universal argument. Principal risk: none identified in the elementary algebra; the range of exponents yielding prime \(q\) remains unknown.

## Originality — PASS
OEIS A063906 already records the **sufficient** prime family and its early values; that inclusion is expressly not claimed as new. The new statement is an if-and-only-if classification of all solutions with \(\omega(m)\le2\). Guy–Shanks additionally needs primality of the neighboring integer; Bege–Fogarasi provides an illustrative finite table; Benito treats equal divisor sums at consecutive arguments. The closest published two-almost-prime result imposes \(\Omega\le2\) on **both neighbors**, a strictly different and narrower condition. The fully inspected texts and targeted database and semantic searches did not yield an unrestricted converse for \(\omega(m)\le2\). Residual risk: an unindexed prior proof of this elementary necessity argument could exist; absence in searched literature is not a proof of global novelty.

## Value — PASS
The equation is independently recorded and studied as a generalized perfect-number problem. The result completes the first nonempty distinct-prime-support layer with no size or exponent bound and shows all other prime-support shapes are impossible in that layer. The known sufficient construction does not itself supply this exclusion. For example the certified solution \(36472996363223648799\) has composite neighbor \((m-1)/2\), so the classification genuinely exceeds the special consecutive-divisor-sum construction. It makes no claim about three-or-more-support solutions or infinitude of admissible exponents.

Self-review: passed. Independent audit: not yet performed.
