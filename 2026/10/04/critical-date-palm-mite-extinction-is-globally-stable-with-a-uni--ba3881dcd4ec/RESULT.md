# Critical date-palm-mite extinction is globally stable with a universal \(t^{-1}\) stage profile
## Finding
Consider the uncontrolled four-stage date-palm-mite model
\[
\begin{aligned}
\dot E&=\frac{\beta A}{1+(A+N+L)/K}-\alpha_1E,\\
\dot L&=\gamma_EE-\alpha_2L,\\
\dot N&=\gamma_LL-\alpha_3N,\\
\dot A&=\gamma_NN-\mu_AA,
\end{aligned}
\]
where \(\alpha_1=\gamma_E+\mu_E\), \(\alpha_2=\gamma_L+\mu_L\), and \(\alpha_3=\gamma_N+\mu_N\), with every displayed biological parameter and \(K\) strictly positive. At the exact reproduction threshold
\[
\mathcal R_0=\frac{\beta\gamma_E\gamma_L\gamma_N}{\alpha_1\alpha_2\alpha_3\mu_A}=1,
\]
the extinction equilibrium \(P_0=(0,0,0,0)\) is globally asymptotically stable on \(\mathbb R_{\ge0}^4\).

The critical convergence is not exponential. Define
\[
r=\left(\frac{\beta}{\alpha_1},\frac{\beta\gamma_E}{\alpha_1\alpha_2},\frac{\beta\gamma_E\gamma_L}{\alpha_1\alpha_2\alpha_3},1\right)^T,
\]
\[
H=\frac1{\alpha_1}+\frac1{\alpha_2}+\frac1{\alpha_3}+\frac1{\mu_A},
\qquad
C=1+r_L+r_N,
\qquad
Q=\frac{KH}{C}.
\]
For every nonzero initial state in \(\mathbb R_{\ge0}^4\),
\[
t\,(E(t),L(t),N(t),A(t))\longrightarrow Qr.
\]
Equivalently, \(tA(t)\to Q\), while the other three stage limits are obtained by multiplying \(Q\) by the first three components of \(r\). Hence the exact threshold still lies on the extinction side when dynamics are restricted to the biological cone, but extinction is critically slowed to order \(t^{-1}\).

## Assumptions and scope
The claim concerns exactly the autonomous uncontrolled system displayed above and the nonnegative state cone. All transition, mortality, reproduction, and carrying-capacity parameters are strictly positive. The equality \(\mathcal R_0=1\) is imposed exactly; no perturbative statement away from threshold is used.

The asymptotic formula excludes only the zero initial state, whose solution is identically zero. No claim is made about the controlled system, stochastic perturbations, parameter uncertainty, finite-time eradication, or field validity of the biological parameterization. The result is an infinite-time statement for the deterministic ODE.

## Proof
Write \(S=A+N+L\). The source uses the positive linear Lyapunov function
\[
V=c_1E+c_2L+c_3N+A,
\]
with
\[
c_1=\frac{\gamma_E\gamma_L\gamma_N}{\alpha_1\alpha_2\alpha_3},\qquad
c_2=\frac{\gamma_L\gamma_N}{\alpha_2\alpha_3},\qquad
c_3=\frac{\gamma_N}{\alpha_3}.
\]
At \(\mathcal R_0=1\), the identity \(c_1\beta=\mu_A\) is exact, so differentiation gives the stronger equality
\[
\dot V
=\mu_AA\left(\frac1{1+S/K}-1\right)
=-\frac{\mu_AAS}{K+S}\le0.
\]
Because \(V\) is positive definite and nonincreasing, every nonnegative trajectory is bounded and the origin is Lyapunov stable. The largest invariant subset of \(\{\dot V=0}\) is only the origin: if \(A=0\) on an invariant trajectory then \(\dot A=\gamma_NN\) forces \(N=0\); then \(\dot N=\gamma_LL\) forces \(L=0\); then \(\dot L=\gamma_EE\) forces \(E=0\). If instead \(S=0\), the same chain begins immediately. LaSalle's invariance principle therefore gives global convergence to \(P_0\). Together with Lyapunov stability, this proves global asymptotic stability on the biological cone.

It remains to determine the sharp rate. Let \(J\) be the Jacobian at \(P_0\) at threshold. Its characteristic polynomial is
\[
\prod_{q\in\{\alpha_1,\alpha_2,\alpha_3,\mu_A\}}(\lambda+q)-\alpha_1\alpha_2\alpha_3\mu_A.
\]
Thus \(0\) is a simple eigenvalue. After factoring out \(\lambda\), the remaining cubic has the positive elementary-symmetric coefficients \(e_1,e_2,e_3\) of \(\alpha_1,\alpha_2,\alpha_3,\mu_A\), and \(e_1e_2>e_3\). The cubic Routh-Hurwitz criterion therefore puts its three roots strictly in the open left half-plane.

A right zero eigenvector with adult component normalized to one is the vector \(r\) above. A positive left zero eigenvector is
\[
\ell=\left(1,\frac{\alpha_1}{\gamma_E},\frac{\alpha_1\alpha_2}{\gamma_E\gamma_L},\frac{\beta}{\mu_A}\right)^T,
\]
where the last component uses the threshold identity. Direct multiplication gives
\[
\ell^Tr=\beta H.
\]
Put \(p=\ell/(\beta H)\), so \(p^Tr=1\), and define the scalar critical coordinate \(z=p^Tx\) for \(x=(E,L,N,A)^T\). Separating the linearization from the nonlinear recruitment term gives
\[
\dot x=Jx+\mathbf e_E n(x),
\qquad
n(x)=-\frac{\beta AS}{K+S}.
\]
Since \(p^TJ=0\) and the first component of \(p\) is \(1/(\beta H)\), there is the exact identity
\[
\dot z=-\frac{AS}{H(K+S)}.
\]
For every nonzero nonnegative state, \(z>0\). Because every component of \(p\) is positive, \(\|x\|_1\le c z\) for a fixed \(c>0\) on the nonnegative cone. Hence \(|n(x)|\le Bz^2\) and \(|\dot z|\le B'z^2\) for fixed constants \(B,B'>0\).

Now decompose \(x=zr+u\), where \(p^Tu=0\). The subspace \(p^Tu=0\) is the stable spectral subspace of \(J\), so its semigroup decays exponentially. Variation of constants gives
\[
u(t)=e^{J(t-t_0)}u(t_0)+\int_{t_0}^t e^{J(t-s)}(I-rp^T)\mathbf e_E n(x(s))\,ds.
\]
The bound \(|\dot z|\le B'z^2\) gives \((1/z)'\le B'\). Set \(R(t)=1/(2B'z(t))\). For \(0\le t-s\le R(t)\), integration of the reciprocal inequality gives \(z(s)\le2z(t)\), so the recent part of the convolution is \(O(z(t)^2)\). On \(t-s\ge R(t)\), boundedness of the trajectory and exponential stability give an \(O(\exp(-\delta R(t)))\) tail. The initial stable transient is \(O(e^{-\delta t})\). Finally \((1/z)'\le B'\) also gives \(z(t)\ge 1/(c+B't)\), so both exponential terms are \(o(z(t))\). Therefore \(u(t)=o(z(t))\).

Therefore
\[
A=z+o(z),\qquad S=Cz+o(z).
\]
Substitution into the exact equation for \(z\) yields
\[
\dot z=-\frac{C}{KH}z^2(1+o(1)).
\]
Writing \(\kappa=C/(KH)\), we obtain
\[
\left(\frac1z\right)'\longrightarrow\kappa,
\qquad
z(t)\sim\frac1{\kappa t}=\frac{Q}t.
\]
Since \(x=zr+o(z)\), the claimed vector limit \(t x(t)\to Qr\) follows.

## Verification
The proof uses exact identities and asymptotic estimates, not finite enumeration. The packaged script `verification/verifier.py` checks the threshold relation, both zero-eigenvector identities, the normalization \(\ell^Tr=\beta H\), the critical coefficient \(\kappa=C/(KH)\), and an exact rational witness.

For the witness
\[
\gamma_E=\gamma_L=\gamma_N=1,\quad
\mu_E=\mu_L=\mu_N=1,\quad
\mu_A=1,\quad K=10,\quad\beta=8,
\]
one has \(\alpha_1=\alpha_2=\alpha_3=2\), \(\mathcal R_0=1\), \(r=(4,2,1,1)^T\), \(H=5/2\), \(C=4\), \(\kappa=4/25\), and \(Q=25/4\). Thus the theorem predicts
\[
t(E,L,N,A)\longrightarrow\left(25,\frac{25}2,\frac{25}4,\frac{25}4\right).
\]
Running `python3 verification/verifier.py` returns `VERIFY_OK`. The script is a consistency check for the displayed algebra; the generic proof is the argument above, not the single witness.

## Relationship to prior work
Aljurbua and El-Shahed derive this four-stage Beverton-Holt model, the threshold \(\mathcal R_0\), global extinction for the strict regime \(\mathcal R_0<1\), and a forward transcritical bifurcation at \(\mathcal R_0=1\). Their global theorem explicitly excludes equality, and their discussion describes the critical point as nonhyperbolic. The present result closes that equality case on the biologically relevant cone and adds the exact all-stage \(t^{-1}\) profile.

The source's forward-bifurcation calculation does not by itself imply the global critical conclusion: a local transcritical normal form controls a neighborhood and does not supply global attraction from arbitrary nonnegative data. Nor does the strict-subthreshold Lyapunov theorem cover equality. The equality identity for \(\dot V\), combined with the invariant-set argument, supplies the missing global step; the stable-mode decomposition then supplies the sharp rate and stage ratios.

A closely related pest-control predecessor by Fitri, Hanum, Kusnanto, and Bakhtiar uses an eleven-compartment plant-insect-pathogen system with different controls and does not contain this four-stage critical threshold problem. Searches for stage-structured Beverton-Holt critical decay, date-palm-mite critical extinction, and equivalent algebraic-relaxation formulations found no source stating or dominating the theorem above.

## Limitations
The theorem is specific to the deterministic four-stage chain and to the exact density-dependent recruitment law in the source. It does not establish robustness of the \(t^{-1}\) coefficient under model perturbations. The literature comparison cannot prove absolute uniqueness; obscure or unindexed work could exist. The result also does not convert asymptotic extinction into a finite-time pest-eradication guarantee.

## References
1. Saleh Fahad Aljurbua and Moustafa El-Shahed, “Cost-effective strategies for controlling date palm mite infestations: an optimal control approach,” AIMS Mathematics 11(8), 26359–26396 (2026), DOI 10.3934/math.20261058.
2. Ihza Rizkia Fitri, Farida Hanum, Ali Kusnanto, and Toni Bakhtiar, “Optimal Pest Control Strategies with Cost-effectiveness Analysis,” The Scientific World Journal (2021), Article 6630193, DOI 10.1155/2021/6630193.
