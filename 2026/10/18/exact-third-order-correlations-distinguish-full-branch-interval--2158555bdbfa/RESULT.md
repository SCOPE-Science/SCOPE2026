# Exact third-order correlations distinguish full-branch interval maps with identical linear and quadratic autocorrelations

## Finding
Fix any integer \(k\ge2\), ordered breakpoints \(0=b_0<b_1<\cdots<b_k=1\), and branch orientations \(\varepsilon_i\in\{+1,-1\}\). Put \(\ell_i=b_i-b_{i-1}\) and \(c_i=(b_{i-1}+b_i)/2\). On branch \((b_{i-1},b_i)\), let \(T\) be the affine bijection onto \((0,1)\) with orientation \(\varepsilon_i\). For stationary \(X_n=T^nX_0\) where \(X_0\) is uniformly distributed on \([0,1]\), define \(g(x)=x-1/2\) and
\[
\theta=\sum_{i=1}^k\varepsilon_i\ell_i^2,\qquad
A=\sum_{i=1}^k\ell_i^3,\qquad
B=2\sum_{i=1}^k\varepsilon_i\ell_i^2(c_i-1/2).
\]
Then for every \(j,m\in\mathbb N\) with \(j,m\ge1\), the complete positive-gap ordered third-correlation array is
\[
\boxed{C_{j,m}=\mathbb E[g(X_0)g(X_j)g(X_{j+m})]
 =\frac{B\theta^j}{12}\sum_{q=0}^{m-1}A^{m-1-q}\theta^q.}
\]
In particular, its double generating function is the rational function
\[
\boxed{\sum_{j,m\ge1}C_{j,m}u^jv^m
=\frac{B}{12}\frac{\theta u}{1-\theta u}
 \frac{v}{(1-Av)(1-\theta v)}}
\]
for \(|\theta u|<1\) and \(\max(A,|\theta|)|v|<1\). The entire array is symmetric under time reversal of the gap pair, \(C_{j,m}=C_{m,j}\) for all positive integers \(j,m\), **if and only if** \(\theta B=0\). Indeed
\[
\boxed{C_{1,2}-C_{2,1}=\theta A B/12.}
\]
The result measures reversal asymmetry of this *one cubic coordinate observable*, not time reversibility of the full path law.

**A sharp identifiability witness.** For four equal branch lengths \(\ell_i=1/4\), compare maps with orientation vectors \((-1,+1,+1,+1)\) and \((+1,-1,+1,+1)\). Both have exactly the same linear and centered-square autocorrelations at every lag, because for both \(\theta=1/8\) and \(A=1/16\). Nevertheless their \(B\) parameters are respectively \(3/32\) and \(1/32\), so
\[
(C_{1,1}^{(1)},C_{1,1}^{(2)})=(1/1024,1/3072),\qquad
(C_{1,2}^{(1)}-C_{2,1}^{(1)}, C_{1,2}^{(2)}-C_{2,1}^{(2)})
=(1/16384,1/49152).
\]
Thus *even the entire pair of ordinary linear and quadratic autocorrelation sequences* fails to determine the simplest genuinely three-time correlation.

**Optimal skew-tent reversal contrast.** For the two-branch skew tent map \(T_a(x)=x/a\) when \(0\le x<a\) and \(T_a(x)=(1-x)/(1-a)\) otherwise, with \(0<a<1\), put \(t=2a-1\). One gets
\[
\theta=t,\qquad A=(1+3t^2)/4,\qquad B=-(1-t^2)/4,
\qquad \boxed{C_{1,2}-C_{2,1}=-\frac{t(1-t^2)(1+3t^2)}{192}.}
\]
The absolute contrast has its strict global maximum (within \(0<a<1\)) at exactly the two cuts
\[
\boxed{a=\frac12\bigl(1\pm\sqrt{(3+2\sqrt6)/15}\bigr).}
\]
Its value is obtained by substituting \(t=\sqrt{(3+2\sqrt6)/15}\) into \(|t|(1-t^2)(1+3t^2)/192\), approximately \(0.0046158691679921\).

## Assumptions and scope
All \(k\) branches have positive lengths, hence \(0<\ell_i<1\). Branch endpoint conventions are arbitrary and immaterial for the Lebesgue stationary laws and integral statements. No continuity across branch boundaries is required. All correlations refer to the uniform invariant state; all positive integers \(j,m\) are included, with no periodicity or rational-length assumption. Every finite branch map in this class is piecewise uniformly expanding. The reference values \(\theta\) and \(A\) satisfy \(|\theta|\le\sum_i\ell_i^2<1\) and \(0<A<1\).

## Proof
**Invariant density and exact conditional-polynomial action.** Each branch has inverse
\[
\phi_i(u)=c_i+\varepsilon_i\ell_i(u-1/2).
\]
Its Jacobian magnitude is \(\ell_i\). Therefore the normalized Perron operator is
\[
(Pf)(u)=\sum_{i=1}^k\ell_i f(\phi_i(u)),\qquad P1=\sum_i\ell_i=1.
\]
By change of variables, \(\int_0^1 f(u)q(Tu)\,du=\int_0^1(Pf)(u)q(u)\,du\). This identity proves stationarity of Lebesgue measure and applies repeatedly to bounded polynomials.

Write \(h(u)=g(u)^2-1/12\). Since \(\sum_i\ell_i(c_i-1/2)=\int_0^1g(x)\,dx=0\), substitution of \(\phi_i\) gives
\[
Pg=\theta g.
\]
Likewise, expanding \(g(\phi_i(u))=(c_i-1/2)+\varepsilon_i\ell_i g(u)\), one finds the coefficient of \(g(u)^2\) in \(Ph\) is \(A\), and that of \(g(u)\) is \(B\). Since \(\int_0^1Ph=\int_0^1h=0\), the constant term is exactly the one needed to yield
\[
\boxed{Ph=A h+B g.}
\]
Induction gives for every integer \(m\ge1\)
\[
P^m h=A^m h+B\sum_{q=0}^{m-1}A^{m-1-q}\theta^qg.
\]
Also \(P^jg=\theta^jg\) for every integer \(j\ge0\).

**Three-time computation.** Transfer duality at time \(j\), and then time \(m\), yields
\[
\begin{aligned}
C_{j,m}
&=\int_0^1 (P^jg)(u)g(u)g(T^mu)\,du\\
&=\theta^j\int_0^1 P^m(g^2)(u)g(u)\,du.
\end{aligned}
\]
Since \(\int g\,du=\int gh\,du=0\), \(\int g^2\,du=1/12\), and \(g^2=h+1/12\), exactly the advertised sum remains. As a finite geometric-series convolution, its double ordinary generating function is the stated product. No denominator division by \(A-\theta\) is used, so the formula also covers the resonant case \(A=\theta\).

**Reversal classification.** Stationarity makes reversal of an ordered three-time configuration \((0,j,j+m)\) correspond to interchanging gaps \(j\) and \(m\); multiplication of the three real observations is commutative. When \(\theta B=0\), the formula gives \(C_{j,m}=0\) for all strictly positive gaps. Conversely \(C_{1,2}-C_{2,1}=\theta BA/12\), and \(A>0\) forces \(\theta B=0\) if the entire tensor is gap symmetric.

**Equal-branch witness.** For each of the two sign vectors, \(\ell_i=1/4\) implies \(A=4(1/4)^3=1/16\) and \(\theta=(3-1)(1/4)^2=1/8\). Direct substitution of the branch midpoints \(c_i\in\{1/8,3/8,5/8,7/8\}\) yields \(B=3/32\) and \(B=1/32\), respectively. The exact third moments then follow from the established formula. Independently, the known pair sequences follow from transfer duality:
\[
\operatorname{Corr}(g(X_0),g(X_n))=\theta^n,
\qquad\operatorname{Corr}(h(X_0),h(X_n))=A^n\quad(n\ge0).
\]
For the second identity \(\int gh=0\) makes the \(B g\) component of \(P^nh\) invisible. Thus both maps have identical pair correlation sequences for *all* nonnegative lags although the cubic tensor differs.

**Sharp skew-tent optimum.** Directly inserting lengths \(a,1-a\) and signs \((+1,-1)\) gives \(\theta=t\), \(A=(1+3t^2)/4\), \(B=-(1-t^2)/4\). For \(0<t<1\), the positive amplitude is \(F(t)=t(1-t^2)(1+3t^2)/192\), with derivative
\[
F'(t)=(1+6t^2-15t^4)/192.
\]
The quadratic polynomial in \(t^2\) has exactly one root in \((0,1)\): \(t^2=(3+2\sqrt6)/15\). The derivative changes from positive to negative there, while \(F(0)=F(1)=0\), giving the unique maximum on the positive half-line; evenness of the absolute contrast provides the two stated cuts.

## Verification
The included standalone `verify.py` implements exact rational inverse-cylinder integration of \(g(X_0)g(X_j)g(X_{j+m})\), **independently of the transfer-polynomial derivation**. It compares this integral with the theorem for multiple positive and negative branch-orientation maps, includes both four-branch comparison examples, and checks the exact rational reversal contrasts. It also symbolically differentiates the skew-tent optimizer using SymPy. Running `python3 verify.py` with Python 3 and SymPy installed returns

`VERIFY_OK 49 exact rational independent cylinder and witness checks; sharp critical 0.72567115994167 amplitude 0.0046158691679921`

Exact finite-cylinder tests support the stated proof but cannot establish its unrestricted-integer quantifiers or independently certify historical novelty; the proof is analytical.

## Relationship to prior work
Lawrance and Papamarkou, *Higher Order Dependency of Chaotic Maps*, NOLTA 2006, pp. 695–698, explicitly derive the **linear** and **mean-adjusted quadratic** autocorrelation sequences for exactly this class of fully stretching piecewise linear maps, and motivate higher-order dependence. Their equations (1)–(3) give precisely the invariants \(\theta\) and \(A\) used here. Papamarkou and Lawrance (2014), *Nonlinear dynamics of trajectories generated by fully-stretching piecewise linear maps*, develops the quadratic autocorrelation and transfer-method foundations further. Thomine (arXiv:1006.2608v1, 2010) studies general spectral gaps and exponential decay for piecewise expanding maps. These established results are not new here.

The claimed additional content is the **evaluated three-time joint cubic tensor at arbitrary two lags**, its complete reversal-vanishing criterion, and a concrete pair of full-branch maps indistinguishable by both previously studied pair-correlation sequences. The published linear/quadratic ACFs do not themselves specify these three-time quantities. A broader previously published polynomial-transfer identity or an unindexed evaluation of all three-time moments might subsume the theorem; the historical priority of the displayed formulas has not been independently settled.

## Limitations
The formulas describe only moments of the *centered coordinate observable* under the stationary Lebesgue law. Vanishing cubic asymmetry does not imply full path reversibility, and nonzero cubic asymmetry witnesses but does not quantify every aspect of dynamical irreversibility. The result does not extend as written to maps whose branches fail to cover the whole interval, nonlinear branches, nonuniform invariant measures, or negative/zero time gaps. The four-branch witness demonstrates a strict limitation of two specified autocorrelation sequences, **not** equality of all bivariate distributions. Published literature may contain equivalent formulas under different notation. No independent mathematical audit or independent historical-priority certification is represented.

## References
1. A. J. Lawrance and T. Papamarkou, *Higher Order Dependency of Chaotic Maps*, Proceedings of NOLTA 2006, Bologna, pp. 695–698. Open proceeding: https://eprints.gla.ac.uk/143409/7/143409.pdf .
2. T. Papamarkou and A. J. Lawrance, *Nonlinear dynamics of trajectories generated by fully-stretching piecewise linear maps*, International Journal of Bifurcation and Chaos 24(05) (2014), 1450071, DOI 10.1142/S0218127414500710; university record: https://eprints.gla.ac.uk/139068/ .
3. D. Thomine, *A spectral gap for transfer operators of piecewise expanding maps*, arXiv:1006.2608v1, first publicly posted 2010-06-14: https://arxiv.org/abs/1006.2608 .
4. V. P. Baranovski and A. J. Lawrance, *Sensitive Parameter Dependence of Autocorrelation Function in Piecewise Linear Maps*, International Journal of Bifurcation and Chaos 17 (2007), DOI 10.1142/S0218127407017768.
