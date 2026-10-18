# A four-to-five-neighbour void transition in three-row triangular bootstrap tubes

## Finding

For each integer \(n\ge4\), let \(T_n\) be the six-regular triangular toroidal strip with vertex set \(\mathbb Z/n\mathbb Z\times\mathbb Z/3\mathbb Z\) and the six neighbours of \((i,r)\) given by
\[
(i,r\pm1),\quad (i\pm1,r),\quad(i-1,r+1),\quad(i+1,r-1),
\]
where both coordinates are reduced modulo their respective periods. For \(t\in\{4,5\}\), a binary occupation configuration is *\(t\)-frozen* if every occupied vertex has at least \(t\) occupied neighbours. Let \(Z_{n,t}\) count all frozen configurations, including the empty configuration.

There are explicit finite integer matrices \(M_4\) and \(M_5\), of orders \(31\) and \(7\), respectively, constructed below such that for every \(n\ge4\),
\[
Z_{n,4}=\operatorname{tr}(M_4^n),\qquad
Z_{n,5}=1+\operatorname{tr}(M_5^n).
\]
The characteristic polynomials factor exactly as
\[
\begin{aligned}
\det(xI-M_4)&=x^7(x-1)P_9(x)P_{14}(x),\\
P_9(x)&=x^9-3x^8-10x^6+12x^5+12x^4+8x^3-14x^2+3x-1,\\
P_{14}(x)&=x^{14}-x^{13}-5x^{11}+6x^{10}-x^9+10x^8-11x^7+x^6\\
&\hspace{1cm}-8x^5+7x^4+6x^3-3x^2+1,\\
\det(xI-M_5)&=x^4(x^3-x^2-3).
\end{aligned}
\]
In particular, if \(\alpha_4\) is the unique zero of \(P_9\) in \((3.45417,3.45418)\) and \(\alpha_5\) is the unique real root greater than one of \(x^3-x^2-3=0\), then the frozen-state entropies per vertex are exactly
\[
\lim_{n\to\infty}\frac{\log Z_{n,t}}{3n}=\frac{\log\alpha_t}{3}
\quad(t=4,5).
\]
Numerically, these are \(0.41319452106981\ldots\) at threshold four and \(0.20752242057033\ldots\) at threshold five.

The change of threshold has a qualitative geometric effect. Every nonempty five-frozen configuration has either three occupied sites in a column or two occupied sites in a column; a two-occupied column (one vacancy) must be separated from every other such column by at least two completely occupied columns, in both cyclic directions. Conversely, every configuration of this form is five-frozen. Thus the five-frozen states are the empty state together with a three-colour, range-two hard-core gas of column vacancies. Four-frozen configurations, by contrast, have a positive limiting fraction of *entirely empty* columns when sampled uniformly among frozen configurations:
\[
\lim_{n\to\infty}\mathbb P_{n,4}\{\text{specified column empty}\}
=0.00833835118453\ldots>0.
\]
For five-frozen configurations the corresponding limit is zero, because only the globally empty state contains an empty column.

For \(X_{n,t}\), the number of occupied sites under the uniform distribution on the \(t\)-frozen states, the density converges in probability:
\[
\frac{X_{n,4}}{3n}\longrightarrow0.79694874568908\ldots,\qquad
\frac{X_{n,5}}{3n}\longrightarrow
1-\frac{\alpha_5-1}{3(3\alpha_5-2)}
=0.91982940995172\ldots.
\]
For reference, the exact pairs \((Z_{n,4},Z_{n,5})\) for \(n=4,5,6,7\) are \((151,14)\), \((455,17)\), \((1754,47)\) and \((5997,86)\).

## Assumptions and scope

The graph is simple, labelled and periodic in both coordinates; \(n\ge4\) prevents ambiguities in interpreting left and right columns. The culling rule deletes any occupied vertex with fewer than \(t\) occupied neighbours and repeats until stable. Fixed points are exactly the configurations satisfying the stated local condition; their uniform distribution is **not** the distribution obtained by culling Bernoulli initial states. Counts include configurations with no occupied sites. No bulk two-dimensional percolation threshold or temporal relaxation rate is claimed.

## Proof

Identify a column with its three-bit mask \(b\in\{0,\ldots,7\}\), with occupied-row set \(\{r:b_r=1\}\). For consecutive masks \((a,b,c)\), let \(F_t(a,b,c)=1\) precisely when for each \(r\) with \(b_r=1\),
\[
\sum_{s\ne r}b_s+a_r+a_{r+1}+c_r+c_{r-1}\ge t,
\]
with row indices modulo three. This is the exact number of occupied neighbours of \((i,r)\); hence a cyclic word \(b_0,\ldots,b_{n-1}\) is frozen if and only if \(F_t(b_{i-1},b_i,b_{i+1})=1\) for every column index modulo \(n\).

Construct a finite directed graph on the \(64\) ordered pairs \((a,b)\) of masks, with an arrow \((a,b)\to(b,c)\) if \(F_t(a,b,c)=1\). Closed walks of length \(n\) are in bijection with labelled frozen cyclic column words, so \(Z_{n,t}=\operatorname{tr}(A_t^n)\), where \(A_t\) is this explicit \(64\)-by-\(64\) zero-one adjacency matrix. This bijection holds for every \(n\ge4\); it does not infer all-length statements from enumeration of small periods.

Exhaustive checking of the \(512\) possible column triples, followed by strongly-connected-component decomposition, gives exactly one cycle-bearing component for threshold four: \(31\) states and \(79\) internal arrows. Every other component is a loopless singleton. The restricted matrix is \(M_4\). At threshold five there are exactly two cycle-bearing components: the isolated all-zero self-loop \((0,0)\), and a \(7\)-state component containing \(10\) arrows, with states
\[
(7,7),(7,3),(3,7),(7,5),(5,7),(7,6),(6,7).
\]
The latter defines \(M_5\). Its arrows are \((7,7)\to(7,7)\), \((7,7)\to(7,u)\to(u,7)\to(7,7)\) for each \(u\in\{3,5,6\}\); thus a vacancy column has three row choices and consecutive vacancy columns are cyclically separated by at least three columns. The only other frozen configuration is the all-zero one. These finite computations are reproduced exactly in `triangular_tube_verify.py`, which constructs all states and arrows from the six-neighbour rule rather than assuming the component lists.

Forming the two restricted integer matrices and computing their characteristic polynomials gives the displayed exact factorizations. Each restricted directed graph is strongly connected and has a self-loop, so its matrix is primitive. The Perron root \(\alpha_4\) is rigorously bracketed by the Collatz--Wielandt inequalities applied to \(M_4^{30}\mathbf1\):
\[
3.4541746409<\alpha_4<3.4541747640.
\]
Sturm root counts show that \(P_9\) has exactly one real root and \(P_{14}\) has none in the enclosing interval \((3.45417,3.45418)\). The Perron root therefore belongs to \(P_9\). For \(M_5\) the characteristic cubic has a unique positive root greater than one. Perron--Frobenius dominance then proves both entropy limits.

For occupation statistics, put weight \(z^{\operatorname{popcount}(c)}\) on each arrow \((a,b)\to(b,c)\) and call the corresponding restricted matrices \(M_t(z)\). The occupation generating polynomials are precisely \(\operatorname{tr}(M_4(z)^n)\) and \(1+\operatorname{tr}(M_5(z)^n)\). Since both matrices are primitive at \(z=1\), their simple Perron eigenvalues \(\alpha_t(z)\) are analytic near \(1\) and dominate the traces uniformly. Therefore the mean occupation is \(n\alpha_t'(1)/\alpha_t(1)+O(1)\), its variance is \(O(n)\), and the occupation fraction converges in probability by Chebyshev's inequality. For threshold five, the vacancy activity is three and its pressure root solves \(\alpha^3-\alpha^2-3=0\); implicit differentiation yields vacancy-columns-per-column \((\alpha_5-1)/(3\alpha_5-2)\), proving the exact stated density.

For threshold four, write \(l,r\) for strictly positive left/right Perron vectors of \(M_4\), normalized so \(l^\mathsf T r=1\). The limiting occupation fraction is
\[
\frac13\sum_{(a,b)}l_{a,b}r_{a,b}\operatorname{popcount}(b),
\]
and the probability of an entirely empty column is
\[
\sum_{(a,0)}l_{a,0}r_{a,0}.
\]
Both are exact algebraic quantities defined by the explicit integer matrix, with the reported decimal values obtained by numerical eigensolution. The empty-column sum is strictly positive because the primitive component contains \((0,0)\) and \((7,0)\). For threshold five, an empty column occurs only in the all-zero configuration and hence has uniform probability \(1/Z_{n,5}\to0\).

## Verification

The included standalone program `triangular_tube_verify.py` reconstructs the finite directed graphs and strongly connected components from the local criterion; checks both characteristic-polynomial identities symbolically; and computes a rational Collatz--Wielandt bracket and exact Sturm root counts. Independently it builds the physical six-neighbour graph directly from site coordinates, exhausts all \(2^{3n}\) binary occupations for \(n=4,5,6\) at both thresholds, and compares these counts with transfer-matrix traces. The threshold-five hard-core classification is independently enumerated for these sizes and length seven. The program then reports Perron eigenvalues and the occupation/empty-column constants. The exhaustive checks support the algebraic certificate but are not substituted for the all-length transfer bijection.

## Relationship to prior work

Kogut and Leath studied bootstrap culling on square, triangular and cubic lattices by simulation in 1981 (DOI 10.1088/0022-3719/14/22/013). Their accessible abstract describes bulk critical behaviour, not periodic width-three fixed-state counting. Choi and Yu, *Newman-Ziff algorithm for the bootstrap percolation: application to the Archimedean lattices* (arXiv:1903.01595, 2019), §§1--3, study bulk transition thresholds and finite-size scaling on the triangular lattice; their triangular examples and Table 1 do not provide the present frozen-configuration transfer polynomials. Chang and Shrock, *Ground State Entropy of the Potts Antiferromagnet on Triangular Lattice Strips* (arXiv:cond-mat/0004129, 2000), §§1--4, study width-three triangular toroidal strips but enumerate **proper colourings** (chromatic polynomials), not occupancy sets stable under neighbour pruning; this is not a stronger result on the same statistic.

A separate square-lattice three-row, three-neighbour culling count concerns the graph without diagonal bonds and does not determine these six-regular triangular-strip counts. In fact, the four-column mask word \((1,5,7,3)\) obeys triangular threshold-four stability but not square threshold-three stability. Merely reusing a transfer-matrix method does not make the two enumerations equivalent. No claim is made that targeted searches prove priority over every unindexed source.

## Limitations

The 1981 Kogut--Leath article's full text could not be inspected, and an unindexed finite-width frozen-state table remains a genuine bibliographic risk. Only the paper's abstract and bibliographic description were checked. The exact public calendar day for that older paper was not established; the supplied archival date is the documented first arXiv posting day of the directly inspected 2000 triangular-strip geometry paper, not an invented earlier day. Numerical values are approximations to matrix-defined algebraic constants. The theorem applies only to a fixed circumference of three, with periodicity in both directions, and concerns uniform fixed-point counting rather than dynamical basin sizes or the infinite planar critical point.

## References

1. P. M. Kogut and P. L. Leath, "Bootstrap percolation transitions on real lattices," *Journal of Physics C* **14** (1981), 3187--3194. DOI: 10.1088/0022-3719/14/22/013.
2. S.-C. Chang and R. Shrock, "Ground State Entropy of the Potts Antiferromagnet on Triangular Lattice Strips," first public arXiv version 2000-04-10, arXiv:cond-mat/0004129, especially §§1--4.
3. J.-O. Choi and U. Yu, "Newman-Ziff algorithm for the bootstrap percolation: application to the Archimedean lattices," arXiv:1903.01595v1, 2019-03-05, especially §§1--3 and Table 1.
