# Rarefaction richness and ultrametric phylogenetic diversity can be negatively correlated at every interior sampling depth

## Finding
For an integer \(N\ge 1\), draw \(m\in\{1,\ldots,N\}\) distinct individuals uniformly without replacement from a fixed community of \(N\) individuals. Each individual belongs to a species, with at least one individual per species. Species form the tips of a finite rooted phylogenetic tree whose root-to-tip distances are all equal and whose edges have positive lengths. Let \(K_m\) count represented species and \(P_m\) be the rooted phylogenetic diversity (the total length of the union of paths from the root to represented species).

**Theorem (complete sampling-depth sign boundary).** For every community and rooted ultrametric tree, \(\operatorname{Cov}(K_m,P_m)\ge0\) whenever \(m\in\{1,2,N-1,N\}\) (with overlaps understood). Conversely, for every \(N\ge5\) there exists one community and one strictly positive-length rooted ultrametric tree such that
\[
\operatorname{Cov}(K_m,P_m)<0\qquad\text{simultaneously for every }3\le m\le N-2.
\]
Consequently five individuals are the sharp population minimum for negative covariance; among every fixed population size, the displayed four endpoint sampling depths are exactly the depths at which nonnegative covariance is guaranteed for all ultrametric trees and abundance profiles.

The construction provides an exact edge-length phase boundary. Set \(s=N-2\) and take one species represented twice, with each of the other \(s\) species represented once. The root has a length-\(H\) edge directly to the twice-represented tip, and a length-\(H-\varepsilon\) edge to the common ancestor of all \(s\) singleton tips; each singleton tip has a terminal edge of length \(\varepsilon\), where \(0<\varepsilon<H\). For \(3\le m\le N-2\),
\[
\boxed{\operatorname{Cov}(K_m,P_m)
=\frac{m(m-1)(N-m)}{N^2(N-1)}
\left(2\varepsilon-H\frac{N-m-1}{N-1}\right).}
\]
In particular the covariance is negative exactly when
\[
\frac{\varepsilon}{H}<\frac{N-m-1}{2(N-1)}.
\]
Choosing \(0<\varepsilon/H<1/[2(N-1)]\) makes all the interior covariances negative at once. At the first possible population size \(N=5\), \(m=3\), \(H=1\), and \(\varepsilon=1/16\), the covariance equals \(-3/200\).

## Assumptions and scope
The population is a finite labeled multiset of individuals with positive integer species counts. The sample is a uniformly random subset of exactly \(m\) distinct individuals; different sample sizes refer to different random experiments. The tree is rooted, strictly positive-length, ultrametric, and contains one leaf per species, not per individual. Rooted PD always includes the original root. No inference is made about unrooted PD, sampling with replacement, estimator uncertainty, or general covariances between independent ecological communities. The singleton clade in the explicit construction may be multifurcating; a sufficiently small ultrametric bifurcating refinement preserves every strict inequality by continuity.

## Proof
**1. Universal endpoint nonnegativity.** At \(m=1\), each sample contains one species, so \(K_1=1\). At \(m=N\), both statistics are deterministic. Thus their covariance is zero.

At \(m=2\), write \(B=1\) when the two sampled individuals belong to distinct species and \(B=0\) otherwise. Then \(K_2=1+B\). If \(B=0\), the sampled rooted PD equals the common root-to-tip height \(H\). If \(B=1\), the rooted union of two tip paths contains at least one entire height-\(H\) path, hence \(P_2\ge H\). Therefore
\[
\operatorname{Cov}(K_2,P_2)=\Pr(B=0)\,\mathbb E[B(P_2-H)]\ge0.
\]
(The right-hand identity follows by expanding \(P_2=H+(P_2-H)B\), with the second factor understood to vanish when \(B=0\).)

At \(m=N-1\), equivalently omit one uniformly random individual. Let \(S\) denote the total number of species, let \(B\) indicate that the omitted individual was the sole individual of its species, and let \(L\ge0\) be the rooted PD length lost by omitting it. When \(B=0\), \(L=0\), since every species remains. Thus \(K_{N-1}=S-B\), \(P_{N-1}=P_{\mathrm{full}}-L\), and
\[
\operatorname{Cov}(K_{N-1},P_{N-1})
=\operatorname{Cov}(B,L)
=(1-\Pr(B=1))\mathbb E[L]\ge0.
\]
This argument actually does not require ultrametricity at the last two depths.

**2. A common negative example at every other depth.** Fix \(N\ge5\) and the explicit abundance profile and tree in the finding. For any \(3\le m\le N-2\), let \(X\in\{0,1,2\}\) be the number of sampled individuals belonging to the twice-represented species. Because \(m\ge3\) and there are only two such individuals, the singleton clade is always detected. Every sampled singleton individual is a distinct species. Consequently,
\[
K_m=m-\mathbf1_{\{X=2\}},\qquad
P_m=H-\varepsilon+\varepsilon(m-X)+H\mathbf1_{\{X>0\}}.
\]
The variable \(X\) is hypergeometric with sample size \(m\) and a marked population of size two. Write \(p_0=\Pr(X=0)\) and \(p_2=\Pr(X=2)\). Direct counting gives
\[
p_0=\frac{(N-m)(N-m-1)}{N(N-1)},\qquad
p_2=\frac{m(m-1)}{N(N-1)},\qquad
\mathbb E[X]=\frac{2m}{N}.
\]
The events \(X=0\) and \(X=2\) are disjoint, hence
\[
\operatorname{Cov}(K_m,\mathbf1_{\{X>0\}})=-p_0p_2,
\qquad
\operatorname{Cov}(K_m,m-X)=p_2\left(2-\frac{2m}{N}\right).
\]
Multiplying by the two contributions to \(P_m\) and factoring yields the boxed covariance identity. Since \(m\le N-2\), the bound \((N-m-1)/[2(N-1)]\ge1/[2(N-1)]>0\) holds. One common choice of \(\varepsilon\) below that last quantity makes every intermediate covariance strictly negative. Taking \(N=5\) gives the sharp first possible census size, because smaller populations have no sample depth outside the universally nonnegative set.

**3. Robust binary refinement.** Every probability and covariance here is a finite linear or quadratic expression in the tree's edge lengths. The strict simultaneous negative inequalities hold on an open neighborhood of the displayed tree lengths. Resolve the singleton polytomy into any rooted binary topology by inserting sufficiently short positive internal edges and shortening descendant edges to retain tip height \(H\). Continuity preserves all strict signs. Thus the counterexample does not depend on permitting multifurcations.

## Verification
The accompanying `verify.py` independently enumerates labeled-individual subsets, computes observed taxonomic richness and rooted PD as exact rational numbers, and compares its covariance with the analytical hypergeometric identity. For every integer \(5\le N\le12\), it checks all \(1\le m\le N\), including positivity at \(m=2,N-1\), negativity at every intermediate depth, and zero endpoints, using \(H=1\) and \(\varepsilon=1/[4(N-1)]\). It also verifies four exact zero-covariance edge-length boundary cases and the \(N=5\) rational witness. All 72 comparisons passed. This is corroborative finite verification, not the proof for unrestricted \(N\).

For reproducing the check, run `python verify.py` using Python 3's standard library. The program has no external dependencies.

## Relationship to prior work
Nipperess and Matsen (arXiv:1208.6552; journal publication 2013) derive exact formulas for mean and variance of rooted and unrooted phylogenetic diversity under rarefaction, generalizing species-richness calculations. Their full text provides the foundational edge-occupancy covariance framework; it does not state or establish the present universal/nonuniversal sample-depth classification, simultaneous interior negative-covariance construction, or exact branch-length phase boundary. O'Dwyer, Kembel and Green (2012) analyze mean and variance of sampled phylogenetic diversity under community-assembly sampling schemes, rather than this fixed-size richness–PD cross-covariance sign question. Chao and colleagues (first online 2014) establish PD rarefaction/extrapolation curves and estimators; they likewise do not give the present mixed-covariance sign classification.

Earlier formulas can be used to compute particular covariance instances. The structural sign characterization here is the asserted result, not a claim to have discovered the generic hypergeometric or PD formulas.

## Limitations
The theorem is restricted to rooted PD on ultrametric trees and fixed-size sampling without replacement. Positive branch lengths and at least one individual per species are required. The construction proves attainability of negative covariance, not optimal negative magnitude. The lack of an equivalent result in inspected literature is not a proof of bibliographic uniqueness, and independent expert review remains outstanding. No empirical causal inference is claimed.

## References
1. D. A. Nipperess and F. A. Matsen IV, *The mean and variance of phylogenetic diversity under rarefaction*, arXiv:1208.6552 (first submitted 2012-08-31); *Methods in Ecology and Evolution* 4 (2013), 566–572. https://arxiv.org/abs/1208.6552 ; https://doi.org/10.1111/2041-210X.12042 .
2. J. P. O'Dwyer, S. W. Kembel and J. L. Green, *Phylogenetic diversity theory sheds light on the structure of microbial communities*, *PLoS Computational Biology* 8 (2012), e1002832. https://doi.org/10.1371/journal.pcbi.1002832 .
3. A. Chao et al., *Rarefaction and extrapolation of phylogenetic diversity*, *Methods in Ecology and Evolution* (first online 2014-08-11). https://doi.org/10.1111/2041-210X.12247 .
