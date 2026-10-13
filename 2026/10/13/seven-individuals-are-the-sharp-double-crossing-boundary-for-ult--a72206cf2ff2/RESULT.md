# Seven individuals are the sharp double-crossing boundary for ultrametric phylogenetic rarefaction
## Finding
For two finite communities on one fixed rooted ultrametric binary tree with exactly three taxa, expected rooted phylogenetic diversity under rarefaction can reverse the communities' strict ranking twice as sampling effort increases, even when all three taxa are present in both communities and both censuses have equal size.

Seven individuals is the **smallest possible total census** for such a double reversal. For every census \(3\le N\le6\), no two positive three-tip abundance profiles produce two strict sign changes at any real branch-length ratio allowed by ultrametricity.

For \(N=7\), up to separately swapping the two sister species within each abundance profile, **exactly three unordered profile pairs** admit double reversals. Let \(t=h/H\), where \(H\) is the root-to-tip height and \(h\) is the length of the shared sister-clade stem. Their complete parameter intervals are
\[
\begin{array}{c|c}
\text{profiles} & \text{exact parameter interval}\\\hline
(1,1,5)\ \text{versus}\ (3,3,1)&\frac12<t<\frac{13}{23}\\
(1,2,4)\ \text{versus}\ (3,3,1)&\frac17<t<\frac3{17}\\
(1,4,2)\ \text{versus}\ (3,3,1)&\frac15<t<\frac3{13}
\end{array}
\]
The endpoints are excluded: at an endpoint the relevant equality eliminates one of the strict sign changes, even when ties are omitted.

A fully explicit witness is the tree with \(H=9\), \(h=2\) and abundance profiles
\[
x=(1,4,2),\qquad y=(3,3,1).
\]
For integer sample sizes \(m=2,3,4,5,6\), the differences of their expected rooted phylogenetic diversities are exactly
\[
(P_m(x)-P_m(y))_{m=2}^{6}
=\left(\frac1{21},-\frac1{35},-\frac1{35},\frac17,\frac27\right).
\]
Thus the ranking has the strict sign pattern \(+,-,-,+,+\). For the same tree, both profiles have expectation \(9\) at sample size \(1\) and \(25\) at sample size \(7\).

## Assumptions and scope
The fixed tree has three tips labelled \(1,2,3\), with \(1\) and \(2\) sister tips. The internal branch from the root to their common ancestor has strictly positive length \(h\); each sister pendant edge has length \(H-h\); and the pendant outgroup edge has length \(H\), where
\[
0<h<H.
\]
Consequently all branches have strictly positive length, and the tree is ultrametric. Rooted phylogenetic diversity of a selected individual subsample means the sum of lengths of edges ancestral to at least one represented tip, with the root fixed.

Every abundance profile \(p=(a,b,c)\) consists of **strictly positive integers** summing to a common census \(N\). The outgroup's count is \(c\); counts \(a,b\) belong to the sister tips. A sample of exactly \(m\) distinct individuals is chosen uniformly among the \(\binom Nm\) possible subsets, without replacement.

Two profiles are considered equivalent as *expected-PD curve types* if they differ by interchanging the sister counts. Thus \((a,b,c)\) is canonically recorded with \(a\le b\); the outgroup count is never interchangeable with a sister count. For comparisons, the two profiles may each undergo their own sister-tip swap because expected rooted PD is invariant under it. This describes curve-type equivalence, not physical equivalence of independently labelled community data.

A **double strict reversal** means the sequence of signs of the expectations' difference over integer sample sizes \(2,\ldots,N-1\), with all zero signs omitted, contains at least two changes. This includes the possibility of ties at some depths but does not treat resolving a tie as a strict reversal.

## Proof
For integers \(0\le m\le N\), set
\[
Q_m(z)=\binom{N-z}{m},
\]
with \(\binom{u}{m}=0\) when \(u<m\). A branch subtending exactly \(z\) censused individuals is missed by a uniform sample of \(m\) individuals with probability
\[
\frac{Q_m(z)}{\binom Nm}.
\]
The four branches subtend \(a\), \(b\), \(c\), and \(a+b\) individuals, with respective lengths \(H-h\), \(H-h\), \(H\), and \(h\). Therefore
\[
P_m(a,b,c)=3H-h-
\frac{(H-h)[Q_m(a)+Q_m(b)]+H Q_m(c)+h\binom cm}{\binom Nm}.
\]
Define the two integer quantities
\[
A_m(p)=Q_m(a)+Q_m(b)+Q_m(c),
\qquad
B_m(p)=\binom cm-Q_m(a)-Q_m(b).
\]
Factoring out \(H\) and writing \(t=h/H\) yields the exact affine law
\[
\frac{P_m(x)-P_m(y)}{H}
=-\frac{\big[A_m(x)-A_m(y)\big]+t\big[B_m(x)-B_m(y)\big]}{\binom Nm}.
\]
For each fixed pair and depth, the sign is therefore determined by a rational affine function of the **single** real parameter \(t\in(0,1)\). Its sign can change only at a rational root. It suffices to check all open cells between the finitely many roots, and each interior root itself, to classify signs for *all real* \(t\) rather than a grid of branch lengths.

The finite census is exhaustive: for each \(N\in\{3,4,5,6,7\}\), generate every integer \(a,b,c\ge1\) with \(a+b+c=N\) and \(a\le b\). The respective numbers of canonical profiles are \(1,2,4,6,9\). These counts and every profile are independently reproduced by enumerating all ordered positive integer compositions and taking \((\min(a,b),\max(a,b),c)\). For each \(N\), compare every unordered distinct pair of canonical profiles; the total number of pairs is
\[
\binom12+\binom22+\binom42+\binom62+\binom92=58.
\]
For each pair, form the affine coefficients at every \(2\le m\le N-1\), enumerate all roots in \((0,1)\), and check the sign sequence at one exact rational point per open root cell and at each interior root. In total there are \(116\) parameter-cell and root tests. No pair with \(N\le6\) has two strict sign changes. At \(N=7\), precisely the three unordered profile pairs stated above have double reversals.

A human-checkable coefficient certificate for the three positive cases is as follows. Listing \((A_m(x)-A_m(y),B_m(x)-B_m(y))\) in order for \(m=2,3,4,5,6\), the lists are
\[
\begin{aligned}
(1,1,5),(3,3,1):\;&(4,-8),(12,-22),(13,-23),(6,-11),(1,-2),\\
(1,2,4),(3,3,1):\;&(1,-7),(3,-18),(3,-17),(1,-7),(0,-1),\\
(1,4,2),(3,3,1):\;&(1,-5),(3,-13),(3,-13),(1,-6),(0,-1).
\end{aligned}
\]
These yield respectively exactly the root intervals \((1/2,13/23)\), \((1/7,3/17)\), and \((1/5,3/13)\) by elementary sign comparison; equality at an endpoint removes the second strict sign change. The verifier checks each coefficient list directly.

For the last pair at \(t=2/9\), the coefficient signs at successive depths are \((- ,+,+,-,-)\), and the displayed affine law reverses these signs to \((+,-,-,+,+)\) for PD differences. Evaluating with \(H=9\) gives the exact stated fractions, proving attainability and sharpness.

## Verification
The accompanying self-contained `verify_pd_double.py` uses only the Python 3 standard library. It generates the finite profile census in two independent ways; computes the integer affine coefficients for every pair and interior sample depth; partitions \((0,1)\) at all exact rational coefficient roots; and checks a rational representative of every open interval as well as all interior root points.

It verifies the complete first layer, including all three open parameter intervals and the absence of double crossings through \(N=6\). It also independently sums rooted phylogenetic diversity over **every individual subset** at each sample size for every profile through \(N=7\), comparing the result to the edge-coverage formula at \(H=9,h=2\). This supplies \(130\) direct-subset checks and independently checks the final witness differences.

Run with `python3 verify_pd_double.py`; the first output line is `VERIFY_OK`. The census and parameter sweep are exact and finite, and no floating-point comparisons are used. These experiments are not extrapolated to \(N>7\).

## Relationship to prior work
Nipperess and Matsen's work gives exact formulas for the mean and variance of phylogenetic diversity under rarefaction. It also shows how standardizing sampling effort can change rankings of biological assemblages. Their work was publicly available as arXiv:1208.6552 from 31 August 2012, before its journal publication.

Chao, Chiu, Hsieh, Davis, Nipperess, and Faith develop phylogenetic diversity accumulation, rarefaction, and extrapolation curves for comparing assemblages, including ultrametric rooted trees. Their work establishes the practical and mathematical setting in which sampling-depth-dependent rankings matter.

Those checked sources motivate the calculation but do not state the exact minimum three-tip census for *two* strict ranking reversals under a shared ultrametric tree, nor the complete three-pair first layer and its sharp branch-length intervals. The new result is deliberately restricted to that finite boundary and does not claim novelty for rarefaction formulas or for ranking changes in general.

## Limitations
The bound concerns exactly three present taxa, a **shared ultrametric tree**, strictly positive finite integer counts, equal total census, and **uniform individual-based sampling without replacement**. It is not an assertion about other tree topologies, non-ultrametric branch lengths, different census sizes, incidence rarefaction, extrapolation, or stochastic variability around expected PD.

The full census and exact parameter-cell check prove the minimum through \(N=7\). They do not classify larger censuses or give a universal bound on the number of strict reversals beyond this first layer.

Although relevant full-text articles were inspected, their separately hosted supplementary derivations were not all accessible. Equivalent older examples or obscure supplementary data could reduce the originality claim; no independent external audit has been carried out.

## References
1. D. A. Nipperess and F. A. Matsen IV, “The mean and variance of phylogenetic diversity under rarefaction,” first publicly posted 31 August 2012, arXiv:1208.6552. Journal version: *Methods in Ecology and Evolution*, DOI: 10.1111/2041-210X.12042. https://arxiv.org/abs/1208.6552
2. A. Chao, C.-H. Chiu, T. C. Hsieh, T. Davis, D. A. Nipperess, and D. P. Faith, “Rarefaction and extrapolation of phylogenetic diversity,” *Methods in Ecology and Evolution* 6, 380–388 (2015), first online 11 August 2014. DOI: 10.1111/2041-210X.12247. https://doi.org/10.1111/2041-210X.12247
3. *Mathematics Subject Classification 2020*, entry 92D40, Ecology.
