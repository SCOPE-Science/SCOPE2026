# Binary block-language unions attain the rank-width bound within five states

## Finding

Let \(\Sigma=\{0,1\}\), \(A=\{00,10\}\), and \(B=\{01,10\}\). For each integer \(d\ge2\), define the two block languages \(K_d=A^d\) and \(H_d=B^d\), where the exponent denotes concatenation of exactly \(d\) two-bit blocks. The minimal complete deterministic finite automaton for \(K_d\cup H_d\) has exactly

\[
\operatorname{sc}(K_d\cup H_d)=8d-5.
\]

For \(K_d\), the number \(m_t\) of distinct nonempty right quotients after prefixes of length \(t\) is \(1\) for every \(0\le t\le2d\). For \(H_d\), the corresponding number \(n_t\) is \(1\) at even \(t\) and \(2\) at odd \(t\). Consequently, the rank-width upper bound for the union is

\[
\sum_{t=1}^{2d-1}(m_tn_t+m_t+n_t)+3=8d,
\]

and this family attains that bound within exactly five states for every \(d\ge2\). Moreover, among unions with these operand rank profiles, no smaller gap is possible: at prefix length one there are at most two nonempty quotients, and at prefix length \(2d-1\) there are at most three.

## Assumptions and scope

All automata are complete DFAs over the fixed binary alphabet \(\Sigma\). A right quotient after prefix \(p\) is \(p^{-1}L=\{x:px\in L\}\). The rank width at prefix length \(t\) counts distinct nonempty right quotients represented by prefixes of that length; the empty quotient is the single dead state shared across all ranks. The result is an exact extremal statement for the stated operand-width profile, not a formula for arbitrary binary block-language unions.

## Proof

Write \(A^r\) and \(B^r\) for concatenations of \(r\) blocks, with \(A^0=B^0=\{\varepsilon\}\).

For \(K_d=A^d\), every valid prefix of a fixed length has the same residual language: at a block boundary it is \(A^r\), and halfway through a block it is \(\{0\}A^r\). Thus \(m_t=1\) at every rank. For \(H_d=B^d\), at block boundaries the residual is \(B^r\); halfway through a block the next bit is forced to \(1\) after a first bit \(0\), and forced to \(0\) after a first bit \(1\). These two residuals are distinct, so \(n_t=2\) at odd depths and \(n_t=1\) at even depths.

Now count nonempty right quotients of \(K_d\cup H_d\) by prefix length. At depths \(0\) and \(2d\), there is one quotient. At an intermediate even depth \(2j\), where \(1\le j\le d-1\), prefixes split into three nonempty types: prefixes belonging only to \(K_d\), only to \(H_d\), and to both. Their residuals are respectively \(A^{d-j}\), \(B^{d-j}\), and \(A^{d-j}\cup B^{d-j}\). They are pairwise distinct because \((00)^{d-j}\) belongs only to the first component and \((01)^{d-j}\) only to the second. The width is therefore \(3\).

At depth one, the two possible prefixes give exactly two distinct residuals: after \(0\) the residual is \(\{0\}A^{d-1}\cup\{1\}B^{d-1}\), while after \(1\) it is \(\{0\}(A^{d-1}\cup B^{d-1})\). At an odd depth \(2j+1\) with \(1\le j\le d-2\), let \(r=d-j-1\ge1\). The three prefix types from the preceding block boundary yield the following five distinct residuals:

\[
\{0\}A^r, \{1\}B^r, \{0\}A^r\cup\{1\}B^r, \{0\}B^r, \{0\}(A^r\cup B^r).
\]

Distinctness follows from the leading bit and from \(A^r\ne B^r\), with neither contained in the other. Thus the width is \(5\) at each such depth. At the last odd depth \(2d-1\), the residuals are exactly \(\{0\}\), \(\{1\}\), and \(\{0,1\}\), so the width is \(3\).

The sum of nonempty quotient counts is therefore

\[
1+2+3(d-1)+5(d-2)+3+1=8d-6.
\]

All nonempty quotients at different prefix lengths are distinct because they contain words of different lengths. The empty quotient contributes one additional dead state. Myhill--Nerode therefore gives \(\operatorname{sc}(K_d\cup H_d)=8d-5\).

For the upper-bound comparison, the \(d\) odd ranks contribute \(1\cdot2+1+2=5\) each and the \(d-1\) internal even ranks contribute \(1\cdot1+1+1=3\) each; adding the initial, final, and dead states gives \(5d+3(d-1)+3=8d\). The first internal rank has at most two prefixes, hence at most two nonempty quotients; the last internal rank has one-symbol residuals, hence at most three. Those endpoint caps force a loss of at least \(3+2=5\) from this rank-width upper bound for this profile, and the construction attains both caps and all other rank bounds.

## Verification

The embedded standard-library script `verify.py` enumerates every prefix and suffix for \(2\le d\le8\), computes distinct nonempty right quotients directly, and checks the predicted profile and state count. It prints `VERIFY_OK`. This finite computation is a reproducibility check only; the universal result follows from the symbolic quotient argument above.

## Relationship to prior work

Duarte, Moreira, Prigioniero, and Reis establish a rank-width upper bound for unions of block languages and give a witness attaining it over alphabets of size at least three. Their proof explicitly identifies the binary-alphabet obstruction at the rank with only two possible prefixes. The family here is a binary, two-bit encoding of that ternary witness, but the exact intermediate-rank quotient profile and the state count \(8d-5\) are proved directly; the result is not asserted for arbitrary operand profiles or as a global binary-alphabet maximum.

The author's thesis version of the same work contains the same upper bound, ternary witness, and a future direction concerning state-count bounds for Boolean operations. Neither inspected version states the binary profile proved here. The encoding relationship is a genuine originality risk: the construction is motivated by the known ternary witness, while the new statement is the exact rank-by-rank binary quotient count and its five-state extremal gap.

## Limitations

The result only settles the specified infinite family and operand rank profile. It does not determine the maximum state complexity of union for arbitrary binary block languages. Literature and database searches are not proofs of novelty; an unindexed or unpublished equivalent construction may exist. The script checks only \(d\le8\), and is not used as a substitute for the proof for all \(d\ge2\).

## References

1. G. Duarte, N. Moreira, L. Prigioniero, and R. Reis, “Operational State Complexity of Block Languages,” arXiv:2409.06970, first publicly posted 2024-09-11. https://arxiv.org/abs/2409.06970
2. G. Duarte, “Minimal Automata and Operational State Complexity of Block Languages,” author thesis, relevant sections on union of block languages and block complement. https://www.dcc.fc.up.pt/~nam/resources/thesisGD.pdf
