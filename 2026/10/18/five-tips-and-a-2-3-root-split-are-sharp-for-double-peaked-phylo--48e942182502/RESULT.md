# Five tips and a \(2+3\) root split are sharp for double-peaked phylogenetic rarefaction variance

## Finding
Consider rooted, fully bifurcating, ultrametric phylogenetic trees with strictly positive edge lengths and one distinguishable tip per species. Normalize every root-to-tip distance to \(1\). For each \(k\in\{1,\ldots,n\}\), uniformly choose exactly \(k\) of the \(n\) tips without replacement and let \(V_k\) be the population variance of rooted Faith phylogenetic diversity (the length of the union of root-to-chosen-tip paths). A *strict interior variance peak* at \(k\) means \(V_k>V_{k-1}\) and \(V_k>V_{k+1}\), where \(2\le k\le n-1\).

**Theorem.** No such tree with at most four tips has two strict interior peaks. With five tips, two peaks exist, necessarily at \(k=2\) and \(k=4\), and can occur **only** when the root split is \(2+3\), not \(1+4\). Conversely, for a five-tip tree with a \(2+3\) root split, write \(a\) for the age (measured upward from the tips) of the two-tip cherry, \(b\) for that of the three-tip subtree, and \(c\) for the cherry nested inside the three-tip subtree. Thus \(0<a<1\) and \(0<c<b<1\). The tree has exactly two strict interior variance peaks **if and only if** both of the following polynomials are positive:

\[
\begin{aligned}
P(a,b,c)={}&-12a^2+26ab+16ac-18a-9b^2+6bc-14b-12c^2+2c+15,\\
Q(a,b,c)={}&3a^2+14ab-14ac-6a-9b^2-6bc+10b+3c^2+14c-9.
\end{aligned}
\]

Indeed \(P=100(V_2-V_3)\) and \(Q=100(V_4-V_3)\). The admissible positive region is nonempty: at \((a,b,c)=(1/4,3/4,2/3)\),
\[
(V_1,V_2,V_3,V_4,V_5)=\left(0,\frac{263}{4800},\frac{19}{400},\frac{29}{600},0\right),
\qquad V_2-V_3=\frac7{960},\quad V_4-V_3=\frac1{1200}.
\]
Both strict peaks persist under sufficiently small perturbations of all positive branch lengths that preserve ultrametricity.

## Assumptions and scope
A fully bifurcating rooted tree has exactly two children at each internal vertex, including the root. The five tips are distinct and have equal sampling weight. For any nonempty tip set \(S\), define \(Y(S)\) as the sum of lengths of all edges with at least one descendant in \(S\). For \(S_k\) uniform among the \(\binom nk\) subsets of size \(k\), put \(V_k=\mathbb E[Y(S_k)^2]-\mathbb E[Y(S_k)]^2\). Variance is the population variance, with denominator \(\binom nk\), not the unbiased-sample-variance estimator. The root is included in PD; this is not unrooted PD, and fixed-size sampling is not independent Bernoulli thinning. All edge lengths are strictly positive. The unit-height normalization does not restrict peak signs, because scaling all edge lengths scales each \(V_k\) by the same positive square.

## Proof
**1. Small-tip obstruction.** Ultrametricity makes \(Y(S_1)=1\) deterministically, while sampling every tip also makes \(Y(S_n)\) deterministic. Thus \(V_1=V_n=0\). For \(n\le4\), there are at most two interior sample sizes, and for \(n=4\) they are adjacent; adjacent indices cannot both be strict local maxima. Therefore two strict interior peaks require \(n\ge5\). When \(n=5\), the only possible pair of such peaks is \(\{2,4\}\).

**2. Complete shape reduction at five tips.** An unordered root split is either \(1+4\) or \(2+3\). The \(1+4\) case has two distinct fully bifurcating descendant shapes: \(1+(1+(1+2))\) and \(1+((2)+(2))\). The \(2+3\) case has only one shape, \((2)+(1+(2))\). These are all three five-tip rooted binary shapes up to tip relabeling.

For the first \(1+4\) shape, let the ages of its three successive internal vertices below the root be \(a>b>c>0\), with \(a<1\). Set \(x=1-a>0\), \(y=a-b>0\), \(z=b-c>0\). Directly averaging the finitely many root-to-sample path unions yields
\[
100(V_2-V_3)=-12xy-8xz-15y^2-18yz-12z^2<0.
\]
For the second \(1+4\) shape, let \(a\) be the age of the four-tip descendant root and \(b,c\) the ages of its two cherries, so \(0<b,c<a<1\). With \(x=1-a\), \(y=a-b\), \(z=a-c\), the corresponding exact identity is
\[
100(V_2-V_3)=-4\{2x(y+z)+3y^2-4yz+3z^2\}<0.
\]
The inequality holds because \(3y^2-4yz+3z^2=(y-z)^2+2(y^2-yz+z^2)>0\). Thus neither \(1+4\) shape admits a peak at \(k=2\), hence neither admits two peaks.

**3. The \(2+3\) phase diagram.** In the remaining shape, the eight edges have descendant-tip sets and lengths as follows: a two-tip stem of length \(1-a\), its two pendant edges of length \(a\), a three-tip stem of length \(1-b\), the singleton pendant edge of length \(b\), the nested two-tip stem of length \(b-c\), and its two pendant edges of length \(c\). Every edge contributes to \(Y(S)\) exactly when its descendant set meets \(S\). Enumerating the \(10\) two-tip samples, \(10\) three-tip samples and \(5\) four-tip samples gives
\[
\begin{aligned}
100V_2={}&9a^2-4ab-2ac-12a+16b^2-4bc-24b+9c^2-12c+24,\\
100V_3={}&21a^2-30ab-18ac+6a+25b^2-10bc-10b+21c^2-14c+9,\\
25V_4={}&2(3a^2-2ab-4ac+2b^2-2bc+3c^2).
\end{aligned}
\]
Subtracting these gives exactly \(100(V_2-V_3)=P(a,b,c)\) and \(100(V_4-V_3)=Q(a,b,c)\). Since \(V_1=V_5=0\) and variances are nonnegative, the two strict local maxima occur precisely when \(P>0\) and \(Q>0\). This is an exact necessary-and-sufficient semialgebraic characterization of the admissible branch-age region, rather than a numerical grid classification.

**4. Strict witness.** Substitute \((a,b,c)=(1/4,3/4,2/3)\) into the formulas. The corresponding edge lengths are \(3/4,1/4,1/4,1/4,3/4,1/12,2/3,2/3\), all strictly positive, with each root-to-tip path of length one. The exact variances and strictly positive peak gaps shown in the Finding follow. Both inequalities are strict polynomial inequalities on an open admissible parameter region, proving robustness under perturbations.

## Verification
Run \(\texttt{python3 verify.py}\) from the directory containing this document and \(\texttt{verify.py}\). The standard-library-only program independently constructs each of the three rooted five-tip shapes, enumerates all nonempty subsets, forms exact symbolic quadratic variance polynomials, and compares them to both one-versus-four nonpositivity decompositions and the two explicit two-versus-three phase polynomials. It then tests the rational witness and recomputes all \(31\) subset PD values independently with \(\texttt{fractions.Fraction}\). Every identity is exact, with no floating point or random sampling. The proof of the small-tip obstruction and the positivity of the displayed quadratic forms are analytic; the program supplements, rather than substitutes for, those arguments.

## Relationship to prior work
Nipperess and Matsen derived general exact formulas for mean and variance of rooted and unrooted phylogenetic diversity under fixed-size rarefaction. Their formulas and the rooted-PD definition are prior work; this result does not claim either formula. Their discussion identifies sensitivity to tree shape as a direction for further analysis. The contribution here is the exact **shape-restricted peak-count classification** at the first possible tip size, together with the necessary-and-sufficient positive parameter region for the only permissible shape. The general variance formula permits individual instances to be computed, but does not itself state the five-tip root-split obstruction or the two strict peak inequalities.

O'Dwyer, Kembel, and Green study phylogenetic-diversity mean and variance under multiple community-sampling laws, with emphasis on binomial and related random-size processes; those are not uniform fixed-cardinality tip rarefaction. Faller, Pardi, and Steel study diversity under independent species extinction, likewise with random survivor count. Those distinct models do not imply the exact five-tip conditioned-sampling root-shape classification without further analysis. In particular, multiple variance peaks as a function of independent survival probability are not the present two peaks as a function of fixed sample size.

## Limitations
This is a finite-topology and local parameter-phase theorem, not a claim that two peaks are typical in real phylogenies. The input is a known ultrametric tree with strictly positive branches and one tip per species; unequal species abundances, multifurcations, unresolved phylogenetic uncertainty, sample weights, and unrooted PD are excluded. The variance is conditional on exact sampling depth, not an estimator variance or random sample-size variance. The general variance calculation is established prior work; the claimed novelty is specifically the topology-dependent sharp phase classification, subject to further independent bibliographic scrutiny.

## References
1. D. A. Nipperess and F. A. Matsen IV, *The mean and variance of phylogenetic diversity under rarefaction*, arXiv:1208.6552, first public version 31 August 2012; *Methods in Ecology and Evolution* 4 (2013), 566–572. DOI: 10.1111/2041-210X.12042. https://arxiv.org/abs/1208.6552
2. J. P. O'Dwyer, S. W. Kembel, and J. L. Green, *Phylogenetic diversity theory sheds light on the structure of microbial communities*, *PLOS Computational Biology* 8 (2012), e1002832. DOI: 10.1371/journal.pcbi.1002832. https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1002832
3. B. Faller, F. Pardi, and M. Steel, *Distribution of phylogenetic diversity under random extinction*, *Journal of Theoretical Biology* 251 (2008), 286–296. DOI: 10.1016/j.jtbi.2007.11.034. https://pubmed.ncbi.nlm.nih.gov/18199459/
