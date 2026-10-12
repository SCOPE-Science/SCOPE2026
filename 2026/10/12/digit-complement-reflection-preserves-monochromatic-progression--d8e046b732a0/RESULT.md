# Digit-complement reflection preserves monochromatic progression maxima in every base and modulus

## Finding
Fix an integer base \(b\ge2\), a modulus \(m\ge2\), and a length-\(r\) digit pattern \(v\in\{0,1,\ldots,b-1\}^r\) with \(r\ge1\). Assume \(v\ne0^r\) and \(v\ne(b-1)^r\). Let \(\bar v\) be obtained by replacing each digit \(a\) by \(b-1-a\). Define \(e_v(n)\) as the number of overlapping occurrences of \(v\) in the base-\(b\) digits of \(n\), including sufficient leading zeros to count a pattern starting with zeros. Put \(g_v(n)=e_v(n)\bmod m\). For \(d\ge1\), let \(A_v(d)\) be the supremum of lengths of constant-colored progressions \(g_v(n),g_v(n+d),\ldots,g_v(n+(L-1)d)\), over all starts \(n\ge0\) and lengths \(L\ge1\), with value \(+\infty\) if unbounded.

**Theorem.** For every permitted \(b,m,v,d\),
\[
A_v(d)=A_{\bar v}(d).
\]
More precisely, define \(\chi(w)=1\) when \(w=0^t(b-1)^{r-t}\) for some integer \(1\le t<r\), and \(\chi(w)=0\) otherwise. Given any positive integer \(L\), nonnegative \(n\), positive \(d\), and sufficiently large \(K\) with \(n+(L-1)d<b^{K-r}\), put \(N=b^K-1-n-(L-1)d\). Then simultaneously for all \(0\le j<L\),
\[
g_{\bar v}(N+jd)\equiv g_v(n+(L-1-j)d)+\chi(\bar v)\pmod m.
\]
Thus the entire length-\(L\) progression trace is transported to its reversal, with a fixed residue translation. In base two with modulus two, the equality proves the mixed-pattern assertion proposed in Problem 4 of Sobolewski [1] for **every** positive difference and pattern length.

## Assumptions and scope
The digit alphabet is \(\{0,1,\ldots,b-1\}\); powers of a digit denote repetition of that digit, not exponentiation. Every occurrence is contiguous, overlaps are allowed, and digits are most-significant first. A pattern containing at least one nonzero digit has a well-defined count even if its representation is prefixed with arbitrarily many zeros: any factor newly introduced by adding more than \(r-1\) zeros would consist only of zeros. The convention for the integer zero is immaterial because the two excluded all-zero patterns are the only ones that could occur in an all-zero representation. The complementary pattern also contains a nonzero digit, because \(v\ne(b-1)^r\).

The restriction to nonextreme patterns is essential to this particular finite-padding identity; the theorem makes no assertion for the pair of all-zero and all-maximum-digit patterns. It does not assert equality for progressions constrained to start at the same integer or at the origin.

## Proof
Write \(w_K(n)\) for the unique \(K\)-digit base-\(b\) expansion of \(n\in[0,b^K)\), allowing leading zeros, and write \(\kappa(w)\) for the digitwise complement of a finite digit word. Then
\[
\kappa(w_K(n))=w_K(b^K-1-n).
\]

**Padding lemma.** Suppose \(n<b^{K-r}\). The word \(w_K(n)\) begins with at least \(r\) zeros. Because \(v\ne0^r\), the total occurrence count \(e_v(n)\) is exactly the number of occurrences of \(v\) entirely inside \(w_K(n)\): occurrences starting farther left would lie inside a length-\(r\) all-zero block. Likewise, \(w_K(b^K-1-n)\) begins with at least \(r\) copies of the maximum digit \(b-1\). Every occurrence of \(\bar v\) wholly inside this word corresponds, under digitwise complementation, to precisely one occurrence of \(v\) in \(w_K(n)\).

To count the occurrences of \(\bar v\) introduced by the canonical leading-zero convention for \(b^K-1-n\), inspect a length-\(r\) factor that starts before its first digit but ends inside the word. It has exactly \(t\) leading zeros followed by \(r-t\) maximum digits for exactly one \(t\in\{1,\ldots,r-1\}\). Consequently exactly one additional occurrence exists if \(\bar v=0^t(b-1)^{r-t}\) for some such \(t\), and none otherwise. No occurrence lies entirely to the left because \(\bar v\ne0^r\). We therefore have the **exact integer identity**
\[
e_{\bar v}(b^K-1-n)=e_v(n)+\chi(\bar v)
\qquad(0\le n<b^{K-r}).
\]
This includes the edge case \(r=1\), where \(\chi=0\).

**Progression transfer.** Fix any \(L\ge1\), \(d\ge1\), and \(n\ge0\). Choose \(K\) so that \(n+(L-1)d<b^{K-r}\), and define \(N=b^K-1-n-(L-1)d\). Clearly \(N\ge0\). Apply the padding identity to \(n+(L-1-j)d\) for each \(0\le j<L\). Its reflected argument is \(N+jd\), so reducing modulo \(m\) proves the displayed trace identity. Constancy of the starting progression is equivalent to constancy of the reflected one, since reversal and uniform addition of \(\chi(\bar v)\) do not change constancy. Hence every monochromatic progression length attainable for \(v\) is attainable for \(\bar v\), at the **same** difference \(d\). Applying the same argument with \(v\) and \(\bar v\) interchanged proves the opposite inclusion. Their sets of attainable lengths, and therefore their suprema (finite or infinite), agree. \(\square\)

## Verification
The standalone `verify.py` checks the exact integer padding identity on all eligible patterns of lengths one to four over bases two through five, with 128 test inputs per pattern. It also tests the ordered progression-trace identity over bases two through four, pattern lengths one through three, moduli two, three and five, differences one through five, five tested progression lengths, and sixteen starting indices. It prints

`VERIFY_OK count_identities=158464 finite_progression_transfers=142800`

under Python 3 with no nonstandard dependencies. These finite checks are diagnostics; the theorem for unbounded integers, all bases, moduli and lengths follows from the two symbolic steps above.

## Relationship to prior work
Sobolewski [1], Section 6, Problem 4, asks for the differences satisfying \(A_v(d)=A_{\bar v}(d)\), and suggests that for binary patterns other than all zeros and all ones equality should hold for every difference. The present reflection identity proves that proposal, establishes an explicit transfer of arbitrary finite progression traces, and permits all bases and moduli. The general study in [1] gives upper bounds and specific progression lengths but does not give this reflection equivalence; Section 6, Problem 10, also invites generalization in the base and modulus. Aedo et al. [2] consider progression growth for primitive bijective and spin substitutions; Joshi and Rust [3] analyze several individual automatic words. Neither supplies the stated universal complementary-pattern trace transfer.

## Limitations
No analogous assertion for the all-zero versus all-maximum-digit patterns is proved. The origin-constrained function \(A_v(0,d)\) is not generally preserved by the reflected starting point. The argument does not determine the common numerical value of \(A_v(d)\) for a specific pattern and difference, nor does it classify all possible finite arithmetic traces without the reversal-and-shift operation. Bibliographic comparisons cannot exclude an equivalent older result expressed as digital reflection or finite-word duality.

## References
[1] B. Sobolewski, *On monochromatic arithmetic progressions in binary words associated with pattern sequences*, arXiv:2204.05287, first publicly posted 11 April 2022, especially Section 6, Problem 4, and Problem 10. https://arxiv.org/abs/2204.05287

[2] I. Aedo, U. Grimm, N. Mañibo, Y. Nagai, P. Staynova, *Monochromatic arithmetic progressions in automatic sequences with group structure*, arXiv:2302.12908 (2023). https://arxiv.org/abs/2302.12908

[3] R. Joshi and D. Rust, *Monochromatic arithmetic progressions in the Fibonacci, Thue–Morse, and Rudin–Shapiro words*, arXiv:2501.05830 (2025). https://arxiv.org/abs/2501.05830
