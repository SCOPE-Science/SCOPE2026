# A unique rank reversal under uniform thinning of overdispersed epidemic offspring

## Finding

Consider two independent, single-type Galton–Watson processes begun with one ancestor, with negative-binomial offspring having initial means \(R_1>R_2>0\) and dispersion parameters \(0<k_1<k_2\). Each potential secondary infection is retained independently with a common probability \(p\geq0\); for literal independent thinning, \(0\leq p\leq1\). Let \(S_i(p)\) denote the probability of indefinite survival of process \(i\). Then there exists **exactly one nontrivial equality** \(p_*>1/R_2\), and

\[
S_1(p)>S_2(p)\quad(1/R_1<p<p_*),\qquad S_1(p_*)=S_2(p_*)>0,\qquad S_1(p)<S_2(p)\quad(p>p_*).
\]

Both survival probabilities vanish for \(0\leq p\leq1/R_1\), so those trivial equalities are excluded. The unique crossing is specified without numerical branching-process iteration: the positive root \(t_*\) of

\[
\frac{k_1}{k_2}\frac{e^{t_*/k_1}-1}{e^{t_*/k_2}-1}=\frac{R_1}{R_2}
\]

exists uniquely, and

\[
p_*=\frac{k_2(e^{t_*/k_2}-1)}{R_2(1-e^{-t_*})},\qquad S_1(p_*)=S_2(p_*)=1-e^{-t_*}.
\]

Under physical retention \(p\in[0,1]\), the reversal is witnessed at two strict interior control intensities precisely when \(p_*<1\); at \(p_*=1\) only the endpoint ties, and at \(p_*>1\) the reversal is outside the admissible retention range. More generally, whenever the ordering of initial means and the ordering of dispersion parameters agree, there is no positive-survival rank reversal; a strictly higher mean paired with a strictly *smaller* dispersion parameter is the only ordering allowing one. This is a complete pairwise comparison for finite positive parameters.

An exact admissible example is \(R_1=4\), \(k_1=1/2\), \(R_2=3\), \(k_2=1\). Then

\[
p_*=\frac59,\qquad S_1(p_*)=S_2(p_*)=\frac25.
\]

At \(p=1/2\), the first survival probability is \(1-(1+\sqrt{17})/8>1/3\), while the second is \(1/3\). At \(p=1\), the first is \(1-(1+\sqrt{33})/16<2/3\), while the second is \(2/3\).

## Assumptions and scope

For each \(i\), different infectives and generations reproduce independently and identically. The unthinned count has negative-binomial mean \(R_i>0\), dispersion \(k_i>0\), and probability generating function

\[
G_i(z;1)=\bigl[1+(R_i/k_i)(1-z)\bigr]^{-k_i},\quad 0\leq z\leq1.
\]

The parameter \(p\) scales both means without changing either dispersion: independent thinning gives \(G_i(z;p)=G_i(1-p+pz;1)=[1+(pR_i/k_i)(1-z)]^{-k_i}\). Although the formula extends mathematically to \(p>1\) as a reparametrized negative-binomial law, such values are *not* probabilities of retaining contacts. The theorem describes ultimate survival in a branching-process approximation, not a finite-population outbreak probability or the total infected count under susceptible depletion. The two processes are alternatives compared at the same \(p\), not two interacting disease types.

## Proof

**1. Survival and its inverse parameterization.** The standard Galton–Watson fixed-point rule says that the eventual extinction probability is the smallest fixed point of \(G_i\) in \([0,1]\). As \(G_i'(1;p)=pR_i\), survival is zero for \(pR_i\leq1\), and is uniquely positive for \(pR_i>1\) (the pgf is strictly convex and has positive mass at zero). Writing \(s=1-q\), its positive fixed point solves

\[
1-s=\bigl(1+(pR_i/k_i)s\bigr)^{-k_i}
\]

or equivalently

\[
p=\frac{\Phi_{k_i}(s)}{R_i},\qquad\Phi_k(s)=\frac{k\{(1-s)^{-1/k}-1\}}s=\frac1s\int_0^s(1-u)^{-1-1/k}\,du.
\]

For every \(k>0\), the integrand is strictly increasing on \([0,1)\), hence its initial-interval average \(\Phi_k(s)\) is continuous and strictly increasing from \(1\) to \(+\infty\) as \(s\) runs from \(0\) to \(1\). Therefore this parameterization bijectively represents every positive survival probability.

**2. One-crossing lemma.** Put \(s=1-e^{-t}\), \(t>0\). For \(k_1<k_2\),

\[
\frac{\Phi_{k_1}(s)}{\Phi_{k_2}(s)}=\frac{k_1}{k_2}\frac{e^{t/k_1}-1}{e^{t/k_2}-1}=:H(t).
\]

It tends to \(1\) as \(t\downarrow0\) and to \(+\infty\) as \(t\to\infty\). Moreover,

\[
\frac{d}{dt}\log H(t)=\frac{1/k_1}{1-e^{-t/k_1}}-\frac{1/k_2}{1-e^{-t/k_2}}>0.
\]

Indeed, for fixed \(t>0\) the function \(a\mapsto a/(1-e^{-at})\) is strictly increasing: its derivative has numerator \(1-e^{-at}(1+at)>0\), because \(e^{at}>1+at\). Thus \(H\) strictly increases, proving a unique positive solution \(t_*\) to \(H(t_*)=R_1/R_2>1\). The common retention \(p_*\) is found by substituting the common positive \(s_*=1-e^{-t_*}\) into either inverse formula. Since \(\Phi_k(s_*)>1\), it satisfies \(p_*>1/R_2\).

**3. Strict global ranking.** The two required-retention curves are \(p_i(s)=\Phi_{k_i}(s)/R_i\). Their ratio is \(p_1(s)/p_2(s)=H(t)R_2/R_1\), strictly increasing through one at \(s_*\). If \(p\) is between \(1/R_1\) and \(p_*\), either process 2 is still subcritical, or \(S_2(p)<s_*\). In the latter case \(p_1(S_2(p))<p_2(S_2(p))=p\); the strict monotonicity of \(p_1\) gives \(S_1(p)>S_2(p)\). If \(p>p_*\), \(S_2(p)>s_*\) and the same argument with the inequality reversed yields \(S_1(p)<S_2(p)\). At \(p_*\) both positive survival values equal \(s_*\). No other nonzero equality is possible.

For completeness, if \(k_1<k_2\) but \(R_1\leq R_2\), then \(\Phi_{k_1}(s)/R_1>\Phi_{k_2}(s)/R_2\) for every \(s>0\), so process 2 has strictly greater survival whenever it is supercritical; if dispersions are equal, larger \(R\) wins wherever it survives. Reversing labels establishes the full classification.

**4. Exact example.** With the displayed parameters, \(H(t)=(e^t+1)/2\). Equality \(H(t)=4/3\) gives \(e^{t_*}=5/3\) and \(s_*=2/5\), \(p_*=5/9\). At \(p=1/2\), process 1 extinction is the nonunit root of \(q^2(5-4q)=1\), namely \((1+\sqrt{17})/8\); process 2 extinction is \(2/3\). At \(p=1\), the corresponding nonunit roots are \((1+\sqrt{33})/16\) and \(1/3\). Their stated strict order follows by squaring positive quantities or by decimal comparison with rational bounds. This also exhibits an interior, not merely extrapolated, physical-control crossing.

## Verification

Run \(\texttt{python verify.py}\) in an environment with Python 3 and SciPy. The program independently solves the extinction fixed points through the increasing inverse parameterization, checks the exact example, checks 2,500 random opposing-order parameter configurations on both sides of the crossing, and checks 2,000 same-order cases. Finite trials are diagnostic only; Steps 1–4 prove the universal statement for all real positive parameters. The formula for \(p>1\) is a mathematical continuation rather than literal Bernoulli thinning.

## Relationship to prior work

Lloyd-Smith et al. (2005) introduced and analyzed the gamma–Poisson / negative-binomial offspring law and compared the effects of a common reproduction number and varying dispersion; their population-wide intervention scales the mean while preserving the dispersion parameter. These established equations are premises, **not** novel model development. Their published qualitative extinction rankings are for fixed mean or distinct control designs, rather than a theorem comparing *both distinct means and distinct dispersions* under a single shared retention parameter with exactly one positive-survival crossing. Sawaya and Klaere (2014) analyze extinction through moments and offspring-distribution comparisons, not this negative-binomial one-crossing classification. Bürger (2026), Section 4.3, develops finite-generation bounds for negative-binomial branching processes, not the cross-model control-intensity ordering asserted here. The present contribution is the complete strict ordering and unique nontrivial crossing, including the explicit physically admissible example.

## Limitations

The entire result is conditional on independent identically distributed offspring and a common uniform retention factor. Repeated-contact dependence, type mixing, generation dependence, depletion of susceptible hosts, or intervention-induced changes in \(k\) are outside the theorem. The prior negative-binomial generating function already makes individual survival curves numerically computable; the contribution is their parameter-uniform comparative structure, not a new epidemic model or a generally improved numerical solver. Claims of historical priority remain provisional: a specialized comparison theorem outside the inspected sources could imply the ranking. A closely related supplement to the 2005 study was not fully accessible for examination. No empirical claim about interventions is made.

## References

1. Lloyd-Smith, J. O., Schreiber, S. J., Kopp, P. E., and Getz, W. M. (2005), “Superspreading and the effect of individual variation on disease emergence,” *Nature* 438, 355–359, doi:10.1038/nature04153. Full original article: https://jdyeakel.github.io/teaching/advtopicsecoevo/papers/LloydSmith_2005.pdf .
2. Sawaya, S., and Klaere, S. (2014), “Extinction in a branching process: why some of the fittest strategies cannot guarantee survival,” *Journal of Statistical Distributions and Applications* 1, 10, doi:10.1186/2195-5832-1-10.
3. Bürger, R. (2026), “Bounds for survival probabilities in supercritical Galton-Watson processes and applications to population genetics,” *Journal of Mathematical Biology* 92, 40, doi:10.1007/s00285-026-02349-7.
