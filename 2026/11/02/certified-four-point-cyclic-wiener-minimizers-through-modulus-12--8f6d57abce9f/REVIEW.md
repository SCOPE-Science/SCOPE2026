# Scientific review — four-point cyclic Wiener minimizers through modulus 128

## Correctness — PASS
The claim is explicitly finite: every \(8\le N\le128\), with exactly four distinct residues and zero-frequency removed. The proof reduces by translation to every anchored triple, proves symmetry of the predicted minimizers, derives candidate values, and rigorously encloses each Fourier magnitude using rational Machin-series and Taylor bounds. The exhaustive comparison is an exact integer inequality with a strict analytic error budget. Four disjoint successful verifier runs cover all 10,667,965 anchored sets and all 121 moduli. The integer-root and overflow bounds were checked in the actual standalone program. The finite computation is a complete certificate only because the program enumerates all anchored subsets; merely testing examples would not establish the result.

## Originality — PASS relative to inspected sources
The June 2026 Fourier-ratio framework (arXiv:2606.15475) and October 22 graph-energy study (arXiv:2610.31807) do not give the statement. The October 26 follow-up (arXiv:2610.36276), in Theorem 2.3, already proves the subgroup-coset case \(4\mid N\), and in Question 9.1 explicitly leaves four-element minimizers open generally. Its computed \(N=17\) local-search obstruction is not an exhaustive global minimizer classification across 121 moduli. Indexed findings concerning four consecutive frequencies calculate the norm of a fixed projection, not the least norm over all four-point indicators. Unindexed prior tables and stronger infinite theorems are residual risks; no claim of global novelty beyond the inspected literature is made.

## Value — PASS
This is a nontrivial complete cutoff in the first unsolved cardinality of a natural Fourier-compressibility minimization: for all 121 consecutive moduli it exhibits three distinct arithmetic extremizer mechanisms and certifies their exclusivity across more than ten million Fourier-support configurations. It makes exact, independently reproducible predictions for the bipartite graph-labeling problem in that finite regime and supplies evidence toward, but does not settle, the unbounded four-element classification. The case divisible by four is credited to known subgroup results and is included to make the finite statement complete.

## Limitations and residual risks
The cutoff is 128, not infinity. The certificate depends on correct execution of the included exact-integer code and verified elementary error bounds. It is not independent formal certification. The closest preprint appeared after the source-week anchor; it is used only to compare originality, not as the earliest motivating publication. Earlier equivalent enumerations might exist without being indexed.

Self-review: passed. Independent audit: not yet performed.
