# A sharp all-sweep exchange-stability wall for two-node positive integral deferred correction

## Finding

Consider the two-node Gauss–Lobatto Stable Positive Integral Deferred Correction (SPIDeC) method, including its exponential predictor and any finite number \(m\geq0\) of correction sweeps, on the strictly positive two-species exchange problem
\[
\dot y_1=a(y_2-y_1),\qquad \dot y_2=b(y_1-y_2),\qquad a,b>0.
\]
Every equilibrium \(\bar y=(s,s)\), \(s>0\), is preserved by the numerical one-step map \(F_{h,m}\), which also maps every strictly positive input to a strictly positive output for every \(h>0\). Let \(u=h(a+b)/2\). The eigenvalues of \(DF_{h,m}(\bar y)\) are precisely \(1\), tangent to the line of equilibria, and
\[
R_m(u)=\frac{1-u+2(-1)^{m+1}u^{m+2}}{1+u},
\]
transverse to that line. For **every** finite \(m\geq0\),
\[
|R_m(u)|<1\quad\Longleftrightarrow\quad 0<u<1.
\]
At \(u=1\), \(R_m(1)=(-1)^{m+1}\). For \(u>1\), even \(m\) gives \(R_m(u)<-1\), whereas odd \(m\) gives \(R_m(u)>1\). Thus the exact transverse linear contraction threshold for *every finite sweep count* is \(h(a+b)<2\). Adding arbitrarily many finite sweeps does not expand it.

In contrast, the locally defined **fully implicit multiplicative trapezoidal collocation map** at the same equilibrium has transverse derivative
\[
R_{\mathrm{coll}}(u)=\frac{1-u}{1+u},
\]
whose modulus is strictly below one for every \(u>0\). The finite-sweep transverse derivatives converge to this collocation value as \(m\to\infty\) **if and only if** \(u<1\); they alternate at \(u=1\) and have unbounded magnitude with \(m\) for \(u>1\).

For example, the exchange rates \(a=b=1\), step \(h=3/2\), and one correction sweep give \(R_1=5/2\) although the corresponding implicit collocation derivative is \(-1/5\). Both finite-sweep and implicit updates preserve the positive equilibrium. The exact flow's transverse multiplier is \(e^{-3}\).

## Assumptions and scope

The coefficients \(a,b\) are arbitrary strictly positive real constants; \(h\) is a fixed positive step; \(m\) is any fixed nonnegative integer; and all state components are strictly positive. The nodal parameters are exactly \(\tau_0=0\) and \(\tau_1=1\), with endpoint quadrature weights \(Q_{1,0}=Q_{1,1}=1/2\). No conservation of the **discrete** nonlinear state sum is assumed or asserted. The neutral derivative eigenvalue \(1\) reflects an entire line of fixed equilibria: stability and instability statements in this result concern the *transverse linearized direction*, not asymptotic convergence to a particular equilibrium or global nonlinear contractivity.

For \(x=(x_1,x_2)\) define \(g_i(x)=f_i(x)/x_i\), where \(f=(a(x_2-x_1),b(x_1-x_2))\). Let \(\odot\) and \(\exp\) act componentwise. The source's two-node method specializes exactly to
\[
F_{h,0}(x)=x\odot\exp(hg(x)),\qquad
F_{h,m}(x)=x\odot\exp\!\left[\frac h2\big(g(x)+g(F_{h,m-1}(x))\big)\right]\quad(m\ge1).
\]
These expressions define the finite-sweep maps without any stage solver. Their collocation counterpart solves \(z=x\odot\exp[\frac h2(g(x)+g(z))]\) locally around \(x=z=(s,s)\).

## Proof

Write
\[
Q=\begin{pmatrix}-a&a\\b&-b\end{pmatrix}.
\]
At every \(\bar y=(s,s)\), \(g(\bar y)=0\), and the derivative of \(g\) is \(Dg(\bar y)=Q/s\). By induction all finite-sweep maps fix \(\bar y\). The derivative of the componentwise exponential at zero is one, so the chain rule gives
\[
DF_{h,0}(\bar y)=I+hQ,\qquad
DF_{h,m}(\bar y)=I+\frac h2Q\big(I+DF_{h,m-1}(\bar y)\big).
\]
The matrix \(Q\) has eigenvalue \(0\) with eigenvector \((1,1)\), and eigenvalue \(-(a+b)\) with eigenvector \((a,-b)\). Hence each Jacobian has a neutral eigenvalue \(1\), while its other eigenvalue satisfies the scalar recurrence
\[
R_0(u)=1-2u,\qquad R_m(u)=1-u(1+R_{m-1}(u)).
\]
The fixed point of that affine recurrence is \(r=(1-u)/(1+u)\), and subtracting \(r\) shows
\[
R_m(u)=r+(-u)^m\big(R_0(u)-r\big)
=\frac{1-u+2(-1)^{m+1}u^{m+2}}{1+u}.
\]
For \(0<u<1\), if \(m\) is odd then \(R_m(u)>-1\) and \(R_m(u)<1\) is equivalent to \(u^{m+1}<1\). If \(m\) is even then \(R_m(u)<1\) and \(R_m(u)>-1\) is equivalent to \(u^{m+2}<1\). Both inequalities hold. At \(u=1\), the recurrence alternates between \(-1\) and \(1\). For \(u>1\), odd \(m\) satisfies
\[
R_m(u)-1=\frac{2u(u^{m+1}-1)}{1+u}>0,
\]
whereas even \(m\) satisfies
\[
R_m(u)+1=\frac{2(1-u^{m+2})}{1+u}<0.
\]
This proves the complete finite-sweep threshold, including the boundary and parity classification. Strict positivity holds for arbitrary positive inputs by the exponential formulas, with every operation defined inductively at each finite sweep.

For the collocation equation, differentiating its logarithmic form at \(z=x=\bar y\) gives
\[
\left(I-\frac h2Q\right)Dz=I+\frac h2Q.
\]
The matrix on the left is invertible for every \(h>0\) (eigenvalues \(1\) and \(1+u\)), so the implicit function theorem supplies a unique smooth local branch. Its transverse derivative is \((1-u)/(1+u)\), whose magnitude is less than one for all \(u>0\). Finally, the closed formula for \(R_m\) shows that its difference from this derivative has magnitude \(2u^{m+2}/(1+u)\). Thus the derivative convergence, boundary alternation, and divergence assertions follow.

## Verification

Run `python3 verify.py` using only Python's standard library. The script uses exact rational arithmetic to check the recurrence, closed formula, and strict stability inequalities across rational steps and multiple finite sweep counts; it also evaluates the original nonlinear exponential maps independently for four symmetric and asymmetric rate pairs and compares centered finite differences against the analytical transverse derivative. On the packaged script the checks total **9,766**, all passing. These checks are supplementary; the preceding algebra and implicit-function argument prove statements for every admissible parameter and every finite sweep count.

## Relationship to prior work

Pezzella [1] introduced SPIDeC, including its multiplicative sweep formula (Section 2), unconditional componentwise positivity and equilibria preservation (Section 3), diagonal scalar test-equation exactness (Theorem 5.1), and conditional estimates for the predictor and corrected maps (Theorems 5.6–5.7). The last estimate is a small-step, finite-correction bound; the scalar diagonal exactness relies on constant componentwise ratios \(f_i(y)/y_i\), which are not constant for coupled exchange. The present result identifies an exact, sweep-count-independent transverse boundary for the coupled exchange family and contrasts it with the locally defined collocation limit. It does not invalidate the source's theorems.

Scheiber [2] treats classical additive numerical Picard iteration and step-dependent convergence of collocation approximations. Such contraction principles are relevant background, but they do not directly state the exact finite-sweep multipliers of this multiplicative positive method on the two-rate exchange system. These formulas use standard Picard and eigenvalue algebra; unknown equivalent earlier specializations remain a priority risk.

## Limitations

The result is restricted to **two** Gauss–Lobatto nodes and two exchange species, with fixed positive rates and exact arithmetic. It does not cover Gauss–Radau discretizations, more quadrature nodes, globally nonlinear attraction, invariance of discrete mass, arbitrary network generators, or full nonlinear collocation away from the equilibrium line. At the critical step \(u=1\), the result asserts marginal transverse *linear* behavior only. A transverse unstable derivative implies arbitrarily near positive states exhibit first-order expansion, but it does not establish their global long-term fate. The numerical checker alone cannot certify the universal statements.

## References

1. M. Pezzella, *Stable Positive Integral Deferred Correction Methods for Positive Dynamical Systems*, arXiv:2606.29523, initially submitted 2026-06-28, https://arxiv.org/abs/2606.29523.
2. E. Scheiber, *On the numerical Picard iterations with collocations for the initial value problem*, Journal of Numerical Analysis and Approximation Theory **48** (2019), https://ictp.acad.ro/jnaat/journal/article/view/1146/1372.
