# Five tips are the sharp threshold for noise-driven changes in optimal phylogenetic sampling

## Finding
For a rooted binary ultrametric phylogenetic tree with positive edge lengths and a known Brownian evolutionary covariance, suppose exactly \(k\) distinct extant taxa are chosen to estimate their unknown common root-trait mean. Assume one trait observation per selected taxon, an independent Gaussian measurement-error variance \(\eta\ge 0\) shared by all taxa, and a fixed unit Brownian evolutionary variance per branch-length unit. An optimal subset minimizes the variance of the generalized least-squares root-mean estimator, equivalently maximizes
\[
I_S(\eta)=\mathbf1^{\mathsf T}(K_S+\eta I)^{-1}\mathbf1.
\]
For every rooted binary ultrametric tree with at most four tips and every fixed sample size \(1\le k\le n\), there is a subset that is optimal simultaneously for all \(\eta\ge0\). Five tips suffice to destroy this universal invariance: an explicit positive-edge-length, five-tip ultrametric tree with \(k=4\) has two disjoint sets of optimal taxon subsets on opposite sides of one strictly positive measurement-noise threshold. Thus five is the sharp minimum number of tips for a change of optimal subset driven solely by common measurement-error variance in this model.

## Assumptions and scope
The phylogenetic tree is rooted, fully binary, ultrametric, with strictly positive lengths on all its edges. The tree and all lengths are known. Let its root-to-tip height be \(H>0\). Conditional on an unknown fixed root value \(\mu\), the latent tip traits follow independent unit-variance Brownian increments on each evolutionary branch. For two tips, their evolutionary covariance equals their shared path length from the root to their most recent common ancestor. In particular, \(K_{ii}=H\). Measurement errors are independent across tips and from evolution, centered Gaussian with the same known variance \(\eta\ge0\). Exactly \(k\) different tips are measured once each; no taxon is measured repeatedly. The parameter \(\mu\) is the sole unknown in the information calculation, so \(I_S\) is the Fisher information for \(\mu\); the best linear unbiased estimator has variance \(1/I_S\). No Bayesian prior or estimation of branch lengths or measurement variance is involved.

For the five-tip construction, name the taxa \(A,B,C,D,E\). The root has two children: one is the ancestor of \(C,D\), reached along an edge of length \(50\), with two terminal edges of length \(5\). The other is the ancestor of \(A,B,E\), reached along an edge of length \(25\); its child \(B\) has a terminal edge of length \(30\), while its other child is the ancestor of \(A,E\), reached along an edge of length \(10\), with terminal edges of length \(20\). Every root-to-tip length equals \(55\). In tip order \((A,B,C,D,E)\), the covariance is
\[
K=\begin{pmatrix}
55&25&0&0&35\\
25&55&0&0&25\\
0&0&55&50&0\\
0&0&50&55&0\\
35&25&0&0&55
\end{pmatrix}.
\]

## Proof
**1. Universal nonswitching up through four tips.** For \(k=1\), every tip has the same observation variance \(H+\eta\), so every singleton is optimal. For \(k=n\), there is just one subset. For \(k=2\), a pair with shared ancestral path length \(a\) has covariance matrix \(\begin{psmallmatrix}H+\eta&a\\a&H+\eta\end{psmallmatrix}\), hence information \(2/(H+\eta+a)\). Choosing a pair with minimal \(a\) optimizes the information for every noise variance. These cases settle all choices for \(n\le3\) and all except \(n=4,k=3\).

Set \(D=H+\eta\). If the four-tip root split is \(2+2\), every three-tip subset contains a cherry from one root branch and one tip from the other. The two root branches are independent conditional on the fixed root state. Information is \(2/(D+a)+1/D\), with \(a\) the shared ancestral depth of the retained cherry. The same cherry minimizes \(a\) at every \(\eta\).

If the root split is \(1+3\), name the solitary root-child tip \(o\). A three-tip subset containing \(o\) has an independent observation with information \(1/D\) and a pair from the other root branch with information \(2/(D+a)\); thus the best such subset always pairs \(o\) with a least-correlated pair in the three-tip branch. It remains to exclude the three-tip subset that omits \(o\). For those three tips the covariance (after reordering so the last two form a cherry) has the shape
\[
\Sigma=\begin{pmatrix}D&a&a\\a&D&b\\a&b&D\end{pmatrix},\qquad 0\le a\le b<D.
\]
Direct inversion gives the **unnormalized** generalized least-squares weights
\[
\Sigma^{-1}\mathbf1=\frac{1}{D(D+b)-2a^2}
\begin{pmatrix}D+b-2a\\D-a\\D-a\end{pmatrix}.
\]
All three coordinates are strictly positive because \(D>b\ge a\ge0\), and the denominator is positive. Normalize the weights to sum to one. Replace any one of the three correlated tips by \(o\), leaving the same positive weights assigned to the two retained tips and to \(o\). All diagonal observation variances remain \(D\), the retained pair's covariance is unchanged, and both covariances touching the replacement tip fall from nonnegative values to zero. Its variance therefore cannot increase. Reoptimizing the GLS weights can only decrease that variance further. Consequently a best three-tip subset containing \(o\) exists for every \(\eta\), and the same pair of the other three tips minimizes \(a\) for all \(\eta\). This proves a common optimal subset for every \(n\le4\).

**2. The five-tip witness.** All five four-tip subsets are obtained by omitting one taxon. Write \(x=\eta\). For convenience, let \(L(x)\) be the information when omitting \(C\) or \(D\), \(R(x)\) when omitting \(A\) or \(E\), and \(M(x)\) when omitting \(B\). Direct inversion of the displayed covariance gives
\[
\begin{aligned}
L(x)&=\frac{2(2x^2+205x+4600)}{(x+55)(x^2+145x+3700)},\\
R(x)&=\frac{2}{x+105}+\frac{2}{x+80},\\
M(x)&=\frac{2}{x+105}+\frac{2}{x+90}.
\end{aligned}
\]
The formula for \(L\) can also be reconstructed from independent root branches: the three-tip branch has precision \(q=2/(x+40)+1/(x+30)\) at its internal branching node, a shared upstream segment of length \(25\) changes it to \(q/(1+25q)\), and the single tip from the other branch supplies \(1/(x+55)\). This equals the stated \(L(x)\).

The differences factor exactly as
\[
R(x)-M(x)=\frac{20}{(x+80)(x+90)}>0,
\]
and
\[
L(x)-R(x)=\frac{-10(2x^3+205x^2-1225x-198500)}{(x+55)(x+80)(x+105)(x^2+145x+3700)}.
\]
Every denominator is positive for \(x\ge0\). The cubic \(p(x)=2x^3+205x^2-1225x-198500\) has exactly one positive root: its coefficient sequence has one sign change, so Descartes' rule allows at most one, while \(p(0)<0\) and \(p(x)\to+\infty\) imply existence. Since \(p(29)=-12842\) and \(p(30)=3250\), the threshold \(x_*\) lies in \((29,30)\), with numerical value \(x_*\approx29.8018144905886\). Hence for \(0\le x<x_*\) only the two subsets omitting \(C\) or \(D\) are optimal. For \(x>x_*\) only the two subsets omitting \(A\) or \(E\) are optimal. At \(x=x_*\) these four subsets tie, while omitting \(B\) is always strictly suboptimal. The optimal families strictly change and are disjoint on either side, completing sharpness.

## Verification
The accompanying standalone `verify.py` uses exact symbolic inversion of all five \(4\times4\) principal submatrices of \(K+xI\) and verifies the three rational information formulas, both factorized differences, and exact signs at rational parameter values \(x=0,1,10,29,30,100,1000\). It also verifies all three coordinates of the inverse-covariance weight formula used for the four-tip argument. Descartes' rule and the covariance comparison constitute mathematical proofs beyond the tested parameter grid. Execute using `python verify.py` in an environment with SymPy installed.

## Relationship to prior work
Felsenstein (1985) formulated the Brownian phylogenetic comparative framework. Ives, Midford and Garland (2007) developed estimators allowing trait measurement error, including generalized least-squares ancestral-mean estimation. Ané (2008) explicitly discussed and numerically optimized tree-informed taxon subset selection for ancestral reconstruction under Brownian correlation, using effective sample size at zero separate measurement noise. Bartoszek (2015 preprint) likewise discusses mean effective sample size and incorporating measurement-error covariance by adding an error matrix. Those covariance formulas, the GLS estimator, and the broader taxon-selection motivation are prior results and are **not** claimed as new. The finding here is the exact **sharp five-tip onset of changes in optimal subset as independent measurement-error variance alone is varied**, accompanied by a concrete complete rational comparison and a four-tip impossibility proof. Searches did not identify a previously published statement of that threshold, but lack of a matching source is not a mathematical proof of novelty.

## Limitations
This is an exact theorem for known, ultrametric, fully binary trees with positive branch lengths and Gaussian Brownian traits, one observation per selected taxon, homogeneous independent measurement errors, and fixed sample size. It neither predicts empirical ancestral traits nor accounts for evolving measurement quality, within-species parameter estimation, phylogenetic uncertainty, nonlinear traits, or arbitrary optimal-design objectives. It proves sharp minimality but does not classify all five-tip topologies or the number of switches possible on larger trees. An equivalent theorem from general correlated-Gaussian experimental design or specialized phylogenetic design remains a literature-overlap risk. Numerical tests are corroborative, not a substitute for the all-parameter symbolic proof.

## References
- J. Felsenstein (1985), “Phylogenies and the Comparative Method,” *The American Naturalist* 125, 1–15. DOI: https://doi.org/10.1086/284325.
- A. R. Ives, P. E. Midford, T. Garland Jr. (2007), “Within-Species Variation and Measurement Error in Phylogenetic Comparative Methods,” *Systematic Biology* 56, 252–270. DOI: https://doi.org/10.1080/10635150701313830. Open author-hosted text: https://biology.ucr.edu/people/faculty/Garland/Ives_et_al_2007.pdf.
- C. Ané (2008), “Analysis of Comparative Data with Hierarchical Autocorrelation,” *Annals of Applied Statistics* 2, 1078–1102. DOI: https://doi.org/10.1214/08-AOAS173. Public preprint: https://arxiv.org/abs/0804.3166 (first submitted April 19, 2008).
- K. Bartoszek (2015 preprint; journal version 2016), “Phylogenetic effective sample size,” *Journal of Theoretical Biology* 407, 371–386. Public preprint: https://arxiv.org/abs/1507.07113 (first submitted July 25, 2015); journal DOI: https://doi.org/10.1016/j.jtbi.2016.06.026.
