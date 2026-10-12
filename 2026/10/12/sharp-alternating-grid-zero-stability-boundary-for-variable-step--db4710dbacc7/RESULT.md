# Sharp alternating-grid zero-stability boundary for variable-step BDF through order five

## Finding
Let \(k\in\{1,2,3,4,5\}\) and apply the standard interpolation-based variable-step backward differentiation formula of order \(k\) to the homogeneous scalar ODE \(y'=0\). Suppose the positive steps indefinitely alternate between \(rh\) and \(h\), for fixed \(h>0\) and \(r>0\), with no startup restrictions. Strong zero-stability means the constant solution is the only unit-modulus Floquet mode and every parasitic two-step Floquet multiplier has modulus strictly less than one; ordinary zero-stability means every homogeneous solution from arbitrary \(k\) initial values stays bounded uniformly in the number of time steps.

For orders \(1\) through \(4\), **both properties hold for every fixed \(r>0\)**. At order \(5\), set
\[
H(r)=4r^6-8r^5-83r^4-143r^3-83r^2-8r+4.
\]
Let \(r_-\in(0,1)\) and \(r_+>1\) be its two positive roots, with \(r_-r_+=1\). Numerically, \(r_-=0.15902289348450932\ldots\) and \(r_+=6.2884027455921725\ldots\). Order-five BDF is strongly zero-stable **if and only if** \(r_-<r<r_+\), and ordinarily zero-stable **if and only if** \(r_-\le r\le r_+\). At either endpoint exactly one simple parasitic two-step multiplier equals \(-1\); for \(r\) outside the closed interval a real parasitic Floquet multiplier has modulus greater than one.

## Assumptions and scope
For each step, use the \(k+1\) actual (possibly nonuniform) interpolation nodes \(t_n,t_{n-1},\ldots,t_{n-k}\). The coefficients are the Lagrange-polynomial derivative weights at \(t_n\), not frozen constant-step BDF coefficients or a Nordsieck interpolation variant. Take \(r\) constant in time; alternating steps are positive and continue indefinitely. The stability statement concerns the homogeneous recurrence, not A-stability, convergence order on a fixed interval, nonlinear dynamics, or arbitrarily varying (nonperiodic) step ratios. The alternating start phase does not affect Floquet multipliers.

## Proof
Write \(t_n=0\) and \(t_{n-j}=-\sum_{i=0}^{j-1}h_{n-i}\). Denote the Lagrange interpolation cardinal polynomials by \(\ell_j\), and define \(w_j=\ell_j'(0)\). The exact zero-equation BDF recurrence is
\[
y_n=\sum_{j=1}^{k}a_jy_{n-j},\qquad a_j=-w_j/w_0,\qquad \sum_{j=1}^k a_j=1.
\]
Set \(d_n=y_n-y_{n-1}\). Substitution eliminates the constant root and yields a companion update on the \(k-1\) differences:
\[
d_n=-\sum_{\ell=1}^{k-1}\Bigl(\sum_{j=\ell+1}^k a_j\Bigr)d_{n-\ell}.
\]
Let \(M_k(r)\) be its companion matrix for present and previous steps \((rh,h,rh,\ldots)\), and \(M_k(1/r)\) the companion for \((h,rh,h,\ldots)\). The parasitic monodromy is the explicitly reconstructible matrix \(P_k(r)=M_k(1/r)M_k(r)\), with the second factor interpreted using common scale \(h\) rather than rescaling the physical time origin. In the accompanying checker the two matrices are constructed directly from \((r,1,r,\ldots)\) and \((1,r,1,\ldots)\).

**Orders one and two.** BDF1 has no parasitic mode. At BDF2, the unique multiplier is \(r/((1+2r)(r+2))\), strictly between zero and one for every \(r>0\).

**Order three.** Set \(D_3=(r^2+5r+5)(5r^2+5r+1)\). The parasitic characteristic polynomial is \(z^2+a z+b\), where
\[
a=\frac{r^4-r^3-5r^2-r+1}{D_3},\qquad b=\frac{r(r+1)^2}{D_3}.
\]
The quadratic strict Schur inequalities \(1-b>0\), \(1+a+b>0\), and \(1-a+b>0\) hold, with numerators respectively \(5r^4+29r^3+49r^2+29r+5\), \(2(2r^4+16r^3+29r^2+16r+2)\), and \(6(r+1)^2(r^2+3r+1)\). The common denominator is \(D_3>0\).

**Order four.** Let \(D_4=(r+4)(2r+3)(3r+2)(4r+1)\). Its characteristic polynomial is \(z^3+a z^2+b z+c\), where
\[
\begin{aligned}
a&=\frac{24r^4+34r^3+5r^2+34r+24}{D_4},\\
b&=\frac{6r^3+19r^2+6r}{D_4},\\
c&=-\frac{2r^3+5r^2+2r}{D_4}.
\end{aligned}
\]
The cubic strict Schur inequalities are \(|c|<1\), \(1+a+b+c>0\), \(1-a+b-c>0\), and \(1-b+ac-c^2>0\). The last three expressions are, respectively,
\[
\frac{48(r+1)^4}{D_4},\qquad
\frac{32r(4r^2+9r+4)}{D_4},\qquad
\frac{16Q_8(r)}{D_4^2},
\]
where
\[
Q_8(r)=36r^8+450r^7+2191r^6+5332r^5+7112r^4+5332r^3+2191r^2+450r+36.
\]
All are strictly positive for \(r>0\); also \(-1<c<0\).

**Order five.** Define
\[
\begin{aligned}
D_5&=(4r^3+30r^2+63r+40)(40r^3+63r^2+30r+4),\\
D_+&=160r^6+1460r^5+4566r^4+6541r^3+4566r^2+1460r+160.
\end{aligned}
\]
Direct interpolation gives the parasitic quartic \(F(z)=z^4+Az^3+Bz^2+Cz+E\), with
\[
\begin{aligned}
A&=\frac{304r^6+1348r^5+2442r^4+2781r^3+2442r^2+1348r+304}{D_5},\\
B&=\frac{16r^6+108r^5+362r^4+547r^3+362r^2+108r+16}{D_5},\\
C&=-\frac{36r^5+170r^4+269r^3+170r^2+36r}{D_5},\\
E&=\frac{8r^5+36r^4+56r^3+36r^2+8r}{D_5}.
\end{aligned}
\]
In particular \(0<E<1\). The standard Schur reduction \((F(z)-EF^*(z))/(z(1-E^2))\), where \(F^*(z)=z^4F(1/z)\), is a monic cubic \(z^3+az^2+bz+c\) with \(a=(A-EC)/(1-E^2)\), \(b=(B-EB)/(1-E^2)\), \(c=(C-EA)/(1-E^2)\). Its cubic Jury conditions are strict except possibly
\[
1-a+b-c=-\frac{32H(r)}{D_+}.
\]
Indeed \(1\pm c>0\), \(1+a+b+c=480(r+1)^6/D_+>0\), and \(1-b+ac-c^2>0\) for all \(r>0\). The last positivity is an exact rational identity whose reduced numerator and denominator are nonzero polynomials having only nonnegative coefficients, verified symbolically by the standalone checker; it is not an empirical sign guess.

Since \(H\) has coefficient sign pattern \(+,-,-,-,-,-,+\), Descartes' rule bounds its positive zeros by two. As \(H(0)=4>0\), \(H(1)=-317<0\), and \(H(r)\to+\infty\), it has exactly two distinct positive zeros and changes sign there; moreover \(r^6H(1/r)=H(r)\). The strict Schur criterion therefore gives exactly the open interval stated.

On its endpoints, \(F(-1)=-32H(r)/D_5=0\), whereas \(F(1)>0\); the other transformed Schur inequalities remain strict. The exact polynomial-gcd identity \(\gcd(H(r),\operatorname{numerator}(\partial_zF(-1)))=1\) shows the \(-1\) root is simple at either positive root of \(H\); the remaining parasitic multipliers are strictly inside the disk by the non-strict Schur boundary and continuity. Thus two-step monodromy powers remain bounded at endpoints. Outside, failure of the strict sign condition \(F(-1)>0\) combined with \(F(z)\to+\infty\) as real \(z\to-\infty\) gives a real root less than \(-1\), hence an unbounded solution. The constant-root eigenmode is independent of the difference dynamics, completing ordinary zero-stability.

## Verification
Run `python bdf_alternating_check.py` with SymPy installed. The script derives the variable-step Lagrange derivatives and monodromy matrices symbolically, exactly matches all characteristic-polynomial coefficients through order five, checks the relevant Schur polynomial identities and positivity certificates, verifies the reciprocity and simple-root gcd, and compares twenty exact-rational choices (five step ratios times four orders). It prints `VERIFY_OK` with numerical root approximations. The numerical approximations certify no infinite-range statement; those follow from the explicit algebraic identities, positive coefficients and Descartes' rule.

## Relationship to prior work
General variable-mesh multistep zero-stability and variable-step BDF estimates were developed in earlier work of Gear and Tu, Grigorieff, Skeel and Jackson, Calvo–Lisbona–Montijano, and Guglielmi–Zennaro. The later explicit SSP variable-step multistep results of Hadjimichael et al. (arXiv:1504.04107v1, publicly posted 2015-04-16) address a different scheme. Li and Liao (arXiv:2201.00527v1) prove arbitrary-grid BDF2 stability and conditional BDF3 stability on general nonuniform grids, but do not give the specific alternating-grid BDF1–BDF5 classification here. The new claim is the explicit sharp two-period Floquet characterization, not that older general criteria for products of variable-step matrices were previously unavailable.

## Limitations
This is a linear homogeneous zero-equation statement on fixed two-periodic grids. It gives no nonperiodic arbitrary-grid bound, nonlinear stability or numerical error estimate. Several older primary papers on variable-step zero-stability could not be accessed in complete full text, so an equivalent specialized computation cannot be categorically ruled out. Algebraic certificates are replayable with SymPy; no independent external audit has been performed.

## References
- Y. Hadjimichael, D. Ketcheson, L. Lóczi, A. Németh, *Strong stability preserving explicit linear multistep methods with variable step size*, arXiv:1504.04107v1 (2015-04-16), https://arxiv.org/abs/1504.04107.
- Z. Li and H.-L. Liao, *Stability of variable-step BDF2 and BDF3 methods*, arXiv:2201.00527v1 (2022), https://arxiv.org/abs/2201.00527.
- R. D. Grigorieff, *Stability of multistep-methods on variable grids* (1983), https://doi.org/10.1007/BF01389580.
- R. D. Skeel and L. W. Jackson, *The stability of variable-stepsize Nordsieck methods* (1983), https://doi.org/10.1137/0720056.
- J. C. Butcher's general polynomial root-stability theory; the quadratic and cubic Schur–Jury criteria are standard.
- Calvo, Lisbona and Montijano, *On the stability of variable-stepsize Nordsieck BDF methods* (1987), https://doi.org/10.1137/0724054.
- N. Guglielmi and M. Zennaro, *On the zero-stability of variable stepsize multistep methods: The spectral radius approach* (2001), https://doi.org/10.1007/s211-001-8010-0.
