# Convex Anderson–Darling response to the sample maximum, despite negative covariance

## Finding

Let \(n\ge1\) and let \(X_1,\ldots,X_n\) be independent observations from a fully specified continuous cumulative distribution function \(F_0\). Under the null, set \(U_i=F_0(X_i)\); these variables are independent uniform variables on \((0,1)\). Write \(F_n\) for their empirical distribution function, \(M_n=\max_iU_i\), and use the standard one-sample Anderson–Darling statistic
\[
 A_n^2=n\int_0^1\frac{(F_n(u)-u)^2}{u(1-u)}\,du.
\]
For every integer \(n\ge1\), the regular conditional mean \(g_n(t)=\mathbb E[A_n^2\mid M_n=t]\), for \(0<t<1\), is
\[
\boxed{
 g_n(t)=\frac{(n-1)[t+(1-t)\log(1-t)]+(n-1-nt)^2[-t-\log(1-t)]}{nt^2}+n[-1-\log t+t].
}
\]
This function is strictly convex on \((0,1)\), tends to \(+\infty\) at both endpoints, and therefore has **exactly one minimizer** there. Nevertheless, the unconditional association with the upper extreme is nonpositive:
\[
\boxed{\operatorname{Cov}(A_n^2,M_n)=\frac{2n-(n+1)H_n}{n(n+1)^2},\quad H_n=\sum_{j=1}^{n}\frac1j.}
\]
The covariance is zero for \(n=1\), strictly negative for every \(n\ge2\), and equals \(-[\log n+\gamma-2+o(1)]/n^2\) as \(n\to\infty\), where \(\gamma\) is Euler's constant.

## Assumptions and scope

The null distribution \(F_0\) is **fully specified** and continuous; no parameters are estimated from these data. Probability-integral transformation reduces the result to independent uniforms. Conditional means use the usual regular conditional law at \(M_n=t\), defined by the positive density \(nt^{n-1}\) on \((0,1)\). Neither a composite-null Anderson–Darling correction nor conditioning on an estimated parameter is included. The formulas hold for every positive integer \(n\), including \(n=1\); when \(n=1\), \(g_1(t)=-1-\log[t(1-t)]\).

## Proof

**Step 1: exact conditional mean.** Given \(M_n=t\), the remaining \(n-1\) points are independent uniforms on \((0,t)\). For \(0<u<t\), the empirical count is \(K_u\sim\operatorname{Binomial}(n-1,u/t)\); hence
\[
\mathbb E[(F_n(u)-u)^2\mid M_n=t]
=\frac{(n-1)u(t-u)}{n^2t^2}
 +\frac{u^2(n-1-nt)^2}{n^2t^2}.
\]
For \(t\le u<1\), \(F_n(u)=1\). Substitution in the defining integral gives the three elementary integrals
\[
 \int_0^t\frac{t-u}{1-u}\,du=t+(1-t)\log(1-t),\qquad
 \int_0^t\frac{u}{1-u}\,du=-t-\log(1-t),\qquad
 \int_t^1\frac{1-u}{u}\,du=-1-\log t+t.
\]
Their weighted sum is exactly the displayed expression for \(g_n(t)\). The same derivation is valid for \(n=1\), when the binomial part is empty.

**Step 2: strict convexity and a unique minimum.** For uniform order statistics \(U_{(1)}<\cdots<U_{(n)}\), integration over the empirical steps gives the exact, non-asymptotic log representation
\[
 A_n^2=-n-\frac1n\sum_{j=1}^n(2j-1)
 [\log U_{(j)}+\log(1-U_{(n+1-j)})].
\]
Given \(M_n=t\), put \(V_k=U_{(k)}/t\), with \(V_n=1\). For \(1\le k<n\), \(V_k\) is the \(k\)-th order statistic of \(n-1\) independent uniforms, independent of \(t\), with \(V_k\sim\operatorname{Beta}(k,n-k)\). Using \(\mathbb E\log V_k=H_{k-1}-H_{n-1}\), we get
\[
 g_n(t)=C_n-n\log t
 -\frac1n\sum_{k=1}^n(2n+1-2k)\mathbb E\log(1-tV_k),
\quad
 C_n=-n-\frac1n\sum_{j=1}^{n-1}(2j-1)(H_{j-1}-H_{n-1}).
\]
All weights \(2n+1-2k\) are positive. Differentiation on compact subintervals of \((0,1)\) is dominated, so
\[
 g_n''(t)=\frac n{t^2}+\frac1n\sum_{k=1}^n(2n+1-2k)
 \mathbb E\frac{V_k^2}{(1-tV_k)^2}>0.
\]
As \(t\downarrow0\), the term \(-n\log t\) diverges; as \(t\uparrow1\), the \(k=n\) term \(-\log(1-t)/n\) diverges, while the other beta-log expectations have finite endpoint limits. This proves exactly one interior minimizer for all \(n\ge1\).

**Step 3: exact covariance.** Let \(M=M_n\). The beta law \(M\sim\operatorname{Beta}(n,1)\) implies
\[
 \operatorname{Cov}(\log M,M)=\frac1{(n+1)^2}.
\]
For each \(1\le j\le n\), write \(U_{(j)}=MV_j\) with \(V_j\) independent of \(M\) (and \(V_n=1\)); thus
\[
 \operatorname{Cov}(\log U_{(j)},M)=\frac1{(n+1)^2}.
\]
On the other hand, conditional on \(U_{(j)}=u\), the \(n-j\) larger observations are independent uniforms on \((u,1)\), whence
\[
 \mathbb E[M\mid U_{(j)}=u]=1-\frac{1-u}{n-j+1}.
\]
Since \(1-U_{(j)}\sim\operatorname{Beta}(n+1-j,j)\) and for \(Y\sim\operatorname{Beta}(a,b)\) one has \(\operatorname{Cov}(Y,\log Y)=b/(a+b)^2\), it follows that
\[
 \operatorname{Cov}(\log(1-U_{(j)}),M)
 =-\frac{j}{(n-j+1)(n+1)^2}.
\]
Insert these two rank-by-rank covariances into the exact log representation:
\[
\begin{aligned}
 \operatorname{Cov}(A_n^2,M)
 &=-\frac1{n(n+1)^2}\sum_{j=1}^n(2j-1)\left(2-\frac{n+1}{j}\right)\\
 &=\frac{2n-(n+1)H_n}{n(n+1)^2}.
\end{aligned}
\]
For \(n=1\), the numerator vanishes. For \(n\ge2\), \(H_n>2n/(n+1)\): at \(n=2\) this is immediate, and the increment \(1/(n+1)\) of the left side exceeds the increment \(2/[(n+1)(n+2)]\) of the right side. The displayed covariance is therefore strictly negative. Finally, \(H_n=\log n+\gamma+o(1)\) gives the stated asymptotic. This completes the proof.

## Verification

Run `python3 checker.py` with a standard Python installation. It separately compares the conditional integral formula to a beta-order-statistic log-series calculation at 100 parameter pairs, tests 500 covariance identities with exact rational arithmetic, and compares conditional means with seeded simulations in 12 cases. The checker returns `VERIFY_OK` when these finite diagnostics pass. The analytic proof above, not the finite checks, establishes all \(n\ge1\) and all \(0<t<1\).

## Relationship to prior work

The Anderson–Darling statistic and its ordered-log formula are standard. Tolikas and Heravi (2008, Secs. 2–6) analyze critical values with **estimated** parameters for a three-parameter lognormal null. Stephens (1974, Sec. 11 and power analyses) decomposes the statistic into spectral components and studies its power; neither inspected development gives a maximum-conditioned regression or the displayed exact mixed moment. Lockhart (2012, Theorems 1–2 and Remark 6) studies **asymptotic** conditioning on complete sufficient statistics for parametric families; that paper explicitly excludes the Anderson–Darling endpoint weight from its main proof. None of those results supplies the present finite-sample conditional formula or implies the covariance from marginal statistics alone.

## Limitations

This is a fully specified null-distribution calculation; no statements about alternatives, fitted distributions, conditional test size, or independent certification are made. The minimizer is characterized as unique but not given in a closed elementary form. Targeted comparisons do not rule out a previously published joint order-statistic generating function or an unindexed mixed-moment identity under another notation. Finite numerical checks are diagnostics, not an infinite proof.

## References

1. K. Tolikas and S. Heravi (2008), *The Anderson–Darling Goodness-of-Fit Test Statistic for the Three-Parameter Lognormal Distribution*, Communications in Statistics—Theory and Methods 37(19), 3135–3143. DOI: 10.1080/03610920802101571. First online 2008-08-15; reported primary MSC: 62G10 and 62G20.
2. M. A. Stephens (1974), *Components of goodness-of-fit statistics*, Annales de l'Institut Henri Poincaré, Section B 10(1), 37–54. Full text: https://www.numdam.org/item/AIHPB_1974__10_1_37_0.pdf .
3. R. A. Lockhart (2012), *Conditional limit laws for goodness-of-fit tests*, Bernoulli 18(3), 857–882. arXiv:1207.5967, https://arxiv.org/pdf/1207.5967 .
4. T. W. Anderson and D. A. Darling (1954), *A Test of Goodness of Fit*, J. Amer. Statist. Assoc. 49(268), 765–769. DOI: 10.1080/01621459.1954.10501232.
