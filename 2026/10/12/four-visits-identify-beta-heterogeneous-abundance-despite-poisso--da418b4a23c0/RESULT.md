# Four visits identify beta-heterogeneous abundance despite Poisson false detections

## Finding

A closed, unmarked animal population observed by repeated site-level counts can be structurally identifiable even when both individual detectability and false-positive counts are unknown, but **four visits are sharp** in the following precise model. Suppose the site abundance is Poisson with unknown mean \(\mu>0\), individual persistent detection propensities are independent \(\operatorname{Beta}(\alpha,\beta)\) with \(\alpha,\beta>0\), and every visit independently adds an unobserved Poisson false-positive count with unknown mean \(\xi\geq0\). Given the exact joint population law of the unlabeled counts at \(T\) visits, all four parameters \((\mu,\alpha,\beta,\xi)\) are uniquely determined if \(T\geq4\). For \(T\leq3\), every interior parameter choice with \(\xi>0\) has arbitrarily close observationally equivalent alternatives. If zero background contamination \(\xi=0\) is externally known, three visits, rather than four, are necessary and sufficient.

More explicitly, let \(c_r\) be the joint cumulant of the counts on any \(r\) **distinct** visits, with \(c_1\) the mean count. For four visits put \(r=c_3/c_2\), \(s=c_4/c_3\). Then

\[
0<r<s<\frac{3r}{r+2}<1,\qquad
S=\frac{1-3s+2r}{s-r},\qquad
\alpha=r(S+2)-2,\qquad\beta=S-\alpha,
\]
\[
\mu=\frac{c_2S(S+1)}{\alpha(\alpha+1)},\qquad
\xi=c_1-\frac{c_2(S+1)}{\alpha+1}.
\]

The possible quadruples \((c_1,c_2,c_3,c_4)\) are characterized exactly by \(c_2>0\), the strict ratio inequalities above, and \(\xi\geq0\) calculated by the displayed formula. The characterization describes cross-cumulants, not arbitrary four-dimensional count laws; the full law must also have the compound-Poisson form stipulated below.

An exact nonidentifiability witness for three visits is

\[
(\mu,\alpha,\beta,\xi)=(10,2,3,2)
\quad\text{and}\quad
\left(\frac{686}{75},\frac{18}{7},\frac{24}{7},\frac{52}{25}\right).
\]

Both yield \((c_1,c_2,c_3)=(6,2,8/7)\), and therefore **identical entire joint three-visit distributions**. Four visits separate them: their fourth cross-cumulants are respectively \(5/7=105/147\) and \(104/147\).

## Assumptions and scope

At each independent sampling site let \(N\sim\operatorname{Poisson}(\mu)\). Conditional on \(N\), draw independent \(Q_i\sim\operatorname{Beta}(\alpha,\beta)\), once per individual and persistently across the \(T\) survey occasions. Conditional on the propensities, individual detections \(Z_{it}\sim\operatorname{Bernoulli}(Q_i)\) are independent across individuals and visits. Independent background counts \(B_t\sim\operatorname{Poisson}(\xi)\) are also independent of everything else. Only \(Y_t=\sum_{i=1}^N Z_{it}+B_t\) is recorded; no animal identities or false-positive labels are available. The population stays closed, all visits use the same protocol, and sites are independent copies of this model. The known distributional family and exact population law are **structural** assumptions, not claims about a finite dataset.

For \(r\) distinct visit indices define
\[
c_r=\left.\frac{\partial^r}{\partial z_1\cdots\partial z_r}
\log\mathbb E\!\left[\prod_{t=1}^{T}z_t^{Y_t}\right]\right|_{z_1=\cdots=z_T=1}.
\]
These equal the ordinary joint cumulants on distinct visits. In particular \(c_2\) is between-visit covariance; \(c_3\) is the three-visit centered-product mean; and \(c_4\) is the four-visit centered-product mean minus the three products of pair covariances.

## Proof

**1. Compound-Poisson identity.** Write \(u_t=z_t-1\). Conditioning on the Poisson number of individuals and on their independent random propensities gives the **exact**, finite multivariate generating-function identity
\[
\log \mathbb E\prod_{t=1}^{T}z_t^{Y_t}
=\xi\sum_{t=1}^{T}u_t+
\mu\left(\mathbb E_Q\prod_{t=1}^{T}(1+Q u_t)-1\right)
=\sum_{\varnothing\ne A\subseteq\{1,\ldots,T\}}c_{|A|}\prod_{t\in A}u_t.
\]
Here the coefficients necessarily satisfy
\[
c_1=\xi+\mu\frac{\alpha}{\alpha+\beta},\qquad
c_j=\mu\frac{(\alpha)_j}{(\alpha+\beta)_j}\quad(2\leq j\leq T),
\]
where \((x)_j=x(x+1)\cdots(x+j-1)\) is the rising factorial. Thus the **entire** \(T\)-visit distribution is determined by exactly the available \(T\) coefficients \(c_1,\ldots,c_T\). Conversely the law recovers those coefficients as its generating-function derivatives.

**2. Recovery from four visits.** Set \(S=\alpha+\beta\). From the displayed moments,
\[
r=\frac{\alpha+2}{S+2},\qquad s=\frac{\alpha+3}{S+3}.
\]
Their difference is \(s-r=\beta/((S+2)(S+3))>0\); direct subtraction also yields
\[
\frac{3r}{r+2}-s
=\frac{\alpha\beta}{(S+3)(3\alpha+2\beta+6)}>0.
\]
Hence the stated inequalities hold. Solving these two linear-fractional equations gives the unique displayed \(S\) and \(\alpha\), followed by \(\beta\). The second cross-cumulant gives \(\mu\); the first then gives \(\xi\). This proves global injectivity for every \(T\geq4\). Conversely, if positive \(c_2\), the ratio inequalities, and nonnegative recovered \(\xi\) hold, those formulas give \(\alpha,\beta,\mu>0\) and reproduce the four cumulants, proving exact feasibility.

**3. Sharp failure at three visits.** Fix any interior parameters with \(\xi>0\) and \(T=3\). Their coefficients determine \(r=c_3/c_2=(\alpha+2)/(S+2)\). Vary \(S\) in a sufficiently small open interval about its original value, set \(\alpha(S)=r(S+2)-2\), \(\beta(S)=S-\alpha(S)\), \(\mu(S)=c_2S(S+1)/(\alpha(S)(\alpha(S)+1))\), and \(\xi(S)=c_1-\mu(S)\alpha(S)/S\). All parameters remain admissible by continuity and all three coefficients remain unchanged. Step 1 proves equality of the entire joint law, not just of three moments. Its marginals give failure for \(T<3\). The exact rational witness in the Finding supplies a separate explicit certificate and its unequal fourth cumulants prove that four visits genuinely distinguish the two models.

**4. Zero known background.** If \(\xi\equiv0\) is known, put \(a=c_2/c_1=(\alpha+1)/(S+1)\), \(b=c_3/c_2=(\alpha+2)/(S+2)\). For positive shapes \(a<b\), and the inverse \(S=(1-2b+a)/(b-a)\), \(\alpha=a(S+1)-1\), \(\beta=S-\alpha\), \(\mu=c_1S/\alpha\) is unique. With two visits only \(c_1,c_2\) are available and varying \(S\) in a neighborhood of its true value retains both while changing the parameters. Three visits are therefore sharp in this externally calibrated zero-background submodel.

## Verification

Run `python3 verify.py` from the extracted package. The standalone Python program uses exact rational arithmetic and no third-party dependencies. It checks five positive parameter tuples against the four-visit inverses, 50 independent Poisson-mark identities, six explicit nonidentifiable three-visit profiles, exact equality of all three-visit Poisson-mark intensities for the displayed pair, and the exact fourth-cumulant difference \(1/147\). These calculations corroborate the displayed identities and witness but are **not** a substitute for the general analytical argument in the Proof.

## Relationship to prior work

Royle's 2004 Poisson \(N\)-mixture model introduced unmarked spatially replicated counts with imperfect detection but used common individual detection probability and did not incorporate unlabelled Poisson false-positive counts. Dennis, Morgan and Ridout (2015) explicitly identified the multivariate-Poisson splitting of that conventional model; this known decomposition is used here, not claimed new. Dorazio and Royle (2003) studied beta-distributed individual capture heterogeneity in identity-resolved capture–recapture work; the exact anonymous-count/Poisson-background sharp four-visit boundary is distinct from the result visible in its abstract. Clement, Royle and Mixan (2022) treat misclassified acoustic detections with Poisson observation intensities, including an exogenous-background extension; their count-generating mechanism and goal differ. The contribution assessed here is the **joint** sharp 3-versus-4 identifiability threshold, an explicit indistinguishable pair of complete count laws, and an exact region of admissible cross-cumulants for persistent individual beta heterogeneity and exogenous Poisson counts. A general result on identifiability of multivariate compound-Poisson beta-thinning models may still imply the theorem and is a residual priority risk.

## Limitations

The result is structural, not a finite-sample guarantee: estimating third and fourth cross-cumulants may be unstable in sparse field data. It requires Poisson abundance, independently Poisson false counts of homogeneous intensity, a correctly specified beta distribution of **persistent per-individual** detection probabilities, independent conditional detections, closure, and at least four comparable visits. It does not cover contamination correlated across visits, a point mass of permanently undetectable individuals, random detection propensities redrawn each visit, negative-binomial abundance, or visit-specific covariates. The unrestricted nonparametric distribution of individual detectability is not identified from finitely many moments by this theorem.

## References

1. Dorazio, R. M. and Royle, J. A. (2003). Mixture models for estimating the size of a closed population when capture rates vary among individuals. *Biometrics* 59, 351–364. DOI: 10.1111/1541-0420.00042. First publicly dated 2003-06-11. https://doi.org/10.1111/1541-0420.00042
2. Royle, J. A. (2004). N-Mixture Models for Estimating Population Size from Spatially Replicated Counts. *Biometrics* 60, 108–115. DOI: 10.1111/j.0006-341X.2004.00142.x. https://webhome.auburn.edu/~grandjb/wildpop/readings/Occupancy/Royle_2004_Nmixture_models.pdf
3. Dennis, E. B., Morgan, B. J. T. and Ridout, M. S. (2015). Computational aspects of N-mixture models. *Biometrics* 71, 237–246. DOI: 10.1111/biom.12246. https://doi.org/10.1111/biom.12246
4. Veech, J. A., Ott, J. R. and Troy, J. R. (2016). Intrinsic heterogeneity in detection probability and its effect on N-mixture models. *Methods in Ecology and Evolution*. DOI: 10.1111/2041-210X.12566. https://doi.org/10.1111/2041-210X.12566
5. Clement, M. J., Royle, J. A. and Mixan, R. J. (2022). Estimating occupancy from autonomous recording unit data in the presence of misclassifications and detection heterogeneity. *Methods in Ecology and Evolution* 13, 1719–1729. DOI: 10.1111/2041-210X.13895. https://doi.org/10.1111/2041-210X.13895
