# A six-symbol orientable cycle of order four and period 603
## Finding
There is a cyclic word on the alphabet \(\{0,1,2,3,4,5\}\) of period \(603\) in which every circular four-symbol window is nonpalindromic and no two circular four-symbol windows are reversals of each other. Equivalently, if \(M_6(4)\) is the maximum period of an orientable six-symbol sequence of order four, then
\[
M_6(4)\ge 603.
\]
A published 2026 table lists the longest then-known example as \(552\) and an upper bound of \(612\). The exhibited example therefore increases that recorded lower bound by \(51\), leaving a gap of \(9\) below the published upper bound. We do not claim that \(603\) is optimal.

## Assumptions and scope
A cyclic word \(s=(s_0,\ldots,s_{m-1})\) is extended periodically using subscripts modulo \(m\). Its circular factor of length four beginning at \(i\) is \(F_i=(s_i,s_{i+1},s_{i+2},s_{i+3})\). It is *orientable of order four* if, for every ordered pair \(0\le i,j<m\), we have \(F_i\ne F_j^{\mathrm{rev}}\), where \(\mathrm{rev}\) reverses the four entries. This includes \(i=j\), so palindromic factors are excluded. The established orientable-sequence convention includes two requirements: ordinary cyclic-window uniqueness and exclusion of reversed window pairs. Both requirements are checked independently below.

The certificate `witness.txt` is a single row of exactly \(603\) symbols drawn from \(\{0,1,2,3,4,5\}\). Circular wraparound is essential: the last three windows may cross the end of the written row.

## Proof
Let \(s\) be the word in `witness.txt`, with positions indexed by \(0,\ldots,602\). The following finite assertions are established by the complete, deterministic verifier `verify.py`, which is also given in full:

1. The word has exactly \(603\) characters, and every character lies in the specified six-symbol alphabet.
2. The set \(\{F_i:0\le i<603\}\) of cyclic four-windows has \(603\) elements.
3. For every \(0\le i,j<603\), the directly formed \(F_i\) is different from the directly formed reversed factor \(F_j^{\mathrm{rev}}\). The program executes all \(603^2=363609\) ordered comparisons, not a sample.
4. The length-four palindromes (there are \(6^2=36\)) are absent. The forward and backward window sets each have \(603\) elements and are disjoint.

The verification uses exact character comparisons and finite exhaustive loops; it makes no floating-point assumptions and invokes no external solver. The first two properties show that \(s\) is an order-four window sequence. The third and fourth show orientability. Distinct windows also imply that the least period of \(s\) is \(603\), because any shorter period would force repeated windows. Thus \(s\) is an orientable sequence of order four and period \(603\), as claimed.

As a consistency check, the \(6^4=1296\) possible four-letter strings comprise \(36\) palindromes and \(630\) nonpalindromic reversal pairs. This witness represents \(603\) distinct reversal pairs, leaving \(27\) unused.

## Verification
Place `verify.py` and `witness.txt` in one directory and run `python3 verify.py`. A successful run prints

```
VERIFY_OK period=603 distinct_four_windows=603 distinct_reverse_windows=603 partitioned_words=1242 omitted_reversal_pairs=27
```

The verifier also checks all possible periods shorter than \(603\), although window uniqueness already proves primitivity. The certificate is a self-contained, finite existence proof; the software used to discover it is not required for its validation.

## Relationship to prior work
Gabrić and Sawada [1] developed general constructions for \(k\)-ary orientable sequences and explained their position-sensing motivation. Alhakim, Mitchell, Szmidt, and Wild [2] established general nonbinary constructions and upper-bound methods. Mitchell and Wild [3, Table 7] listed the best known order-four example on six letters as period \(534\) with upper bound \(612\). Their revised 2026 paper [4, Table 4] improves the reported order-four six-letter lower bound to \(552\), while retaining upper bound \(612\). The present explicit finite witness provides the stronger lower bound \(603\), without claiming a new universal upper bound.

## Limitations
The assertion is existential and applies only to the alphabet size six and window order four. It does not classify all extremal words or prove that \(603\) is the maximum possible period. The published upper bound of \(612\) is quoted from [3,4] rather than independently reproved. The absence of an indexed equivalent construction is not a mathematical priority guarantee; an unindexed or later source could contain the same 603-symbol construction.

## References
[1] D. Gabrić and J. Sawada, *Constructing k-ary Orientable Sequences with Asymptotically Optimal Length*, arXiv:2407.07029v1 (9 July 2024), https://arxiv.org/abs/2407.07029.

[2] A. Alhakim, C. J. Mitchell, J. Szmidt and P. R. Wild, *Orientable sequences over non-binary alphabets*, arXiv:2407.14866v1 (20 July 2024), https://arxiv.org/abs/2407.14866.

[3] C. J. Mitchell and P. R. Wild, *New orientable sequences*, arXiv:2507.02526v1 (3 July 2025), https://arxiv.org/abs/2507.02526.

[4] C. J. Mitchell and P. R. Wild, *Constructing orientable and negative orientable sequences with asymptotically optimal period*, arXiv:2603.18646v2 (14 August 2026), https://arxiv.org/abs/2603.18646.
