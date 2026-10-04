# Exact prey-invasion threshold and the hidden saddle branch in a herd predator-prey model

## Finding

Consider the model
\[
\dot N=rN\left(1-\frac NK\right)-\frac{a\Phi(N,\alpha)P}{1+bN^{\alpha+q}+cP},
\qquad
\dot P=sP\left(1-\frac PH\right)+\frac{ea\Phi(N,\alpha)P}{1+bN^{\alpha+q}+cP},
\]
with
\[
\Phi(N,\alpha)=\frac{N}{1+N^{1-\alpha}},
\qquad
\frac12\le\alpha<1,
\qquad
q\in\{0,1\},
\]
and positive \(a,b,c,e,r,s,K,H\).

Every coexistence equilibrium is exactly parameterized by a prey coordinate \(N\in(0,K)\). Its predator coordinate is
\[
P_+(N)=\frac H2\left(1+\sqrt{1+\frac{4er}{sKH}N(K-N)}\right),
\]
and the corresponding attack rate is
\[
A(N)=r\left(1-\frac NK\right)
\frac{(1+N^{1-\alpha})(1+bN^{\alpha+q}+cP_+(N))}{P_+(N)}.
\]

Consequently, a coexistence branch can meet the predator-only equilibrium \((0,H)\) only at
\[
a_*=\lim_{N\downarrow0}A(N)=cr+\frac rH.
\]
This is exactly the parameter value at which the prey-invasion eigenvalue at \((0,H)\),
\[
\lambda_N=r-\frac{aH}{1+cH},
\]
vanishes.

The local coexistence branch lies on the \(a>a_*\) side and is a saddle. Let
\[
\delta=1-\alpha.
\]
Then
\[
A(N)=a_*\left(1+C N^\delta+o(N^\delta)\right),
\]
where
\[
C=
\begin{cases}
1+\dfrac{b}{1+cH},&(\alpha,q)=\left(\dfrac12,0\right),\\
1,&\text{otherwise}.
\end{cases}
\]
Moreover,
\[
\det J=-rsC\delta N^\delta+o(N^\delta)<0
\]
along that branch for all sufficiently small \(N>0\).

For the paper's parameter set
\[
b=0.3,\quad c=0.5,\quad e=0.6,\quad r=0.4,\quad s=0.3,\quad
K=40,\quad H=50,\quad \alpha=\frac12,\quad q=1,
\]
the exact collision threshold is
\[
a_*=0.208.
\]
Hence the numerically reported transition near \(a\approx1.08834\) cannot be a transcritical collision between coexistence and \((0,H)\): any such collision must occur at \(a=0.208\).

At the paper's own value \(a=0.8\), the exact branch equation has two coexistence equilibria:
\[
(N,P)\approx(8.3358197853,54.8152125587)
\]
and
\[
(N,P)\approx(32.0797287675,54.6492858751).
\]
The first has negative determinant and is a saddle; the second has positive determinant and negative trace and is locally asymptotically stable.

## Assumptions and scope

The result concerns the two-population model printed in Acotto and Venturino (2024), with the parameter restrictions stated above. It concerns equilibrium geometry and local stability only. No claim is made about global basin sizes, uniqueness of a fold for arbitrary parameters, or the exact dynamical event represented by every trajectory-based numerical transition in the paper.

## Proof

At a coexistence equilibrium, multiply the prey equation by \(e\) and add the predator equation. The interaction terms cancel, giving
\[
\frac{er}K N^2+\frac sH P^2-erN-sP=0.
\]
For \(0<N<K\), this is a quadratic in \(P\):
\[
P^2-HP+\frac{erH}{sK}N(N-K)=0.
\]
Its constant term is negative, so the two roots have opposite signs. The unique positive root is \(P_+(N)\) displayed above.

Conversely, divide the prey equilibrium equation by \(N>0\), substitute
\[
\frac{\Phi(N,\alpha)}N=\frac1{1+N^{1-\alpha}},
\]
and solve for \(a\). This gives exactly \(a=A(N)\). Thus \(N\mapsto(P_+(N),A(N))\) parameterizes every positive equilibrium.

Since
\[
P_+(N)=H+\frac{er}sN+O(N^2)
\]
as \(N\downarrow0\), direct substitution gives
\[
\lim_{N\downarrow0}A(N)
=r\frac{1+cH}H
=cr+\frac rH.
\]
The Jacobian at the predator-only equilibrium \((0,H)\) is triangular in the prey-invasion direction and has eigenvalues
\[
\lambda_N=r-\frac{aH}{1+cH},
\qquad
\lambda_P=-s.
\]
Hence the only possible boundary collision value is \(a=a_*\).

For the branch direction, write \(\delta=1-\alpha\). Because
\[
P_+(N)=H+O(N),
\]
the factors involving \(P_+\) and \(1-N/K\) contribute only \(O(N)\). Since \(0<\delta\le1/2\) and \(lpha+q\ge1/2\), the dominant correction is \(N^\delta\), except when \((\alpha,q)=(1/2,0)\), where the \(bN^{\alpha+q}\) term occurs at the same order. This yields the stated coefficient \(C>0\), so \(A(N)>a_*\) for all sufficiently small \(N>0\).

To determine the local type, write the vector field as
\[
\dot N=Nf(N,P,a),
\qquad
\dot P=Pg(N,P,a).
\]
At an interior equilibrium,
\[
J=
\begin{pmatrix}
Nf_N&Nf_P\\
Pg_N&Pg_P
\end{pmatrix}.
\]
Along the small-\(N\) branch,
\[
f_N=rC\delta N^{\delta-1}+o(N^{\delta-1}),
\qquad
g_P=-\frac sH+o(1),
\]
while \(f_P\) and \(g_N\) remain bounded. Therefore
\[
\det J
=NP(f_Ng_P-f_Pg_N)
=-rsC\delta N^\delta+o(N^\delta)<0.
\]
The branch is therefore a saddle branch.

## Verification

The bundled script reconstructs \(P_+(N)\), \(A(N)\), the full Jacobian, and the source parameter set. It checks \(a_*=0.208\), confirms that \(A(N)>a_*\) for a sequence of small positive \(N\), solves \(A(N)=0.8\) by bisection in two disjoint intervals, evaluates the original equilibrium residuals, and verifies the local stability signs.

The two roots at \(a=0.8\) are approximately
\[
N_1=8.3358197853,\qquad P_1=54.8152125587,
\]
and
\[
N_2=32.0797287675,\qquad P_2=54.6492858751.
\]
The first has \(\det J<0\); the second has \(\det J>0\) and \(\operatorname{tr}J<0\).

## Relationship to prior work

Acotto and Venturino (2024), DOI 10.3934/math.2024831, introduce the exact model studied here. They derive the same ellipse relation after canceling the interaction terms and state that the predator-only equilibrium is stable exactly when \(a>cr+r/H\). They nevertheless describe a trajectory transition near \(a\approx1.08834\), for their reference parameters, as a transcritical bifurcation between coexistence and the predator-only equilibrium, even though \(cr+r/H=0.208\) for those parameters. The exact branch parameterization above resolves the discrepancy: the predator-only collision threshold is fixed by the boundary eigenvalue and cannot depend on initial conditions.

The 2023 predecessor by the same authors, DOI 10.1002/mma.9262, uses a different herd-response interaction. Its relevant boundary equilibrium is structurally different and does not supply this regularized branch asymptotic or the exact \(a_*\) collision argument for the 2024 Beddington-DeAngelis model.

A published finding on stability exchange at boundary collisions in a different predator-dependent replicator model gives a related determinant-sign principle, but it concerns different equations and parameters and does not imply the present exact parameterization or threshold.

## Limitations

The theorem proves the exact boundary collision value and the existence and saddle character of the one-sided local branch. It does not prove that \(A(N)\) has only one interior turning point for every admissible parameter set. It also does not identify every trajectory-based numerical transition in the source; it only proves that a transition near \(a\approx1.08834\) cannot be a transcritical collision with \((0,H)\).

## References

1. F. Acotto, E. Venturino, “How do predator interference, prey herding and their possible retaliation affect prey-predator coexistence?”, AIMS Mathematics 9 (2024), 17122–17145. DOI: 10.3934/math.2024831.
2. F. Acotto, E. Venturino, “Modeling the herd prey response to individualistic predators attacks”, Mathematical Methods in the Applied Sciences 46 (2023), 13436–13456. DOI: 10.1002/mma.9262.
