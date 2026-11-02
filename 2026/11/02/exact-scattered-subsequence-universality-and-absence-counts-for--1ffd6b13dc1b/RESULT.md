# Exact scattered-subsequence universality and absence counts for Rudin–Shapiro prefixes

## Finding
Let \(r(t)\in\{0,1\}\) be the parity of the number of adjacent occurrences of \(11\) in the standard binary expansion of the nonnegative integer \(t\), equivalently
\[
r(t)=\operatorname{popcount}(t\mathbin{\&}\lfloor t/2\rfloor)\pmod 2.
\]
Let \(R_k=r(0)r(1)\cdots r(2^k-1)\), for every integer \(k\ge4\). A subsequence is *scattered*: symbols are read in strictly increasing positions, not necessarily contiguously. Let \(\iota(W)\) be the largest length such that **every** binary word of that length is a subsequence of \(W\). Let \(\operatorname{SAS}(W)\) be the set of absent binary subsequences of the shortest possible length (necessarily \(\iota(W)+1\)). Put \(e_k=1\) for even \(k\), and \(e_k=0\) for odd \(k\). Then
\[
\boxed{\iota(R_k)=5\cdot2^{k-4}-e_k,\qquad
|\operatorname{SAS}(R_k)|=2^{\,2^{k-4}-e_k}.}
\]

A stronger statement explains the unusually simple count. Define the four binary length-\(16\) blocks

| Block | Binary content |
|:--|:--|
| A | `0001001000011101` |
| B | `0001001011100010` |
| C | `1110110100011101` |
| D | `1110110111100010` |

For *every* nonempty concatenation \(W\) of \(q\ge1\) blocks from this four-element set, in any order with repetitions,
\[
\boxed{|\operatorname{SAS}(W)|=2^{\,\iota(W)-4q}.}
\]
Both displayed results concern **distinct absent words**, not the number of failed embeddings.

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\). A word is present as a scattered subsequence when there exists at least one strictly increasing embedding. All indices in the definition of \(R_k\) start at zero. The four displayed blocks are literal, not arbitrary substitutions of variable symbols. No restriction on the order of blocks is imposed in the block theorem. The specialized closed formulas are asserted only for complete power-of-two prefixes of rank \(k\ge4\).

## Proof
**1. Two-option shortest-absence recursion.** For a finite suffix \(S\), set \(p_a(S)\) to the least position of symbol \(a\), when present. Associate to option \(a\) a pair \((d_a,c_a)\): if \(a\) is absent, use \((0,1)\); otherwise let \((d_a,c_a)\) be the shortest-absent length and its number of distinct realizations for the suffix strictly *after* \(p_a(S)\). Greedy embedding at the earliest occurrence of a chosen first symbol is possible exactly when any embedding with that first symbol is possible. Consequently the shortest-absent length \(\ell(S)\) and count \(N(S)\) satisfy
\[
\ell(S)=1+\min(d_0,d_1),\qquad
N(S)=\sum_{a:d_a=\min(d_0,d_1)}c_a.
\]
When a symbol \(b\) is prepended, replace only \((d_b,c_b)\) by \((\ell(S),N(S))\); the other option is unchanged. Starting at the empty suffix, the option data are \(d_0=d_1=0\) and \(c_0=c_1=1\). Inductively \(|d_0-d_1|\le1\). Write \(\delta=d_0-d_1\in\{-1,0,+1\}\) and \(m=\min(d_0,d_1)\). At the end \(\iota(S)=m\); when \(\delta\ne0\), the shortest-absent count is the \(c_a\) belonging to the unique minimizing option.

**2. Exact finite block transfer.** Apply the preceding prepend rule from right to left across each of the four literal length-\(16\) blocks. The following table gives, for an incoming state with minimum option distance \(m\), difference \(\delta\), and **equal** option counts \(c_0=c_1=c\), the outgoing difference, increment \(\Delta m\), and common outgoing count divided by \(c\). The left-to-right order of input differences is \(-1,0,+1\).

| Block | Outgoing \(\delta\) | \(\Delta m\) for \(-1,0,+1\) | Outgoing count multiplier for \(-1,0,+1\) |
|:--|--:|:--|:--|
| A | \(+1\) | \(4,4,5\) | \(1,1,2\) |
| B | \(+1\) | \(6,5,5\) | \(4,2,2\) |
| C | \(-1\) | \(5,5,6\) | \(2,2,4\) |
| D | \(-1\) | \(5,4,4\) | \(2,1,1\) |

Each cell is a finite composition of sixteen explicitly defined one-symbol update rules, so the table needs no conjectural infinite extrapolation; the accompanying checker independently recomputes all twelve cells. In every cell, the two outgoing counts are equal and their multiplier is exactly \(2^{\Delta m-4}\). Initially the counts are equal; therefore they remain equal after each block. Every output difference is \(\pm1\). After \(q\) blocks, the minimum distance has increased from zero to \(m=\iota(W)\), while the common count has been multiplied by
\[
\prod_{j=1}^{q}2^{\Delta m_j-4}=2^{m-4q}.
\]
Since the final difference is nonzero, the shortest-absent count is exactly this common count. This proves the general block theorem.

**3. Identifying the Rudin–Shapiro block substitution.** With \(r(t)\) as defined, for \(0\le j<16\), splitting the binary expansion at the fourth bit gives
\[
r(16t+j)=r(t)\oplus\bigl((t\bmod2)\,\lfloor j/8\rfloor\bigr)\oplus r(j),
\]
where \(\oplus\) is exclusive-or. The length-\(16\) block at index \(t\) is therefore A, B, C, or D according as \((r(t),t\bmod2)\) is \((0,0),(0,1),(1,1),(1,0)\), respectively. Moreover,
\[
r(2t)=r(t),\qquad r(2t+1)=r(t)\oplus(t\bmod2),
\]
so the block-label word is the initial segment of the fixed point of
\[
\mathrm A\mapsto\mathrm{AB},\qquad
\mathrm B\mapsto\mathrm{AC},\qquad
\mathrm C\mapsto\mathrm{DB},\qquad
\mathrm D\mapsto\mathrm{DC}.
\]
For rank \(k\), it has exactly \(q=2^{k-4}\) labels.

**4. Summing the exact index.** Read the labels from right to left. If \(q\ge2\), the rightmost index \(q-1\) is odd, hence its block has type B or C and contributes \(\Delta m=5\) from the initial difference \(0\). By the transfer table, a block at position \(t<q-1\) contributes \(5+\epsilon_t\), where
\[
\epsilon_t=(2(t\bmod2)-1)\bigl(r(t)\oplus r(t+1)\bigr).
\]
It follows that \(\iota(R_k)=5q+E(q)\), with \(E(q)=\sum_{t=0}^{q-2}\epsilon_t\). In particular \(E(2)=0\). For every even \(q\ge2\), group consecutive edge terms at \(t=2s\) and \(t=2s+1\), using the two identities for \(r(2t)\) and \(r(2t+1)\). Every complete pair contributes the *negative* of its edge term at scale \(q\); the final unmatched even edge contributes \(-1\). Thus
\[
E(2q)=-E(q)-1\quad(q\ge2\text{ even}).
\]
Induction gives \(E(2^h)=0\) for odd \(h\ge1\) and \(E(2^h)=-1\) for even \(h\ge2\). At rank \(k=4\) there is one A block, and the table gives index \(4=5-1\). Consequently, with \(e_k\) as above, \(\iota(R_k)=5q-e_k\) for all \(k\ge4\). Substitution into the already proved block identity yields \(|\operatorname{SAS}(R_k)|=2^{(5q-e_k)-4q}=2^{q-e_k}\), completing both formulas.

## Verification
`checker.py` contains two finite checks: a direct next-occurrence suffix dynamic program for shortest-absent lengths and counts, and a separate right-to-left block-transfer implementation. It checks all \(12\) table cells; **all** \(4^q\) block strings for each \(1\le q\le4\); and the complete Rudin–Shapiro prefixes for every \(4\le k\le13\), comparing the dynamic program, greedy arch index, morphic construction, block identity, and specialized formulas. These checks passed when executed from the delivered standalone file. The infinite-rank conclusion follows from Steps 1–4; the finite experiments alone are not its proof.

## Relationship to prior work
Currie–Rampersad–Saari–Zamboni (2013, arXiv:1301.4972) use the classical four-letter morphism and coding for Rudin–Shapiro while studying *lexicographically extremal infinite words*; their Section 8 does not give shortest absent scattered-subsequence counts. Schaeffer–Shallit (2015, arXiv:1508.02074) develop factor properties of automatic sequences, including Rudin–Shapiro, but their properties are of **contiguous factors**, not the asserted scattered-language invariant. Hofman–Martens (2015) investigate language separability by bounded-length subsequences, not exact counts for this particular morphic word. Kosche–Koß–Manea–Siemer (arXiv:2108.13968) characterize and represent general shortest absent subsequences; their general results do not state the four-block multiplicative identity or the Rudin–Shapiro closed formulas. Adamson and collaborators (arXiv:2407.18599) determine general extremal absence counts at fixed universality, not this family's values. General-purpose algorithms can compute individual finite cases, but the all-rank formulas are not a direct quoted consequence of those algorithms.

## Limitations
The dyadic formulas cover rank \(k\ge4\), not arbitrary prefix lengths; the arbitrary-concatenation extension uses exactly the four listed length-\(16\) blocks. The theorem counts *shortest* absent scattered subsequences, not all absent subsequences, not minimal absent contiguous factors, and not all embeddings. No independent mathematical audit has been performed. The cited work is a targeted, non-exhaustive historical comparison, so an unidentified equivalent result remains a priority risk.

## References
1. J. D. Currie, N. Rampersad, K. Saari and L. Q. Zamboni, *Extremal words in morphic subshifts*, arXiv:1301.4972 (first submitted 2013-01-21), especially Section 8, https://arxiv.org/abs/1301.4972.
2. L. Schaeffer and J. Shallit, *Closed, Palindromic, Rich, Privileged, Trapezoidal, and Balanced Words in Automatic Sequences*, arXiv:1508.02074 (first submitted 2015-08-09), https://arxiv.org/abs/1508.02074.
3. P. Hofman and W. Martens, *Separability by Short Subsequences and Subwords*, ICDT 2015, DOI:10.4230/LIPIcs.ICDT.2015.230 (2015-03-19).
4. M. Kosche, T. Koß, F. Manea and S. Siemer, *Absent Subsequences in Words*, arXiv:2108.13968 (first submitted 2021-08-31), https://arxiv.org/abs/2108.13968.
5. D. Adamson et al., *Tight Bounds for the Number of Absent Subsequences*, arXiv:2407.18599 (first submitted 2024-07-26), https://arxiv.org/abs/2407.18599.
