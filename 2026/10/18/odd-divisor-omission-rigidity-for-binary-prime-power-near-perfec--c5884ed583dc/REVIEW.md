# Scientific review

## Correctness — PASS
The divisor-sum identity \(\sigma(2^kp^e)-2\cdot2^kp^e=(2^{k+1}-p)Q-1\), where \(Q=1+\cdots+p^{e-1}\), follows by direct factorization and \(p^e=(p-1)Q+1\). For a subset of odd divisors, the two endpoint exponents contribute at most two copies of the residue one modulo \(Q\). The resulting integer \(R\) is a positive multiple of \(Q\) in \([1,Q+2]\), so it equals \(Q\). Modulo the odd prime \(p\), the endpoint count is zero; all internal powers must then be selected. The identity forces the Mersenne equality, and the converse is direct. This reasoning holds uniformly over all quantified parameters. Recomputations across \(1{,}680\) parameter triples checked \(243{,}840\) candidate odd-only subsets. The finite checks do not substitute for the proof.

## Originality — PASS on inspected evidence
The originating 2023/2024 work treats exactly two deleted divisors with odd prime exponent at most two. The later 2025/2026 completion treats exactly two deleted divisors for every larger odd prime exponent and proves only the exponent-three Mersenne-cube solution in that case. Neither classifies all odd-only deletion subsets of arbitrary size; the present theorem makes new statements for every exponent \(e\ge4\). Related indexed findings about single-divisor near-perfect numbers, squarefree three-prime two-near-perfect numbers, deficient-perfect numbers, and strongly pseudoperfect numbers have different hypotheses and do not imply the all-odd arbitrary-cardinality classification. The Adajar thesis (2016) could not be fully inspected, and an equivalent result in unindexed work remains an originality risk.

## Mathematical value — PASS
Near-perfect numbers are naturally stratified by the number and arithmetic type of omitted divisors. In the two-prime-support family, odd omissions are the canonical divisor layer supplied by the odd prime power. The theorem classifies the entire set-valued odd-only omission spectrum, proving uniqueness and forcing the Mersenne condition simultaneously for every exponent; the number of such omissions grows without bound even on a fixed prime support. This is a structural classification at the previously untreated higher-cardinality boundary, not a finite instance or a mere substitution in an existing two-deletion theorem.

## Scope and residual limitations
No classification of mixed-parity deletion sets or of the unrestricted minimum omission count follows. Existing open questions about infinitely many Mersenne primes are unaffected. The inspected primary sources establish the respective two-deletion statements but do not exclude possible equivalent results elsewhere. The 2016 thesis is a specific unresolved reference.

Self-review: passed. Independent audit: not yet performed.
