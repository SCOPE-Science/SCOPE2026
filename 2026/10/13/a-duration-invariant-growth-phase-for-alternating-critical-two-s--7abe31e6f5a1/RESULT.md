# A duration-invariant growth phase for alternating critical two-stage populations

## Finding
Let \(A=L(j_A,f_A)\) and \(B=L(j_B,f_B)\) be two individually neutral two-stage ecological projection matrices as defined below. For every pair of positive integer spell lengths \(m,n\), the spectral growth factor of the repeating regime \(A^mB^n\) is above, below, or equal to one according to a single signed product:
\[
\begin{aligned}
\rho(A^mB^n)>1&\iff(j_A-j_B)(f_A-f_B)<0,\\
\rho(A^mB^n)<1&\iff(j_A-j_B)(f_A-f_B)>0,\\
\rho(A^mB^n)=1&\iff(j_A-j_B)(f_A-f_B)=0.
\end{aligned}
\]
Thus a tradeoff between juvenile maturation survival and adult fecundity across individually neutral environments generates growth, while concordant shifts generate decline. The result holds for every positive duration of each uninterrupted environmental spell, not only alternating single periods.

A sharp identity supporting the phase classification is
\[
\det(I-A^mB^n)=
\frac{1-(-j_A f_A)^m}{1+j_A f_A}
\frac{1-(-j_B f_B)^n}{1+j_B f_B}
(j_A-j_B)(f_A-f_B).
\]
Moreover, for every \(0<t<1\), the convex environment average \(C_t=(1-t)A+tB\) satisfies
\[
\det(I-C_t)=t(1-t)(j_A-j_B)(f_A-f_B),
\]
so averaging and blocked alternation agree on which side of critical growth the population lies. The exact long-spell limit is
\[
\lim_{m,n\to\infty}\rho(A^mB^n)
=\frac{(1+j_A f_B)(1+j_B f_A)}{(1+j_A f_A)(1+j_B f_B)}.
\]

## Assumptions and scope
The population state is \((\text{adults},\text{juveniles})^\mathsf T\). One time step in an environment with maturation survival \(j\) and adult fecundity \(f\) follows the linear projection
\[
L(j,f)=\begin{pmatrix}s&j\\f&0\end{pmatrix},\qquad s=1-jf,
\]
where \(0<j\le1\), \(f>0\), and \(0<jf<1\), so the adult survival probability \(s\) lies strictly between zero and one. Juveniles do not survive indefinitely within their stage: those who survive maturation become adults in the next step. Each isolated environment is at critical demographic replacement by construction. With two fixed distinct regimes \(A\) and \(B\), one period consists of \(m\ge1\) steps of one regime and \(n\ge1\) steps of the other; the order does not affect the monodromy eigenvalues because the two block products are cyclic permutations. Growth means growth of deterministic expected-stage population counts, not almost-sure survival of a finite stochastic population.

## Proof
**Isolated criticality.** The characteristic polynomial is \((\lambda-1)(\lambda+jf)\). Since \(0<jf<1\), the nonnegative matrix is primitive, its Perron eigenvalue is exactly \(1\), and its other eigenvalue is \(-jf\). Set \(q_A=-j_A f_A\) and \(q_B=-j_B f_B\), each in \((-1,0)\).

**Powers of the neutral matrices.** Cayley–Hamilton, or interpolation at eigenvalues \(1\) and \(q_A\), gives for every integer \(m\ge1\)
\[
A^m=I+\alpha_m(A-I),\quad \alpha_m=\frac{1-q_A^m}{1-q_A}>0.
\]
Similarly, \(B^n=I+\beta_n(B-I)\) with \(\beta_n=(1-q_B^n)/(1-q_B)>0\). Write \(X=A-I\), \(Y=B-I\). Since \(\mathrm{tr}(X)=q_A-1\), \(\mathrm{tr}(Y)=q_B-1\), the product \(P=A^mB^n\) has
\[
\mathrm{tr}(P)=q_A^m+q_B^n+\alpha_m\beta_n\mathrm{tr}(XY),\qquad
\det(P)=q_A^m q_B^n.
\]
Therefore
\[
\begin{aligned}
\det(I-P)&=1-\mathrm{tr}(P)+\det(P)\\
&=(1-q_A^m)(1-q_B^n)-\alpha_m\beta_n\mathrm{tr}(XY)\\
&=\alpha_m\beta_n\big[(1-q_A)(1-q_B)-\mathrm{tr}(XY)\big]\\
&=\alpha_m\beta_n\det(I-AB).
\end{aligned}
\]
Here the last equality follows by applying the same trace–determinant calculation with \(m=n=1\). Direct multiplication of the two explicitly specified two-stage matrices gives
\[
\det(I-AB)=(j_A-j_B)(f_A-f_B).
\]
This establishes the determinant identity with all hypotheses and quantifiers.

**Spectral phase.** Each one-step matrix has positive entries except its bottom-right zero; hence \(P=A^mB^n\) is strictly positive for all \(m,n\ge1\). Perron–Frobenius gives two real eigenvalues \(r=\rho(P)>0\) and \(\eta\), with \(|\eta|<r\). Also \(|\det P|=(j_A f_A)^m(j_B f_B)^n<1\). If \(r\ge1\), then \(|\eta|=|\det P|/r<1\); if \(r<1\), then \(|\eta|<r<1\). Thus \(1-\eta>0\) always, and
\[
\operatorname{sgn}\det(I-P)=\operatorname{sgn}[(1-r)(1-\eta)]=\operatorname{sgn}(1-r).
\]
The two positive power factors preserve the sign of \((j_A-j_B)(f_A-f_B)\), proving the three cases, including equality.

**Averaged environment.** Both \(A\) and \(B\) have \(\det(I-A)=\det(I-B)=0\). Expanding the determinant of \(I-[(1-t)A+tB]\) as a quadratic in \(t\) yields
\[
\det(I-C_t)=t(1-t)\det(I-AB)=t(1-t)(j_A-j_B)(f_A-f_B).
\]
For \(0<t<1\), the averaged matrix has strictly positive off-diagonal entries and zero bottom-right entry, hence determinant \(-\bar j\,\bar f<0\) with \(\bar j=(1-t)j_A+tj_B>0\) and \(\bar f=(1-t)f_A+tf_B>0\). Its two real eigenvalues have opposite signs; the negative eigenvalue \(\eta<0\) gives \(1-\eta>0\), so \(\operatorname{sgn}\det(I-C_t)=\operatorname{sgn}(1-\rho(C_t))\) without any bound on the modulus of the negative eigenvalue. Consequently its Perron root shares the blocked-cycle phase classification.

**Long spells.** The spectral projector of \(L(j,f)\) for eigenvalue one is
\[
\Pi(j,f)=\frac{1}{1+jf}\begin{pmatrix}1&j\\f&jf\end{pmatrix}
=\frac{(1,f)^\mathsf T(1,j)}{1+jf}.
\]
Its complementary mode decays as \((-jf)^m\), so \(A^m\to\Pi(j_A,f_A)\) and \(B^n\to\Pi(j_B,f_B)\). The rank-one product of these projectors has nonzero eigenvalue
\[
\frac{(1+j_A f_B)(1+j_B f_A)}{(1+j_A f_A)(1+j_B f_B)}.
\]
Continuity of the spectral radius proves the stated limit. The per-step growth multiplier, \(\rho(A^mB^n)^{1/(m+n)}\), tends to one even when the per-cycle limit differs from one.

## Verification
The standalone file `check_periodic_population.py` (Python standard library only) checks the determinant identity in exact rational arithmetic for 169 ordered parameter pairs and every \(m,n\in\{1,\ldots,8\}\), totaling 10,816 exact block cases. It also checks the convex-average determinant identity on a rational parameter grid, two explicit sign examples, and the rank-one projector limit. Run `python check_periodic_population.py` from the extracted package directory; the expected final output starts with `VERIFY_OK`. These finite checks illustrate and guard the algebra but do not establish the unbounded quantifier over positive spell lengths, which is proved above.

For growth, choose \((j_A,f_A)=(1/2,1)\) and \((j_B,f_B)=(1/4,2)\). Both one-step matrices are neutral and have adult survival \(1/2\), but \(\rho(AB)=(3+\sqrt5)/4>1\). For decay choose \((j_A,f_A)=(1/4,1)\) and \((j_B,f_B)=(1/2,3/2)\); now \(\det(I-AB)=1/8>0\), so \(\rho(AB)<1\). The exact sign identity extends both examples to every positive pair of spell lengths.

## Relationship to prior work
Classical periodic matrix demography, including Caswell–Trevisan (1994) and Caswell (2019), treats growth and sensitivity through products of environment-specific matrices; Cushing (2006) studies how the phase of fertility and survival variation changes persistence thresholds in a juvenile–adult model. Cushing–Ackleh (2011) derives a general periodic net reproduction framework, including formulas for period-two Leslie systems. The present specialized result imposes a distinct fixed criticality condition on *each* environment and proves a complete sign classification uniform over *all* two-block durations, together with an exact limiting multiplier and a temporal-averaging comparison. It is not a general formula for the spectral radius of arbitrary periodic products.

## Limitations
The matrices describe a linear, deterministic, closed, spatially homogeneous population with precisely two stages and critically balanced isolated regimes. The classification does not cover arbitrary multiblock sequences, stochastic environments, density dependence, dispersal, measurement uncertainty, or regimes outside \(0<jf<1\). Excluding the \(jf=1\) boundary is important for strict positivity of the power factors, and the exact statements are not extended across that boundary. Prior work on periodic demographic tradeoffs is extensive; although targeted comparisons did not identify this full uniform-duration classification, possible older or inaccessible stronger coverage remains a scientific residual risk.

## References
1. Caswell, H., and Trevisan, M. C. (1994). *Sensitivity Analysis of Periodic Matrix Models*. Ecology 75, 1299–1303. DOI: 10.2307/1937455. First online 1994-07-01.
2. Cushing, J. M. (2006). *A juvenile-adult model with periodic vital rates*. Journal of Mathematical Biology 53, 520–539. DOI: 10.1007/s00285-006-0382-6. First public 2006-04-24.
3. Cushing, J. M., and Ackleh, A. S. (2011 online). *A net reproductive number for periodic matrix models*. Journal of Biological Dynamics 6, 166–188. DOI: 10.1080/17513758.2010.544410. First online 2011-02-18.
4. Caswell, H. (2019). *Periodic Models*. In *Sensitivity Analysis: Matrix Methods in Demography and Ecology*, chapter 8. DOI: 10.1007/978-3-030-10534-1_8.
