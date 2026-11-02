# Four-season ecological growth has an exact temporal-order reversal at half dispersal

## Finding

For a two-patch, density-independent seasonal population with common symmetric dispersal, the cyclic order of four prescribed seasonal growth profiles has a complete, sharp, parameter-independent ranking. Label the seasons so that their relative patch-fitness ratios obey \(a_1/b_1<a_2/b_2<a_3/b_3<a_4/b_4\). Let \(R_\sigma\) denote the four-step Perron multiplier for the cyclic order \(\sigma\). For \(0<m<1/2\),

\[
R_{1243}>R_{1234}>R_{1324}.
\]

For \(1/2<m<1\) both inequalities reverse. Every one of the twenty-four permutations is cyclically or reversally equivalent to exactly one of these three orders. At \(m=1/2\), all orders tie. Every order of up to three arbitrary positive seasonal profiles is spectrally equivalent under rearrangement, so four seasons are the smallest cycle length permitting this effect in this model. The complete trace-difference identities below also determine all ties when fitness ratios coincide.

For an exact rational example, the temporal order alone changes whether the linear population increases or decreases over one cycle, with every seasonal profile and the dispersal rate held fixed.

## Assumptions and scope

Time is discrete with nonoverlapping generations. Abundance is a nonnegative two-coordinate column vector, with coordinates representing two fixed habitat patches. In each season \(i\), local per-capita reproduction/survival is \(D_i=\operatorname{diag}(a_i,b_i)\), where \(a_i,b_i>0\). After local growth, the same fraction \(m\in(0,1)\) of offspring switches patches, symmetrically, using

\[
M_m=\begin{pmatrix}1-m&m\\m&1-m\end{pmatrix}.
\]

The environment repeats exactly four seasons, but their order is selectable without changing their multiset or duration. The step map is \(M_mD_i\). A cyclic order \(\sigma\) has chronological four-step matrix \(P_\sigma=(M_mD_{\sigma_4})\cdots(M_mD_{\sigma_1})\). Set \(R_\sigma=\rho(P_\sigma)\); its asymptotic per-season log growth is \(\frac14\log R_\sigma\). The objective is this density-independent growth/invasion multiplier, not equilibrium abundance or evolutionary stability of a density-dependent system. By transposition and cyclic trace invariance, reversing a chronological order preserves its multiplier.

For arbitrary positive profiles, define \(\Delta_{ij}=a_i b_j-a_j b_i\), \(c_m=m^2(1-2m)\), and \(T_\sigma=\operatorname{tr}(P_\sigma)\). The three representative trace differences obey exactly

\[
\begin{aligned}
T_{1234}-T_{1324}&=c_m\Delta_{14}\Delta_{23},\\
T_{1234}-T_{1243}&=-c_m\Delta_{12}\Delta_{34},\\
T_{1324}-T_{1243}&=-c_m\Delta_{13}\Delta_{24}.
\end{aligned}
\]

These identities hold with no ordering restriction on the ratios. The strict ranking in the finding requires four distinct ratios, labeled in increasing order. At \(m=1/2\) the matrix has rank one and \(R_\sigma=\prod_{i=1}^4(a_i+b_i)/2\). The no-dispersal endpoint \(m=0\), not included in the theorem's strict ranges, is also order-independent.

## Proof

**1. All four-step determinants coincide.** The determinant of a step is \(\det(M_mD_i)=(1-2m)a_ib_i\). Therefore every four-step product has the same determinant

\[
\delta=(1-2m)^4\prod_{i=1}^4 a_i b_i\geq0.
\]

For \(m\ne1/2\) this is positive. Because each four-step product has strictly positive entries when \(0<m<1\), its eigenvalues are real and unequal: the discriminant equals the square of the difference of diagonal entries plus four times the product of positive off-diagonal entries. Its dominant eigenvalue is

\[
R_\sigma=\frac{T_\sigma+\sqrt{T_\sigma^2-4\delta}}{2}.
\]

At fixed \(\delta\), this is strictly increasing in \(T_\sigma\) on the physical domain. The same conclusion also holds at \(\delta=0\), when \(R_\sigma=T_\sigma\).

**2. Cyclic and reversal symmetries.** Cyclically shifting the four factors preserves trace and determinant, hence the spectrum. Since each \(D_i\) and \(M_m\) is symmetric, transposing a factor product and then cyclically shifting identifies the reversed order and gives the same trace. Rotations and reversals of a four-cycle partition its twenty-four permutations into exactly three classes represented by \(1243,1234,1324\). For cycles of length at most three, rotations and reversals already connect *every* permutation. Thus all their possible orders have identical traces and determinants, proving the minimal-cycle assertion.

**3. Exact four-season comparison.** Expand

\[
\operatorname{tr}(D_1M_mD_2M_mD_3M_mD_4M_m)
\]

as the sum over all sixteen cyclic sequences of the two habitat indices. Group terms according to which of the four dispersal transitions switch habitats. Terms with zero switches are identical in every ordering. Terms with two and four switches pair under reversal; subtracting the three representative orders and factoring gives exactly the three displayed identities with \(c_m=m^2((1-m)^2-m^2)=m^2(1-2m)\). These are polynomial identities, independently re-expanded in the exact symbolic checker; no sampling assumption enters this step.

If \(a_1/b_1<\cdots<a_4/b_4\), then \(\Delta_{ij}<0\) for every \(i<j\). Consequently each product of two displayed \(\Delta\)'s is strictly positive. When \(0<m<1/2\), \(c_m>0\), yielding \(T_{1243}>T_{1234}>T_{1324}\). When \(1/2<m<1\), \(c_m<0\) and the inequalities reverse. Step 1 transfers this ordering to the Perron multipliers. At \(m=1/2\), all step maps have the same one-dimensional image, and multiplying their scalar effects gives \(\prod_i(a_i+b_i)/2\), independent of temporal order. This proves the complete classification.

**4. Exactly certified change of the growth/decline decision.** Take \(m=3/4\) and

\[
D_i=\frac9{10}\operatorname{diag}(r_i,1),\qquad
(r_1,r_2,r_3,r_4)=\left(\frac14,\frac12,2,4\right).
\]

Every order has \(\delta=43046721/1600000000<1\). Direct exact matrix multiplication gives the characteristic polynomial at one, \(\det(I-P_\sigma)=1-T_\sigma+\delta\), as

\[
\begin{array}{c|c}
\sigma&\det(I-P_\sigma)\\\hline
1243&641568143/12800000000\\
1234&-539411857/12800000000\\
1324&-13825436857/12800000000
\end{array}
\]

The non-Perron eigenvalue is positive and, whenever the Perron root is at least one, strictly below one because \(\delta<1\). Hence the characteristic polynomial at one is positive for the first order precisely when \(R_{1243}<1\), and is negative for the others precisely when \(R_{1234},R_{1324}>1\). Thus the same four seasons give either decline or growth solely through temporal reordering.

## Verification

Run \(\texttt{python verify.py}\) in an environment with Python 3 and SymPy. The standalone checker formally expands each of the three polynomial identities, checks the one-, two-, and three-season permutation invariance, checks 400 independent sets of exact-rational parameters against all 24 four-season permutations, reproduces the exact characteristic-polynomial signs in the displayed example, and checks the rank-one half-dispersal identity for all permutations. All stated checker stages completed successfully. These finite rational tests support the analytical proof, not replace it.

## Relationship to prior work

Schreiber (2010) studies how temporal autocorrelation and spatial heterogeneity affect metapopulation growth, using analytic approximations and simulation regimes; it motivates the precise temporal-order comparison here but does not give the exact exhaustive four-season classification. Schreiber and Li (2010 preprint; 2011 journal publication) analyze evolutionarily stable dispersal in periodic environments, including a period-two theorem. Bansaye and Lambert (2011 preprint) treat persistence in source-sink populations, with a detailed two-period environmental case. Altenberg (2013 preprint and journal paper) provides spectral-radius inequalities and identifies a reversal linked to the sign of the non-Perron eigenvalue of a two-state mixing matrix; the inspected Corollary 15 compares mixing parameters for \(M_m^2D\), not permutations of four distinct season-specific diagonal matrices. These are substantive precedents. The result here is the exact ordered-four-season comparison and minimality theorem, not a general claim about arbitrary mixing matrices, arbitrary periods, or novelty of Perron growth criteria.

## Limitations

This is a two-patch, deterministic *mean-abundance* or linearized invasion model. Growth matrices are positive diagonal profiles, dispersal is constant and symmetric, and the period has exactly four steps. Arbitrary seasonal movement matrices, demographic density dependence, stochastic temporal weather, non-periodic switching, and three or more patches may invalidate the ordering. The deterministic crossing of \(R=1\) alone is not a proved extinction-probability statement for every stochastic individual-based model. Finite checker results are not exhaustive proofs of infinite-parameter statements. Historical priority remains provisional because broader spectral rearrangement inequalities could conceivably imply this special case; the named primary sources were compared at the statement/implication level, and no such implication was found in inspected material.

## References

1. S. J. Schreiber, “Interactive effects of temporal correlations, spatial heterogeneity and dispersal on population persistence,” *Proceedings of the Royal Society B* 277 (2010), 1907–1914. First public online date 2010-02-17. https://doi.org/10.1098/rspb.2009.2006
2. S. J. Schreiber and C.-K. Li, “Evolution of unconditional dispersal in periodic environments,” arXiv:1007.5267, first submitted 2010-07-29. https://arxiv.org/abs/1007.5267
3. V. Bansaye and A. Lambert, “Past, growth and persistence of source-sink metapopulations,” arXiv:1111.2535, first submitted 2011-11-10. https://arxiv.org/abs/1111.2535
4. L. Altenberg, “On the Ordering of Spectral Radius Product \(r(A)r(AD)\) versus \(r(A^2D)\) and Related Applications,” arXiv:1301.4969, first submitted 2013-01-21. https://arxiv.org/abs/1301.4969
