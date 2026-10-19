# The first order-sensitive seasonal schedules in a two-patch metapopulation

## Finding
Consider two habitat patches, a fixed exchange fraction \(0<p<1\), and positive patch-specific low-density multipliers \((a_j,b_j)\) during each phase \(j\). A phase applies the matrix
\[
M_j=D_jP,\qquad D_j=\operatorname{diag}(a_j,b_j),\qquad
P=\begin{pmatrix}1-p&p\\p&1-p\end{pmatrix}.
\]
In a period of \(m\) phases, the population's asymptotic per-period growth factor is the Perron root of their ordered product. Rearranging a *fixed multiset* of at most three phase matrices never changes that growth factor. Four is the least number of phases for which rearrangement can matter.

For exactly four phases, relabel the phases so that their *relative patch advantages* satisfy
\[
r_1=\frac{a_1}{b_1}\le r_2=\frac{a_2}{b_2}\le r_3=\frac{a_3}{b_3}\le r_4=\frac{a_4}{b_4}.
\]
Write \(\Lambda_{ijkl}=\rho(M_iM_jM_kM_l)\). For \(0<p<1/2\), **every ordering** obeys the sharp three-class ranking
\[
\Lambda_{1243}\ge\Lambda_{1234}\ge\Lambda_{1324}.
\]
The 24 orderings reduce to these three spectral classes under cyclic rotation and reversal. The inequalities are strict if all four relative advantages are distinct. For \(1/2<p<1\), both inequalities reverse; for \(p=1/2\), all orderings have exactly the same Perron root.

More precisely, putting \(T_{ijkl}=\operatorname{tr}(M_iM_jM_kM_l)\) and \(\Delta_{ij}=a_ib_j-a_jb_i\), the exact comparison identities are
\[
\begin{aligned}
T_{1243}-T_{1234}&=p^2(1-2p)\Delta_{12}\Delta_{34},\\
T_{1234}-T_{1324}&=p^2(1-2p)\Delta_{14}\Delta_{23},\\
T_{1243}-T_{1324}&=p^2(1-2p)\Delta_{13}\Delta_{24}.
\end{aligned}
\]
Consequently, the preferred schedule is determined by the ordering of patch-advantage ratios, without having to calculate any eigenvalues.

This rearrangement can change the invasion verdict. With \(p=1/4\) and \((a_j,b_j)=(16j/29,16/29)\) for \(j=1,2,3,4\), the same four seasonal environments satisfy
\[
\Lambda_{1243}>1>\Lambda_{1324}.
\]
Thus one ordering grows from rarity whereas another declines, with identical phase-specific rates and dispersal.

## Assumptions and scope
Matrices act on column vectors of two nonnegative patch abundances. Within a phase, organisms redistribute according to the common, symmetric, column-stochastic matrix \(P\), and then multiply locally by \(D_j\). Every \(a_j,b_j\) is strictly positive, and the same \(p\in(0,1)\) applies to all phases. The period is repeated indefinitely. For an ordering \(i_1,\ldots,i_m\) we represent the trace and eigenvalues with \(M_{i_1}\cdots M_{i_m}\); reversing the written multiplication order produces the chronologically applied monodromy and has the same spectrum in this model. The result concerns low-density linear growth, not nonlinear regulation, demographic stochastic extinction probability, or scheduling feasibility.

The statement for four phases includes ratio ties (weak inequalities); strictness requires distinct ratios. A common positive rescaling of every patch rate in every phase rescales all four-phase multipliers equally. No claim is made about optimal orderings for five or more distinct phases, nonsymmetric migration, changing migration across phases, or three or more habitat patches.

## Proof
**1. Reversal and short-period invariance.** Let \(M_j=D_jP\). For \(p\ne1/2\), \(P\) is invertible and
\[
M_j^{\mathsf T}=PD_j=PM_jP^{-1}.
\]
Taking the transpose of any product and then conjugating therefore gives
\[
\operatorname{tr}(M_{i_1}\cdots M_{i_m})
=\operatorname{tr}(M_{i_m}\cdots M_{i_1}).
\]
Trace also respects cyclic rotation. Rotations and reversal generate every permutation of one, two, or three labels. Furthermore, for each \(m\), every ordering has the same determinant
\[
\det(M_{i_1}\cdots M_{i_m})=(1-2p)^m\prod_{j=1}^m a_jb_j.
\]
Since trace and determinant determine the spectrum of a \(2\times2\) matrix, all short-period orderings have the same spectral radius. When \(p=1/2\), each \(M_j\) has rank one, and the nonzero eigenvalue of any ordered product is \(2^{-m}\prod_j(a_j+b_j)\), also order independent. This proves universal invariance for \(m\le3\).

**2. Four phases and three equivalence classes.** Rotation and reversal identify all 24 permutations of four distinct labels with one of \(1234,1243,1324\). Direct expansion of the two-by-two matrix products gives the three factorizations in the Finding. These are polynomial identities for *all* real values of the symbols, and the standalone symbolic checker reproduces all three without floating-point arithmetic.

**3. Signs and Perron roots.** In the stipulated increasing ratio order, \(\Delta_{ij}=b_ib_j(r_i-r_j)\le0\) whenever \(i<j\). Each product on the right of the three factorization identities is therefore nonnegative, and positive if the four ratios are pairwise distinct. The common prefactor \(p^2(1-2p)\) determines the sign. All four-factor products have the same determinant \((1-2p)^4\prod_j a_jb_j\ge0\) and strictly positive entries. At a fixed determinant, the larger trace gives the larger positive Perron root, because the other eigenvalue is nonnegative and the Perron root is \((T+\sqrt{T^2-4\det})/2\). This establishes the complete ranking and its reversal at \(p=1/2\). It also exhibits strict inequality for generic data, so no period smaller than four can be order-sensitive.

**4. A change of invasion verdict.** For \(p=1/4\) and the stated rates, exact multiplication gives the common monodromy determinant
\[
d=\frac{6442450944}{500246412961}
\]
and traces \(T_{1243}=716800/707281\) and \(T_{1324}=708608/707281\). The corresponding exact characteristic-polynomial evaluations are
\[
\begin{aligned}
1-T_{1243}+d&=-\frac{290156895}{500246412961}<0,\\
1-T_{1324}+d&=\frac{5503889057}{500246412961}>0.
\end{aligned}
\]
Because \(0<d<1\), the smaller nonnegative eigenvalue of either positive product is less than one; consequently the sign of \(1-T+d=\det(I-Q)\) identifies whether its Perron root exceeds one. This proves the claimed threshold reversal using exact rational inequalities.

## Verification
The included `verify_exact.py` reproduces the three symbolic trace factorizations, all 24 four-phase trace classes, the trace-and-determinant invariance for all phase permutations through length three, the common self-adjointness identity, 100 additional independent rational parameter comparisons using a separate \(2\times2\) matrix multiplication routine, and the exact threshold example. Execute `python verify_exact.py` with Python 3 and SymPy installed; successful execution prints `EXACT_CHECK_OK 100 rational samples plus symbolic universal identities`. The universal statement rests on the explicit algebraic proof above; the numerical sample checks serve only as supplementary consistency tests.

## Relationship to prior work
Caswell and Trevisan (1994) introduced phase-specific sensitivity analysis for periodic matrix population models; that framework takes the season order as given. Schreiber (2010) examined spatial heterogeneity, temporal correlations, and dispersal in population growth. Schreiber and Li (2010 preprint; 2011 journal publication) considered evolutionary stability of dispersal in periodically varying environments. Roth, Caswell, and colleagues (2016) explain that matrix order matters generally while cyclic rephasings preserve asymptotic growth rates. Caswell's later full open-access treatment (2019, adapting Caswell and Shyu 2012) explicitly proves cyclic phase invariance and develops sensitivities. None of those inspected materials states the special two-patch, common-migration three-phase invariance, the complete four-phase ordering determined by relative patch advantages, or the exact invasion-threshold witness. General noncommutativity and cyclic invariance do not imply this particular three-class comparison.

The algebra also overlaps general matrix-product rearrangement questions, but it is not the two-symbol spectral-norm rearrangement problem: there are four different diagonal fecundity factors, a fixed migration operator, and a Perron-root comparison. No exhaustive claim of mathematical-literature uniqueness is made.

## Limitations
The result is conditional on exactly two patches, symmetric phase-independent dispersal, strictly positive demographic multipliers, and periodically repeated linear low-density dynamics. An arbitrary migration matrix or phase-dependent dispersal can destroy the simultaneous reversal identity. Full-text access to some older sources was limited, and an equivalent theorem under a different matrix-rearrangement terminology remains a possibility. A unit Perron root is a marginal linear threshold only; the theorem makes no assertion about stochastic persistence or nonlinear equilibria. The included checker is exact but does not substitute for independent review.

## References
- Caswell, H. and Trevisan, M. C. (1994), *Sensitivity analysis of periodic matrix models*, Ecology 75, 1299–1303. DOI: 10.2307/1937455. First published 1994-07-01.
- Schreiber, S. J. (2010), *Interactive effects of temporal correlations, spatial heterogeneity and dispersal on population persistence*, Proceedings of the Royal Society B 277, 1907–1914. DOI: 10.1098/rspb.2009.2006. Online 2010-02-17.
- Schreiber, S. J. and Li, C.-K. (2011), *Evolution of unconditional dispersal in periodic environments*, Journal of Biological Dynamics 5, 120–134. DOI: 10.1080/17513758.2010.525667; arXiv:1007.5267 (2010-07-29).
- Roth, G. et al. (2016), *Hyperstate matrix models: extending demographic state spaces to higher dimensions*, Methods in Ecology and Evolution. DOI: 10.1111/2041-210X.12622.
- Caswell, H. (2019), *Periodic Models*, in *Sensitivity Analysis: Matrix Methods in Demography and Ecology*, Chapter 8, open-access DOI: 10.1007/978-3-030-10534-1_8 (adapted from Caswell and Shyu, 2012).
