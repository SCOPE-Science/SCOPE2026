# Sharper quantitative sparsity in the prime-gap distinct-product construction

## Result

Consider the prime-gap greedy set \(A\) from Przemek Chojecki's *Distinct Consecutive Products*: every prime is retained, and the interior of each consecutive-prime gap is either retained in full or rejected in full according to the collision test. For a rejected gap \(v=(p_v,q_v)\), write
\[
x(v)=q_v,\qquad d(v)=q_v-p_v.
\]
With the paper's fixed choice \(\theta=1/20\), call \(v\) short when \(d(v)\le p_v^\theta\), and raw when it admits a canonical witness whose earlier block crosses no earlier rejected gap.

The raw-gap count and the total short-gap deletion admit the sharper bounds
\[
\#\{v:\ v\text{ raw and short},\ x(v)\le X\}
   =O(X^{3/4+o(1)})
\]
and
\[
\boxed{\sum_{\substack{v\text{ short rejected}\\x(v)\le X}}d(v)
   =O(X^{13/16+o(1)})}.
\]
The latter improves Chojecki's \(X^{9/10+o(1)}\) bound and the later
\(X^{43/50+o(1)}\) length-sensitive refinement in the public audit of
Sneiderman.

The same calculation can be parameterized. For any fixed
\[
2/43<\theta\le 1/20
\]
sufficiently close to \(2/43\), the raw short-gap count is
\[
O\!\left(X^{1/2+5\theta+o(1)}\right),
\]
and the length-sensitive forest summation gives
\[
O\!\left(
X^{\,1/2+(13/2)\theta-5\theta^2+o(1)}
\right)
\]
for the total length of the corresponding short rejected gaps. Hence, for
every \(\varepsilon>0\), one may choose \(\theta>2/43\) so that this short-gap
mass is
\[
O_\varepsilon\!\left(
X^{2927/3698+\varepsilon}
\right),
\qquad
\frac{2927}{3698}=0.7915089237\ldots.
\]

Finally, the canonical set \(A\) itself satisfies a quantitative density-one
statement stronger than the published \(o(X)\) conclusion:
\[
\boxed{
\forall C>0,\qquad
|[1,X]\setminus A|
=O_C\!\left(\frac{X}{(\log X)^C}\right).
}
\]
The distinct-consecutive-product property of \(A\) is unchanged.

## Proof

### 1. Stratifying the split-product curve bound

For a raw witness, Chojecki reduces the collision to
\[
\prod_{i=0}^{r-1}(x-i)
=
\prod_{j=0}^{s-1}(y+j),
\qquad r>s\ge1,
\]
with \(x,y\le X\). If the rejected gap is short, then
\[
s\le X^\theta,\qquad
r\le L:=\lceil X^\theta\log_2X\rceil.
\]

Write
\[
h=(r,s),\qquad r=uh,\qquad s=vh,\qquad (u,v)=1,\quad u>v.
\]
Chojecki's split-product proposition gives, for each fixed \((r,s)\),
\[
N_{r,s}(X)
\ll
X^{1/u}(r^3\log X+r^4).
\]
The published raw-gap proof replaces \(u\) uniformly by \(2\) and then sums
over all \(O(L^2)\) pairs \((r,s)\). The loss from that replacement is
avoidable.

If \(u=2\), coprimality and \(u>v\) force \(v=1\). Thus
\[
(r,s)=(2h,h),
\]
so there are only \(O(L)\) such pairs, and
\[
\sum_{u=2}N_{r,s}(X)
\ll
X^{1/2}\sum_{h\le L/2}
\bigl((2h)^3\log X+(2h)^4\bigr)
=
O(X^{1/2}L^5\log X).
\]
If \(u\ge3\), then \(X^{1/u}\le X^{1/3}\). Summing crudely over all
\(s<r\le L\) gives
\[
\sum_{u\ge3}N_{r,s}(X)
\ll
X^{1/3}L^6\log X.
\]
Therefore, for any fixed \(\theta<1/6\),
\[
\#\{\text{raw short rejected gaps up to }X\}
\ll
X^{\max(1/2+5\theta,\ 1/3+6\theta)+o(1)}
=
X^{1/2+5\theta+o(1)}.
\]
At \(\theta=1/20\), this is \(X^{3/4+o(1)}\), while the \(u\ge3\) part is
only \(X^{19/30+o(1)}\).

### 2. Feeding the improvement into the length-sensitive forest sum

Sneiderman's refinement of the \(t=0\) all-equal part of the witness forest
sums the lengths of descendants of a raw root before discarding scale
information. If the raw-root count exponent is \(A_0<1\), that argument gives
the exponent
\[
(1-\theta)A_0+2\theta
\]
for nonempty all-equal descendants.

With \(A_0=3/4\) and \(\theta=1/20\), this becomes
\[
(1-\theta)A_0+2\theta
=
\frac{19}{20}\frac34+\frac1{10}
=
\frac{13}{16}.
\]

The remaining forest contributions are smaller. Raw roots themselves,
weighted by their maximum short length, contribute exponent
\[
A_0+\theta=\frac45.
\]
For paths from a raw root with at least one unequal edge, put
\(\rho=(2-\theta)^{-1}=20/39\). Replacing the old raw exponent \(4/5\) by
\(3/4\) in the forest exponent gives, at the first unequal edge,
\[
E_1=\frac{103}{156},
\]
and subsequent terms decrease because the coefficient controlling the
\(\rho^t\) term is
\[
\frac34+\theta-\frac{4\theta}{1-\rho}
=\frac{37}{95}>0.
\]
The long-root branch is unchanged: its first exponent is
\[
L_1=1-\rho+5\theta=\frac{115}{156},
\]
and it decreases because
\[
(1-\rho)-\frac{4\theta\rho}{1-\rho}
=\frac{205}{741}>0.
\]
Thus
\[
\max\left\{
\frac{13}{16},\frac45,\frac{103}{156},\frac{115}{156}
\right\}
=\frac{13}{16},
\]
proving the fixed-\(\theta\) short-gap bound.

### 3. Approaching the short-interval threshold

For \(2/43<\theta\le1/20\), the same split-product stratification gives
\[
A(\theta)=\frac12+5\theta.
\]
The length-sensitive all-equal exponent is therefore
\[
F(\theta)
=(1-\theta)A(\theta)+2\theta
=
\frac12+\frac{13}{2}\theta-5\theta^2.
\]
The inequalities making the remaining forest paths smaller are strict at
\(\theta=2/43\), and hence remain valid for \(\theta\) in a right
neighborhood. Moreover Li's almost-all short-interval theorem is available
with exponent \(2/43+\eta\) for arbitrarily small fixed \(\eta>0\), so the
long-gap argument may be rerun for every fixed \(\theta>2/43\). Taking
\(\theta\downarrow2/43\) gives
\[
F(2/43)
=
\frac{2927}{3698}.
\]
This proves the stated \(2927/3698+\varepsilon\) short-gap consequence.

### 4. Quantitative density convergence

Li's theorem states that for every sufficiently large fixed \(B\), all but
\[
O\!\left(X(\log X)^{-B}\right)
\]
starting points in a dyadic interval have a prime in
\([n,n+n^{2/43+\eta}]\). Chojecki's long-gap conversion therefore yields,
for arbitrarily large fixed \(B\),
\[
\sum_{\substack{Y\le p<2Y\\p^+-p>p^\theta}}
(p^+-p)
\ll
Y(\log Y)^{-B}.
\]
The construction of \(A\) does not depend on \(B\). Summing dyadically gives
\[
\text{long rejected mass up to }X
=
O_B\!\left(X(\log X)^{-B}+X^{1/2}\right).
\]
The short rejected mass has a fixed power saving, for example
\(O(X^{13/16+o(1)})\) at \(\theta=1/20\). For any prescribed \(C>0\), choose
\(B>C\); both the short and long contributions are then
\(O_C(X(\log X)^{-C})\). Since the complement of \(A\) is exactly the union
of rejected gap interiors, apart from the initial integer, the asserted
quantitative density estimate follows.

## Context and significance

Chojecki's current preprint proves existence of a density-one set with
distinct products of all distinct consecutive blocks and gives the short-gap
mass bound \(O(X^{9/10+o(1)})\). A public reconstruction by Rob Sneiderman
independently expands the proof and improves this to
\(O(X^{43/50+o(1)})\) by a length-sensitive summation of all-equal
descendants. The present observation is complementary: it uses the reduced
degree ratio already present in the split-product curve estimate to improve
the raw-root exponent, and then combines that improvement with the
length-sensitive summation.

The resulting \(13/16\) exponent is strictly smaller than both \(43/50\) and
\(9/10\). The super-logarithmic density convergence is a separate quantitative
corollary of the arbitrary logarithmic exceptional-set power in Li's theorem
together with the fixed power saving for short gaps.

## Reproducibility

`artifacts/check_exponents.py` checks all rational exponent identities and
the comparisons used in the fixed-\(\theta\) forest calculation.
`artifacts/check-exponents-output.txt` records its output.

## Limitations

- The result sharpens quantitative estimates for Chojecki's particular
  prime-gap greedy construction; it does not claim an optimal deletion rate
  among all density-one constructions.
- The exponent \(2927/3698\) applies to the part classified as short after
  choosing \(\theta\) just above \(2/43\). The full complement is not shown
  to have a power saving because the available long-gap input supplies
  arbitrary logarithmic savings rather than a polynomial exceptional-set
  bound.
- Originality is to the best of our knowledge. The most relevant independently
  inspected prior refinement is Sneiderman's \(43/50\) bound, which does not
  stratify the raw curve count by the reduced degree ratio.
- Ryan Kielhorn's September 2026 Zenodo preprint
  *Distinct consecutive products in a density-one set via prime-gap deletions*
  is highly relevant. Its accessible abstract and formalization description
  were inspected, but the full mathematical preprint was not inspected here;
  it remains the principal residual originality risk because it uses a related
  prime-gap deletion strategy.

## References

1. Przemek Chojecki, *Distinct Consecutive Products*, arXiv:2609.17543.
   https://arxiv.org/abs/2609.17543
2. Rob Sneiderman, *A complete reconstruction of the gap-greedy proof for
   Erdős Problem 421*, public audit repository, pinned commit
   `318c112c7a70879d98d86d8c3d9a280d77dadb35`.
   https://github.com/Robby955/erdos-421-audit/tree/318c112c7a70879d98d86d8c3d9a280d77dadb35
3. Runbo Li, *Primes in almost all short intervals*, arXiv:2407.05651v6.
   https://arxiv.org/abs/2407.05651
4. Ryan Kielhorn, *Distinct consecutive products in a density-one set via
   prime-gap deletions*, Zenodo, DOI 10.5281/zenodo.21287064.
   https://doi.org/10.5281/zenodo.21287064
