# Fourth-order arithmetic micro-oscillation on the Spearman–Gini boundary

## Result

Let \(\overline\rho(g)\) be the greatest Spearman rho among bivariate copulas with Gini gamma equal to \(g\). Ansari, Rockel and Steinmaßl (arXiv:2609.19890v1) recently determined this boundary exactly and gave a parametrization
\[
(G(\theta),P(\theta))=(\gamma(C_\theta),\rho(C_\theta)),\qquad \theta\in[0,\infty],
\]
with \(P(\theta)=\overline\rho(G(\theta))\). Their non-elementary branch consists of countably many algebraic pieces accumulating at comonotonicity \((1,1)\).

Write
\[
x_\theta=1-G(\theta),\qquad y_\theta=1-P(\theta),\qquad
q_\theta=\operatorname{dist}(\theta,\mathbb Z)\in[0,1/2].
\]
Then, as \(\theta\to\infty\),
\[
\boxed{
 y_\theta
 =\frac32x_\theta^2
 -\frac{5+3\sqrt3}{2}x_\theta^3
 +\Psi(q_\theta)x_\theta^4
 +o(x_\theta^4),
}
\]
where
\[
\boxed{
\Psi(q)=\frac{78+45\sqrt3}{4}+16q^3-24q^4,
\qquad 0\le q\le\frac12.
}
\]
The remainder is uniform with respect to the fractional part of \(\theta\).

Consequently, with \(x=1-g\downarrow0\), the rho-maximal boundary has the universal cubic Peano expansion
\[
\boxed{
1-\overline\rho(1-x)
=\frac32x^2-\frac{5+3\sqrt3}{2}x^3+O(x^4).
}
\]
In particular,
\[
1-\overline\rho(g)\sim \frac32(1-g)^2\qquad(g\uparrow1).
\]
Thus Spearman rho approaches its comonotone value quadratically faster than Gini gamma along the sharp boundary.

The fourth-order coefficient does not converge. More precisely, the complete set of subsequential limits is
\[
\boxed{
\left\{
\lim \frac{1-\overline\rho(g)-\frac32(1-g)^2+\frac{5+3\sqrt3}{2}(1-g)^3}{(1-g)^4}
\right\}
=
\left[
\frac{78+45\sqrt3}{4},
\frac{80+45\sqrt3}{4}
\right].
}
\]
Every value in this interval occurs. Hence the endpoint admits a universal expansion through cubic order but no fourth-order Peano coefficient. The oscillation width is exactly \(1/2\).

## Proof

For \(\theta>1\), use the notation of arXiv:2609.19890v1:
\[
N=\lfloor\theta\rfloor,\quad s=\theta^{-1},\quad
L=(2N)^{-1},\quad R=(2N+2)^{-1},
\]
\[
\ell=\begin{cases}L,&s\ge L+R,\\R,&s<L+R,\end{cases}
\qquad \delta=s-2\ell,
\qquad p=1-2N(N+1)|\delta|,
\]
\[
m=\ell+N(N+1)\delta|\delta|,
\]
\[
q=\ell(2m-\ell)+\frac23N(N+1)|\delta|^3,
\]
\[
c=\frac{\ell^2-s\ell-\ell p\delta}{2},
\quad
\alpha=\frac{1+\sqrt{1+2\theta^2c}}2,
\quad
t=(\theta+\alpha)^{-1},
\quad a=\alpha t,
\quad z=\theta t.
\]
The exact boundary coordinates are
\[
G=1-2a^2-z^2m,
\qquad
P=1-2a^3-\frac32z^3q.
\]

Set \(h=N^{-1}\) and \(r=\theta-N\in[0,1)\). The branch switch is at
\[
r=\frac{N}{2N+1}=\frac12+O(h).
\]
Taylor expansion of the exact formulas gives, on either branch,
\[
x=\frac h2+a_2(r)h^2+a_3(r)h^3+O(h^4),
\]
\[
y=\frac38h^2+b_3(r)h^3+b_4(r)h^4+O(h^5),
\]
uniformly for \(r\in[0,1]\). Eliminating \(h\) yields
\[
y=\frac32x^2-\frac{5+3\sqrt3}{2}x^3+C_4(r)x^4+O(x^5).
\]
For \(0\le r\le1/2\),
\[
C_4(r)=\frac{78+45\sqrt3}{4}+16r^3-24r^4,
\]
while for \(1/2\le r<1\),
\[
C_4(r)=\frac{78+45\sqrt3}{4}+16(1-r)^3-24(1-r)^4.
\]
The two expressions agree at \(r=1/2\). The exact switch differs from \(1/2\) by only \(O(h)\); moreover the two polynomial expressions differ by a cubic multiple of \(2r-1\). Thus replacing the exact selector by \(q_\theta=\min(r,1-r)\) changes the displayed fourth-order coefficient by \(o(1)\), establishing the stated uniform expansion.

Finally,
\[
\Psi'(q)=48q^2(1-2q)\ge0\quad(0\le q\le1/2),
\]
so
\[
\Psi(0)=\frac{78+45\sqrt3}{4},\qquad
\Psi(1/2)=\frac{80+45\sqrt3}{4}.
\]
Choosing \(\theta=N+r\) with any fixed \(r\in[0,1]\) realizes the corresponding limit, proving the exact interval of fourth-order accumulation points.

## Scientific context and originality boundary

The exact rho–gamma region, its extremizing copulas, and formulas for \(G(\theta)\) and \(P(\theta)\) are due to Ansari, Rockel and Steinmaßl, arXiv:2609.19890v1. Their construction in turn uses the exact rho–footrule optimizer of Ansari and Rockel, arXiv:2608.20176v1. Earlier work studied local bounds and exact regions for Gini gamma with other concordance measures.

The claim here is restricted to the comonotone endpoint asymptotics extracted from the new exact parametrization: the sharp quadratic law, the universal cubic coefficient, the explicit arithmetic fourth-order phase \(\Psi(\operatorname{dist}(\theta,\mathbb Z))\), and the resulting nonexistence of a fourth-order Peano coefficient. Searches for these exact statements and coefficients did not locate prior coverage. To the best of our knowledge, they are new.

A residual originality risk is that asymptotic regularity of the auxiliary rho–footrule boundary may have been analyzed in terminology not captured by searches. No claim is made that the countably piecewise algebraic structure itself is new; that structure is part of the cited exact-region work.

## Limitations

The result is a local asymptotic statement at the comonotone endpoint of the rho-maximal boundary. It does not give a new global description of the attainable region, nor does it replace the optimal-transport proof of the exact boundary. The phase is expressed in the source parametrization \(\theta\); an intrinsic closed form for the phase solely in terms of \(g\) is not asserted. The argument relies on the exact formulas of arXiv:2609.19890v1.

## References

- J. Ansari, M. Rockel, S. Steinmaßl, *The exact region determined by Spearman's rho and Gini's gamma*, arXiv:2609.19890v1 (2026). https://arxiv.org/abs/2609.19890
- J. Ansari, M. Rockel, *The exact Spearman rho-footrule region via optimal transport with applications to finite rankings, mixability, and Chatterjee's rank correlation*, arXiv:2608.20176v1 (2026). https://arxiv.org/abs/2608.20176
- D. Kokol Bukovšek, T. Košir, B. Mojškerc, M. Omladič, *Spearman's footrule and Gini's gamma: Local bounds for bivariate copulas and the exact region with respect to Blomqvist's beta*, J. Comput. Appl. Math. 397 (2021), 113385. https://doi.org/10.1016/j.cam.2021.113385
