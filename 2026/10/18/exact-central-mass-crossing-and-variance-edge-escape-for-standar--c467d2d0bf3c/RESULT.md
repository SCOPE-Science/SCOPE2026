# Exact central-mass crossing and variance-edge escape for standardized Student laws

## Finding

Let \(T_\nu\) be Student with \(\nu>2\) degrees of freedom, and put \(X_\nu=\sqrt{(\nu-2)/\nu}\,T_\nu\), so \(\operatorname{Var}(X_\nu)=1\). Let \(Z\sim N(0,1)\), and set
\[
D_\nu(r)=\Pr(|X_\nu|\le r)-\Pr(|Z|\le r),\qquad r\ge0.
\]
For every real \(\nu>2\), there is a **unique** radius \(R_\nu>0\) with \(D_\nu(R_\nu)=0\). Moreover,
\[
D_\nu(r)>0\quad(0<r<R_\nu),\qquad D_\nu(r)<0\quad(r>R_\nu).
\]
There are exactly two positive intersections \(a_\nu<b_\nu\) of the densities of \(X_\nu\) and \(Z\), and
\[
0<a_\nu<\sqrt3<b_\nu,\qquad a_\nu<R_\nu<b_\nu.
\] The crossover obeys the sharp boundary law
\[
\boxed{R_\nu^2=2\log\frac1{\nu-2}+\log\!\left(2\log\frac1{\nu-2}\right)+\log\frac8\pi+o(1)}
\qquad(\nu\downarrow2).
\]
Using the published local density expansion of Ouimet (2022), one additionally gets
\[
R_\nu=\sqrt3+\frac1{\sqrt3\,\nu}+O(\nu^{-2})\qquad(\nu\to\infty).
\]
The large-degree expansion is a consequence of the cited work and is not presented as an independent novelty claim.

## Assumptions and scope

All degrees \(\nu\) are real and strictly larger than two; no integer restriction is used. Let \(\phi(x)=(2\pi)^{-1/2}e^{-x^2/2}\). The density of the standardized Student variable is
\[
f_\nu(x)=\frac{\Gamma((\nu+1)/2)}{\sqrt{\pi(\nu-2)}\,\Gamma(\nu/2)}\left(1+\frac{x^2}{\nu-2}\right)^{-(\nu+1)/2},\qquad x\in\mathbb R.
\]
The crossover concerns symmetric interval probabilities, **not** stochastic domination on the whole real line. The right-hand limit at infinity of both central masses is one, so \(D_\nu(\infty)=0\).

## Proof

**1. Two and only two density intersections.** Set \(z=x^2\) and \(L_\nu(z)=\log(f_\nu(\sqrt z)/\phi(\sqrt z))\). An exact calculation gives
\[
L_\nu(z)=\log\frac{\sqrt2\,\Gamma((\nu+1)/2)}{\sqrt{\nu-2}\,\Gamma(\nu/2)}
+\frac z2-\frac{\nu+1}{2}\log\left(1+\frac z{\nu-2}\right),
\qquad L'_\nu(z)=\frac{z-3}{2(\nu-2+z)}.
\]
Thus \(L_\nu\) decreases strictly from zero to three and increases strictly afterward. For independent \(G\sim N(0,1)\) and \(Q\sim\chi^2_\nu\), the representation \(X_\nu=\sqrt{V}\,G\), where \(V=(\nu-2)/Q\), has \(\mathbb EV=1\) and nonconstant \(V\). Strict Jensen for \(v\mapsto v^{-1/2}\) yields
\[
\frac{f_\nu(0)}{\phi(0)}=\mathbb E[V^{-1/2}]>(\mathbb EV)^{-1/2}=1.
\]
Therefore \(L_\nu(0)>0\). Since both densities integrate to one, \(L_\nu(3)<0\): otherwise the exact monotonicity would imply \(f_\nu(x)\ge\phi(x)\) everywhere with strict inequality somewhere, contradicting total mass. Finally \(L_\nu(z)\to+\infty\) as \(z\to\infty\). The intermediate value theorem and monotonicity give precisely two positive density-crossing radii \(a_\nu<\sqrt3<b_\nu\); the difference \(f_\nu-\phi\) has sign \(+,-,+\) across the resulting intervals.

**2. Exactly one central-mass crossing.** By symmetry,
\[
D'_\nu(r)=2(f_\nu(r)-\phi(r)).
\]
Hence \(D_\nu\) increases strictly on \((0,a_\nu)\), decreases strictly on \((a_\nu,b_\nu)\), and increases strictly on \((b_\nu,\infty)\). It starts at zero, so \(D_\nu(a_\nu)>0\). The positive far-tail density difference and the fact that \(D_\nu(\infty)=0\) show
\[
D_\nu(b_\nu)=-2\int_{b_\nu}^{\infty}(f_\nu(u)-\phi(u))\,du<0.
\]
Strict decrease between the two turning points produces exactly one zero \(R_\nu\), and the derivative signs rule out any others.

**3. The sharp boundary law as \(\nu\downarrow2\).** Put \(\varepsilon=\nu-2\) and \(H=\log(1/\varepsilon)\). In the normal–inverse-chi-square representation, \(\sqrt{\varepsilon/Q}\,G\to0\) in probability as \(\nu\downarrow2\); the denominators \(Q\sim\chi^2_\nu\) are tight away from zero in probability. Therefore \(D_\nu(r)\to1-\Pr(|Z|\le r)>0\) for each fixed \(r>0\). By the just-proved sign rule, \(R_\nu\to\infty\).

Direct integration of the stated Student density gives, uniformly for \(2<\nu\le3\), \(x\to\infty\), and \(\varepsilon/x^2\to0\),
\[
\Pr(X_\nu>x)=A_\nu\varepsilon^{\nu/2}x^{-\nu}
\left(1+O\left(\frac\varepsilon{x^2}\right)\right),\quad
A_\nu=\frac{\Gamma((\nu+1)/2)}{\nu\sqrt\pi\,\Gamma(\nu/2)}\longrightarrow\frac14.
\]
The equality \(D_\nu(R_\nu)=0\) is exactly equality of the two *one-sided* tails. The normal Mills estimate
\[
\Pr(Z>x)=\frac{e^{-x^2/2}}{\sqrt{2\pi}\,x}\left(1+O(x^{-2})\right)
\]
then yields
\[
R_\nu^2=\nu H+2(\nu-1)\log R_\nu
+2\log\frac1{A_\nu\sqrt{2\pi}}+o(1).
\]
Since \(R_\nu\to\infty\), this equation implies \(R_\nu^2=O(H)\) (use \(\log R=o(R^2)\)), followed by \(R_\nu^2\sim2H\). In particular \(\log R_\nu=\frac12\log(2H)+o(1)\), while \((\nu-2)H\to0\). Substitution and \(A_\nu\to1/4\) give the claimed \(2H+\log(2H)+\log(8/\pi)+o(1)\) law, including the additive constant.

**4. Large-degree endpoint (dependent on existing literature).** Ouimet (2022, Lemma 1) expands the standardized Student-to-Gaussian density ratio for fixed \(r\) through order \(\nu^{-2}\). Writing \(H_j\) for the probabilists' Hermite polynomial, its coefficients are \(H_4/4\) at order \(\nu^{-1}\), and \(H_4+H_6/3+H_8/32\) at order \(\nu^{-2}\). Integration over \([-r,r]\), using \((\phi H_{j-1})'=-\phi H_j\), gives locally uniformly
\[
\frac{D_\nu(r)}{\phi(r)}=
\frac{r(3-r^2)}{2\nu}
-\frac{2}{\nu^2}\left(H_3(r)+\frac{H_5(r)}3+\frac{H_7(r)}{32}\right)+O(\nu^{-3}).
\]
At \(r=\sqrt3\), the expression in parentheses equals \(-\sqrt3/2\). The first-order term has a simple zero with derivative \(-3\). The unique crossing therefore lies near \(\sqrt3\) and has the stated expansion \(R_\nu=\sqrt3+1/(\sqrt3\nu)+O(\nu^{-2})\). The source already contains the expansion needed for this deduction.

## Verification

The standalone script `verification.py` reconstructs the normalized density ratio, locates both density intersections and the central-mass intersection for a range of real degrees, and checks the predicted sign diagram and the two boundary approximations. It also checks the Hermite decomposition at exact rational arguments. Execute with `python verification.py` using Python 3, SciPy and standard-library modules. The proof above, not numerical root finding, establishes the uniform all-degree and asymptotic statements.

## Relationship to prior work

Frédéric Ouimet, *Refined normal approximations for the Student distribution*, arXiv:2201.05950 (first made public January 16, 2022), studies local density-ratio and survival-function expansions for large degrees and normal quantile approximations. Its full text provides the large-degree expansion used in Step 4; that expansion is neither an all-degree sign-classification theorem nor an asymptotic theorem at the finite-variance boundary \(\nu=2\). The present result makes those additional claims for the same variance-matched family. Searches of related mathematical records identified no matching all-degree crossing plus variance-edge asymptotic, but non-discovery is not proof of novelty. A general scale-mixture comparison theorem, if it exists and applies, could subsume Step 2 without matching the sharp boundary law.

## Limitations

There is no assertion that \(R_\nu>\sqrt3\) for every degree. A stronger monotonicity law for \(\nu\mapsto R_\nu\) is not proved, and no explicit elementary closed form for \(R_\nu\) is given. The boundary law applies only after variance normalization and only to centered symmetric intervals. Numerical checks do not certify infinitely many degrees. Earlier equivalent statements outside inspected sources remain a priority risk.

## References

1. F. Ouimet (2022), *Refined normal approximations for the Student distribution*, arXiv:2201.05950, https://arxiv.org/html/2201.05950v2; first version January 16, 2022. Lemma 1, Theorems 1–2, and proofs inspected.
2. F. Ouimet (2022), *Refined normal approximations for the Student distribution*, Journal of Classical Analysis 20(1), 23–33; https://doi.org/10.7153/jca-2022-20-03. MSC2020 primary 62E20.
