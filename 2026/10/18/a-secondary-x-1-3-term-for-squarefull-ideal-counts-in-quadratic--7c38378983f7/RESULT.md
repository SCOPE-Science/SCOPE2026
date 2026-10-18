# A secondary \(x^{1/3}\) term for squarefull ideal counts in quadratic fields

## Finding
Let \(K\) be any fixed quadratic number field and \(\mathcal O_K\) its ring of integers. An integral ideal \(I\ne0\) is **squarefull** if each prime ideal occurring in \(I\) occurs with exponent at least two. Write \(P_K(x)\) for the number of squarefull integral ideals of absolute norm at most \(x\), and \(\rho_K=\operatorname{Res}_{s=1}\zeta_K(s)>0\). Then
\[
P_K(x)=\rho_K\frac{\zeta_K(3/2)}{\zeta_K(3)}x^{1/2}+\rho_K\frac{\zeta_K(2/3)}{\zeta_K(2)}x^{1/3}+O_K\bigl(x^{3/10}\log(2x)\bigr)
\qquad(x\to\infty).
\]
The secondary coefficient is interpreted using analytic continuation of the Dedekind zeta function. For the Gaussian field \(K=\mathbb Q(i)\), the secondary coefficient is negative, since \(\zeta_K(s)=\zeta(s)\beta(s)\), \(\zeta(2/3)<0\) and \(\beta(2/3)>0\).

## Assumptions and scope
The field \(K\) is quadratic over \(\mathbb Q\), either real or imaginary, and is fixed as \(x\) tends to infinity. Ideals, not generators modulo units, are counted; the unit ideal is included. All constants in error estimates may depend on \(K\). No assumption about the ideal class group, GRH, or the nonvanishing of \(\zeta_K(2/3)\) is needed.

## Proof
Write \(A_K(y)\) for the number of all nonzero integral ideals of norm at most \(y\) and \(S_K(y)\) for those which are squarefree. The classical ideal-counting estimate for a quadratic field gives
\[
 A_K(y)=\rho_K y+O_K(y^{1/2})\qquad(y\ge1).
\tag{1}
\]
This also follows elementarily from \(\zeta_K(s)=\zeta(s)L(s,\chi_D)\), Dirichlet's hyperbola method, and bounded partial sums of the nonprincipal periodic quadratic character \(\chi_D\).

Every squarefree ideal is detected by \(\mu_K^2(I)=\sum_{J^2\mid I}\mu_K(J)\). Consequently, using (1),
\[
 S_K(y)=\sum_{N(J)\le\sqrt y}\mu_K(J)A_K(y/N(J)^2)
 =\kappa_K y+O_K(y^{1/2}\log(2y)),\qquad
 \kappa_K:=\frac{\rho_K}{\zeta_K(2)}.
\tag{2}
\]
Indeed the main coefficient follows by extending \(\sum_J\mu_K(J)N(J)^{-2}=1/\zeta_K(2)\), whose omitted tail contributes \(O_K(y^{1/2})\); the individual error terms contribute at most \(O_K(\sqrt y\sum_{N(J)\le\sqrt y}N(J)^{-1})=O_K(\sqrt y\log(2y))\).

By Abel summation of (1), for any fixed \(1/2<\sigma<1\),
\[
 \sum_{N(I)\le Y}N(I)^{-\sigma}
 =\frac{\rho_K}{1-\sigma}Y^{1-\sigma}+\zeta_K(\sigma)+O_K(Y^{1/2-\sigma}).
\tag{3}
\]
Similarly, by partial summation of (2),
\[
 \sum_{\substack{J\ \mathrm{squarefree}\\N(J)>Y}}N(J)^{-3/2}
 =2\kappa_K Y^{-1/2}+O_K(Y^{-1}\log(2Y)).
\tag{4}
\]
Unique prime-ideal factorization gives a unique decomposition \(I=A^2B^3\) for each squarefull ideal, where \(A\) is integral and \(B\) is squarefree. The factors need not be coprime. Hence the Dirichlet series is
\[
 \sum_{I\ \mathrm{squarefull}}N(I)^{-s}
 =\frac{\zeta_K(2s)\zeta_K(3s)}{\zeta_K(6s)}.
\tag{5}
\]
Put \(T=x^{1/5}\). Every admissible pair \((A,B)\) has \(N(A)\le T\) or \(N(B)\le T\), since otherwise \(N(A)^2N(B)^3>x\). Their intersection rectangle is automatically admissible. Thus the *exact* hyperbola identity is
\[
 P_K(x)=\sum_{\substack{B\ \mathrm{squarefree}\\N(B)\le T}}A_K\!\left(\sqrt{x/N(B)^3}\right)
 +\sum_{N(A)\le T}S_K\!\left((x/N(A)^2)^{1/3}\right)
 -A_K(T)S_K(T).
\tag{6}
\]
In the first sum, (1) and (4), together with \(\sum_{N(B)\le T}N(B)^{-3/4}=O_K(T^{1/4})\), give
\[
 \rho_K\frac{\zeta_K(3/2)}{\zeta_K(3)}x^{1/2}
 -2\rho_K\kappa_K x^{1/2}T^{-1/2}
 +O_K(x^{1/2}T^{-1}\log(2T)+x^{1/4}T^{1/4}).
\tag{7}
\]
In the second sum, (2) and (3) at \(\sigma=2/3\) give
\[
 \kappa_K\zeta_K(2/3)x^{1/3}+3\rho_K\kappa_K x^{1/3}T^{1/3}
 +O_K(x^{1/3}T^{-1/6}+x^{1/6}T^{2/3}\log(2x)).
\tag{8}
\]
Finally (1) and (2) imply
\[
 A_K(T)S_K(T)=\rho_K\kappa_K T^2+O_K(T^{3/2}\log(2T)).
\tag{9}
\]
At \(T=x^{1/5}\), the three \(x^{2/5}\) contributions cancel exactly:
\(-2\rho_K\kappa_K+3\rho_K\kappa_K-\rho_K\kappa_K=0\).
Every remaining error in (7)--(9) is \(O_K(x^{3/10}\log(2x))\), proving the theorem. For \(\mathbb Q(i)\), \(\beta(2/3)>0\) by its alternating series, whereas \(\zeta(2/3)<0\) by the alternating eta series; this proves the stated sign.

## Verification
The independent coefficient enumeration in `check.py` uses the rational-prime splitting rules for \(\mathbb Q(i)\) and compares direct multiplicative squarefull-ideal coefficients with the \(A^2B^3\) decomposition at five finite cutoffs. It checks the finite formulas only; the asymptotic theorem follows from (1)--(9), not from extrapolating numerical data.

## Relationship to prior work
Horikx and Pieropan (arXiv:2610.12543v1, first posted 8 October 2026), Theorem 1 and Corollary 2, prove the leading \(x^{1/2}\) term for squarefull ideals of arbitrary number fields with an \(O_K(x^{1/3})\) error in the quadratic case. That remainder does not resolve the coefficient of \(x^{1/3}\). The present argument isolates this term and proves an error smaller than \(x^{1/3}\) for quadratic fields. Bateman--Grosswald (1958) and Ivić--Shiu (1982) give more precise results for squarefull *rational integers*; those results do not themselves count ideals of a nontrivial quadratic field. The proof uses classical ideal counting rather than claims about class-by-class second terms.

## Limitations
The field is fixed, so the implied constant need not be uniform in its discriminant. The result does not assert optimality of the exponent \(3/10\), does not count individual ideal classes, and does not imply that the secondary coefficient is nonzero for every quadratic field. Earlier general-purpose methods for Dirichlet series with multiple poles could imply related formulas; absence of a discovered identical statement is not a proof of historical priority.

## References
1. M. Horikx and M. Pieropan, *On m-fullness in number fields*, arXiv:2610.12543v1 (8 October 2026), Theorem 1, Corollary 2 and Section 3. https://arxiv.org/html/2610.12543v1
2. P. T. Bateman and E. Grosswald, *On a theorem of Erdős and Szekeres*, Illinois J. Math. **2** (1958), 88--98. https://projecteuclid.org/euclid.ijm/1255380836
3. A. Ivić and P. Shiu, *The distribution of powerful integers*, Illinois J. Math. **26** (1982), 576--590. https://doi.org/10.1215/ijm/1256046597
4. O. Ramaré, *Explicit count of integral ideals of an imaginary quadratic field*, arXiv:2308.10876 (2023). https://arxiv.org/abs/2308.10876
