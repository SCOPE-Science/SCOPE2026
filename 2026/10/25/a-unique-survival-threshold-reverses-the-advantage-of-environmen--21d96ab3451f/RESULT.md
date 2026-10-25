# A unique survival threshold reverses the advantage of environmental persistence in a two-stage population

## Finding

Consider the two-stage positive population projection matrices
\[
A_i(s)=u v_i^{\mathsf T}+s\operatorname{diag}(b,c),\qquad i\in\{0,1\},\quad s>0,
\]
with \(u=(u_1,u_2)^{\mathsf T}\), \(v_i=(x_i,y_i)^{\mathsf T}\), all vector coordinates positive, and \(0<b<c\). Assume the strict tradeoff
\[
x_0>x_1>0,\qquad 0<y_0<y_1,\qquad
u_1x_0+u_2y_0>u_1x_1+u_2y_1.
\]
Denote the Perron eigenvalue by \(\lambda_i(s)=\rho(A_i(s))\) and define two equally frequent deterministic environmental schedules:
\[
g_{\rm alt}(s)=\frac12\log\rho(A_1(s)A_0(s)),\qquad
 g_{\rm block}(s)=\frac12\log(\lambda_0(s)\lambda_1(s)).
\]
The second expression is the limiting per-time growth rate of successively longer equal blocks: it equals the limit as \(m\to\infty\), through positive integers, of \((2m)^{-1}\log\rho(A_1(s)^m A_0(s)^m)\). In contrast, the first is the exact rate of perfect alternation.

**Theorem.** The unique positive crossover parameter is
\[
\boxed{
 s_*=\frac{u_1(x_0-x_1)-u_2(y_1-y_0)}{c-b}
 \left(\frac{x_0}{x_0-x_1}+\frac{y_0}{y_1-y_0}\right).
}
\]
For \(0<s<s_*\) one has \(g_{\rm block}(s)>g_{\rm alt}(s)\); equality holds exactly at \(s=s_*\); and for \(s>s_*\) one has \(g_{\rm block}(s)<g_{\rm alt}(s)\). Thus the advantage of persistent environments switches exactly once as common stage retention increases.

At the same crossover, the two projection matrices have both a common Perron eigenvalue \(\Lambda_*>0\) and a common strictly positive right Perron eigenvector \(w\). Consequently **every** finite or infinite switching arrangement, including arrangements with unequal environmental frequencies, has per-step asymptotic logarithmic growth \(\log\Lambda_*\) when applied to any strictly positive initial population vector. This order-indifference is stronger than equality of the two benchmark schedules.

## Assumptions and scope

The matrices describe a positive linear, density-independent, two-stage population model in which the environment changes the vector of stage-specific recruitment coefficients \(v_i\), while the distribution of recruits \(u\) and the diagonal stage-retention ratios \(b<c\) are unchanged. Parameter \(s\) scales both retention coefficients together. The ordered tradeoff means that environment 0 gives more recruitment from stage 1 but less from stage 2, with larger weighted aggregate recruitment in environment 0 before retention acts.

All entries and inequalities stated in the theorem are strict. There is no stochastic independence assumption: the two schedules are deterministic products. Matrix spectral radii, not mean one-year abundances, determine asymptotic growth. The two-stage and rank-one-recruitment structure are essential; no theorem is asserted for arbitrary positive matrices, three or more stages, unequal common retention directions, or all frequencies away from the crossover. Values of \(s\) for which \(sb\) or \(sc\) exceed one are algebraically admissible but may not represent literal survival probabilities without rescaling. The theorem also applies in physically bounded ranges whenever they contain \(s_*\).

## Proof

**1. Positivity and eigenvalue normalization.** Each \(A_i(s)\) is strictly positive. Its determinant is
\[
\det A_i(s)=s(cu_1x_i+bu_2y_i)+s^2bc>0.
\]
Thus its two real eigenvalues obey \(0<\mu_i(s)<\lambda_i(s)\), where the strict inequality follows from positive off-diagonal entries. Writing the Perron eigenrelation as
\[
(\lambda_i I-s\operatorname{diag}(b,c))r_i=u(v_i^{\mathsf T}r_i),
\]
one obtains \(\lambda_i>sc\) and may normalize the right Perron vector to
\[
r_i=\begin{pmatrix}u_1/(\lambda_i-sb)\\u_2/(\lambda_i-sc)\end{pmatrix}.
\]
The remaining scalar eigenvalue equation is
\[
1=\frac{u_1x_i}{\lambda_i-sb}+\frac{u_2y_i}{\lambda_i-sc},\qquad \lambda_i>sc.
\tag{1}
\]
For every fixed \(s>0\), the right side decreases strictly from infinity to zero as \(\lambda_i\) increases from \(sc\) to infinity; hence equation (1) uniquely characterizes \(\lambda_i\).

**2. A unique coincidence of Perron roots.** Put \(\Delta x=x_0-x_1>0\) and \(\Delta y=y_1-y_0>0\). Since \(u_1\Delta x>u_2\Delta y\), the ratio
\[
R=\frac{u_2\Delta y}{u_1\Delta x}
\]
lies strictly between zero and one. If \(\lambda_0(s)=\lambda_1(s)=L\), subtracting the two instances of (1) gives
\[
\frac{u_1\Delta x}{L-sb}=\frac{u_2\Delta y}{L-sc},
\qquad
L-s c=R(L-s b).
\]
Hence \(L=s(c-Rb)/(1-R)\). Substitution into (1) for environment 0 gives
\[
s=\frac{1-R}{c-b}\left(u_1x_0+\frac{u_2y_0}{R}\right)=s_*.
\]
Conversely, at this strictly positive \(s_*\), that displayed value of \(L\) solves both eigenvalue equations and exceeds \(s_*c\). Thus there is precisely one positive coincidence.

As \(s\downarrow0\), \(\lambda_i(s)\to u_1x_i+u_2y_i\); therefore \(\lambda_0>\lambda_1\) for small positive \(s\). As \(s\to\infty\), equation (1) gives \(\lambda_i(s)=sc+u_2y_i+O(s^{-1})\), so \(\lambda_1>\lambda_0\) for large \(s\). Continuity and uniqueness of their crossing imply
\[
\operatorname{sgn}(\lambda_0(s)-\lambda_1(s))=\operatorname{sgn}(s_*-s).
\tag{2}
\]

**3. Ordering of right and left Perron rays.** Direct calculation from the chosen right eigenvectors shows
\[
\det[r_0,r_1]=\frac{u_1u_2s(c-b)(\lambda_0-\lambda_1)}{
(\lambda_0-sb)(\lambda_0-sc)(\lambda_1-sb)(\lambda_1-sc)}.
\tag{3}
\]
All denominators are positive, so this determinant has the sign of \(\lambda_0-\lambda_1\).

Let \(\ell_i>0\) be a left Perron column vector, normalized so that its second coordinate is one. Writing its first coordinate as \(z_i>0\), the left eigenvalue equations give
\[
u_1y_i z_i^2+[s(c-b)+u_2y_i-u_1x_i]z_i-u_2x_i=0.
\tag{4}
\]
For fixed positive parameters, the quadratic has exactly one positive root. At that root the derivative of its left side with respect to \(z_i\) is positive. Its derivative with respect to \(x_i\) is \(-u_1z_i-u_2<0\), while the derivative with respect to \(y_i\) is \(u_1z_i^2+u_2z_i>0\). Therefore that positive root increases strictly with \(x_i\) and decreases strictly with \(y_i\). The assumed fertility tradeoff yields \(z_0>z_1\). In particular,
\[
\det[\ell_0,\ell_1]=z_0-z_1>0.
\tag{5}
\]

**4. Product-growth comparison.** Set \(P_i=r_i\ell_i^{\mathsf T}/(\ell_i^{\mathsf T}r_i)\). Since \(A_i\) is two dimensional, diagonalizable, and has eigenvalues \(\lambda_i>\mu_i>0\), it has the spectral decomposition
\[
A_i=\mu_i I+(\lambda_i-\mu_i)P_i.
\]
Multiplication and taking traces yields
\[
\operatorname{tr}(A_0A_1)-(\lambda_0\lambda_1+\mu_0\mu_1)
=(\lambda_0-\mu_0)(\lambda_1-\mu_1)(\operatorname{tr}(P_0P_1)-1).
\]
The elementary two-dimensional determinant identity gives
\[
\operatorname{tr}(P_0P_1)-1
=-\frac{\det[r_0,r_1]\det[\ell_0,\ell_1]}
{(\ell_0^{\mathsf T}r_0)(\ell_1^{\mathsf T}r_1)}.
\tag{6}
\]
Let \(X=\lambda_0\lambda_1\). The characteristic polynomial of \(A_0A_1\), evaluated at \(X\), equals
\[
X\bigl(\lambda_0\lambda_1+\mu_0\mu_1-\operatorname{tr}(A_0A_1)\bigr).
\]
Because \(\det(A_0A_1)=\lambda_0\lambda_1\mu_0\mu_1\) and \(X>\sqrt{\det(A_0A_1)}\), the sign of this characteristic-polynomial value is exactly the sign of \(X-\rho(A_0A_1)\). Using (3)–(6), all remaining factors are positive, so
\[
\operatorname{sgn}\bigl(\lambda_0\lambda_1-\rho(A_0A_1)\bigr)
=\operatorname{sgn}(\lambda_0-\lambda_1).
\tag{7}
\]
Taking logarithms and combining with (2) proves all three strict/equality alternatives for \(g_{\rm block}-g_{\rm alt}\).

**5. The strong equality case.** At \(s=s_*\), both Perron eigenvalues equal \(\Lambda_*\). The displayed formula for \(r_i\) depends only on \(s,\lambda_i,u,b,c\), so the two positive right Perron eigenvectors coincide. Denote their common ray by \(w\). Each matrix satisfies \(A_i(s_*)w=\Lambda_*w\). For any initial positive population vector \(p\), choose \(0<\alpha\le\beta\) so that \(\alpha w\le p\le\beta w\) componentwise. Every length-\(n\) positive matrix product \(M_n\) in these two matrices obeys
\[
\alpha\Lambda_*^n w\le M_n p\le\beta\Lambda_*^n w.
\]
Taking the logarithm of any positive monotone norm and dividing by \(n\) shows convergence to \(\log\Lambda_*\) uniformly in the environment sequence. This proves the schedule-indifference statement.

**6. The long-block limit.** For each fixed \(s>0\), Perron–Frobenius spectral decomposition gives \(A_i^m=\lambda_i^m(P_i+(\mu_i/\lambda_i)^m(I-P_i))\). The product of these expressions, normalized by \((\lambda_0\lambda_1)^m\), tends to \(P_1P_0\), whose sole nonzero eigenvalue \(\operatorname{tr}(P_1P_0)\) is strictly positive. Consequently \(\lim_{m\to\infty}(2m)^{-1}\log\rho(A_1^m A_0^m)=\frac12\log(\lambda_0\lambda_1)\), validating the operational interpretation of \(g_{\rm block}\).

## Verification

All formulas can be reproduced using the standalone file `verify.py` supplied with this result; execute `python verify.py` in the same directory. The program uses rational arithmetic for the exact crossover example and independently implemented two-by-two Perron eigenvalues for finite stress tests. These checks support, but do not replace, the universal proof above.

For
\[
u=(1,1)^{\mathsf T},\quad v_0=(2,1)^{\mathsf T},\quad
v_1=(1,19/10)^{\mathsf T},\quad (b,c)=(1/4,3/4),
\]
the exact values are \(s_*=28/45\), \(\Lambda_*=49/15\), and a common right eigenvector \(w=(9,10)^{\mathsf T}\). Direct fraction arithmetic confirms \(A_i(s_*)w=(49/15)w\) for both environments. The block-minus-alternation logarithmic growth gaps are approximately \(+0.0001273701223469\) at \(s=1/4\) and \(-0.0004054717878462\) at \(s=1\). Both of those retention parameters have \(0<sb<sc<1\).

The verifier independently generated 12,000 admissible parameter choices, testing sign regimes and numerical equality at the threshold; it reported 10,469 strict-regime checks, 1,531 threshold checks and a maximal floating-point equality residual about \(2.22\times10^{-16}\). The theorem is not based on finite enumeration.

## Relationship to prior work

Environmental temporal autocorrelation can affect long-run growth of structured populations: this is established in Tuljapurkar and Haridas (2006). The present exact periodic-versus-persistent comparison is not an assertion that this qualitative phenomenon is new. Engen et al. (2013) analyze autocorrelation contributions in age-structured populations, including a recruitment-variation example, but the complete accessible theoretical exposition does not state the positive-matrix one-crossing threshold under the present tradeoff. Steinsaltz, Tuljapurkar, and Horvitz (2011) derive sensitivities to Markov-environment transition parameters; that general derivative framework does not by itself state the finite amplitude, opposite-endpoint period comparison or its exact common-Perron-ray point. Altenberg (2013) studies related spectral product inequalities, principally products related by multiplicative diagonal matrices and commuting/symmetrizable factorizations; the full accessible preprint does not establish the additive, noncommuting rank-one-plus-diagonal two-environment threshold here. Protasov and Logofet (2014) directly study rank-one fertility corrections of demographic transition matrices and identify the second-eigenvalue location, but their full accessible account concerns the spectrum of single matrices rather than growth of the alternating product relative to long environmental blocks. The exact rank-one product limit at \(s=0\) is elementary and is not a novelty claim.

## Limitations

This is a deterministic two-pattern ordering theorem, not a universal monotonicity theorem for every Markov environmental correlation coefficient. Physical identification of environmental recurrence and stage carry-over requires model calibration. Strong schedule-indifference is asserted only at \(s=s_*\); it does not assert finite-time equality for different initial population vectors or different transient prefactors. Positivity, the two-stage assumption, common recruit direction, diagonal retention, and strictly opposed recruitment tradeoffs are indispensable to the proof. The original 2006 article was not fully accessible during comparison; the 2011 arXiv preprint, the 2013 ecological full text, and the 2013 spectral-inequality preprint were examined; a stronger or differently formulated historical theorem may cover portions of the result. Priority should be checked independently before publication.

## References

1. Tuljapurkar, S., and Haridas, C. V. (2006), "Temporal autocorrelation and stochastic population growth," *Ecology Letters* 9:327–337. First online 25 January 2006. https://doi.org/10.1111/j.1461-0248.2006.00881.x
2. Engen, S., et al. (2013), "Estimating the effect of temporally autocorrelated environments on the demography of density-independent age-structured populations," *Methods in Ecology and Evolution* 4:573–584. https://doi.org/10.1111/2041-210X.12043
3. Steinsaltz, D., Tuljapurkar, S., and Horvitz, C. (2011), "Derivatives of the stochastic growth rate," *Theoretical Population Biology* 80:1–15. https://doi.org/10.1016/j.tpb.2011.03.004 ; preprint https://arxiv.org/abs/1002.1424
4. Altenberg, L. (2013), "On the ordering of spectral radius product \(r(A)r(AD)\) versus \(r(A^2D)\) and related applications," *SIAM Journal on Matrix Analysis and Applications*. https://arxiv.org/abs/1301.4969
5. Protasov, V. Yu., and Logofet, D. O. (2014), "Rank-One Corrections of Nonnegative Matrices, With an Application to Matrix Population Models," *SIAM Journal on Matrix Analysis and Applications* 35:749–764. https://doi.org/10.1137/130935537
