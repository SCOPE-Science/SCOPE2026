# The complete circular antidictionary of three distinct binary gaps

## Finding
For all integers \(1\le a<b<c\), take the cyclic binary word
\[
 w=0\,1^a0\,1^b0\,1^c.
\]
Its complete set of minimal absent contiguous factors is
\[
\begin{aligned}
\mathcal M(w)={}&\{00,\ 1^{c+1},\ 1^{b+1}0\,1^{a+1},\\
&0\,1^a0\,1^{b+1},\ 1^{a+1}0\,1^b0,\\
&0\,1^a0\,1^a0,\ 0\,1^b0\,1^a0\}\\
&\cup\{0\,1^j0:\ 1\le j<c,\ j\notin\{a,b\}\}.
\end{aligned}
\]
There are no repetitions between the displayed terms, and
\[
\boxed{|\mathcal M(w)|=c+4.}
\]
The number of words in \(\mathcal M(w)\) containing exactly \(0,1,2,3\) zeros is respectively \(1,1,c,2\); no minimal absent word contains more than three zeros. In particular the total depends only on the largest gap \(c\), not on the other two gap lengths.

## Assumptions and scope
A cyclic word is viewed through its bi-infinite periodic extension. A *factor* is a finite contiguous block from this extension, with wrapping across a displayed boundary allowed. A word \(u\) of length at least two is *minimal absent* when \(u\) does not occur but its length-one-shorter prefix and suffix both occur. Those two conditions imply that every proper factor occurs. The alphabet is exactly \(\{0,1\}\); both one-letter factors occur. The positive integer gaps satisfy \(1\le a<b<c\), so each full zero-to-zero gap identifies a unique cyclic phase.

## Proof
Write the three successive one-run gap lengths as \(a,b,c\). The gap-successor map is \(a\mapsto b\mapsto c\mapsto a\), and the gap-predecessor map is \(a\mapsto c\mapsto b\mapsto a\). Each factor \(0\,1^j0\) occurs if and only if \(j\in\{a,b,c\}\); for each such \(j\) it occurs at one phase per period. Also the longest factor consisting entirely of ones has length \(c\).

**Phase uniqueness.** Any occurring factor containing two successive zeros with their full separating gap \(j\in\{a,b,c\}\) fixes a unique start phase modulo the period. Consequently, a minimal absent word \(u\) cannot have such a pair of zeros in its interior \(u[2..|u|-1]\): occurrences of its proper prefix and proper suffix would share the uniquely positioned interior and would force an occurrence of the complete word. This will rule out long patterns.

**Zero and one zero symbols.** The only minimal absent all-one word is \(1^{c+1}\). No one-letter word is absent. A word with one zero and positive ones on both sides has shape \(1^p0\,1^q\). It occurs precisely when some zero has at least \(p\) predecessor ones and \(q\) successor ones. The three adjacent gap pairs are \((c,a),(a,b),(b,c)\), and \((a,b)\) is coordinatewise dominated by \((b,c)\). Therefore occurrence is equivalent to
\[
(p\le c\ \land\ q\le a)\quad\text{or}\quad(p\le b\ \land\ q\le c).
\]
Among pairs with \(p,q\le c\), exactly the pair \((b+1,a+1)\) is minimally excluded under shortening at either end. This gives \(1^{b+1}0\,1^{a+1}\). A word with one zero at an endpoint is always present as long as its one-runs do not exceed \(c\); longer ones already contain \(1^{c+1}\). Thus the displayed one-zero item is the only one.

**Two zeros.** The factor \(00\) is minimally absent because all zeros are isolated. The factors \(0\,1^j0\) with \(1\le j<c\), \(j\notin\{a,b\}\), are minimally absent; their immediate proper prefix and suffix fit inside the largest run, and the exact gap does not occur. No other unobserved complete gap can be minimal, since a gap beyond \(c\) contains \(1^{c+1}\). If the complete gap is \(j\in\{a,b,c\}\), a two-zero word with extensions on both outer sides has a unique interior gap and is forbidden by phase uniqueness from minimality. A minimal candidate with extra ones only on the right is necessarily \(0\,1^j0\,1^{\operatorname{succ}(j)+1}\), provided the shorter suffix \(1^j0\,1^{\operatorname{succ}(j)+1}\) occurs. This happens only for \(j=a\), where the suffix can be realized at the zero with adjacent gaps \((b,c)\), producing \(0\,1^a0\,1^{b+1}\). For \(j=b\), its right-run exponent exceeds \(c\); for \(j=c\), the suffix is absent. Symmetrically, an extension only on the left yields \(1^{a+1}0\,1^b0\) for \(j=b\); for \(j=a\), the required left-run exponent exceeds \(c\), and for \(j=c\), the proper prefix is absent. These two and the absent full gaps exhaust the two-zero case.

**Three zeros.** If a three-zero minimal absent word has any nonzero outer run, its interior still contains two successive zeros separated by one complete gap, contradicting phase uniqueness. Thus it is \(0\,1^i0\,1^j0\). To have both proper prefix and suffix present, necessarily \(i,j\in\{a,b,c\}\), \(j\le\operatorname{succ}(i)\), and \(i\le\operatorname{pred}(j)\). The three occurring ordered gap pairs are \((a,b),(b,c),(c,a)\). Checking the six remaining pairs shows exactly \((i,j)=(a,a)\) and \((b,a)\) satisfy both inequalities. These give \(0\,1^a0\,1^a0\) and \(0\,1^b0\,1^a0\).

**Four or more zeros.** The interior of every word with at least four zeros contains at least two successive zeros and their complete intervening one-run. If that gap is absent, the interior does not occur; if present, phase uniqueness prevents minimal absence. This excludes all remaining possibilities.

There are seven individually listed minimal absent words and exactly \(c-3\) choices of the auxiliary gap \(j\), giving \(7+c-3=c+4\). Counting zeros also yields the asserted profile. This completes the proof.

## Verification
The accompanying standalone `check_three_gap_maw.py` enumerates every parameter triple satisfying \(1\le a<b<c\le24\). For each instance, it explicitly constructs all circular factors to the primitive period length and extracts minimal absent factors from occurrence of both proper sides; it compares the resulting complete set with the theorem, including its count. An independently coded circular indexing procedure checks five parameter instances and all rotations of three additional words. These finite checks support, but do not replace, the unbounded proof above.

## Relationship to prior work
Fici, Restivo, and Rizzo (arXiv:1707.04450, first public 2017-07-14) give general circular-word minimal-forbidden-factor theory, an exact reduction to bounded factors of a doubled word, and specialized circular Fibonacci constructions. Their general extraction method does not itself state the three-distinct-gap classification or its \(c+4\) closed formula. Akagi et al. (arXiv:2202.13591) analyze minimal absent words in run-length-encoded *linear* strings and representation/algorithmic bounds. Ota and Manada (DOI:10.1587/transfun.2023TAP0015) study circular binary reconstruction from substrings and minimal absent words. The present statement is a parameter-uniform closed antidictionary, not an assertion that minimal absent factors, circular indexing, or run-length processing are themselves new.

## Limitations
The ordered distinct-gap hypothesis is essential to the phase-uniqueness proof; no result is claimed for repeated gaps or arbitrary numbers of zeros. The words are factors of the *circular* periodic language, not just the displayed finite linear word. A complete search of all historical literature is impossible; implicit or unindexed earlier equivalences remain possible. Finite program checks cannot certify the infinite assertion independently of the proof.

## References
1. G. Fici, A. Restivo, L. Rizzo, *Minimal Forbidden Factors of Circular Words*, arXiv:1707.04450 (first public 2017-07-14), https://arxiv.org/abs/1707.04450.
2. T. Akagi et al., *Minimal Absent Words on Run-Length Encoded Strings*, arXiv:2202.13591 (2022), https://arxiv.org/abs/2202.13591.
3. T. Ota, A. Manada, *A Reconstruction of Circular Binary String Using Substrings and Minimal Absent Words* (2023), https://doi.org/10.1587/transfun.2023TAP0015.
