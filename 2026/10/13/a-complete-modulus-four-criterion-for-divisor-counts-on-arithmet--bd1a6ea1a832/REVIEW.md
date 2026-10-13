# Review: a complete modulus-four criterion for divisor counts on arithmetic progressions

**Correctness — PASS.** For each \(p^a\Vert A\), the inequality \(\nu_p(B)<a\) fixes the valuation in every term. Their divisor-count factors give a forced product \(J\). When \(J\) is odd, the explicitly defined square \(E\), CRT and Dirichlet primes construct a term \(Eq\equiv B\pmod A\) having exactly two modulo-four divisors. When \(J\equiv2\pmod4\), the only possible nonzero divisor-count residue is caused by \(pt^2\); the exact quadratic congruence is both necessary and sufficient, including its fixed exponent \(1\pmod4\). The application counts exactly the \(p\)-adic valuation-one residue classes and resolves the remaining square condition modulo \(8\) and \(p\). The standard-library verifier checks numerous finite instances, not the infinite theorem.

**Originality — PASS with explicit residual risk.** Merca's 2022 full-text introduction states the \(\mathcal B_{1,p}\) cardinality as a conjecture depending on cubefreeness, and Theorem 3 proves only \(p=3,5\). The general progression criterion and the \(p\bmod8\) cardinality are stronger than those particular results. The conjecture predicts \(54\) at \(p=109\) because \(27\mid108\), while the theorem proves \(108\). A separately recorded parameter result for \(r\in\{3,5,7\}\) is already covered and is not a distinct claimed contribution. Related results on totient congruences and divisibility of sums of divisors address different arithmetic functions, and do not imply this theorem. An unindexed equivalent classification remains possible.

**Value — PASS.** The theorem gives a finite necessary-and-sufficient test for all mod-four divisor congruences on arbitrary arithmetic progressions; it also resolves and corrects a specifically motivated 2022 prime-square counting conjecture. The quadratic-residue obstruction is structural and not an arbitrary finite parameter census.

Scientific limitations: only modulus four and linear progressions. A self-contained unconditional proof is present; the checker is supporting regression only.

Self-review: passed. Independent audit: not yet performed.
