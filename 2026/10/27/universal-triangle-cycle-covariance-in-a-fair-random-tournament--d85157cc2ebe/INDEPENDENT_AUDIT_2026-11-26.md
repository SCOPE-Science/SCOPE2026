# Independent mathematical audit

## correctness

PASS

An unconditioned triple is cyclic with probability 1/4; fixing one arc does not change this, and fixing a directed two-edge path increases the probability to 1/2. A specified k-cycle with k >= 4 fixes two arcs on exactly its k successive triples (distinct even for k = 4) and fixes at most one on every other triple. For k = 3 the one fully fixed triple gains 3/4 instead. The conditional gain is therefore k/4, including when n = k. Each of the (n)_k/k oriented candidates, modulo rotation but not reversal, has probability 2^(-k); summing its indicator covariance gives (n)_k/(4*2^k). Since C_3 = T, Var(T) = 3*binom(n,3)/16, and Cauchy–Schwarz yields the claimed relative-variance bound, its k = 3 equality, and the stated Hamiltonian specialization. The supplied verifier was inspected, not executed or relied on for the proof.

## originality

PASS

Pass is for the uniform exact finite covariance and conditional-response identity for all cycle lengths with its uniform variance consequence, not for the already documented k = 4 specialization, the k = 3 triangle variance, or asymptotic Hamiltonian fluctuations. The strongest exact overlap recovered is confined to three- and four-cycle counts; the broader inspected results do not supply the uniform law. This is a best-of-knowledge assessment.

## value

PASS

This computes a uniform finite cross-statistic of natural dependent cycle counts: it identifies exactly how a prescribed long cycle biases triangles, and gives a computable projection-based variance floor at every length without enumerating overlaps of two long cycles. The Hamiltonian specialization gives a relative-variance floor of order 1/n. The value is in the uniform calculation, not the known four-cycle entry or the routine Cauchy–Schwarz step alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
