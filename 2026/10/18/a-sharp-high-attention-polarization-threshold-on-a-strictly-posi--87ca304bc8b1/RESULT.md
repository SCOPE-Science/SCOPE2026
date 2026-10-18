# A sharp high-attention polarization threshold on a strictly positive two-community graphon

## Finding

A saturated, *entirely cooperative* opinion flow admits stable, persistently polarized states, even though all interactions have strictly positive weight. More precisely, for the equal-mass two-community kernel and parameters below, the two opposite block-polarized branches exist for every \(u>u_-\), but are linearly unstable for \(u_-<u<u_*\) and locally exponentially asymptotically stable for \(u>u_*\). The threshold is the **unique** solution of an explicit hyperbolic equation. For \(u>u_*\), both consensus states are also locally exponentially asymptotically stable, so the full graphon flow has at least four distinct locally exponentially stable stationary states.

Set \(L_-=\gamma(a-b)/2\) and \(L_+=\gamma(a+b)/2\). The polarized states have values \(s\) and \(-s\) on opposite blocks, with \(s>0\) solving \(ds=u\tanh(L_-s)\); they exist precisely for \(u>u_-=d/L_-\). Define \(z_*>0\) as the unique solution
\[
\frac{\sinh(2z_*)}{2z_*}=\frac{L_+}{L_-}=\frac{a+b}{a-b}
\]
and set
\[
 u_*=\frac{d z_*}{L_-\tanh z_*}.
\]
Then \(u_*>u_-\), and the polarized states have exactly one unstable block-mean eigenvalue when \(u_-<u<u_*\), a zero eigenvalue at equality, and no nonnegative eigenvalues when \(u>u_*\). No nonlinear stability classification is asserted at equality.

## Assumptions and scope

Fix a probability space \([0,1]\) with Lebesgue measure, partitioned into two measurable sets \(B_1,B_2\), each of measure \(1/2\). Let \(0<b<a\le1\), \(d>0\), \(\gamma>0\), and \(u>0\). Set the symmetric graphon \(W(y,z)=a\) when \(y,z\) belong to the same block and \(W(y,z)=b\) otherwise. Both within- and between-community weights are strictly positive; hence no inhibitory or negative-weight edge is used.

Consider the zero-bias, zero-self-feedback saturating opinion equation on real \(L^2([0,1])\):
\[
 \partial_t\theta(y,t)=-d\theta(y,t)+u\tanh\!\left(\gamma\int_0^1W(y,z)\theta(z,t)\,dz\right).
\]
The integral defines a bounded finite-rank operator, and the right-hand side is globally Lipschitz on \(L^2\), so there is a unique global solution from every \(L^2\) initial condition. The result concerns stationarity and **local**, not global, basin stability, for the complete continuum equation.

For the explicit choice \(a=1\), \(b=1/3\), \(d=\gamma=1\), the two-community polarization branch exists for \(u>3\), while the stabilizing threshold is \(u_*\approx4.10098722992990\). This provides a concrete interval of unstable polarized equilibria followed by a robust regime of stable polarization under positive social influence.

## Proof

**Step 1: exact block reduction, including non-step initial data.** Put \(m_i(t)=2\int_{B_i}\theta(y,t)\,dy\). Since the nonlinear forcing is constant on each block, integrating the full equation yields the **exact** planar system
\[
\begin{aligned}
 \dot m_1&=-dm_1+u\tanh\!\left(\frac\gamma2(am_1+bm_2)\right),\\
 \dot m_2&=-dm_2+u\tanh\!\left(\frac\gamma2(bm_1+am_2)\right).
\end{aligned}
\]
For almost every \(y\in B_i\), subtracting the mean equation from the original gives
\[
 \theta(y,t)-m_i(t)=e^{-dt}[\theta(y,0)-m_i(0)].
\]
Thus the subspace of block-constant states is invariant and its orthogonal complement decays *exactly* as \(e^{-dt}\). In particular, the full graphon equilibrium problem and its local stability reduce without approximation to the planar block-mean system.

**Step 2: exact existence of the polarized branches.** On the antisymmetric line \((m_1,m_2)=(s,-s)\), the system reduces to
\[
 \dot s=-ds+u\tanh(L_-s).
\]
For \(s>0\), the ratio \(\tanh(L_-s)/s\) decreases strictly from \(L_-\) to zero, because for \(z>0\),
\[
 \tanh z-z\operatorname{sech}^2z>0,
\]
as follows by differentiation: its derivative is \(2z\operatorname{sech}^2z\tanh z>0\) and its value at zero is zero. Hence a unique positive \(s\) exists exactly when \(uL_->d\), and its negative gives the distinct opposite polarized state. Writing \(z=L_-s>0\), the equilibrium equation is equivalent to \(u=d z/(L_-\tanh z)\). By the same inequality, this is a strictly increasing bijection from \((0,\infty)\) to \((u_-,\infty)\).

**Step 3: full spectrum and sharp sign switch.** At either polarized equilibrium the hyperbolic tangent arguments have magnitudes \(z\), hence the planar Jacobian is
\[
 J=-dI+u\operatorname{sech}^2(z)\begin{pmatrix}\gamma a/2&\gamma b/2\\\gamma b/2&\gamma a/2\end{pmatrix}.
\]
The common and antisymmetric eigenvectors have respective eigenvalues
\[
 \lambda_+=-d+uL_+\operatorname{sech}^2z,\qquad
 \lambda_-=-d+uL_-\operatorname{sech}^2z.
\]
Every transverse non-step perturbation has exact eigenvalue \(-d\), with infinite-dimensional eigenspace. Substituting the equilibrium relation gives
\[
 \frac{uL_-\operatorname{sech}^2z}{d}=\frac{2z}{\sinh(2z)}<1,
\]
so \(\lambda_-<0\). Likewise
\[
 \frac{\lambda_+}{d}=-1+\frac{L_+}{L_-}\frac{2z}{\sinh(2z)}.
\]
The function \(h(z)=\sinh(2z)/(2z)\) is strictly increasing from one to infinity for \(z>0\), since \(2z\cosh(2z)-\sinh(2z)\) vanishes at zero and has derivative \(4z\sinh(2z)>0\). As \(L_+/L_->1\), there is a unique crossing \(z_*\). Strict monotonicity of \(u(z)\) transfers this to the unique threshold \(u_*\). Below it \(\lambda_+>0\); above it all three spectral types are strictly negative. Standard finite-dimensional hyperbolic linearization, combined with the exact transverse identity of Step 1, proves the stated local nonlinear instability or exponential asymptotic stability in \(L^2\). At equality the linearization has one zero eigenvalue, and no nonlinear stability verdict is made.

**Step 4: stable consensus coexists with stable polarization.** On the symmetric line \(m_1=m_2=c\), the positive consensus state solves \(dc=u\tanh(L_+c)\). Exactly as in Step 2, it exists uniquely for \(u>d/L_+\); the negative is its counterpart. At \((c,c)\), the Jacobian eigenvalues are \(-d+uL_+\operatorname{sech}^2(L_+c)\) and \(-d+uL_-\operatorname{sech}^2(L_+c)\). The first is negative by the scalar equilibrium inequality; the second is still smaller because \(L_-<L_+\). All transverse modes are \(-d\). Because \(u_*>u_->d/L_+\), for \(u>u_*\) both consensus states and both polarized states coexist and are locally exponentially asymptotically stable. Distinctness follows from their opposite sign patterns.

## Verification

The accompanying standalone `verify.py` reproduces the threshold by bisection, verifies the exact equilibrium identities numerically on each block, checks both Jacobian eigenvalue signs on either side of the threshold, and checks the critical eigenvalue identity. At \(a=1,b=1/3,d=\gamma=1\), one obtains \(z_*\approx1.08865949248265\), \(u_*\approx4.10098722992990\), with polarized common-mode eigenvalue approximately \(0.06286519\) at \(u=4\) and \(-0.21137395\) at \(u=4.5\). These finite checks are illustrative; the proof above is analytic and applies for every admissible real parameter tuple.

## Relationship to prior work

Xing, Bizyaeva and Johansson (2026) introduce this saturating graphon opinion flow and analyze approximation of finite-network dynamics and equilibria by graphon limits. Their work motivates examining explicit continuum stability away from primary bifurcations. Xing, Bizyaeva and Johansson (2024) analyze equilibria and community information in nonlinear opinion dynamics, particularly spectral behavior close to onset. Bizyaeva, Franci and Leonard (2020/2023) establish broader nonlinear-opinion bifurcation phenomena and agreement/disagreement patterns. The existence of multistable opinion dynamics or of polarized states is **not claimed to be new** in general. The narrower contribution here is the exact unrestricted-gain threshold \(\sinh(2z_*)/(2z_*)=(a+b)/(a-b)\), its lift to all continuum perturbations, and coexistence of four robust locally stable equilibria even for a strictly positive two-block kernel and absent intrinsic self-feedback. The inspected claims did not explicitly provide that combined result; whether a broader general bistability theorem subsumes it remains a research-priority risk.

## Limitations

Only equal-mass, symmetric, strictly cooperative **two-block** graphons with no intrinsic self-feedback and zero external bias are covered. The threshold is for **local** attraction; the proof does not classify global basins, all nonsymmetric stationary states, or the nonlinear type of the nonhyperbolic branch at \(u=u_*\). No finite-network probability, finite-size threshold, noisy social dynamics, or empirical human-behavior conclusion follows automatically. The result is a direct specialization of the general model but is not a priority or independent-certification claim.

## References

1. Yu Xing, Anastasia Bizyaeva, Karl H. Johansson, *Behavior of Nonlinear Opinion Dynamics over Large Networks* (2026), arXiv:2609.14086v1, first public September 12, 2026. https://arxiv.org/abs/2609.14086
2. Yu Xing, Anastasia Bizyaeva, Karl H. Johansson, *Learning Communities from Equilibria of Nonlinear Opinion Dynamics* (2024), arXiv:2409.08004. https://arxiv.org/abs/2409.08004
3. Anastasia Bizyaeva, Alessio Franci, Naomi Ehrich Leonard, *Nonlinear Opinion Dynamics with Tunable Sensitivity* (2020 preprint; 2023 publication), arXiv:2009.04332. https://arxiv.org/abs/2009.04332
