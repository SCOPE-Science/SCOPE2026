# A sharp log-concavity threshold for equal-shape Gamma rate mixtures

## Finding
Let \(\alpha>0\), \(0<a<b\), and \(0<w<1\). Consider the two-point rate mixture of Gamma densities with **common shape** \(\alpha\):
\[
f(x)=\frac{x^{\alpha-1}}{\Gamma(\alpha)}\bigl((1-w)a^{\alpha}e^{-ax}+wb^{\alpha}e^{-bx}\bigr),\qquad x>0.
\]
Define the normalized fast-rate amplitude ratio and shape-dependent threshold by
\[
r=\frac{wb^{\alpha}}{(1-w)a^{\alpha}},\qquad
R_{\alpha}=e^{2\sqrt{\alpha}}\frac{\sqrt{\alpha}-1}{\sqrt{\alpha}+1}\quad(\alpha>1).
\]
Then the density is log-concave on its whole support **if and only if**
\[
\boxed{\alpha>1\quad\text{and}\quad r\le R_{\alpha}.}
\]
At the sharp boundary \(r=R_{\alpha}\), its logarithmic second derivative is zero at exactly one point, \(x=2\sqrt{\alpha}/(b-a)\), and strictly negative everywhere else. For \(\alpha>1\) and \(r>R_{\alpha}\), the logarithmic second derivative is positive on exactly one nonempty bounded open interval and negative outside its closure. For \(0<\alpha\le1\), it is strictly positive at every positive \(x\).

Equivalently, for \(\alpha>1\) the largest admissible weight on the faster-rate component is
\[
w_*(\alpha,a,b)=\frac{R_{\alpha}a^{\alpha}}{b^{\alpha}+R_{\alpha}a^{\alpha}}.
\]
The criterion is exact, including equality; notably, the critical **amplitude ratio** \(R_{\alpha}\) depends on the common shape alone, not on the rate separation. For Erlang-2 components with rates \(a=1,b=2\), the threshold is \(w_*(2,1,2)\approx0.4205260186\); the weight \(w=2/5\) is admissible and \(w=1/2\) is not.

## Assumptions and scope
The Gamma rate parameterization is \(g_{\alpha,\lambda}(x)=\lambda^{\alpha}x^{\alpha-1}e^{-\lambda x}/\Gamma(\alpha)\) on \(x>0\). Both mixing weights are strictly positive, the rates are strictly positive and distinct, and \(\alpha\) is any real positive shape. When the rates coincide or a mixing weight is zero, the mixture reduces to a single Gamma density, which is log-concave exactly when \(\alpha\ge1\). This separate degenerate case is not included in the displayed two-rate equivalence.

## Proof
Put \(d=b-a>0\), \(q=\alpha-1\), and \(c=\log r\), and set \(t=dx\). Factoring the slow-rate component gives
\[
\log f(x)=(\alpha-1)\log x-ax+\log(1+re^{-dx})+\text{constant}.
\]
Two differentiations yield the exact identity
\[
\frac{(\log f)''(x)}{d^2}=-\frac{q}{t^2}+\frac{re^{-t}}{(1+re^{-t})^2}
=-\frac{q}{t^2}+\frac1{4\cosh^2((t-c)/2)}.\tag{1}
\]
If \(\alpha\le1\), the first term is nonnegative and the second strictly positive: global log-concavity fails, with strict positive curvature everywhere.

Now suppose \(q>0\) and define
\[
H_c(t)=\frac{t}{2\cosh((t-c)/2)},\qquad t>0.
\]
By (1), global log-concavity is equivalent to \(\sup_{t>0}H_c(t)\le\sqrt q\). Moreover,
\[
(\log H_c)'(t)=\frac1t-\frac12\tanh((t-c)/2),\qquad
(\log H_c)''(t)=-\frac1{t^2}-\frac14\operatorname{sech}^2((t-c)/2)<0.
\]
The function \(H_c\) tends to zero both as \(t\downarrow0\) and as \(t\to\infty\), so it has a unique strict maximum. Its maximum \(M(c)\) is **strictly increasing** in \(c\): for every \(h>0\) and every \(t>0\),
\[
H_{c+h}(t+h)=\frac{t+h}{t}H_c(t)>H_c(t).
\]
In particular, using a maximizer for \(H_c\) proves \(M(c+h)>M(c)\). Also, \(M(c)\le2e^{c/2-1}\to0\) as \(c\to-\infty\), and \(M(c)\ge c/2\to\infty\) as \(c\to\infty\) through positive \(c\). Consequently there is exactly one critical \(c_*\) with \(M(c_*)=\sqrt q\).

At that boundary let \(t_*\) be the unique maximizer and \(u=(t_*-c_*)/2\). The equalities \(H_{c_*}(t_*)=\sqrt q\) and \((\log H_{c_*})'(t_*)=0\) give
\[
\operatorname{sech}^2u=\frac{4q}{t_*^2},\qquad
\tanh u=\frac2{t_*}.
\]
Using \(\operatorname{sech}^2u+\tanh^2u=1\) yields \(t_*^2=4(q+1)=4\alpha\). Since \(u>0\),
\[
c_*=2\sqrt\alpha-2\operatorname{arsinh}\bigl(1/\sqrt{\alpha-1}\bigr)
=\log\!\left(e^{2\sqrt\alpha}\frac{\sqrt\alpha-1}{\sqrt\alpha+1}\right)=\log R_\alpha.
\]
Because \(M\) increases strictly, the requisite inequality holds precisely when \(c\le c_*\), equivalently \(r\le R_\alpha\). If \(r=R_\alpha\), uniqueness of the maximizer makes the curvature vanish only at \(t_*=2\sqrt\alpha\). If \(r>R_\alpha\), strict concavity of \(\log H_c\) and the two zero endpoint limits show that the superlevel set \(\{t:H_c(t)>\sqrt q\}\) is exactly one nonempty bounded open interval with precisely two boundary points. The sign conclusions follow from (1). This proves the whole classification.

For the tail-instability consequence, fix any \(\alpha>1\), \(a>0\), and a fast-component weight satisfying \(w>R_\alpha/(1+R_\alpha)\). As \(b\downarrow a\) through strictly larger rates, \(r\to w/(1-w)>R_\alpha\); hence all sufficiently close unequal-rate mixtures fail log-concavity although they converge in total variation to the log-concave Gamma density of rate \(a\). For any fixed \(c>c_*\), the positive-curvature interval lies at \(x=t/d\) with \(t\) bounded away from zero, so its location escapes to infinity as \(d\downarrow0\). All limiting assertions follow by continuity of Gamma densities in their rate and dominated convergence.

## Verification
The standalone program `verify.py` uses the standard Python library to check 100 exact-rational reformulations of the curvature numerator, critical tangencies for nine shapes, sign changes on a finite parameter grid, and the Erlang-2 weight example; it reports 196 checks. These are consistency diagnostics. The all-parameter, all-\(x\) theorem follows from the analytic differentiation and strictly concave one-variable maximization above, not finite grid sampling. To reproduce, run `python verify.py` with Python 3; no data, specialized software, or external files are needed.

## Relationship to prior work
Two-stage and more general hyper-Erlang mixtures are standard finite phase-type models. Neumüller, Robert, and Heuberger (2022) study **convolution** and algebraic evaluation for hyper-Erlang and hyper-exponential distributions; the available abstract does not state an intrinsic log-concavity boundary, although the complete article was not accessible for comparison. Yu (2009, especially Section 2, Example 5) gives stochastic-order comparisons for Gamma scale mixtures and proves convexity of the log ratio of a mixture to a fixed-family reference; that relative log-concavity statement does not itself compare the mixture's log-Hessian to zero or supply the present sharp threshold. Levy (arXiv:2006.12428, Sections 2–4) develops convolution-density identities rather than a two-point mixing-weight curvature classification. Mu (arXiv:1312.2166) treats shape-constrained **Beta** mixtures, not Gamma rate mixtures. A common-rate Gamma **shape**-mixture has densities proportional to \(x^{\alpha-1}e^{-\lambda x}(A+Bx^d)\), whereas the present rate-mixture family has \(x^{\alpha-1}(Ae^{-ax}+Be^{-bx})\). Neither family contains the other for distinct parameters.

## Limitations
The result concerns exactly two rates and a common positive shape; it does not classify three-or-more-rate Gamma mixtures, mixtures of unequal shapes, unequal-shape/unequal-rate mixtures, or arbitrary continuous mixing laws. The explicit threshold applies to ordinary density log-concavity and does not itself determine other reliability orders or optimal estimation procedures. The cited 2022 hyper-Erlang conference article could not be read in full, and a 2026 general two-log-concave-component separation preprint was available only through abstract-level material; an equivalent earlier or more general result cannot be ruled out without further primary-source inspection.

## References
1. C. Neumüller, J. Robert, and A. Heuberger, *Convolving Hyper-Erlang with Hyper-Exponential Distributions Using Linear Algebra* (ICoMS 2022), DOI: 10.1145/3545839.3545840. Public author listing dates the article to September 10, 2022.
2. Y. Yu, *Stochastic Ordering of Exponential Family Distributions and Their Mixtures*, Journal of Applied Probability 46 (2009), 244–254, DOI: 10.1239/jap/1238592127.
3. E. Levy, *On the density for sums of independent exponential, Erlang and gamma variates*, arXiv:2006.12428, first posted June 22, 2020.
4. X. Mu, *Log-concavity of a Mixture of Beta Distributions*, arXiv:1312.2166, 2013.
5. M. T. Boedihardjo and Y. Xie, *Mixture and separation of log-concave measures*, arXiv:2607.17368, 2026 (abstract-level comparison only).
