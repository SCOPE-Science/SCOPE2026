# Three distinct finite-population assays identify prevalence and both error rates without a gold standard

## Finding

**Theorem (sharp three-result identification and feasibility).** Fix a known integer \(N\ge3\). A closed finite population contains an unknown integer \(M\in\{1,\ldots,N-1\}\) affected individuals. An ordered sample of three **distinct** individuals is uniform without replacement. The same binary assay, independently conditionally on the true states, has unknown sensitivity \(a\), unknown false-positive probability \(b\), and \(0<b<a<1\). Let its reported results be \(Y_1,Y_2,Y_3\in\{0,1\}\), with population moments

\[
 u=\mathbb E Y_1,\qquad v=\operatorname{Cov}(Y_1,Y_2),\qquad w=\mathbb E[(Y_1-u)(Y_2-u)(Y_3-u)].
\]

These **three** moments identify \((M,a,b)\) uniquely. Define

\[
 z=\frac{(N-2)w}{2\sqrt{N-1}(-v)^{3/2}},\qquad
 p=\frac12\left(1-\frac{z}{\sqrt{z^2+4}}\right),\qquad
 c=\sqrt{\frac{-(N-1)v}{p(1-p)}}.
\]

The unique parameters are \(M=Np\), \(a=u+c(1-p)\), and \(b=u-cp\). In particular \(v<0\). An **exchangeable** Bernoulli triple with statistics \((u,v,w)\) arises from this model if and only if \(v<0\), the reconstructed \(Np\) is an integer between \(1\) and \(N-1\), and \(0<u-cp<u+c(1-p)<1\); these conditions are an exact three-moment feasibility test.

Three results are sharp: for **every** \(N\ge3\) there are two distinct admissible parameter triples with identical **complete two-result joint distributions** but distinct three-result laws. For fixed \(c=1/4\) and \(u=1/2\), the choices \(M=1\) and \(M=N-1\), with \(b=u-cM/N\) and \(a=b+c\), have the same two-result covariance \(-1/(16N^2)\) and opposite third central moments \(\pm1/(32N^3)\).

## Assumptions and scope

One population of known size \(N\) has a **fixed**, not binomially random, number \(M\) of affected individuals. The sampling unit is an ordered triple of distinct population members, sampled uniformly without replacement; repeated independently randomized triples are one possible way of learning its population distribution, provided repeat measurements have fresh conditionally independent errors. The one assay is homogeneous across individuals and occasions. Given true statuses \(X_i\in\{0,1\}\), reports are independent and satisfy \(\Pr(Y_i=1\mid X_i=1)=a\) and \(\Pr(Y_i=1\mid X_i=0)=b\). We assume \(0<b<a<1\), meaning better-than-random test discrimination. Identifiability concerns the **population joint distribution**, not recovery from a single observed triple or accuracy of finite-sample estimation. The unrestricted result covers every \(N\ge3\) and \(1\le M\le N-1\).

## Proof

**1. Hypergeometric moments.** Write \(p=M/N\) and \(c=a-b\). For distinct uniformly sampled individuals, \(\mathbb E X_i=p\), and the standard finite-composition factorial identities give

\[
\mathbb E X_1X_2=\frac{M(M-1)}{N(N-1)},\quad
\mathbb E X_1X_2X_3=\frac{M(M-1)(M-2)}{N(N-1)(N-2)}.
\]

Expansion of centered products yields

\[
\operatorname{Cov}(X_1,X_2)=-\frac{p(1-p)}{N-1},\qquad
\mathbb E\prod_{i=1}^3(X_i-p)=\frac{2p(1-p)(1-2p)}{(N-1)(N-2)}.
\]

Both identities remain valid if \(M=1\) or \(N-1\) because falling factorials then vanish appropriately. In particular there are no independence assumptions on \(X_1,X_2,X_3\).

**2. Exact error transfer.** Conditional independence implies \(\mathbb E[Y_i\mid X_1,X_2,X_3]=b+cX_i\). Repeated conditioning gives, for products involving **distinct** indices, covariance and third centered cross moment equal those of the conditional expectations. Consequently

\[
 u=b+cp,\qquad
 v=-\frac{c^2p(1-p)}{N-1},\qquad
 w=\frac{2c^3p(1-p)(1-2p)}{(N-1)(N-2)}.
\]

The sign of \(w\) is the sign of \(1-2p\). In particular \(v<0\).

**3. Global inverse.** Eliminating \(c\) gives

\[
\frac{(N-2)w}{2\sqrt{N-1}(-v)^{3/2}}
=\frac{1-2p}{\sqrt{p(1-p)}}.
\]

The right side strictly decreases from \(+\infty\) to \(-\infty\) as \(p\) increases from zero to one: letting \(s=1-2p\) makes it \(2s/\sqrt{1-s^2}\), with positive derivative in \(s\). Its unique inverse is the stated \(p\). The strictly positive \(c\) follows from \(v\), then \(a,b\) from \(u\). This proves global injectivity with no exceptional half-prevalence case: \(w=0\) forces \(p=1/2\).

**4. Exact feasibility of an exchangeable observed triple.** The derived inequalities and integrality condition are necessary. Conversely, given an exchangeable Bernoulli law and moments satisfying them, construct \((M,a,b)\) from the inverse. It reproduces the three moments by the identities above. Every exchangeable Bernoulli triple is determined by its common first raw moment \(u\), second raw cross moment \(u^2+v\), and third raw cross moment \(u^3+3uv+w\): for \(K=Y_1+Y_2+Y_3\),

\[
\begin{aligned}
\Pr(K=3)&=m_3,\\
\Pr(K=2)&=3(m_2-m_3),\\
\Pr(K=1)&=3(m_1-2m_2+m_3),\\
\Pr(K=0)&=1-3m_1+3m_2-m_3,
\end{aligned}
\]

where \(m_1=u\), \(m_2=u^2+v\), and \(m_3=u^3+3uv+w\). Therefore matching the moments matches every one of the eight labeled outcome probabilities, proving sufficiency.

**5. Sharp two-result ambiguity.** For any \(N\ge3\), put \(c=1/4\), \(u=1/2\), and construct model A with \(p=1/N\) and model B with \(p'=1-1/N\). For either model use \(b=u-cp\), \(a=b+c\) (with its own prevalence). Both obey \(0<b<a<1\), both have reported mean \(1/2\) and pair covariance \(-1/(16N^2)\). Since every symmetric pair of Bernoulli variables is determined by its mean and covariance, their entire two-result laws coincide. Their third centered moments equal \(+1/(32N^3)\) and \(-1/(32N^3)\), respectively, so their three-result laws differ. Thus one or two test results cannot universally identify the model, whereas three can.

## Verification

The standalone `verify.py` enumerates ordered disease-status vectors via exact finite-population factorial counts and every possible observed binary output. It uses rational arithmetic throughout and checks the exact mean, covariance, third moment, inversion identities, and the explicit indistinguishable-pair construction for \(N=3,\ldots,11\). It tests four strictly interior assay pairs for every admissible \(M\), giving 216 independently enumerated configurations and nine separate two-result equivalence checks. Run `python verify.py` to reproduce `certificate.json` (standard library only).

For example, \(N=7\), \(M=2\), \(a=4/5\), and \(b=1/10\) give \(u=3/10\), \(v=-1/60\), and \(w=1/500\). These are illustrations only: the unrestricted theorem follows from the factorial-moment proof, not from finite enumeration.

## Relationship to prior work

Hui and Walter (1980) identify errors using **two distinct diagnostic tests across two populations with different prevalences**, unlike one assay applied to a fixed-composition population. Su, Gardner, and Johnson (2004) explicitly develop **finite-population** diagnostic inference without a gold standard, but their accessible abstract frames the model around joint/sequential **two-test and two-population** designs; the complete text was not accessible for comparison. The claim here is limited to an explicit one-assay, three-*distinct-person* population-law inverse and sharp two-result non-identifiability, not to a claim of inventing finite-population diagnostic inference.

Huang et al. (2016 first online) prove three distinct **pool sizes** optimal for estimating prevalence and two assay error parameters under a **binomial independent-pool** model; their full paper uses group-size response probabilities, rather than the negative dependence of three individuals drawn without replacement. Ge et al. (2023 preprint) analyze one imperfect assay with fixed finite-population prevalence but assume **known** sensitivity and specificity; the accessible full text focuses on variance and interval correction, not unknown-error structural identification. These results do not give the stated three-distinct-person inversion or two-result indistinguishability construction under the present model.

## Limitations

This is **structural**, not practical, identification. For fixed interior \(p\) and \(c\), \(|v|=\Theta(N^{-1})\) and \(|w|=\Theta(N^{-2})\), making the inverse poorly conditioned in large populations; no finite-sample confidence guarantees are proved. Conditional error independence and homogeneous error rates are essential. If the composition is binomially randomized independently before each individual draw, the finite-population cross-moments disappear and this mechanism does not identify the errors. If \(M=0\) or \(M=N\), or \(a=b\), identification fails. If the orientation \(a>b\) is dropped, disease-label interchange prevents uniqueness. Repeated testing must not silently be treated as independent if errors are persistent within individuals. Literature overlap beyond accessible full texts remains possible, especially Su et al. (2004).

## References

1. Hui, S. L., and Walter, S. D. (1980). *Estimating the error rates of diagnostic tests.* Biometrics 36, 167–171. DOI: 10.2307/2530508. PubMed 7370371.
2. Su, C.-L., Gardner, I. A., and Johnson, W. O. (2004). *Diagnostic test accuracy and prevalence inferences based on joint and sequential testing with finite population sampling.* Statistics in Medicine 23, 2237–2255. DOI: 10.1002/sim.1809. First online June 29, 2004.
3. Huang, S.-H., Huang, M.-N. L., Shedden, K., and Wong, W. K. (2016 online). *Optimal group testing designs for estimating prevalence with uncertain testing errors.* DOI: 10.1111/rssb.12223. Accessible full text at https://pmc.ncbi.nlm.nih.gov/articles/PMC5726813/ .
4. Ge, L., Zhang, Y., Waller, L. A., and Lyles, R. H. (2023 preprint). *Enhanced inference for finite population sampling-based prevalence estimation with misclassification errors.* arXiv:2302.03558; accessible manuscript at https://pmc.ncbi.nlm.nih.gov/articles/PMC11027951/ .
