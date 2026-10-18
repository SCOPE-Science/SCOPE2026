# A sharp correlation threshold for submodular outbreak-overload protection on stars

## Finding

For every integer \(d\ge2\), let an infected index case expose \(d\) susceptible individuals once. A single unobserved index-case infectiousness \(P\) is sampled from \(\mathrm{Beta}(\alpha,\beta)\), where \(\alpha,\beta>0\). Conditional on \(P\), transmission to distinct unvaccinated individuals is independent with success probability \(P\). Vaccinated individuals cannot be infected and do not change \(P\). For a subset \(S\) vaccinated before exposure, write \(X_S\) for the number of infections among the remaining \(d-|S|\) individuals, and fix an integer overload threshold \(1\le r\le d\). Define

\[
 B(S)=\Pr(X_{\varnothing}\ge r)-\Pr(X_S\ge r).
\]

Then \(B\) is nonnegative, normalized, and increasing. The following is a **necessary-and-sufficient classification of submodularity on the entire vaccination powerset**:

* If \(r=1\), \(B\) is never submodular.
* If \(r=d\), \(B\) is always submodular.
* If \(2\le r\le d-1\), \(B\) is submodular if and only if

\[
 (r-1)\beta-(d-r)\alpha\ge d-1. \tag{1}
\]

Equivalently, if \(\mu=\alpha/(\alpha+\beta)\) denotes the marginal infection probability and \(\rho=1/(\alpha+\beta+1)\) the positive pairwise correlation of distinct infection indicators, then condition (1) is

\[
 \mu+\frac{\rho}{1-\rho}\le\frac{r-1}{d-1}. \tag{2}
\]

In particular, for \(d=5\), \(r=3\), and fixed \(\mu=1/4\), the pairs \((\alpha,\beta)=(5/4,15/4),(1,3),(1/2,3/2)\) produce correlations \(1/6,1/5,1/3\), respectively. The interaction between vaccinating two distinct individuals from the empty set equals, respectively, \(-195/57344,0,3/256\). Thus diminishing returns fails in the last case, even though the expected number of transmissions prevented, \(\mu|S|\), is identical for all three cases.

## Assumptions and scope

This is a one-generation, star-shaped contact network with exactly one infected central case. It is not a final-size theorem for a multi-generation epidemic. Transmission indicators are exchangeable, conditionally independent given a common \(P\), and positively correlated after integrating over \(P\). Vaccination is perfect, pre-exposure, and directed only at leaves. A vaccinated leaf has zero secondary-infection probability. The overload event always uses the fixed original threshold \(r\), not a threshold recalculated after vaccination.

A set function \(B\) is submodular when \(B(S\cup\{i,j\})-B(S\cup\{i\})-B(S\cup\{j\})+B(S)\le0\) for all distinct unvaccinated \(i,j\) and all \(S\) excluding them. The parameters \(\alpha,\beta\) can be any strictly positive real numbers. The exact common-infectiousness model is part of the theorem; no assertion is made for arbitrary dependence or heterogeneous individuals.

## Proof

Write \((z)_k=z(z+1)\cdots(z+k-1)\) for \(k\ge1\), with \((z)_0=1\). Beta integration yields the exact beta-binomial law

\[
 \Pr(X_S=k)=\binom{m}{k}\frac{(\alpha)_k(\beta)_{m-k}}{(\alpha+\beta)_m},\qquad m=d-|S|,\quad 0\le k\le m.
\]

To evaluate a discrete second difference, fix \(S\) and two further leaves \(i,j\), and let \(n=d-|S|-2\). Given \(P=p\), let \(Y\sim\mathrm{Bin}(n,p)\) count infections among the remaining \(n\) leaves. Exposing or vaccinating the two distinguished leaves and conditioning on their infection outcomes gives

\[
 \Delta_{i,j}B(S):=B(S\cup\{i,j\})-B(S\cup\{i\})-B(S\cup\{j\})+B(S)
 =-\mathbb E\!\left[P^2\bigl(\Pr(Y=r-2\mid P)-\Pr(Y=r-1\mid P)\bigr)\right].\tag{3}
\]

Here out-of-range binomial probabilities are zero. Put \(A_n=\mathbb E[P^2\Pr(Y=r-2\mid P)]\) and \(C_n=\mathbb E[P^2\Pr(Y=r-1\mid P)]\). For \(n\ge r-1\), direct Beta integration gives

\[
 A_n=\binom{n}{r-2}\frac{(\alpha)_r(\beta)_{n-r+2}}{(\alpha+\beta)_{n+2}},\qquad
 C_n=\binom{n}{r-1}\frac{(\alpha)_{r+1}(\beta)_{n-r+1}}{(\alpha+\beta)_{n+2}}.
\]

All factors are strictly positive in this range; consequently

\[
 \frac{C_n}{A_n}=\frac{n-r+2}{r-1}\frac{\alpha+r}{\beta+n-r+1}.\tag{4}
\]

For \(2\le r\le d-1\), equations (3)–(4) show that \(\Delta_{i,j}B(S)\le0\) precisely when

\[
 L(n):=(r-1)(\beta+n-r+1)-(n-r+2)(\alpha+r)\ge0, \qquad n\ge r-1.\tag{5}
\]

The affine function \(L(n)\) is strictly decreasing, with slope \(-\alpha-1\). Hence the worst case across all \(S\) is the largest available \(n=d-2\), attained when \(S=\varnothing\). Its condition simplifies to \(L(d-2)=(r-1)\beta-(d-r)\alpha-(d-1)\ge0\), giving (1). When \(n=r-2\), \(C_n=0<A_n\), so (3) is strictly negative; when \(n<r-2\), both terms vanish. Thus no overlooked smaller subset violates the criterion. Conversely, if (1) fails, choosing \(S=\varnothing\) gives a strictly positive discrete second difference.

When \(r=1\), equation (3) has the first probability identically zero, while the second is strictly positive for \(n\ge0\), so every available pair violates submodularity. When \(r=d\), equation (3) has \(C_n=0\) for all \(0\le n\le d-2\) and \(A_n\ge0\), proving submodularity. Monotonicity follows by coupling the same infection draws before and after vaccination.

Finally, \(\mathbb E[P]=\mu\) and \(\mathrm{Var}(P)/[\mu(1-\mu)]=1/(\alpha+\beta+1)=\rho\). Rewriting (1) gives (2). The fixed-mean examples follow from exact beta-binomial fractions and are reproduced independently by the verification program.

## Verification

The standalone, standard-library program `verification/beta_star_verify.py` computes beta-binomial tail probabilities in exact rational arithmetic using rising factorials. It separately computes all second differences and the Beta-moment expression (3), tests every pair and vaccination subset for all \(d=2,\ldots,8\), all permissible \(r\), and a \(6\times6\) grid of positive rational \(\alpha,\beta\), totaling 1,260 full parameter configurations. It additionally enumerates all binary infection assignments for three representative stars and reproduces the three exact fixed-mean interactions.

Run `python verification/beta_star_verify.py` from a directory containing the extracted package. These finite checks supplement but do not replace the preceding all-integer, all-positive-parameter proof.

## Relationship to prior work

Enns, Mounzer and Brandeau (2011) study how contact-edge removal can mitigate epidemics; the exposed abstract concerns optimal partitioning rather than the present beta-binomial overload objective. House and colleagues (2012) estimate household transmission with heterogeneous case infectiousness, motivating a common-infectiousness uncertainty model, but their examined methods and results do not classify vaccination benefit curvature. Han, Huang and Luo (2016; expanded 2018) prove log-submodularity properties of **independent** Poisson-binomial reliability tails and introduce surrogate objectives; their original tail objective need not be submodular. Conditioning on the common infectivity in our model produces independent binomial variables, but **averaging** that conditional relation does not imply a submodularity criterion for the resulting correlated tail; equations (3)–(5) give the additional, explicit correlation-dependent classification.

A theorem under any alias, such as discrete concavity of the beta-binomial tail as its trial count varies, would cover this result if it already establishes the exact criterion. No such prior classification was located in the literature examined, but that is not a proof of unique provenance.

## Limitations

The result applies to one-generation homogeneous stars, not general epidemic contact networks or adaptive vaccination. Each leaf is exchangeable, so choosing **which** leaves to vaccinate at a fixed coverage level is trivial; the mathematical content concerns the shape of the **coverage response** and how common infectiousness correlation can reverse its curvature. The correlation formula requires a Beta prior for the shared success probability. The threshold is for the probability of reaching at least \(r\) secondary infections; expected infections prevented remains modular. No claims about observed real-world efficacy or nonlinear epidemics follow. Some related papers were only accessible at abstract level; an unexamined equivalent beta-binomial reliability theorem remains a possible originality risk.

## References

1. E. A. Enns, J. J. Mounzer, M. L. Brandeau, “Optimal link removal for epidemic mitigation: a two-way partitioning approach,” *Mathematical Biosciences* 235 (2012), 138–147; first online 16 November 2011. DOI: 10.1016/j.mbs.2011.11.006.
2. T. House et al., “Estimation of outbreak severity and transmissibility: Influenza A(H1N1)pdm09 in households,” *BMC Medicine* 10, 117 (9 October 2012). DOI: 10.1186/1741-7015-10-117.
3. K. Han, H. Huang, J. Luo, “Posted pricing for robust crowdsensing,” ACM MobiHoc (2016), 261–270; expanded as “Quality-aware pricing for mobile crowdsensing,” *IEEE/ACM Transactions on Networking* 26 (2018), 1728–1741. DOI: 10.1109/TNET.2018.2846569.
