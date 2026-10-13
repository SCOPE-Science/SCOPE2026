# Sharp log-concavity region for binary Concrete densities

## Finding

For any \(\alpha>0\) and \(\tau>0\), define the binary Concrete density on \((0,1)\) by

\[
f_{\alpha,\tau}(x)=
\frac{\tau\alpha x^{\tau-1}(1-x)^{\tau-1}}
{\bigl(x^\tau+\alpha(1-x)^\tau\bigr)^2}.
\]

**Theorem.** The density is log-concave throughout \((0,1)\) if and only if

\[
\boxed{\tau\ge \frac{\sqrt\alpha+\alpha^{-1/2}}2}.
\]

Equivalently, for the associated Bernoulli probability \(p=\alpha/(1+\alpha)\), the exact threshold is

\[
\boxed{\tau\ge\frac{1}{2\sqrt{p(1-p)}}}.
\]

In particular, \(\tau\le1\) yields log-concavity only in the uniform case \(\tau=\alpha=1\). For every \(0<\tau<1\), the density is strictly log-convex. When \(\tau>1\), it is log-concave exactly for the bias interval

\[
\bigl(\tau-\sqrt{\tau^2-1}\bigr)^2
\le\alpha\le
\bigl(\tau+\sqrt{\tau^2-1}\bigr)^2.
\]

This bound is sharp. At \(\tau=2\), \(\alpha=100\), the curvature at the midpoint is explicitly positive:

\[
\left.\frac{d^2}{dx^2}\log f_{100,2}(x)\right|_{x=1/2}
=\frac{68808}{10201}>0.
\]

## Assumptions and scope

All parameters are real, \(\alpha,\tau>0\), and log-concavity means concavity of the log density on the open support, not of a logit-transformed density. The CDF is

\[
F(x)=\frac{x^\tau}{x^\tau+\alpha(1-x)^\tau},
\]

so direct differentiation yields \(F'=f_{\alpha,\tau}\), establishing normalization. The result is invariant under positive affine changes of the observed variable (in particular, replacing the unit interval with a binary-symbol interval).

## Proof

Put

\[
h=x(1-x),\quad s=\tfrac12\log\frac{x}{1-x},\quad
 a=\tfrac12\log\alpha,\quad
 u=\tanh s=2x-1,\quad
 v=\tanh(\tau s-a)=2F(x)-1.
\]

Using \(F'=f\), or differentiating the displayed density directly, gives

\[
\frac{d}{dx}\log f=\frac{u-\tau v}{h},\qquad
2h^2\frac{d^2}{dx^2}\log f
=\bigl(\tau v-u\bigr)^2-(\tau^2-1).\tag{1}
\]

One may verify the second identity from \(u'=2\) and \(v'=\tau(1-v^2)/(2h)\). Because \(h>0\), the sign of logarithmic curvature is precisely the sign of the right side of (1).

If \(\tau<1\), the right side is everywhere positive. If \(\tau=1\), it is a square, vanishing for all \(x\) only if \(a=0\), when \(f\equiv1\). Suppose henceforth that \(\tau>1\), and write

\[
r=\sqrt{\tau^2-1},\qquad b=\operatorname{arcosh}\tau,
\qquad r=\sinh b,\quad\tanh b=r/\tau.
\]

Define \(H_a(s)=\tau\tanh(\tau s-a)-\tanh s\). Identity (1) says log-concavity is equivalent to \(\lvert H_a(s)\rvert\le r\) for every real \(s\). Evaluating at \(s=0\) gives the **necessary condition**

\[
\tau\lvert\tanh a\rvert\le r
\iff |a|\le b.
\tag{2}
\]

It remains to prove sufficiency. Since \(H_a(s)\) decreases with \(a\), whenever \(-b\le a\le b\), we have \(H_b(s)\le H_a(s)\le H_{-b}(s)\). Thus it is enough to show \(H_b(s)\ge-r\), since \(H_{-b}(s)=-H_b(-s)\) will then give the upper bound.

Write \(u=\tanh s\). If \((u-r)/\tau\le-1\), then the desired inequality follows immediately from \(\tanh(\tau s-b)\ge-1\). Otherwise the quantity \((u-r)/\tau\) lies strictly between \(-1\) and \(1\). In that region put

\[
J(s)=\tau s-\operatorname{arctanh}\left(\frac{\tanh s-r}{\tau}\right).
\]

Differentiation yields the identity

\[
J'(s)=\frac{2\tau r\tanh s}
{\tau^2-(\tanh s-r)^2}.
\]

The denominator is strictly positive on this region, which is an interval containing \(s=0\). Consequently \(J\) decreases to \(0\) and then increases, with global minimum \(J(0)=\operatorname{arctanh}(r/\tau)=b\). Therefore \(J(s)\ge b\), or

\[
\tanh(\tau s-b)\ge\frac{\tanh s-r}{\tau},
\]

which is precisely \(H_b(s)\ge-r\). Reflection supplies \(H_{-b}(s)\le r\), so (2) is sufficient. Finally, \(|a|\le b\) is equivalent to

\[
\cosh\!\left(\frac{\log\alpha}{2}\right)\le\tau,
\]

which is the asserted sharp threshold. The boundary \(|a|=b\) gives zero logarithmic curvature at \(x=1/2\) and satisfies the global nonpositive-curvature inequality, so the endpoint cases are included. This completes the proof.

## Verification

The standalone program `verify_concrete.py` checks the exact polynomial identity behind (1), differentiates the CDF for six rational/integer parameter pairs, verifies midpoint-curvature formulas and the unit-logistic parameter change, and conducts 76 finite rational curvature diagnostics. It reports a positive midpoint curvature of \(68808/10201\) for \(\tau=2,\alpha=100\). Run `python verify_concrete.py` with Python 3 and SymPy. Finite diagnostics do not prove the all-real-parameter theorem: the complete proof is the hyperbolic comparison and monotonicity argument above.

## Relationship to prior work

Maddison, Mnih and Teh [1, Appendix B, Proposition 2] introduce the binary Concrete density and prove log-convexity for temperature at most one. They do not provide the complementary global log-concavity region. Beck, Bockelmann and Dekorsy [2, Section II-B, Figure 1 caption] state that the binary density is log-concave above temperature one without a bias restriction; the exact curvature counterexample above shows that this blanket assertion does not hold for unequal weights.

The same probability family is known as the **unit-logistic** or \(L_B\) family [3,4]. In [3]'s median/shape notation, the correspondence is \(\beta=\tau\) and \(\alpha=(\mu/(1-\mu))^\tau\), so the theorem can also be read as the precise log-concavity region for that established family. The inspected unit-logistic account [3] discusses density shapes and estimation but not this global sharp log-concavity criterion. Earlier treatment in [4] is a residual bibliographic risk; its full original text was not inspected.

## Limitations

The classification concerns a one-dimensional, two-category density on its original probability scale. It neither establishes multivariate Concrete log-concavity nor claims that a non-log-concave density must be multimodal. The comparison of relevant accessible texts does not establish exhaustive priority over all historical density-shape literature. In particular, the original 1982 account of the equivalent \(L_B\) family remains a possible source of earlier equivalent characterization.

## References

1. C. J. Maddison, A. Mnih, and Y. W. Teh, *The Concrete Distribution: A Continuous Relaxation of Discrete Random Variables*, arXiv:1611.00712 (first posted 2016-11-02), Appendix B. https://arxiv.org/abs/1611.00712
2. E. Beck, C. Bockelmann, and A. Dekorsy, *CMDNet: Learning a Probabilistic Relaxation of Discrete Variables for Soft Detection with Low Complexity*, arXiv:2102.12756 (first posted 2021-02-25), Section II-B and Figure 1 caption. https://arxiv.org/abs/2102.12756
3. A. F. B. Menezes, J. Mazucheli, and S. Dey, *The Unit-Logistic Distribution: Different Methods of Estimation*, Pesquisa Operacional **38** (2018), 555–578, DOI:10.1590/0101-7438.2018.038.03.0555. https://doi.org/10.1590/0101-7438.2018.038.03.0555
4. P. R. Tadikamalla and N. L. Johnson, *Systems of frequency curves generated by transformations of logistic variables*, Biometrika **69** (1982), 461–465, DOI:10.1093/biomet/69.2.461. https://doi.org/10.1093/biomet/69.2.461
