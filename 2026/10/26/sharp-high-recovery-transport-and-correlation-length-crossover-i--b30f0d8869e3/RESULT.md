# Subleading strong-recovery asymptotics of correlations at maximum tandem-exclusion current

## Finding

Consider the thermodynamic stationary Gibbs state of the periodic tandem exclusion process, with local transitions \(110\to101\) at rate \(\alpha>0\) and \(101\to011\) at rate \(\beta>0\). Set \(q=\beta/\alpha\). The exact stationary formulas are from [1]. Write \(\rho_*(q)\) for the unique density maximizing the thermodynamic current \(J(\rho,q)\); the uniqueness and leading current and density asymptotics are established in [2]. The leading growth of the optimal correlation length is also available in [3].

For \(q>1\), define the occupation correlation length \(\xi\) by the inverse negative logarithm of the subleading-to-leading transfer eigenvalue ratio and define \(\chi(\rho,q)=\sum_{k\in\mathbb Z}\operatorname{Cov}(\eta_0,\eta_k)\). As \(q\to\infty\),
\[
\xi(\rho_*,q)=2^{-1/3}q^{1/3}-\frac13+O(q^{-1/3}),\qquad
\chi(\rho_*,q)=1-2^{1/3}q^{-1/3}+O(q^{-2/3}).
\]
The diverging correlation length is accompanied by a vanishing covariance amplitude and a susceptibility with finite limit one. The optimizing density and normalized peak current have the refinements
\[
\begin{aligned}
1-\rho_*&=2^{-2/3}q^{-1/3}-\frac{2^{-4/3}}3 q^{-2/3}+O(q^{-1}),\\
\frac{J(\rho_*,q)}{\alpha}&=1-3\,2^{-2/3}q^{-1/3}+5\,2^{-4/3}q^{-2/3}+O(q^{-1}).
\end{aligned}
\]
At each fixed \(0<\rho<1\), the square-root growth law has coefficient \(\xi(\rho,q)\sim\sqrt{q\rho(1-\rho)}\), correcting the coefficient in [1, Eq. (19)].

## Assumptions and scope

The thermodynamic limit in the active sector of the periodic process is taken at fixed density before varying density or taking large \(q\). The susceptibility is the sum in the infinite stationary Gibbs state, not the sum around a finite ring with fixed particle number. The results do not assert a joint rate/size limit, finite-ring optimization or mixing estimates.

## Proof

**Refining the optimum.** The positive stationary parameter \(s\) and normalized current \(j\) satisfy [1, Eqs. (10)–(12)]
\[
\rho=\frac{s(1+qs)}{1+2s+qs^2},\qquad
j=\frac{qs^2\{2+(q+1)s\}}{(1+s)(1+qs)(1+2s+qs^2)}.
\]
As in [2], \(\rho\) increases bijectively with \(s>0\) by differentiation, and the optimizer \(s_*(q)\) is the unique positive zero of
\[
 P_q(s)=(q^3+q^2)s^5+4q^2s^4-(2q^2+2)s^3-(2q^2+8q+6)s^2-(5q+9)s-4.
\]
Indeed \(j'(s)=-qs P_q(s)/[(1+s)^2(1+qs)^2(1+2s+qs^2)^2]\), so the one sign change of \(P_q\) and its signs at zero and infinity yield uniqueness and maximality. Let \(\epsilon=q^{-1/3}\), \(c=2^{1/3}\), and write \(s=\epsilon v\). The scaled polynomial satisfies
\[
 \epsilon^4P_{\epsilon^{-3}}(\epsilon v)=v^5-2v^2-2\epsilon v^3+O(\epsilon^2)
\]
on bounded \(v\)-intervals and is polynomial in \(v,\epsilon\). The zero at \(v=c\) is simple with derivative \(6c\). By the implicit function theorem, the positive root is \(v_*=c+(c^2/3)\epsilon+O(\epsilon^2)\). For \(v\) near \(c\), the density identity yields
\[
1-\rho=\epsilon v^{-2}+\epsilon^2(v^{-1}-v^{-4})+O(\epsilon^3).
\]
Writing \(j=(1+(1+2s)/(qs^2))^{-1}\{(1+s)^{-1}+(1+qs)^{-1}\}\) gives
\[
j=1-\epsilon(v+v^{-2})+\epsilon^2(v^2+v^{-4})+O(\epsilon^3).
\]
Since the derivative of \(v+v^{-2}\) vanishes at \(c\), insertion of \(v_*\) gives \(j_*=1-(3c/2)\epsilon+(5c^2/4)\epsilon^2+O(\epsilon^3)\). For the density one obtains \(1-\rho_*=(c/2)\epsilon-(c^2/12)\epsilon^2+O(\epsilon^3)\). These coefficients are those in the Finding.

**Correlations and susceptibility.** Write \(r=\rho(1-\rho)\) and \(x=\Pr(\eta_0=1,\eta_1=0)=\Pr(\eta_0=0,\eta_1=1)\). For the two-state Gibbs Markov chain of [1], the transition probabilities into state 1 from states 0 and 1 are \(s/(1+s)\) and \(qs/(1+qs)\), respectively. The odds ratio of the two-site law is therefore \((\rho-x)(1-\rho-x)/x^2=q\). Solving \((q-1)x^2+x=r\) gives \(x=2r/(1+D)\), where \(D=\sqrt{1+4(q-1)r}\). The nontrivial transition eigenvalue is
\[
R=1-\frac{x}{\rho}-\frac{x}{1-\rho}=\frac{D-1}{D+1},
\]
equal to the transfer eigenvalue ratio. For \(q>1\) this is positive and less than one. The centered occupation spans the nonconstant eigenspace, so the covariance at separation \(k\) is \(r R^{|k|}\). Consequently
\[
\xi=\left[\log\frac{D+1}{D-1}\right]^{-1},\qquad
\chi=r\frac{1+R}{1-R}=rD.
\]
Along the optimum, \(r_*=(c/2)\epsilon-(c^2/3)\epsilon^2+O(\epsilon^3)\), hence \(D_*=c^2\epsilon^{-1}-2/3+O(\epsilon)\). For large \(D\), \(\log[(D+1)/(D-1)]=2/D+O(D^{-3})\), so \(\xi_*=D_*/2+O(\epsilon)\) and \(\chi_*=r_*D_*\). These are the asserted expansions. At fixed interior density, \(D\sim 2\sqrt{q\rho(1-\rho)}\), giving the stated fixed-density coefficient. The expression printed in [1, Eq. (19)], \(\tfrac12\sqrt{q(1-\rho)/\rho}\), agrees only at \(\rho=1/2\). Equivalently, at fixed density the source's exact quadratic gives \(s\sim \sqrt{\rho/(1-\rho)}q^{-1/2}\); both \(s\) and \(1/(qs)\) contribute at leading order to the logarithm of the exact inverse transfer ratio.

## Verification and limitations

The supplied `verify_tep.py` remains applicable to the original current and transfer formulas and the displayed asymptotic coefficients; it uses Python with SymPy, NumPy and SciPy. Numerical checks are corroboration, not proofs of uniform remainder estimates or uniqueness. The two-state derivation above establishes the susceptibility identity for the thermodynamic Gibbs state without relying on finite tests.

## Relationship to prior work

The current and transfer matrix are from [1]. The unique optimum, its quintic characterization and the leading optimal density and peak current scales are from [2]. The leading optimal correlation-length scale is explicitly covered by [3]. The refinements here are the next-order optimized coefficients, including the additive correlation-length correction, the finite susceptibility and its first correction at the optimum, and the corrected fixed-density prefactor. These follow from the known exact formulas, not from a new stationarity theorem. The asymptotic estimates are for the specified thermodynamic regimes, not uniform finite-ring estimates.

## References

1. N. P. N. Ngoc, L. T. Nhung and H. A. Thi, *Tandem Exclusion Process*, [arXiv:2606.01568v1](https://arxiv.org/abs/2606.01568v1), Eqs. (10)–(12), (17)–(19), and Appendix B.
2. *Unique optimal density and cube-root strong-recovery saturation in the tandem exclusion process*, [Resultary record 567080689ef1](https://github.com/Resultary/2026/blob/main/2026/10/13/SCOPE-unique-optimal-density-and-cube-root-strong-recovery-saturation--567080689ef1/RESULT.md).
3. *A unique optimal-density reversal and cubic-root transport boundary layer in tandem exclusion*, [Resultary record 9e615aab7046](https://github.com/Resultary/2026/blob/main/2026/11/8/SCOPE-a-unique-optimal-density-reversal-and-cubic-root-transport-bound--9e615aab7046/RESULT.md).
