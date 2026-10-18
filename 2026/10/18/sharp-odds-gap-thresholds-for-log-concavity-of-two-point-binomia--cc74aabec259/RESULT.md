# Sharp odds-gap thresholds for log-concavity of two-point binomial mixtures

## Finding

Let \(n\ge2\) be an integer, \(0<p<q<1\), and \(0<w<1\). Conditional on a random success probability taking value \(p\) with probability \(1-w\) and value \(q\) with probability \(w\), let \(Y\) be binomial with \(n\) trials. Thus
\[
 a_k=\Pr(Y=k)=\binom nk\left[(1-w)p^k(1-p)^{n-k}+wq^k(1-q)^{n-k}\right],\quad 0\le k\le n.
\]
Put \(r=q(1-p)/(p(1-q))>1\) and \(\Delta=r+r^{-1}-2>0\). The following two conditions are **sharp**: 

**Uniform-in-weight ultra-log-concavity:** \(a_k\) is ultra-log-concave for *every* mixing weight \(0<w<1\) if and only if
\[
 \boxed{\Delta\le\frac4{n-1}.}
\]
**Uniform-in-weight ordinary log-concavity:** \(a_k\) is log-concave for *every* mixing weight \(0<w<1\) if and only if
\[
 \boxed{\Delta\le\frac{4(n+1)}{\lfloor n^2/4\rfloor}.}
\]
When a condition fails, an interior weight violating the corresponding curvature inequality exists. Both bounds include equality. For each fixed weight, the sets of indices where either curvature condition fails are each empty or a *single consecutive block*.

Equivalently, writing \(h=\operatorname{logit}(q)-\operatorname{logit}(p)=\log r\), the sharp robust radii are \(h\le2\operatorname{arsinh}(1/\sqrt{n-1})\) for ultra-log-concavity and \(h\le2\operatorname{arsinh}(\sqrt{(n+1)/\lfloor n^2/4\rfloor})\) for ordinary log-concavity. These radii are asymptotic to \(2/\sqrt n\) and \(4/\sqrt n\), respectively.

## Assumptions and scope

The trial count is a fixed integer \(n\ge2\); the conditional success parameter has *exactly two* strictly interior values \(p<q\). Every component probability is positive on \(\{0,\ldots,n\}\). Ordinary log-concavity means \(a_k^2\ge a_{k-1}a_{k+1}\) for all \(1\le k\le n-1\). Ultra-log-concavity means \(k a_k^2\ge(k+1)a_{k-1}a_{k+1}\) for all such \(k\). The endpoint inequalities are automatic because the mass vanishes beyond the support.

For a fixed weight, define
\[
 t=\frac{w}{1-w}\left(\frac{1-q}{1-p}\right)^n>0,\qquad z_k=t r^k.
\]
The exact pointwise tests, valid for all the stated parameters, are
\[
 \begin{aligned}
 \text{ULC at }k&\iff\Delta(n-k)\frac{z_k}{(1+z_k)^2}\le1,\\
 \text{LC at }k&\iff\frac{\Delta k(n-k)}{n+1}\frac{z_k}{(1+z_k)^2}\le1.
 \end{aligned}
\]
These give a finite exact classification at each individual mixing weight, as well as the uniform-in-weight thresholds.

## Proof

Set \(u=p/(1-p)\), \(A=(1-w)(1-p)^n\), and \(B=w(1-q)^n\). Then \(r=[q/(1-q)]/u\), \(t=B/A\), and
\[
 a_k=\binom nk Au^k(1+tr^k).
\]
For \(1\le k\le n-1\), direct cancellation yields the **exact** ratio identity
\[
 \frac{a_{k-1}a_{k+1}}{a_k^2}
 =\frac{k(n-k)}{(k+1)(n-k+1)}
 \frac{(1+z_k/r)(1+r z_k)}{(1+z_k)^2}
 =\frac{k(n-k)}{(k+1)(n-k+1)}
 \left(1+\Delta\frac{z_k}{(1+z_k)^2}\right).
\]
Substitution into the definitions of LC and ULC proves the two pointwise tests. The elementary inequality \(z/(1+z)^2\le1/4\), with equality precisely at \(z=1\), proves sufficiency for *every* weight. For ULC the most restrictive index is \(k=1\), because \(n-k\) is largest there. For LC the most restrictive index maximizes \(k(n-k)\), whose exact maximum over the interior integer indices is \(\lfloor n^2/4\rfloor\). This establishes the stated numerical thresholds.

For necessity, at any fixed interior \(k\), \(z_k=t r^k\) ranges through all positive real numbers when \(w\) varies through \((0,1)\). In particular, choose \(t=r^{-k}\), or equivalently
\[
 w=\frac{r^{-k}((1-p)/(1-q))^n}{1+r^{-k}((1-p)/(1-q))^n},
\]
so that \(z_k=1\). Choosing \(k=1\) in the ULC case and a maximizing \(k\) in the LC case shows strict failure whenever its respective threshold is exceeded. At equality, the appropriate curvature inequality becomes equality at the indicated weight, proving sharpness including boundaries.

To prove the consecutiveness assertion, interpolate \(z_x=tr^x\) to real \(0<x<n\). The two left-hand sides of the pointwise tests are positive multiples of
\[
 F_{\mathrm U}(x)=\frac{(n-x)z_x}{(1+z_x)^2},\qquad
 F_{\mathrm L}(x)=\frac{x(n-x)z_x}{(1+z_x)^2}.
\]
With \(h=\log r>0\), their second logarithmic derivatives are respectively
\[
 (\log F_{\mathrm U})''(x)=-\frac1{(n-x)^2}-\frac{2h^2z_x}{(1+z_x)^2}<0
\]
and
\[
 (\log F_{\mathrm L})''(x)=-\frac1{x^2}-\frac1{(n-x)^2}-\frac{2h^2z_x}{(1+z_x)^2}<0.
\]
Thus each strict superlevel set is an interval. Intersecting that interval with the integer indices shows that curvature violations cannot form two disjoint bands. Finally, \(r+r^{-1}-2=4\sinh^2(h/2)\) gives the log-odds formulations and asymptotic radii.

## Verification

The exact finite certificate \(n=10\), \(p=1/3\), \(q=1/2\), \(w=524288/583337\) has \(r=2\), \(\Delta=1/2\), \(z_1=1\), and
\[
 \frac{a_1^2}{2a_0a_2}=\frac{80}{81}<1.
\]
Nevertheless \(\Delta=1/2<44/25\), so **every** mixture of these two binomials is ordinarily log-concave even though the indicated mixture fails ultra-log-concavity. Conversely, for \(n=5\), \(p=1/3\), and \(q=1/2\), the inequality \(1/2<4/(5-1)\) guarantees ultra-log-concavity for every mixing weight.

The standalone standard-library checker `verify.py` tests the exact rational ratio identities and curvature equivalences over 12,285 interior indices from 1,755 rational parameter configurations, in addition to the exact displayed witness. These computations are finite consistency tests; the proof above establishes the universal quantifiers.

A nontrivial two-point mixture has \(\operatorname{Var}(W)>0\), hence the exchangeable Bernoulli indicators have positive pairwise covariance. Thus the result gives explicit positively dependent count laws to which general ultra-log-concave concentration theorems apply. Such counts need not be Poisson-binomial: with \(\mu=\mathbb EW\), their variance is \(n\mu(1-\mu)+n(n-1)\operatorname{Var}(W)\), strictly greater than the largest variance possible for a sum of \(n\) independent Bernoulli indicators with the same mean.

## Relationship to prior work

Kella and Löpker (2022, arXiv:2202.10296, Section 6) define binomial mixing \(Y\mid W\sim\operatorname{Bin}(n,W)\), study admissibility, generalized mixing, thinning, and limits. Their theorems do not give sharp LC/ULC membership criteria for two-point mixing. Aravinda, Marsiglietti, and Melbourne (2021, arXiv:2104.05054) prove concentration for distributions *already* known to be ULC; the present criteria determine when that hypothesis holds for a family of dependent binomial counts.

Gross, Mansour, Tucker, and Wang (2014, arXiv:1407.6325, Section 2) give sufficient synchronicity criteria for LC of positive linear combinations. These do not supply the present necessary-and-sufficient optimal odds-gap threshold: for example, with \(n=10\), \(p=1/4\), \(q=1/2\), the pair is not synchronized (at \(k=5\) synchronicity would require the component odds ratio \(r=3\) to be at most the binomial coefficient ratio \(36/25\)), while \(\Delta=4/3<44/25\) proves LC for every weight. Xia and Lv (2024) classify LC of **compound** binomial sums, formed by random numbers of independent jumps, not mixtures of the binomial success probability. Badiella, del Castillo, and Puig (2023) study **fixed-sample order statistics**, not mixtures over a latent Bernoulli parameter.

## Limitations

The result treats two support points for the latent success probability and a fixed common number of trials. It does not classify beta-binomial or arbitrary continuous mixtures, mixtures with unequal trial counts, higher-order total positivity, or sharp concentration constants. The identified prior literature does not give the same thresholds, but an earlier formulation under different terminology cannot be excluded without independent priority review.

## References

- O. Kella and A. Löpker, *On Binomial Thinning and Mixing*, arXiv:2202.10296v1 (21 February 2022), Section 6; https://arxiv.org/abs/2202.10296.
- H. Aravinda, A. Marsiglietti, and J. Melbourne, *Concentration Inequalities for Ultra Log-Concave Distributions*, arXiv:2104.05054v1 (11 April 2021); https://arxiv.org/abs/2104.05054.
- J. L. Gross, T. Mansour, T. W. Tucker, and D. G. L. Wang, *Log-Concavity of Combinations of Sequences and Applications to Genus Distributions*, arXiv:1407.6325v1 (23 July 2014), Section 2; https://arxiv.org/abs/1407.6325.
- W. Xia and W. Lv, *Log-concavity and relative log-concave ordering of compound distributions*, *Probability in the Engineering and Informational Sciences* 38 (2024), 579–593; https://doi.org/10.1017/S0269964823000293.
- L. Badiella, J. del Castillo, and P. Puig, *Ultra log-concavity of discrete order statistics*, *Statistics & Probability Letters* 201 (2023), 109900; https://doi.org/10.1016/j.spl.2023.109900.
