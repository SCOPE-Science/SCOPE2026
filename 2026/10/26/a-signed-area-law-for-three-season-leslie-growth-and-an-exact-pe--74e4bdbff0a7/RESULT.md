# A signed-area law for three-season Leslie growth and an exact persistence window

## Finding

Consider the two-age, density-independent Leslie population model with **three distinct seasonal environments**, each applied once per repeated three-step cycle. Assume the juvenile and adult fecundities and maturation probabilities have the form
\[
 A_i(b)=\begin{pmatrix} f_i&b\\s_i&0\end{pmatrix},\qquad f_i>0,\quad 0<s_i\leq1,\quad b>0,\quad i=1,2,3.
\]
The adult fecundity \(b\) is common to the seasons, whereas juvenile fecundity \(f_i\) and maturation probability \(s_i\) can covary. A chronological cycle \((i,j,k)\) has three-step projection matrix \(M_{ijk}=A_k(b)A_j(b)A_i(b)\). Its dominant three-step multiplier is \(R_{ijk}=\rho(M_{ijk})\), so growth per step is \(R_{ijk}^{1/3}\).

Put
\[
 F=f_1f_2f_3,\quad Q=s_1s_2s_3,\quad
 L_+=f_1s_3+f_2s_1+f_3s_2,\quad
 L_-=f_1s_2+f_2s_3+f_3s_1,
\]
\[
 \Delta=L_+-L_-=f_1(s_3-s_2)+f_2(s_1-s_3)+f_3(s_2-s_1).
\]
The six chronological permutations split into precisely two cyclic classes. The class \((1,3,2),(3,2,1),(2,1,3)\) has multiplier
\[
 R_+(b)=\frac{F+bL_++\sqrt{(F+bL_+)^2+4b^3Q}}2;
\]
the class \((1,2,3),(2,3,1),(3,1,2)\) has the same formula with \(L_-\) in place of \(L_+\). Consequently,
\[
 \operatorname{sgn}(R_+(b)-R_-(b))=\operatorname{sgn}(\Delta).
\]
The order effect is **exactly absent**, for every \(b>0\), if and only if the three parameter points \((f_i,s_i)\) are collinear: \(\Delta\) is the negative of their signed double area. The geometry is independent of adult fecundity.

If \(F<1\) and \(\Delta>0\), there are unique critical fecundities \(0<b_+<b_-\), respectively determined by
\[
 1-F-b_+L_+-b_+^3Q=0,\qquad
 1-F-b_-L_--b_-^3Q=0.
\]
For **every** \(b\in(b_+,b_-)\), cycling the seasons in the positive-area orientation gives \(R_+>1\), whereas reversing that cycle gives \(R_-<1\). Below \(b_+\) both cycles decay exponentially; above \(b_-\) both grow exponentially. When \(\Delta<0\), the two labels interchange. If \(\Delta=0\), their persistence thresholds coincide. If \(F\geq1\), both cycles grow for every \(b>0\) and no mixed persistence window is possible.

For the exact admissible parameters
\[
 (f_1,f_2,f_3)=(1/5,1/2,9/10),\quad (s_1,s_2,s_3)=(1/5,4/5,1/2),\quad b=1,
\]
one obtains \(F=9/100\), \(Q=2/25\), \(L_+=23/25\), \(L_-=59/100\), and \(\Delta=33/100\). The positive-orientation cycle has trace \(101/100\) and \(1-\operatorname{tr}(M_+)+\det(M_+)=-9/100\), hence \(R_+>1\); the reverse cycle has trace \(17/25\) and the same expression \(6/25\), hence \(R_-<1\). The crossing values are numerically \(b_+\approx0.9211616242\) and \(b_-\approx1.2667517488\). This is an exact rational-data example where simply reversing the three seasons changes asymptotic growth into extinction.

## Assumptions and scope

There are exactly two age/stage classes, three discrete seasons repeated deterministically and without density feedback, positive fertilities, positive maturation probabilities at most one, and a common positive adult-fecundity parameter. Seasonal parameters are fixed, and each of the three environments is used exactly once per three-step cycle. Extinction/growth are asymptotic statements for all nonzero nonnegative initial vectors; a critical multiplier of one is **neutral** and is not counted as either exponential growth or decay. There is no claim about stochastic environmental variation, additional stage classes, stage-dependent feedback, finite-horizon counts, or nonlinear persistence.

## Proof

**1. Product invariants and orientation.** By direct multiplication in chronological order,
\[
 \operatorname{tr}(A_3A_2A_1)=f_1f_2f_3+b(f_1s_2+f_2s_3+f_3s_1)=F+bL_-,
\]
\[
 \operatorname{tr}(A_2A_3A_1)=f_1f_2f_3+b(f_1s_3+f_2s_1+f_3s_2)=F+bL_+.
\]
Cyclic permutations preserve trace, including for noninvertible matrices, so these identities cover all six orders. Since \(\det A_i=-bs_i\), both orientation classes have determinant \(-b^3Q\). Each product has strictly positive entries: the product of two such matrices is already strictly positive, and multiplication by a positive-on-its-support Leslie matrix preserves strict positivity. Thus there is one simple positive Perron eigenvalue \(R\) strictly exceeding the modulus of the other eigenvalue. Its characteristic equation is
\[
 R^2-(F+bL)R-b^3Q=0.
\]
The positive root yields the two displayed formulas. For \(x>0\), \(\partial[(x+\sqrt{x^2+4b^3Q})/2]/\partial x>0\); therefore its ranking is the sign of \(L_+-L_-\). The oriented determinant of rows \((f_i,s_i,1)\) is \(-\Delta\), which vanishes exactly when the three points are collinear, also covering repeated points. This proves the geometry and its sharp equality case.

**2. Persistence criterion.** For any positive trace \(T\) and positive \(V=b^3Q\), the characteristic polynomial \(p(z)=z^2-Tz-V\) has one positive and one negative real root, so \(p(1)=1-T-V\) is positive, zero, or negative exactly as its positive root is below, equal to, or above one. For each orientation this gives the explicit test
\[
 R_\pm(b)>1\quad\Longleftrightarrow\quad F+bL_\pm+b^3Q>1.
\]
All parameters \(L_\pm,Q\) are strictly positive. If \(F<1\), the function \(1-F-bL_\pm-b^3Q\) decreases strictly from a positive value to negative infinity on \(b\geq0\), so it has exactly one positive zero. If \(\Delta>0\), then \(L_+>L_-\): at any positive \(b\), the plus-oriented expression crosses one earlier; thus \(b_+<b_-\) and all asserted intervals follow. The inequalities reverse for \(\Delta<0\), coincide for \(\Delta=0\). If \(F\geq1\), strict positivity of \(bL_\pm+b^3Q\) gives \(R_\pm>1\) for all \(b>0\). At a threshold \(R=1\) while the other eigenvalue is strictly inside the unit circle, since the product is strictly positive and primitive; the system is neutral, not exponentially decaying.

**3. Actual population trajectories.** For any nonzero vector \(x_0\geq0\), strict positivity of the three-step monodromy ensures its Perron coefficient is strictly positive. The Perron–Frobenius decomposition then gives \(M^nx_0=cR^nv+o(R^n)\) for positive \(c,v\). At the two intermediate seasonal phases the same conclusion follows by multiplying by fixed nonnegative season matrices, which do not annihilate positive vectors. Hence the multiplier comparisons establish exponential extinction or growth at every phase, not only at cycle boundaries.

**4. Minimal period and witness.** For just two seasonal matrices, the two possible products \(AB\) and \(BA\) have equal trace and determinant, hence the same spectrum and asymptotic growth, whether or not either is invertible. Three seasons are therefore minimal for a strict ordering effect. The rational witness follows by substituting in step 1: \(1-T_+-b^3Q=-9/100<0\) while \(1-T_--b^3Q=6/25>0\). The displayed opposite persistence conclusions require no numerical approximation.

## Verification

A standalone standard-library script `verify.py` reproduces the rational witness, classifies all six chronological permutations, checks trace and determinant identities on 3,000 independently generated rational parameter triples, and computes the unique critical roots by bisection. Run `python3 verify.py` in a directory containing that file. Expected final lines include `PASS 3000 exact-rational six-permutation trace/determinant and ordering checks` and `PASS exact rational persistence witness with opposite signs at unit adult fertility`. The finite tests are corroboration; the four analytic steps above establish the universally quantified theorem.

## Relationship to prior work

Leslie (1945) introduced the age-structured matrix population framework and a Perron-eigenvalue growth analysis. Its accessible original text, including the matrix specification and dominant-root sections, provides the model foundation, not the present sharp three-season permutation theorem. Cushing and Ackleh (2012) analyze net reproductive number for general periodic matrix models, including detailed period-two Leslie cases, establishing relevant broader Floquet context. The accessible material does not state the signed-area orientation test or the exact mixed-growth window, but complete full-text comparison was not possible. Tuljapurkar and Haridas (2006) investigate population growth in variable environments, particularly stochastic environmental fluctuation; their nonidentical question concerns long-run random-environment effects rather than an exact deterministic three-year ordering comparison. In the special case where maturation is season-invariant, \(s_1=s_2=s_3\), the area vanishes, so fertility-only changes cannot generate the three-season orientation effect. More general positive-matrix-product ordering results could conceivably cover this case without matching model terminology; this is a stated limitation on the originality assessment.

## Limitations

The three-state seasonal scheduling comparison is a deterministic, linear, density-independent result; it neither quantifies finite-population extinction probability nor guarantees nonlinear persistence. A common adult-fecundity coefficient is essential to the compact displayed area formula; general season-varying adult fertility is not classified. Strict positivity excludes degenerate survival values of zero. Critical points are neutral, not classified as thriving or extinct. The explicitly inspected foundational text and accessible related source material are not a systematic proof that no older general theorem implies the result; complete comparison with one highly relevant periodic-Leslie article remains incomplete. Independent validation has not been performed.

## References

1. P. H. Leslie, *On the Use of Matrices in Certain Population Mathematics*, Biometrika 33 (1945), 183–212; DOI 10.1093/biomet/33.3.183. Public date 1945-11-01. Scanned original hosted at https://jxshix.people.wm.edu/2009-harbin-course/classic/leslie.pdf; publisher bibliographic record https://doi.org/10.1093/biomet/33.3.183.
2. J. M. Cushing and A. S. Ackleh, *A net reproductive number for periodic matrix models*, Journal of Biological Dynamics, 2012; DOI 10.1080/17513758.2010.544410. Accessible summaries and indexed sections reviewed; full text not fully inspected.
3. S. Tuljapurkar and C. V. Haridas, *Temporal autocorrelation and stochastic population growth*, Ecology Letters, 2006; DOI 10.1111/j.1461-0248.2006.00881.x. Accessible author-hosted manuscript text inspected.
