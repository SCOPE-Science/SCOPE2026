# A uniform finite-horizon throughput budget for aperiodically driven quadratic ribosome-flow chains

## Finding

**Theorem (finite-horizon nonperiodic throughput and turnpike bound).** Fix an integer \(n\geq1\) and numbers \(0<m\leq M<\infty\). There exist constants \(c=c(n,m,M)>0\) and \(C=C(n,m,M)<\infty\) such that the following holds for **every** horizon \(T>0\), every measurable family of controls \(u_i:[0,T]\to[m,M]\), \(0\leq i\leq n\), and every initial condition \(x(0)\in[0,1]^n\). Let \(x\) be the Carathéodory solution of
\[
\dot x_j=u_{j-1}(t)x_{j-1}(1-x_j^2)-u_j(t)x_j(1-x_{j+1}^2),
\qquad 1\leq j\leq n,
\]
where \(x_0\equiv1\) and \(x_{n+1}\equiv0\). Set the **actual horizon means**
\[
\lambda_i=\frac1T\int_0^T u_i(t)\,dt\qquad (0\leq i\leq n).
\]
Let \(e=e(\lambda)\in(0,1)^n\) be the unique constant-rate equilibrium and let \(R(\lambda)=\lambda_n e_n\) denote its terminal flow. Then
\[
\boxed{\displaystyle
\frac1T\int_0^T u_n(t)x_n(t)\,dt
+\frac{c}{T}\int_0^T\sum_{j=1}^n|x_j(t)-e_j|^2\,dt
\leq R(\lambda)+\frac{C}{T}.}
\]
Neither common periodicity nor recurrence of the controls is assumed. In particular, if the Cesàro means of all controls exist, \(\lambda_i(T)\to\lambda_i^\infty\), then
\[
\limsup_{T\to\infty}\frac1T\int_0^T u_n(t)x_n(t)\,dt\leq R(\lambda^\infty).
\]
Moreover, for any sequence of horizons on which the output average approaches \(R(\lambda^\infty)\), the mean-square distance from the corresponding constant-rate equilibrium tends to zero.

The rate \(C/T\) is genuinely necessary for arbitrary initial states: for one site, constant unit rates, and initial occupancy one, the output average exceeds its stationary benchmark by a positive constant times \(T^{-1}\) as \(T\to\infty\).

## Assumptions and scope

The dimension \(n\) is fixed but arbitrary. The rate bounds \(m,M\) are common to all edges and all times. Controls may be discontinuous, nonperiodic, or nonrecurrent; measurability and the stated essential bounds suffice. The quadratic vacancy factor is precisely \(1-x^2\). The conclusion concerns *unweighted time-averaged terminal throughput* and the squared distance from the constant-rate equilibrium defined by **the same horizon's control means**. Constants do not depend on horizon, control profile, or initial occupancy, but may depend on \(n,m,M\). No fixed constant works uniformly as \(m\downarrow0\) without further hypotheses.

Each vector field is Lipschitz in \(x\) with a uniform Lipschitz constant and measurable in time. At the lower face \(x_j=0\), the derivative is nonnegative; at the upper face \(x_j=1\), it is nonpositive. Thus a unique absolutely continuous trajectory exists and remains in the cube. For any positive constant rate vector, the corresponding equilibrium is unique and interior; see Zhou [1, Theorem 2.2]. Its steady edge factors are
\[
e_0=1,\quad e_{n+1}=0,\quad
c_i=e_i(1-e_{i+1}^2)>0,\quad
\lambda_i c_i=R(\lambda)\quad(0\leq i\leq n).
\]
For completeness, one can establish the needed equilibrium uniqueness without relying on any long-time convergence theorem. Choose an exit current \(R>0\), set \(e_n=R/\lambda_n\), and recursively define \(e_i=R/[\lambda_i(1-e_{i+1}^2)]\) backwards. Starting at \(R=0\), all these coordinates increase strictly and continuously until the first admissibility boundary. This boundary occurs when \(e_1\) reaches one: if a later coordinate reached one earlier, the preceding coordinate would diverge before that point. The entrance-current difference \(\lambda_0(1-e_1(R)^2)-R\) decreases strictly from a positive value to a negative value, so it has exactly one zero. That zero yields the unique interior equilibrium. Compactness then gives continuity of \(e(\lambda)\) on \([m,M]^{n+1}\): any convergent subsequence of equilibria solves the limiting equilibrium equations, and the interior limits are forced by the positive boundary flux recursion. All coordinates therefore stay uniformly away from zero and one on this compact rate cube.

## Proof

**1. Weights, edge errors, and an exact storage identity.** Fix a horizon and suppress its dependence in \(\lambda,e,R\). Write \(z_j=x_j-e_j\), with \(z_0=z_{n+1}=0\), and define
\[
\theta_j=\frac{2e_j^2}{1-e_j^2},\qquad
p_j=p_{j-1}\theta_j\quad(1\leq j\leq n),\qquad
\sum_{i=0}^n p_i=1.
\]
Every \(p_i\) is positive. For the edge factors define
\[
\begin{aligned}
\eta_i&=(1-e_{i+1}^2)z_i-2e_i e_{i+1}z_{i+1},\\
\rho_i&=x_i(1-x_{i+1}^2)-c_i-\eta_i,\\
d_i(x;\lambda)&=\frac{\eta_i^2}{c_i}-\left(1-\frac{\eta_i}{c_i}\right)\rho_i,
\qquad (0\leq i\leq n).
\end{aligned}
\]
Let \(q_i(t)=u_i(t)x_i(t)(1-x_{i+1}(t)^2)\). The source of the edge-dissipation construction is Zhou [1, §3]; the following **nonperiodic storage form** retains boundary terms that disappear when averaging a periodic orbit:
\[
V_\lambda(x)=\frac12\sum_{j=1}^n\frac{p_j}{e_j}z_j^2,
\qquad
H_\lambda(x)=V_\lambda(x)+\sum_{j=1}^n\left(\sum_{i=0}^{j-1}p_i\right)x_j.
\]
The recursion for the \(p_i\) gives the telescoping identity
\[
\frac{p_i}{c_i}\eta_i=
\frac{p_i}{e_i}z_i-\frac{p_{i+1}}{e_{i+1}}z_{i+1}
\quad (i<n),
\]
interpreting the first term as zero at the entrance edge. At the exit, \(p_n\eta_n/c_n=p_nz_n/e_n\). Consequently, conservation \(\dot x_j=q_{j-1}-q_j\) gives, for almost every \(t\),
\[
\dot V_\lambda=-\sum_{i=0}^n\frac{p_i}{c_i}q_i\eta_i.
\]
By the definitions of the Taylor remainder and dissipation,
\[
q_i-u_ic_i+u_id_i=\frac{q_i\eta_i}{c_i}.
\]
Also conservation yields the *unaveraged* weighted-flow decomposition
\[
\sum_{i=0}^n p_iq_i=q_n+
\frac d{dt}\sum_{j=1}^n\left(\sum_{i=0}^{j-1}p_i\right)x_j.
\]
Combining these algebraic equalities proves the exact, pointwise, nonperiodic balance
\[
\boxed{\displaystyle
q_n+\sum_{i=0}^np_i u_i d_i+\frac d{dt}H_\lambda(x)
=\sum_{i=0}^np_i u_i c_i.}
\tag{1}
\]
The reference \(\lambda\) remains fixed **throughout the chosen horizon**. Its dependence on \(T\) creates no extra derivative in (1).

**2. Uniform quadratic lower bound on dissipation.** For each edge \(i<n\), write \(a=e_i>0\), \(b=e_{i+1}\in(0,1)\), \(y=x_{i+1}\in[0,1]\), and
\[
r=\frac{x_i-a}{a},\qquad
s=\frac{2b(y-b)}{1-b^2},\qquad
A=\frac{1-y^2}{1-b^2}.
\]
At the entrance edge \(i=0\), take \(a=x_0=1\), so \(r=0\). Direct substitution, not a limiting argument, gives the exact identity
\[
\frac{d_i}{c_i}=1-A(1+r)(1-r+s).
\tag{2}
\]
If \(s\leq-2\), then \(r\geq-1\) and \((1+r)(1-r+s)\leq0\), whence \(d_i/c_i\geq1\). If \(s>-2\), complete the square:
\[
\frac{d_i}{c_i}=A\left(r-\frac{s}{2}\right)^2+G_b(y),
\qquad
G_b(y)=1-\frac{1-y^2}{1-b^2}
\left(1+\frac{b(y-b)}{1-b^2}\right)^2.
\tag{3}
\]
For \(y<1\), strict convexity of \(W(y)=(1-y^2)^{-1/2}\) implies \(G_b(y)>0\) whenever \(y\ne b\) and \(s>-2\); at \(y=1\) it equals one. This argument includes \(y=0\) whenever \(s>-2\). An explicit Taylor calculation gives
\[
\lim_{y\to b}\frac{G_b(y)}{(y-b)^2}
=\frac{1+2b^2}{(1-b^2)^2}>0.
\tag{4}
\]
Consequently, for every compact interval \(K\subset(0,1)\) there exists \(k_K>0\) such that, for all \(b\in K\) and \(0\le y\le1\) with \(s>-2\), one has \(G_b(y)\ge k_K(y-b)^2\). This follows by extending the ratio continuously across \(y=b\) using (4) and minimizing it on the compact set \(b\in K\), \(y\in[0,1]\), \(s\ge-2\). Decreasing \(k_K\) to at most one covers \(s\le-2\) by the previous estimate. The bounds from both cases therefore imply
\[
\boxed{\displaystyle d_i(x;\lambda)\ge c_i k_K(x_{i+1}-e_{i+1})^2,\qquad 0\le i<n.}
\tag{5}
\]
This includes configurations on the boundary. In addition \(d_n=z_n^2/e_n\ge0\).

Take \(K\) to contain every equilibrium coordinate of every \(\lambda\in[m,M]^{n+1}\). The positive continuous quantities \(p_i(\lambda)c_i(\lambda)\) then have a uniform positive minimum, so (5) yields a constant \(\kappa=\kappa(n,m,M)>0\) satisfying
\[
\sum_{i=0}^np_i(\lambda)d_i(x;\lambda)
\ge\kappa\sum_{j=1}^n(x_j-e_j(\lambda))^2
\quad\text{for every }x\in[0,1]^n.
\tag{6}
\]
Since \(u_i\ge m\), the instantaneous weighted dissipation in (1) is at least \(m\kappa\sum_jz_j^2\).

**3. Integrate over an arbitrary horizon.** Since \(\lambda_i c_i=R\) and \(\lambda_i=T^{-1}\int_0^Tu_i\),
\[
\int_0^T\sum_{i=0}^np_i u_i c_i\,dt
=T\sum_{i=0}^np_i\lambda_i c_i=TR.
\]
Integrating the exact identity (1) gives
\[
\frac1T\int_0^Tq_n\,dt+
\frac1T\int_0^T\sum_{i=0}^np_i u_i d_i\,dt
=R+\frac{H_\lambda(x(0))-H_\lambda(x(T))}{T}.
\tag{7}
\]
On the compact set of rate references \(\lambda\in[m,M]^{n+1}\) and states \(x\in[0,1]^n\), the storage \(H_\lambda(x)\) is uniformly bounded. Define
\[
C=\max_{\lambda\in[m,M]^{n+1}}
\left(\max_{x\in[0,1]^n}H_\lambda(x)-\min_{x\in[0,1]^n}H_\lambda(x)\right)<\infty.
\]
Together with (6), equation (7) proves the theorem with \(c=m\kappa\). No periodic orbit, invariant probability measure, or recurrence argument has been used.

**4. Long-time consequence and optimal transient order.** If \(\lambda(T)\to\lambda^\infty\), continuity of the equilibrium implies \(R(\lambda(T))\to R(\lambda^\infty)\). Dropping the nonnegative penalty and sending \(T\to\infty\) proves the stated limsup bound. If the output averages converge to this upper bound, (7)–(6) imply that the squared time-averaged distance from \(e(\lambda(T))\) vanishes; uniform convergence \(e(\lambda(T))\to e(\lambda^\infty)\) gives the same conclusion for the limiting equilibrium.

For necessity of a transient correction, take \(n=1\), \(u_0=u_1=1\), \(x(0)=1\). The constant equilibrium is \(e=(\sqrt5-1)/2\), and the scalar equation factors as
\[
\dot x=1-x-x^2=-(x-e)(x+e+1).
\]
The solution decreases toward \(e\), and a change of variables gives the **positive exact total transient excess**
\[
\int_0^\infty (x(t)-e)\,dt
=\int_e^1\frac{dx}{x+e+1}
=\log\frac{e+2}{2e+1}>0.
\]
It follows that
\[
\frac1T\int_0^T x(t)\,dt
=e+\frac1T\log\frac{e+2}{2e+1}+o(T^{-1}).
\]
Hence the uncorrected finite-horizon inequality is false even for constant controls and one site, and the order \(T^{-1}\) cannot be improved uniformly over initial states.

## Verification

The attached self-contained `verify.py` uses exact rational arithmetic. It constructs rational steady states and their compatible edge rates, independently computes the flux Jacobian action, weighted quadratic storage derivative, edge remainders, and the new pointwise identity, and confirms nonnegative dissipation at sampled configurations including boundary states. It checks \(n=1,2,3\) and multiple distinct rate vectors. Executing `python verify.py` produced:

`VERIFY_OK: 3170 exact rational identities/nonnegative dissipations; n=1,2,3; all boundary states sampled`

The infinite-dimensional statement in the number of choices of \(n\), controls, and horizons is proved by identities (1)–(7), not by finite enumeration. The exact-rational verification only stress-tests the algebra. Formula (4) is also independently consistent with the positive explicit endpoint dissipation
\[
d_0=\frac{1+e_1^2+2e_1x_1}{1-e_1^2}(x_1-e_1)^2.
\]

## Relationship to prior work

Zhou [1, §3, Theorems 3.2 and 3.5] supplies the nonlinear edge-error and weighted-dissipation ingredients for **jointly periodic controls evaluated on their periodic solution**. The present finding retains the previously canceled storage term, combines conservation of fluxes with a second storage component, proves a control- and horizon-uniform quadratic dissipation inequality, and obtains a **finite-horizon nonperiodic throughput bound for arbitrary initial states**. This responds to [1, §7]'s explicit question about noncommon-period and more general recurrent input regimes. The nonlinear curvature property itself and the underlying periodic no-gain theorem are credited to [1].

Massas and Margaliot [2] treat the **classical linear vacancy factor** and **periodic** controls. Their full derivation of a weighted quadratic Lyapunov function is closely related, but their Theorem 1 and Proposition 7 do not state a nonperiodic, all-initial-state finite-horizon budget for the quadratic vacancy law. Ali Al-Radhawi, Margaliot, and Sontag [3] analyze periodic optimal allocation, including terminal boundary conditions for optimizing periodic orbits; they do not state this quantitative aperiodic result. Massas and Margaliot [4] study feedforward nonlinear filter cascades under periodic input, which differ structurally from the mutually coupled exclusion chain. Broader pre-existing dissipativity/storage principles are acknowledged: the novelty asserted here is the precise uniform chain-specific inequality and its aperiodic mean-rate corollary, **not** the general idea of integrating a storage identity.

## Limitations

The result is confined to the quadratic vacancy law and to controls uniformly bounded above and bounded away from zero. It does not establish no-gain for vacancy laws with nonconvex reciprocal-square-root response; positive gain is known to occur for some such laws [1]. It does not assert convergence of occupancy trajectories, an aperiodic attracting response, existence of a time-average for the output, or any conclusion uniform in an unbounded number of sites. Equality rigidity for arbitrary aperiodic forcing is not claimed. The constant \(c\) is proved positive but not optimized. An equivalent statement may exist in earlier nonperiodic control or dissipativity literature; originality remains provisional pending independent literature and scientific review.

## References

[1] H. Zhou, *Gain of Entrainment in Ribosome Flow Models with Nonlinear Steric Hindrance: Global Rigidity and Dimension-Induced Gain*, arXiv:2610.10602v1 (first posted 7 October 2026), §§2–3 and 7. https://arxiv.org/html/2610.10602v1

[2] R. Massas and M. Margaliot, *On the Cost of Entrainment in Protein Translation*, arXiv:2607.25435v1 (28 July 2026), Theorem 1, Proposition 7 and proof. https://arxiv.org/abs/2607.25435

[3] M. Ali Al-Radhawi, M. Margaliot and E. D. Sontag, *Maximizing average throughput in oscillatory biochemical synthesis systems: an optimal control approach*, Royal Society Open Science 8 (2021), 210878. https://pmc.ncbi.nlm.nih.gov/articles/PMC8456142/

[4] R. Massas and M. Margaliot, *Gain of Entrainment in Nonlinear Cascades*, arXiv:2608.15214v1 (15 August 2026). https://arxiv.org/abs/2608.15214
