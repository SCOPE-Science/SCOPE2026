# Strict sampling-majorization for the nonuniform clumsy coupon collector

## Finding

For the clumsy coupon collector with a fixed common probability of losing the selected type, **balancing the sampling probabilities strictly improves the entire probability-generating function of the first all-present time**, not only its expectation. The result holds at every finite alphabet size, with an exact transform and exact heterogeneity penalties.

Put \(r=p/(1-p)\), and for a subset \(S\subseteq[m]\) put \(W_S=\sum_{i\in S}w_i\), including \(W_{\varnothing}=0\). For every \(s>0\), set \(z=(1+s)^{-1}\). Then

\[
\mathbb E_{\boldsymbol w}[z^T]
=\frac{\displaystyle\int_0^\infty e^{-st}\prod_{i=1}^{m}(1-e^{-w_it})\,dt}
{\displaystyle\int_0^\infty e^{-st}\prod_{i=1}^{m}(1+r e^{-w_it})\,dt}
=\frac{\displaystyle\sum_{S\subseteq[m]}\frac{(-1)^{|S|}}{s+W_S}}
{\displaystyle\sum_{S\subseteq[m]}\frac{r^{|S|}}{s+W_S}}.
\]

In particular,

\[
\boxed{\quad\mathbb E_{\boldsymbol w}T
=\sum_{\varnothing\ne S\subseteq[m]}
\frac{r^{|S|}-(-1)^{|S|}}{W_S}.\quad}
\]

If \(\boldsymbol w\) majorizes \(\boldsymbol v\), so that \(\boldsymbol w\) is at least as unequal as \(\boldsymbol v\), then for every \(0<z<1\),

\[
\mathbb E_{\boldsymbol w}[z^T]\le\mathbb E_{\boldsymbol v}[z^T].
\]

The inequality is strict unless the two positive vectors are permutations of one another. Consequently \(\boldsymbol w=(1/m,\ldots,1/m)\) uniquely minimizes \(\mathbb E T\) and uniquely maximizes the probability-generating function among all strictly positive sampling vectors, up to the trivial permutation equivalence. This is **transform order**, not a claim of ordinary stochastic domination.

For two coordinates \(a=w_i\), \(b=w_j\), write \(\bar a=\bar b=(a+b)/2\), and leave the other coordinates unchanged. The exact positive mean penalty before balancing is

\[
\boxed{\quad
\mathbb E_{\boldsymbol w}T-\mathbb E_{\bar{\boldsymbol w}}T
=\int_0^\infty e^{-(a+b)t/2}
\bigg[2\cosh\!\left(\frac{(a-b)t}{2}\right)-2\bigg]
\bigg[r\prod_{k\notin\{i,j\}}(1+r e^{-w_kt})
+\prod_{k\notin\{i,j\}}(1-e^{-w_kt})\bigg]dt.\quad}
\]

For \(m=2\), where \(a+b=1\), the gap simplifies to \((a-b)^2/((1-p)ab)\). More generally, for any fixed tangent direction \(\boldsymbol v\) with \(\sum_i v_i=0\) and sufficiently small real \(\varepsilon\),

\[
\mathbb E_{\boldsymbol u+\varepsilon\boldsymbol v}T
=m\sum_{\ell=1}^{m}\frac{1}{\ell(1-p)^\ell}
+\frac{\varepsilon^2}{2}\,H_{m,p}\sum_i v_i^2
+O_{m,p,\boldsymbol v}(|\varepsilon|^3),
\qquad \boldsymbol u=(1/m,\ldots,1/m),
\]

with strictly positive curvature

\[
H_{m,p}=\int_0^\infty t^2e^{-t/m}
\left[r(1+r e^{-t/m})^{m-2}+(1-e^{-t/m})^{m-2}\right]dt>0.
\]

## Assumptions and scope

Fix an integer \(m\ge2\), a **common** clumsiness probability \(p\in[0,1)\), and a sampling vector \(\boldsymbol w=(w_1,\ldots,w_m)\) with \(w_i>0\) and \(\sum_iw_i=1\). Initially every one of the \(m\) types is absent. At each discrete step, independently select type \(i\) with probability \(w_i\); overwrite its state with an independent Bernoulli\((1-p)\) state (present on success), leaving the other coordinates untouched. Let \(T\) be the first *positive* step at which all coordinates are present. No global reset is involved. All formulas and optimality claims are finite-\(m\) exact results. The case \(m=1\) has an obvious one-coordinate formula but no meaningful choice of weights.

A vector majorizes another when every sorted descending partial sum is at least as large and their totals agree. A strict balancing step replaces two unequal coordinates by a convex averaging of those coordinates; the remaining coordinates do not change. The T-transform characterization of majorization is used below.

## Proof

**1. Independent-coordinate Poissonization.** Embed the discrete chain in a rate-one marked Poisson process. Independent thinning of the marks gives independent rate-\(w_i\) Poisson refresh clocks on each coordinate. Denote the continuous-time first all-present hitting time by \(\tau\). Because the rate-one inter-event intervals are independent of the marked embedded chain,

\[
\mathbb E e^{-s\tau}=\mathbb E(1+s)^{-T},\qquad s>0.
\]

For each coordinate, from an initially absent state, the probability of being present at time \(t\) is \((1-p)(1-e^{-w_it})\). From an initially present state, it is \((1-p)+p e^{-w_it}\). Independence therefore yields, with \(\boldsymbol0\) and \(\boldsymbol1\) the empty and full states,

\[
P_t(\boldsymbol0,\boldsymbol1)=(1-p)^m\prod_i(1-e^{-w_it}),\qquad
P_t(\boldsymbol1,\boldsymbol1)=(1-p)^m\prod_i(1+r e^{-w_it}).
\]

For the continuous-time resolvent \(G_s(x,y)=\int_0^\infty e^{-st}P_t(x,y)\,dt\), the strong Markov property at \(\tau\) gives

\[
G_s(\boldsymbol0,\boldsymbol1)=\mathbb E_{\boldsymbol0}[e^{-s\tau}]\,G_s(\boldsymbol1,\boldsymbol1).
\]

The common factor \((1-p)^m\) cancels. Expand the finite products, integrate each exponential and obtain the stated integral and subset-sum probability-generating functions. All denominators are positive for \(s>0\); the integral form shows the denominator is strictly positive. The argument also holds at \(p=0\), when the full state is absorbing.

**2. Exact mean.** Write the two subset-sum functions as \(A(s)=s^{-1}+a_0+O(s)\) and \(B(s)=s^{-1}+b_0+O(s)\). Their ratio is \(1-s(b_0-a_0)+O(s^2)\). The chain hits the full state in finite mean: each block of \(m\) steps has a probability at least \(m!\prod_iw_i(1-p)^m>0\) to select each type once and refresh it successfully, regardless of its initial configuration. Hence \(-\partial_s\mathbb E e^{-s\tau}|_{s=0}=\mathbb E\tau=\mathbb ET\), and the coefficient difference gives the stated finite subset-sum mean formula.

**3. Transform order under balancing.** Consider two weights \(a,b\) and put \(x=e^{-at}\), \(y=e^{-bt}\), \(h=(a+b)/2\). For each \(t>0\), \(xy=e^{-2ht}\) is unchanged by balancing, but

\[
x+y=2e^{-ht}\cosh((a-b)t/2)\ge 2e^{-ht},\]

with strict inequality for unequal \(a,b\). The pair factors of the numerator and denominator integrands are respectively

\[
(1-x)(1-y)=1-(x+y)+xy,
\qquad (1+rx)(1+ry)=1+r(x+y)+r^2xy.
\]

After balancing, the numerator factor strictly **increases** and the denominator factor weakly **decreases** (strictly if \(p>0\)). All remaining factors are positive for \(t>0\); their weighted integrals preserve these inequalities, and the numerator strictly increases. The ratio therefore strictly increases for every \(s>0\). The same comparison applies to a *partial* balancing: at fixed \(a+b\), the quantity \(x+y=2e^{-ht}\cosh((a-b)t/2)\) decreases strictly whenever \(|a-b|\) decreases. A finite sequence of such partial-balancing T-transforms represents majorization, proving strict Schur concavity, with permutation symmetry giving the only equality case. In particular the uniform vector maximizes the transform.

**4. Exact mean penalty.** Let \(u=e^{-ht}\) and define

\[
A_{-ij}(t)=\prod_{k\notin\{i,j\}}(1+r e^{-w_kt}),\qquad
B_{-ij}(t)=\prod_{k\notin\{i,j\}}(1-e^{-w_kt}).
\]

From the mean obtained by integrating the difference of the products (equivalently, from the finite subset sum), the change under balancing is exactly

\[
\int_0^\infty (x+y-2u)\,[r A_{-ij}(t)+B_{-ij}(t)]\,dt.
\]

Substituting the hyperbolic-cosine identity gives the displayed mean-gap formula, strictly positive for every \(a\ne b\). With \(m=2\), the empty products equal one and integration yields \((a-b)^2/((1-p)ab)\). This also verifies strict expected-time optimality directly, without inferring it from transform order.

**5. Local curvature.** The integrated product expression is analytic in the positive weights in a neighborhood of the uniform vector by dominated differentiation. Symmetry makes its first derivative zero on the hyperplane \(\sum_i v_i=0\). The tangent-space Hessian has diagonal-minus-off-diagonal value

\[
\int_0^\infty t^2e^{-t/m}
\{r(1+r e^{-t/m})^{m-2}+(1-e^{-t/m})^{m-2}\}\,dt.
\]

Thus its quadratic form is \(H_{m,p}\sum_i v_i^2\), proving the Taylor expansion and positivity. At the uniform vector the exact mean reduces to the published formula \(m\sum_{\ell=1}^m(\ell(1-p)^\ell)^{-1}\).

## Verification

`verify.py` uses only the Python standard library and exact `fractions.Fraction` arithmetic. Run `python3 verify.py`; its reference result is `PASS: 394 exact-rational assertions (the curvature tolerance check is a rational inequality).` It independently solves the full \((2^m-1)\)-state absorbing linear system at small \(m\), comparing the resulting expectation and probability-generating function against the subset formulas, including the boundary \(p=0\). It also checks published uniform special cases, exact two-type penalties, arbitrary-weight pair balancing, strict transform improvement and the local curvature coefficient. Finite computations corroborate the exact formulas but do not prove the all-\(m\) claims; those rely on the argument above.

## Relationship to prior work

Attrill and Garoni (2026, arXiv:2605.14206v1) establish the generating function and finite mean for the **uniformly selected** clumsy collector and analyze asymptotic regimes. The present transform recovers their uniform mean but treats an arbitrary positive selection vector and proves strict finite-size sampling-majorization, an exact positive heterogeneity penalty and local curvature. Long (2026, arXiv:2605.14511v1) obtains stationary-entry asymptotics for the uniform clumsy process; the unequal-probability treatment in its section 3.6 instead concerns the **global reset-button** model, not the selected-type loss model. Classical unequal-probability coupon collection corresponds to the boundary \(p=0\), for which some uniform-optimality consequences are already known; it is not presented as new here. Kleiner (2026, DOI:10.3390/math14203729) proves a Schur-concavity statement for the *fragile* collector with **loss only before first observation**, a different success event without reversible loss of already-collected types. These related statements do not directly imply the asserted exact first-hitting-time transform for local post-collection loss.

## Limitations

The result requires the same refresh-success probability for every type and strictly positive fixed sampling weights, and concerns the first hitting time from the all-absent configuration. It proves probability-generating-function/Laplace-transform order, **not** ordinary tail stochastic order, convex order, or asymptotic optimality under changing loss probabilities. It does not cover type-dependent success probabilities, global resets, or collection success before independent deadlines. Broader historical random-scan or hypercube-hitting literature could contain an equivalent result; mathematical priority is not independently certified. The related October 2026 fragile-coupon article could be compared via indexed textual sections, but its complete publisher page was not available for uninterrupted direct inspection.

## References

1. L. J. Attrill and T. M. Garoni, *The clumsy coupon collector's problem*, arXiv:2605.14206v1, first posted 2026-05-14. https://arxiv.org/html/2605.14206v1
2. C. D. Long, *Clumsy and Careless: Stationary-Entry Flux in Non-monotone Coupon Collectors*, arXiv:2605.14511v1, first posted 2026-05-14. https://arxiv.org/html/2605.14511v1
3. I. Kleiner, *The Fragile Coupon Collector: Random Deadlines, Critical Fragility, and Optimal Sampling*, Mathematics 14 (2026), 3729, https://doi.org/10.3390/math14203729
4. N. B. Shank and H. Yang, *Coupon Collector Problem for Non-Uniform Coupons and Random Quotas*, Electronic Journal of Combinatorics 20 (2013), P33, https://doi.org/10.37236/3348
