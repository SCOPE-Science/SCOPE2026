# Quantitative deficiency exponents for distinct consecutive products

## Result

Let \(A\subseteq\mathbb N\) be the prime-gap retain/reject set constructed in Przemek Chojecki, *Distinct Consecutive Products* (arXiv:2609.17543v1): every prime is retained, and the interior of a consecutive-prime gap is retained unless adjoining it would create two distinct consecutive blocks with equal product. The construction itself is independent of the auxiliary short-gap exponent used to estimate its density.

For a rejected prime gap \((p,p^+)\), call it \(\theta\)-short when \(p^+-p\le p^\theta\). Then the following quantitative refinement holds.

**Theorem.** For every \(\varepsilon>0\), the number of short raw rejected gaps with right endpoint at most \(X\) is
\[
O_\varepsilon\!\left(X^{17/24+\varepsilon}\right),
\]
and the sum of the lengths of all short rejected gaps with right endpoint at most \(X\) is
\[
O_\varepsilon\!\left(X^{19/24+\varepsilon}\right).
\]
Moreover, for every \(B>0\),
\[
\#([1,X]\setminus A)
\ll_{\varepsilon,B}
X^{19/24+\varepsilon}+\frac{X}{(\log X)^B}.
\]
In particular, the same set \(A\) has deficiency smaller than \(X/(\log X)^B\) for every fixed \(B>0\).

The exponents arise from a more general transfer statement. Suppose one has a prime-in-almost-all-short-intervals theorem at exponent \(\eta\): for each fixed \(B>0\) and every sufficiently small \(\delta>0\), all but \(O_B(X(\log X)^{-B})\) integers \(n\in[X,2X]\) have a prime in an interval of length \(n^{\eta+\delta}\). If \(\eta<1/20\), then Chojecki's construction satisfies, for every \(\varepsilon>0\),
\[
N_{\rm raw}(X)=O_\varepsilon\!\left(X^{1/2+5\eta+\varepsilon}\right),
\]
\[
L_{\rm short}(X)=O_\varepsilon\!\left(X^{1/2+7\eta+\varepsilon}\right),
\]
and
\[
\#([1,X]\setminus A)
\ll_{\varepsilon,B}
X^{1/2+7\eta+\varepsilon}+\frac{X}{(\log X)^B}.
\]
Runbo Li's *Primes in almost all short intervals III* gives \(\eta=1/24\), yielding \(17/24\) and \(19/24\).

## Context

Chojecki proves that \(A\) has natural density one and that all distinct consecutive blocks in the increasing enumeration of \(A\) have distinct products. The quantitative part of the published argument uses two ingredients:

- a uniform integral-point estimate on the split-product curves
  \[
  \prod_{i=0}^{r-1}(x-i)=\prod_{j=0}^{s-1}(y+j),\qquad r>s,
  \]
  where, writing \(h=(r,s)\), \(r=ph\), \(s=qh\), every absolute irreducible component has degree at least \(p\);
- a forest of rejected prime gaps in which unequal parent-child edges contract scale by \(\rho=1/(2-\theta)\), while equal-edge strings admit a direct compression bound.

In arXiv:2609.17543v1 the integral-point estimate is uniformly weakened to the worst case \(p=2\) before summing over all \((r,s)\), producing \(O(X^{4/5+o(1)})\) raw short gaps for \(\theta=1/20\), and then \(O(X^{9/10+o(1)})\) total short rejected length. The point below is that the degree-two case is extremely sparse in the \((r,s)\)-sum.

## Proof

### 1. The degree-two locus is one-dimensional

For fixed \(r>s\), put
\[
h=(r,s),\qquad r=ph,\qquad s=qh,\qquad (p,q)=1.
\]
Chojecki's split-product proposition gives
\[
N_{r,s}(X)
\ll
X^{1/p}(r^3\log X+r^4).
\]
The condition \(p=2\) forces \(q=1\), because \(q<p\) and \((p,q)=1\). Hence
\[
p=2\quad\Longleftrightarrow\quad r=2s.
\]
Thus the worst \(X^{1/2}\) contribution occurs for only \(O(L)\) pairs rather than \(O(L^2)\) pairs, where for a \(\theta\)-short raw witness the source argument gives
\[
r\le L=\lceil X^\theta\log_2X\rceil.
\]
Summing the degree-two locus gives
\[
\sum_{s\le L/2}N_{2s,s}(X)
\ll
X^{1/2}(L^4\log X+L^5).
\]
For all remaining pairs one has \(p\ge3\), hence
\[
\sum_{\substack{s<r\le L\\r\ne2s}}N_{r,s}(X)
\ll
X^{1/3}(L^5\log X+L^6).
\]
Therefore, for every fixed \(\theta<1/6\),
\[
N_{\rm raw}(X)
\ll
X^{1/2+5\theta+o(1)}+X^{1/3+6\theta+o(1)}
=
X^{1/2+5\theta+o(1)}.
\]
This replaces the source exponent \(1/2+6\theta\) by \(1/2+5\theta\).

### 2. Propagation through the witness forest

The source forest lemmas are unchanged when the auxiliary cutoff \(\theta\) is allowed to vary in a fixed compact subinterval of \((0,1/20]\). At child scale \(Z\), an unequal step followed by a compressed equal string contributes at most
\[
Z^{4\theta+o(1)},
\]
and backwards across a short unequal edge the scale contracts to
\[
O(Z^\rho),\qquad \rho=\frac1{2-\theta}.
\]
A path rooted at a raw short gap and containing exactly \(t\ge0\) unequal edges therefore contributes, after including the terminal gap length, exponent
\[
E_{\rm raw}(t)
=
\left(\frac12+5\theta\right)\rho^t
+\frac{4\theta(1-\rho^t)}{1-\rho}
+\theta\rho^t+\theta.
\]
Collecting the \(\rho^t\) coefficient gives
\[
E_{\rm raw}(t)
=
\frac{4\theta}{1-\rho}+\theta
+
\rho^t\left(
\frac12+6\theta-\frac{4\theta}{1-\rho}
\right).
\]
For \(0<\theta\le1/20\), the coefficient in parentheses is positive. Hence this exponent decreases with \(t\), and its maximum occurs at \(t=0\):
\[
E_{\rm raw}(0)=\frac12+7\theta.
\]

For a path whose first ancestor is a long gap, the source argument gives
\[
E_{\rm long}(t)
=(1-\rho)\rho^{t-1}
+\frac{4\theta(1-\rho^t)}{1-\rho}
+\theta,
\qquad t\ge1.
\]
Again this decreases with \(t\) throughout \(0<\theta\le1/20\), so its maximum is
\[
E_{\rm long}(1)=1-\rho+5\theta.
\]
In this range
\[
1-\rho+5\theta<\frac12+7\theta,
\]
so the raw-rooted paths dominate. The same harmless summation over scale tuples as in the source therefore gives
\[
L_{\rm short}(X)
=
O\!\left(X^{1/2+7\theta+o(1)}\right).
\]

### 3. Optimizing the cutoff with the current short-prime input

Li proves in *Primes in almost all short intervals III* that for every sufficiently small \(\delta>0\), outside \(O_B(X(\log X)^{-B})\) exceptional integers, the interval
\[
[n-n^{1/24+\delta},n]
\]
contains primes, with \(B\) arbitrarily large after enlarging constants. Choose
\[
\frac1{24}+\delta<\theta<\frac1{20}
\]
and let \(\theta\downarrow1/24\). Then
\[
\frac12+5\theta\downarrow\frac{17}{24},
\qquad
\frac12+7\theta\downarrow\frac{19}{24}.
\]
This proves the stated \(17/24+\varepsilon\) and \(19/24+\varepsilon\) bounds.

The same exceptional-set argument used for long gaps in the source is quantitative. A long gap of length \(g>p^\theta\), with \(\theta>1/24+\delta\), supplies \(\gg g\) exceptional starting points for Li's theorem. Distinct prime gaps supply disjoint sets of starting points. Summing dyadically gives, for every fixed \(B>0\),
\[
L_{\rm long}(X)=O_B\!\left(\frac{X}{(\log X)^B}\right).
\]
Since the complement of \(A\) is, apart from a bounded initial set, the union of interiors of rejected prime gaps, the full deficiency estimate follows.

## Numerical exponent check

At the limiting value \(\theta=1/24\),
\[
\rho=\frac{24}{47},\qquad
\frac12+5\theta=\frac{17}{24},\qquad
\frac12+7\theta=\frac{19}{24},
\]
while the long-root exponent is
\[
1-\rho+5\theta=\frac{787}{1128}<\frac{19}{24}.
\]
The coefficients controlling monotonicity are also strictly positive:
\[
\frac12+6\theta-\frac{4\theta}{1-\rho}=\frac{113}{276}>0,
\]
\[
(1-\rho)-\frac{4\theta\rho}{1-\rho}=\frac{341}{1081}>0.
\]
A compact exact-arithmetic verification is included in `artifacts/verify_exponents.py`.

## Originality and literature boundary

To the best of our knowledge, the quantitative refinement above is not stated in the inspected literature. Chojecki's current arXiv version states the \(4/5\) raw-gap and \(9/10\) short-length exponents, obtained by applying the \(p=2\) estimate uniformly before the \((r,s)\)-sum. Li's later short-prime theorem supplies the stronger \(1/24\) input with a logarithmically small exceptional set. Searches for the resulting \(17/24\), \(19/24\), the relation \(p=2\iff r=2s\), and equivalent quantitative-deficiency formulations did not identify prior coverage.

A closely related September 2026 Zenodo preprint by Ryan Kielhorn, *Distinct consecutive products in a density-one set via prime-gap deletions* (DOI 10.5281/zenodo.21287064), is a material residual originality risk because its abstract describes a separate prime-gap deletion proof of the same density-one headline theorem. Its available indexed metadata and abstract do not state the \(17/24\) or \(19/24\) refinements, but its full preprint text was not inspected here; consequently no claim is made that it omits every comparable quantitative estimate.

## Limitations

The result is a quantitative refinement of the specific prime-gap greedy construction, not an optimality theorem for the Erdős--Graham problem. No matching lower bound for the deficiency is claimed. The overall deficiency is limited by current exceptional-set control for long prime gaps; the power-saving \(19/24+\varepsilon\) estimate applies to the short rejected part, while the full complement is bounded by an arbitrary negative power of \(\log X\). The argument inherits the structural construction, split-product proposition, and witness-forest lemmas of arXiv:2609.17543v1; the present contribution is the sparse degree-two summation, the resulting transfer exponents, and their optimization with the later \(1/24\) short-prime theorem.

## References

1. P. Chojecki, *Distinct Consecutive Products*, arXiv:2609.17543v1 (2026), https://arxiv.org/abs/2609.17543.
2. R. Li, *Primes in almost all short intervals III*, manuscript, https://runbolicarey.com/assets/downloads/Primes_in_almost_all_short_intervals_III.pdf.
3. W. Castryck, R. Cluckers, P. Dittmann, K. H. Nguyen, *The dimension growth conjecture, polynomial in the degree and without logarithmic factors*, Algebra & Number Theory 14 (2020), 2261--2294.
4. R. Kielhorn, *Distinct consecutive products in a density-one set via prime-gap deletions*, Zenodo (2026), DOI: 10.5281/zenodo.21287064.
