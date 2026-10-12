# A 106-symbol quaternary orientable cycle of order four

## Finding
There exists a cyclic sequence over the four-symbol alphabet \(\{0,1,2,3\}\) whose \(106\) length-four cyclic windows are nonpalindromic and pairwise distinct even after identifying each window with its reversal. Consequently the maximum period of a quaternary orientable sequence of order four satisfies
\[
M_4(4)\ge 106.
\]
The explicit complete witness, given without any cyclic padding, is in `witness.txt`. This improves the published construction period \(88\) in Mitchell and Wild (2025, Table 7) by \(18\) and leaves a gap of at most \(6\) to their upper bound \(112\).

## Assumptions and scope
A *cyclic word* of length \(L\) is an indexed tuple \((s_0,\ldots,s_{L-1})\) with every index taken modulo \(L\). At position \(i\), the order-four factor is the word \(f_i=s_i s_{i+1}s_{i+2}s_{i+3}\). Its reversal is \(f_i^R=s_{i+3}s_{i+2}s_{i+1}s_i\). The word is *orientable of order four* if each \(f_i\) differs from every \(f_j^R\), including when \(i=j\). Its maximum possible length over an alphabet of size four is denoted \(M_4(4)\).

The statement is an explicit finite existence theorem over precisely four symbols and windows of length four. It is not a theorem about arbitrary orders, alphabets, or maximality.

## Proof
Read the string in `witness.txt` cyclically; it has precisely \(106\) symbols, all in \(\{0,1,2,3\}\). Form the \(106\) length-four cyclic factors \(f_i\), one for each \(0\le i<106\). The checkers exhaustively establish both: (i) \(f_i\ne f_i^R\) for all indices, and (ii) \(f_i\notin\{f_j,f_j^R\}\) for each pair \(0\le j<i<106\). This is a finite exhaustive check of exactly \(106\) individual nonpalindrome conditions and \(\binom{106}{2}=5565\) unordered pairs, with no unexamined positions or boundary cases because indexing is modular.

For an additional independent accounting check, one verifier enumerates every word of length four on the alphabet. There are \(4^4=256\) words, of which \(4^2=16\) are palindromes, so the nonpalindromic words fall into exactly \((256-16)/2=120\) reversal-pair orbits. The witness occupies exactly \(106\) distinct such orbits. The other \(14\) orbits are recorded in `missing_orbits.txt`. Thus this word meets the definition and proves \(M_4(4)\ge106\).

## Verification
Place `witness.txt`, `verify.py`, and `verify.c` in the same folder. Execute `python3 verify.py` to enumerate all cyclic windows, reversal classes, and omitted orbits. Independently execute `cc -std=c11 -O2 -Wall -Wextra -pedantic -o verify_c verify.c` followed by `./verify_c` from that folder; this compares every pair of cyclic windows literally and checks the absence of palindromic factors. The results are `VERIFY_OK period=106 windows=106 reversal_orbits=106 unused_orbits=14` and `VERIFY_OK cyclic_length=106 all_5565_factor_pairs_distinct_under_reversal`, respectively. The source files contain the full checks and have no external dependencies beyond standard Python and C toolchains.

## Relationship to prior work
Gabrić and Sawada (2024), *Constructing k-ary Orientable Sequences with Asymptotically Optimal Length*, provide asymptotically optimal constructions for arbitrary alphabets. Alhakim and collaborators (2024), *Orientable sequences over non-binary alphabets*, study the nonbinary setting and derive a general upper bound. Mitchell and Wild (2025), *New orientable sequences*, develop stronger bounds and constructions; their **Table 7** explicitly lists a largest then-known period \(88\) and upper bound \(112\) for four symbols and order four. Their construction for this parameter has period \(88\). The present explicit \(106\)-symbol witness exceeds that documented value, but does not improve the proven upper bound.

## Limitations
Only the lower bound \(M_4(4)\ge106\) is proved; no claim is made that \(106\) is the maximum. The comparison to the 2025 literature records the previously *documented* maximum known construction; an independently discovered or unindexed longer cycle would take priority. The exhaustive check proves one finite witness, not an infinite family or an asymptotic statement. The scientific assessment is not an independent audit.

## References
- D. Gabrić and J. Sawada, *Constructing k-ary Orientable Sequences with Asymptotically Optimal Length*, arXiv:2407.07029v1, first submitted 2024-07-09. https://arxiv.org/abs/2407.07029
- A. Alhakim et al., *Orientable sequences over non-binary alphabets*, arXiv:2407.14866v1, first submitted 2024-07-20. https://arxiv.org/abs/2407.14866
- C. J. Mitchell and P. R. Wild, *New orientable sequences*, arXiv:2507.02526v1, first submitted 2025-07-03, especially Table 7. https://arxiv.org/html/2507.02526v1
