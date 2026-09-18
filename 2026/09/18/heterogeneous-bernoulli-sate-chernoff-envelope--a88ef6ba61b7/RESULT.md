# Exact rare-arm Chernoff envelopes for heterogeneous Bernoulli treatment effects

## Setting

For units \(i=1,\dots,n\), let the treatment indicators be independent,
\[
Z_i\sim\operatorname{Bernoulli}(p_i),\qquad 0<p_i<1,
\]
with fixed potential outcomes satisfying known, possibly unit- and arm-specific bounds
\[
Y_i(1)\in[a_{i1},b_{i1}],\qquad Y_i(0)\in[a_{i0},b_{i0}].
\]
The finite-population sample average treatment effect is
\[
\tau=\frac1n\sum_{i=1}^n\{Y_i(1)-Y_i(0)\}.
\]
Define the propensity-weighted endpoint interval
\[
\ell_i=(1-p_i)a_{i1}+p_i a_{i0},\qquad
\nu_i=(1-p_i)b_{i1}+p_i b_{i0},
\]
its midpoint and radius
\[
m_i^*=\frac{\ell_i+\nu_i}{2},\qquad
r_i=\frac{\nu_i-\ell_i}{2},
\]
and the midpoint-differenced estimator
\[
\widehat\tau_*
=\frac1n\sum_{i=1}^n\left[
\frac{Z_i}{p_i}\{Y_i(1)-m_i^*\}
-\frac{1-Z_i}{1-p_i}\{Y_i(0)-m_i^*\}
\right].
\]
It is design-unbiased for \(\tau\).

For \(q\in(0,1/2]\), write the centered-Bernoulli log-MGF as
\[
\psi_q(s)=\log\left((1-q)e^{-qs}+qe^{(1-q)s}\right).
\]
Also set
\[
q_i=\min\{p_i,1-p_i\},\qquad
d_i=\frac{r_i}{p_i(1-p_i)}.
\]

## Main theorem: exact least-favorable Laplace envelope

For every \(\lambda\ge0\),
\[
\boxed{
\sup_{\{Y_i(z)\ \text{within their stated bounds}\}}
\mathbb E\exp\!\left\{\lambda n(\widehat\tau_*-\tau)\right\}
=
\exp\!\left\{\sum_{i=1}^n\psi_{q_i}(\lambda d_i)\right\}.
}
\]
The same equality holds with \(\widehat\tau_*-\tau\) replaced by its negative.
The supremum is attained by endpoint potential-outcome schedules, coordinate by coordinate.

Consequently, for every \(\alpha\in(0,1)\) and every \(\lambda>0\),
\[
\boxed{
\Pr\!\left(
|\widehat\tau_*-\tau|>
\frac{\log(2/\alpha)+\sum_i\psi_{q_i}(\lambda d_i)}{n\lambda}
\right)
\le \alpha.
}
\]
Thus the optimized Chernoff half-width is
\[
\boxed{
\rho_\alpha^{\rm Ch}
=
\inf_{\lambda>0}
\frac{\log(2/\alpha)+\sum_i\psi_{q_i}(\lambda d_i)}{n\lambda}.
}
\]
This is a one-dimensional convex-dual computation even when the propensities are heterogeneous.

The exact worst-case randomization variance of this estimator is
\[
\boxed{
\sup \operatorname{Var}(\widehat\tau_*-\tau)
=
\frac1{n^2}\sum_{i=1}^n\frac{r_i^2}{p_i(1-p_i)}.
}
\]
Again, endpoint schedules attain the bound simultaneously.

A standard Bernstein corollary of the envelope is obtained by defining
\[
V=\sum_{i=1}^n\frac{r_i^2}{p_i(1-p_i)},\qquad
R=\max_i\frac{r_i}{q_i},\qquad L=\log(2/\alpha).
\]
Then
\[
\boxed{
\Pr\left(
|\widehat\tau_*-\tau|>
\frac1n\left\{\frac{RL}{3}+\sqrt{2VL+(RL/3)^2}\right\}
\right)\le\alpha.
}
\]
The novelty claim is not the generic Bernstein inequality; independent unequal-probability sampling has a long concentration literature. The point here is the exact least-favorable Bernoulli envelope induced by the two-arm potential-outcome geometry.

## Proof

Let
\[
A_i=(1-p_i)Y_i(1)+p_iY_i(0).
\]
A direct calculation gives
\[
\widehat\tau_*-\tau
=\frac1n\sum_{i=1}^n c_i(Z_i-p_i),
\qquad
c_i=\frac{A_i-m_i^*}{p_i(1-p_i)}.
\]
Because \(A_i\in[\ell_i,\nu_i]\), midpoint centering gives \(|c_i|\le d_i\), with both endpoints \(\pm d_i\) attainable by taking the two potential outcomes simultaneously at their lower or upper bounds.

For a single coordinate define
\[
M_p(s)=(1-p)e^{-ps}+pe^{(1-p)s}.
\]
For fixed \(\lambda\ge0\), \(c\mapsto M_p(\lambda c)\) is convex, hence its maximum on \([-d,d]\) occurs at an endpoint. If \(p\le1/2\) and \(u\ge0\),
\[
M_p(u)-M_p(-u)
=2\left[p\sinh((1-p)u)-(1-p)\sinh(pu)\right]\ge0,
\]
because \(x\mapsto \sinh(x)/x\) is increasing for \(x>0\). For \(p>1/2\), symmetry exchanges \(p\) with \(1-p\). Therefore
\[
\max_{|c|\le d}\mathbb E e^{\lambda c(Z-p)}
=M_{\min(p,1-p)}(\lambda d)
=e^{\psi_{\min(p,1-p)}(\lambda d)}.
\]
Independence factorizes the joint MGF, and the maximizing endpoint choices can be made simultaneously for all units. This proves the exact upper-tail envelope. Reversing all maximizing endpoint choices proves the identical lower-tail envelope. Chernoff's method and a union bound give the stated confidence interval.

For the variance,
\[
\operatorname{Var}\{c_i(Z_i-p_i)\}=c_i^2p_i(1-p_i)
\le\frac{r_i^2}{p_i(1-p_i)},
\]
and equality for every coordinate is attained at either endpoint schedule. Summing independent variances proves the exact worst-case variance formula. Also
\[
|c_i(Z_i-p_i)|\le \frac{r_i}{q_i},
\]
so the displayed Bernstein bound follows from the standard independent-sum Bernstein inequality.

## Coordinatewise minimax centering

More generally, if unit \(i\) uses an arbitrary deterministic center \(m_i\), then its coefficient ranges over
\[
\left[
\frac{\ell_i-m_i}{p_i(1-p_i)},
\frac{\nu_i-m_i}{p_i(1-p_i)}
\right].
\]
For every fixed \(\lambda>0\), the worst of the positive- and negative-tail coordinate MGFs is an increasing function of the maximum absolute coefficient. Hence
\[
m_i^*=(\ell_i+\nu_i)/2
\]
uniquely minimizes the two-sided coordinate envelope, the maximum jump magnitude, the Hoeffding radius, and the worst-case coordinate variance. This is a coordinatewise statement; no claim is made here that it solves every possible global criterion for arbitrary asymmetric confidence procedures.

## Common bounded-outcome specialization and rare-arm scaling

Suppose every potential outcome lies in a common interval \([a,b]\), with width \(w=b-a\). Then
\[
m_i^*=\frac{a+b}{2},\qquad r_i=\frac w2
\]
for all \(i\), even when the \(p_i\) differ.

Freidling (2026, Proposition 3.4) gives for this midpoint estimator the heterogeneous Hoeffding half-width
\[
\rho_\alpha^{\rm H}
=
\frac{w}{2n}
\sqrt{\frac{\log(2/\alpha)}2
\sum_{i=1}^n\frac1{p_i^2(1-p_i)^2}}.
\]
The present exact envelope is pointwise no larger than the corresponding Hoeffding exponential envelope, since Hoeffding's lemma gives \(\psi_q(s)\le s^2/8\).

If in addition \(p_i=p\) for all \(i\), put \(q=\min(p,1-p)\) and
\[
d=\frac{w}{2p(1-p)}=\frac{w}{2q(1-q)}.
\]
The least-favorable upper-tail MGF is exactly the MGF of
\[
d\{\operatorname{Bin}(n,q)-nq\}.
\]
Thus, whenever \(0\le x/d\le1-q\),
\[
\boxed{
\Pr(|\widehat\tau_*-\tau|\ge x)
\le
2\exp\left[-nD\!\left(q+\frac{x}{d}\middle\|q\right)\right],
}
\]
where \(D(\cdot\|\cdot)\) is binary relative entropy. In the fixed-confidence regime with \(nq\to\infty\), the optimized Chernoff half-width has leading behavior
\[
\boxed{
\rho_\alpha^{\rm Ch}
\sim
\frac w2
\sqrt{\frac{2\log(2/\alpha)}{nq(1-q)}}.
}
\]
Hence it has the optimal rare-arm order \(O((nq)^{-1/2})\), rather than the \(O((nq^2)^{-1/2})\) scaling of the support-only Hoeffding bound. Sandoval et al. (2026) already achieved the \(O((n\pi)^{-1/2})\) order for common treatment probability using a sub-Bernoulli argument, and Freidling adapts that result to common-propensity centered estimators. The present contribution is the exact least-favorable envelope that retains this rare-arm behavior under heterogeneous propensities while keeping midpoint centering.

## Numerical check

For \(n=500\), \([a,b]=[0,1]\), and \(\alpha=0.05\), deterministic evaluation of the three displayed bounds gives

| \(p\) | midpoint Hoeffding | exact Chernoff | Bernstein |
|---:|---:|---:|---:|
| 0.50 | 0.121472292 | 0.121322687 | 0.123956437 |
| 0.20 | 0.189800457 | 0.156203957 | 0.158112918 |
| 0.05 | 0.639327855 | 0.300796639 | 0.304352092 |
| 0.01 | 3.067482131 | 0.722122751 | 0.745645472 |

The accompanying script also verifies the single-coordinate rare-arm orientation identity on a deterministic grid.

## Relation to prior work

- Freidling, *Randomization Inference with Concentration Inequalities* (2026), arXiv:2609.18586, allows heterogeneous independent Bernoulli assignment in its midpoint-Hoeffding result, and explicitly notes the improved rare-treatment scaling of the common-propensity sub-Bernoulli method. Its Proposition 3.5 assumes equal treatment probabilities.
- Sandoval et al., *On Nonasymptotic Confidence Intervals for Treatment Effects in Randomized Experiments* (2026), arXiv:2601.11744, establishes common-propensity sub-Bernoulli intervals with the optimal rare-arm order.
- Aronow and Lopatto, *Minimax unbiased estimation for finite populations with bounded outcomes* (2026), arXiv:2605.20572, proves the midpoint-differenced Horvitz-Thompson estimator is minimax for worst-case squared error under independent inclusion sampling. Midpoint differencing itself is therefore prior art.
- Bertail and Clémençon, *Sharp exponential inequalities in survey sampling: conditional Poisson sampling schemes* (2019; arXiv:1610.03776), emphasizes that standard independent-sum exponential inequalities carry over directly to unequal-probability Poisson sampling. Generic Bernstein/Bennett concentration for independent unequal-probability sampling is therefore also prior art.

To the best of our knowledge, the exact least-favorable two-sided Laplace envelope above, its rare-arm endpoint orientation and attainment, and its heterogeneous-propensity treatment-effect specialization have not been stated in these sources or in the closely related literature inspected here.

## Limitations

The result assumes independent Bernoulli assignment and fixed bounded potential outcomes. It does not cover complete randomization, rejective designs, adaptive assignments, interference, or estimated propensities. The Laplace envelope is exact, but Chernoff inversion need not equal the exact worst-case tail probability. The interval is worst-case over the stated outcome rectangle and is not variance-adaptive. The common-propensity rate comparison concerns the midpoint estimator and should not be read as a dominance claim over every existing sub-Bernoulli or empirical-Bernstein interval.

## References

1. Tobias Freidling, *Randomization Inference with Concentration Inequalities*, arXiv:2609.18586 (2026). https://arxiv.org/abs/2609.18586
2. Sandoval et al., *On Nonasymptotic Confidence Intervals for Treatment Effects in Randomized Experiments*, arXiv:2601.11744 (2026). https://arxiv.org/abs/2601.11744
3. P. M. Aronow and Patrick Lopatto, *Minimax unbiased estimation for finite populations with bounded outcomes*, arXiv:2605.20572 (2026). https://arxiv.org/abs/2605.20572
4. Patrice Bertail and Stephan Clémençon, *Sharp exponential inequalities in survey sampling: conditional Poisson sampling schemes*, arXiv:1610.03776 (published 2019). https://arxiv.org/abs/1610.03776
5. Steven R. Howard, Aaditya Ramdas, Jon McAuliffe, and Jasjeet Sekhon, *Time-uniform, nonparametric, nonasymptotic confidence sequences*, Annals of Statistics 49 (2021), 1055–1080. https://doi.org/10.1214/20-AOS1991
