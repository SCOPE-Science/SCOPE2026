# Self-review

## Correctness — PASS

For every odd prime \(p\) and every positive integer \(n\), the corrected binomial quotient is integer by Lucas's congruence modulo \(p\), and its parity is exactly the binary-submask condition from Lucas modulo two. The central new digit-deposition identity is proved by fixing each binary digit of Rowland's parameter and summing its exact integer coefficient; it proves equality of the original printed parameter set with the submask residue set, including its cardinality. No inference from finitely many checked cases is needed. The included verifier reconstructs the original floor sums for 429 odd primes through 3000 and independently checks 11,816 exact integer-binomial cases across 44 primes.

## Originality — PASS, residual risks

E. Rowland, *Two binomial coefficient conjectures*, arXiv:1102.1464v1 (7 February 2011), Section 3, Conjecture 2, asks exactly for the unusual floor-sum residue parametrization. Its proved preceding proposition controls fractional parts but does **not** equate that parametrization with the elementary Lucas parity criterion. Rowland explicitly describes the parametrization as unproved and its membership test as unclear. This result proves the missing digit-deposition equivalence and so proves the printed conjecture; the classical Lucas criterion and Rowland's preceding proposition are acknowledged as prior inputs, not original discoveries.

Rowland's earlier arXiv:1001.1783 (2010) counts nonzero entries in Pascal's triangle modulo prime powers, rather than characterizing this \(\binom{n}{2p}/n\) exception set. The Lu–Tsai periodicity theorem quoted in Rowland establishes periodicity, not Rowland's printed digit parametrization. Searches for a prior resolution and close research records did not reveal the same statement, but this is not a proof of global uniqueness. An unindexed resolution or a stronger unlocated theorem remains a residual originality risk.

## Mathematical value — PASS

The claim gives a self-contained proof of an explicitly published, infinite-parameter number-theory conjecture, and converts an obscure floor-sum existential test into a single binary mask comparison. It also identifies the exact number \(2^{L-s_2(2p)}\) of exceptional residue classes per binary period. These answer a motivated question about binomial congruences, not an arbitrary numerical slice.

## Scope and remaining limitations

The proof assumes \(p\) an odd prime and does not address Rowland's unrelated Conjecture 1, composite \(p\), or an analogous conjecture for arbitrary products of distinct primes. The original 2011 source predates the archival cutoff; no source date from later revisions is substituted. Computational checks support but do not establish the infinite proof. Independent examination of the new theorem and a global literature audit remain to be done.

Self-review: passed. Independent audit: not yet performed.
