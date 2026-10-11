# Sharp critical-period birth at an isochronous cubic balance in a global quintic Liénard center

## Finding
For every real \(b\ne0\) and \(a>-2\), consider the original-time polynomial vector field
\[
\dot x=y,\qquad \dot y=-x-a x^3-x^5-bxy.
\]
Each nonzero trajectory is periodic (the global-center statement is due to Chen, Li and Zhang). Let \(T_{a,b}(A)\), for \(A>0\), be the *minimal original-time period* of the trajectory starting at \((A,0)\). The period extends evenly and real-analytically to \(A=0\), and its first nonconstant terms are
\[
\frac{T_{a,b}(A)}{2\pi}=1+\frac{b^2-9a}{24}A^2+
\left(\frac{57a^2}{256}-\frac{11ab^2}{384}+\frac{b^4}{2304}-\frac5{16}\right)A^4+O(A^6).
\tag{1}
\]
The codimension-one balance \(a=b^2/9\) cancels the quadratic term, but leaves the **universal, strictly negative quartic coefficient** \(-5/16\), independently of \(b\).

Fix any \(b\ne0\), and vary \(a=(b^2-\mu)/9\) with \(\mu\) near zero. There are numbers \(\epsilon,\delta>0\) such that the period has exactly one critical point in \(0<A<\delta\) when \(0<\mu<\epsilon\), and has none there when \(-\epsilon<\mu\le0\). For \(\mu>0\) the unique small critical point is a strict nondegenerate maximum, with sharp location and height
\[
A_*(\mu)^2=\frac{\mu}{15}+O(\mu^2),\qquad
T_{(b^2-\mu)/9,b}(A_*(\mu))=2\pi+\frac{\pi\mu^2}{360}+O(\mu^3).
\tag{2}
\]
For any fixed admissible \((a,b)\), the opposite endpoint has the original-time asymptotic
\[
\lim_{A\to\infty}A^2 T_{a,b}(A)=\frac{2\sqrt3}{3}\mathrm B\left(\frac16,\frac12\right).
\tag{3}
\]
Consequently, whenever \(a>-2\) and \(b^2>9a\), the period function has an attained global maximum at a positive amplitude (not asserted to be unique). In particular, (2) quantifies the local birth of a maximum from the center as the modified-Emden cubic balance is crossed.

## Assumptions and scope
All parameters and solutions are real. The center is the origin. The amplitude \(A\) is the positive \(x\)-turning coordinate at a point with \(y=0\); it is not an arbitrary Euclidean radius or energy coordinate. A critical point means \(dT_{a,b}/dA=0\) for \(A>0\). The local uniqueness statement has quantifiers \(\forall b\in\mathbb R\setminus\{0\}\ \exists\epsilon,\delta>0\) with \(a=(b^2-\mu)/9>-2\) for \(|\mu|<\epsilon\). This is not a classification of all critical points for all amplitudes. The beta constant in (3) is \(\mathrm B(s,t)=\int_0^1z^{s-1}(1-z)^{t-1}\,dz\).

The supplied global-center premise can be checked against Chen--Li--Zhang's criterion: the restoring polynomial has \(xg(x)>0\) away from zero because \(1+ax^2+x^4=(x^2-1)^2+(a+2)x^2>0\); the odd damping is \(f(x)=bx\); and the integrated damping \(F(x)=bx^2/2\) is even. Their Theorem 4 identifies this normalized family and its global-center domain. No new global-center classification is claimed.

## Proof
**Analytic period and parity.** At the linear center the eigenvalues are \(\pm i\). Near the origin, the flow and the return time to the positive \(x\)-axis are analytic in the nonzero initial amplitude, as follows by the analytic implicit-function theorem for the normalized return map. The vector field is reversible under \((x,y,t)\mapsto(-x,y,-t)\). Every sufficiently small periodic orbit crosses the fixed axis \(x=0\), so that reflection reverses its orientation without changing the orbit. In particular, its two points on the \(x\)-axis have coordinates \(\pm A\), and the periods of initial data \((A,0)\) and \((-A,0)\) agree. Thus the period is even and analytic in \(A\), locally analytic in \(u=A^2\), and analytic in the parameters.

**Exact period constants.** Write \(x(t)=A U(\theta,A)\) and \(\theta=\omega(A)t\), normalized by \(U(0,A)=1\), \(\partial_\theta U(0,A)=0\). Primes below are derivatives in \(\theta\). The equation is
\[
\omega^2 U''+U+bA\omega UU'+aA^2U^3+A^4U^5=0.
\tag{4}
\]
Insert \(U=\cos\theta+\sum_{j\ge1}A^jU_j(\theta)\), with each \(U_j(0)=U'_j(0)=0\), and \(\omega=1+\sum_{j\ge1}w_j A^j\). At every order solve \(U_j''+U_j=-R_j+2w_j\cos\theta\), choosing \(w_j\) to cancel the \(\cos\theta\) resonance. Reversibility cancels the sine resonance. For a Fourier coefficient \(R_{j,k}\) at harmonic \(k\ne\pm1\), the particular coefficient is \(-R_{j,k}/(1-k^2)\); the homogeneous first harmonics are then fixed by the two initial conditions. Explicitly, the first two corrections are
\[
U_1=\frac b3\sin\theta-\frac b6\sin2\theta,
\quad U_2=\left(-\frac a{32}-\frac{23b^2}{288}\right)\cos\theta+\frac{b^2}{9}\cos2\theta+\frac{a-b^2}{32}\cos3\theta.
\]
Continuation of this finite rational Fourier recurrence through order four yields
\[
w_1=w_3=0,\quad w_2=\frac{3a}{8}-\frac{b^2}{24},\quad
w_4=\frac5{16}-\frac{21a^2}{256}-\frac{ab^2}{384}+\frac{b^4}{768}.
\tag{5}
\]
The standalone symbolic check reproduces the resonance elimination and all coefficients without numerical fitting. Since \(T=2\pi/\omega\), substituting (5) gives (1). On \(a=b^2/9\), direct simplification of the quartic coefficient gives exactly \(-5/16\). Finite Fourier arithmetic checks the displayed coefficients; existence and convergence of the underlying local Taylor expansion instead follow from the analytic return-time argument.

**Small critical-period bifurcation.** Hold \(b\ne0\) fixed, set \(a=(b^2-\mu)/9\), and define the analytic map
\[
G(u,\mu)=\frac1{2\pi}\partial_uT_{(b^2-\mu)/9,b}(\sqrt u),\qquad u\ge0.
\]
Equation (1) gives \(G(0,\mu)=\mu/24\), \(G(0,0)=0\), and \(\partial_uG(0,0)=-5/8\ne0\). Therefore the implicit-function theorem gives a unique real-analytic zero \(u_*(\mu)\) near the origin with
\[
u_*(\mu)=\frac{\mu}{15}+O(\mu^2).
\]
For small positive \(\mu\) it lies in \(u>0\); for small negative \(\mu\) it is negative, and at \(\mu=0\) the only local zero is the excluded boundary \(u=0\). Shrinking the neighborhood if needed, \(\partial_uG<0\) throughout, proving absence of additional small positive roots. At \(u=u_*>0\) the second derivative \(d^2T/dA^2=4A^2\partial_u^2T<0\), so the maximum is nondegenerate. Substituting \(u_*(\mu)\) into (1) gives \(T/(2\pi)=1+\mu^2/720+O(\mu^3)\), which is (2).

**High-amplitude endpoint.** For fixed admissible \(a,b\), put \(x=A X\), \(y=A^3Y\), \(s=A^2 t\). With \((X(0),Y(0))=(1,0)\), the rescaled equations are
\[
X'=Y,\qquad Y'=-X^5-\frac bA XY-\frac a{A^2}X^3-\frac1{A^4}X.
\tag{6}
\]
On every compact rescaled time interval, smooth dependence on \(1/A\) gives convergence to the regular Hamiltonian oscillator \(X''+X^5=0\) with the same initial data. This limiting orbit has energy \(Y^2/2+X^6/6=1/6\) and a simple transverse return to the positive turning section \(\{Y=0,X>0\}\) at its minimal period. By the implicit-function theorem for that return and compact separation from earlier positive-turning returns, the corresponding minimal rescaled periods converge. The limiting quarter-period is \(\sqrt3\int_0^1(1-z^6)^{-1/2}\,dz\), hence the full period equals \((2\sqrt3/3)\mathrm B(1/6,1/2)\). Because \(s=A^2t\), this proves (3).

**Existence of a global maximum.** If \(\mu=b^2-9a>0\), (1) implies \(T(A)>2\pi\) for sufficiently small positive \(A\), while (3) implies \(T(A)\to0\) as \(A\to\infty\). Continuity, plus these strict endpoint inequalities, forces the supremum to be attained at a finite positive \(A\). The argument asserts neither uniqueness of that global maximum nor absence of other critical periods.

## Verification
Run `python checks/period_bifurcation_check.py` with `sympy>=1.12,<2` installed. The program represents trigonometric polynomials by exact rational complex Fourier coefficients, solves (4) order-by-order through \(A^4\), verifies both resonant equations, and asserts (1), the parameter-independent quartic restriction, and (2)'s leading coefficients. It prints `CHECK_OK` on success. This is a finite symbolic identity check, not a replacement for the analytic-return and rescaled-flow proofs. The original-time scaling in (6) and the beta-function normalization can be checked directly from the displayed equations.

## Relationship to prior work
Chen, Li and Zhang (arXiv:2208.06184v1, Theorem 4) classified precisely this normalized global-center family, but did not derive its period constants, critical-period birth, or high-amplitude law. Mañosas and Villadelprat's 2006 period theorem applies to *potential Hamiltonian* systems without the term \(bxy\); even its strong global at-most-one-critical-period statement does not cover the present non-Hamiltonian vector field. Oliveira, Sánchez-Sánchez and Torregrosa (2021/2022) provide general period-constant methods and an isochronicity classification, but their theorems do not specify the present normalized quintic family at \(a=b^2/9\) or the sharp branch (2). Classical modified-Emden isochronicity explains why \(a=b^2/9\) is a natural balancing surface for the *cubic truncation*. The retained quintic restoring force breaks that isochronicity at exactly fourth amplitude order. No general novelty claim is made for the implicit-function theorem itself or the pure quintic beta integral.

## Limitations
This is an analytic theorem for the stated coefficient-normalized, globally centered system. Its quantitative critical-point uniqueness is **local near the origin and near the balance surface only**. Global uniqueness, global monotonicity away from that neighborhood, parameter-uniform large-amplitude error bounds, and uniqueness of an absolute maximizer are not established. The claim uses the period in unmodified physical time, not a time-changed orbital equivalent system. Some broad Liénard period-function literature is accessible only by abstract; a prior equivalent specialized coefficient computation cannot be categorically excluded. No independent external audit has been performed.

## References
1. H. Chen, Z. Li, R. Zhang, *A sufficient and necessary condition of generalized polynomial Liénard systems with global centers*, arXiv:2208.06184v1 (first public version 2022-08-12), Theorem 4, https://arxiv.org/pdf/2208.06184.
2. F. Mañosas and J. Villadelprat, *A note on the critical periods of potential systems*, International Journal of Bifurcation and Chaos 16 (2006), 765--774, doi:10.1142/S0218127406015155.
3. R. D. S. Oliveira, I. Sánchez-Sánchez and J. Torregrosa, *Simultaneous Bifurcation of Limit Cycles and Critical Periods*, Qualitative Theory of Dynamical Systems 21 (2022), article 20, doi:10.1007/s12346-021-00546-x.
4. L.-J. Yang and X.-W. Zeng, *The period function of Liénard systems*, Proc. Roy. Soc. Edinburgh Sect. A 143 (2013), 205--221, doi:10.1017/S0308210511000096 (abstract consulted; full text not inspected).
5. H. Li, *Local bifurcations of critical periods for quartic Liénard equations with quintic damping*, Advances in Difference Equations (2012), article 24, doi:10.1186/1687-1847-2012-24.
