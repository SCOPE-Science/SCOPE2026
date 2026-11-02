# A three-season orientation criterion for global persistence of saturated two-stage populations

## Finding

Three seasonal environments can have identical annual vital rates yet opposing long-term outcomes solely because the order in which they occur is reversed. For a density-limited juvenile–adult projection model, a three-dimensional determinant of the seasonal vital-rate triples selects the winning calendar and gives a complete *global*, not merely linearized, extinction/critical/persistence classification. The result includes an admissible exact-rational instance where one order eliminates the population while the other supports a unique attracting positive seasonal cycle.

## Assumptions and scope

For \(i\in\{1,2,3\}\), define
\[
P_i=\begin{pmatrix}0&f_i\\s_i&t_i\end{pmatrix},\qquad F_i(x)=\frac{P_i x}{1+c_i^{\mathsf T}x},
\]
where \(f_i>0\), \(0<s_i,t_i<1\), and \(c_i\in(0,\infty)^2\). The juvenile–adult state is \(x\in[0,\infty)^2\). A chronological order \(i_1i_2i_3\) means that \(F_{i_1}\), then \(F_{i_2}\), then \(F_{i_3}\) acts, with that calendar repeated indefinitely. There is no immigration, randomness, delay or stage-specific density multiplier: the *whole* seasonal projection is divided by one common positive affine density factor. Initial abundance is arbitrary nonzero and nonnegative. The integer \(k\) counts complete three-season cycles.

For an order \(i_1i_2i_3\), write
\[
M=P_{i_3}P_{i_2}P_{i_1},\quad
C^{\mathsf T}=c_{i_1}^{\mathsf T}+c_{i_2}^{\mathsf T}P_{i_1}+c_{i_3}^{\mathsf T}P_{i_2}P_{i_1}.
\]
All entries of \(M\) and \(C\) are strictly positive. Let \(\lambda>0\) be the Perron eigenvalue of \(M\), and let \(v>0\) be *any* positive Perron right eigenvector (the subsequent formulas are invariant under scaling of \(v\)).

**Global trichotomy.** From every \(x_0\ne0\), the state after \(k\) complete cycles converges to zero if \(\lambda<1\); if \(\lambda=1\) it obeys
\[
\lim_{k\to\infty} kx_k=\frac{v}{C^{\mathsf T}v};
\]
and if \(\lambda>1\) it converges to the unique strictly positive cycle-boundary fixed point
\[
x_* = \frac{(\lambda-1)v}{C^{\mathsf T}v}.
\]
The three intermediate seasonal states converge to the corresponding phase values of the unique positive three-periodic orbit when \(\lambda>1\).

**Calendar comparison.** Define
\[
K=\prod_{i=1}^3 f_i s_i,\qquad T_{123}=\operatorname{tr}(P_3P_2P_1),\qquad T_{132}=\operatorname{tr}(P_2P_3P_1),
\]
and \(\Delta=\det\begin{pmatrix}f_1&s_1&t_1\\f_2&s_2&t_2\\f_3&s_3&t_3\end{pmatrix}\). Then
\[
T_{123}-T_{132}=\Delta,\qquad \det M_{123}=\det M_{132}=-K,
\]
and each calendar is persistent, critical or extinct according as \(T+K\) is greater than, equal to or less than \(1\). For \(\Delta>0\) calendar 123 has strictly greater long-run linear growth factor, and for \(\Delta<0\) calendar 132 does; equality is a growth-rate tie. All three cyclic shifts of either calendar share its Perron root, but need not have identical abundances at a fixed observation phase. Two or fewer seasons cannot exhibit a noncyclic order effect in the Perron root.

If \(t_1=t_2=t_3=t>0\) and \(f_1<f_2<f_3\), this orientation determinant is
\[
\Delta=t(f_2-f_1)(f_3-f_2)\left(\frac{s_3-s_2}{f_3-f_2}-\frac{s_2-s_1}{f_2-f_1}\right).
\]
Thus the comparison is governed by the curvature of the seasonal survival-versus-fecundity tradeoff.

## Proof

**1. Exact nonlinear cycle composition.** Direct substitution of \(x\mapsto A x/(1+a^{\mathsf T}x)\) into \(x\mapsto Bx/(1+b^{\mathsf T}x)\) gives \(x\mapsto BAx/[1+(a^{\mathsf T}+b^{\mathsf T}A)x]\). Applied to the three phases, this yields \(G(x)=Mx/(1+C^{\mathsf T}x)\) exactly. Induction (not an asymptotic approximation) gives
\[
x_k=\frac{M^k x_0}{1+C^{\mathsf T}\sum_{j=0}^{k-1}M^j x_0}.
\]

**2. Global convergence including the critical boundary.** Because \(M\) has strictly positive entries, Perron–Frobenius theory gives a simple dominant positive eigenvalue \(\lambda\), positive left/right eigenvectors, and a second eigenvalue of strictly smaller absolute value. For every nonzero \(x_0\ge0\), write \(M^k x_0=\alpha\lambda^k v+o(\lambda^k)\) with \(\alpha>0\). If \(\lambda<1\), the nonnegative denominator in the exact formula is at least one and the numerator tends to zero. If \(\lambda=1\), the numerator tends to \(\alpha v\) and the denominator is \(k\alpha C^{\mathsf T}v+o(k)\), proving the sharp limit above. If \(\lambda>1\), the denominator grows as \(\alpha C^{\mathsf T}v\,\lambda^k/(\lambda-1)\), giving the positive limit. Every strictly positive fixed point of \(G\) is a positive eigenvector of \(M\), hence is proportional to \(v\); substitution fixes its coefficient uniquely to \((\lambda-1)/(C^{\mathsf T}v)\). Continuity of the seasonal maps gives the full attracting three-periodic orbit. Notice that this is a global conclusion for every nonzero nonnegative state, including those on the boundary of the cone.

**3. The exact orientation identity.** Matrix multiplication gives
\[
T_{123}=t_1t_2t_3+s_1f_3t_2+s_3f_2t_1+s_2f_1t_3,
\]
\[
T_{132}=t_1t_2t_3+s_1f_2t_3+s_2f_3t_1+s_3f_1t_2.
\]
Their difference expands to the stated \(3\)-by-\(3\) determinant. Each \(\det P_i=-f_i s_i\), so the three-product determinant is \(-K\). Therefore its characteristic polynomial is \(z^2-Tz-K\), whose unique positive root is the Perron eigenvalue. As this polynomial is strictly increasing beyond its positive root, evaluation at \(z=1\) gives \(\lambda>1\) if and only if \(T+K>1\); the other cases are analogous. With common \(K\), the positive root increases strictly with \(T\). Cyclic shifts preserve the trace and determinant by cyclic trace invariance and determinant multiplicativity; with one or two seasons every reordering is cyclic. The common-stasis identity follows by collecting the determinant's terms.

**4. Exact extinction/persistence reversal.** Take
\[
(f_1,f_2,f_3)=\left(\frac35,\frac65,\frac{12}5\right),\quad
(s_1,s_2,s_3)=\left(\frac14,\frac12,\frac34\right),\quad t_1=t_2=t_3=\frac25.
\]
Exact multiplication gives \(T_{123}=98/125\), \(T_{132}=211/250\), \(K=81/500\), and \(\Delta=-3/50\). Consequently \(1-T_{123}-K=27/500>0\), while \(1-T_{132}-K=-3/500<0\). The global trichotomy now proves extinction in 123 and global attraction to a positive cycle in 132, for **every** set of strictly positive crowding vectors.

## Verification

The included standalone `verify.py` checks, using symbolic algebra, all trace, determinant and recruitment-loop identities; it additionally verifies the equality under all six season permutations on 500 deterministic exact-rational test systems. The exact counterposed viability inequalities are checked as rational numbers. Independently, it composes the nonlinear seasonal maps with exact fractions and checks their cycle-power closed form for two calendars, three initial states including cone boundaries and seven cycles (42 exact equalities). These computational checks support the algebraic reconstruction; the infinite-time global claims follow from the explicit proof and Perron–Frobenius asymptotics, **not** from finite enumeration.

Reproduce with `python verify.py` using Python, `sympy`, and no external datasets.

## Relationship to prior work

Mertens, Yearsley, van den Bosch and Gilligan (2006) develop transient sensitivity analysis of general *linear* periodic population matrices, explain cyclic versus noncyclic environmental permutations, and illustrate crop-order effects. They do not give this three-parameter stage-matrix orientation determinant coupled to a complete nonlinear global population threshold. The 2006 full research paper was inspected, including its methods, discussion and comparison of noncyclic/cyclic orders. Caswell and Shyu's periodic-matrix sensitivity treatment, available in Caswell's open 2019 chapter, also addresses nonlinear seasonal projections but uses general perturbation formulas rather than an exact projectively saturated global trichotomy and the sharp three-season orientation test. Cushing and Ackleh's periodic net-reproduction study gives a more general threshold framework and period-two Leslie examples, but its accessible material did not establish this full model-specific conclusion. The linear trace identity, the Perron eigenvalue threshold and elementary Beverton–Holt saturation are **not** claimed separately as novel.

## Limitations

This is a theorem only for two-stage, three-environment *common-denominator* rational saturation, with no environmental noise, spatial coupling or heterogeneous density effects across transition entries. Calendar feasibility is a biological constraint: the mathematical reversal is relevant where season order can actually be managed. The orientation determinant orders **spectral growth factors**, not total equilibrium abundance across distinct calendar phases. The result has self-review, not independent peer or archival priority certification; a broader theorem on positive projective-fractional maps or rearrangement might subsume it.

## References

- Mertens, S. K., Yearsley, J. M., van den Bosch, F., and Gilligan, C. A. (2006). *Transient population dynamics in periodic matrix models: methodology and effects of cyclic permutations*. *Ecology* 87:2338–2348. First public date 2006-09-01. DOI: `10.1890/0012-9658(2006)87[2338:TPDIPM]2.0.CO;2`. Author-hosted full text: https://api.unil.ch/iris/server/api/core/bitstreams/39f4a4a0-30ec-490e-8314-846a5f9f412b/content.
- Cushing, J. M., and Ackleh, A. S. (2011). *A net reproductive number for periodic matrix models*. DOI: `10.1080/17513758.2010.544410` (online 2011-02-18).
- Caswell, H., and Shyu, E. (2012). *Sensitivity analysis of periodic matrix population models*. *Theoretical Population Biology* 82:329–339. Material is adapted as chapter 8 of Caswell (2019), *Sensitivity Analysis: Matrix Methods in Demography and Ecology*, DOI: `10.1007/978-3-030-10534-1_8`. Open full text: https://link.springer.com/chapter/10.1007/978-3-030-10534-1_8.
