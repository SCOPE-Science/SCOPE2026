# An exact three-mode accuracy barrier for positive-residue parallel exponential propagators

## Finding
Fix a time \(t>0\). Consider approximating \(e^{-tA}\) for a real symmetric positive-semidefinite matrix \(A\) by a *positive-residue parallel resolvent sum*
\[
 R(A)=cI+\sum_{j=1}^{m}w_j(A+s_jI)^{-1},\qquad
 m\ge0,\quad c\ge0,\quad w_j\ge0,\quad s_j>0.
\]
There is no restriction on the finite number of distinct positive shifts. For \(h=(\log3)/t\) and \(A_0=h\operatorname{diag}(0,1,2)\), the exact minimax spectral-norm error over this entire class is
\[
 \boxed{\inf_R\|R(A_0)-e^{-tA_0}\|_2=E_*:=\frac{2\sqrt3-3}{9}=0.051566846126417\ldots.}
\]
Equality is attained by a *single* resolvent,
\[
 R_*(A_0)=\frac{w_*h}{A_0+s_*hI},\qquad
 s_*:=\frac{\sqrt3-1}{2},\qquad w_*:=\frac{2\sqrt3}{9},
\]
whose errors on the three eigenvalues are exactly \((+E_*,-E_*,+E_*)\). Every equality case has the same effective pole; splitting its positive weight among identical poles changes nothing.

More generally, on \(\operatorname{diag}(0,h,2h)\), writing \(q=e^{-th}\in(0,1)\), the exact minimax error is the unique positive root \(E(q)\) of
\[
 4E(q)^2+(3-2q+3q^2)E(q)-q(1-q)^2=0.
\]
It is attained by one positive resolvent with normalized pole \(\alpha_q=u_q/(1-u_q)\) and normalized weight \(\alpha_q(1+E(q))\), where \(u_q=(q-E(q))/(1+E(q))\). The strict global maximum of \(E(q)\) occurs at \(q=1/3\), giving the displayed universal three-mode certificate.

The barrier is **not** an artifact of a zero eigenvalue. For the strictly positive-definite matrix
\[
 A_{1/4}=h\operatorname{diag}\!\left(\tfrac14,\tfrac54,\tfrac94\right),
 \qquad \kappa_2(A_{1/4})=9,
\]
the exact minimax error is
\[
 \boxed{\inf_R\|R(A_{1/4})-e^{-tA_{1/4}}\|_2=3^{-1/4}E_*=0.039182329883356\ldots.}
\]
One attaining member is \(R(A)=3^{-1/4}w_*h\bigl(A+(s_*-\tfrac14)hI\bigr)^{-1}\), whose shift is strictly positive.

## Assumptions and scope
All matrices are finite-dimensional real symmetric, all norms above are operator \(2\)-norms, and every inverse is of a strictly positive shift of a positive-semidefinite or positive-definite matrix. The scalar \(c\) is optional; allowing it does not improve the optimum. Both \(t\) and the spectral spacing \(h\) are strictly positive. The class is **only** finite nonnegative sums of *simple shifted inverses* plus a nonnegative constant; products, signed coefficients, higher-order poles, and unrestricted rational functions are not included. The stated universal maximum is over three equally spaced **nonnegative** eigenvalues whose bottom one is zero, and not over all possible spectral geometries or all approximation algorithms.

## Proof
**1. A three-point Stieltjes constraint.** Let \(r(x)=c+\sum_jw_j/(x+s_j)\) with \(c,w_j\ge0\), \(s_j>0\), and write \(r_i=r(\lambda_0+ih)\) for \(i=0,1,2\), where \(\lambda_0\ge0\), \(h>0\). When \(r_0>0\), form a probability distribution using each contribution \(w_j/(\lambda_0+s_j)\) to \(r_0\), and the constant contribution \(c\). Associate to the former the parameter \(u_j=(\lambda_0+s_j)/(\lambda_0+s_j+h)\in(0,1)\), and to the latter the parameter \(u=1\). Its first moment is \(r_1/r_0\), while its expectation of \(f(u)=u/(2-u)\) is \(r_2/r_0\). Since \(f''(u)=4/(2-u)^3>0\) on \([0,1]\), Jensen's inequality gives
\[
 \frac{r_2}{r_0}\ge f\!\left(\frac{r_1}{r_0}\right),\qquad
 \boxed{r_2\ge\frac{r_0r_1}{2r_0-r_1}.}
\]
The denominator is positive because \(0<r_1\le r_0\). If \(r_0=0\), then all terms vanish, yielding error at least one against the normalized target; this cannot minimize the error. Equality in Jensen requires all positive contributions to have a common \(u\); if that \(u<1\), it forces \(c=0\) and a single effective shift.

**2. Exact error lower bound.** First take \(\lambda_0=0\) and set \(q=e^{-th}\in(0,1)\). If the three uniform errors are at most \(\varepsilon\), then
\[
 r_0\le1+\varepsilon,\qquad r_1\ge q-\varepsilon,
 \qquad r_2\le q^2+\varepsilon.
\]
For \(0\le\varepsilon<q\), the function \(H(x,y)=xy/(2x-y)\) is decreasing in \(x\) and increasing in \(y\) whenever \(0<y\le x\). Therefore Jensen's inequality implies
\[
 q^2+\varepsilon\ge H(1+\varepsilon,q-\varepsilon)
 =\frac{(1+\varepsilon)(q-\varepsilon)}{2+3\varepsilon-q}.
\]
Clearing the strictly positive denominator gives
\[
 F(\varepsilon,q):=4\varepsilon^2+(3-2q+3q^2)\varepsilon-q(1-q)^2\ge0.
\]
For each \(q\in(0,1)\), the function \(F(\cdot,q)\) increases strictly from a negative value on \([0,\infty)\), and its positive root \(E(q)\) belongs to \((0,q)\). If \(\varepsilon\ge q\), the same required inequality \(\varepsilon\ge E(q)\) is automatic. Thus every allowed \(r\) has error at least \(E(q)\).

**3. Attainment and rigidity.** Set \(u_q=(q-E(q))/(1+E(q))\in(0,1)\) and \(\alpha_q=u_q/(1-u_q)>0\). Then
\[
 r_*(x)=\frac{h\alpha_q(1+E(q))}{x+h\alpha_q}
\]
satisfies \(r_*(0)=1+E(q)\), \(r_*(h)=q-E(q)\), and—by \(F(E(q),q)=0\)—\(r_*(2h)=q^2+E(q)\). Hence the lower bound is attained. Any minimizer must saturate each of the three error inequalities as well as strict Jensen convexity, which forces the same effective \(u_q\) and excludes positive constant mass. This proves the one-pole characterization, up to duplicating the same pole.

**4. Sharp spectral spacing.** Differentiate \(F(E(q),q)=0\). Direct simplification gives
\[
 E'(q)=-\frac{(3q-1)(2E(q)+1-q)}{8E(q)+3-2q+3q^2}.
\]
All factors except \(3q-1\) in the numerator are positive. Thus \(E(q)\) increases strictly for \(q<1/3\) and decreases strictly for \(q>1/3\). At \(q=1/3\), the defining equation reduces to \(27E^2+18E-1=0\), whose positive root is \(E_*=(2\sqrt3-3)/9\). Substitution into the one-pole formula gives \(s_*=(\sqrt3-1)/2\) and \(w_*=2\sqrt3/9\).

**5. Positive-definite witness.** With \(\delta=1/4\), write the three eigenvalues of \(A_{\delta}\) as \((\delta+i)h\). The exact semigroup values are \(3^{-\delta}(1,1/3,1/9)\), while the Jensen three-point inequality applies unchanged after any nonnegative common eigenvalue shift. Consequently the minimax error is at least \(3^{-\delta}E_*\). Since \(s_*>\delta\), the admissible positive shift \((s_*-\delta)h\) and weight \(3^{-\delta}w_*h\) attain precisely that error. The condition number is \((\delta+2)/\delta=9\), proving the SPD formula.

## Verification
The standard-library Python program `check.py` reconstructs all algebraic identities at 80-digit decimal precision, checks the sharp three-node error signs, verifies the strictly positive shifted-system pole, evaluates the root inequality at 999 interior spacing parameters, and tests 2,000 independently sampled positive resolvent mixtures against both the three-point Jensen bound and the exact \(q=1/3\) error floor. Run `python check.py` from a directory containing this file. These finite calculations corroborate the formulas only: universal optimality, all dimensions, and all positive sums follow from the preceding analytical argument, not from enumeration.

## Relationship to prior work
Güttel and Shao's 2026 research on uniform-in-time rational approximation of matrix exponentials motivates sums of shifted real-pole resolvent solves as an efficient parallel computational primitive. Publicly accessible companion computational scripts compute **unconstrained** partial-fraction coefficients by solving linear systems and therefore do not establish the minimax behavior under the additional sign restriction \(w_j\ge0\). Earlier unrestricted rational approximation theory likewise does not impose this residue cone. The present result isolates that cone's exact finite-spectrum error floor, identifies its unique effective attaining pole, optimizes the sampling spacing, and gives a moderate-condition-number SPD witness. Its Jensen inequality is classical, but the sharp constrained approximation calculation and full spectral quantification are the assessed contribution.

## Limitations
The stated constraint on residues is essential: negative residues, polynomial/rational compositions, repeated poles, and other methods may exceed this accuracy. The theorem is an exact obstruction on specified spectral triples and supplies a lower bound for matrices containing them; it is **not** a lower bound for all positive-operator propagators and does not assert a global minimax error on an entire continuous spectral interval. Numerical tests are finite. The motivating full manuscript and some historical sources were not available for page-by-page comparison, so unindexed or uninspected related literature remains a possible originality risk. No independent validation has been performed.

## References
1. S. Güttel and L. Shao, *Uniform-in-time rational approximation of the matrix exponential with real poles*, arXiv:2607.18018 (first public version July 20, 2026), https://arxiv.org/abs/2607.18018 .
2. Numerical Linear Algebra Group, public companion code for the preceding study, `drive_three_approximants.m` and `drive_time_uniform_error_1.m`, https://github.com/nla-group/uniform-in-time-exponential .
3. S. Güttel and L. Shao, *Concentrated real-pole uniform-in-time approximation*, arXiv:2511.21858 (first public version November 26, 2025), https://arxiv.org/abs/2511.21858 .
4. A. Schönhage, *Rational Approximation to \(e^{-x}\)*, SIAM Journal on Computing (1982), https://doi.org/10.1137/0719077 .
