# Exact three-threshold weight phase diagram for two-Laplace tails
## Finding
Let \(X_1,X_2\) be independent standard Laplace random variables, each with density \(e^{-|x|}/2\). For nonnegative weights \(a,b\) constrained by \(a^2+b^2=1\), define
\[
T_t(a,b)=\Pr\!\left\{aX_1+bX_2>\sqrt{2}\,t}\right\},\qquad t>0.
\]
Since interchange of the two weights does not change the law, write
\[
r=\frac{\min(a,b)}{\max(a,b)}\in[0,1].
\]
For \(0<r<1\), with \(a=(1+r^2)^{-1/2}\) and \(b=ra\), the upper tail is exactly
\[
T_t(r)=\frac{\exp\!\big(-\sqrt{2}\,t\sqrt{1+r^2}\big)-r^2\exp\!\big(-\sqrt{2}\,t\sqrt{1+r^2}/r\big)}{2(1-r^2)}.
\]
There are three natural thresholds in the variance-normalized weight geometry.

First, the sparse endpoint \(r=0\) changes local type at
\[
t_s=\sqrt2.
\]
It is a strict relative local minimum for \(0<t<t_s\) and a strict relative local maximum for \(t>t_s\).

Second, the equal-weight endpoint \(r=1\) changes local type at
\[
t_e=\frac{3+\sqrt{21}}4=1.895643923738960\ldots.
\]
It is a strict relative local maximum for \(0<t<t_e\) and a strict relative local minimum for \(t>t_e\).

Third, the sparse and equal endpoint tail heights cross at one positive threshold
\[
t_*=-1-\frac{W_{-1}(-(2-\sqrt2)e^{-(2-\sqrt2)})}{2-\sqrt2}
   =1.687952825208936\ldots,
\]
where \(W_{-1}\) denotes the lower real branch of the Lambert \(W\) function. These thresholds satisfy
\[
\sqrt2<t_*<\frac{3+\sqrt{21}}4.
\]
Consequently, throughout the nonempty coexistence window
\[
\sqrt2<t<\frac{3+\sqrt{21}}4,
\]
both the sparse and equal-weight endpoints are strict relative local maxima. Because the tail profile is continuous on the compact unordered weight arc, it therefore has at least one interior global minimizer in this window. The taller endpoint maximum is the equal-weight endpoint for \(t<t_*\), and the sparse endpoint for \(t>t_*\). No uniqueness of the interior minimizer and no global-maximality of either endpoint are asserted.

## Assumptions and scope
The random variables are independent and exactly standard Laplace. The normalization \(a^2+b^2=1\) fixes \(\operatorname{Var}(aX_1+bX_2)=2\), so \(t\) is measured in standard-deviation units in the same normalization used by variance-scaled Laplace tail bounds. Signs of the weights are irrelevant by symmetry, so taking \(a,b\ge0\) loses no distributional generality for two summands. Endpoint statements are relative to the unordered compact arc of weights.

The claim is an exact two-summand finite-threshold statement. It does not classify all stationary points, does not claim uniqueness of the interior minimizer, and does not extend the local phase diagram to three or more summands.

## Proof
Assume first that \(a>b>0\) and set \(S=aX_1+bX_2\). The moment-generating function is
\[
\mathbb E e^{sS}=\frac1{(1-a^2s^2)(1-b^2s^2)}
=\frac{a^2}{a^2-b^2}\frac1{1-a^2s^2}-\frac{b^2}{a^2-b^2}\frac1{1-b^2s^2}.
\]
The two terms are the moment-generating functions of centered Laplace laws with scales \(a\) and \(b\). Therefore, for \(z>0\),
\[
\Pr\{S>z\}=
\frac{a^2e^{-z/a}-b^2e^{-z/b}}{2(a^2-b^2)}.
\]
Taking \(z=\sqrt2\,t\), \(a=(1+r^2)^{-1/2}\), and \(b=ra\) gives the displayed formula for \(T_t(r)\).

At the sparse endpoint,
\[
T_t(0)=\frac12e^{-\sqrt2\,t}.
\]
For fixed \(t>0\), the second exponential in the exact interior formula is flat at \(r=0\), while the first term has the expansion
\[
T_t(r)=\frac12e^{-\sqrt2\,t}\left[1+\left(1-\frac{t}{\sqrt2}\right)r^2+O(r^4)\right].
\]
Hence the sparse endpoint is a strict relative local minimum for \(t<\sqrt2\) and a strict relative local maximum for \(t>\sqrt2\).

For the equal endpoint it is convenient to write \(p=a^2\in[1/2,1]\), so \(b^2=1-p\), and put \(x=\sqrt2\,t\) and
\[
h_x(u)=u\exp(-x/\sqrt u).
\]
For \(p\ne1/2\),
\[
T_t(p)=\frac{h_x(p)-h_x(1-p)}{2(2p-1)}.
\]
Writing \(p=1/2+q\), Taylor expansion gives
\[
T_t(1/2+q)=\frac12h_x'(1/2)+\frac{q^2}{12}h_x'''(1/2)+O(q^4).
\]
Direct differentiation yields
\[
h_x'''(u)=\frac{x e^{-x/\sqrt u}}{8u^{7/2}}
\left(x^2-3x\sqrt u-3u\right).
\]
At \(u=1/2\), its sign is the sign of \(4t^2-6t-3\). The unique positive zero is
\[
t_e=\frac{3+\sqrt{21}}4,
\]
which proves the equal-endpoint local classification. The limiting value itself is the familiar two-Laplace convolution tail
\[
T_t(1)=\frac12(1+t)e^{-2t}.
\]

The ratio of the equal to sparse endpoint tails is
\[
R(t)=\frac{T_t(1)}{T_t(0)}=(1+t)e^{-(2-\sqrt2)t}.
\]
Its logarithmic derivative is
\[
\frac{d}{dt}\log R(t)=\frac1{1+t}-(2-\sqrt2),
\]
so \(R\) increases up to \(t=1/\sqrt2\) and then decreases strictly to zero. Because \(R(0)=1\), there can be at most one further positive crossing. It exists after \(\sqrt2\): indeed
\[
\log R(\sqrt2)=\log(1+\sqrt2)-(2\sqrt2-2)>0.
\]
For the last inequality, \(\log(1+\sqrt2)=\operatorname{arsinh}(1)=\int_0^1(1+u^2)^{-1/2}\,du\ge5/6\), while \(2\sqrt2-2<5/6\). At \(t_e\), \(1+t_e<3\). Moreover \(e^{11/10}>\sum_{k=0}^{5}(11/10)^k/k!>3\), so \(\log3<11/10\). Also \(2-\sqrt2>117/200\) and \(t_e>3791/2000\), hence \((2-\sqrt2)t_e>443547/400000>11/10\). Therefore \(\log R(t_e)<0\), and the unique positive crossing lies strictly between \(\sqrt2\) and \(t_e\). Solving \((1+t)e^{-(2-\sqrt2)t}=1\) gives the stated Lambert-\(W\) expression on branch \(W_{-1}\).

Finally, when \(\sqrt2<t<t_e\), both endpoints are strict relative local maxima. Continuity on the compact arc guarantees a global minimum, and neither endpoint can be a minimizer, so at least one global minimizer lies in the interior.

## Verification
The accompanying `verify.py` independently evaluates the exact tail formula, the endpoint formulas, the two local-type coefficients, and the three threshold values. It brackets the unique positive endpoint crossover by bisection on the strictly decreasing post-maximum branch and checks
\[
\sqrt2<t_*<t_e.
\]
It also evaluates nearby weights on both sides of the phase changes as a numerical stress test. These computations check the algebra and constants; the proof of the local classifications is the Taylor analysis above, not the finite numerical sampling.

## Relationship to prior work
Li and Tkocz study weighted sums of independent two-sided exponentials and prove nonasymptotic upper and lower bounds whose leading large-threshold behavior is controlled by the largest weight. Their Theorem 1 uses the same variance normalization and shows the tail scale \(e^{-\alpha t+o(t)}\), while their Section 4.2 discusses an S-inequality improvement for small thresholds. The inspected full text does not give the exact two-summand weight profile, the sparse and equal local-type thresholds, their coexistence window, or the endpoint-height crossover derived here.

Gluskin and Kwapień give broad tail and moment estimates for weighted sums with logarithmically concave tails, exact up to distribution-dependent constants. Such estimates do not determine the exact finite-threshold bifurcation constants above. The S-inequality literature cited by Li and Tkocz controls dilations of unconditional sets; it supplies a different type of comparison and does not state this exact signed-linear-form weight phase diagram.

A search of published mathematical findings for aliases such as fixed-variance weighted Laplace tails, sparse-versus-equal weights, two-Laplace convolution tail extrema, and endpoint crossover returned no statement implying the three-threshold classification. The closest returned items concern positive gamma-sum quantile curvature or unrelated Laplace location-modulus problems, not the same tail functional.

## Limitations
The exact convolution formula itself is classical and is not claimed as new. The originality claim is the finite-threshold three-phase synthesis: the two endpoint local bifurcations, the unique positive endpoint-height crossover, the strict ordering of those thresholds, and the resulting coexistence window with an interior global minimizer.

A residual literature risk remains that a specialized majorization or convolution paper not located in the searches may contain an equivalent exact two-weight classification. The result is only for two independent standard Laplace variables under fixed variance; higher-dimensional weight simplices may have additional stationary-point phenomena. The degenerate threshold values \(t=\sqrt2\) and \(t=t_e\) are identified as changes of the quadratic local coefficient but no higher-order classification at those exact values is claimed.

## References
1. Jiawei Li and Tomasz Tkocz, “Tail bounds for sums of independent two-sided exponential random variables,” arXiv:2109.14387, first submitted 2021-09-29; later in *High Dimensional Probability IX*, 2023.
2. E. D. Gluskin and S. Kwapień, “Tail and moment estimates for sums of independent random variables with logarithmically concave tails,” *Studia Mathematica* 114 (1995), 303–309, DOI 10.4064/sm-114-3-303-309.
3. Piotr Nayar and Tomasz Tkocz, “The unconditional case of the complex S-inequality,” *Israel Journal of Mathematics* 197 (2013), 99–106.
