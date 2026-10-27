# Scientific review

## Correctness — PASS
The first-appearance threshold follows exactly from the greedy embedding of binary words in a block-alternating host: only an adjacent `01` can be consumed within one block. For a repeated root, there are \(q\) internal copies of each edge and \(q-1\) closing edges. The weighted two-state transfer matrix therefore enumerates every root exactly once; matrix inversion, Fibonacci/Lucas coefficient extraction and cumulative counting give the stated formulas for all parameters. The standalone verifier checked 133 independent direct-enumeration parameter pairs and additionally tested root-length coefficients and jump sizes. Its finite evidence supplements but does not replace the symbolic proof.

## Originality — PASS with residual risk
The closest full-text primary research is Inoue et al. (2018), which optimizes lengths of common square subsequences, and Lai et al. (2022), which studies adjacent letter-block duplication. Neither gives the exact number of distinct unrestricted roots of concatenated powers occurring in an alternating host, nor the residue-dependent Fibonacci–Lucas law or root-length bivariate generating function. The older Kosowski (2004) source is an optimization result according to its abstract, but its full text could not be accessed. Searches using the aliases *tandem scattered subsequence*, *square subsequence*, *repeated subsequence*, *power subsequence*, *periodic binary host*, and *alternating word* identified no equivalent formula. Absence from these searches is not proof of priority; obscure or unindexed specializations remain a risk.

## Mathematical value — PASS
A full exact enumeration complements optimization results for tandem scattered subsequences. Its two-residue support and the fact that the host-size jump magnitudes do not depend on the repetition exponent are structural, not merely isolated small instances. The marked rational series also resolves the number of roots of each length, which is useful whenever root complexity or power length is constrained. These properties make the infinite-family result meaningful independently of possible extensions to arbitrary hosts.

## Limits
The theorem concerns only alternating binary hosts and **concatenated**, not shuffle, powers. External independent validation has not occurred.

Self-review: passed. Independent audit: not yet performed.
