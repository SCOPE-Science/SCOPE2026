# Sharp Hilbert norm and rigidity of the centered maximal operator on the Petersen graph

## Finding

Write the Petersen graph as the Kneser graph \(KG(5,2)\): its ten vertices are the two-element subsets of \(\{1,2,3,4,5\}\), adjacent when disjoint. For the counting-measure centered graph-ball Hardy--Littlewood maximal operator \(M\) on real functions, the **sharp, attained strong Hilbert norm** is
\[
\boxed{\|M\|_{\ell^2\to\ell^2}=\sqrt{\lambda_*}=1.218268608940424\ldots},
\]
where \(\lambda_*\) is the unique root in \((1.484,1.485)\) of
\[
200\lambda^3-355\lambda^2+87\lambda-1=0.
\]

All nonzero extremizers are classified as follows. Choose distinct ground-set elements \(a,b\in\{1,2,3,4,5\}\), a positive scale, and arbitrary independent coordinate signs. After taking absolute values and normalizing the largest coordinate to one, set
\[
|f(\{a,c\})|=1\quad(c\notin\{a,b\}),\qquad
|f(\{a,b\})|=s_*,\qquad
|f(\{i,j\})|=t_*\quad(a\notin\{i,j\}),
\]
where, with \(D_*=200\lambda_*^2-81\lambda_*+1\),
\[
t_*={49\lambda_*-1\over D_*}=0.2232060800355\ldots,\qquad
s_*={24\lambda_*+3\over D_*}=0.1201856078060\ldots.
\]
These are exactly \(20\) distinct labeled nonnegative extremizing rays, one for each ordered pair \((a,b)\) with \(a\ne b\). The maximum is not attained by a point mass or a constant function.

## Assumptions and scope

The graph is simple and unweighted, edge lengths are one, vertex masses are one, and the norm uses the counting-measure \(\ell^2\) space. For every real \(f\) on the vertex set, define
\[
(Mf)(v)=\max_{r\in\{0,1,2\}}\frac{1}{|B(v,r)|}\sum_{w\in B(v,r)}|f(w)|.
\]
The Petersen graph is cubic and has diameter two, so the distinct ball sizes are \(1,4,10\). Results about other graphs, measures, radii or exponents are not implied.

## Proof

**Finite exact reduction.** For each radius assignment \(\rho:V\to\{0,1,2\}\), let \(A_\rho\) have row \(v\) equal to the normalized indicator of \(B(v,\rho(v))\). Since every entry is nonnegative, the pointwise choice of a maximizing radius gives
\[
\|Mf\|_2^2=\max_\rho\|A_\rho|f|\|_2^2,\qquad
\|M\|_{2\to2}^2=\max_\rho\lambda_{\max}(A_\rho^{\mathsf T}A_\rho).
\]
For the second identity, the top singular vector of a nonnegative matrix can be taken nonnegative (by replacing its entries with absolute values).

There are exactly \(3^{10}=59049\) assignments. Every permutation of the five underlying elements induces a graph automorphism; the resulting \(120\) permutations partition the radius assignments into \(792\) orbits. The standalone exact-arithmetic program `petersen_verifier.py` reconstructs those orbits without any graph or numerical library. It constructs the integer matrix \(B_\rho=20A_\rho\); the possible row entries are \(20\), \(5\), and \(2\). For precisely \(791\) orbit representatives it verifies, by fraction-free Sylvester elimination with integer division checked at every step, that
\[
2964I-5B_\rho^{\mathsf T}B_\rho\succ0.
\]
Therefore all \(59029\) corresponding assignments satisfy
\[
\lambda_{\max}(A_\rho^{\mathsf T}A_\rho)<\frac{741}{500}=1.482.
\]
The sole exceptional orbit has \(20\) members. These are exactly the assignments determined by distinct \(a,b\): radius zero on the three pairs containing \(a\) but not \(b\), radius two on \(\{a,b\}\), radius one on the three pairs containing \(b\) but not \(a\), and radius two on the other three pairs. No numerical spectral comparison is used in this exhaustive conclusion.

**The exceptional spectral value.** By permuting ground-set labels it suffices to consider one exceptional assignment. Write the input values as \(H=1\) on the three high pairs, \(T\) on the six pairs not containing \(a\), and \(S\) on the omitted pair \(\{a,b\}\). The selected output equals \(H\) at three vertices, \(q=(H+T)/2\) at three vertices, and \(\mu=(3H+6T+S)/10\) at four vertices. Consequently its squared Rayleigh ratio on this three-level family is
\[
\frac{3H^2+3q^2+4\mu^2}{3H^2+6T^2+S^2}.
\]
On the entire ten-dimensional space, direct inspection of the selected averaging rows shows that a three-level vector is an eigenvector of \(A_\rho^{\mathsf T}A_\rho\) with eigenvalue \(\lambda\) precisely when
\[
\lambda H=H+\frac25\mu+\frac12q,\qquad
\lambda T=\frac25\mu+\frac14q,\qquad
\lambda S=\frac25\mu.
\]
Set \(H=1\), \(T=(49\lambda-1)/D\), \(S=(24\lambda+3)/D\), \(D=200\lambda^2-81\lambda+1\). Substitution into the three equations reduces each identity to a multiple of \(200\lambda^3-355\lambda^2+87\lambda-1\). The verifier checks all three polynomial identities exactly, modulo this cubic.

The cubic changes sign between \(1484/1000\) and \(1485/1000\); its derivative \(600\lambda^2-710\lambda+87\) is strictly positive on that interval. The chosen root has \(0<S<T<H\). Every entry of \(A_\rho^{\mathsf T}A_\rho\) is strictly positive, because four selected rows average over the entire vertex set. Perron--Frobenius therefore makes this strictly positive eigenvector the unique top eigenvector up to scale. Its eigenvalue exceeds \(741/500\), proving that the \(20\) exceptional assignments are exactly the maximizing ones.

**Equality and radius activation.** Equality forces the chosen radius assignment into the exceptional orbit and forces \(|f|\) onto that assignment's unique top eigenray. The verifier checks by exact rational interval inequalities that the indicated radius at every vertex strictly beats the other two at the displayed eigenvector. Distinct ordered pairs \((a,b)\) yield distinct sets of three maximal coordinates and hence distinct rays. Since \(M\) depends only on \(|f|\), independent coordinate signs give every real extremizer.

## Verification

Run `python3 petersen_verifier.py` with Python 3 and its standard library. It produces `CERTIFICATE_OK selections=59049 automorphisms=120 orbits=792 strict=791 winning_orbit_size=20`. In particular it exhausts all assignments by explicit automorphism orbits, checks all strict positive-definiteness certificates using arbitrary-precision integers, identifies the exceptional orbit, verifies the cubic eigenvector identities over exact rational polynomials, isolates the root, and proves strict radius activation using rational interval estimates. The complete executable is included with this result; no separate dataset, package installation, solver or precomputed spectrum is needed.

## Relationship to prior work

Soria and Tradacete (arXiv:1410.6204, first posted 22 October 2014) introduced the finite-graph centered maximal-operator problem, established sharp \(\ell^p\) bounds in the range \(0<p\le1\), and treated small examples such as the four-cycle. González-Riquelme and Madrid (arXiv:2005.03146 and arXiv:2011.02630) obtained sharp strong \(\ell^2\) results for complete graphs and stars; their stated graph-specific results do not give the Petersen value or the present extremizer classification. Greenblatt's 2016 thesis studies dimensional asymptotics, including spherical maximal averages on Cartesian powers of the Petersen graph; the accessible abstract does not assert the present exact centered-ball norm. Its full text could not be inspected in the current source-access conditions, so the possibility of an overlooked equivalent calculation remains explicitly open. The exact cubic and the three-level equality pattern are the contribution claimed here; the finite-matrix reduction by itself is not claimed as new.

## Limitations

The conclusion concerns only the unweighted Petersen graph, counting measure, centered metric-ball averages and real strong \(\ell^2\) norm. There is no assertion about higher Kneser graphs, Cartesian powers, spherical rather than ball maximal operators, uncentered averages, weighted measures, or other exponents. Exhaustive arithmetic establishes the stated finite result but is not an independent scientific review. An unindexed equivalent calculation may exist, notably within related literature whose full text was inaccessible.

## References

1. J. Soria and P. Tradacete, *Best constants for the Hardy--Littlewood maximal operator on finite graphs*, arXiv:1410.6204v1 (22 October 2014), https://arxiv.org/abs/1410.6204.
2. C. González-Riquelme and J. Madrid, *Sharp inequalities for maximal operators on finite graphs*, arXiv:2005.03146 (initially 6 May 2020), https://arxiv.org/abs/2005.03146.
3. C. González-Riquelme and J. Madrid, *Sharp inequalities for maximal operators on finite graphs, II*, arXiv:2011.02630 (initially 5 November 2020), https://arxiv.org/abs/2011.02630.
4. J. S. Greenblatt, *Dimensional Asymptotics for Norms of Maximal Averaging Operators on Cartesian Powers of Finite Graphs*, doctoral dissertation (2016), https://escholarship.org/uc/item/16k3f6p1.
