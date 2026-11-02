# Balanced migration maximizes growth in antiphase seasonal two-patch networks

## Finding

**Theorem (strict rate-balance ordering and exact viability boundary).** Fix a half-sum of migration rates \(h>0\), a seasonal contrast \(g>0\), a full season-cycle period \(T>0\), and a common annual mean local growth rate \(r\in\mathbb R\). For every \(a,b\geq0\) with \(a+b=2h\), let \(\lambda(a,b)\) be the principal Floquet growth rate of the two-patch model defined below. Then \(\lambda(a,b)\) is a strictly increasing function of \(ab\) on \([0,h^2]\). Consequently, the **unique maximizer** is balanced bidirectional migration \(a=b=h\); the two one-way migration endpoints are the only minimizers, with minimum \(\lambda=r\). For \(ab>0\), \(\lambda(a,b)>r\).

When \(r<0\), the two isolated patches are average-growth sinks. If \(\lambda(h,h)>0\), there is a unique critical product \(p_*\in(0,h^2)\) such that \(\lambda(a,b)>0\) precisely when \(ab>p_*\), and \(\lambda(a,b)=0\) precisely when \(ab=p_*\). If \(\lambda(h,h)=0\), every unbalanced choice decays exponentially, whereas the balanced choice is critical; if \(\lambda(h,h)<0\), all migration directions decay. These claims concern the linear, density-independent population model and its exponential Floquet growth, not nonlinear long-run population sizes.

## Assumptions and scope

Let \(x_1,x_2\) denote nonnegative population abundances and let \(x=(x_1,x_2)^\mathsf T\). During the first half of each period, \(\dot x=A_1x\); during the second half, \(\dot x=A_2x\), with

\[
A_1=\begin{pmatrix}r+g-a&b\\a&r-g-b\end{pmatrix},\qquad
A_2=\begin{pmatrix}r-g-a&b\\a&r+g-b\end{pmatrix}.
\]

Here \(a\) is the rate from patch 1 to patch 2 and \(b\) is the rate from patch 2 to patch 1. They are constant across seasons; the growth contrasts switch signs exactly halfway through the period. The uncoupled time average of each patch is exactly \(r\). No assertion is made for unequal season durations, non-antiphase growth, time-varying migration, or three or more patches.

Write \(t=T/2\), \(d=(a-b)/2\), \(p=ab=h^2-d^2\), and

\[
\kappa_-=(h^2+g^2-2gd)^{1/2},\qquad
\kappa_+=(h^2+g^2+2gd)^{1/2}.
\]

Set \(\operatorname{sinhc}(z)=\sinh(z)/z\), with its continuous value \(\operatorname{sinhc}(0)=1\). Define

\[
C_p(t)=\cosh(\kappa_-t)\cosh(\kappa_+t)
 +(h^2-g^2)t^2\operatorname{sinhc}(\kappa_-t)
 \operatorname{sinhc}(\kappa_+t).
\]

The dependence on \(d\) is through \(p\) alone, as follows from the proof. The exact growth formula, valid even for one-way migration and vanishing \(\kappa_\pm\), is

\[
\boxed{\lambda(a,b)=r-h+T^{-1}\operatorname{arcosh}C_p(T/2).}
\]

For \(r<0\) and \(\lambda(h,h)>0\), the critical product is uniquely defined by

\[
\boxed{C_{p_*}(T/2)=\cosh((h-r)T).}
\]

In particular, for fixed \(h,g,d,r\) as \(T\downarrow0\),

\[
\lambda(a,b)=r+\frac{g^2ab}{24h}T^2+O(T^4).
\]

## Proof

**Step 1: exact normalized monodromy.** Both seasonal matrices have trace \(2(r-h)\). Define traceless matrices \(M_j=A_j-(r-h)I\). Direct multiplication gives

\[
M_1^2=\kappa_-^2 I,\quad M_2^2=\kappa_+^2I,\quad
\tfrac12\operatorname{tr}(M_2M_1)=h^2-g^2.
\]

The Cayley--Hamilton identity therefore gives

\[
e^{tM_j}=\cosh(\kappa_jt)I+
 t\operatorname{sinhc}(\kappa_jt)M_j.
\]

The normalized full-period monodromy \(P=e^{-(r-h)T}e^{tA_2}e^{tA_1}=e^{tM_2}e^{tM_1}\) has determinant one and half-trace \(C_p(t)\) displayed above. Its eigenvalues are \(C_p(t)\pm\sqrt{C_p(t)^2-1}\). We establish below that \(C_p(t)\geq\cosh(2ht)>1\); thus the larger eigenvalue is \(e^{\operatorname{arcosh}C_p(t)}\). Multiplication by the scalar \(e^{(r-h)T}\) gives the boxed exact Floquet formula. No diagonalizability assumption is needed at a zero seasonal spectral gap.

**Step 2: a positive Volterra representation.** For \(s\) sufficiently large, using the Laplace transforms of products of hyperbolic functions gives the exact rational identity

\[
\begin{aligned}
\widehat C_p(s)
&=\frac{s(s^2-4g^2)}{s^4-4(h^2+g^2)s^2+16g^2d^2}\\
&=\frac{s}{s^2-4h^2}\left(1-
 \frac{16g^2p}{(s^2-4h^2)(s^2-4g^2)}\right)^{-1}.
\end{aligned}
\]

The first equality follows either by Laplace transforming the preceding finite hyperbolic expression or by reducing its four exponential terms to a common denominator; the second uses \(d^2=h^2-p\). Let \(f(t)=\cosh(2ht)\) and \(k(t)=(u_h*u_g)(t)\), where \(u_c(t)=\sinh(2ct)/(2c)\) for \(t\geq0\), and \(*\) denotes causal convolution. Both \(f\) and \(k\) are nonnegative, and \(k(t)>0\) for every \(t>0\). Inverting the displayed Laplace identity yields the Volterra equation

\[
C_p(t)=f(t)+16g^2p\,(k*C_p)(t).
\]

The unique continuous solution has the convergent Neumann expansion

\[
\boxed{C_p(t)=f(t)+\sum_{j=1}^{\infty}(16g^2p)^j
 (k^{*j}*f)(t).}
\]

For rigor, on any compact time interval \([0,R]\), both \(k\) and \(f\) are bounded. Successive convolution terms are bounded by a constant times \(K^jR^j/j!\), so the series converges uniformly and solves the Volterra equation. The Laplace transform identifies it with the previously derived half-trace. Every term \((k^{*j}*f)(t)\) is strictly positive for \(t>0\). Consequently, for fixed \(h,g,t>0\), \(p\mapsto C_p(t)\) is continuous and **strictly increasing** on \([0,h^2]\), and \(C_0(t)=f(t)=\cosh(2ht)>1\).

**Step 3: growth ordering and sharp criticality.** The inverse hyperbolic cosine is strictly increasing above one. Therefore \(\lambda(a,b)\) is strictly increasing in \(p=ab\). With fixed \(a+b=2h\), \(p\) is maximal only for \(a=b=h\) and is zero exactly at the two unidirectional endpoints. At \(p=0\),

\[
\lambda=r-h+T^{-1}\operatorname{arcosh}(\cosh(hT))=r.
\]

This proves the sharp optimization and the strict gain under positive bidirectional migration. For \(r<0\), \(\lambda(0)\) is negative and \(\lambda(p)\) is continuous and strictly increasing; hence the intermediate value theorem gives all three viability cases and uniqueness of \(p_*\). The equation for \(p_*\) is the zero-Floquet condition \(\operatorname{arcosh}C_p=(h-r)T\). A positive Floquet exponent means exponential growth of every strictly positive initial state, and a negative one means extinction exponentially; zero exponent is a neutral linear boundary and is not called nonlinear persistence.

**Step 4: short-period law.** Taylor expansion of the exact half-trace at \(t=0\) gives \(C_p(t)=\cosh(2ht)+(2/3)g^2pt^4+O(t^6)\). Expanding the inverse hyperbolic cosine about \(\cosh(2ht)\), dividing by \(T=2t\), and using \(h>0\) yields the displayed \(T^2\) correction with \(O(T^4)\) remainder.

## Verification

The companion standalone file `VERIFY.py` uses independent scaling-and-squaring Taylor matrix exponentials to test the displayed closed formula against the spectral radius of the actual two-season monodromy. Its deterministic run passed 2,400 independent comparisons, 950 ordered parameter families, a five-point sink-threshold example, and 100 zero-seasonality boundary checks. To reproduce, run `python VERIFY.py` with a standard Python 3 interpreter.

For example, with \(h=g=1\), \(T=4\), and \(r=-1/5\), the one-way directions have exponent \(-0.2\); the imbalanced directions \((a,b)=(1/2,3/2)\) and \((3/2,1/2)\) have exponent approximately \(-0.002496363\); and the balanced direction \((1,1)\) has exponent approximately \(0.042658432\). These computed values illustrate, but do not establish, the all-parameter theorem. The proof above supplies the infinite-parameter justification.

## Relationship to prior work

Benaïm, Lobry, Sari and Strickler (2021), §2.2.3, derive an exact growth formula for symmetric two-patch antiphase seasonality; §3.2, especially equations (37)--(38), introduces asymmetric dispersal but discusses fixed-bias asymptotics rather than an ordering of every direction at a fixed total migration rate. Katriel (2021), §2.1, assumes a symmetric migration matrix and studies periodicity and dispersal-induced growth. Benaïm et al. (2023), §§4.2--4.3 and supplementary §S1, analyze periodic growth with constant asymmetric migration, supply particular numerical examples, and discuss period dependence; their results do not state a global strict ordering by the directed-rate product for the equal-mean square-wave family. Benaïm et al. (2024) develop broader time-periodic growth/decay analysis; this does not supply the fixed-rate-sum comparison. The result here is a distinct precise fixed-budget optimization and a necessary-and-sufficient viability corridor, not a claim that asymmetric dispersal is always inferior in every habitat model.

## Limitations

The conclusion depends on exactly antiphase growth with equal seasonal durations, equal local annual means, and a fixed total constant directed migration rate. It does not apply to general heterogeneous growth means, asymmetric season lengths, seasonal migration, stochastic switching, or nonlinear density-dependent equilibria. The Floquet statement concerns a linearization and cannot alone guarantee nonlinear persistence in models with additional mechanisms. Prior specialized equivalent formulations may remain unlocated. There has been no independent external audit.

## References

1. M. Benaïm, C. Lobry, T. Sari, E. Strickler, *When can a population spreading across sink habitats persist?*, arXiv:2311.04706v1 (first public November 8, 2023), especially §§4.2--4.3 and supplementary §S1. https://arxiv.org/abs/2311.04706
2. M. Benaïm, C. Lobry, T. Sari, E. Strickler, *Untangling the role of temporal and spatial variations in persistance of populations*, arXiv:2111.12633v1 (November 24, 2021), especially §§2.2.3 and 3.2. https://arxiv.org/abs/2111.12633
3. G. Katriel, *Dispersal-induced growth in a time-periodic environment*, arXiv:2104.01589v1 (April 4, 2021), especially §2.1. https://arxiv.org/abs/2104.01589
4. M. Benaïm, C. Lobry, T. Sari, E. Strickler, *Dispersal-induced growth or decay in a time-periodic environment*, arXiv:2407.07553v1 (July 2024), especially §§1--3. https://arxiv.org/abs/2407.07553
5. H. Wu, Y. Wang, Y. Li, D. L. DeAngelis, *Dispersal asymmetry in a two-patch system with source-sink populations*, Theoretical Population Biology 2020, DOI:10.1016/j.tpb.2019.11.004. Constant-environment, different model; included to delimit the claim. https://doi.org/10.1016/j.tpb.2019.11.004
