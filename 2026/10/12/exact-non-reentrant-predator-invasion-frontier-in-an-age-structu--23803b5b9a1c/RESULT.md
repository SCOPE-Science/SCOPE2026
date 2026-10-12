# Exact non-reentrant predator-invasion frontier in an age-structured role-reversal model
## Finding
For the age-structured role-reversal model, the predator-free equilibrium is
\[
(\bar x,\bar u)=\left(\frac{r}{a},0\right).
\]
At this state, define
\[
\phi_A(\tau)=\frac{1}{1+e^{-\nu(\tau-\tau^*)}},
\qquad
\phi_J(\tau)=\frac{1}{1+e^{-\nu(\tau^*-\tau)}},
\]
and
\[
S_g(\tau)=\exp\!\left(
-\int_0^\tau
\left[g\bar x\,\phi_J(s)+\mu_B(s)+\mu_Me^{-\rho\bar x}\right]ds
\right).
\]
Then the exact low-density predator reproduction number is
\[
\mathcal R_P(g,k)=
\int_0^\infty
\left[
k\bar x\,\phi_A(\tau)+
\tilde B(\tau)(1-e^{-\zeta\bar x})
\right]S_g(\tau)\,d\tau.
\]

The predator-free equilibrium is linearly exponentially stable when
\[
\mathcal R_P(g,k)<1,
\]
unstable when
\[
\mathcal R_P(g,k)>1,
\]
and has a zero invasion eigenvalue at equality.

Moreover,
\[
\mathcal R_P(g,k)=A(g)+k\bar x\,C(g),
\]
where
\[
A(g)=(1-e^{-\zeta\bar x})
\int_0^\infty\tilde B(\tau)S_g(\tau)\,d\tau,
\]
\[
C(g)=\int_0^\infty\phi_A(\tau)S_g(\tau)\,d\tau.
\]
Both \(A\) and \(C\) are strictly decreasing in the juvenile-consumption parameter \(g\). Therefore the exact reproduction threshold in \(k\),
\[
k_c(g)=\frac{1-A(g)}{\bar x\,C(g)},
\]
whenever \(A(g)<1\), is strictly increasing in \(g\). For fixed \(k\), \(\mathcal R_P(g,k)\) strictly decreases to zero as \(g\to\infty\), so if invasion is possible at \(g=0\), there is exactly one threshold \(g_c(k)\).

For the exact sharp-maturation limit and the source's explicit profiles,
\[
\tilde B(\tau)=
\begin{cases}
0,&\tau<\tau^*,\\
b_p(e^{-b_{ep}(\tau-\tau^*)}+1),&\tau\ge\tau^*,
\end{cases}
\]
\[
\mu_B(\tau)=d_pe^{d_{ep}(\tau-L)},
\]
the invasion number factorizes as
\[
\mathcal R_P^\sharp(\tau^*,g,k)
=e^{-g\bar x\tau^*}Q(\tau^*,k),
\]
with
\[
Q(\tau^*,k)=
\int_0^\infty
\left[
k\bar x+b_p(e^{-b_{ep}s}+1)(1-e^{-\zeta\bar x})
\right]
e^{-h(\tau^*+s)-M_B(\tau^*+s)}\,ds,
\]
where
\[
h=\mu_Me^{-\rho\bar x},
\qquad
M_B(q)=\int_0^q\mu_B(v)\,dv.
\]
This \(Q\) is strictly decreasing in \(\tau^*\). Wherever \(Q>1\),
\[
g_c(\tau^*;k)
=
\frac{\log Q(\tau^*,k)}{\bar x\tau^*}
\]
is strictly decreasing in \(\tau^*\).

Thus the local predator-free invasion boundary is non-reentrant: increasing juvenile predation cannot restore predator invasibility, and in the sharp-maturation model increasing maturation age lowers the juvenile-predation threshold for extinction.

## Assumptions and scope
The prey equation is
\[
\dot x=x(r-ax+sy_1-by_2),
\]
and the predator equation is the source's McKendrick-type renewal equation with
\[
B(x,\tau)
=
kx\phi_A(\tau)+\tilde B(\tau)(1-e^{-\zeta x}),
\]
\[
\mu(x,\tau)
=
gx\phi_J(\tau)+\mu_B(\tau)+\mu_Me^{-\rho x}.
\]
All biological parameters appearing in denominators or mortality terms are positive, while \(g\ge0\) and \(k\ge0\). The source assumes bounded nonnegative fertility and positive mortality profiles sufficient for the renewal problem; the strictly positive hunger-mortality term
\[
\mu_Me^{-\rho\bar x}
\]
gives exponential tail control at the predator-free state.

The finite-smoothness statements hold for every \(\nu>0\). The explicit \(\tau^*\)-factorization is only for the exact sharp limit \(\nu=\infty\) together with the source's profiles from its numerical section. If a hard maximal age \(L\) is imposed in addition, the upper integration limit becomes \(L-\tau^*\); the shrinking domain only strengthens the strict decrease with \(\tau^*\).

The result is local at the predator-free equilibrium. It does not determine which coexistence attractor is reached after successful invasion, nor does it prove a global predator-extinction theorem for every initial condition.

## Proof
At \(u=0\), the prey equation reduces to
\[
\dot x=x(r-ax),
\]
so the positive prey-only state is \(\bar x=r/a\).

Write a perturbation as \((\xi,v)\). Because every derivative of \(B\) or \(\mu\) with respect to prey abundance is multiplied by the equilibrium predator density \(u=0\), the predator component of the linearization is autonomous:
\[
v_t+v_\tau=-\mu(\bar x,\tau)v,
\qquad
v(t,0)=\int_0^\infty B(\bar x,\tau)v(t,\tau)\,d\tau.
\]
The prey perturbation satisfies
\[
\dot\xi=-r\xi+
\bar x\left(
s\int_0^{\tau^*}v(t,\tau)\,d\tau
-b\int_{\tau^*}^\infty v(t,\tau)\,d\tau
\right),
\]
so the full linearization is triangular and contributes the stable prey eigenvalue \(-r\).

For an exponential predator mode
\[
v(t,\tau)=e^{\lambda t}q(\tau),
\]
the transport equation gives
\[
q(\tau)=q(0)S_g(\tau)e^{-\lambda\tau}.
\]
The renewal boundary condition is therefore
\[
1=
\int_0^\infty
B(\bar x,\tau)S_g(\tau)e^{-\lambda\tau}\,d\tau.
\]
At \(\lambda=0\), the right-hand side is exactly \(\mathcal R_P\).

If \(\mathcal R_P<1\) and \(\operatorname{Re}\lambda\ge0\), then
\[
\left|
\int_0^\infty
B(\bar x,\tau)S_g(\tau)e^{-\lambda\tau}\,d\tau
\right|
\le
\int_0^\infty
B(\bar x,\tau)S_g(\tau)\,d\tau
=
\mathcal R_P<1,
\]
so no characteristic root can lie in the closed right half-plane. The positive hunger-mortality term places the uncoupled transport spectrum strictly to the left. Standard renewal-equation linearized-stability theory then gives exponential stability.

If \(\mathcal R_P>1\), define for real \(\lambda\ge0\)
\[
K(\lambda)=
\int_0^\infty
B(\bar x,\tau)S_g(\tau)e^{-\lambda\tau}\,d\tau.
\]
It is continuous, strictly decreasing wherever reproduction occurs at positive ages, satisfies \(K(0)>1\), and tends to zero. Thus there is a unique positive real root of \(K(\lambda)=1\), proving instability. Equality \(\mathcal R_P=1\) gives \(\lambda=0\).

For the parameter monotonicity, define
\[
H(\tau)=\bar x\int_0^\tau\phi_J(s)\,ds.
\]
For every \(\tau>0\), \(H(\tau)>0\), and
\[
S_g(\tau)=S_0(\tau)e^{-gH(\tau)}.
\]
Therefore
\[
A'(g)=
-(1-e^{-\zeta\bar x})
\int_0^\infty
\tilde B(\tau)S_g(\tau)H(\tau)\,d\tau<0,
\]
and
\[
C'(g)=
-\int_0^\infty
\phi_A(\tau)S_g(\tau)H(\tau)\,d\tau<0.
\]
The strict signs follow from the source's positive adult reproduction and the positive smooth maturation weights.

Since
\[
\mathcal R_P=A+k\bar xC,
\]
it is affine and strictly increasing in \(k\). If \(A(g)<1\), the threshold
\[
k_c(g)=\frac{1-A(g)}{\bar xC(g)}
\]
is positive. For \(g_2>g_1\), the numerator strictly increases and the denominator strictly decreases, so
\[
k_c(g_2)>k_c(g_1).
\]

For fixed \(k\), the integrand defining \(\mathcal R_P\) decreases strictly in \(g\) at every positive age where reproduction occurs. Also
\[
S_0(\tau)\le e^{-h\tau},
\qquad
h=\mu_Me^{-\rho\bar x}>0,
\]
which gives an integrable dominating function. Dominated convergence yields
\[
\mathcal R_P(g,k)\to0
\]
as \(g\to\infty\). Hence a unique \(g_c(k)\) exists whenever \(\mathcal R_P(0,k)>1\).

For the sharp limit, juvenile mortality \(g\bar x\) acts exactly on the interval \([0,\tau^*)\), while reproduction starts at \(\tau^*\). Put \(\tau=\tau^*+s\). The source's explicit birth profile becomes independent of \(\tau^*\):
\[
k\bar x+b_p(e^{-b_{ep}s}+1)(1-e^{-\zeta\bar x}).
\]
Survival to age \(\tau^*+s\) is
\[
e^{-g\bar x\tau^*}
e^{-h(\tau^*+s)-M_B(\tau^*+s)}.
\]
This proves the factorization
\[
\mathcal R_P^\sharp=e^{-g\bar x\tau^*}Q.
\]
Differentiating the integrand of \(Q\) with respect to \(\tau^*\) multiplies it by
\[
-[h+\mu_B(\tau^*+s)]<0,
\]
so \(Q\) is strictly decreasing. On the region \(Q>1\), both \(\log Q\) decreases and the positive denominator \(\bar x\tau^*\) increases, hence
\[
g_c(\tau^*;k)=\frac{\log Q}{\bar x\tau^*}
\]
is strictly decreasing.

## Verification
The bundled script `verification/verify.py` evaluates representative admissible profiles using numerical quadrature. It verifies that the finite-smoothness reproduction number decreases strictly with \(g\), increases affinely with \(k\), that the inferred \(k_c(g)\) increases, and that the sharp-maturation formula agrees with direct integration and gives a decreasing \(g_c(\tau^*)\).

These computations are not used as proof. The threshold equation and monotonicity statements above are analytic.

## Relationship to prior work
Classical age-structured population theory already establishes the role of the low-density net reproductive rate in stability of the zero population. Cushing (1984) studies McKendrick equations using the inherent net reproductive rate and shows loss of stability at the replacement value one. That general threshold principle is used here and is not claimed as new.

Lu and Liu (2018) derive a predator net reproductive number for a different predator-prey system in which the prey, rather than the predator, is age structured, and prove global predator-free stability below threshold and predator persistence above threshold. This establishes that reproduction-number thresholds in structured predator-prey systems are prior art.

The new point is source-specific. Suarez et al. do not derive a predator-free invasion number for their role-reversal PDE/ODE system; instead, they classify predator extinction numerically and identify \(g\) and \(\tau^*\) as the dominant parameters. Their phase diagrams sample \(g\) on a grid and label predator-free cases after time integration. The exact decomposition
\[
\mathcal R_P=A(g)+k\bar xC(g),
\]
the strict one-way threshold in \(g\), the monotone \(k_c(g)\), and the sharp-maturation factorization
\[
\mathcal R_P^\sharp=e^{-g\bar x\tau^*}Q(\tau^*,k)
\]
do not appear in the inspected source or the two closest threshold references.

## Limitations
The result identifies the local invasion boundary at the predator-free equilibrium. It does not prove that every initial condition converges to that equilibrium when \(\mathcal R_P<1\), and it does not classify coexistence equilibrium or periodic-attractor stability when \(\mathcal R_P>1\).

The monotonicity in \(g\) and \(k\) is exact for every finite \(\nu>0\). The explicit monotonicity in \(\tau^*\) is proved only for the exact sharp-maturation limit with the source's numerical birth/death profiles. The source's finite \(\nu=100\) simulation is close to, but not identical with, that limit.

The result concerns the original unsaturated birth-rate model. The source also proposes a saturation modification; a fresh invasion calculation is required for that modified birth function.

## References
1. L. Suarez, M. K. Cameron, W. F. Fagan, D. Levy, “A predator-prey model with age-structured role reversal,” arXiv:2502.19748 (first public version 27 February 2025); Journal of Mathematical Biology 92 (2026), 73. DOI: 10.1007/s00285-026-02402-5.
2. J. M. Cushing, “Existence and stability of equilibria in age-structured population dynamics,” Journal of Mathematical Biology 20 (1984), 259–276. DOI: 10.1007/BF00275988.
3. Y. Lu, S. Liu, “Threshold dynamics of a predator-prey model with age-structured prey,” Advances in Difference Equations 2018 (2018), 164. DOI: 10.1186/s13662-018-1614-y.
