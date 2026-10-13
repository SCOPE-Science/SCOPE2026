# Sample-size-invariant cherry–external-length covariance in Kingman’s coalescent

## Finding
In a standard \(n\)-leaf Kingman genealogy, let \(C_n\) count cherries (coalescences whose two children are original singleton leaves), and let \(E_n\) be the total external branch length. Then
\[
\operatorname{Cov}(C_n,E_n)=\begin{cases}0,&n=2,3,\\-2/9,&n\ge4.\end{cases}
\]
The negative covariance is **exactly constant across all sample sizes \(n\ge4\)**. More precisely, for every integer \(n\ge4\) and \(2\le k\le n\), the number \(B_k\) of still-singleton lineages when \(k\) ancestral lineages remain satisfies
\[
\operatorname{Cov}(C_n,B_k)=-\frac{k(k-1)(n-k)(n-k-1)}{3(n-1)(n-2)(n-3)}.
\]
This level-resolved identity, when weighted by the independent Kingman holding times, gives the constant covariance.

## Assumptions and scope
Fix an integer \(n\ge2\). Start with \(n\) distinctly labelled singleton lineages. While \(k\) lineages remain, every unordered pair coalesces at rate \(1\); independently of which pair is chosen, the holding time \(T_k\) is exponential of rate \(k(k-1)/2\), so \(\mathbb E T_k=2/[k(k-1)]\). All holding times are mutually independent and independent of the entire sequence of chosen pairs. The genealogy stops at its most recent common ancestor. A *cherry* is the internal node created by coalescing two singleton lineages that still each represent just one original sampled leaf. Let \(J_j\) indicate such a merger in the step \(j\to j-1\); thus \(C_n=\sum_{j=2}^{n}J_j\). Let \(B_k\) be the number of original singleton lineages extant at level \(k\), so
\[
E_n=\sum_{k=2}^{n}B_kT_k.
\]
In particular, this is total pendant/external length, **not** total tree length. No conditioning on tree shape, no variable effective population size, and no nonbinary mergers are assumed.

## Proof
For \(n=2,3\), every genealogy has exactly one cherry, making the covariance zero. Hence assume \(n\ge4\). Write \((a)_r=a(a-1)\cdots(a-r+1)\) for a falling factorial. If \(r\in\{1,2,3\}\) specified original leaves must remain singletons at level \(k\), every merger from level \(s\) to \(s-1\) must avoid all those leaves. Its probability is \((s-r)(s-r-1)/[s(s-1)]\). Multiplying over \(s=n,n-1,\ldots,k+1\) and summing ordered choices of \(r\) leaves gives
\[
\mathbb E[(B_k)_r]=\frac{(k)_r(k-1)_r}{(n-1)_r}
\qquad(r=1,2,3).
\tag{1}
\]
By conditioning the next merger on \(B_j\), \(\mathbb E[J_j\mid B_j]=(B_j)_2/[j(j-1)]\). Formula (1) yields, for \(3\le j\le n\),
\[
\mathbb E J_j=\frac{(j-1)(j-2)}{(n-1)(n-2)},\qquad
\mathbb E B_k=\frac{k(k-1)}{n-1}.
\tag{2}
\]
Here \(J_2=0\), since the step at level \(2\) cannot merge two original singletons when \(n\ge3\). Summing (2) gives \(\mathbb EC_n=n/3\).

We next calculate the mixed moment \(\mathbb E[B_k J_j]\), distinguishing the relative positions of the two levels. For \(3\le j\le k\le n\), a specified pair of extant original singleton leaves at level \(k\) survives without either participating in a merger until level \(j\), and the members then coalesce with each other, with probability
\[
\left(\prod_{s=j+1}^{k}\frac{(s-2)(s-3)}{s(s-1)}\right)\frac{2}{j(j-1)}
=\frac{2(j-1)(j-2)}{k(k-1)^2(k-2)}.
\]
Multiplying by the number \(\binom{B_k}{2}\) of candidate pairs, weighting by \(B_k\), and using \(B_k(B_k)_2=(B_k)_3+2(B_k)_2\) and (1) yields
\[
\mathbb E[B_kJ_j]
=\mathbb EJ_j\left(2+\frac{(k-2)(k-3)}{n-3}\right).
\tag{3}
\]
For \(2\le k<j\le n\), conditional on \(J_j=1\), the next state has \(j-1\) lineages, among which the expected number of original singletons is \((j-2)(j-3)/(n-3)\), by (3) at \(k=j\), followed by removal of the two singleton children. Each such singleton subsequently survives until level \(k\) with probability \(k(k-1)/[(j-1)(j-2)]\). Thus
\[
\mathbb E[B_kJ_j]
=\frac{k(k-1)(j-2)(j-3)}{(n-1)(n-2)(n-3)}.
\tag{4}
\]
Formula (3) is needed only for \(k\ge3\); when \(k=2\), its index range is empty. Summing (3) and (4) across \(j\), subtracting \(\mathbb EC_n\mathbb EB_k\), and applying \(\sum_{j=3}^{m}(j-1)(j-2)=m(m-1)(m-2)/3\) gives
\[
\operatorname{Cov}(C_n,B_k)
=-\frac{k(k-1)(n-k)(n-k-1)}{3(n-1)(n-2)(n-3)}
\quad(2\le k\le n),
\tag{5}
\]
including both endpoint values directly.

Independence of holding times from merger choices now gives
\[
\begin{aligned}
\operatorname{Cov}(C_n,E_n)
&=\sum_{k=2}^{n}\mathbb ET_k\operatorname{Cov}(C_n,B_k)\\
&=-\frac{2}{3(n-1)(n-2)(n-3)}
\sum_{k=2}^{n}(n-k)(n-k-1)\\
&=-\frac{2}{3(n-1)(n-2)(n-3)}\frac{(n-1)(n-2)(n-3)}{3}
=-\frac29.
\end{aligned}
\]
The same identities show \(\mathbb EE_n=2\) for every \(n\ge2\). If unordered pairs instead coalesce at rate \(\beta>0\), each holding time is divided by \(\beta\), hence the covariance is divided by \(\beta\). This proves the stated scope.

## Verification
The accompanying self-contained program `verify_cherry_external.py` uses exact rational arithmetic. It independently (i) enumerates every pair-merger history with distinctly labelled initial leaves for \(2\le n\le7\) (59,602 complete histories), (ii) propagates a Markov recursion for \(\mathbb EC_n\), \(\mathbb EE_n\) and the mixed moment for \(2\le n\le60\), and (iii) checks all 1,767 instances of the level-resolved covariance for \(4\le n\le60\). No simulation, numerical tolerances, or finite enumeration is used as an infinite-dimensional proof; the displayed algebra proves the result for all permissible \(n\).

## Relationship to prior work
Janson–Kersting [1] analyze total external length through a singleton-count urn chain, including its mean, variance and asymptotics; this paper does not supply a cherry mixed moment. Disanto–Wiehe [2] derive exact distributions of cherry and pitchfork counts in ranked Kingman tree *topologies*, explicitly excluding branch lengths. Palacios and collaborators [3, Appendix A] encode both singleton counts and cherries in a ranked-tree state representation, permitting joint-distribution calculations, but do not state the exact sample-size-invariant mixed covariance derived here. Alimpiev–Rosenberg [4] collect exact coalescent correlations among six time/length statistics without a cherry count. François–Mioland [5, sections 2 and 4] treat the **marginal** cherry count and, separately, the marginal total height of cherries and external-length sum under a Popović point-process model; their Gaussian approximation results are not an exact Kingman cherry-count/external-length mixed moment. Thus (5) and the constant \(-2/9\) fill a specific mixed topology–branch-length question not expressed in those inspected sources. A possible earlier joint-generating-function derivation remains a residual literature risk despite the directly related full-paper comparison [5].

## Limitations
The theorem concerns a fixed-size, neutral, homogeneous binary Kingman genealogy in unit coalescent time. It does not establish independence, a joint distribution, other mixed moments, population-size-varying coalescents, or results for multiple mergers. Any different convention for pairwise coalescent rate requires rescaling. Historical publication under alternate terminology for the same mixed moment cannot be categorically excluded by the inspected sources.

## References
[1] S. Janson and G. Kersting, *The external lengths in Kingman’s coalescent*, arXiv:1004.5011, first submitted 2010-04-28. https://arxiv.org/abs/1004.5011

[2] F. Disanto and T. Wiehe, *Exact enumeration of cherries and pitchforks in ranked trees under the coalescent model*, arXiv:1112.1295 (2011). https://arxiv.org/abs/1112.1295

[3] J. A. Palacios et al., *Bayesian Estimation of Population Size Changes by Sampling Tajima’s Trees*, *Genetics* **213** (2019), 967–986, doi:10.1534/genetics.119.302373. https://doi.org/10.1534/genetics.119.302373

[4] E. Alimpiev and N. A. Rosenberg, *A compendium of covariances and correlation coefficients of coalescent tree properties*, arXiv:2103.13467 (2021). https://arxiv.org/abs/2103.13467

[5] O. François and C. Mioland, *Gaussian approximations for phylogenetic branch length statistics under stochastic models of biodiversity*, *Mathematical Biosciences* **209** (2007), 108–123; first available online 2007-02-04. https://doi.org/10.1016/j.mbs.2007.01.005
