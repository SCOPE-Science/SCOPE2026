# Sharp local gap widths for the Sturmian beta staircase

## Finding

For an irrational slope \(\alpha\in(0,1)\), put \(a_j(\alpha)=\lceil(j+1)\alpha\rceil-\lceil j\alpha\rceil\), \(j\ge0\), and let \(\beta(\alpha)\in(1,2)\) be the unique root of
\[
\sum_{j\ge0} a_j(\alpha)\beta(\alpha)^{-j-1}=1.
\]
Write \(\mathcal B=\{\beta(\alpha):\alpha\in(0,1)\setminus\mathbb Q\}\) and \(C=\overline{\mathcal B}\) in \([1,2]\). Denote Kwon's left and right staircase limits at a reduced rational \(p/q\in(0,1)\) by \(b^-_{p/q}\) and \(b^+_{p/q}\). Their open interval is a complementary gap of \(C\).

**Local gap-width law.** For any reduced rationals \(p_k/q_k\to\alpha\in(0,1)\setminus\mathbb Q\), set \(B_k=b^-_{p_k/q_k}\) and \(\beta=\beta(\alpha)\). Then
\[
\lim_{k\to\infty} (b^+_{p_k/q_k}-b^-_{p_k/q_k}) B_k^{q_k}
=\frac{1-\beta^{-1}}{\displaystyle\sum_{j=0}^{\infty}(j+1)a_j(\alpha)\beta^{-j-2}}>0.
\]
The normalization uses the left endpoint of each gap, not the limiting base. No rate of rational approximation is required.

**Metric cover.** For every \(\varepsilon>0\) and integer \(n\ge1\), the truncated set \(C\cap[1+\varepsilon,2]\) can be covered by at most \(\sum_{q=1}^n\varphi(q)\le n^2\) intervals of length at most \(4\varepsilon^{-1}(1+\varepsilon)^{-n}\), where \(\varphi(1)=1\). In particular each nonempty truncated set has upper box dimension zero, and \(C\) has Hausdorff dimension zero.

## Assumptions and scope

Only the binary maximal characteristic Sturmian expansions of \(1\) at irrational slopes enter \(\mathcal B\); their identification with the displayed root parametrization is due to Chi and Kwon. The rational limit bases and the endpoints \(1,2\) of the base range enter the closure, not \(\mathcal B\). The results do not apply to all emergent beta parameters or all beta-shifts lacking typical periodic optimization. No global upper box dimension statement at the accumulation endpoint 1 is made, and the limit is not asserted when the slopes converge to a rational.

## Prior staircase formulas in the ceiling convention

Kwon's staircase \(\Delta\) restricted to irrational slopes in \((0,1)\) is \(\beta(\alpha)\). Its strict increase, continuity at irrationals and jumps at rationals are in his Theorem 2.7. His Propositions 3.2–3.3 give the expansions and root polynomials of the two rational limits. Here is the translation into ceiling digits, also recording the exact difference of the two digit series used below.

For \(p/q\) reduced, put \(u_j=\lceil(j+1)p/q\rceil-\lceil jp/q\rceil\) for \(0\le j<q\), and set \(P_{p,q}(t)=\sum_{j=0}^{q-1}u_jt^{j+1}\). This digit block is the upper Christoffel period \(1z_{p,q}0\) in Kwon's notation. As the slope approaches \(p/q\) from below, \(\lceil m\alpha\rceil\) equals \(\lceil mp/q\rceil\) eventually for every fixed \(m\ge1\). From above it is eventually larger by one exactly when \(q\mid m\). Hence the limiting left and right power series in \(t\) are
\[
F^-_{p/q}(t)=\frac{P_{p,q}(t)}{1-t^q},\qquad
F^+_{p/q}(t)=\frac{P_{p,q}(t)+(1-t)t^q}{1-t^q}.
\]
The limits are binary, start with one, and have infinitely many ones and zeros. Evaluated at \(t=1/b\), each series is strictly decreasing from infinity to a value below one as \(b\) runs from 1 to 2. Root convergence follows by uniform convergence of digit series on compact base intervals in \((1,2]\) and by bracketing each limiting root. Thus \(F^-_{p/q}(1/b^-_{p/q})=F^+_{p/q}(1/b^+_{p/q})=1\) and \(b^-_{p/q}<b^+_{p/q}\). Explicitly the endpoint equations, equivalent to Kwon's integer polynomials, are
\[
P_{p,q}(1/b^-_{p/q})=1-(b^-_{p/q})^{-q},\qquad
P_{p,q}(1/b^+_{p/q})+(2-(b^+_{p/q})^{-1})(b^+_{p/q})^{-q}=1.
\]
For example, at \(1/2\) the left base is the golden ratio and the right base is the largest real root of \(b^3-b^2-2b+1=0\).

The complement is obtained by taking the slope cut at any base outside \(C\). An irrational cut is excluded by continuity there. The limits at the range ends are 1 and 2 by convergence of the corresponding digit strings to \(1000\ldots\) and \(1111\ldots\), respectively, tested at fixed bases in \((1,2)\), so the cut is internal. At a rational cut the two one-sided limits belong to \(C\) and the base is strictly between them. Conversely such gaps contain no points of \(C\) by strict monotonicity. The closed set is perfect, since every value at an irrational slope is approached by distinct such values, and no isolated point can be added by closure. The metric cover below gives empty interior and hence total disconnectedness. We include this Cantor-set description for context, not as a claim of priority for the staircase or its gap endpoints.

## Proof of the local width law

Use reduced rationals \(p_k/q_k\to\alpha\) with \(\alpha\) irrational. Then \(q_k\to\infty\). Given a fixed prefix length, the irrational slope avoids all discontinuities of the finitely many ceiling functions that determine the prefix. For sufficiently large \(k\) the two rational limit prefixes both agree with the irrational prefix. The digit series therefore converge locally uniformly in base, and bracketing about the strictly decreasing irrational series' root gives \(B_k,b^+_{p_k/q_k}\to\beta\).

Write \(G_k(b)=F^+_{p_k/q_k}(1/b)\). At the left root,
\[
G_k(B_k)-1=\frac{(1-B_k^{-1})B_k^{-q_k}}{1-B_k^{-q_k}}.
\]
The mean-value theorem, comparing against \(G_k(b^+_{p_k/q_k})=1\), gives for some \(\xi_k\in(B_k,b^+_{p_k/q_k})\)
\[
(b^+_{p_k/q_k}-B_k)B_k^{q_k}
=\frac{1-B_k^{-1}}{(1-B_k^{-q_k})[-G_k'(\xi_k)]}.
\]
On any compact base interval around \(\beta\) bounded below by \(b_0>1\), the derivative-term bounds \((j+1)b_0^{-j-2}\) are summable, and the stabilized prefixes give convergence of the derivatives uniformly there. Since \(\xi_k\to\beta\), the positive derivative magnitude tends to \(\sum_{j\ge0}(j+1)a_j(\alpha)\beta^{-j-2}\), positive by \(a_0(\alpha)=1\). Finally \(B_k^{-q_k}\to0\). This proves the limit for arbitrary rational approaches, not only convergents.

## Proof of the metric cover

Deleting the rationals of reduced denominator at most \(n\) splits \((0,1)\) into \(1+\sum_{q=2}^n\varphi(q)\) open cells. The length-\(n\) ceiling prefix is constant on every cell, so this also bounds the number of prefixes represented at irrational slopes. For a prefix \(w\) let \(H_w(b)=\sum_{j=0}^{n-1}w_j b^{-j-1}\). A base \(b\ge1+\varepsilon\) with that prefix has
\[
1-\varepsilon^{-1}(1+\varepsilon)^{-n}\le H_w(b)\le1
\]
by the bound \(b^{-n}/(b-1)\) on the rest of the series. The inequalities apply also to closure points in \([1+\varepsilon,2]\): take a subsequence of irrational-slope bases with one fixed length-\(n\) prefix and pass to the limit using the tail bound at their bases. Since \(w_0=1\), \(-H_w'(b)\ge b^{-2}\ge1/4\) there. Bases belonging to a single prefix thus lie in an interval of the claimed length. The counting bound is polynomial in \(n\) and the length bound decreases exponentially, giving upper box dimension zero (the successive length scales have a fixed ratio). The countable union of the truncated sets with \(\varepsilon=1/m\), together with \(\{1\}\), is \(C\); hence the Hausdorff dimension is zero.

## Verification

The supplied standard-library `verify.py` uses exact rational identities for bounded rational slopes and prefix counts, and high-precision root bisection for the two endpoints. It also compares the normalized widths along convergents to \(\sqrt2-1\) with the constant in the local limit. These are finite consistency checks, not proofs of either quantitative assertion or priority for the endpoint equations.

## Relationship to prior work

Kwon gives the same staircase and the lower and upper self-Christoffel endpoint polynomials in Theorem 2.7 and Propositions 3.2–3.3; the gap labels and both endpoint equations above are consequences of these results. His Lemma 2.5 provides a common-prefix stability estimate for series roots; the metric cover uses the number of rational-cut cells to control all prefixes simultaneously and gives an explicit scale and covering count. Kwon's measure-zero conclusion for the staircase range is distinct from the box-dimension estimate. His slope-derivative analysis concerns changes in the staircase relative to changes in slope, whereas the limit above compares the two one-sided bases **at the same rational slope**, normalizing the jump by the denominator power and retaining its leading coefficient. Chi–Kwon establish the underlying parametrization and transcendence of the irrational-slope bases. Anagnostopoulou–Jenkinson study Farey constructions of periodic words and symbolic supports. Huang–Jenkinson–Xu–Zhang motivate interest in the locus through failure of typical periodic optimization. No absolute priority is asserted for the quantitative claims.

## References

1. D. Kwon, *A devil’s staircase from rotations and irrationality measures for Liouville numbers*, arXiv:0709.1642, especially Lemma 2.5, Theorem 2.7 and Propositions 3.2–3.3, https://arxiv.org/abs/0709.1642.
2. D. P. Chi and D. Kwon, *Sturmian words, beta-shifts, and transcendence*, Theoretical Computer Science **321** (2004), 395–404, https://arxiv.org/abs/math/0308140.
3. V. Anagnostopoulou and O. Jenkinson, *Which beta-shifts have a largest invariant measure?*, Journal of the London Mathematical Society **79** (2009), 445–464, https://webspace.maths.qmul.ac.uk/o.m.jenkinson/betamax11.pdf.
4. W. Huang, O. Jenkinson, L. Xu, and Y. Zhang, *Sturmian beta-shifts do not have typical periodic optimization*, arXiv:2610.03619v1, https://arxiv.org/abs/2610.03619.
