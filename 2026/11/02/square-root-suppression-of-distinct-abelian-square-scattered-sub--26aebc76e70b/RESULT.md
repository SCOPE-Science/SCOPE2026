# Square-root suppression of distinct Abelian-square scattered subsequences

## Finding

A word is an **Abelian square** if it has the form \(xy\), where \(x\) and \(y\) are nonempty, have equal lengths, and have identical Parikh vectors (each letter occurs equally often in both halves). A scattered subsequence preserves order but need not occupy consecutive positions. Different embeddings of the same string are counted only once.

Let \(W_n\) be an independently generated binary word with fixed \(\Pr(W_n(i)=1)=p\in(0,1)\). Let \(A_{n,L}\) count its distinct Abelian-square scattered subsequence strings of length \(2L\), and put \(A_n=\sum_{L\ge1}A_{n,L}\). Define
\[
g_0(z)=\frac{(1-p)z}{1-pz},\qquad g_1(z)=\frac{pz}{1-(1-p)z}.
\]
The exact length-refined expectation generating function is
\[
\boxed{\sum_{n\ge0}\sum_{L\ge1}\mathbb E[A_{n,L}]z^nu^L
=\frac{1}{1-z}\left(\frac1{\sqrt{1-2u(g_0(z)^2+g_1(z)^2)+u^2(g_0(z)^2-g_1(z)^2)^2}}-1\right).}
\tag{1}
\]
All square roots in formal series are the branches with constant term \(1\). At \(u=1\), the ordinary generating function for \(\mathbb E[A_n]\) is obtained.

Writing \(t=\sqrt{p(1-p)}\), as \(n\to\infty\) with fixed \(0<p<1\),
\[
\boxed{\mathbb E[A_n]\sim \frac{(1+2t)\sqrt{1+t}}{4\sqrt\pi\,t^{3/2}}\frac{(1+t)^n}{\sqrt n}.}
\tag{2}
\]
If \(D_n\) counts **all** distinct nonempty scattered subsequence strings of \(W_n\), then
\[
\mathbb E[D_n]\sim \frac{1+2t}{2t}(1+t)^n,\qquad
\boxed{\frac{\mathbb E[A_n]}{\mathbb E[D_n]}\sim \sqrt{\frac{1+t}{4\pi t n}}.}
\tag{3}
\]
Thus the Abelian-square and unrestricted expectations have the same exponential growth rate, but the restricted expectation has a universal square-root suppression. This is a **ratio of expectations**, not the expectation of a random ratio. The exponential base \(1+\sqrt{p(1-p)}\) has its unique maximum at the fair source \(p=1/2\).

## Assumptions and scope

The ambient alphabet is the fixed, labeled binary alphabet \(\{0,1\}\). The source letters are independent and identically distributed, and both letter probabilities are strictly positive and fixed as \(n\) grows. The count is of distinct **strings** that are subsequences, not positional embeddings, factors, or strings realized by splitting the entire host. All subsequence lengths are admitted, but Abelian squares have a nonempty common half-length. The empty word is excluded. The normalization \(\mathbb E[A_0]=0\) follows from (1).

The deterministic endpoints illustrate a genuine boundary: if \(p\in\{0,1\}\), then every host is constant, \(A_n=\lfloor n/2\rfloor\), \(D_n=n\), and their ratio tends to \(1/2\), unlike (3) for every fixed interior \(p\).

## Proof

**1. Greedy waiting times.** Fix a nonempty binary pattern \(v=v_1\cdots v_m\). Embed it greedily into an infinite i.i.d. source by waiting for \(v_1\), then for \(v_2\), and so on. If \(T_v\) is the first completion time, then \(v\) occurs as a scattered subsequence of \(W_n\) exactly when \(T_v\le n\). Independent fresh-source tails show that the waiting gaps are independent geometric random variables on \(\{1,2,\ldots\}\), with probability generating functions \(g_{v_i}(z)\). Therefore
\[
\mathbb E[z^{T_v}]=\prod_{i=1}^m g_{v_i}(z),\qquad
\sum_{n\ge0}\Pr(T_v\le n)z^n=\frac{\prod_{i=1}^m g_{v_i}(z)}{1-z}.
\tag{4}
\]
Every fixed string contributes at most one indicator, independently of its embedding multiplicity. This justifies summing (4) over distinct patterns.

**2. Abelian-square enumeration.** Consider Abelian squares of length \(2L\). If each half contains exactly \(j\) zeros and \(L-j\) ones, there are \(\binom Lj^2\) distinct strings, and every one has \(2j\) zeros and \(2(L-j)\) ones. Summation of (4), with \(u\) marking \(L\), gives
\[
(1-z)\sum_{n\ge0}\sum_{L\ge1}\mathbb E[A_{n,L}]z^nu^L
=\sum_{L\ge1}u^L\sum_{j=0}^L\binom Lj^2g_0(z)^{2j}g_1(z)^{2(L-j)}.
\tag{5}
\]
The needed binomial-square identity is, as a formal series in \(a,b\),
\[
\sum_{L\ge0}\sum_{j=0}^L\binom Lj^2a^{2j}b^{2(L-j)}
=\operatorname{CT}_{w}\frac1{1-(aw+b)(aw^{-1}+b)}
=\frac1{\sqrt{1-2(a^2+b^2)+(a^2-b^2)^2}}.
\tag{6}
\]
The first equality follows by expanding the geometric series and retaining the zero Laurent exponent. For the second, the standard Laurent constant term of \((c-d(w+w^{-1}))^{-1}\) is \((c^2-4d^2)^{-1/2}\), which also follows by expanding \(\sum_{k\ge0}\binom{2k}{k}(d/c)^{2k}/c\). Substitute \(a=\sqrt u\,g_0(z)\), \(b=\sqrt u\,g_1(z)\) into (6); all surviving terms have integral powers of \(u\). Subtract the \(L=0\) term and divide by \(1-z\) to obtain (1).

**3. Exact dominant singularity.** Let \(S(z)=g_0(z)+g_1(z)\), \(T(z)=g_0(z)-g_1(z)\). At \(u=1\), the radical in (1) factors as
\[
1-2(g_0^2+g_1^2)+(g_0^2-g_1^2)^2=(1-S(z)^2)(1-T(z)^2).
\tag{7}
\]
Both \(g_0\) and \(g_1\) have strictly positive coefficients in every positive degree, and \(S(z)\) increases strictly from \(0\) to \(2\) as real \(z\) increases from \(0\) to \(1\). Thus there is exactly one \(r\in(0,1)\) satisfying \(S(r)=1\). Direct substitution yields, with \(t=\sqrt{p(1-p)}\),
\[
r=\frac1{1+t},\quad
v_0=g_0(r)=\frac{\sqrt{1-p}}{\sqrt{1-p}+\sqrt p},\quad
v_1=g_1(r)=\frac{\sqrt p}{\sqrt{1-p}+\sqrt p},\quad
v_0v_1=\frac t{1+2t}.
\tag{8}
\]
Differentiation gives
\[
\mu=rS'(r)=\frac{2(1+t)}{1+2t}>0.
\tag{9}
\]
In a neighborhood of \(z=r\),
\[
1-S(z)^2=2\mu(1-z/r)+O((1-z/r)^2),\qquad
1-T(r)^2=4v_0v_1.
\tag{10}
\]
For complex \(z\) on \(|z|=r\) with \(z\ne r\), strict triangle inequality applied to the positive full-support series of each \(g_i\) shows \(|g_i(z)|<g_i(r)\). Hence both \(|S(z)|<1\) and \(|T(z)|<1\), and the factors in (7) have no other singularities on \(|z|=r\). Their poles are outside the unit circle. The algebraic generating function therefore has a unique dominant square-root singularity and admits a dented disk continuation at \(r\).

Combining (7)--(10),
\[
\frac1{\sqrt{(1-S(z)^2)(1-T(z)^2)}}
=\frac{1+2t}{4\sqrt{t(1+t)}}(1-z/r)^{-1/2}
+O((1-z/r)^{1/2}).
\tag{11}
\]
The factor \((1-z)^{-1}\) in (1) is analytic and nonzero at \(r<1\). The standard transfer formula \([z^n](1-z/r)^{-1/2}\sim r^{-n}/\sqrt{\pi n}\) now proves (2).

**4. Unrestricted baseline and the ratio.** For all nonempty binary patterns, the weight sum over patterns of length \(m\) equals \(S(z)^m\). The same greedy argument therefore gives the unrestricted expectation generating function
\[
\sum_{n\ge0}\mathbb E[D_n]z^n=\frac1{1-z}\left(\frac1{1-S(z)}-1\right).
\tag{12}
\]
Near \(r\), \(1-S(z)=\mu(1-z/r)+O((1-z/r)^2)\). The simple-pole coefficient is thus \(((1-r)\mu)^{-1}\), which equals \((1+2t)/(2t)\) by (8)--(9). Dividing the two proved asymptotic expressions gives (3). The unique maximum of \(1+t\) follows from \(p(1-p)\le1/4\), with equality only at \(p=1/2\). The endpoint statement follows by inspecting constant words directly.

## Verification

The independent standard-library program `verify.py` implements three exact finite calculations: (i) explicit sets of all distinct scattered subsequences for every binary host of length at most \(12\), grouped by host Hamming weight; (ii) a pattern-first sum over geometric waiting-time distributions indexed by the Parikh vectors of both halves; and (iii) a separate formal power-series recurrence using \(H(z)^2(1-S(z)^2)(1-T(z)^2)=1\). The three methods agree as rational numbers for \(p\in\{1/2,1/3,2/5,1/5\}\) through host length \(12\), comprising \(8190\) explicitly generated nonempty hosts and \(52\) equalities including the empty host normalization. Both deterministic endpoint cases are checked.

Run with `python3 verify.py` from the directory containing the extracted file. Only the standard Python library is needed. The exact rational checks validate initial coefficients and normalization, but **do not** replace the singularity-analysis proof for all \(n\).

For the fair source, the first eleven expectations (at host lengths \(0\) through \(10\)) are \(0,0,1/2,1,7/4,11/4,133/32,49/8,1141/128,1649/128,9503/512\). The fair-source leading constant in (2) specializes to \(\sqrt{3/\pi}\).

## Relationship to prior work

Richmond and Shallit [2] give binomial/multinomial counts of **all Abelian-square strings by their own length**, including the central-binomial identity underlying (6); their result does not address the probability that each distinct pattern embeds in a finite random host. Bennink [4] improves enumeration of the unrestricted Abelian-square language, not its scattered-subsequence expectation. Biers-Ariel, Godbole and Kelley [3] study expected **unrestricted** distinct subsequences of random source words. Fici, Mignosi and Shallit [1] study distinct Abelian-square **contiguous factors**, while Rubinchik and Shur [5] study random contiguous palindrome and square factors. None of the inspected material gives the binary biased-source length-refined generating function (1) or the fixed-bias suppression constant (3).

The binomial-square identity, geometric waiting times and transfer theorems are classical and are not presented as new. The assessed result is their exact combination for a distinct constrained **scattered**-pattern expectation, with its bias-dependent leading constant and ratio. A broader weighted-language counting theorem might potentially subsume this specialization; the mathematical novelty requires independent literature review.

## Limitations

The theorem is for the binary alphabet and fixed, independent, identically distributed, strictly positive letter probabilities. It does not establish the corresponding formula for correlated, nonstationary, or larger-alphabet sources. Asymptotics are pointwise in fixed \(p\), not uniform as \(p\) approaches \(0\) or \(1\). The theorem concerns the **ratio of expectations**, not concentration of the random count or the expectation of its ratio to all distinct subsequences. Exhaustive finite checks are reproducibility evidence only. Publication or mathematical priority has not been independently certified.

## References

1. G. Fici, F. Mignosi and J. Shallit, *Abelian-Square-Rich Words*, first public arXiv posting 2017-01-04, arXiv:1701.00948, https://arxiv.org/abs/1701.00948.
2. L. B. Richmond and J. Shallit, *Counting Abelian Squares*, arXiv:0807.5028 (2008), https://arxiv.org/abs/0807.5028.
3. Y. Biers-Ariel, A. Godbole and E. Kelley, *Expected Number of Distinct Subsequences in Randomly Generated Binary Strings*, arXiv:1704.08661 (first public 2017-04-27), https://arxiv.org/abs/1704.08661.
4. R. S. Bennink, *Counting Abelian Squares More Efficiently*, arXiv:2203.11886 (2022), https://arxiv.org/abs/2203.11886.
5. M. Rubinchik and A. M. Shur, *The Number of Distinct Subpalindromes in Random Words*, arXiv:1505.08043 (2015), https://arxiv.org/abs/1505.08043.
