# Exact word growth and arithmetic square-root oscillations in a valuation-parity spacing shift

## Finding

Let \(\nu_2(d)\) be the exponent of two in a nonzero integer \(d\). Consider the two-sided binary spacing shift
\[
X=\{x\in\{0,1\}^{\mathbb Z}:x_i=x_j=1,\ i\ne j\Longrightarrow\nu_2(|i-j|)\text{ is odd}\}.
\]
Write \(p(n)\) for the number of length-\(n\) words in its language. Define \(F(0)=G(0)=1\), \(F(1)=G(1)=2\), and, for every integer \(n\ge2\),
\[
\begin{aligned}
F(n)&=G(\lceil n/2\rceil)+G(\lfloor n/2\rfloor)-1,\\
G(n)&=F(\lceil n/2\rceil)F(\lfloor n/2\rfloor).
\end{aligned}
\]
**The exact complexity at every length is \(p(n)=F(n)\).** In particular, for every integer \(n\ge1\),
\[
\boxed{p(4n)=2p(n)^2-1.}
\]
Consequently, for every integer \(m\ge0\),
\[
\boxed{\begin{aligned}
p(4^m)&=\frac{(2+\sqrt3)^{2^m}+(2-\sqrt3)^{2^m}}2,\\
p(2\cdot4^m)&=\frac{(3+2\sqrt2)^{2^m}+(3-2\sqrt2)^{2^m}}2.
\end{aligned}}
\]
For each fixed positive integer \(r\), a stronger all-base renormalization holds:
\[
\lim_{m\to\infty}\frac{\log p(r4^m)}{\sqrt{r4^m}}
=\frac{\operatorname{arcosh}(p(r))}{\sqrt r}.
\]
In particular the scaled logarithmic complexity does **not** converge, since along two dyadic subsequences its limits are distinct:
\[
\lim_{m\to\infty}\frac{\log p(4^m)}{2^m}
=\log(2+\sqrt3)=1.3169578969\ldots,
\]
\[
\lim_{m\to\infty}\frac{\log p(2\cdot4^m)}{2^m\sqrt2}
=\frac{\log(3+2\sqrt2)}{\sqrt2}=1.2464504803\ldots.
\]
Nevertheless, \(\log p(n)=\Theta(\sqrt n)\), so its entropy vanishes and
\[
\lim_{n\to\infty}\frac{\log\log p(n)}{\log n}=\frac12.
\]
Moreover, this shift is uncountable, uniquely ergodic with the point mass on the all-zero sequence as its **only invariant probability**, proximal, nonsofic, and has the all-zero sequence as its **only periodic point**.

## Assumptions and scope

Indices range over all integers, and binary words may be embedded into bi-infinite configurations by padding both sides with zeros. Thus every finite word meeting the pairwise distance constraint occurs in \(X\). Only **pairwise distances among all occurrences of one**, not merely distances between consecutive ones, are constrained. Logarithms are natural; the displayed entropy constants are in nats. The auxiliary count \(G(n)\) applies the same condition with **even** (rather than odd) valuation of every nonzero pairwise distance. The empty word has one possibility.

## Proof

**1. Exhaustive parity splitting.** In a word of length \(n\), the even-index positions form a subsequence of length \(\lceil n/2\rceil\) and the odd-index positions one of length \(\lfloor n/2\rfloor\), using positions \(0,\ldots,n-1\). Positions of different parity differ by an odd number, of valuation zero. Under the odd-valuation rule, no word can have ones in both parity subsequences. Inside either chosen parity, dividing the position differences by two switches odd to even valuation. The two possible choices of active parity therefore have counts \(G(\lceil n/2\rceil)\) and \(G(\lfloor n/2\rfloor)\), with the empty word counted twice. This proves the formula for \(F\). Under the even-valuation rule cross-parity pairs are all allowed; inside each parity the required condition switches to odd valuation. The two restricted subsequences can be chosen independently, proving the product formula for \(G\). The base counts are immediate. Since padding by zero always works, \(p(n)=F(n)\) for every \(n\ge0\).

**2. Exact fourfold renormalization and closed values.** The two formulas with an even argument give, for every \(n\ge1\),
\[
F(4n)=2G(2n)-1=2F(n)^2-1.
\]
Write \(p(4^m)=a_m\) and \(p(2\cdot4^m)=b_m\). Both satisfy \(u_{m+1}=2u_m^2-1\), with \(a_0=2\) and \(b_0=3\). The identity \(2\cosh^2(t)-1=\cosh(2t)\) gives
\[
a_m=\cosh(2^m\operatorname{arcosh}2),\qquad
b_m=\cosh(2^m\operatorname{arcosh}3).
\]
Using \(\operatorname{arcosh}2=\log(2+\sqrt3)\) and \(\operatorname{arcosh}3=\log(3+2\sqrt2)\) yields the exact radical formulas. Iterating the fourfold identity from any fixed \(r\ge1\) proves \(p(r4^m)=\cosh(2^m\operatorname{arcosh}p(r))\), hence the stated general limit because \(\log\cosh t=t-\log2+o(1)\) as \(t\to\infty\). The two displayed constants differ, as certified for example by the enclosing intervals \((1.3169,1.3170)\) and \((1.2464,1.2465)\); hence a single square-root-normalized limit cannot exist.

**3. Growth exponent, entropy and unique invariance.** Word complexity is nondecreasing: every admissible word extends by zero. For \(4^m\le n<4^{m+1}\), monotonicity and the exact formulas bound \(\log p(n)\) between \(\log p(4^m)\) and \(\log p(4^{m+1})\), both comparable to \(\sqrt n\) with absolute positive constants. Therefore \(\log p(n)=\Theta(\sqrt n)\), yielding both the entropy assertion and the stated log-log complexity exponent.

There is also a uniform sparsity estimate. Among any \(4^m\) consecutive sites the support can contain at most \(2^m\) ones: at each of the \(m\) even positions in the low-to-high binary-residue tree only one of the two descendants can be occupied, and at each intervening odd position at most two descendants can be occupied. This estimate is sharp: choosing indices whose even-positioned binary digits all vanish realizes exactly \(2^m\) sites in a length-\(4^m\) block. Hence any length-\(n\) word has at most \(2\sqrt n\) ones. For any shift-invariant Borel probability \(\mu\), stationarity gives
\[
n\mu(\{x:x_0=1\})=\int\sum_{i=0}^{n-1}x_i\,d\mu(x)\le2\sqrt n.
\]
Letting \(n\to\infty\) shows the cylinder \(\{x:x_0=1\}\) has measure zero. Translation invariance and countable additivity force \(\mu\) to be the Dirac mass at the all-zero sequence. Since each configuration (and each pair of configurations) has arbitrarily long all-zero windows, one also obtains proximality directly by shifting to a window where the union of both sparse supports vanishes.

**4. Other structure.** A periodic configuration containing a one at \(i\) with period \(d>0\) must also contain ones at \(i+d\) and \(i+2d\). But \(\nu_2(2d)=\nu_2(d)+1\); the two differences cannot both have odd valuation. Thus the only periodic point is zero. The set of nonnegative integers whose binary digits at even-indexed positions are all zero has pairwise differences of odd valuation. Assigning ones to an arbitrary subset of this infinite set and zeros elsewhere produces continuum many points of \(X\). Finally, a zero-entropy sofic shift has polynomial word growth: in a finite right-resolving presentation, subexponential distinct-label growth forces the path adjacency matrix to have spectral radius at most one, and finite matrix powers then grow at most polynomially. Our \(p(n)=\exp(\Theta(\sqrt n))\) is superpolynomial, so \(X\) is not sofic.

## Verification

The included standalone `verify.py` implements the exact recursions and independently enumerates binary masks rather than reusing the recurrence to test finite words. It checked **both valuation rules at every length from 1 through 18**, the fourfold identity for every \(1\le n\le1000\), both closed-form integer-doubling sequences through \(m=8\), maximum support at lengths 1, 4 and 16, and separated numerical enclosures for both limiting constants. Its output begins `VERIFY_OK` on successful execution. The exhaustive mask checks provide finite corroboration, while the four steps above prove the all-length and infinite-system assertions.

## Relationship to prior work

Spacing shifts and their general entropy, recurrence and proximality properties were developed in the works listed below. In particular, [1] characterizes zero entropy for general spacing shifts, [2] supplies general hereditary-shift equivalences, and [3] analyzes proximal, periodic and chaotic behavior in examples. Those broad results cover generic consequences such as zero entropy implying proximality; they do **not**, in the material inspected, supply the valuation-parity distance rule's exact all-length recursion, the fourfold renormalization, or the distinct square-root constants. The integer subsequences in the two dyadic formulas are **not new numerical sequences**: they coincide with the already catalogued Chebyshev/Lucas–Lehmer sequences [4] and [5]. The proposed contribution is their exact dynamical realization and the complete word-complexity recursion together with its nonconvergent normalization, not rediscovery of those integer values or the general theory of hereditary shifts.

## Limitations

No complete description of the accumulation set of \(\log p(n)/\sqrt n\) over *all* integers \(n\) is claimed; only exact constants along every fixed four-adic dilation family are proved. The proof does not claim an analogous classification for arbitrary valuation congruences, other primes, or unrelated spacing shifts. Historical priority may be affected by an unindexed study of independent sets on two-adic hierarchical graphs, even if not expressed in spacing-shift terminology. General uniquely ergodic and proximal consequences were known, and numerical Chebyshev subsequences were tabulated independently of this dynamical example.

## References

[1] D. Ahmadi Dastjerdi and M. Dabbaghian Amiri, *Characterization of Entropy for Spacing Shifts*, arXiv:1110.6144v1, first posted 2011-10-27; journal version in *Acta Mathematica Universitatis Comenianae* 81 (2012), 221–226.

[2] D. Kwietniak, *Topological entropy and distributional chaos in hereditary shifts with applications to spacing shifts and beta shifts*, arXiv:1111.0190v1, first posted 2011-11-01; *Discrete and Continuous Dynamical Systems* 33 (2013), 2451–2467, DOI:10.3934/dcds.2013.33.2451.

[3] J. Banks, T. T. D. Nguyen, P. Oprocha, B. Stanley and B. Trotta, *Dynamics of spacing shifts*, *Discrete and Continuous Dynamical Systems* 33 (2013), 4207–4232, DOI:10.3934/dcds.2013.33.4207.

[4] OEIS A002812, integer sequence with initial value 2 and iteration \(a\mapsto2a^2-1\). https://oeis.org/A002812

[5] OEIS A001601, integer sequence with initial value 3 and iteration \(b\mapsto2b^2-1\). https://oeis.org/A001601
