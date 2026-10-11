# Heightwise variance rigidity and a strict contraction gap in a hidden-attractor quadratic flow

## Finding

For real parameters \(k>0\), \(p>q>0\), and \(c\in\mathbb R\), consider the polynomial flow
\[
\dot x=z,\qquad \dot y=x-y,\qquad \dot z=c-kx-pxz+qyz.
\]
It contains system SE17 of Molaie, Jafari, Sprott and Golpayegani at \((k,p,q,c)=(31/10,3/10,1/5,57/100)\). Let
\[
P=z+\frac p2x^2-qxy+\frac q2y^2,
\qquad E_c=(c/k,c/k,0).
\]
For **every compactly supported invariant Borel probability measure** \(\mu\) of this flow, the following heightwise stationary law holds for \(\mu\)-almost every value of \(P\):
\[
\boxed{\mathbb E_\mu[kx+q(x-y)^2\mid P]=c.}
\]
In particular, writing \(d_\mu=\int(x-y)^2\,d\mu\) and \(\bar x=\int x\,d\mu\),
\[
\boxed{\bar x=\frac ck-\frac qk d_\mu\le \frac ck.}
\]
Equality holds **if and only if** \(\mu=\delta_{E_c}\). The stable-filter coordinate also obeys the separate heightwise law \(\mathbb E_\mu[x\mid y]=y\), which implies
\[
d_\mu=\operatorname{Var}_\mu(x)-\operatorname{Var}_\mu(y).
\]
The mean infinitesimal phase-volume contraction \(\mathcal L(\mu)=\int\nabla\cdot F\,d\mu\) satisfies the exact rigidity identity
\[
\boxed{\mathcal L(\mu)=-1-\frac{(p-q)c}{k}+\frac{(p-q)q}{k}d_\mu.}
\]
Thus every stationary state other than the equilibrium atom has **strictly larger** mean divergence than the equilibrium, and its mean \(x\)-coordinate lies strictly below the equilibrium's coordinate. For an ergodic such measure \(\mathcal L\) is the sum of its three Lyapunov exponents almost surely, by the derivative determinant identity.

At the published SE17 parameters these statements become the exact laws
\[
\mathbb E_\mu[x\mid P]=\frac{57}{310}-\frac2{31}\mathbb E_\mu[(x-y)^2\mid P],\qquad
\mathcal L(\mu)=-1-\frac{57}{3100}+\frac1{155}d_\mu.
\]
They apply to any compact stationary state, whether an equilibrium, a periodic orbit, or a nontrivial attractor, **without assuming that a chaotic invariant measure has been proved to exist**.

## Assumptions and scope

The phase space is \(\mathbb R^3\); the vector field is the displayed polynomial, and \(\mu\) is any invariant Borel probability supported on a compact invariant set, not necessarily ergodic. Conditional expectations are taken with respect to the observable \(P\) or \(y\), respectively, on the probability space \((\mathbb R^3,\mu)\). Compact support ensures all test functions, moments and Oseledets integrability conditions used here. Nothing assumes that every initial condition generates a bounded orbit. The inequalities use \(k>0\), \(q>0\), and \(p>q\); the underlying polynomial identity holds for all real coefficients.

## Proof

**(1) A polynomial coboundary.** Differentiating \(P\) along the vector field yields
\[
\begin{aligned}
\dot P&=c-kx-pxz+qyz+pxz-q(yz+x(x-y))+qy(x-y)\\
&=\boxed{c-kx-q(x-y)^2}.
\end{aligned}
\]
The original quadratic transport terms cancel exactly. For every differentiable scalar test function \(\varphi\), invariance and compact support imply \(\int\varphi'(P)\dot P\,d\mu=0\). Define the compactly supported finite signed measure \(\nu(B)=\int_{P^{-1}(B)}\dot P\,d\mu\). Its distributional derivative vanishes because \(\int\varphi'\,d\nu=0\) for every compactly supported smooth \(\varphi\); therefore \(\nu\) is a constant multiple of Lebesgue measure, and compact support forces \(\nu=0\). Consequently \(\mathbb E_\mu[\dot P\mid P]=0\) almost surely, giving the first heightwise identity and its integrated mean law.

**(2) A heightwise stable-filter law.** Since \(\dot y=x-y\), apply the same compactly supported signed-measure argument to \(y\) to obtain \(\mathbb E_\mu[x-y\mid y]=0\). Therefore \(\mathbb E[x]=\mathbb E[y]\) and \(\mathbb E[xy]=\mathbb E[y^2]\). Expanding \(\mathbb E[(x-y)^2]\) and using equality of means proves the variance identity.

**(3) Strictness of the moment gap.** If \(d_\mu=0\), then \(x=y\) almost surely. The support of an invariant probability is invariant under the flow on its compact support. Thus every trajectory in that support remains in \(x=y\). On this subspace, \(\dot y=0\); hence \(y\) and \(x=y\) are constant. The equation \(\dot x=z\) then forces \(z=0\), and \(\dot z=c-kx\) forces \(x=y=c/k\). The support is the singleton \(E_c\), hence \(\mu=\delta_{E_c}\). Conversely this atom is invariant and has zero defect. Since \(q>0\), every other invariant measure has \(\bar x<c/k\).

**(4) Strict phase-volume gap.** Direct differentiation gives \(\nabla\cdot F=-1-px+qy\). Using \(\int y=\int x\),
\[
\mathcal L(\mu)=-1-(p-q)\bar x
=-1-\frac{(p-q)c}{k}+\frac{(p-q)q}{k}d_\mu.
\]
As \(p>q>0\), strictness follows from step (3). On each compact invariant support the flow is complete, and the fundamental-matrix determinant satisfies \(\log|\det D\phi_t|=\int_0^t\nabla\cdot F(\phi_s)\,ds\). For ergodic \(\mu\), Birkhoff's and Oseledets' theorems identify its limit divided by \(t\) with the sum of Lyapunov exponents. No positive or zero Lyapunov exponent is assumed.

## Verification

The accompanying standalone `check_se17.py` uses symbolic differentiation to check the polynomial coboundary, the stable-filter product identities, the Jacobian trace and equilibrium substitution. It checks the exact rational reductions at the original SE17 coefficient tuple and emits `SE17_SYMBOLIC_CHECKS_PASS`. These computer-algebra steps support the algebra only; the conditional-expectation, compact-invariance and strictness arguments above are analytical proofs. Reproduce using Python 3 and SymPy with `python check_se17.py`.

## Relationship to prior work

Molaie et al. (2013, Table 1, SE17) introduced the displayed source equation and reported numerical Lyapunov data for a hidden-attractor regime, but gave neither the observable \(P\) nor its conditional stationary law or exact contraction-gap formula. Guo (2018) studies a different planar Liénard family with a genuine cubic term in its primitive damping function, rather than this three-dimensional quadratic cross-feedback system; its theorems do not imply the stated heightwise identity. Li et al. (2021) investigate Jacobi stability of simple chaotic systems at selected parameters; only abstract-level material was accessible for this comparison, so exact priority relative to its full body is not settled. Generic invariant-flux and Liouville principles are known, but those principles alone do not supply the source-specific cancelling polynomial \(P\).

## Limitations

No proof is offered for existence, uniqueness, or smoothness of any non-equilibrium compact invariant measure at the published parameters; the reported chaotic dynamics are a motivation, not a premise. The theorem is a collection of exact **necessary stationary constraints**, not a full classification of attractors or basins. A compact invariant set with connecting orbits need not itself support a nontrivial stationary measure. Historical priority may be affected by unindexed work or by the inaccessible body of the 2021 follow-up. The strict divergence comparison requires \(p>q>0\); the equality law remains algebraically valid beyond this range but may lose its strict sign.

## References

1. M. Molaie, S. Jafari, J. C. Sprott and S. M. R. H. Golpayegani, *Simple chaotic flows with one stable equilibrium*, International Journal of Bifurcation and Chaos **23** (2013), 1350188, DOI: 10.1142/S0218127413501885. Author-hosted full text: https://sprott.physics.wisc.edu/pubs/paper399.pdf .
2. F. Guo, *Global Analysis of a Liénard System with Quadratic Damping*, Journal of Applied Mathematics (2018), Article 1249620, DOI: 10.1155/2018/1249620.
3. C. Li et al., *Jacobi Stability of Simple Chaotic Systems With One Lyapunov Stable Equilibrium*, Journal of Computational and Nonlinear Dynamics (2021), DOI: 10.1115/1.4050954 (abstract-level comparison only).
