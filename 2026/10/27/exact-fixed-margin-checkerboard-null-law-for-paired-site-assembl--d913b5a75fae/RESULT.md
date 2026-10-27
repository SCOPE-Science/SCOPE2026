# Exact fixed-margin checkerboard null law for paired-site assemblages

## Finding

Consider an incidence matrix for \(n\) named species and \(m=3n/2\) named sites, where \(n\ge2\) is even, every species occupies exactly three sites, and every site supports exactly two species. Under the **uniform fixed-margin null** (each admissible binary incidence matrix equally likely), the Stone–Roberts mean checkerboard score has an exact all-size probability generating function and finite, nonasymptotic tail probabilities. In particular, four species and six sites are the smallest admissible design in this family permitting strict significance at the conventional one-sided \(5\%\) upper tail.

Let \(s_{ij}\) be the number of sites shared by distinct species \(i,j\), \(Q=\binom n2\), and
\[
C=\frac1Q\sum_{i<j}(3-s_{ij})^2,\qquad B=\sum_{i<j}\binom{s_{ij}}2.
\]
Then for every admissible matrix,
\[
QC=9Q-5m+2B.
\]
The complete null law of \(B\) is
\[
\mathbb E[u^B]=\frac{W_n(u)}{W_n(1)},
\qquad W_n(u)=[x_1^3\cdots x_n^3]\prod_{i<j}\left(1+x_ix_j+\frac{u}{2}x_i^2x_j^2+\frac{u^3}{6}x_i^3x_j^3\right).
\]
In the first nontrivial four-species design, \(C\) has values \(4,14/3,6\) with exact probabilities \(12/31,18/31,1/31\), respectively. Consequently an observed score \(C=6\) has exact inclusive upper-tail null probability \(1/31<1/20\); in the two-species design the score is deterministic and cannot have a strict upper-tail probability below \(1/20\). No assertion is made for alternative margins, nonuniform nulls, or causal species competition.

## Assumptions and scope

A binary \(n\times m\) matrix has rows indexed by distinct species and columns indexed by distinct sites. Every row sums to \(3\), and every column sums to \(2\). Thus \(n\) must be even and \(m=3n/2\). Matrices are labeled, not quotiented by row or column relabelings. The null law is uniform on all labeled matrices satisfying these margins. The C-score is the **unnormalized Stone–Roberts mean over unordered species pairs**; no alternative package-specific C-score normalization is used. The test tail is inclusive: \(P(C_{\rm null}\ge C_{\rm observed})\). A strict rejection means this probability is less than \(0.05\), not less than or equal.

## Proof

Represent each site by the unordered pair of species present there. There are \(m\) labeled pairs, repetition allowed, and every species has total pair incidence exactly \(3\). Write \(s_{ij}\in\{0,1,2,3\}\) for the multiplicity of the pair \(\{i,j\}\). Each site contributes to exactly one pair, so \(\sum_{i<j}s_{ij}=m\). Also \(s_{ij}^2=s_{ij}+2\binom{s_{ij}}2\). Expanding the checkerboard score gives
\[
QC=9Q-6\sum_{i<j}s_{ij}+\sum_{i<j}s_{ij}^2
=9Q-5m+2\sum_{i<j}\binom{s_{ij}}2,
\]
proving the affine statistic identity.

Fix an unordered pair of species. It may occupy \(k\in\{0,1,2,3\}\) sites, contributing degree \(k\) to each endpoint, \(\binom{k}{2}\) to \(B\), and \(1/k!\) to the weight for distributing labeled sites among unordered pairs. These are exactly the four terms in the displayed factor of \(W_n(u)\). Extracting the coefficient \([x_1^3\cdots x_n^3]\) enforces all species row degrees. Multiplication by \(m!\) assigns the site labels, so the number of null matrices with \(B=b\) is exactly \(m![u^b]W_n(u)\). Dividing by \(m!W_n(1)\) proves the generating-function identity, including the correct uniform labeled-matrix weighting.

For \(n=2\), both species occur in all three sites: exactly one labeled matrix exists, with \(s_{12}=3\), \(C=0\), and null upper-tail probability \(1\).

For \(n=4\), associate the six possible species pairs with edges of a four-vertex loopless multigraph, in which each vertex has degree \(3\). The degree equations force opposite edge multiplicities to agree. Thus the six multiplicities occur in three opposite pairs, say with values \(a,b,c\), where \(a,b,c\ge0\) and \(a+b+c=3\). Up to permuting the three opposite pairs, the only possibilities are \((1,1,1)\), \((2,1,0)\), and \((3,0,0)\). They have respectively \(B=0,2,6\). The numbers of labeled-site matrices are
\[
6!=720,\qquad 6\frac{6!}{2!2!}=1080,\qquad 3\frac{6!}{3!3!}=60.
\]
The total is \(1860\), giving \(P(B=0,2,6)=(12,18,1)/31\) in that order. Since \(Q=m=6\), the affine score identity yields \(C=4+B/3\). Only the uppermost score has one-sided upper-tail probability below \(0.05\): \(60/1860=1/31\). No smaller admissible \(n\) than \(4\) can do so, because \(n\) is positive even and \(n=2\) is degenerate. This proves the asserted sharp threshold.

## Verification

The dependency-free `verify.py` implements an exact integer dynamic program for the all-size coefficient formula. It returns the full \(B\)-frequency tables for \(n=2,4,6,8\), multiplying coefficient weights by \(m!\) exactly. Separately, for \(n=4\), it enumerates all \(6^6=46{,}656\) ordered six-site assignments of species pairs, retains those satisfying all row margins, and directly computes \(B\). The two methods produce exactly \(720,1080,60\) matrices at \(B=0,2,6\) and the same total \(1860\). The machine-readable output is `certificate.json`; execute `python3 verify.py` from this package and compare its stdout to `certificate.json`. These finite checks supplement, but do not replace, the all-\(n\) coefficient argument and the hand-counted four-species proof.

## Relationship to prior work

Stone and Roberts (1990) defined the C-score as the mean checkerboard units per species pair, using \((r_i-s_{ij})(r_j-s_{ij})\), and explicitly counted a different tiny design: \(4\times4\) incidence matrices with all row and column sums \(2\). Gotelli (2000) compared co-occurrence nulls and discussed the performance of the C-score. Artzy-Randrup and Stone (2005) analyzed sampling uniformly from fixed-margin incidence matrices and demonstrated Monte Carlo sampling biases. These works motivate the present **exact finite uniform null law for the all-\(3\)-by-\(2\) margin family**, rather than establishing that law or its sharp four-species \(5\%\) threshold. Tishby et al. (2023) treat cycle counts in degree-two regular graphs; their degree-two cycle model is not the cubic species-pair multigraph arising from these margins. The present claim does not assert novelty of the C-score, fixed-margin sampling, or generic coefficient enumeration methods.

## Limitations

The assumption that all labeled incidence matrices with the specified margins are equiprobable is a statistical null, not an ecological mechanism. A significant C-score does not imply competition or identify causes of species segregation. The smallest detectable size is specific to every species occupying three sites, every site containing two species, and the strict inclusive-tail \(5\%\) rule. The generating function is exact but can require exponential-time computation as \(n\) grows. The four-species class is not evidence of empirical power in noisy field data. An equivalent specialized calibration may have been published under graph-multigraph terminology not detected in the surveyed literature.

## References

- L. Stone and A. Roberts, "The checkerboard score and species distributions," *Oecologia* **85** (1990), 74–79. DOI: 10.1007/BF00317345.
- N. J. Gotelli, "Null model analysis of species co-occurrence patterns," *Ecology* **81** (2000), 2606–2621. DOI: 10.1890/0012-9658(2000)081[2606:NMAOSC]2.0.CO;2. First published 2000-09-01.
- Y. Artzy-Randrup and L. Stone, "Generating uniformly distributed random networks," *Physical Review E* **72** (2005), 056708. DOI: 10.1103/PhysRevE.72.056708.
- I. Tishby, O. Biham, E. Katzav, and R. Kühn, "The distribution of the number of cycles in directed and undirected random regular graphs of degree 2," *Physical Review E* **107** (2023), 024308. arXiv:2301.03686.
