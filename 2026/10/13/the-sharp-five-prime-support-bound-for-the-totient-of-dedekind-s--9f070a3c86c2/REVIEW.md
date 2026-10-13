# Review of the five-prime-support Dedekind–totient bound

## Correctness — PASS

The proof handles all integers \(n\ge3\) with \(\omega(n)\le5\) via four exhaustive cases. For an even mixed-support integer, \(6\mid\psi(n)\) forces the \(1/3\) totient ratio, and the first-five-primes product gives \(1152/385\); both equality requirements together give exactly \(2^a3^b\cdot5\cdot7\cdot11\) for positive exponents \(a,b\). For an odd integer, splitting on whether \(3\mid\psi(n)\) gives the strict upper bounds \(512/715\) and \(20480/22971\). Pure powers of two have ratio \(1/2\) in the stated range. All comparisons use exact rational identities and cover unbounded prime exponents. The explicit \(39270\) counterexample establishes the sharp support cutoff. The verifier independently checks bounded inputs, but the proof—not the finite check—establishes the universal result.

## Originality — PASS, with residual risk

The most relevant complete published source is Sándor's 2005 paper, which proves the inequality for even \(\omega(n)\le2\) and odd \(\omega(n)\le4\), and notes the sufficient regime \(\psi(n)\le2n\). The new equality case \(n=2310\) is outside that sufficient regime since \(\psi(2310)/2310=1152/385>2\). The same work knows the six-prime counterexample \(39270\), and OEIS A196200 tabulates violations, but neither contains the unrestricted \(\omega(n)\le5\) sharp \(384/385\) bound. The 2016 Sándor note has a different subject. Exact-alias and broader-implication searches in published records found no covering statement. A prior unindexed proof remains possible; search absence is not mathematical proof of novelty.

## Value — PASS

The bound supplies an exact natural invariant—the maximal normalized \(\varphi\circ\psi\) ratio on the infinite five-prime-support layer—together with every extremizer. It also closes the precise support gap between the partial results in Sándor's paper and its six-prime counterexamples. Its value is a structural sharp classification, not a finite computational record or a claim about the unrestricted inequality.

## Limitations and closest sources

The theorem does not apply to integers with six or more distinct prime factors, does not determine the frequency of violations, and the finite verifier alone does not establish any unbounded assertion. Closest literature: J. Sándor, *JIPAM* 6(3), Art. 73 (2005), Theorem 3.9, Remark 3.10, Remark 3.26; OEIS A196200 (dated 2012-12-21); J. Sándor, *NNTDM* 22(1), 5–7 (2016).

Self-review: passed. Independent audit: not yet performed.
