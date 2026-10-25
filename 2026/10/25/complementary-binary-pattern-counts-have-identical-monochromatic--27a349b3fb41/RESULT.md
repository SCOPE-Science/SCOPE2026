# Complementary binary-pattern counts have identical monochromatic progression lengths

## Finding
Let \(v\) be any nonempty finite binary word that contains both \(0\) and \(1\), and let \(\bar v\) be its bitwise complement. For every integer \(q\ge2\) and every integer \(d\ge1\),
\[
A_{v,q}(d)=A_{\bar v,q}(d).
\]
In particular, the equality holds for the parity-colorings of Sobolewski's Problem 4, for **every** mixed pattern \(v\), without a restriction on pattern length or arithmetic-progression difference.

The underlying stronger statement is an **exact integer-valued reflection**, not merely an equality modulo \(2\). Define
\[
\varepsilon_v=\begin{cases}1,&v=1^r0^s\text{ for integers }r,s\ge1,\\0,&\text{otherwise.}\end{cases}
\]
For any \(n\ge0\), \(d\ge1\), \(L\ge1\), and any integer \(K\) at least \(|v|\) plus the binary digit length of \(n+(L-1)d\), put
\[
x_j=n+jd,\qquad y_j=2^K-1-x_{L-1-j},\qquad0\le j<L.
\]
Then \((y_j)\) is an increasing nonnegative arithmetic progression with step \(d\) and
\[
e_{\bar v}(y_j)=e_v(x_{L-1-j})+\varepsilon_v
\quad(0\le j<L).
\]
Thus the entire color word along the progression is reversed, possibly shifted by one common residue, at **every** modulus \(q\).

## Assumptions and scope
For \(n\ge0\), \(e_v(n)\) is the number of possibly overlapping occurrences of \(v\) in the ordinary base-two expansion of \(n\). When \(v\) begins with \(r\ge1\) zeros followed by a one, precede that expansion by exactly \(r\) zeros before counting; when \(v\) starts with a one, do not prepend zeros. Write \(0\) in binary as the one-digit word \(0\). This is the standard pattern-sequence convention used in the motivating paper.

For \(q\ge2\), a length-\(L\) progression \(n,n+d,\ldots,n+(L-1)d\) is \(v\)-monochromatic modulo \(q\) if the \(L\) integers \(e_v(n+jd)\) are congruent modulo \(q\). Define \(A_{v,q}(d)\) to be the supremum of all attainable positive lengths \(L\) over all starts \(n\ge0\), allowing an infinite supremum. For \(q=2\), this is the invariant \(A_v(d)\) introduced by Sobolewski. The theorem is restricted to **mixed** patterns; no result is asserted for constant patterns such as \(00\) or \(111\).

## Proof
**1. Padding invariance.** Let \(m=|v|\), and let \(B\) be the ordinary base-two expansion of a nonnegative integer \(x\). If \(v\) begins with a one, any number of zeros prepended to \(B\) creates no new occurrence of \(v\). If \(v\) begins with exactly \(r\ge1\) zeros, then its next digit is a one (because \(v\) is mixed). Every occurrence of \(v\) starting in the leading zero padding must use one of the last \(r\) zeros before the first one of \(B\): any earlier start would put a zero where the required one must occur. Therefore prepending \(m\) or more zeros gives exactly the same count as the prescribed \(r\)-zero padding. This argument also applies to \(x=0\), where no mixed pattern can occur in any all-zero expansion.

**2. Complementing a long padded word.** Choose an integer \(K\ge m+\ell\), where \(\ell\) is the ordinary binary digit length of \(x\) (take \(\ell=1\) when \(x=0\)). Its unique \(K\)-digit zero-padded binary word \(W\) begins with at least \(m\) zeros. By step 1, the number of \(v\)-occurrences in \(W\) is \(e_v(x)\). Let \(Y\) be the bitwise complement of \(W\). This is the **ordinary** binary expansion of \(2^K-1-x\), and it begins with at least \(m\) ones. Complementation is a positionwise bijection between occurrences of \(v\) in \(W\) and occurrences of \(\bar v\) in \(Y\). Thus the latter has exactly \(e_v(x)\) occurrences before the standard leading-zero adjustment.

If \(\bar v\) begins with a one, no adjustment is prescribed, so \(e_{\bar v}(2^K-1-x)=e_v(x)\). Otherwise write \(\bar v=0^r1u\) with \(r\ge1\). The prescribed \(r\) zeros preceding \(Y\) can create at most one occurrence: the only possible start aligns the entire \(0^r\) prefix before the initial digit of \(Y\). Since the first \(m\) digits of \(Y\) are ones, this new occurrence appears exactly when \(\bar v=0^r1^{m-r}\), or equivalently when \(v=1^r0^{m-r}\). Accordingly, **for all** \(x\) and \(K\) satisfying the digit-length condition,
\[
e_{\bar v}(2^K-1-x)=e_v(x)+\varepsilon_v.
\]
The correction \(\varepsilon_v\) depends only on \(v\), not on \(x\) or \(K\).

**3. Reverse a progression.** Fix \(n,d,L\) as in the statement, choose one \(K\) large enough for its largest member, and apply step 2 to each member. The reflection of the progression is
\[
y_j=2^K-1-[n+(L-1-j)d]
=\bigl(2^K-1-n-(L-1)d\bigr)+jd.
\]
Every \(y_j\) is nonnegative, and consecutive values differ by exactly \(d\). Applying step 2 termwise yields the claimed exact reversal identity. Reducing modulo \(q\), a constant color word stays constant under reversal and under addition of one fixed residue. Consequently, every length \(L\) available for \(v\) at difference \(d\) is available for \(\bar v\) at the same difference. Repeat the argument with \(v\) and \(\bar v\) exchanged to obtain the reverse inclusion of sets of attainable lengths, hence equality of their suprema, including the infinite case. \(\square\)

## Verification
The accompanying standard-library script `verify.py` checks exact integer identities for every mixed binary pattern of lengths \(2\) through \(7\) and for \(256\) distinct nonnegative arguments per pattern, varying the allowed padding width. It separately checks exact reflected arithmetic progressions with several lengths and differences, and residue congruences modulo \(2,3,5,7\). It tests \(240\) patterns, \(61{,}440\) point identities and \(4{,}800\) progression reversals. Execute `python3 verify.py`; successful completion prints a `VERIFIED:` line. The computation is supplementary to the symbolic proof and does not establish the infinite statement on its own.

## Relationship to prior work
B. Sobolewski's 2022 preprint (revised in 2023) defines these pattern-counting colorings and progression-length invariants and, in Section 6, **Problem 4**, asks for the differences \(d\) for which \(A_v(d)=A_{\bar v}(d)\). It reports computations for patterns of length at most three and suggests equality for every mixed pattern, but does not prove that general case. The present statement establishes this proposed equality for all mixed patterns and all \(d\) through a finite-word reflection. The arbitrary-modulus extension follows from the **integer** identity and is not a claim about explicit values of \(A_{v,q}(d)\). Bounds for one pattern, and identities relating \(d\) to \(2d\), do not imply comparison with its bitwise complement.

## Limitations
The theorem does not cover constant patterns, does not calculate the common numerical value of the progression invariant, and does not establish analogous statements for nonbinary bases. Priority remains subject to unindexed earlier results and uninspected revisions of the published journal version; the relevant passages of the open-access arXiv preprint were inspected. The finite verifier is not an infinite certificate.

## References
1. B. Sobolewski, *On monochromatic arithmetic progressions in binary words associated with pattern sequences*, arXiv:2204.05287, first posted 11 April 2022, revised 17 July 2023; Section 1 (definitions), Section 6 (Problem 4), Section 7 (computational method). https://arxiv.org/abs/2204.05287
2. B. Sobolewski, journal version, *Theoretical Computer Science* **1018** (2024), article 114815, DOI:10.1016/j.tcs.2024.114815. The index and abstract were accessible; no assertion of a full line-by-line journal-version inspection is made. https://doi.org/10.1016/j.tcs.2024.114815
