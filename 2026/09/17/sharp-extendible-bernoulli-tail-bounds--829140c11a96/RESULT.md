# Exact Bernoulli tail envelopes under infinite exchangeability

**SCOPE Phase II research record.**  
**Record ID:** SCOPE-20260917-829140c11a96  
**Scope Run ID:** 2026-09-17T14:59:51Z-fbc82dda-4274-4501-a8dc-b18695ad57a8

## 1. Question

Let \(X_1,X_2,\ldots\) be an infinitely exchangeable Bernoulli sequence with the
single marginal constraint
\[
\mathbb E X_1=p\in[0,1],
\qquad
S_n=\sum_{i=1}^n X_i.
\]
For fixed \(1\le k\le n\), what is the exact possible range of
\(\mathbb P(S_n\ge k)\)?

For arbitrary *finite* exchangeable Bernoulli \(n\)-vectors, Zaigraev and
Kaniovski (2010) give the sharp marginal-only interval
\[
\max\!\left\{\frac{np-k+1}{n-k+1},0\right\}
\le \mathbb P(S_n\ge k)
\le \min\!\left\{\frac{np}{k},1\right\}.
\]
Infinite extendibility is a genuine additional constraint. The result below gives
its exact finite-\(n\) effect and shows that this improvement disappears
asymptotically at proportional thresholds.

## 2. Definitions

Write
\[
g_{n,k}(\theta)
=\mathbb P\{\operatorname{Bin}(n,\theta)\ge k\}
=\sum_{j=k}^n {n\choose j}\theta^j(1-\theta)^{n-j}.
\]

For \(2\le k\le n-1\), let \(\tau_{n,k}\) be the unique solution in
\(((k-1)/(n-1),1)\) of
\[
\tau\, g'_{n,k}(\tau)=g_{n,k}(\tau).
\]
Equivalently, the line from the origin to
\((\tau_{n,k},g_{n,k}(\tau_{n,k}))\) is tangent to the binomial upper-tail
curve.

Define \(U_{n,k}:[0,1]\to[0,1]\) by
\[
U_{n,1}(p)=1-(1-p)^n,\qquad U_{n,n}(p)=p,
\]
and, for \(2\le k\le n-1\),
\[
U_{n,k}(p)=
\begin{cases}
\dfrac{p}{\tau_{n,k}}\,g_{n,k}(\tau_{n,k}),&0\le p\le\tau_{n,k},\\[6pt]
g_{n,k}(p),&\tau_{n,k}\le p\le1.
\end{cases}
\]
Finally set
\[
L_{n,k}(p)=1-U_{n,n-k+1}(1-p).
\]

## 3. Main theorem: the exact feasible interval

For every infinitely exchangeable Bernoulli sequence with
\(\mathbb E X_1=p\),
\[
\boxed{\quad
L_{n,k}(p)\le \mathbb P(S_n\ge k)\le U_{n,k}(p).
\quad}
\]
Both endpoints are attained. Moreover every value in the closed interval
\([L_{n,k}(p),U_{n,k}(p)]\) is attained by an infinitely exchangeable
Bernoulli sequence having marginal mean \(p\).

For the upper endpoint, an explicit directing measure is:

- \(k=1\): \(\Theta=p\) almost surely;
- \(k=n\): \(\Theta\in\{0,1\}\) with
  \(\mathbb P(\Theta=1)=p\);
- \(2\le k\le n-1\), \(p<\tau_{n,k}\):
  \[
  \mathbb P(\Theta=\tau_{n,k})=p/\tau_{n,k},
  \qquad
  \mathbb P(\Theta=0)=1-p/\tau_{n,k};
  \]
- \(2\le k\le n-1\), \(p\ge\tau_{n,k}\):
  \(\Theta=p\) almost surely.

Lower-endpoint extremizers follow by complementing successes and failures.

### Proof

By de Finetti's theorem there is a directing random variable
\(\Theta\in[0,1]\) such that, conditional on \(\Theta\), the \(X_i\) are
i.i.d. Bernoulli\((\Theta)\). Hence
\[
\mathbb E\Theta=p,\qquad
\mathbb P(S_n\ge k)=\mathbb E\,g_{n,k}(\Theta).
\]
Thus the upper problem is the one-moment extremal problem
\[
\sup_{\nu:\,\int\theta\,d\nu=p}\int g_{n,k}(\theta)\,d\nu(\theta),
\]
whose value is the least concave majorant of \(g_{n,k}\) evaluated at \(p\).
Here that majorant can be determined explicitly.

For \(2\le k\le n-1\),
\[
g'_{n,k}(\theta)
=n{n-1\choose k-1}\theta^{k-1}(1-\theta)^{n-k},
\]
and therefore \(g''_{n,k}\) has the sign of
\[
(k-1)-(n-1)\theta.
\]
So \(g_{n,k}\) is convex before
\(q=(k-1)/(n-1)\) and concave after \(q\).

Let
\[
h(\theta)=\theta g'_{n,k}(\theta)-g_{n,k}(\theta).
\]
Then \(h'(\theta)=\theta g''_{n,k}(\theta)\). Also
\[
h(\theta)\sim (k-1){n\choose k}\theta^k>0
\quad(\theta\downarrow0),
\qquad
h(1)=-1.
\]
Consequently \(h\) first increases and then strictly decreases, and has a
unique zero \(\tau_{n,k}\in(q,1)\). Since
\[
\frac{d}{d\theta}\frac{g_{n,k}(\theta)}{\theta}
=\frac{h(\theta)}{\theta^2},
\]
the ratio \(g_{n,k}(\theta)/\theta\) increases up to \(\tau_{n,k}\) and
decreases thereafter. Hence, on \([0,\tau_{n,k}]\), the tangent chord
\[
\theta\longmapsto
\frac{\theta}{\tau_{n,k}}g_{n,k}(\tau_{n,k})
\]
majorizes \(g_{n,k}\). At \(\tau_{n,k}\) its slope equals
\(g'_{n,k}(\tau_{n,k})\), and \(g_{n,k}\) is concave on
\([\tau_{n,k},1]\). The piecewise function \(U_{n,k}\) is therefore concave
and majorizes \(g_{n,k}\).

It is the *least* such concave majorant. Indeed, if \(F\) is any concave
majorant, then for \(0\le p\le\tau_{n,k}\),
\[
F(p)\ge
\left(1-\frac p{\tau_{n,k}}\right)F(0)
+\frac p{\tau_{n,k}}F(\tau_{n,k})
\ge
\frac p{\tau_{n,k}}g_{n,k}(\tau_{n,k}),
\]
while for \(p\ge\tau_{n,k}\), \(F(p)\ge g_{n,k}(p)\).
Jensen's inequality now gives
\[
\mathbb E g_{n,k}(\Theta)
\le \mathbb E U_{n,k}(\Theta)
\le U_{n,k}(\mathbb E\Theta)=U_{n,k}(p),
\]
and the directing measures listed above attain equality.

The edge cases follow directly: \(g_{n,1}(\theta)=1-(1-\theta)^n\) is
concave, while \(g_{n,n}(\theta)=\theta^n\) has least concave majorant
\(\theta\).

For the lower endpoint, put \(Y_i=1-X_i\). Then \(Y_i\) is infinitely
exchangeable with mean \(1-p\), and
\[
\mathbb P_X(S_n\ge k)
=
1-\mathbb P_Y\!\left(\sum_{i=1}^nY_i\ge n-k+1\right).
\]
Maximizing the probability on the right gives exactly
\(L_{n,k}(p)=1-U_{n,n-k+1}(1-p)\). Finally, convex mixtures of any upper
and lower extremizing sequence laws remain infinitely exchangeable and
keep marginal mean \(p\), so every intermediate tail probability is attained.
\(\square\)

## 4. Strict finite-sample extendibility gap

The sharp finite-exchangeable bounds of Zaigraev--Kaniovski contain the
infinitely extendible interval, but are generically strictly wider.

For \(n>1\), \(0<p<1\):

- if \(1<k<n\), both endpoints improve strictly;
- if \(k=1\), the upper endpoint improves strictly while the lower endpoint
  remains \(p\);
- if \(k=n\), the lower endpoint improves strictly while the upper endpoint
  remains \(p\).

For \(2\le k<n\), strictness of the upper comparison follows from the strict
Markov inequality for \(B\sim\operatorname{Bin}(n,\theta)\):
\[
g_{n,k}(\theta)<\frac{n\theta}{k}
\quad(0<\theta\le1),
\]
with the endpoint \(\theta=1\) also strict because \(k<n\).
Thus the maximum slope of \(g_{n,k}(\theta)/\theta\) is strictly below
\(n/k\), while \(U_{n,k}(p)<1\) for \(p<1\). The \(k=1\) case follows from
\(1-(1-p)^n<\min\{np,1\}\). The lower comparison follows by complement.

Example:
for \(n=10,k=6,p=0.3\),
\[
\tau_{10,6}=0.744388302998\ldots,
\]
and the exact infinitely extendible range is
\[
[\,0.0473489874,\ 0.3688182436\,],
\]
whereas the sharp arbitrary finite-exchangeable range is
\[
[\,0,\ 0.5\,].
\]
The i.i.d. Bernoulli\((0.3)\) tail equals \(0.0473489874\); in this example
it happens to attain the lower endpoint, not the upper one.

## 5. Proportional-threshold asymptotics: the gap vanishes

Let \(k_n/n\to a\in(0,1)\) and keep \(p\in[0,1]\) fixed. Then
\[
\boxed{
\lim_{n\to\infty}\sup
\mathbb P(S_n\ge k_n)
=
\min\!\left\{1,\frac pa\right\},
}
\]
where the supremum is over all infinitely exchangeable Bernoulli sequences
with marginal mean \(p\). Likewise
\[
\boxed{
\lim_{n\to\infty}\inf
\mathbb P(S_n\ge k_n)
=
\max\!\left\{0,\frac{p-a}{1-a}\right\}.
}
\]

For the upper limit, Markov's inequality gives
\[
\mathbb P(S_n\ge k_n)\le \min\{np/k_n,1\}.
\]
If \(p<a\), choose
\(\theta_n=k_n/n+\delta_n\), with \(\delta_n=n^{-1/4}\) for all sufficiently
large \(n\), and use a directing law placing mass \(p/\theta_n\) at
\(\theta_n\) and the rest at zero. Hoeffding's inequality gives
\[
\mathbb P\{\operatorname{Bin}(n,\theta_n)<k_n\}
\le e^{-2n\delta_n^2}\to0,
\]
so the resulting tail tends to \(p/a\). If \(p=a\), replace \(\theta_n\) by
\(\max\{a,k_n/n\}+\delta_n\) (with a harmless cap below 1); the same argument
gives limit one. If \(p>a\), the i.i.d. directing law \(\Theta=p\) gives
tail probability tending to one. The lower limit follows by complement.

Thus infinite extendibility gives a strict finite-\(n\) refinement of the
marginal-only finite-exchangeable interval, but at thresholds proportional
to \(n\) its worst-case interval converges to the same Markov-type limits.
In particular, infinite exchangeability plus only the unconditional marginal
mean does **not** produce concentration of \(S_n/n\) around \(p\).

## 6. Relation to recent and prior literature

Recent work emphasizes exactly why unconditional-mean concentration for
exchangeable data needs information about the de Finetti mixture. Gottschling
and Caprio (2026) give Hoeffding-style exchangeable bounds centered at the
largest/smallest conditional means in the support of the directing measure.
Lin, Frei and de la Peña (2026) decompose bounded-difference deviations into
conditional sampling fluctuation and latent mixture fluctuation, and obtain
mean-centered concentration when that mixture fluctuation is controlled.
The theorem here addresses a different marginal-only extremal question and
makes the obstruction explicit for Bernoulli threshold events.

The closest finite-dimensional predecessor located in the search is
Zaigraev and Kaniovski (2010), with a geometric refinement by Di Cecco
(2011). Those works optimize over arbitrary finite exchangeable Bernoulli
vectors (and, in the latter work, add correlation information). Infinite
extendibility restricts that polytope to binomial mixtures, producing the
smaller interval above.

Misra, Singh and Harner (2003) study stochastic and variability orderings
between binomial variables and mixed binomials, including equal-mean
comparisons. That literature is structurally close, but the inspected
statement does not give the fixed-mean exact threshold envelope above.

The variational identity "one fixed moment -> least concave majorant" is
standard. The contribution claimed here is therefore not that general
principle; it is the explicit tangent formula for the binomial threshold
curve, the exact upper-and-lower feasible interval for infinitely extendible
exchangeable Bernoulli trials, its strict comparison with the sharp
finite-exchangeable interval, and the proportional-threshold asymptotic
collapse of the extendibility gap.

## 7. Limitations

- Infinite exchangeability (equivalently, infinite extendibility of every
  finite prefix) is essential. The formula is not asserted for merely
  \(n\)-exchangeable or finitely \(N\)-extendible Bernoulli vectors.
- Only the one-dimensional marginal mean \(p\) is fixed. Additional
  information about pairwise correlation or the directing measure can
  sharpen the interval further.
- Originality is asserted only to the best of the documented search.
  Classical mixed-binomial and moment-problem literature is broad; an older
  equivalent formulation may exist.
- Numerical checks in the supplied artifact support the algebra but are not
  used in place of the proof.

## 8. Reproducibility

Run

```text
python3 artifacts/verify_envelope.py
```

using Python 3 and only the standard library. The script computes the tangent
point by bisection, reproduces representative intervals, checks the tangent
equation numerically, and checks the majorant/concavity properties on a grid.

## References

1. B. de Finetti, classical representation theorem for infinitely exchangeable
   Bernoulli sequences.
2. A. Zaigraev and S. Kaniovski, "Exact bounds on the probability of at least
   k successes in n exchangeable Bernoulli trials as a function of correlation
   coefficients," *Statistics & Probability Letters* 80 (2010), 1079--1084.
   https://doi.org/10.1016/j.spl.2010.02.023
3. D. Di Cecco, "A geometric approach to a class of optimization problems
   concerning exchangeable binary variables," *Statistics & Probability
   Letters* 81 (2011), 411--416.
   https://doi.org/10.1016/j.spl.2010.11.016
4. N. Misra, H. Singh and E. J. Harner, "Stochastic comparisons of Poisson and
   binomial random variables with their mixtures," *Statistics & Probability
   Letters* 65 (2003), 279--290.
   https://doi.org/10.1016/j.spl.2003.07.002
5. N. M. Gottschling and M. Caprio, "Hoeffding-Style Concentration Bounds for
   Exchangeable Random Variables," arXiv:2603.10190 (2026).
   https://arxiv.org/abs/2603.10190
6. F. Lin, S. Frei and V. H. de la Peña, "Bounded Difference Concentration for
   Infinitely Exchangeable Sequences with Applications to AI Benchmark
   Uncertainty," arXiv:2606.17426 (2026).
   https://arxiv.org/abs/2606.17426
7. W. Tang, "Finite and Infinite Weighted Exchangeable Sequences,"
   *Mathematics* 14 (2026), 3291.
   https://doi.org/10.3390/math14183291
