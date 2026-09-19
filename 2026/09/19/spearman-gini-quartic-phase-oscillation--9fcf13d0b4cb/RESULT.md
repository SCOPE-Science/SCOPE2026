# Third-order universality and quartic phase oscillation at the Spearman–Gini boundary

## Statement

Let
\[
\overline\rho(g)=\max\{\rho(C): C\text{ a bivariate copula},\ \gamma(C)=g\}
\]
be the rho-maximal boundary at fixed Gini's gamma. Ansari, Rockel and Steinmaßl (2026) give an exact parametrization
\((G(\theta),P(\theta))\), \(\theta\in[0,\infty]\), with
\(\overline\rho(G(\theta))=P(\theta)\), and show only the leading endpoint relation
\[
\overline\rho(g)=1-\frac32(1-g)^2+O((1-g)^3),\qquad g\uparrow1.
\]

The same exact parametrization yields the sharper universal expansion
\[
\boxed{
\overline\rho(g)
=1-\frac32(1-g)^2
+\frac{5+3\sqrt3}{2}(1-g)^3
+O((1-g)^4).
}
\tag{1}
\]
Thus the infinitely many algebraic pieces accumulating at comonotonicity are invisible through cubic order.

They first become visible at quartic order. Put
\[
A=\frac{5+3\sqrt3}{2},\qquad
K_0=\frac{39}{2}+\frac{45\sqrt3}{4}.
\]
For \(\theta=N+x\), with fixed \(x\in[0,1)\) and \(N\to\infty\), set
\[
y_N=1-G(N+x),\qquad r_N=1-P(N+x),\qquad
u=\min\{x,1-x\}.
\]
Then
\[
\boxed{
\frac{r_N-\frac32y_N^2+A y_N^3}{y_N^4}
\longrightarrow
K(u):=K_0+16u^3-24u^4.
}
\tag{2}
\]
At \(x=1/2\), the formula is understood through the branch selected by the exact parametrization; the same limit results.

Consequently the normalized quartic remainder has the full cluster interval
\[
\boxed{
\operatorname{Clust}_{g\uparrow1}
\frac{1-\overline\rho(g)-\frac32(1-g)^2+A(1-g)^3}
{(1-g)^4}
=
\left[K_0,K_0+\frac12\right].
}
\tag{3}
\]
In particular, the endpoint has a universal third-order Peano expansion but no fourth-order Peano coefficient. Hence the boundary cannot admit a \(C^4\) extension through \(g=1\).

The two endpoint values in (3) correspond precisely to the two breakpoint families in the source parametrization: integer parameters \(\theta=N\) give \(K_0\), while the secondary junctions
\[
\theta_N^*=\frac{2N(N+1)}{2N+1}
=N+\frac{N}{2N+1}
\]
approach the coefficient \(K_0+1/2\). Thus the countably piecewise algebraic geometry first leaves an asymptotic fingerprint at order four.

## Proof

For \(\theta>1\), write \(N=\lfloor\theta\rfloor\), \(s=1/\theta\),
\[
L=\frac1{2N},\qquad R=\frac1{2(N+1)},
\]
and use the exact source formulas
\[
\ell=\begin{cases}
L,&s\ge L+R,\\
R,&s<L+R,
\end{cases}
\qquad
\delta=s-2\ell,
\qquad
p=1-2N(N+1)|\delta|,
\]
\[
m=\ell+N(N+1)\delta|\delta|,
\]
\[
q=\ell(2m-\ell)+\frac23N(N+1)|\delta|^3,
\qquad
c=\frac{\ell^2-s\ell-\ell p\delta}{2},
\]
\[
\alpha=\frac{1+\sqrt{1+2\theta^2c}}2,
\qquad
t=\frac1{\theta+\alpha},
\qquad
a=\alpha t,
\qquad
z=\theta t,
\]
\[
G=1-2a^2-z^2m,
\qquad
P=1-2a^3-\frac32z^3q.
\tag{4}
\]
The branch switch is at
\[
\theta_N^*=\frac{2N(N+1)}{2N+1},
\qquad
x_N^*=\theta_N^*-N=\frac{N}{2N+1}.
\tag{5}
\]
Hence a fixed phase \(x<1/2\) eventually uses \(\ell=L\), while a fixed \(x>1/2\) eventually uses \(\ell=R\).

Set \(\varepsilon=N^{-1}\) and \(\theta=N+x\). Direct Taylor expansion of (4) gives
\[
G=1-\frac12\varepsilon+B\varepsilon^2+C\varepsilon^3+O(\varepsilon^4),
\qquad
P=1-\frac38\varepsilon^2+E\varepsilon^3+F\varepsilon^4+O(\varepsilon^5).
\tag{6}
\]
On the \(L\)-branch,
\[
B_L=x^2-\frac38-\frac{\sqrt3}{4},
\]
\[
C_L=-2x^3+\left(\frac12-\frac{\sqrt3}{3}\right)x^2
+\left(1+\frac{2\sqrt3}{3}\right)x
+\frac{31}{32}+\frac{9\sqrt3}{16},
\]
\[
E_L=\frac32x^2-\frac14-\frac{3\sqrt3}{16},
\]
\[
F_L=-4x^3-\frac{7\sqrt3}{8}x^2
+\left(\frac32+\sqrt3\right)x
+\frac{165}{128}+\frac{3\sqrt3}{4}.
\tag{7}
\]
On the \(R\)-branch,
\[
B_R=-x^2+2x-\frac78-\frac{\sqrt3}{4},
\]
\[
C_R=2x^3+\left(-\frac52+\frac{\sqrt3}{3}\right)x^2
+\frac{55}{32}+\frac{35\sqrt3}{48},
\]
\[
E_R=-\frac32x^2+3x-1-\frac{3\sqrt3}{16},
\]
\[
F_R=4x^3+\left(-\frac92+\frac{7\sqrt3}{8}\right)x^2
+\left(-\frac32-\frac{3\sqrt3}{4}\right)x
+\frac{373}{128}+\frac{19\sqrt3}{16}.
\tag{8}
\]
The remainders are uniform on the corresponding compact phase intervals because the exact expressions are rational functions and a square root whose radicand stays uniformly away from zero for sufficiently large \(N\).

Now put \(y=1-G\) and \(r=1-P\). Reverting (6) through fourth order gives
\[
r=\frac32y^2+Q_3y^3+Q_4y^4+O(y^5).
\tag{9}
\]
For either branch, substitution of (7) or (8) gives the same cubic coefficient
\[
Q_3=-\frac{5+3\sqrt3}{2}=-A.
\tag{10}
\]
This proves (1).

At quartic order the cancellation stops. On the lower-half branch,
\[
Q_{4,L}(x)=K_0+16x^3-24x^4,
\tag{11}
\]
while on the upper-half branch,
\[
Q_{4,R}(x)=K_0+16(1-x)^3-24(1-x)^4.
\tag{12}
\]
Equations (11)--(12) prove (2).

The polynomial
\[
K(u)=K_0+16u^3-24u^4
\]
satisfies
\[
K'(u)=48u^2(1-2u)\ge0\qquad(0\le u\le1/2),
\]
so
\[
K([0,1/2])=[K_0,K_0+1/2].
\]
Every \(u\in[0,1/2]\) is realized by a fixed-phase subsequence. Conversely, every sequence \(\theta\to\infty\) has a subsequence whose fractional part converges, and the two branch formulas force every quartic-remainder limit into this same interval; at the moving switch (5), both branches converge to \(u=1/2\). This proves (3).

## Verification

`artifacts/verify_asymptotics.py` performs exact symbolic checks of the cubic cancellation and the two quartic formulas, and separately evaluates the exact parametrization numerically at several phases. The symbolic checks return zero residuals for both branches.

## Relation to prior work and originality boundary

Ansari, Rockel and Steinmaßl determine the exact rho--gamma region and give the parametrization (4). Their Remark 2.2 identifies the two accumulating breakpoint families and proves only
\[
\overline\rho(g)=1-\frac32(1-g)^2+O((1-g)^3).
\]
The present result is a higher-order analysis of their exact formulas: it identifies the universal cubic coefficient, the first phase-sensitive order, its explicit phase function, and the complete quartic cluster interval.

The auxiliary rho--footrule optimizer underlying (4) comes from Ansari and Rockel (2026), and earlier work studies exact regions and inequalities among other concordance measures. Searches by the exact constants, endpoint-regularity language, Taylor/asymptotic formulations, and synonymous rho--gamma boundary terminology did not locate the cubic coefficient or quartic phase law. To the best of our knowledge, (1)--(3) are not stated in the existing literature.

A residual originality risk is that the quartic law may be obtainable as an unrecorded specialization of higher-order calculations for the rho--footrule optimizer. The claim here is therefore limited to the explicit rho--gamma endpoint expansion and phase/cluster statements above; it does not claim novelty for the source parametrization or its transport optimizer.

## Limitations

The result concerns only the rho-maximal boundary near the comonotonic endpoint \((1,1)\). Central symmetry gives the corresponding reflected statement at \((-1,-1)\), but no higher-order analysis is claimed at the elementary/non-elementary junction \(g_*\). The phase law is asymptotic; it does not replace the exact finite-\(\theta\) algebraic formulas. No claim is made about statistical sampling distributions of empirical rho or gamma.

## References

1. J. Ansari, M. Rockel, S. Steinmaßl, *The exact region determined by Spearman's rho and Gini's gamma*, arXiv:2609.19890 (2026). https://arxiv.org/abs/2609.19890
2. J. Ansari, M. Rockel, *The exact Spearman rho-footrule region via optimal transport with applications to finite rankings, mixability, and Chatterjee's rank correlation*, arXiv:2608.20176 (2026). https://arxiv.org/abs/2608.20176
3. D. Kokol Bukovšek, T. Košir, B. Mojškerc, M. Omladič, *Spearman's footrule and Gini's gamma: Local bounds for bivariate copulas and the exact region with respect to Blomqvist's beta*, Journal of Computational and Applied Mathematics 390 (2021), 113385. https://doi.org/10.1016/j.cam.2021.113385
