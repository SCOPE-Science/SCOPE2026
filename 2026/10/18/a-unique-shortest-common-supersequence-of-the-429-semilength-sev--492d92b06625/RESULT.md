# A unique shortest common supersequence of the 429 semilength-seven Dyck words

## Finding
Let \(D_7\) consist of all balanced parentheses words of length \(14\) with seven opening and seven closing symbols, whose every prefix has at least as many openings as closings. Then \(|D_7|=429\). Among all linear words over the same two-symbol alphabet, with no balance restriction on the host, the shortest containing every element of \(D_7\) as a scattered subsequence has length \(22\). There is exactly one such minimum host:

`(()(()()()()()()())())`

Uniqueness is for literal, indexed linear strings, without identifying rotation, reversal, or alphabet exchange.

## Assumptions and scope
A word \(u\) is a subsequence of \(w\) when strictly increasing positions in \(w\) spell \(u\). The parenthesis alphabet has exactly two distinct symbols. All \(429\) Dyck targets are required; the covering host itself may be non-Dyck and may repeat symbols arbitrarily. This is an exact finite claim for semilength \(7\) only, not an asymptotic formula or claim at other semilengths. The Catalan recurrence, or the recursive generator in the attached program, gives \(|D_7|=\frac{1}{8}\binom{14}{7}=429\).

## Proof
The proof is a self-contained finite exhaustion; its complete C++ program is supplied as `verify_exhaustive.cpp`. First, define `gen(a,b,mask)` to append an opening parenthesis if \(a<7\), or a closing parenthesis if \(b<a\), stopping when \(a+b=14\); storing a closing at bit position \(a+b\) in a 14-bit unsigned integer. This recursion visits every member of \(D_7\) exactly once: every generated path is a Dyck prefix at all times, and every Dyck word has a unique choice sequence. It generates exactly \(429\) distinct masks.

For a fixed target \(t\), the function `covers(host,L,t,7)` scans host positions \(0,\ldots,L-1\) from left to right and advances target position \(j\) when the next required symbol matches. Its return value \(j=14\) is equivalent to subsequence containment: the greedy earliest match exists whenever any embedding exists, proved inductively because selecting the earliest available match cannot remove a future possible embedding.

For each \(L\in\{21,22\}\), the program loops through **every** one of the \(2^L\) binary host masks \(0,\ldots,2^L-1\), testing subsequence containment of the two extremal Dyck targets first as an optional computational filter and then testing every remaining Dyck target. The filter is sound because those two are members of \(D_7\); no host can be counted as universal without passing *all* \(429\) target tests. The certified output is:

```
L=21 prefilter_pass=10824 universal=0 witness=
L=22 prefilter_pass=70158 universal=1 witness=(()(()()()()()()())())
```

The mask loop bounds exhaust all \(2^{21}=2097152\) length-21 hosts and all \(2^{22}=4194304\) length-22 hosts. Thus no length-21 universal host exists, and there is exactly one length-22 universal host. Any shorter universal host could be extended by arbitrarily appended symbols to a length-21 universal host, since subsequence containment is monotone under insertion. Such a host therefore cannot exist. This proves the minimum and uniqueness.

A second independent algorithm in `verify_bfs.cpp` enumerates the length-\(14\) Dyck targets as ordinary strings and performs a breadth-first search over vectors of longest greedily embedded target-prefix lengths. Each input symbol advances precisely the target entries whose next symbol matches. The greedy-prefix lemma above shows state sufficiency. State merging preserves the number of distinct histories of minimum depth; its search produces the same unique 22-letter host.

## Verification
With a C++17 compiler, from a directory containing both attached source files:

```
g++ -O3 -std=c++17 verify_exhaustive.cpp -o verify_exhaustive
./verify_exhaustive
g++ -O3 -std=c++17 verify_bfs.cpp -o verify_bfs
./verify_bfs 7 3000000
```

The first program outputs exactly the two lines above and terminates with nonzero status if the exhaustive counts are not \(0\) and \(1\). The second prints `n=7 dyck=429 min=22 optimal_host_words=1 reachable_states=1690893 expanded=919290` and the same witness. The direct full-host enumeration is the primary exhaustive certificate; the BFS cross-check uses a different search representation and accounts for state multiplicities. Both programs were compiled and run from the delivered source bytes prior to inclusion. Source inspection remains necessary: a numerical log alone would not prove exhaustiveness.

## Relationship to prior work
The general shortest common supersequence problem is classical; Clifford, Gotthilf, Lewenstein and Popa (2010, arXiv:1004.0424) study restricted supersequences under a fixed multiset of available symbols. Their full text describes general hardness and approximability, not the exact unrestricted-host, all-Dyck-semilength-seven family. In particular, a general solution method does not itself imply the numerical optimum and complete uniqueness census without carrying out the associated computation. Other published results concerning all-binary-subsequence universality and Dyck shift entropy concern different target collections and invariants. Literature and published-record searches did not identify a theorem or table containing the present \(22\)/unique exact pair; absence from a search is not a proof of novelty.

## Limitations
The claim is a finite computer-assisted classification requiring trust in the provided, human-auditable exhaustive C++ loops and the execution environment; no independent external audit or machine-checked formal proof is asserted. Generalization beyond semilength \(7\) is not proved. An earlier source could have enumerated the same value under a different name; comprehensive indexing and accessible full-text coverage cannot be guaranteed.

## References
1. R. Clifford, Z. Gotthilf, M. Lewenstein and A. Popa, *Restricted Common Superstring and Restricted Common Supersequence*, arXiv:1004.0424, first public 2010-04-03, https://arxiv.org/html/1004.0424v2 (full text inspected, Sections 1 and 3).
2. OEIS A000108 (Catalan numbers), https://oeis.org/A000108 (standard cardinality reference, not a shortest-supersequence table).
3. `verify_exhaustive.cpp` and `verify_bfs.cpp` (included reproducibility sources for the claim).
