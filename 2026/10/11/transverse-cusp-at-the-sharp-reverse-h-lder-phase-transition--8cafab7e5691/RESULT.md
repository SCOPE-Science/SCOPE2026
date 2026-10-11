# Transverse cusp at the sharp reverse-Hölder phase transition
## Finding
Let \(E\) be a standard exponential random variable. For \(p\ge 1\), set
\[
A(p)=\Gamma(p+1)^{1/p},\qquad
B(p)=\frac{e}{2}\bigl(\mathbb E|E-1|^p\bigr)^{1/p},
\qquad
C_p=\max\{A(p),B(p)\}.
\]
The sharp reverse-Hölder theorem of Melbourne, Roysdon, Tang and Tkocz gives a unique transition exponent
\[
p_0\in(2.9414,2.9415)
\]
such that \(C_p=A(p)\) for \(1\le p\le p_0\) and \(C_p=B(p)\) for \(p\ge p_0\).

At this transition the two branches cross transversely. In particular, \(C_p\) is continuous but not differentiable at \(p_0\), and
\[
C'_+(p_0)-C'_-(p_0)
>
\frac{C_{p_0}}{90p_0}
>
\frac{C_{p_0}}{270}.
\]
Thus the change of extremizer is a genuine first-order cusp in the optimal constant.

## Assumptions and scope
The statement concerns the sharp \(L_p\)-to-\(L_1\) constant for centered one-dimensional log-concave random variables from arXiv:2505.00944. The proof uses the source theorem identifying the two exact analytic branches and the source bracket \(p_0\in(2.9414,2.9415)\). No claim is made here about the separate variance-normalized transition discussed in the same literature.

Write
\[
M(p)=\mathbb E|E-1|^p,\qquad
J(p)=\int_0^1 x^p e^x\,dx,
\]
so that
\[
M(p)=e^{-1}\bigl(\Gamma(p+1)+J(p)\bigr).
\]
Also define
\[
h(p)=A(p)^p-B(p)^p
=\Gamma(p+1)-\left(\frac e2\right)^p M(p).
\]
The source proves that \(h\) is positive immediately to the left of \(p_0\), negative immediately to the right, and vanishes at \(p_0\).

## Proof
Put \(p=p_0\), \(\Gamma_0=\Gamma(p+1)\), and \(q=J(p)/\Gamma_0\). At the crossing,
\[
\Gamma_0=\left(\frac e2\right)^p e^{-1}\bigl(\Gamma_0+J(p)\bigr),
\]
hence
\[
1+q=e\left(\frac2e\right)^p.
\]
Using \(\log 2<7/10\) and \(p>2.94=147/50\),
\[
\log(1+q)
=
1-p(1-\log 2)
<
\frac{59}{500}.
\]
Since \(\log(6/5)>1/6>59/500\), it follows that \(q<1/5\), and therefore
\[
\frac q{1+q}<\frac16.
\]

Differentiate \(h\). Since
\[
M'(p)=e^{-1}\left(\Gamma(p+1)\psi(p+1)+J'(p)\right),
\]
the crossing identity gives
\[
\frac{h'(p)}{\Gamma_0}
=
\frac q{1+q}
\left(\psi(p+1)-\frac{J'(p)}{J(p)}\right)
-
\log\frac e2.
\]
Here \(\psi\) is the logarithmic derivative of \(\Gamma\).

Strict convexity of \(\log\Gamma\) gives
\[
\psi(p+1)<\log(p+1)<\log 4<\frac75.
\]
For the integral term, use the probability measure on \((0,1)\) with density proportional to \(x^p\). The function \(e^x\) is increasing while \(-\log x\) is decreasing, so the opposite-monotonicity covariance inequality yields
\[
-\frac{J'(p)}{J(p)}<\frac1{p+1}<\frac13.
\]
Consequently,
\[
\frac{h'(p_0)}{\Gamma(p_0+1)}
<
\frac16\left(\frac75+\frac13\right)-\frac3{10}
=
-\frac1{90}.
\]
In particular, \(h'(p_0)<0\).

At the crossing \(A(p_0)=B(p_0)=C_{p_0}\), and direct differentiation of \(h=A^p-B^p\) gives
\[
h'(p_0)
=
p_0 C_{p_0}^{p_0-1}
\bigl(A'(p_0)-B'(p_0)\bigr).
\]
The source branch ordering implies \(C'_-(p_0)=A'(p_0)\) and \(C'_+(p_0)=B'(p_0)\). Therefore
\[
C'_+(p_0)-C'_-(p_0)
=
-\frac{h'(p_0)}{p_0C_{p_0}^{p_0-1}}
>
\frac{\Gamma(p_0+1)}{90p_0C_{p_0}^{p_0-1}}
=
\frac{C_{p_0}}{90p_0}.
\]
Finally \(p_0<3\), so this is strictly larger than \(C_{p_0}/270\).

## Verification
The accompanying script `verify.py` independently evaluates the crossing by standard-library quadrature and bisection, evaluates the two branch derivatives numerically, and checks the exact rational margin
\[
\frac16\left(\frac75+\frac13\right)-\frac3{10}=-\frac1{90}.
\]
Its numerical output is only a consistency check. The proof above is analytic and does not depend on floating-point calculations.

## Relationship to prior work
Melbourne, Roysdon, Tang and Tkocz determine the exact sharp constant as the maximum of the two branches above and prove that the branch difference has a unique zero \(p_0\in(2.9414,2.9415)\) with the stated sign change. Their appendix establishes uniqueness and the sign pattern by a crossing argument, but does not give a nonzero derivative at the crossing or a differentiability analysis of \(C_p\).

Eitan's earlier theorem reduces general centered log-concave norm-ratio problems to a one-parameter two-sided exponential family. It does not determine this \(L_1\)-normalized transition or the derivative jump. The present statement is therefore a local structural refinement of the newly determined sharp constant: a sign-changing crossing could in principle have odd order greater than one, whereas the estimate above proves quantitative transversality.

## Limitations
The lower bound \(C_{p_0}/(90p_0)\) is deliberately coarse and is not claimed to be sharp. Numerical evaluation gives a much larger derivative jump, but no numerical value is part of the theorem. The result concerns only the sharp \(L_p\)-to-\(L_1\) constant and does not settle the separate \(L_p\)-to-\(L_2\) transition problem.

## References
1. J. Melbourne, M. Roysdon, C. Tang, T. Tkocz, *From simplex slicing to sharp reverse Hölder inequalities*, arXiv:2505.00944, first posted 2025-05-02; Journal of the London Mathematical Society, DOI 10.1112/jlms.70461.
2. Y. Eitan, *The centered convex body whose marginals have the heaviest tails*, Studia Mathematica 274 (2024), 201--215; arXiv:2110.14382.
