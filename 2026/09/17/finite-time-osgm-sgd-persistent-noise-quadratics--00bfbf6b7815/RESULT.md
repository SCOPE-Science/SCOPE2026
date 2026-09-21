# Finite-time absorption of OSGM-SGD under persistent discrete gradient noise

## Statement

Consider the one-dimensional quadratic objective
\[
f(x)=\frac{a}{2}x^2+C,\qquad a>0,
\]
with an unbiased stochastic-gradient oracle
\[
g(x;B)=ax+B,
\]
where successive \(B\)'s are independent and identically distributed, have finite
nonzero support, satisfy \(\mathbb E B=0\), and obey
\(\mathbb P(B\ne0)=1\). Thus the gradient noise does not vanish at the optimum:
\[
\operatorname{Var}(g(0;B))=\mathbb E B^2>0.
\]

Run the scalar hypergradient version of OSGM-SGD with exact objective values,
candidate stepsizes
\[
\mathcal P=[0,1/a],
\]
OSGM learning rate \(\eta=1/a\), and the exact-function hypergradient feedback
\[
h_{x,B}(p)=
\frac{f(x-pg(x;B))-f(x)}{g(x;B)^2}.
\]
At each iteration, first form the stochastic-gradient trial point
\(y=x-pg(x;B)\), accept whichever of \(x,y\) has smaller full objective value
(the null step), and then update \(p\) by projected online gradient descent on
\(h_{x,B}\).

Let
\[
b_{\min}=\min\{|b|:\mathbb P(B=b)>0\},
\]
and suppose
\[
|a x_0|<b_{\min}.
\]
Define
\[
q_+=\mathbb P(B>0),\qquad q_-=\mathbb P(B<0),
\]
and
\[
c_+=\sum_{b>0}\mathbb P(B=b)^2,\qquad
c_-=\sum_{b<0}\mathbb P(B=b)^2,
\]
where the sums are over distinct atoms. Set
\[
q=\min\{q_-c_+,\,q_+c_-\}>0.
\]
If
\[
T=\inf\{k\ge0:x_k=0\},
\]
then, for every integer \(m\ge0\),
\[
\boxed{\mathbb P(T>3m)\le(1-q)^m,}
\]
and consequently
\[
\boxed{T<\infty\ \text{almost surely},\qquad \mathbb ET\le \frac{3}{q}.}
\]
After \(x_k=0\) is reached, the exact null step keeps the iterate at the optimum.

Thus this smooth strongly convex quadratic admits exact finite-time convergence
of this OSGM-SGD specialization even though its stochastic gradient has
persistent nonzero variance at the optimum.

## Finite-sum corollary

A concrete finite-sum realization is
\[
f_i(x)=\frac a2x^2+b_i x+c_i,\qquad i=1,\dots,n,
\]
sampled uniformly, with
\[
\frac1n\sum_{i=1}^n b_i=0,\qquad b_i\ne0.
\]
Then the full objective is \(f(x)=a x^2/2+C\) after an additive constant, and
the stochastic gradient is \(ax+b_i\).

Let \(m_+\) and \(m_-\) denote the numbers of positive and negative offsets.
For uniform sampling,
\[
q\ge \frac{m_+m_-}{n^3},
\]
so
\[
\mathbb P(T>3m)\le
\left(1-\frac{m_+m_-}{n^3}\right)^m,
\qquad
\mathbb ET\le \frac{3n^3}{m_+m_-}.
\]
For the two-component balanced example \(b_1=\sigma\), \(b_2=-\sigma\),
the bound gives \(q=1/8\) and \(\mathbb ET\le24\).

## Proof

For the quadratic objective,
\[
h_{x,B}(p)
=\frac{\frac a2(x-pg)^2-\frac a2x^2}{g^2},
\qquad g=ax+B.
\]
Differentiation gives
\[
h'_{x,B}(p)=a\left(p-\frac{x}{ax+B}\right).
\]
With \(\eta=1/a\), the stepsize update therefore collapses to
\[
\boxed{
p^+=\Pi_{[0,1/a]}
\left(\frac{x}{ax+B}\right).
}
\tag{1}
\]

The null step never increases \(f\), hence never increases \(|x|\). Therefore
the strict local condition \(|ax|<b_{\min}\) is invariant.

Suppose first that \(x>0\). Under the invariant condition:

1. If \(B<0\), then \(ax+B<0\). For every \(p\ge0\),
   \[
   y=x-p(ax+B)\ge x,
   \]
   so the exact null step leaves \(x\) unchanged. Equation (1) gives \(p^+=0\).

2. On the next iteration, if \(B=b>0\), the current stepsize is zero, so the
   iterate remains \(x\), while (1) gives
   \[
   p^+=\frac{x}{ax+b}\in(0,1/a).
   \]

3. If the same positive atom \(b\) is drawn once more, the trial point is
   exactly
   \[
   x-\frac{x}{ax+b}(ax+b)=0.
   \]
   The null step accepts it.

Thus, starting from any nonzero \(x>0\) in the invariant region and any current
stepsize in \([0,1/a]\), a three-draw pattern consisting of a negative atom,
then two copies of the same positive atom, hits the optimum. Its probability is
\[
q_-c_+.
\]

For \(x<0\), the symmetric pattern--a positive atom followed by two copies of
the same negative atom--hits zero with probability \(q_+c_-\). Since a
mean-zero nonzero finite-support distribution must have both positive and
negative mass, \(q>0\).

At the start of each disjoint block of three iterations, conditional on not
having reached zero already, the probability of reaching zero during that
block is at least \(q\), regardless of the current nonzero state and stepsize.
Iterating conditional probabilities yields
\[
\mathbb P(T>3m)\le(1-q)^m.
\]
Summing the tail blockwise gives \(\mathbb ET\le3/q\).

If \(x=0\), every trial point has objective value at least \(f(0)\), so the
null step keeps \(x=0\). Hence zero is absorbing for the iterate. In addition,
the following hypergradient update sends the stepsize to zero because (1)
has numerator \(x=0\).

For the finite-sum bound, under uniform sampling
\(q_+=m_+/n\) and \(q_-=m_-/n\). If several indices share the same offset,
group them by atom. For the positive atoms,
\[
c_+=\sum_j(r_j/n)^2\ge m_+/n^2,
\]
where the positive multiplicities satisfy \(\sum_jr_j=m_+\); similarly
\(c_-\ge m_-/n^2\). This gives
\(q\ge m_+m_-/n^3\).

## Why the gradient-noise condition is genuinely violated

The OSGM-SGD analysis in Zhang--Gao--Ye--Udell assumes a gradient-norm
condition in which stochastic-gradient error is controlled relative to
\(\|\nabla f(x)\|\). Here
\[
\nabla f(x)=ax,\qquad g(x;B)-\nabla f(x)=B.
\]
At the optimum, \(\nabla f(0)=0\) while \(B\ne0\) almost surely. More generally,
the ratio \(|B|/|ax|\) diverges as \(x\to0\). The theorem therefore lies outside
that relative-noise regime rather than being a restatement of its convergence
guarantee.

## Contrast with fixed-stepsize SGD

For fixed-step SGD on the same oracle,
\[
x_{k+1}=(1-a\alpha)x_k-\alpha B_k.
\]
If \(0<\alpha<2/a\) and
\(\sigma_B^2=\mathbb E B^2\), independence and zero mean give
\[
\mathbb E x_{k+1}^2
=(1-a\alpha)^2\mathbb E x_k^2+\alpha^2\sigma_B^2.
\]
Hence
\[
\lim_{k\to\infty}\mathbb E x_k^2
=
\frac{\alpha\sigma_B^2}{a(2-a\alpha)}>0.
\]
Constant-step SGD therefore has a stationary mean-square noise floor in this
model, whereas the exact-function OSGM-SGD specialization above reaches the
exact minimizer in finite time almost surely.

This comparison is only with fixed nonzero stepsizes; diminishing-step SGD can
converge asymptotically under persistent noise.

## Context and originality

Zhang, Gao, Ye, and Udell introduced stochastic online scaled gradient methods
and proved OSGM-SGD convergence under a relative gradient-noise condition. Their
current arXiv version explicitly leaves convergence under non-vanishing
gradient noise as an open direction. It also identifies the exact-function
hypergradient/null-step regime used here as a legitimate OSGM-SGD setting.

The finite-time phenomenon above is not a generic consequence of persistent
noise. It relies on four special features acting together: a scalar quadratic
with known curvature scale, an exact full-objective null step, atomic gradient
noise, and the hypergradient learning rate \(\eta=1/a\), which turns the
scheduler update into the exact ratio (1).

Prior work by Zhou, Mertikopoulos, Bambos, Boyd, and Glynn proves almost-sure
finite-time attainment under persistent gradient noise for stochastic mirror
descent at *sharp* minima. That result does not cover the present objective:
the smooth quadratic minimum is not sharp in their sense, and the absorption
mechanism here comes from adaptive stepsize feedback and repeated noise atoms.
Related adaptive SGD, stochastic line-search, Polyak-stepsize, and
hypergradient literature was also checked; no theorem matching the stated
OSGM-SGD absorption mechanism and bound was located.

Accordingly, originality is claimed only **to the best of our knowledge**.

## Limitations

- The result is one-dimensional and local: it assumes
  \(|a x_0|<b_{\min}\).
- The full objective value used by the null step and hypergradient feedback is
  exact.
- The noise must be discrete with finite nonzero support. For a nonatomic
  continuous distribution, the repeated-atom event used in the proof has
  probability zero, so this finite-time argument does not extend.
- The hypergradient learning rate is tuned to the curvature,
  \(\eta=1/a\), and the candidate interval uses \(1/a\).
- The theorem establishes a concrete positive special case of convergence
  under non-vanishing gradient noise; it is not a general solution of that
  open problem.

## References

1. W. Zhang, W. Gao, Y. Ye, and M. Udell,
   *Stochastic Gradient Methods with Online Scaling*,
   arXiv:2609.11751v2, 2026.
2. W. Gao, Y. Chu, Y. Ye, and M. Udell,
   *Gradient Methods with Online Scaling, Part I: Theoretical Foundations*,
   arXiv:2505.23081, 2025.
3. A. G. Baydin, R. Cornish, D. Martínez Rubio, M. Schmidt, and F. Wood,
   *Online Learning Rate Adaptation with Hypergradient Descent*,
   ICLR 2018; arXiv:1703.04782.
4. Z. Zhou, P. Mertikopoulos, N. Bambos, S. P. Boyd, and P. W. Glynn,
   *On the Convergence of Mirror Descent beyond Stochastic Convex
   Programming*, SIAM Journal on Optimization 30(1):687--716, 2020;
   arXiv:1706.05681.
