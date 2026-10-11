# Exact quadratic generalized rectangular constant and extremizers of real \(L_4\)

## Finding
Let \((\Omega,\Sigma,\nu)\) be a measure space containing two disjoint measurable sets of finite, strictly positive measure, and let \(X=L_4(\nu;\mathbb R)\). For unit vectors \(x,y\in X\), write \(x\perp_B y\) when \(\|x+t y\|_4\ge\|x\|_4\) for every real \(t\). Define the Gastinel–Joly quadratic generalized rectangular constant
\[
\mu_2(X)=\sup_{\substack{x,y\in S_X,\ x\perp_B y\\ \lambda\ge0}}
\frac{(1+\lambda^2)^{1/2}}{\|x+\lambda y\|_4}.
\]
Let \(u_*\) be the unique root in \((0,1/\sqrt3)\) of
\[
P(u)=9u^4+9u^3-12u^2-3u+1=0.
\]
Then
\[
\boxed{\displaystyle
\mu_2(X)^4=\frac{(9u_*^4-9u_*^3-6u_*^2+9u_*+1)^2}
{(1+3u_*^2)^2(1+9u_*^2-9u_*^4)}}
\]
and \(\mu_2(X)=1.38784956695846120434\ldots\). This value is independent of the dimension, of the presence of atoms, and of the positive measures of the available disjoint sets. The supremum is attained by vectors supported on any two such sets.

More precisely, put
\[
\lambda_*=\frac{3\sqrt{u_*(1-u_*^2)}}{1-3u_*^2},\qquad
 t_\pm=\frac{-\sqrt{1-u_*^2}\pm\sqrt{1+3u_*^2}}{2\sqrt{u_*}},
\]
\[
w_+=\frac{-t_-}{t_+-t_-},\qquad w_-=\frac{t_+}{t_+-t_-}.
\]
Every maximizing triple \((x,y,\lambda)\), with \(\lambda\ge0\), has \(\lambda=\lambda_*\) and, after discarding common zero sets, the ratio \(y/x\) is \(t_+\) on one measurable part and \(t_-\) on its complement; the respective integrals of \(|x|^4\) are exactly \(w_+,w_-\). Conversely, every such pair, with \(\|x\|_4=1\), is maximizing. Signed changes of \(x\) on its support are harmless. This is an equality classification, not merely a construction of one extremizer.

## Assumptions and scope
All spaces and orthogonality notions here are **real**. No total-finiteness or sigma-finiteness assumption on \(\nu\) is needed beyond the two finite positive-measure sets above. Integrals below are over \(\Omega\). The subscript \(2\) belongs to the numerator exponent in the Gastinel–Joly definition; the ambient norm exponent is \(4\). The theorem therefore does **not** give the classical rectangular constant \(\mu_1\) or the exponent-matched value \(\mu_4\).

## Proof
**1. Moment reduction.** Because the real \(L_4\)-norm is smooth, for unit vectors \(x,y\), Birkhoff–James orthogonality is equivalent to \(\int x^3y\,d\nu=0\). Set
\[
A=\int x^2y^2\,d\nu,\qquad B=\int xy^3\,d\nu.
\]
Hölder's inequality gives \(0\le A\le1\). The exact quartic expansion is
\[
\|x+\lambda y\|_4^4=1+\lambda^4+6A\lambda^2+4B\lambda^3.
\]
By orthogonality and Cauchy–Schwarz,
\[
B=\int xy(y^2-Ax^2)\,d\nu,\quad
 B^2\le A\int(y^2-Ax^2)^2\,d\nu=A(1-A^2).
\]
Thus, with \(s(u)=\sqrt{u(1-u^2)}\),
\[
\|x+\lambda y\|_4^4\ge D(A,\lambda)
 :=1+\lambda^4+6A\lambda^2-4\lambda^3s(A).
\]

**2. The reduction is sharp at every parameter.** Fix \(0<u<1\), set \(c=\sqrt{(1-u^2)/u}\), and take \(t_+,t_-\) as in the finding with \(u\) in place of \(u_*\). These are the positive and negative roots of \(t^2+ct-u=0\). Let \(w_+=-t_-/(t_+-t_-)\) and \(w_-=t_+/(t_+-t_-)\). The probability law assigning mass \(w_\pm\) to \(t_\pm\) has moments
\[
\mathbb E[t]=0,\quad \mathbb E[t^2]=u,\quad
\mathbb E[t^3]=-\sqrt{u(1-u^2)},\quad \mathbb E[t^4]=1.
\]
Indeed \(t^2=u-ct\), from which all four identities follow recursively. On two disjoint finite positive-measure sets \(E_+,E_-\), take \(x\) to equal \((w_\pm/\nu(E_\pm))^{1/4}\) on \(E_\pm\), zero otherwise, and let \(y=t_\pm x\) there. Then \(x,y\) are unit vectors, \(\int x^3y=0\), \(A=u\), and \(B=-s(u)\). Hence the lower bound \(D(u,\lambda)\) is attained simultaneously for every \(\lambda\ge0\) at each fixed \(u\in(0,1)\). Continuity handles \(u=0,1\) when taking infima. Consequently
\[
\mu_2(X)^4=\sup_{u\in[0,1],\,\lambda\ge0}
\frac{(1+\lambda^2)^2}{D(u,\lambda)}.
\]

**3. Optimizing the overlap moment.** For fixed \(\lambda>0\), \(s(u)\) is strictly concave on \([0,1]\), so \(D(u,\lambda)\) is strictly convex in \(u\). Its derivative is
\[
\partial_u D=6\lambda^2-2\lambda^3\frac{1-3u^2}{s(u)}.
\]
This derivative is negative near \(u=0\), positive for \(u\ge1/\sqrt3\), and strictly increasing. Thus its unique zero, and hence the unique minimizing overlap parameter, lies in \((0,1/\sqrt3)\). The zero equation is
\[
\lambda=\lambda(u):=\frac{3s(u)}{1-3u^2}.
\]
Since \(s'(u)\) strictly decreases from \(+\infty\) to \(0\) on that interval, \(\lambda(u)=3/(2s'(u))\) is a strictly increasing bijection onto \((0,\infty)\).

**4. Optimizing the quadratic numerator.** Substitute \(\lambda(u)\) into the ratio. Direct algebra, without estimates, yields
\[
G(u):=\frac{(1+\lambda(u)^2)^2}{D(u,\lambda(u))}
 =\frac{R(u)^2}{(1+3u^2)^2(1+9u^2-9u^4)},
\]
where \(R(u)=9u^4-9u^3-6u^2+9u+1\). Its derivative factors as
\[
G'(u)=\frac{-18(3u^4-6u^2-1)R(u)P(u)}
{(1+3u^2)^3(9u^4-9u^2-1)^2}.
\]
For \(0<u<1/\sqrt3\), the denominator is strictly positive, \(3u^4-6u^2-1<0\), and \(R(u)>0\), since \(R(u)=(1-3u^2)^2+9u(1-u^2)\). Therefore \(G'\) has the sign of \(P\). We have \(P(0)=1\), \(P(1/\sqrt3)=-2\). Moreover \(P''(u)=108u^2+54u-24\) is strictly increasing with one zero, so \(P'(u)\) first decreases and then increases; both endpoint values \(P'(0)=-3\) and \(P'(1/\sqrt3)=6-4\sqrt3\) are negative. Thus \(P\) strictly decreases and has a unique root \(u_*\) in the interval. It follows that \(G\) has one global maximum there. The limits of the original ratio as \(\lambda\to0\) or \(\lambda\to\infty\) equal \(1\), whereas the interior maximum is greater than \(1\); the displayed expression is therefore the global constant.

**5. Rigidity of equality.** Uniqueness in steps 3–4 forces \(A=u_*\) and \(\lambda=\lambda_*\). Equality in Cauchy–Schwarz requires \(y^2-u_*x^2=-cxy\) a.e., where \(c=\sqrt{(1-u_*^2)/u_*}\), with the negative sign forced by \(B=-s(u_*)\). At points where \(x=0\), the equation forces \(y=0\). Elsewhere \(y/x\) must be one of the two roots \(t_\pm\). The orthogonality equation, normalization and positivity of the two roots' weights force exactly the quoted \(w_\pm\); conversely the moment construction attains equality. This proves the claimed classification for finite- or infinite-dimensional real \(L_4\).

## Verification
The included standalone `verify.py` performs exact symbolic identities with SymPy for the rational profile and its derivative factorization; it checks the endpoint polynomial values, computes the unique root at 75-digit precision, reconstructs the two-atom extremizer through five moment identities, and tests 16,800 finite-dimensional numerical ratios for orthogonal pairs in dimensions 2, 3, 4, 6 and 9. Its expected first output line is `VERIFY_OK symbolic_identities=3 root_bracket=1 two_atom_moments=5 random_pair_ratios=16800`. The symbolic identities and independent derivation above—not the finite random tests—support the theorem over arbitrary measure spaces.

## Relationship to prior work
Baronti, Casini and Papini [1] define and examine the generalized Gastinel–Joly parameter; their Section 5 gives bounds for the exponent-matched \(\mu_p(\ell_p)\) and states that exact values are generally unknown. Their parameter definition covers \(\mu_2\) on \(L_4\), but the inspected ten-page article does not give the present exact value or extremizers. A related published computation [2] determines \(\mu_4(\ell_4^2)\), not \(\mu_2\); its critical overlap parameter is \(\sqrt{(5-\sqrt{17})/12}\approx0.270323\), whereas this problem's unique critical overlap is \(u_*\approx0.200994\). Their common Cauchy moment envelope does not itself determine the different quadratic numerator's sharp optimization or the entire \(L_4\) equality classification. Paul, Ghosh and Sain [3] address the classical \(\mu_1\), which is not the present constant.

## Limitations
The result is for **real** \(L_4\) spaces with at least two disjoint positive finite-measure sets and only for the generalized exponent \(2\). No assertion about complex \(L_4\), the classical exponent \(1\), or other ambient exponents is made. A full-text comparison with Gastinel and Joly's original 1970 paper was unavailable; unindexed equivalent formulations are a residual originality risk. The numerical checks do not certify infinite-dimensional statements.

## References
[1] M. Baronti, E. Casini, P. L. Papini, “Revisiting the Rectangular Constant in Banach Spaces,” *Bull. Aust. Math. Soc.* 105 (2022), 124–133, first publicly available 26 April 2021; DOI: 10.1017/S0004972721000253.

[2] “Exact generalized rectangular constant of the real \(\ell_4^2\) plane,” published research note, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-generalized-rectangular-constant-of-the-real-ell-4-2-plane--1e948b1d4c03.

[3] K. Paul, P. Ghosh, D. Sain, “On rectangular constant in normed linear spaces,” *J. Convex Anal.* 24 (2017), 917–925, arXiv:1407.1353, first public submission 5 July 2014.

[4] N. Gastinel, J. L. Joly, “Condition numbers and general projection method,” *Linear Algebra Appl.* 3 (1970), 185–224, DOI: 10.1016/0024-3795(70)90015-7 (full text not inspected).
