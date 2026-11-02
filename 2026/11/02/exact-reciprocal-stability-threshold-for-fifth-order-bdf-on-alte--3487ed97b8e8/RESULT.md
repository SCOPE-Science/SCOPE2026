# Exact reciprocal stability threshold for fifth-order BDF on alternating grids

## Finding

For the genuine variable-coefficient five-step backward differentiation formula (BDF5), applied to the zero differential equation \(y'=0\), consider a fixed positive two-periodic sequence of steps \(rh,h,rh,h,\ldots\), where \(h>0\) and \(r>0\). Set
\[
 g(u)=4u^3-8u^2-95u-127.
\]
There is exactly one root \(u_*>2\) of \(g(u)=0\). Write
\[
 R_* = \frac{u_*+\sqrt{u_*^2-4}}2
      = 6.288402745592172\ldots.
\]
The four parasitic Floquet multipliers have modulus less than one if and only if
\[
              R_*^{-1}<r<R_*.
\]
At either boundary \(r\in\{R_*^{-1},R_*\}\), exactly one parasitic multiplier is the **simple** root \(-1\) and the other three have modulus less than one; the full method is power-bounded and zero-stable on the fixed periodic grid, although the parasitic mode is no longer strictly damped. For \(0<r<R_*^{-1}\) or \(r>R_*\), exactly one parasitic multiplier is real and less than \(-1\), with the other three strictly inside the unit disk, and zero-stability fails. The stable and unstable regimes are symmetric under interchanging the two step sizes.

This classifies *all* positive alternating-step ratios for BDF5, not arbitrary variable meshes. In particular the known isolated instability example at ratio \(10\) lies in the unstable regime; the complete reciprocal boundary and the unique unstable Floquet mode are the additional results.

## Assumptions and scope

The formula is the standard variable-coefficient BDF5 obtained by differentiating the degree-five Lagrange interpolant at the newest time, **not** a fixed-coefficient or Nordsieck-interpolated implementation. The five backward steps at the newest time are \(h_n,\ldots,h_{n-4}\), all positive. Write \(S_0=0\) and \(S_j=\sum_{\ell=0}^{j-1}h_{n-\ell}\) for \(1\le j\le5\). With interpolation nodes \(0,-S_1,\ldots,-S_5\), the derivative coefficients \(\alpha_0,\ldots,\alpha_5\) are
\[
 \alpha_0=\sum_{j=1}^5\frac1{S_j},\qquad
 \alpha_j=-\frac1{S_j}\prod_{\substack{1\le\ell\le5\\ \ell\ne j}}
                    \frac{S_\ell}{S_\ell-S_j}\quad(1\le j\le5).
\]
They satisfy \(\sum_{j=0}^5\alpha_j=0\), and the homogeneous numerical method is \(\sum_{j=0}^5\alpha_jy_{n-j}=0\). No smoothness, bounded adjacent ratio or proximity to unit ratios is assumed, but the two-periodic pattern is held fixed as the number of time steps grows.

## Proof

**1. Remove the constant solution.** Define \(d_n=y_n-y_{n-1}\) and \(\beta_j=\sum_{\ell=0}^j\alpha_\ell\) for \(0\le j\le4\). Then the recurrence is
\[
  \sum_{j=0}^4\beta_jd_{n-j}=0,
  \qquad d_n=-\sum_{j=1}^4\frac{\beta_j}{\beta_0}d_{n-j}.
\]
For any five positive backward steps \(H=(h_0,\ldots,h_4)\), let \(M(H)\) be the companion matrix with first row \((-\beta_1/\beta_0,\ldots,-\beta_4/\beta_0)\) and remaining rows shifting the four difference coordinates. Because every \(\beta_0=\alpha_0>0\), this is well-defined. Homogeneity in step length allows \(h=1\), so a two-step monodromy is
\[
 T(r)=M(1,r,1,r,1)M(r,1,r,1,r).
\]
Reversing the starting phase interchanges the two factors without changing their characteristic polynomial.

**2. Exact monodromy polynomial.** Direct rational simplification of the interpolation coefficients gives
\[
\begin{aligned}
 D&=(4r^3+30r^2+63r+40)(40r^3+63r^2+30r+4),\\
 A&=304r^6+1348r^5+2442r^4+2781r^3+2442r^2+1348r+304,\\
 B&=16r^6+108r^5+362r^4+547r^3+362r^2+108r+16,\\
 C&=-r(36r^4+170r^3+269r^2+170r+36),\\
 E&=4r(r+1)^2(r+2)(2r+1).
\end{aligned}
\]
Thus \(D>0\) and
\[
 \det(zI_4-T(r))=D^{-1}(Dz^4+Az^3+Bz^2+Cz+E).
\]
The coefficient expressions are reciprocal-palindromic in the relevant degree, hence unchanged under \(r\mapsto1/r\).

**3. A real Hurwitz certificate for the full unit-disk problem.** Apply the Cayley transform \(z=(1+s)/(1-s)\). Its inverse \(s=(z-1)/(z+1)\) maps \(|z|<1\) bijectively onto \(\operatorname{Re}s<0\). Define the transformed quartic
\[
 Q_r(s)=(1-s)^4\bigl(D\det(zI_4-T(r))\bigr)
       \big|_{z=(1+s)/(1-s)}
       =q_4s^4+q_3s^3+q_2s^2+q_1s+q_0.
\]
Writing \(P(r)=4r^6-8r^5-83r^4-143r^3-83r^2-8r+4\), the exact coefficients are
\[
\begin{aligned}
q_0&=480(r+1)^6,\\
q_1&=8(156r^6+1068r^5+2900r^4+3977r^3+2900r^2+1068r+156),\\
q_2&=8(116r^6+1068r^5+3334r^4+4769r^3+3334r^2+1068r+116),\\
q_3&=16(2r^6+188r^5+797r^4+1226r^3+797r^2+188r+2),\\
q_4&=-32P(r).
\end{aligned}
\]
For every \(r>0\), the first four coefficients are strictly positive. The Hurwitz determinants have the *global* strictly positive certificates
\[
 \Delta_2=q_3q_2-q_4q_1=128\sum_{j=0}^{12} a_jr^j,
 \qquad
 \Delta_3=q_3q_2q_1-q_3^2q_0-q_4q_1^2
        =1024\sum_{j=0}^{18}b_jr^j,
\]
where \(a_j=a_{12-j}\), \(b_j=b_{18-j}\), and the listed low-to-middle coefficients are
\[
\begin{aligned}
(a_0,\ldots,a_6)=&(1480,29992,280120,1393254,4109082,7683087,9431320),\\
(b_0,\ldots,b_9)=&(230400,6166272,74849696,543723184,2642541168,\\
&9125913628,23234325050,44646921618,65712229619,74682902480).
\end{aligned}
\]
All coefficients in these two sums are positive. Thus if \(q_4>0\), the quartic Routh–Hurwitz criterion \(q_4,q_3,\Delta_2,\Delta_3,q_0>0\) places all four roots of \(Q_r\) in the open left half-plane, equivalently all Floquet multipliers in the open unit disk.

If \(q_4=0\), \(Q_r\) is a cubic and its leading coefficient \(q_3>0\). The identity \(\Delta_3=q_3(q_2q_1-q_3q_0)>0\) proves this cubic is strictly Hurwitz. The fourth Floquet root is \(z=-1\) because \(Q_r\) has lost its quartic term; it is simple since \(q_3>0\). For \(q_4<0\), the Routh first-column signs, namely those of
\[
       q_4,\quad q_3,\quad \Delta_2/q_3,
       \quad \Delta_3/\Delta_2,\quad q_0,
\]
are \(-,+,+,+,+\). Hence exactly one Cayley root lies in the open right half-plane and the other three in the open left half-plane. Further, \(D\det(-I_4-T(r))=q_4<0\), while the monic characteristic polynomial is positive as \(z\to-\infty\). It follows that the unique exterior multiplier is real and lies strictly below \(-1\).

**4. Solve the sign transition exactly.** The reciprocal sextic satisfies
\[
       P(r)=r^3g(r+r^{-1}),
       \qquad g(u)=4u^3-8u^2-95u-127.
\]
For \(r>0\), \(u=r+r^{-1}\ge2\). Since \(g(2)=-317<0\), \(g(u)\to+\infty\), and the coefficient signs of \(g\) have one change, Descartes' rule of signs gives exactly one positive root \(u_*>2\). Therefore \(P(r)<0\) precisely for \(R_*^{-1}<r<R_*\), vanishes at the two endpoints, and is positive outside. Since \(q_4=-32P\), the three cases of Step 3 give the classification. Finally, the full five-step recurrence has in addition the simple constant-mode multiplier \(1\); this completes the zero-stability assertion on any fixed alternating grid.

## Verification

Run `python verifier.py` with Python 3, SymPy and optionally NumPy. The standalone source independently derives the five-point interpolation-based difference companion matrices, recomputes the monodromy characteristic polynomial, checks every Cayley coefficient, expands both positive Hurwitz determinants, verifies the cubic reciprocal reduction and its unique root on \((2,\infty)\), and optionally evaluates nine finite floating-point samples. All **exact symbolic identities** must pass before the final success message appears; sampling is supplementary, not an infinite proof.

The coefficient arrays shown in the proof are finite exact certificates of globally positive polynomials, not empirical fitted coefficients. The analytic sign arguments prove every positive \(r\), including arbitrarily small or large ones.

## Relationship to prior work

Skeel (1986) develops variable-coefficient and alternative variable-stepsize multistep constructions; that foundational interpolation setting is assumed here, rather than new. Grigorieff (1983) and Calvo–Grande–Grigorieff (1990) develop stability criteria and sufficient consecutive-ratio bounds for variable-step BDF methods, including high orders; those bounds are not asserted to be novel. Guglielmi–Zennaro (2001) analyze BDF3 via the spectral-radius approach, rather than the exact two-periodic BDF5 quartic considered here. Söderlind–Fekete–Faragó (2018) prove stability on sufficiently smooth nonuniform grids, for which adjacent step ratios tend to one as mesh resolution grows; the fixed alternating ratio \(r\ne1\) is outside that smooth-grid hypothesis.

An earlier investigation of the two-periodic BDF4 problem identified a BDF5 unstable witness at \(r=10\). This witness is **prior-covered** and is not presented as new. The additional claim is the exact *if and only if*, reciprocal critical ratio, complete boundary classification, and uniqueness of the unstable real multiplier at every exterior ratio. No claim is made that broad necessary-and-sufficient stability frameworks are new. The unavailable complete text of the 1990 Calvo–Grande–Grigorieff article and 1983 Grigorieff article leaves a specialist-priority risk about whether one contains an equivalent specialization.

## Limitations

The result concerns the homogeneous equation \(y'=0\), the genuine variable-coefficient degree-five BDF formula, and a **fixed** two-periodic sequence of positive step lengths. It does not establish nonzero-test-equation absolute stability, A-stability, variable-order switching, general nonperiodic-grid zero-stability, or a uniform zero-stability constant over all stable ratios tending to a critical endpoint. At the critical ratios, the multiplier \(-1\) is simple and power-bounded but is not decaying. The priority comparison is subject to inaccessible original specialist full texts and independent mathematical review has not been performed.

For bibliographic date provenance, the earliest precisely dated public electronic version established for the focal historical source is the author upload on January 30, 2015; the underlying journal paper dates to 1990. This digital-release date must not be interpreted as the paper's original publication date.

## References

- R. D. Skeel, *Construction of Variable-Stepsize Multistep Formulas*, Mathematics of Computation 47 (1986), 503–510, https://doi.org/10.1090/S0025-5718-1986-0856699-X . Accessible full-text transcription: https://www.researchgate.net/publication/278992956_Construction_of_variable-stepsize_multistep_formulas .
- R. D. Grigorieff, *Stability of multistep-methods on variable grids*, Numerische Mathematik 42 (1983), 359–377, https://doi.org/10.1007/BF01389580 . Abstract inspected; full text unavailable.
- M. Calvo, T. Grande, R. D. Grigorieff, *On the zero stability of the variable order variable stepsize BDF-Formulas*, Numerische Mathematik 57 (1990), 39–50, https://doi.org/10.1007/BF01386395 . Author's January 30, 2015 public upload: https://www.researchgate.net/publication/226854075_On_the_zero_stability_of_the_variable_order_variable_stepsize_BDF-Formulas . Full text unavailable.
- N. Guglielmi, M. Zennaro, *On the zero-stability of variable stepsize multistep methods: The spectral radius approach*, Numerische Mathematik 88 (2001), 445–458, https://doi.org/10.1007/s211-001-8010-0 . Abstract inspected.
- G. Söderlind, I. Fekete, I. Faragó, *On the zero-stability of multistep methods on smooth nonuniform grids*, BIT Numerical Mathematics 58 (2018), 1125–1143, https://doi.org/10.1007/s10543-018-0716-y . Open full article inspected.
