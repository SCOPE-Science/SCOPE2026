# Exact extreme-order Kendall concordance for heterogeneous proportional hazards

## Finding

Let \(n\ge2\) independent continuous component lifetimes have proportional hazards
\(\Pr(X_i>x)=\exp[-\lambda_i H(x)]\), for arbitrary rates \(\lambda_i>0\) and a common continuous strictly increasing cumulative hazard \(H\) satisfying \(H(0)=0\) and \(H(x)\to\infty\). Put \(U=\min_i X_i\), \(V=\max_i X_i\), and \(\Lambda=\sum_i\lambda_i\). For every nonempty proper subset \(S\subsetneq\{1,\ldots,n\}\) define
\[
 r_S=\sum_{i\in S}\lambda_i,\qquad c_S=(-1)^{|S|+1}\frac{\Lambda-r_S}{\Lambda}.
\]
Then the population Kendall rank correlation of the two extreme order statistics has the **finite, baseline-free rational formula**
\[
\boxed{\displaystyle
\tau(U,V)=\sum_{\varnothing\ne S,T\subsetneq\{1,\ldots,n\}}
 c_Sc_T\frac{r_Sr_T}{r_S+r_T}
 \left(\frac{1}{\Lambda+r_S}+\frac{1}{\Lambda+r_T}\right).}
\tag{1}
\]
The coefficient representation involves at most \((2^n-2)^2\) terms; the signed coefficients arise from inclusion-exclusion. All denominators are strictly positive.

For exactly two components, with rates \(a,b>0\) and normalized squared contrast \(t=((a-b)/(a+b))^2\in[0,1)\), equation (1) reduces to
\[
\boxed{\displaystyle \tau(U,V)
=\frac{2ab(a^2+4ab+b^2)}{(a+b)^2(a+2b)(2a+b)}
=\frac{(1-t)(3-t)}{9-t}.}
\tag{2}
\]
Consequently a single population rank-concordance parameter identifies the unordered relative hazard ratio \(R=\max(a,b)/\min(a,b)\), without knowing the common baseline:
\[
\boxed{\displaystyle t=\frac{4-\tau-\sqrt{\tau^2+28\tau+4}}2,
\qquad R=\frac{1+\sqrt t}{1-\sqrt t}.}
\tag{3}
\]
Here \(0<\tau\le1/3\), with equality exactly for equal rates; \(\tau\downarrow0\) as the rate ratio diverges. The optimal quantitative sensitivity bounds are, whenever \(0\le t_1<t_2<1\),
\[
\frac14(t_2-t_1)<\tau(t_1)-\tau(t_2)<\frac{11}{27}(t_2-t_1).
\tag{4}
\]
Both constants are sharp as limiting derivatives, not as finite-interval equalities.

## Assumptions and scope

The \(X_i\) are independent, proper, absolutely continuous lifetimes with a common strictly increasing cumulative-hazard transform \(H\) and strictly positive finite rates. Their order statistics have continuous marginal distributions, so population Kendall's tau is the expectation of the sign product from two independent copies of the pair \((U,V)\), with no tie corrections. The two-component identification is of the **unordered ratio**, not of labels, absolute scale, or the baseline hazard. The formula does not apply to dependent component lifetimes, nonproportional hazards, or observations subject to censoring without separate adjustment. The class includes exponential and Weibull proportional-hazard families.

## Proof

**1. Reduction and the independent spacing.** The strictly increasing transformation \(Z_i=H(X_i)\) turns the independent lifetimes into exponentials of rates \(\lambda_i\), preserving minimum, maximum and Kendall's tau. Work in the exponential coordinates. Exponential racing gives \(M=\min_iZ_i\sim\operatorname{Exp}(\Lambda)\). Its index \(I\) has \(\Pr(I=i)=\lambda_i/\Lambda\), independently of \(M\). Given \(I=i\), exponential memorylessness says that the residual lives \(Z_j-M\), \(j\ne i\), are independent exponentials with the original rates \(\lambda_j\), independently of \(M\). Therefore \(G=\max_iZ_i-M\) is independent of \(M\), and the maximum equals \(M+G\).

**2. The spacing law.** For every \(x\ge0\), conditional on the winner \(i\),
\[
\Pr(G>x\mid I=i)=1-\prod_{j\ne i}(1-e^{-\lambda_j x}).
\]
Expanding the product and summing the winner weights yields
\[
\Pr(G>x)=\sum_{\varnothing\ne S\subsetneq[n]}c_S e^{-r_Sx},
\qquad f_G(x)=\sum_{\varnothing\ne S\subsetneq[n]}c_Sr_Se^{-r_Sx}.
\tag{5}
\]
Equation (5) is a genuine density even though individual terms can be signed, because it was obtained from a conditional probability identity.

**3. A rank-concordance transform.** Take independent copies \((M,G)\), \((M',G')\). The difference \(M-M'\) has centered Laplace density \(\Lambda e^{-\Lambda|z|}/2\) and is independent of \(G-G'\). For any fixed \(d=G-G'\), the two differences \(M-M'\) and \(M+G-M'-G'\) are discordant exactly when the former lies between \(-d\) and \(0\); this has probability \((1-e^{-\Lambda|d|})/2\). Since there are no ties, \(\tau=1-2\Pr(\text{discordance})\), hence
\[
\tau(M,M+G)=\mathbb E[e^{-\Lambda|G-G'|}].
\tag{6}
\]

**4. Finite exact evaluation.** For independent exponentials \(E_s\sim\operatorname{Exp}(s)\), \(E_t\sim\operatorname{Exp}(t)\), direct integration over \(E_s<E_t\) and \(E_s>E_t\) gives
\[
\mathbb E[e^{-\Lambda|E_s-E_t|}]
=\frac{st}{s+t}\left(\frac1{\Lambda+s}+\frac1{\Lambda+t}\right).
\tag{7}
\]
Substituting the finite density expansion (5) twice into (6) and integrating term by term using (7) proves (1). No convergence rearrangement is required because the sums are finite.

**5. Two-component inversion and sharpness.** For \(n=2\), the only proper nonempty subsets are singletons. Their residual-gap exponential weights are \(a/(a+b)\) at rate \(b\) and \(b/(a+b)\) at rate \(a\). Substitution into (1) and clearing positive factors gives the first equality (2). Elementary algebra with \(t=(a-b)^2/(a+b)^2\) gives the second. Differentiation yields
\[
\frac{d\tau}{dt}=-\frac{t^2-18t+33}{(9-t)^2}<0,
\qquad \frac{d^2\tau}{dt^2}=\frac{96}{(9-t)^3}>0
\quad(0\le t<1).
\tag{8}
\]
Thus the population concordance is strictly decreasing in squared contrast, and its range is \((0,1/3]\). Solving the quadratic \(\tau(9-t)=(1-t)(3-t)\) gives (3); the other algebraic root lies outside \([0,1)\). The derivative in (8) grows strictly from \(-11/27\) at \(t=0\) toward \(-1/4\) as \(t\uparrow1\). The mean-value theorem proves (4), while these endpoint derivatives establish optimality of both constants.

## Verification

The accompanying standalone `verify.py` uses Python standard-library exact fractions to evaluate (1). It checks the two-rate expression independently against competing-race mixing for all 144 pairs of integer rates from 1 through 12; it also checks invariance under rate interchange, common rate scaling, and the squared-contrast parametrization. For homogeneous samples of sizes 2 through 6 it reproduces the known \(\tau=1/(2n-1)\). It checks further heterogeneous vectors, fixed reference fractions and independent, fixed-seed Monte Carlo diagnostics. Run `python verify.py`; the expected terminal line starts `VERIFY_OK`. These finite checks are not a replacement for the proof above.

## Relationship to prior work

Dolati, Genest and Kochar (2008) derive the full heterogeneous extreme-order copula implicitly and obtain a concordance **upper bound** through an order comparison; their discussion §4.2 explicitly notes the difficulty of computing heterogeneous concordance. Kochar's February 16, 2022 preprint extends dependence ordering to intermediate order statistics under heterogeneous proportional hazards; its formulas for Kendall's tau concern the homogeneous comparison sample. Avérous, Genest and Kochar (2005), Fuchs and Schmidt (2018), and Navarro and Balakrishnan (2010) give rank-concordance calculations for identically distributed or exchangeable parent samples. Those results encompass the homogeneous check but do not state the heterogeneous finite subset-sum identity (1) or the two-rate inverse calibration (3). Formula (1) is a **quantitative evaluation within the previously characterized joint law**, not a new identification of the full copula or a replacement of the known concordance inequality.

## Limitations

The finite expression has exponentially many subsets and quadratic pair count; no numerical stability guarantee is made for floating-point evaluation with large \(n\) because signed terms can cancel. Exact fractions are practical only at modest sizes. The ratio identification requires the model assumptions and population concordance; no finite-sample estimator, asymptotic confidence interval, censored-data procedure, or claim of identifiability for three or more rate parameters from a single scalar is supplied. Although the searched primary literature did not reveal an equivalent explicit identity, older dependence and reliability formulations might contain one; publication priority has not been independently established.

## References

1. S. Kochar, "Dependence comparisons of order statistics in the proportional hazards model," arXiv:2202.07874v1 (first posted 2022-02-16), https://arxiv.org/html/2202.07874v1 .
2. A. Dolati, C. Genest, S. C. Kochar, "On the dependence between the extreme order statistics in the proportional hazards model," *Journal of Multivariate Analysis* 99 (2008), 777-786, doi:10.1016/j.jmva.2007.03.001 ; full author-posted manuscript https://web.pdx.edu/~kochar/Papers/New%20papers/Genest/JMVA-06-249-R1.pdf .
3. J. Avérous, C. Genest, S. C. Kochar, "On the dependence structure of order statistics," *Journal of Multivariate Analysis* 94 (2005), 159-171, doi:10.1016/j.jmva.2004.03.004 ; https://web.pdx.edu/~kochar/Papers/d_papers/JMVA2005.pdf .
4. S. Fuchs, K. D. Schmidt, "On Kendall's Tau for Order Statistics," arXiv:1808.01156v1 (2018), https://arxiv.org/pdf/1808.01156 .
5. S. Kochar, "Stochastic Comparisons of Order Statistics and Spacings: A Review," 2012, doi:10.5402/2012/839473 ; https://onlinelibrary.wiley.com/doi/10.5402/2012/839473 .
6. J. Navarro, N. Balakrishnan, "Study of some measures of dependence between order statistics and systems," *Journal of Multivariate Analysis* 101 (2010), 52-67, https://ideas.repec.org/a/eee/jmvana/v101y2010i1p52-67.html .
