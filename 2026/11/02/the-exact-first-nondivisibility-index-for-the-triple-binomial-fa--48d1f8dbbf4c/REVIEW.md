# Self-review

**Correctness — PASS.** The circular-block action proves the indispensable global factor \(n\) in the adjacent binomial coefficient. The exact adjacent-binomial identity converts the target to divisibility by \(3n\), and Kummer's theorem proves that only indices with \(3\mid bn+1\) can fail. Lucas digit dominance then gives the sharp lower bound and a matching witness for every valuation depth. The cyclic action has no stabilizer because \(\gcd(3n-1,n)=1\). The base-three carry and digit claims, including valuation depth one, were checked separately. Exact-integer reproducibility checks agree on the tested range. No finite computation is used to infer the infinite assertion.

**Originality — PASS, with residual risk.** Sun [1] defines this same invariant and gives examples and the universal \(\gcd\)-corrected divisor; the displayed statements do not fix the first failing index. Guo–Krattenthaler [2] proves infinitely many failures and a general upper bound, but no exact formula in the \(a=3\) family. Comparisons of actual statements, prime-power conditions and Lucas arguments did not find the sharp three-adic valuation law. Search and accessible document reading cannot exclude an unlocated equivalent earlier derivation.

**Mathematical value — PASS.** The sharp answer settles an entire natural one-parameter slice of a published least-failure invariant, rather than an arbitrary isolated integer case. The unbounded family \(f(3,3^s-2)=(3^s+1)/2\) makes the arithmetic structure and limitations of known generic upper bounds explicit. This is a complete classification motivated by the original published object.

The computation is finite; the universal claim relies on the proof. The result does not give every later failing index or solve arbitrary first parameter. Earlier independent review is not claimed.

Self-review: passed. Independent audit: not yet performed.
