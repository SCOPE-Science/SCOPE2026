# Sharp Wasserstein contraction phases of power-biased interval splitting walks

## Finding
For every real \(p\ge0\), consider the interval Markov transition \(P_p(x,\cdot)\) which samples uniformly on \((0,x)\) with probability \(x^p/[x^p+(1-x)^p]\) and uniformly on \((x,1)\) with the complementary probability. Its optimal one-step Euclidean \(1\)-Wasserstein Lipschitz coefficient is
\[
C_p:=\sup_{0<x<y<1}\frac{W_1(P_p(x,\cdot),P_p(y,\cdot))}{y-x}
=\begin{cases}
\tfrac12,&p=0,\\
+\infty,&0<p<1,\\
0,&p=1,\\
\tfrac12,&1<p\le2,\\
\tfrac{p-1}{2},&p\ge2.
\end{cases}
\]
Consequently the kernel is nonexpansive in \(W_1\) precisely for \(p=0\) or \(1\le p\le3\), and is strictly contractive precisely for \(p=0\) or \(1\le p<3\). At \(p=1\) all transition laws are uniform on \((0,1)\). Here *strictly contractive* means its optimal coefficient is less than one, not that every different pair is separated by a strict inequality.

## Assumptions and scope
The state space is the open interval \((0,1)\), equipped with Euclidean distance; the endpoint values are used only as limiting states to compute suprema. The probability law has a density for every interior state. The parameter range in this theorem is exactly \(p\in[0,\infty)\), not the negative-parameter absorbing extension in the source paper. \(W_1\) is defined by the infimum of expected absolute displacement over all couplings; for laws on the real line it equals the integral of the absolute difference of their cumulative distribution functions.

## Proof
Write \(D(x)=x^p+(1-x)^p\), \(a(x)=x^{p-1}/D(x)\), and \(b(x)=(1-x)^{p-1}/D(x)\). For a threshold \(z\in(0,1)\), the transition CDF is
\[
F_x(z)=\begin{cases}z a(x),&z\le x,\\1-(1-z)b(x),&z\ge x.\end{cases}
\]
The two formulas agree at \(z=x\), and the derivative with respect to \(x\) therefore has no boundary delta mass. For each interior \(x\), dominated convergence on a sufficiently small state neighborhood and the one-dimensional transport identity give the exact infinitesimal slope
\[
\ell_p(x)=\lim_{h\to0}\frac{W_1(P_p(x+h,\cdot),P_p(x,\cdot))}{|h|}=
\frac{x^2|a'(x)|+(1-x)^2|b'(x)|}{2}.
\]
Integrating the CDF derivative along each state segment and using the triangle inequality gives \(W_1(P_p(x),P_p(y))\le\int_x^y\ell_p(s)\,ds\). The opposite bound for the supremum follows from the infinitesimal limit, so \(C_p=\sup_{0<x<1}\ell_p(x)\), including when the supremum is infinite.

When \(p=0\), \(a(x)=1/(2x)\) and \(b(x)=1/[2(1-x)]\), hence \(\ell_0\equiv1/2\). When \(p=1\), both densities are one, so \(\ell_1\equiv0\). For \(0<p<1\), direct expansion at the left endpoint yields \(b'(x)\sim-px^{p-1}\) and \(x^2|a'(x)|=O(x^p)\). Consequently \(\ell_p(x)\sim (p/2)x^{p-1}\to\infty\), proving the infinite coefficient.

It remains to consider \(p>1\). Reflecting \(x\mapsto1-x\), restrict to \(0<x\le1/2\) and introduce \(t=x/(1-x)\in(0,1]\). Elementary differentiation gives
\[
x^2a'(x)=\frac{v}{(1+t^p)^2},\quad
(1-x)^2b'(x)=\frac{u}{(1+t^p)^2},
\]
where
\[
v=t^p((p-1)+pt-t^p)>0,\qquad
u=1-pt^{p-1}+(1-p)t^p.
\]
If \(u\ge0\), then
\[
2\ell_p(x)=\frac{v+u}{(1+t^p)^2}
=\frac{1-pt^{p-1}(1-t^2)-t^{2p}}{(1+t^p)^2}\le1.
\]
If \(u<0\), algebra gives
\[
2\ell_p(x)=\frac{v-u}{(1+t^p)^2}=
\frac{pt^{p-1}(1+t)^2}{(1+t^p)^2}-1=R_p(t)-1.
\]
The function \(R_p\) is strictly increasing on \((0,1)\), since its logarithmic derivative has the sign of
\[
(p-1)(1-t^{p+1})+(p+1)(t-t^p)>0.
\]
As \(R_p(1)=p\), this branch yields \(\ell_p(x)\le(p-1)/2\). Conversely, \(\ell_p(x)\to1/2\) as \(x\downarrow0\), and \(\ell_p(1/2)=(p-1)/2\). Therefore \(C_p=\max\{1/2,(p-1)/2\}\). This proves all cases, including the exact boundary \(p=3\).

## Verification
The included standard-library script `check_w1.py` performs 4,704 finite assertions, including exact-rational integration of pairwise CDF differences for integer parameters, the exact inequalities at rational states, and finite differences for noninteger parameters. Reproduce using `python check_w1.py` with Python 3. All universal and endpoint claims are proved above; finite checks are independent regression evidence, not a replacement for the analytic argument.

## Relationship to prior work
Shah and Winstein [1] introduce the power-biased split kernel and establish its stationary distributions and Doeblin convergence in the positive-parameter regime (their Theorem 3.2). This finding addresses a different quantitative problem: the exact optimal \(W_1\) Lipschitz coefficient of **one transition** for every nonnegative parameter. In particular, the interval \(0<p<1\) has uniform ergodicity via the published minorization but an infinite one-step \(W_1\) Lipschitz coefficient. General iterated-random-function methods [2] motivate contractions but do not by themselves supply this sharp, parameter-dependent coefficient.

## Limitations
The theorem does not claim that absence of a one-step contraction precludes mixing, or that \(W_1\) expands after multiple transitions. Its metric is the ordinary Euclidean distance; other ground metrics may yield different results. Negative parameters and endpoint-absorbing extensions are excluded. Priority remains subject to previously unpublished or unindexed equivalent Lipschitz calculations.

## References
[1] Rikhav Shah and Vilas Winstein, *The maximum-entropy median-martingale*, arXiv:2605.03206v3 (first arXiv submission 2026-05-04), §3, especially Eq. (10) and Theorem 3.2. https://arxiv.org/pdf/2605.03206v3

[2] Persi Diaconis and David Freedman, *Iterated random functions*, SIAM Review 41 (1999), 45–76. https://doi.org/10.1137/S0036144598338446
