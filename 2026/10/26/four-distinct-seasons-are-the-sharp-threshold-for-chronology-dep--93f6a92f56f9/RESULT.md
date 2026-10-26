# Four distinct seasons are the sharp threshold for chronology-dependent two-habitat population growth

## Finding

Consider the same collection of seasonal habitat conditions applied in two different chronological orders to a mobile population. In a two-habitat model with fixed symmetric migration, **one, two, or three seasonal phases cannot produce an order effect on the exponential population growth rate**. Four phases are the first possibility.

For four phases, the exact signed difference in the two growth rates is governed solely by a product of two seasonal habitat-contrast differences. Four phases can even reverse extinction into exponential growth with no change whatsoever in any season's duration, either habitat's mean growth, or the migration rate.

For a seasonal order \(\pi\), define its principal Floquet growth exponent by
\[
\Lambda_\pi=\frac{1}{T}\log\rho(E_{\pi_1}E_{\pi_2}\cdots E_{\pi_k}),\qquad T=\sum_{i=1}^{k}\tau_i.
\]

Let the season-specific contrasts be \(b_i=(r_{i1}-r_{i2})/2\). For four phases the comparison \(1234\) versus \(1324\) obeys the exact sign law
\[
\operatorname{sgn}(\Lambda_{1234}-\Lambda_{1324})
=\operatorname{sgn}((b_1-b_4)(b_2-b_3)).
\]
The two growth exponents agree if and only if \(b_1=b_4\) or \(b_2=b_3\).

Moreover, **among the 24 possible orders there are at most three distinct growth exponents, and exactly three if the four contrasts are pairwise distinct**.

## Assumptions and scope

Let \(m>0\) be a time-independent symmetric migration rate. During phase \(i\) of positive duration \(\tau_i\), the linear population density vector \(x(t)\in\mathbb R^2_{\ge0}\) follows
\[
\dot x=A_i x,\qquad
A_i=\begin{pmatrix}r_{i1}-m&m\\m&r_{i2}-m\end{pmatrix},
\]
where every \(r_{ij}\in\mathbb R\). The environment repeats after total time \(T=\sum_i\tau_i\). Define the phase propagator \(E_i=e^{\tau_i A_i}\). The monodromy in chronological order is actually \(E_{\pi_k}\cdots E_{\pi_1}\); its spectral radius equals that of the reversed product \(E_{\pi_1}\cdots E_{\pi_k}\), since each factor is symmetric and transposition preserves spectrum. Thus our order notation measures the physical order without ambiguity. Each \(E_i\) is symmetric positive definite and strictly entrywise positive. All claims concern the associated principal Floquet exponent, and extinction or growth of the linear population from nonzero nonnegative initial states.

The hypotheses require exactly one common \(m\) across phases. If phase-specific or asymmetric migration is allowed, the trace factorization and sharp three-phase invariance need not hold.

## Proof

**Phase decomposition.** Write
\[
a_i=\frac{r_{i1}+r_{i2}}2-m,\qquad
b_i=\frac{r_{i1}-r_{i2}}2,\qquad
d_i=\sqrt{m^2+b_i^2},
\]
\[
B_i=\begin{pmatrix}b_i&m\\m&-b_i\end{pmatrix},\qquad B_i^2=d_i^2 I.
\]
Since \(A_i=a_iI+B_i\), with \(c_i=\cosh(\tau_i d_i)\) and \(q_i=\sinh(\tau_i d_i)/d_i>0\),
\[
E_i=e^{\tau_i a_i}(c_iI+q_iB_i).
\]

**Why three phases never suffice.** For symmetric matrices, trace is invariant under any cyclic permutation of factors and also under reversal of all factors by transposition. For at most three factors, cyclic permutations and reversal generate the entire permutation group. Therefore every ordering has the same monodromy trace. Independently, all orderings have the same determinant \(\prod_i\det E_i>0\). Two-dimensional characteristic polynomials are fixed by trace and determinant, so their eigenvalues and principal Floquet exponents are identical.

**Exact four-phase trace identity.** Expand each \(E_i\) using the decomposition above. Terms with zero, one, two, or three \(B_i\) factors have identical total traces in the two orders: the single-factor and triple-factor traces are zero, and pairwise traces \(\operatorname{tr}(B_iB_j)=2(m^2+b_ib_j)\) are independent of order. The only difference is the four-factor term. Direct multiplication, using \(B_i^2=(m^2+b_i^2)I\), gives
\[
\operatorname{tr}(B_1B_2B_3B_4)-\operatorname{tr}(B_1B_3B_2B_4)
=4m^2(b_1-b_4)(b_2-b_3).
\]
Thus
\[
\boxed{\operatorname{tr}(E_1E_2E_3E_4)-\operatorname{tr}(E_1E_3E_2E_4)
=4m^2 e^{\sum_i \tau_i a_i}\left(\prod_{i=1}^4q_i\right)
(b_1-b_4)(b_2-b_3).}
\]
Every prefactor other than the two contrasts is strictly positive.

**Trace order is growth order.** Each product has strictly positive entries and positive determinant \(D=\exp(\sum_i2a_i\tau_i)\), irrespective of order. Its eigenvalues are positive and distinct, and for trace \(s>2\sqrt D\) the Perron eigenvalue equals \((s+\sqrt{s^2-4D})/2\), strictly increasing in \(s\). The trace sign law therefore gives exactly the asserted principal-exponent sign law, including equality.

**Three classes among four-phase orders.** Cyclic permutation and reversal generate a dihedral subgroup acting on the four phase labels with three orbits of eight orderings. This gives at most three distinct traces and exponents. Representatives may be taken as the three cyclic arrangements of the same four labels. For two different representatives, a relabeling of the preceding trace difference identity expresses their nonzero trace difference as a strictly positive prefactor times \(4m^2(b_i-b_j)(b_k-b_l)\), with \(\{i,j,k,l\}=\{1,2,3,4\}\). If all four contrasts differ, none of the three differences vanishes. Hence there are exactly three different exponents.

**Exact extinction-versus-growth witness.** Take \(\tau_i=1\), \(m=1\), \(b=(1,-1,2,-2)\), \(r_{i1}=b_i-2/5\), and \(r_{i2}=-b_i-2/5\). Both isolated habitats have the same arithmetic average rate \(-2/5<0\) over the four phases. The coupled seasonal matrices are
\[
A_i=\begin{pmatrix}b_i-7/5&1\\1&-b_i-7/5\end{pmatrix}.
\]
Set \(C_i=A_i+4I=\bigl(\begin{smallmatrix}b_i+13/5&1\\1&-b_i+13/5\end{smallmatrix}\bigr)\). All entries of every \(C_i\) are nonnegative, and their maximum row sum is at most \(28/5\). For either order \(\pi\), define \(K_\pi=\prod_i e^{C_{\pi_i}}\) and \(M_\pi=e^{-16}K_\pi\); then \(\det M_\pi=e^{-56/5}<1\). Because both eigenvalues of \(M_\pi\) are positive, the leading eigenvalue exceeds one exactly when
\[
\operatorname{tr}K_\pi>e^{16}+e^{24/5}.
\]
A rational Taylor-series certificate provides strict bounds
\[
6436128<\operatorname{tr}K_{1234}<6436129,
\]
\[
8886232<e^{16}+e^{24/5}<8886233,
\]
\[
15910318<\operatorname{tr}K_{1324}<15910319.
\]
The first trace is strictly below the threshold while the second is strictly above. Therefore \(\Lambda_{1234}<0<\Lambda_{1324}\). The exact inequality certification is given by the standalone `verify.py` and does not rely on floating-point output. This proves the four-phase cutoff is attained.

## Verification

Run `python verify.py` with Python 3.9 or later. The checker uses only standard-library exact rational fractions to enclose the four matrix exponentials by \(60\)-term Taylor polynomials and explicit geometric upper bounds on their tails. It likewise encloses \(e^{16}\) and \(e^{24/5}\) with \(120\)-term rational Taylor intervals. Every claimed strict interval above is verified by exact rational comparison. Additional finite exact checks confirm examples of the four-factor trace polynomial identity and the three dihedral trace classes. Such finite checks are corroborations; the universal statements are established by the symbolic proof above.

## Relationship to prior work

Dispersal-induced growth in periodic two-patch systems, including growth from habitats that separately decline, is the central subject of Katriel (2021/2022). Benaïm–Lobry–Sari–Strickler (2021/2023) analyze migration under alternating favorable/unfavorable habitat phases and related temporal models. Benaïm and collaborators (2024) study dispersal-induced growth or decay for reducible migration matrices. Monmarché–Schreiber–Strickler (2024) analyze periodic and random temporal environmental variation and general ordered monodromy matrices. These studies supply the natural model, but the inspected texts do not state the **sharp minimum number of symmetric constant-dispersal phases**, the **exact four-phase contrast-product ordering law**, or the **certified same-multiset opposite-growth witness** together.

Cyclic invariance of trace, reversal invariance for symmetric factors, and the standard two-by-two characteristic polynomial are classical matrix facts and are not claimed as new. The new contribution assessed here is the precise ecological ordering classification and its demonstrated extinction boundary. Broader or differently formulated matrix-product literature may overlap; no assertion of exhaustive publication priority is made.

## Limitations

The result assumes exactly two habitats, one fixed symmetric positive migration rate, piecewise-constant deterministic periodic vital rates, and the linear growth regime. It makes no claim about three-phase invariance with season-specific migration or asymmetric movement, and no global nonlinear population-persistence conclusion. The analytic sign identity is universal within the stated model; the integer trace certificate establishes the displayed example only. Publication priority remains subject to independent examination of the wider matrix-product and ecological season-order literature.

## References

1. G. Katriel, *Dispersal-induced growth in a time-periodic environment*, arXiv:2104.01589, first posted 2021-04-04; Journal of Mathematical Biology 85 (2022), 24. https://arxiv.org/abs/2104.01589
2. M. Benaïm, C. Lobry, T. Sari and E. Strickler, *Untangling the role of temporal and spatial variations in persistance of populations*, arXiv:2111.12633, first posted 2021-11-24. https://arxiv.org/abs/2111.12633
3. M. Benaïm and collaborators, *Dispersal-induced growth or decay in a time-periodic environment: The case of reducible migration matrices*, arXiv:2407.07553, first posted 2024-07-10. https://arxiv.org/abs/2407.07553
4. P. Monmarché, S. J. Schreiber and E. Strickler, *Impacts of Tempo and Mode of Environmental Fluctuations on Population Growth*, arXiv:2408.11179, first posted 2024-08-20. https://arxiv.org/abs/2408.11179
