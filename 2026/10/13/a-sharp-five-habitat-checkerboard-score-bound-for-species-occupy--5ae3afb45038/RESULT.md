# A sharp five-habitat checkerboard-score bound for species occupying exactly two sites
## Finding
In a binary species-by-site incidence matrix, suppose there are exactly five sites and \(s\ge2\) species, each present at exactly two sites. For species \(i\) and \(j\), write \(o_{ij}\) for their number of shared sites. Their classical Stone–Roberts number of checkerboard units is
\[
U_{ij}=(2-o_{ij})^2.
\]
Define the total and mean checkerboard scores as
\[
U=\sum_{i<j}U_{ij},
\qquad
C=\frac{U}{\binom{s}{2}}.
\]
Then the **sharp universal upper bounds** are
\[
\boxed{U\le\frac{12}{11}s^2},
\qquad
\boxed{C\le\frac{24s}{11(s-1)}}.
\]
Equality holds if and only if \(11\mid s\). If \(s=11t\) for an integer \(t\ge1\), then every equality pattern, after relabeling sites and species, has exactly four occupied site-pair types:
\[
\begin{array}{c|cccc}
\text{site pair}&\{1,2\}&\{3,4\}&\{3,5\}&\{4,5\}\\
\hline
\text{number of species}&5t&2t&2t&2t.
\end{array}
\]
All six other site-pair types are unused. There are exactly ten optimal occupancy multiplicity vectors when the five sites retain fixed labels, one for each possible choice of the first site pair.

For \(s=11\), the total is \(U=132\), and the classical average is \(C=12/5\). The most segregated arrangement is not built solely from mutually disjoint occupancy pairs: the three less frequent types intersect one another.

The four-site comparison has the lower ceiling \(U\le s^2\), with equality for even \(s\) when half the species occupy one site pair and half its disjoint complement. The five-site result is the first nontrivial increase beyond this two-block segregation pattern.

## Assumptions and scope
The incidence matrix has \(s\) *distinct* species as its rows and exactly five labeled habitats as its columns. Every row is binary with sum two. Species having identical occupancy patterns remain distinct species in the score calculation.

No column sums or habitat richnesses are fixed. Empty columns are allowed in the domain, but none occur in equality cases. The score is the unnormalized Stone–Roberts pairwise checkerboard-unit count and its ordinary mean over all unordered distinct species pairs. Some software offers a different normalized score by default; that variant is not being optimized here.

The sharp bound holds for **every** integer \(s\ge2\). Equality is characterized only for \(11\mid s\); the exact smaller strict maxima for other remainders are not asserted.

## Proof
Identify the five habitats with the vertices of a complete graph. Each species' two occupied sites form one of its ten edges. For each edge \(e\), let \(c_e\) count species with that occupancy type, so that
\[
\sum_e c_e=s.
\]
Two species with the same type contribute zero checkerboard units. For distinct edges, species contribute four units if the edges are disjoint and one unit if they intersect. Consequently
\[
U=\sum_{e<f}w_{ef}c_ec_f,
\qquad
w_{ef}=\begin{cases}4,&e\cap f=\varnothing,\\1,&|e\cap f|=1.\end{cases}
\]
With \(x_e=c_e/s\), the problem becomes the scale-free quadratic optimization
\[
\max_{x_e\ge0,\ \sum_e x_e=1}Q(x),
\qquad Q(x)=\sum_{e<f}w_{ef}x_ex_f.
\]
The ten edge types are the vertices of the Petersen disjointness graph; disjoint pairs have weight four, while all other distinct pairs have weight one.

We now give an *exact finite certificate* for the continuous optimization; it proves the bound for arbitrarily large integer species censuses. Let \(W\) be the symmetric ten-by-ten matrix with \(W_{ef}=w_{ef}\) when \(e\ne f\) and zeros on the diagonal. For every nonempty subset \(S\) of the ten types, a candidate with positive weights on exactly \(S\) must satisfy
\[
W_Sx=\lambda\mathbf1,
\qquad\mathbf1^{\mathsf T}x=1.
\]
If \(j\) is the last type in \(S\), the Hessian on the tangent hyperplane of this face has entries
\[
H_{ab}=W_{ab}-W_{aj}-W_{jb}+W_{jj},
\qquad a,b\in S\setminus\{j\}.
\]
At a strict interior maximum of that face, \(H\) must be negative definite. This is checked exactly using the alternating signs of all leading principal determinants. The stationary equations are then uniquely solvable over the rationals. All \(2^{10}-1=1023\) nonempty supports are checked by the embedded verifier, using integer Bareiss determinants and rational Gaussian elimination. The complete table of supports with negative-definite tangent Hessian and a positive stationary point is:

| Support size | Stationary value of \(Q\) | Number of supports |
| ---: | ---: | ---: |
| 1 | \(0\) | 10 |
| 2 | \(1/4\) | 30 |
| 2 | \(1\) | 15 |
| 3 | \(1/3\) | 30 |
| 3 | \(16/15\) | 30 |
| 4 | \(3/8\) | 5 |
| 4 | \(12/11\) | 10 |

No larger support has negative-definite tangent Hessian. The largest entry is \(12/11\).

For completeness, an arbitrary global maximum exists by compactness. If its restricted Hessian is singular rather than negative definite, the first-order conditions and a nonzero tangent null vector provide a line along which the quadratic form stays constant. Moving to a boundary endpoint strictly reduces its positive support without changing the maximum. Iterating produces a maximizing candidate in the finite table. Thus **no global maximum can exceed \(12/11\)**.

The ten winning candidates have an explicit common form under site relabeling:
\[
x_{12}=\frac5{11},
\quad x_{34}=x_{35}=x_{45}=\frac2{11},
\quad x_e=0\ \text{otherwise}.
\]
Its value is
\[
Q(x)=4\left(\frac5{11}\right)\left(\frac6{11}\right)+3\left(\frac2{11}\right)^2
=\frac{132}{121}=\frac{12}{11}.
\]
For each winning vector, \((Wx)_e=24/11\) on its four positive types, but \((Wx)_e=17/11\) on every zero type. This strict external gradient gap excludes any other maximizer with additional positive types: a flat direction reaching a winning boundary face from an additional type would have strictly negative first derivative. Together with strict concavity on each winning face, this proves the **complete equality classification**.

Since equality requires occupancy proportions with denominator eleven in lowest terms, an integer census achieves the bound only when \(11\mid s\). Conversely, for \(s=11t\) the stated integer multiplicities attain equality.

The same exact support method applied to three and four habitats gives maxima \(Q=1/3\) and \(Q=1\), respectively; for four habitats the three winning supports each consist of a pair of disjoint site pairs with equal weights. Therefore the five-site increase is strict and its four-type optimizer is structurally different.

## Verification
Run the complete standard-library certificate:

`python3 verify_checkerboard_five_sites.py`

The output must terminate with `VERIFY_OK`.

The certificate independently checks every one of 1,023 possible positive support sets for five habitats, solving all admissible stationary systems in exact rational arithmetic, checking all ten winning multiplicity patterns and the strict external gradient slack.

It also verifies the three- and four-habitat comparison and directly enumerates every integer occupancy-type multiset with two through eleven species. Across these ten census sizes it checks 352,705 multisets, computes all checkerboard sums as exact integers, verifies the quadratic identity in independent form in the smaller cases, and finds exactly ten optimal multiplicity vectors when \(s=11\).

## Relationship to prior work
Stone and Roberts (1990) introduced the exact pairwise checkerboard-unit formula and the matrix-wide average used here. Their full paper discusses constraints on species incidence matrices and gives a complete fixed-margins four-by-four example together with a larger twenty-by-twenty extremal illustration, but not the present five-habitat, uniform two-site occupancy optimization or a quadratic coefficient \(12/11\).

Gotelli (2000) compares null-model randomization algorithms and the statistical behavior of ecological co-occurrence indices. Heino (2013) applies the C-score to stream communities and explicitly emphasizes that raw values depend on matrix size. Neither analyzed source supplies a deterministic sharp upper bound for all species counts with five habitats and occupancy two.

The reduction to a weighted quadratic on the Petersen disjointness graph is related to classical graph-Lagrangian methods, but the ordinary Motzkin–Straus unweighted clique formula does not directly determine the mixed weights one and four or classify this extremal ecological incidence family. Targeted database and exact-constant searches found no statement covering the displayed sharp formula or equality classification.

## Limitations
The theorem fixes **five** habitats and **exactly two** occupied habitats per species. It allows site richnesses to vary. Fixing both row and column marginals, changing row occupancy, or allowing more habitat columns gives a different optimization problem.

The sharp real-proportion upper bound remains valid for species counts not divisible by eleven, but is then unattainable. Their integer-exact maxima are not classified by the theorem.

A high raw C-score does not by itself establish competitive exclusion or a statistically significant ecological mechanism: habitat heterogeneity, dispersal and the chosen null model remain important. The deterministic bound is a normalization and extremal-structure result, not a hypothesis test.

The primary metric source is from 1990 but has month-level date evidence; the day-resolved archive source used for temporal placement was first published on January 9, 2013.

## References
1. L. Stone and A. Roberts, “The checkerboard score and species distributions,” *Oecologia* **85** (1990), 74–79. DOI: 10.1007/BF00317345. Full article, pages 74–79, inspected.
2. N. J. Gotelli, “Null model analysis of species co-occurrence patterns,” *Ecology* **81** (2000), 2606–2621. DOI: 10.1890/0012-9658(2000)081[2606:NMAOSC]2.0.CO;2.
3. J. Heino, “Environmental heterogeneity, dispersal mode, and co-occurrence in stream macroinvertebrates,” *Ecology and Evolution* **3** (2013), 344–355. DOI: 10.1002/ece3.470. First published January 9, 2013.
4. B. Wu and Y. Peng, “The connection between polynomial optimization, maximum cliques and Turán densities,” *Discrete Applied Mathematics* **225** (2017), 114–121. DOI: 10.1016/j.dam.2017.03.014. Used only for generic graph-Lagrangian context, not the archived biological source.
