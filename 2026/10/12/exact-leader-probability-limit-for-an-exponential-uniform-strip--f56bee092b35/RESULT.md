# Correct leader limit and sharp convergence rate for the exponential–uniform strip

## Finding

Let \(X\sim\operatorname{Exp}(1)\) and \(V\sim\operatorname{Unif}(0,1)\) be independent. For \(n\) independent vectors with law \((X,X+V)\), let \(a_n\) be the probability that one sampled vector is coordinatewise at least all the others. Then \(a_n\) is strictly decreasing, and
\[
a_n\downarrow L=\int_0^1\frac{dw}{e^w-w}=0.843078886983\ldots>\frac45,
\qquad \lim_{n\to\infty}(a_n-L)^{1/n}=e^{-1}.
\]
In particular the simulation suggestion of at least \(0.8\) in [1, §5.2] is correct for this model. The strip CDF printed there instead leads to a different limit below \(0.8\): it replaces a conditional exceedance probability that varies with the competitor's first coordinate by a constant.

## Proof

Let \(widetilde X,\widetilde V\) be an independent competitor with the same law. Write \(w=1-v\) for the nominated mark \(v\), fix its first coordinate \(x>0\), and let \(F(x,x+v)\) be the chance the competitor is below it in both coordinates. The chance of \(widetilde X>x\) is \(e^{-x}\). If instead \(widetilde X=x-d\) with \(0\le d\le\min(w,x)\), the chance of second-coordinate exceedance is
\[
\Pr\{\widetilde V>1-w+d\}=w-d;
\]
for \(d>w\) it is zero. Thus
\[
1-F(x,x+v)=e^{-x}\left[1+\int_0^{\min(w,x)}e^d(w-d)\,dd\right].
\]
Set \(t=e^{-x}\) and \(A(w)=e^w-w\). The resulting exceedance probability, as a function of \(t\), is
\[
S_w(t)=\begin{cases}
A(w)t,&0\le t\le e^{-w},\\
1+w+\log t-wt,&e^{-w}<t\le1.
\end{cases}
\]
In particular at \(x\ge w\) the tail multiplier is \(e^w-w\), not \(1+w(e^w-1)\) as obtained from the printed CDF.

Almost surely there is at most one leader because the first marginal is continuous. Conditioning on a nominated sample point and then summing over its index gives \(a_n=n\mathbb E[F(X,X+V)^{n-1}]\). The variables \(e^{-X}\) and \(w=1-V\) are independent uniforms on \((0,1)\). For \(0<w<1\), the function \(S_w\) increases from 0 to 1 with positive derivative, constant \(A(w)\) on its first branch and strictly decreasing on its second branch. At the junction the derivatives agree. Write \(z=S_w(t)\), let \(g_w(z)=(S_w^{-1})'(z)\), and put \(z_0(w)=1-w e^{-w}\), the junction value. The function \(g_w\) is constant \(1/A(w)\) on \([0,z_0(w)]\) and strictly increasing thereafter. Consequently
\[
a_n=\int_0^1\int_0^1 n(1-z)^{n-1}g_w(z)\,dz\,dw.
\]
The inner expression equals \(\mathbb E[g_w(1-U^{1/n})]\) for an auxiliary uniform \(U\) on \((0,1)\). Under this coupling \(1-U^{1/n}\) decreases strictly with \(n\); for each \(0<w<1\), it exceeds \(z_0(w)\) with positive probability for any finite \(n\). Thus the inner expression and \(a_n\) decrease strictly.

Subtract \(L=\int_0^1 A(w)^{-1}dw\) using \(\int_0^1n(1-z)^{n-1}dz=1\). The remainder is a strictly positive integral with integrand \(n(1-z)^{n-1}(g_w(z)-A(w)^{-1})\) supported on \(z>z_0(w)\). There \(1-z<w e^{-w}\le e^{-1}\), so \(a_n-L\le n e^{-(n-1)}\), since \(\int_0^1g_w(z)dz=1\). Conversely, for every \(0<\eta<e^{-1}\) choose \(w_0<1\) sufficiently close to 1 so that \(w_0 e^{-w_0}>e^{-1}-\eta\), and choose a nonempty closed rectangle with positive area around a point \((w_0,z)\) satisfying \(z_0(w_0)<z<1-e^{-1}+\eta\). The rectangle can be chosen entirely in that open region and within \((0,1)^2\). The continuous difference \(g_w(z)-A(w)^{-1}\) is positive there and has a positive minimum. The contribution is at least a positive constant times \(n(e^{-1}-\eta)^{n-1}\). Taking roots and then \(\eta\downarrow0\) proves the sharp rate.

Finally \(e^w-w\le1+(e-2)w^2\) for \(0\le w\le1\), by the exponential series. Convexity of \(y\mapsto 1/(1+(e-2)y)\) gives \(L\ge 3/(e+1)>4/5\) since \(e<11/4\). This comparison needs no quadrature.

## Relation to prior work and scope

The motivating paper [1, §5.2] studies this same strip, obtains a positive lower bound and reports simulations suggesting a limit of at least \(0.8\). It correctly expresses the CDF as a density integral but mis-evaluates that integral in its displayed closed form. The corrected limit also specializes the general concurrence formulas [2, Theorems 1–2]: after exponentiating the two coordinates and dividing the second by \(\mathbb E e^V=e-1\), the model is a standard Pareto scalar \(e^X\) times the bounded, unit-mean spectral vector \((1,e^V/(e-1))\). The Pareto tail establishes its max-domain of attraction by conditioning on this vector, and the inner expected maximum of the spectral ratios reduces to \(\mathbb E_{V'}\max(1,e^{V'-v})=e^w-w\). The finite-sample strict ordering and sharp geometric error rate here use both branches of the strip's actual CDF. The nonincrease and polynomial bias for max-stable inputs in [2, Proposition 3] concern a different hypothesis, not merely membership in a max-domain of attraction. The conclusion does not extend here to other mark laws or other marginal tail classes.

## References

1. A. M. Răducan, C. Z. Rădulescu, M. Rădulescu, and G. Zbăganu, “On the Probability of Finding Extremes in a Random Set,” *Mathematics* 10 (2022), 1623. DOI: 10.3390/math10101623.
2. C. Dombry, M. Ribatet, and S. Stoev, “Probabilities of concurrent extremes,” *Journal of the American Statistical Association* 113 (2018), 1565–1582. DOI: 10.1080/01621459.2017.1356321.
