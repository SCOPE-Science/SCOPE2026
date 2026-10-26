# A unique switching-period invasion cutoff for reciprocal directed SIS contact layers

## Finding

Consider an SIS independent-probability approximation on two groups with identical positive recovery rate \(\mu\), infection-rate multiplier \(\beta>0\), and periodically alternating directed weighted contacts. For exactly half of each period \(T>0\), the contact matrix is \(A_1=\begin{pmatrix}0&a\\b&0\end{pmatrix}\); for the other half it is \(A_2=\begin{pmatrix}0&b\\a&0\end{pmatrix}\), where \(a,b>0\). Write \(\kappa=\sqrt{ab}\), \(m=(a+b)/2\), and \(\Gamma=m/\kappa\).

The exact largest disease-free Floquet exponent is
\[
\boxed{\Lambda(T)=-\mu+\frac{2}{T}\operatorname{arsinh}\!\left(\Gamma\sinh\frac{\beta\kappa T}{2}\right).}
\]
When \(a\ne b\), it is **strictly decreasing** throughout \(T>0\), with exact endpoint limits
\[
\Lambda(0+) = \beta m-\mu,\qquad \Lambda(+\infty)=\beta\kappa-\mu.
\]
Therefore there is a unique finite zero \(T_c\) **if and only if**
\[
\boxed{\beta\sqrt{ab}<\mu<\frac{\beta(a+b)}2.}
\]
In this case the two static directed contact layers are each strictly subcritical, but their alternating realization is linearly supercritical **for every \(0<T<T_c\)**, critical at \(T=T_c\), and subcritical **for every \(T>T_c\)**. If \(\mu\le\beta\kappa\), the alternating system is supercritical for every finite \(T>0\); if \(\mu\ge\beta m\), it is subcritical for every finite \(T>0\). At \(a=b\), \(\Lambda(T)=\beta a-\mu\) is independent of the period.

The threshold has a quantitative square-root onset. With \(a\ne b\), \(\beta,a,b\) fixed, let \(\epsilon=\beta m-\mu\downarrow0\) within the strict-cutoff regime and set
\[
C_2=\frac{\beta^3\kappa^3\Gamma(\Gamma^2-1)}{24}>0.
\]
Then \(T_c=\sqrt{\epsilon/C_2}\,[1+O(\epsilon)]\). The formula also gives the long-period correction \(\Lambda(T)=\beta\kappa-\mu+2\log\Gamma/T+O(e^{-\beta\kappa T}/T)\).

## Assumptions and scope

For group infection probabilities \(x_i(t)\in[0,1]\), the deterministic equations are
\[
\dot x_i(t)=\beta[1-x_i(t)]\sum_{j=1}^2 A_{ij}(t)x_j(t)-\mu x_i(t),\quad i=1,2.
\]
The right-hand side is locally Lipschitz within each phase and preserves the probability square. The disease-free state is \(x=(0,0)\), with linearization \(\dot z=(\beta A(t)-\mu I)z\). The contact layers are strongly connected directed two-group networks when \(a,b>0\); they are not assumed symmetric. All rates and dwell times are positive, and the two dwell times are exactly equal. The largest Floquet exponent is \(T^{-1}\log\rho(P_T)\), where \(P_T\) is the one-period linear monodromy. Positive/negative signs mean linear instability/asymptotic stability of the disease-free solution in this deterministic approximation.

## Proof

**Exact monodromy.** Because \(A_1^2=A_2^2=ab I=\kappa^2 I\), let \(z=\beta\kappa T/2\) and put
\[
E_j=\exp(\beta A_jT/2)=\cosh z\,I+\frac{\sinh z}{\kappa}A_j.
\]
The monodromy is \(P_T=e^{-\mu T}E_2E_1\), and \(\det(E_2E_1)=1\). Direct multiplication gives
\[
\tfrac12\operatorname{tr}(E_2E_1)
=\cosh^2z+\frac{a^2+b^2}{2ab}\sinh^2z
=1+2\Gamma^2\sinh^2z
=\cosh\bigl(2\operatorname{arsinh}(\Gamma\sinh z)\bigr).
\]
Every entry of \(E_2E_1\) is positive. The two eigenvalues of this positive, determinant-one matrix are \(\exp[\pm2\operatorname{arsinh}(\Gamma\sinh z)]\). Multiplication by \(e^{-\mu T}\) proves the Floquet formula. Each static growth exponent is \(\beta\kappa-\mu\), since each \(A_j\) has eigenvalues \(\pm\kappa\).

**Strict monotonicity and classification.** For \(\Gamma>1\), define \(f(z)=\operatorname{arsinh}(\Gamma\sinh z)\). Direct differentiation gives
\[
f(0)=0,\quad f''(z)=\frac{\Gamma(1-\Gamma^2)\sinh z}{(1+\Gamma^2\sinh^2z)^{3/2}}<0\quad(z>0).
\]
Thus strict concavity gives that \(f(z)/z\) strictly decreases for \(z>0\), and \(\Lambda(T)+\mu=\beta\kappa f(z)/z\) is strictly decreasing. Because \(f'(0)=\Gamma\) and \(f(z)/z\to1\) as \(z\to\infty\), its limits are precisely \(\beta m-\mu\) and \(\beta\kappa-\mu\). The intermediate-value theorem and strict monotonicity establish all sign classifications, including equality at the endpoint recovery rates. If \(a=b\), \(\Gamma=1\), so \(f(z)=z\) and the Floquet exponent is constant.

**Quantitative endpoints.** The Taylor expansions of the hyperbolic sine and inverse hyperbolic sine imply
\[
f(z)=\Gamma z-\frac{\Gamma(\Gamma^2-1)}6 z^3+O(z^5).
\]
Consequently \(\Lambda(T)=\epsilon-C_2T^2+O(T^4)\) near \(T=0\). Strict monotonicity forces the unique zero to tend to zero when \(\epsilon\downarrow0\); the expansion then implies the stated square-root cutoff with relative error \(O(\epsilon)\). For large positive \(z\), \(f(z)=z+\log\Gamma+O(e^{-2z})\), proving the long-period correction.

## Verification

The reproducible standalone file `verify.py` calculates \(E_2E_1\) independently of the closed formula, checks its Perron exponent on 300 seeded random parameter sets, compares 250 finite-difference second derivatives with the exact concavity formula, and tests the crossing plus its square-root onset. It uses only the Python standard library and does not replace the analytic proof.

For the exact contact weights \(a=9\), \(b=1\), infection multiplier \(\beta=1\), and recovery \(\mu=4\), each static disease-free exponent is \(-1\), whereas the fast-switching exponent tends to \(+1\). The unique period threshold is numerically
\[
0.9472132<T_c<0.9472133.
\]
In this example \(C_2=10/3\). The computations corroborate the matrix identity and signs; the infinite-parameter claims follow from the proof, not numerical sampling.

## Relationship to prior work

Sejunti, Taylor and Masuda (arXiv:2406.16787; first public version 24 June 2024) formulate the continuous-time SIS temporal-network linearization and investigate the opposite, **suppressive** paradox using undirected symmetric weighted contact layers. Their numerical search found no reverse cases among symmetric matrices. The present claim concerns unequal **directed** reciprocal contact weights and derives an exact all-period phase boundary, not a theorem that all switched epidemics exhibit this behavior.

Ait Rami, Bokharaie, Mason and Wirth (arXiv:1306.0135, Section 6) already establish that rapid switching can produce persistence even when every individual switched SIS subsystem is stable, provided an average matrix is unstable. Thus the **qualitative possibility** of reverse switching-induced epidemic instability is **prior work**, not a novelty assertion here. The new specialized information is the exact elementary two-group Floquet interpolation, strict period monotonicity, necessary-and-sufficient phase boundary, unique crossing, and square-root onset in the irreducible reciprocal-directed family. Sanatkar and colleagues (arXiv:1501.02472) give matrix-product epidemic threshold criteria for discrete-time switching; these do not state the present continuous-time formula or its all-period monotonicity. Symmetric patch-model frequency monotonicity literature concerns a different symmetry class, and does not transfer to these nonsymmetric contacts without separate proof.

## Limitations

This is a complete invasion-spectrum classification only for two groups, two mirror-oriented layers, equal half-periods, common recovery, and positive reciprocal weights. It does not classify asymmetric dwell fractions, larger graphs, heterogeneous recoveries, or the nonlinear attracting endemic solution for every supercritical period. In a finite stochastic SIS population eventual absorption at zero is possible (indeed unavoidable without spontaneous infection); the Floquet sign concerns the deterministic independent-probability approximation near zero, not permanent stochastic survival. The known rapid-switching existence principle is not claimed to be new, and an abstract equivalent exact two-matrix formula elsewhere remains a bibliographic risk. Independent validation has not been performed.

## References

1. M. I. Sejunti, D. Taylor and N. Masuda, *A Parrondo paradox in susceptible-infectious-susceptible dynamics over periodic temporal networks*, arXiv:2406.16787v1 (24 June 2024); later version https://arxiv.org/html/2406.16787v3.
2. M. Ait Rami, V. S. Bokharaie, O. Mason and F. R. Wirth, *Stability Criteria for SIS Epidemiological Models under Switching Policies*, arXiv:1306.0135; DCDS-B 19 (2014), 2865–2887, https://doi.org/10.3934/dcdsb.2014.19.2865.
3. M. R. Sanatkar, W. N. White, B. Natarajan, C. Scoglio and K. Garrett, *Epidemic Threshold of an SIS Model in Dynamic Switching Networks*, arXiv:1501.02472v2 (2015).
4. X. Liu, Y. Lou and S. Song, *A New Monotonicity for Principal Eigenvalues with Applications to Time-Periodic Patch Models*, SIAM Journal on Applied Mathematics (2022), https://doi.org/10.1137/20M1320973.
