# Exact circular Burrows–Wheeler transform of dyadic paperfolding prefixes

## Finding

Let \(p(i)\), for \(i\ge1\), equal \(1\) when the odd part of \(i\) is congruent to \(1\pmod4\), and equal \(0\) otherwise. Let \(P_k=p(1)\cdots p(2^k)\) for integer \(k\ge6\), with alphabet order \(0<1\). The **circular Burrows–Wheeler transform** \(\operatorname{BWT}(P_k)\) sorts all \(2^k\) cyclic rotations lexicographically and concatenates their preceding letters (equivalently, their last columns), without adding a sentinel.

Put \(q=2^{k-5}\). For every integer \(j\ge7\), define the explicit binary word
\[
A_j=1^{2^{j-7}}0^{2^{j-7}-1}1^{2^{j-7}}0^{2^{j-7}+1}.
\]
Set \(B_6=1011\), and recursively let \(B_j=A_jB_{j-1}\) for every \(j\ge7\). These symbols denote ordinary string concatenation, and \(0^0\) denotes the empty word.

**Exact-transform theorem.** For every integer \(k\ge6\), \(\operatorname{BWT}(P_k)\) is the concatenation, in the indicated order, of these eighteen blocks:

| Index | Entire block |
|---:|:---|
| 1 | \(1^{2q-1}\) |
| 2 | \(1^{2q}0^{2q-1}\) |
| 3 | \(1^{2q+1}\) |
| 4 | \(0^{2q}\) |
| 5 | \(1^q\) |
| 6 | \(0^q\) |
| 7 | \(1^q\) |
| 8 | \(0^{q-1}\) |
| 9 | \(0^{2q+1}\) |
| 10 | \(1^q0^{q-1}\) |
| 11 | \(1^{2q}\) |
| 12 | \(1^q0^{q+1}\) |
| 13 | \(1^{2q}\) |
| 14 | \(0^q\) |
| 15 | \(A_{k+1}\) |
| 16 | \(0^q\) |
| 17 | \(B_k\) |
| 18 | \(0^{2q+1}\) |

In particular, the number of **maximal equal-letter runs** in this transform is exactly
\[
\boxed{\operatorname{runs}(\operatorname{BWT}(P_k))=4k-4,\qquad k\ge6.}
\]
This gives an exact logarithmic-in-length BWT run count and, more strongly, a complete transform specification for every rank.

## Assumptions and scope

Indices in the paperfolding definition start at \(1\); macroblock indices and cyclic rotation starts begin at \(0\). There is no sentinel, and the last symbol of the original word is the preceding symbol for rotation at position \(0\). A cyclic word of length \(2^k\) can have repeated rotations in general, but the present words are primitive: for \(k\ge2\) they contain exactly \(2^{k-1}+1\) ones, an odd number. Any nontrivial integer power of length \(2^k\) repeats an even number of times, contradicting this parity. Consequently the sorted rotation order is unambiguous.

This theorem covers complete dyadic prefixes \(P_k\) of the ordinary binary paperfolding sequence only, with \(k\ge6\). It is not a claim about arbitrary prefixes, arbitrary paperfolding instructions, or sentinel-terminated BWT.

## Proof

**1. The exact sixteen-symbol macroblocks.** The arithmetic definition gives
\[
p(2a)=p(a),\qquad
p(2a+1)=\begin{cases}1&a\text{ even},\\0&a\text{ odd}.
\end{cases}
\]
In particular, \(\#\{i\le2^t:p(i)=1\}=2^{t-1}+1\) for every \(t\ge1\). Put \(m=2^{k-4}\). For \(0\le a<m\), the sixteen symbols in zero-based positions \(16a,\ldots,16a+15\) form precisely
\[
K_e(x)=\begin{cases}
110110011100100x&e=0,\\
110110001100100x&e=1,
\end{cases}
\qquad e=a\bmod2,\quad x=p(a+1).
\]
The word \(P_k\) is the concatenation of these \(m\) macroblocks, with \(m\) even. Write \(r=2^{k-6}\), so \(m=4r\) and \(q=2r\). The numbers of macros of each type \((e,x)\), ordered as \((0,0),(0,1),(1,0),(1,1)\), are exactly
\[
(r,r,r-1,r+1).
\]
For even \(a\), this follows by counting the two residues of \(a/2\pmod2\); for odd \(a=2b+1\), it follows by counting zeros and ones in \(p(1)\cdots p(2r)\). The same formulas apply to the cyclic join, since the last macro is odd and the first is even.

**2. A finite exhaustive seven-symbol classification.** For a start offset \(s\in\{0,\ldots,15\}\) within a macro, the next seven symbols depend only on \(s,e,x\). Indeed, if they cross the macro boundary, the next macro contributes at most its first six letters, which are always \(110110\). Enumerating exactly the \(16\cdot2\cdot2=64\) possible triples \((s,e,x)\) gives the \(28\) different seven-letter factors in `SEVEN_GRAM_TABLE.md`, with their offsets, exact multiplicities, and preceding-symbol rules. This is a finite enumeration of explicit literal blocks, not a numerical extrapolation; the four macro-type multiplicities above convert it into counts for all \(k\ge6\). For twenty-four seven-factors the preceding bit is already forced.

The only seven-factors with two possible preceding bits are \(1000110\), \(1001110\), \(1100100\), and \(1101100\). Distinct seven-letter factors occupy consecutive lexicographic blocks of sorted rotations. We now determine the preceding-bit sequence *inside* each of these four blocks, without assuming that equal seven-factors have arbitrary order.

**3. The first two ambiguous factors.** Each of \(1000110\) and \(1001110\) occurs only at macro offsets \(s=4\) and \(s=12\). At offset \(4\) its preceding bit is \(1\), and at offset \(12\) it is \(0\). In both cases the eighth bit of the rotation is \(0\) at offset \(4\) and \(1\) at offset \(12\). Thus every occurrence preceded by \(1\) sorts before every occurrence preceded by \(0\), and the exact two BWT contributions are respectively
\[
1^q0^{q-1},\qquad 1^q0^{q+1}.
\]
The exponents are the corresponding sums of the four macro-type frequencies.

**4. The third ambiguous factor.** The factor \(1100100\) occurs only at macro offset \(s=8\). Its preceding symbol is \(1\) for even macros and \(0\) for odd macros. Its eighth symbol is \(x\), so the occurrences with \(x=0\) sort before those with \(x=1\). For fixed \(x\), the next distinguishing macro letter is at total rotation offset \(15\): this is \(0\) when the original macro is even and \(1\) when it is odd. Thus within each \(x\) group, the \(1\)-preceded occurrences sort before the \(0\)-preceded ones. The exact contribution is
\[
1^r0^{r-1}1^r0^{r+1}=A_{k+1}.
\]

**5. The recursively ordered fourth ambiguous factor.** The factor \(1101100\) occurs only at macro offset \(s=0\). Sorting rotations starting at such offsets is equivalent to sorting cyclic macro sequences \(K_{a\bmod2}(p(a+1))K_{(a+1)\bmod2}(p(a+2))\cdots\). The eighth macro bit is \(0\) for odd \(a\), and \(1\) for even \(a\); hence all odd macro indices sort before all even ones. Within a fixed parity, the succession of trailing macro bits compares exactly the rotations of the shorter paperfolding word \(P_{k-4}\) at the corresponding indices. This last reduction is valid even at the cyclic boundary because \(p(m)=1\), the same bit as at the end of the shorter prefix.

The preceding bit for macro index \(a\) is \(p(a)\) when \(a>0\), and \(p(m)=1\) when \(a=0\). Consider odd indices \(a=2b+1\). Their shorter-word rotations begin with \(p(b+1)\), followed by \(p(2b+3)\), which is \(0\) for even \(b\) and \(1\) for odd \(b\). Their preceding bits are \(1\) for even \(b\) and \(0\) for odd \(b\). The relevant four cardinalities are \(r/2,r/2-1,r/2,r/2+1\) for \(k\ge7\), giving precisely \(A_k\) as the preceding-bit string of the odd-index block.

For even indices \(a=2b\), the shorter-word rotations begin with \(p(2b+1)\), which groups odd \(b\) before even \(b\); within either group the remaining symbols compare the rotations of \(P_{k-5}\). Their preceding bits are \(p(b)\), with the cyclic boundary convention preserved. Therefore the even-index block repeats exactly the same order-and-predecessor problem one rank lower. At \(k=6\) direct four-index ordering gives \(B_6=1011\). By induction the entire \(1101100\)-block contributes \(B_k=A_kB_{k-1}\) for all \(k\ge7\).

**6. Concatenation and run count.** Sorting the \(28\) rows of `SEVEN_GRAM_TABLE.md` lexicographically, using the uniform preceding bits for twenty-four rows and the four explicit contributions proved above, produces the eighteen consecutive blocks in the theorem. Their lengths sum to \(2^k\), so no rotation is omitted or duplicated. For \(k\ge7\), \(B_k\) begins in \(1\), ends in \(1\), and has exactly \(4k-23\) runs: \(B_7=11001011\) has five, while prepending \(A_{k+1}\) for the next rank adds exactly four. Directly counting transitions between the eighteen displayed blocks (including their internal runs) yields \(19+\operatorname{runs}(B_k)\) for \(k\ge7\), hence \(4k-4\). The separately evaluated base \(k=6\) has twenty runs, also \(4k-4\). This proves the theorem for all claimed ranks. \(\square\)

## Verification

The bundled `checker.py` constructs paperfolding prefixes from the odd-part definition; compares a cyclic suffix-doubling sorter to independent literal-rotation sorting for ranks \(2\)–\(9\); checks the complete eighteen-block formula and resulting run count for ranks \(6\)–\(14\); and separately re-enumerates all sixty-four macrotype/offset cases symbolically with the rank-dependent type frequencies. The observed run counts for ranks \(6\)–\(14\) are \(20,24,28,32,36,40,44,48,52\). Running `python checker.py` prints `VERIFY_OK` when all assertions hold. The proof above, not these bounded experiments, establishes the unrestricted induction.

## Relationship to prior work

Burrows and Wheeler (1994) define the cyclic-rotation sorting transform; their report does not analyze paperfolding prefixes. Allouche (1992) proves the length-seven factor complexity of infinite paperfolding sequences (including the value \(28\)) and develops parity-based factor classifications, but does not compute a BWT of finite dyadic prefixes. Frosini et al. (2022) establish logarithmic run-count bounds for broad morphic-word classes by bispecial-factor methods; the inspected full preprint does not contain a paperfolding-specific exact BWT formula, and a general growth bound does not imply this exact constant or the eighteen-block transform. The present proof uses a local macroblock classification and a recursively ordered exceptional seven-factor.

## Limitations

The theorem uses the **sentinel-free circular** BWT of complete prefixes, not the more commonly implemented BWT with an end marker. Its explicit formulas begin at rank six. The novelty comparison is best-knowledge rather than a universal priority guarantee; work whose terminology or indexing differs could have escaped searches. Independent mathematical checking has not been performed.

## References

1. J.-P. Allouche, *The number of factors in a paperfolding sequence*, Bulletin of the Australian Mathematical Society **46** (1992), 23–32. DOI: 10.1017/S0004972700011655. Full text: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/E051B7126B0C5DC6127BAD6B6C59BEA9/S0004972700011655a.pdf/the-number-of-factors-in-a-paperfolding-sequence.pdf.
2. M. Burrows and D. J. Wheeler, *A Block-sorting Lossless Data Compression Algorithm*, Digital Systems Research Center, Research Report 124, May 10, 1994. Full text: https://www.cs.jhu.edu/~langmea/resources/burrows_wheeler.pdf.
3. A. Frosini, I. Mancini, S. Rinaldi, G. Romana, and M. Sciortino, *Logarithmic equal-letter runs for BWT of purely morphic words*, 2022, arXiv:2202.02609, https://arxiv.org/abs/2202.02609.
