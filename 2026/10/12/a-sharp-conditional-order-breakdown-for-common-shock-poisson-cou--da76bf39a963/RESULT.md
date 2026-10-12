# A sharp conditional-order breakdown for common-shock Poisson counts

## Finding

**Theorem.** Fix an integer \(n\geq 2\) and real parameters \(a,b>0\). Let \(Y_1,\ldots,Y_n,Z\) be mutually independent with \(Y_i\sim\operatorname{Pois}(a)\) and \(Z\sim\operatorname{Pois}(b)\). Set
\[
 X_i=Y_i+Z,\qquad S_n=\sum_{i=1}^nX_i,
 \qquad Q_{n,s}=\mathcal L(X_1\mid S_n=s).
\]
The following statements hold.

1. The joint law of \((X_1,\ldots,X_n)\) is multivariate totally positive of order two (\(\mathrm{MTP}_2\)). Each marginal is \(\operatorname{Pois}(a+b)\), and every off-diagonal covariance equals \(b>0\).
2. For every distinct pair \(i,j\) and all integers \(0\leq s<t\), the conditional distributions \(\mathcal L(X_i\mid X_i+X_j=s)\) and \(\mathcal L(X_i\mid X_i+X_j=t)\) are ordered increasingly in **likelihood-ratio order**.
3. Nevertheless, for every \(n\geq 3\), the upper-tail comparison between adjacent full totals \(n-1\) and \(n\) has the exact transition
\[
 \Pr(X_1\geq2\mid S_n=n)\;\geq\;\Pr(X_1\geq2\mid S_n=n-1)
 \quad\Longleftrightarrow\quad b\leq b_{\mathrm{ST}}(n,a),
\]
where, writing \(q=1/n\),
\[
 r_n=1-(1-q)^{n-1}-(n-1)q(1-q)^{n-2}>0,
 \qquad \delta_n=(n-1)q^2(1-q)^{n-2}>0,
\]
\[
 b_{\mathrm{ST}}(n,a)=\frac{(na)^n}{n!}\frac{\delta_n}{r_n}.
\]
In particular, if \(b>b_{\mathrm{ST}}(n,a)\), the family \(\{Q_{n,s}:s\geq0\}\) is **not** nondecreasing in usual stochastic order, despite the \(\mathrm{MTP}_2\) and pairwise likelihood-ratio properties.
4. At the first dimension where the failure can occur, \(n=3\), both order comparisons at adjacent totals \(2\) and \(3\) have simple, distinct sharp frontiers:
\[
 Q_{3,2}\leq_{\mathrm{LR}}Q_{3,3}\quad\Longleftrightarrow\quad b\leq2a^3,
\]
\[
 Q_{3,2}\leq_{\mathrm{ST}}Q_{3,3}\quad\Longleftrightarrow\quad b\leq6a^3.
\]
Thus there is an interval \(2a^3<b\leq6a^3\) in which ordinary stochastic order survives but likelihood-ratio order does not; above \(6a^3\) even ordinary stochastic monotonicity fails.

## Assumptions and scope

All distributions are on the nonnegative integers. The parameters \(a\) and \(b\) are finite and strictly positive; no limiting or asymptotic assumptions are imposed. Likelihood-ratio order means that the probability ratio of the higher-total conditional law to the lower-total conditional law is nondecreasing on their common ordered support, equivalently that all corresponding cross-products have the appropriate sign. Usual stochastic order is equivalent here to comparing every upper tail. \(\mathrm{MTP}_2\) means that a joint mass function \(p\) satisfies
\[
 p(x)p(y)\leq p(x\wedge y)p(x\vee y)
 \quad\text{for all }x,y\in\mathbb Z_{\geq0}^n.
\]
The sharp thresholds in Part 4 concern **only** the stated comparison \(Q_{3,2}\) versus \(Q_{3,3}\). The theorem does not characterize full-total monotonicity at every pair of levels below either threshold. The general-dimensional sharp threshold in Part 3 concerns the single tail event \(\{X_1\geq2\}\) at levels \(n-1,n\), and is sufficient to disprove global monotonicity above the threshold.

## Proof

**Step 1: multivariate total positivity.** Define the Poisson mass sequence
\[
 u_a(k)=\begin{cases}e^{-a}a^k/k!,&k\geq0,\\0,&k<0.\end{cases}
\]
It is log-concave with interval support: \(u_a(k)^2\geq u_a(k-1)u_a(k+1)\). Hence the Toeplitz kernel \((z,x)\mapsto u_a(x-z)\) is totally positive of order two. The augmented joint mass function
\[
 \Pr(Z=z,X_1=x_1,\ldots,X_n=x_n)
 =\Pr(Z=z)\prod_{i=1}^n u_a(x_i-z)
\]
is a product of nonnegative \(\mathrm{MTP}_2\) factors in the coordinate vector \((z,x_1,\ldots,x_n)\), and therefore is \(\mathrm{MTP}_2\). Marginalizing over \(z\) preserves \(\mathrm{MTP}_2\) by the standard four-functions/total-positivity marginalization theorem (see Fallat et al., Proposition 3.4(ii)). This proves Part 1's first assertion. The remaining assertions follow immediately from independent Poisson summands:
\[
 X_i\sim\operatorname{Pois}(a+b),\qquad
 \operatorname{Cov}(X_i,X_j)=\operatorname{Var}(Z)=b\quad(i\ne j).
\]

**Step 2: the pair-sum likelihood-ratio property.** Because every pair has the same distribution, it suffices to study \((X_1,X_2)\). Its joint probability-generating expression for \((X_1,X_1+X_2)\) is
\[
 \mathbb E[u^{X_1}t^{X_1+X_2}]
 =e^{-2a-b}\exp(at)\exp(aut+but^2).
\]
For \(x\geq0\) and \(k\in\mathbb Z\), put
\[
 A_{x,k}=[t^k]\exp(at)(a+bt)^x,\quad A_{x,k}=0\text{ if }k<0.
\]
The unnormalized joint mass kernel \(g(x,s)\) of \((X_1,X_1+X_2)\) is
\[
 g(x,s)=\frac{A_{x,s-x}}{x!}\quad(s\geq x),\qquad g(x,s)=0\quad(s<x).
\]
For each fixed \(x\), the coefficient sequence \((A_{x,k})_{k\geq0}\) is log-concave: it is the convolution of the log-concave sequences \((a^k/k!)_{k\geq0}\) and \((\binom{x}{j}a^{x-j}b^j)_{0\leq j\leq x}\). Convolution preserves log-concavity for nonnegative sequences with interval support: their Toeplitz matrices have nonnegative minors of order two, and the product Toeplitz matrix of the convolution does as well by the Cauchy–Binet identity on finite truncations.

Fix \(s\geq x\), and abbreviate \(k=s-x\), \(A_j=A_{x,j}\). The relation \(A_{x+1,j}=aA_{x,j}+bA_{x,j-1}\) yields the adjacent minor
\[
 \begin{aligned}
 &g(x,s)g(x+1,s+1)-g(x,s+1)g(x+1,s)\\
 &=\frac{a(A_k^2-A_{k-1}A_{k+1})
       +b(A_kA_{k-1}-A_{k-2}A_{k+1})}{x!(x+1)!}\geq0.
 \end{aligned}
\]
The first bracket is nonnegative by log-concavity. The second is nonnegative by the monotone consecutive ratios of a positive log-concave sequence, with the boundary cases covered by the zero convention. Minors at \(s<x\) are nonnegative directly. Since the positive support is triangular \(\{(x,s):0\leq x\leq s\}\), adjacent nonnegative minors imply all cross-minors by chaining consecutive likelihood ratios on the positive region; when a lower-left cell vanishes, the desired determinant is trivially nonnegative. Thus \(g\) is \(\mathrm{TP}_2\) in \((x,s)\). Column normalization to obtain \(\mathcal L(X_1\mid X_1+X_2=s)\) preserves these minors, proving Part 2 for all totals.

**Step 3: the exact higher-dimensional threshold.** Put \(T_n=\sum_{i=1}^nY_i\sim\operatorname{Pois}(na)\), independently of \(Z\). Then \(S_n=T_n+nZ\). The condition \(S_n=n-1\) forces \(Z=0\) and \(T_n=n-1\); the Poisson splitting identity gives
\[
 Q_{n,n-1}=\operatorname{Bin}(n-1,1/n).
\]
When \(S_n=n\), the only possibilities are \((Z,T_n)=(0,n)\) and \((1,0)\). Their relative unnormalized weights are respectively \((na)^n/n!\) and \(b\). Define
\[
 A_n=\frac{(na)^n}{n!},\qquad w_n=\frac{A_n}{A_n+b}.
\]
Then exactly
\[
 Q_{n,n}=w_n\operatorname{Bin}(n,1/n)
 +(1-w_n)\delta_1.
\]
For \(n\geq3\), the preceding-level tail is
\[
 \Pr(X_1\geq2\mid S_n=n-1)=r_n.
\]
Using one additional Bernoulli trial, the tail of \(\operatorname{Bin}(n,1/n)\) is \(r_n+\delta_n\), with
\[
 \delta_n=\frac1n\Pr(\operatorname{Bin}(n-1,1/n)=1)
 =\frac{n-1}{n^2}(1-1/n)^{n-2}.
\]
Therefore
\[
 \Pr(X_1\geq2\mid S_n=n)=\frac{A_n}{A_n+b}(r_n+\delta_n),
\]
and direct rearrangement gives the claimed equivalence \(b\leq A_n\delta_n/r_n\). Positivity of \(r_n,\delta_n\) holds for every integer \(n\geq3\), so choosing any \(b\) above this explicit cutoff gives a strict failure of stochastic monotonicity.

**Step 4: two distinct sharp frontiers in three coordinates.** For \(n=3\), \(A_3=9a^3/2\) and \(w=w_3=A_3/(A_3+b)\). The conditional probability vectors, indexed by \(x=0,1,2,3\), are
\[
 Q_{3,2}=\left(\frac49,\frac49,\frac19,0\right),
 \qquad Q_{3,3}=\left(\frac{8w}{27},1-\frac{5w}{9},\frac{2w}{9},\frac{w}{27}\right).
\]
Every relevant upper-tail comparison is automatic except the tail beginning at \(2\). That comparison holds exactly when \(7w/27\geq1/9\), equivalently \(w\geq3/7\) and \(b\leq6a^3\). For likelihood-ratio order, the successive nonzero-support ratios of the second mass vector to the first are
\[
 \frac{2w}{3},\qquad\frac{9-5w}{4},\qquad 2w,
\]
followed by a positive mass at \(3\), where the first law has zero mass. The first ratio inequality always holds for \(0<w<1\); the second holds exactly when \(13w\geq9\), or \(b\leq2a^3\). This proves the exact frontiers. \(\square\)

## Verification

The standalone `VERIFY.py` uses only the Python standard library and exact rational arithmetic. Run `python VERIFY.py` with the file beside this document. It independently constructs the conditional laws by enumerating the latent common-shock count and using binomial splitting. The bounded verifier checks 28 exact trivariate threshold cases, 90 general-dimensional transition cases, 676 bivariate adjacent total-positivity minors, and 104,328 finite-lattice \(\mathrm{MTP}_2\) inequalities. Every assertion passed. These finite checks do **not** establish the universal theorem: Step 1 uses the multivariate \(\mathrm{MTP}_2\) marginalization theorem, Step 2 uses the log-concavity closure lemma and an exact adjacent-minor identity, and Steps 3–4 are finite symbolic calculations for arbitrary positive parameters.

## Relationship to prior work

Pellerey and Navarro (2021, published online) investigate monotonicity of dependent coordinates conditional on their sum, including sufficient log-concavity/total-positivity hypotheses (especially Section 3, Proposition 3.1), and discuss the difficulty of multivariate extensions. Their hypotheses concern the pair \((X_i,\sum_{j\ne i}X_j)\); merely knowing joint \(\mathrm{MTP}_2\) is not their assumption. The present result supplies a sharp discrete boundary case in which pairwise conditioning is monotone but full-total conditioning fails. Their nonmonotone examples do not give this Poisson common-shock \(\mathrm{MTP}_2\) example or the cutoffs. Schulz, Genest and Mesfioui (first online 2020; Section 2.4, Eq. 6) explicitly describe the classical multivariate common-shock Poisson model, but their displayed probabilities and estimation discussion do not provide these conditional-order cutoffs. Fallat et al. (2015 preprint; 2017 article) supply the general \(\mathrm{MTP}_2\) theory used in Step 1, not the counterexample. Ellis and Sijtsma (2023) analyze manifest monotonicity of a binary item given the *rest score* (the sum of the other items), not conditional ordering given a full total that includes the item itself. The classical log-concavity/TP2 convolution principle is used, not claimed as new.

## Limitations

The theorem treats strictly positive finite Poisson intensities and the equi-intensity common-shock family; it does not classify arbitrary latent-shock laws or heterogeneous idiosyncratic intensities. The sharp cutoffs concern specific adjacent levels, not a full phase diagram for all \(s<t\). Search-based novelty screening is not proof of first discovery, and prior equivalent formulations in older total-positivity or actuarial literature remain a residual bibliographic risk. The computational checks are bounded corroboration and cannot replace a universal analytic proof.

## References

1. F. Pellerey and J. Navarro, *Stochastic monotonicity of dependent variables given their sum*, TEST 31 (2022), 543–561; first public online 11 October 2021. DOI: https://doi.org/10.1007/s11749-021-00789-5 (Sections 2–4).
2. J. Schulz, C. Genest and M. Mesfioui, *A multivariate Poisson model based on comonotonic shocks*, International Statistical Review 89 (2021), 323–348; first online 19 October 2020. DOI: https://doi.org/10.1111/insr.12408 (Section 2.4 and Eq. 6).
3. J. L. Ellis and K. Sijtsma, *A Test to Distinguish Monotone Homogeneity from Monotone Multifactor Models*, Psychometrika 88 (2023), 387–412. DOI: https://doi.org/10.1007/s11336-023-09905-w (Definition 7, Appendix A).
4. S. Fallat, S. Lauritzen, K. Sadeghi, C. Uhler, N. Wermuth and P. Zwiernik, *Total positivity in Markov structures*, arXiv:1510.01290v2 (2016), Section 3, Proposition 3.4. https://arxiv.org/html/1510.01290v2 .
