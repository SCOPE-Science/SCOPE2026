# A digit-reflection duality for complementary binary pattern progressions

## Finding

Let \(v\) be any finite binary word containing at least one \(0\) and at least one \(1\), let \(\bar v\) be its bitwise complement, and let \(A_v(d)\) be the supremum of lengths of monochromatic arithmetic progressions of positive difference \(d\) in the binary sequence \(n\mapsto e_v(n)\bmod 2\), with occurrences defined below. Then, **for every positive integer \(d\)**,

\[
A_v(d)=A_{\bar v}(d).
\]

This establishes the general mixed-pattern equality proposed in Problem 4 of Sobolewski's 2022 paper. A stronger exact-count duality, not merely a length comparison, provides the proof.

## Assumptions and scope

Let \(\beta(n)\) denote the usual base-two expansion of an integer \(n\ge0\), with \(\beta(0)=0\) and no leading zero for \(n>0\). For a finite word \(w\), let \(a(w)\) be its number of initial zeros. When \(w\) contains a \(1\), define \(e_w(n)\) as the number of *possibly overlapping* occurrences of \(w\) in the word \(0^{a(w)}\beta(n)\). This is the leading-zero convention in Sobolewski, Section 1. Here we consider only mixed patterns, so every pattern and its complement contains a \(1\).

For \(d\ge1\), define \(A_w(d)\) as the supremum, over starting integers \(n\ge0\), of the lengths \(h\ge1\) for which \(e_w(n+jd)\bmod2\) is independent of \(j\) for \(0\le j<h\). An infinite supremum is allowed. Define \(\delta(w)=1\) when \(w=0^a1^{m-a}\) for some \(1\le a<m\), where \(m=|w|\), and \(\delta(w)=0\) otherwise.

The precise stronger statement is: for every mixed \(v\) of length \(m\), every \(L\ge m+1\), and each integer \(0\le n<2^{L-m}\), with \(y=2^L-1-n\),

\[
e_{\bar v}(y)=e_v(n)+\delta(\bar v).
\]

The equality is between full integer occurrence counts, not just parities.

## Proof

**Step 1: arbitrary sufficient zero padding does not change mixed-pattern counts.** Fix a mixed pattern \(v\) of length \(m\). Its occurrence count in the fixed-length word \(0^{L-|\beta(n)|}\beta(n)\), for \(L-|\beta(n)|\ge m\), equals \(e_v(n)\). If \(v\) starts with \(1\), it cannot begin anywhere in a leading zero prefix, so the claim is immediate. Otherwise, let \(a=a(v)\), with \(1\le a<m\); the prefix of \(v\) is \(0^a1\). Every occurrence of \(v\) beginning inside the leading zeros must use exactly the final \(a\) leading zeros before the first nonzero digit of \(\beta(n)\), because the \((a+1)\)-st digit of \(v\) is \(1\). This possible boundary occurrence is already present in \(0^a\beta(n)\). All other occurrences lie inside \(\beta(n)\), and no copy of \(v\) lies entirely in the leading zeros. For \(n=0\), both words contain only zeros and hence no mixed occurrence. Thus sufficient zero padding leaves \(e_v(n)\) unchanged.

**Step 2: bitwise complementation and the sole possible boundary correction.** For \(0\le n<2^{L-m}\), the length-\(L\) padded binary expansion of \(n\) begins with at least \(m\) zeros; its bitwise complement is the length-\(L\) usual expansion of \(y=2^L-1-n\), which begins with at least \(m\) ones. Complementation bijects each occurrence of \(v\) in the padded expansion with an occurrence of \(\bar v\) in \(\beta(y)\), respecting overlapping occurrences. By Step 1, the former count is \(e_v(n)\).

To compute \(e_{\bar v}(y)\), one must prepend \(a(\bar v)\) zeros to \(\beta(y)\). Because \(\beta(y)\) begins with at least \(m\) ones, the added prefix produces exactly one new occurrence precisely when \(\bar v=0^a1^{m-a}\) for some \(1\le a<m\). Indeed, any new occurrence must begin within those initial zeros, its first \(a\) symbols must be the complete zero prefix, and the remaining symbols all come from the initial ones; all other candidate starting locations fail to match the first \(1\) of the pattern. Thus its contribution is \(\delta(\bar v)\), independent of \(n\). The displayed exact-count reflection identity follows.

**Step 3: reverse every finite arithmetic progression.** Fix \(d\ge1\), an arbitrary length \(h\ge1\), and a progression \(x_j=b+jd\) for \(0\le j<h\), with \(b\ge0\). Choose \(L\ge m+1\) so large that \(x_{h-1}<2^{L-m}\). Let

\[
y_j=2^L-1-x_{h-1-j}\qquad(0\le j<h).
\]

All \(y_j\) are nonnegative, strictly increasing with common difference \(d\), and Step 2 yields

\[
e_{\bar v}(y_j)=e_v(x_{h-1-j})+\delta(\bar v).
\]

If the \(v\)-parities along the original progression are equal, the \(\bar v\)-parities along the new progression are equal as well (with a possible uniform color flip). Hence \(A_{\bar v}(d)\ge A_v(d)\). Interchanging \(v\) and \(\bar v\) gives the converse. Both directions hold for all finite \(h\), whether or not the suprema are infinite, proving \(A_v(d)=A_{\bar v}(d)\).

In fact, Step 3 maps **every finite progression color word** for \(v\) to a reversed progression color word for \(\bar v\), possibly with every bit toggled by the constant \(\delta(\bar v)\).

## Verification

The independent illustrative checker `verify.py` counts possibly overlapping binary occurrences directly, including the prescribed leading zeros. It checks every mixed pattern of lengths \(2\) through \(8\), differences \(1\) through \(15\), progression starting points \(0\) through \(30\), and progressions of length five: \(229710\) configurations in total. Every configuration checks the exact reflection identity at each of five terms and the equality of all four consecutive-count differences. Execute `python3 verify.py` with Python 3. The check is finite corroboration; Steps 1–3 establish the universal theorem.

## Relationship to prior work

Bartosz Sobolewski, *On monochromatic arithmetic progressions in binary words associated with pattern sequences* (arXiv:2204.05287, posted 11 April 2022), defines precisely these sequences and \(A_v(d)\). Problem 4 in Section 6 observes numerical equality for mixed words of length at most three and explicitly proposes equality for every mixed binary word and every difference. The proof above establishes that proposed statement and provides the stronger finite-progression reflection.

Abram, Hu, and Li (arXiv:2304.14595) treat the automatic/morphic structure of block-counting sequences rather than the equality of progression lengths for complementary blocks. Aedo and collaborators (arXiv:2302.12908) investigate progression-length asymptotics in a different automatic-substitution framework. Their accessible abstract does not establish the present exact duality. The direct published-problem comparison and semantic searches disclosed no stronger covering theorem in the inspected material; they do not establish absolute bibliographic priority.

## Limitations

The assertion concerns patterns containing *both* binary digits, and arithmetic progressions beginning at arbitrary nonnegative positions. It makes no assertion for constant patterns \(0^m\) or \(1^m\), nor that longest progressions necessarily start at the origin. The chosen reflection location depends on the particular finite progression. The proof concerns base two and occurrences counted modulo two for monochromatic colorings; the exact-count reflection itself is integral. A publisher-hosted later version of the motivating paper and any unindexed subsequent treatments have not been completely compared. Independent scientific assessment has not been performed.

## References

1. Bartosz Sobolewski, *On monochromatic arithmetic progressions in binary words associated with pattern sequences*, arXiv:2204.05287v1 (11 April 2022), Section 1 and Problem 4 in Section 6. https://arxiv.org/abs/2204.05287
2. Antoine Abram, Yining Hu, and Shuo Li, *Block-counting sequences are not purely morphic*, arXiv:2304.14595v1 (28 April 2023). https://arxiv.org/abs/2304.14595
3. Ibai Aedo, Uwe Grimm, Neil Mañibo, Yasushi Nagai, and Petra Staynova, *Monochromatic arithmetic progressions in automatic sequences with group structure*, arXiv:2302.12908v1 (24 February 2023). https://arxiv.org/abs/2302.12908
