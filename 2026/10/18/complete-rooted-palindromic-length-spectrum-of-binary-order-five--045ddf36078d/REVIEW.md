# Scientific review

## Correctness — PASS

The finite domain is exhausted twice: canonical Euler tours of the 16-vertex/32-edge binary de Bruijn graph, and all 65,536 local incoming-outgoing bijection choices. The resulting 2048 word sets agree exactly. Every one of their 65,536 linear cuts is checked by the literal-palindromic-suffix recurrence and by independently expanded odd/even palindrome centers; their answers agree case-by-case. The complete rooted and per-cycle tables are explicitly checked against exact constants. The proof explains why these procedures exhaust every case and why the dynamic programming computes a true optimum. The checker ran successfully from the deliverable package.

## Originality — PASS against inspected sources, with residual risk

Anisiu–Anisiu–Kása (arXiv:1002.2723) use de Bruijn words as generators of palindrome sets, not as a class on which to count shortest palindrome partitions. Ravsky (arXiv:1004.1278) gives worst-case length over all binary words; this does not imply the conditional rooted spectrum or any per-cycle min/max count. Frid–Puzynina–Zamboni (arXiv:1210.6179) address infinite words, Bannai et al. (arXiv:1503.04045) impose diversity of palindrome factors, and Harju–Huova–Zamboni (arXiv:1309.1886) use a different invariant based on palindromic relations. Targeted statement-level searches identified no equivalent rooted de Bruijn order-five table. Related order-five results for longest palindromic factors, BWT runs, and LZ76 parsing do not imply the shortest-partition distribution. Historical priority is not established definitively; unindexed exact computations are a residual risk.

## Mathematical value — PASS

Shortest palindrome partitions measure nonlocal asymmetry, while de Bruijn cycles fix the complete set of five-symbol factors. Their rotation sensitivity is therefore a natural invariant of universal-cycle *arrangement*, not a restatement of factor diversity. This complete order-five census (the 2048-cycle boundary before the leap to 67,108,864 order-six cycles) resolves every attainable rooted length, every best/worst-cut pair, the universal strict cut dependence, and the unique two-cycle worst-best case. It supplies exact finite benchmarks without claiming an unsupported all-order theory.

## Scope and remaining risks

The proof is exhaustive but computational; the auditable source code and two independent implementations reduce, but do not eliminate, implementation risk. No independent scientific audit or external priority certification has been performed. Results apply to minimum numbers of nonempty palindromic contiguous factors under literal reversal on a binary alphabet; they do not concern distinct-only palindrome partitions, palindromic relations, or compression bit rates.

Self-review: passed. Independent audit: not yet performed.
