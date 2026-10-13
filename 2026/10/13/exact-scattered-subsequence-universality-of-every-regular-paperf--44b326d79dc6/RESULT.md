# Exact scattered-subsequence universality of every regular-paperfolding prefix

## Finding

Let \(p_1p_2\cdots\) be the binary regular paperfolding word normalized by
\(p_n=0\) if the odd part of \(n\) is congruent to \(1\pmod 4\), and
\(p_n=1\) if it is congruent to \(3\pmod4\). For \(N\ge0\), let \(U(N)\) be the
largest \(k\) such that **every** binary word of length \(k\) is an
order-preserving (not necessarily contiguous) subsequence of
\(p_1\cdots p_N\), with \(U(0)=0\). Define the bookkeeping value \(p_0=0\).

**Exact prefix theorem.** For every integer \(T\ge0\) and
\(r\in\{0,1,\ldots,7\}\),
\[
U(8T+r)=3T+
\begin{cases}
-p_T,&r=0,\\
0,&r=1,2,\\
1,&r=3,4,\\
1+(T\bmod2),&r=5,\\
2,&r=6,7.
\end{cases}
\]
Consequently, for all \(N\ge0\),
\[
-1\le U(N)-\frac{3N}{8}\le\frac18.
\]
Both bounds are attained infinitely often, and
\(U(2^m)=3\cdot2^{m-3}\) for every integer \(m\ge3\).

More precisely, put \(E(N)=8U(N)-3N\). The complete limiting distribution of
\(E(N)\) across nonnegative prefix lengths \(N\) consists of ten values:
\[
\lim_{X\to\infty}\frac1X\#\{0\le N<X:E(N)=j\}=
\begin{cases}
1/16,&j\in\{-8,-7,0,1\},\\
1/8,&j\in\{-6,-5,-4,-3,-2,-1\},\\
0,&\text{otherwise}.
\end{cases}
\]
In particular, the universality density exists and equals \(3/8\).

## Assumptions and scope

All subsequences preserve the selected letters' relative order but may skip
arbitrary positions. The ambient alphabet is always exactly \(\{0,1\}\),
even for empty or constant prefixes. The definition above fixes the
one-indexed paperfolding normalization. Complementing every letter leaves
\(U(N)\) unchanged; circular universality and the number of distinct absent
subsequences are different invariants and are not asserted here. The value
\(p_0=0\) serves only the formula at \(T=0\).

## Proof

**1. Greedy arches realize the index.** Read any finite binary word from left
to right, ending an *arch* at the earliest position at which both letters
have appeared since the preceding arch. The unconsumed suffix (the *rest*)
contains at most one distinct letter. The number of complete arches is
precisely the universality index. Indeed, if there are \(h\) arches, any
prescribed binary word of length \(h\) can be embedded by selecting its
successive letters from the successive arches. For the converse, choose from
each arch the second distinct letter that completes it. The leftmost greedy
embedding of these \(h\) choices ends exactly at the corresponding arch
endpoints. Append a letter absent from the rest (choose either letter if
the rest is empty). The resulting binary word of length \(h+1\) cannot
embed: its first \(h\) symbols, matched as early as possible, already reach
the end of the last complete arch. This is also the classical arch theorem
of Barker et al. [3], used in Schnoebelen--Veron [1].

**2. An eight-symbol block identity.** Directly from the odd-part rule,
\(p_{2n}=p_n\) for \(n\ge1\), while \(p_{4n+1}=0\) and
\(p_{4n+3}=1\) for \(n\ge0\). Thus the block in positions
\(8t+1,\ldots,8t+8\) is exactly
\[
B_t=0\,0\,1\,(t\bmod2)\,0\,1\,1\,p_{t+1}.
\]
Only four binary blocks are possible. After a complete block, the greedy
rest either has no letters or contains only \(1\)'s. Encode these two
possibilities by \(q=0\) and \(q=1\), respectively. If the next block
ends with \(z=p_{t+1}\), direct examination of its eight letters gives
\[
\begin{array}{c|cc}
 &z=0&z=1\\\hline
q=0& (3,0)&(2,1)\\
q=1& (4,0)&(3,1)
\end{array}
\]
where each entry is (number of newly completed arches, final rest flag).
This table holds for either parity of \(t\). In particular the arch
increment is exactly \(3+q-z\), and the new flag is \(z\).

Initially there are no arches and the flag is \(p_0=0\). Induction shows
that after \(T\) complete blocks the flag is \(p_T\) and the number of
arches is
\[
\sum_{t=0}^{T-1}(3+p_t-p_{t+1})=3T-p_T.
\]

**3. Partial-block calculation.** Write \(a=p_T\), and let
\(b=T\bmod2\). Applying the same greedy rule to the first
\(r=0,\ldots,7\) letters of \(B_T\), with incoming rest flag \(a\),
produces the exact number of further arches
\[
\begin{array}{c|rrrrrrrr}
r&0&1&2&3&4&5&6&7\\\hline
\text{additional arches}&0&a&a&a+1&a+1&a+1+b&a+2&a+2.
\end{array}
\]
The eighth letter is not involved in this partial calculation. Adding
\(3T-a\) and simplifying yields exactly the displayed theorem for every
\(T\) and \(r\). This is a finite symbolic case distinction derived from
the identity for all blocks, not extrapolation from finitely many prefix
lengths.

**4. Sharp discrepancy and distribution.** Substituting the formula gives
\[
E(8T+r)=
\begin{cases}
-8p_T,&r=0,\\
-3,&r=1,\\
-6,&r=2,\\
-1,&r=3,\\
-4,&r=4,\\
8(T\bmod2)-7,&r=5,\\
-2,&r=6,\\
-5,&r=7.
\end{cases}
\]
Hence \(-8\le E(N)\le1\). The minimum occurs for every
\(N=8T\) with \(p_T=1\), for example at all \(T\equiv3\pmod4\);
the maximum occurs for every \(N=8T+5\) with odd \(T\). Both
families are infinite. For \(m\ge3\), \(2^m=8T\) with
\(T=2^{m-3}\), whose odd part is \(1\), so \(p_T=0\); the dyadic formula
follows.

For the limiting frequencies, note that \(p_T=1\) has natural density
\(1/2\). One elementary proof writes
\(A(X)=\#\{1\le t\le X:p_t=1\}\) and uses the exact recurrence
\[
A(X)=A(\lfloor X/2\rfloor)+\lfloor(X+1)/4\rfloor.
\]
It follows inductively that \(A(X)=X/2+O(\log(X+2))\).
Each fixed residue \(r\bmod8\) has density \(1/8\); at \(r=0\),
the two alternatives for \(p_T\) each have conditional density \(1/2\),
and at \(r=5\) the two parities of \(T\) each have density \(1/2\).
All other residues fix one discrepancy value. This gives the ten-point
frequency law exactly, as well as \(U(N)/N\to3/8\).

## Verification

The included standalone Python 3 program `verify.py` derives symbols from
the odd-part definition. It exhaustively checks the eight symbolic
whole-block cases and all sixty-four corresponding partial-block cases;
checks the eight-symbol identity for \(0\le t<20000\); and directly runs
the greedy arch process through \(524288\) prefix positions. For every
\(0\le N\le29\), it also independently checks the defining subsequence
condition by enumerating binary target words of the prescribed length
and verifying that at least one target of the next length is absent.
Dyadic cases \(3\le m\le19\) and both sharp discrepancy extremes are tested.
The verified output is:

```text
VERIFY_OK symbolic_end_transitions=8 symbolic_partial_transitions=64 block_identity_T=0..19999 direct_prefixes_1..524288 defining_subsequence_test_N=0..29 dyadic_levels_m=3..19 discrepancy_range=-8..1 all_10_discrepancies_seen=yes
```

Reproduce using `python3 verify.py` from the directory containing this
text and the standalone program. No external packages, network data, or
unpackaged files are required. The infinite proof is Steps 1--4, not the
finite verification.

## Relationship to prior work

Schnoebelen and Veron [1] develop arch-jumping functions and subword
universality signatures, including algorithms for compressed finite words;
the equivalence between greedy arch count and universality index is prior
work. Their general tools do not state the eight-block paperfolding identity,
the closed formula for **every** paperfolding prefix, the sharp discrepancy,
or its ten-point distribution. Adamson et al. [2] investigate universality
of regular languages and counting/ranking problems for finite-automaton
inputs; those are distinct quantifiers and do not give the present exact
sequence-specific law. The present derivation supplies the special
paperfolding calculation and its asymptotic consequences rather than
claiming originality for greedy arch factorization or finite-word
universality algorithms.

## Limitations

The result is for the explicitly specified regular paperfolding coding and
ordinary subsequence universality of its initial prefixes. It does not
classify universality for all factors, arbitrary fold-instruction words,
other paperfolding codings beyond bitwise complement, or circular
universality. The finite verifier tests samples and symbolic tables; it does
not independently certify an infinite theorem. An equivalent calculation
may exist in literature not indexed by the searches described in the review.

## References

1. P. Schnoebelen and J. Veron, *On arch factorization and subword universality for words and compressed words*, arXiv:2304.11932v1, publicly posted 2023-04-24. https://arxiv.org/abs/2304.11932
2. D. Adamson, P. Fleischmann, A. Huch, T. Koß, F. Manea, and D. Nowotka, *k-Universality of Regular Languages*, arXiv:2311.10658v1, publicly posted 2023-11-17. https://arxiv.org/abs/2311.10658
3. L. Barker, P. Fleischmann, K. Harwardt, F. Manea, and D. Nowotka, *Scattered Factor-Universality of Words*, arXiv:2003.04629v1, publicly posted 2020-03-10. https://arxiv.org/abs/2003.04629
