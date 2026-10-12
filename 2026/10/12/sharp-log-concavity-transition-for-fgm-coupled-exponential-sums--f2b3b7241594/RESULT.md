# Sharp log-concavity transition for FGM-coupled exponential sums

## Finding
Let \(X,Y\) have exponential marginals of common rate \(\lambda>0\) and the Farlie–Gumbel–Morgenstern (FGM) survival copula
\[
\widehat C_\theta(u,v)=uv\{1+\theta(1-u)(1-v)\},\qquad -1\le\theta\le1.
\]
For \(S=X+Y\), there is a **sharp parameter threshold** \(\theta_*\in(0,1)\), specified by the elementary one-variable variational formula below, such that its density is log-concave **if and only if** \(-1\le\theta\le\theta_*\). For \(\theta>\theta_*\), the density has positive logarithmic curvature somewhere in the interior. The result holds for every \(\lambda>0\) without rescaling the threshold.

Set, for \(t>0\),
\[
L(t)=4t(t+1)e^{-t}-2,\qquad
Q(t)=-1+4(t^2-3t+4)e^{-t}-16e^{-2t},\qquad D(t)=L(t)^2+4Q(t).
\]
For \(t>1\), let
\[
r(t)=\begin{cases}
\displaystyle\frac{2}{L(t)+\sqrt{D(t)}}&\text{if }L(t)>0\text{ and }D(t)\ge0,\\
+\infty&\text{otherwise}.
\end{cases}
\qquad
\boxed{\theta_* = \inf_{t>1}r(t).}
\]
The infimum is attained, and no minimizer-uniqueness assertion is required. Numerical optimization of this *exact* formula gives \(\theta_*\approx0.860258273097\), attained near \(t\approx1.641844534256\); these decimals are diagnostics, not certified enclosures. A rigorous lower bound is
\[
\theta_*\ge\frac1{4\varphi(\varphi+1)e^{-\varphi}-2}>\frac12,
\qquad \varphi=\frac{1+\sqrt5}{2},
\]
and the explicit admissible test point \(t=\log5\) supplies the upper bound \(\theta_*\le r(\log5)<1\).

In particular, the legal FGM parameter \(\theta=1\) gives a transparent exact violation at \(s=(\log4)/\lambda\):
\[
\left.\frac{d^2}{ds^2}\log f_S(s)\right|_{s=(\log4)/\lambda,\,\theta=1}
=\lambda^2\frac{2(\log4)^2-2\log4-1}{9(\log4-1)^2}>0.
\]
The stronger log-concavity (ILR) property therefore separates from increasing failure rate (IFR), which is established for this same model throughout the FGM parameter range in Navarro and Pellerey (2021). Our theorem does not challenge their IFR conclusion.

## Assumptions and scope
Both marginals are exponential with exactly the same rate \(\lambda>0\). Their joint survival law is precisely \(\widehat C_\theta\) above, with \(\theta\in[-1,1]\). The joint density is a genuine probability density throughout this range, and the sum density is strictly positive for \(s>0\). Log-concavity means concavity of \(s\mapsto\log f_S(s)\) on the entire open half-line. The statement is a complete classification within this two-parameter model; it does not claim log-concavity for general FGM marginals or characterize other aging classes.

## Proof
**1. Exact sum density and curvature.** The joint density is
\[
f_{X,Y}(x,y)=\lambda^2e^{-\lambda(x+y)}
\{1+\theta(2e^{-\lambda x}-1)(2e^{-\lambda y}-1)\},\qquad x,y>0.
\]
Integrate over the segment \(x+y=s\) and put \(t=\lambda s\). A direct calculation gives
\[
f_S(s)=\lambda e^{-t}A_\theta(t),\quad
A_\theta(t)=t+\theta B(t),\quad
B(t)=t-4+4(t+1)e^{-t}.
\]
Here \(A_\theta(t)>0\) for \(t>0\), because it is the integral of the nonnegative joint-density factor; indeed this factor is strictly positive at interior points of the integration segment. Its derivatives satisfy
\[
B'(t)=1-4te^{-t},\qquad B''(t)=4(t-1)e^{-t}.
\]
Consequently, with \(F(t,\theta)=A_\theta(t)A_\theta''(t)-(A_\theta'(t))^2\),
\[
F(t,\theta)=-1+L(t)\theta+Q(t)\theta^2,
\qquad
\frac{d^2}{ds^2}\log f_S(s)=\lambda^2\frac{F(t,\theta)}{A_\theta(t)^2}.
\]
Thus log-concavity is equivalent to \(F(t,\theta)\le0\) for all \(t>0\).

**2. Every nonpositive dependence parameter is log-concave.** For \(-1\le\theta\le0\), write
\[
A_\theta(t)=a t+b C(t),\quad a=1+\theta\ge0,\quad b=-\theta\ge0,\quad C(t)=4\{1-(1+t)e^{-t}\}.
\]
Elementary differentiation yields, for every \(t>0\),
\[
tC''(t)-2C'(t)=-4t(t+1)e^{-t}<0,
\]
\[
C(t)C''(t)-(C'(t))^2=16\{(1-t)e^{-t}-e^{-2t}\}<0.
\]
The latter inequality follows from \((1-t)e^t<1\): it is immediate when \(t\ge1\), and on \((0,1)\) the left side decreases from one. Expansion gives
\[
F(t,\theta)=-a^2+ab\{tC''-2C'\}+b^2\{CC''-(C')^2\}<0.
\]
This includes the endpoint \(\theta=-1\).

**3. For positive dependence, curvature is negative up to \(t=1\).** When \(0\le\theta\le1\) and \(0<t\le1\), \(A_\theta''=4\theta(t-1)e^{-t}\le0\). Moreover \(A_\theta'>0\), because \(te^{-t}\le e^{-1}\) on this interval and \(1+\theta(1-4/e)\ge2-4/e>0\). Therefore \(F<0\) throughout this region.

**4. A single positive-parameter crossing at each remaining time.** For \(t>1\), we first show \(Q(t)<0\). On \([1,3]\), \(B''\ge0\), while \(B(1)=-3+8/e<0\) and \(B(3)=-1+16/e^3<0\). Convexity places \(B\) below its negative endpoint chord, so \(Q=BB''-(B')^2<0\). For \(t\ge3\), let \(P(t)=t^2-3t+4\). Since
\[
\frac{d}{dt}\{P(t)e^{-t}\}=-(t^2-5t+7)e^{-t}<0,
\]
and \(4P(3)e^{-3}=16e^{-3}<1\), we have \(Q(t)<-1+4P(t)e^{-t}<0\). The strictness at possible derivative-zero points follows from \(B<0\) and \(B''>0\) when \(1<t\le3\).

Also \(L(t)<2\) for every \(t>0\). Indeed \(e^t>t(t+1)\), because
\[
e^t-t(t+1)\ge 1-\frac{t^2}{2}+\frac{t^3}{6}\ge\frac13>0
\]
(the cubic has its minimum at \(t=2\) on \([0,\infty)\)). For a fixed \(t>1\), this implies
\[
\frac{d}{d\theta}\left\{\frac{F(t,\theta)}{\theta^2}\right\}
=\frac{2-L(t)\theta}{\theta^3}>0,\qquad 0<\theta\le1.
\]
The quadratic \(F=-1+L\theta+Q\theta^2\) can therefore change from negative to nonnegative at most once within \((0,1]\), never in the opposite direction. When its relevant positive root exists it is exactly \(r(t)=2/(L+\sqrt{L^2+4Q})\); otherwise the restriction \(\theta\le1\) produces no violation at that time.

**5. Existence and sharpness of the global transition.** The function \(L\) attains its global maximum \(L_{\max}=4\varphi(\varphi+1)e^{-\varphi}-2\) at \(\varphi=(1+\sqrt5)/2\), obtained from \(L'=4e^{-t}(1+t-t^2)\). Since \(Q<0\) for \(t>1\), we have \(F(t,\theta)<0\) for every \(0<\theta\le1/L_{\max}\). Thus \(\theta_*>0\).

At \(t_4=\log4\) and \(\theta=1\), direct substitution gives
\[
F(t_4,1)=2t_4^2-2t_4-1>0.
\]
For a purely rational check of strictness, the first six terms of \(\log2=\sum_{k\ge1}1/(k2^k)\) sum to \(1327/1920>11/16\), so \(t_4>11/8>(1+\sqrt3)/2\). Therefore \(r(t_4)<1\), and \(\theta_*<1\).

The infimum defining \(\theta_*\) is attained: any sequence with \(r(t_n)\to\theta_*<1\) remains away from \(t=1\) because \(F(1,1)<0\) and remains bounded because \(L(t)\to-2\) as \(t\to\infty\); a convergent subsequence gives a finite positive root at its limit. At a boundary where \(D=0\), the candidate root is \(2/L>1\), so the minimizing limit cannot disappear into such a boundary. Hence some \(t_*\in(1,\infty)\) satisfies \(r(t_*)=\theta_*\). The monotone crossing property in Step 4 now yields \(F(t,\theta)\le0\) at all times for \(0<\theta\le\theta_*\), including equality at \(t_*\) when \(\theta=\theta_*\). Conversely, for \(\theta_*<\theta\le1\), \(F(t_*,\theta)>0\). Together with Steps 2–3 this proves the exact if-and-only-if classification.

## Verification
The accompanying standalone script `verify.py` uses Python's standard library only. Running `python verify.py` reports 3,520 exact-rational evaluations of the derivative identities, 40 independently quadrature-integrated sum-density comparisons, elementary rational bounds proving the \(\theta=1\) counterexample, and additional finite grid/optimization diagnostics. These finite tests are consistency checks; Steps 1–5 above constitute the proof on the entire continuous parameter range. The numerical value of \(\theta_*\) is illustrative and is not claimed as a certified decimal enclosure.

## Relationship to prior work
Navarro and Pellerey (first published November 26, 2021), Example 2, derive the FGM exponential-sum survival law and rigorously establish IFR across \(-1\le\theta\le1\). Their discussion of Figure 3 additionally describes ILR as preserved for the plotted parameters, including \(\theta=1\), but presents no sharp ILR parameter classification. The explicit positive curvature above shows that the unrestricted graphical ILR interpretation does not hold. The established IFR result is logically weaker and is not contradicted.

Navarro and Sarabia (first published December 23, 2020) provide general copula-based sum representations and FGM risk examples. Only their abstract and accessible bibliographic material could be inspected; their complete article was not accessible. Navarro, Pellerey and Mulero (2022) consider a different time-transformed exponential dependence class and do not study this FGM sum log-curvature threshold. The classification here is an exact analysis of one natural dependent-sum family, not a general theorem about arbitrary copulas.

## Limitations
The threshold is specified by a one-dimensional infimum; uniqueness of its minimizing time and a machine-certified decimal interval are not established. The theorem assumes equal exponential marginal rates and a bivariate FGM survival copula. It does not characterize general exponential-rate pairs, all copulas, or multivariate sums. The 2020 related full text was inaccessible; an equivalent older result under different terminology cannot be ruled out. The finding has undergone self-review only, not independent audit or independent priority verification.

## References
1. J. Navarro and F. Pellerey, “Preservation of ILR and IFR aging classes in sums of dependent random variables,” *Applied Stochastic Models in Business and Industry* 38 (2022), 240–261. First published November 26, 2021. DOI: 10.1002/asmb.2657. https://onlinelibrary.wiley.com/doi/full/10.1002/asmb.2657
2. J. Navarro and J. M. Sarabia, “Copula representations for the sum of dependent risks: models and comparisons,” *Probability in the Engineering and Informational Sciences* 36 (2022), 320–340. First published December 23, 2020. DOI: 10.1017/S0269964820000649. https://www.cambridge.org/core/journals/probability-in-the-engineering-and-informational-sciences/article/copula-representations-for-the-sum-of-dependent-risks-models-and-comparisons/9E364F59A54ED607C5E3A6A3CC4B2A03
3. J. Navarro, F. Pellerey and J. Mulero, “On sums of dependent random lifetimes under the time-transformed exponential model,” *TEST* 31 (2022), 879–900. DOI: 10.1007/s11749-022-00805-2. https://link.springer.com/article/10.1007/s11749-022-00805-2
