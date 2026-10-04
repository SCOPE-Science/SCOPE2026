# The stochastic coalition model loses the probability cube and its claimed all-join equilibrium

## Finding

Lu, Xing, Xu, Li, and Li model three enterprises choosing whether to join a pollution-control coalition. Their deterministic variables
\[
x,\qquad y,\qquad z
\]
are strategy probabilities in \([0,1]\), and the original replicator equations contain the boundary factors
\[
x(1-x),\qquad y(1-y),\qquad z(1-z).
\]

Section 3 states that the nonnegative factors \(1-x\), \(1-y\), and \(1-z\) have no effect on equilibrium evolution and deletes them. For enterprise \(A\), the resulting stochastic equation is
\[
dX_t
=
X_t\left[
\pi r_A(Y_t+Z_t-Y_tZ_t)-\frac12ua^2
\right]dt
+\sigma X_t\,dW_t,
\]
with analogous equations for enterprises \(B\) and \(C\).

This modification destroys two structural properties required by the stated interpretation.

First, for every \(\sigma>0\), the only possible constant point equilibrium of the printed three-dimensional stochastic system is
\[
(0,0,0).
\]
Indeed, the diffusion vector is
\[
\sigma(X,Y,Z)^{\mathsf T},
\]
which vanishes only at the origin. Hence the paper's claimed stochastic equilibrium
\[
(1,1,1)
\]
cannot be a point equilibrium for any positive noise intensity, regardless of payoff parameters.

Second, the cube
\[
[0,1]^3
\]
is not forward invariant. On the invariant face
\[
Y_t=Z_t=0,
\]
the \(X\)-equation reduces exactly to
\[
dX_t=-k_A X_t\,dt+\sigma X_t\,dW_t,
\qquad
k_A=\frac12ua^2.
\]
Its solution is
\[
X_t=x_0
\exp\!\left[
\left(-k_A-\frac{\sigma^2}{2}\right)t+\sigma W_t
\right].
\]
For every \(x_0\in(0,1)\), every \(\sigma>0\), and every \(t>0\),
\[
\Pr(X_t>1)
=
1-\Phi\!\left(
\frac{\log(1/x_0)+(k_A+\sigma^2/2)t}
{\sigma\sqrt t}
\right)>0.
\]
Thus a variable introduced as a joining probability leaves the admissible interval with positive probability.

The loss of the all-join equilibrium is already visible without noise. The source's original enterprise-\(A\) replicator equation is
\[
\dot x=x(1-x)
\left[
\pi r_A(y+z-yz)-\frac12ua^2
\right].
\]
At \(x=1\), its drift is identically zero. After deleting \(1-x\), the drift at the all-join corner is instead
\[
\pi r_A-\frac12ua^2.
\]
For the paper's numerical joining parameters,
\[
\pi=30,\qquad r_A=\frac16,\qquad u=0.6,\qquad a=2,
\]
this is
\[
30\left(\frac16\right)-\frac12(0.6)(2^2)=3.8>0.
\]
Therefore \((1,1,1)\) is not even an equilibrium of the printed zero-noise system used as the basis for equations (3.4)–(3.6).

A probability-consistent stochastic perturbation must retain coefficients that vanish at both probability boundaries. One elementary repair target is
\[
dX_t
=
X_t(1-X_t)B_A(Y_t,Z_t)\,dt
+
\sigma X_t(1-X_t)\,dW_t,
\]
with corresponding equations for \(Y_t\) and \(Z_t\). This is a different stochastic model; its stability conditions must be derived anew rather than inherited from the printed system.

## Assumptions and scope

The claim concerns equations (2.4) and (3.1)–(3.6) as printed in the source and the source's stated interpretation of \(x,y,z\) as strategy probabilities.

A point equilibrium of an Itô stochastic differential equation means a constant solution. For a constant solution, both drift and diffusion coefficients must vanish at that point.

The exact escape calculation uses only the enterprise-\(A\) equation on the invariant face \(Y=Z=0\). It is therefore unaffected by the notation inconsistencies between the printed \(B,C\) cost coefficients in equations (3.2)–(3.3) and the coefficients used later in the paper.

No claim is made about unpublished simulation code. If code imposed clipping, projection, reflection, or restored the missing boundary factors, then it simulated a different stochastic system.

## Proof

Write
\[
B_A(y,z)
=
\pi r_A(y+z-yz)-\frac12ua^2.
\]
The printed enterprise-\(A\) stochastic equation is
\[
dX_t=X_tB_A(Y_t,Z_t)\,dt+\sigma X_t\,dW_t.
\]

For the full printed system, the diffusion coefficient driven by the common Brownian motion is the vector
\[
G(x,y,z)=\sigma(x,y,z)^{\mathsf T}.
\]
If \(p\) is a constant stochastic equilibrium, then the local martingale part of the constant process must vanish, so
\[
G(p)=0.
\]
When \(\sigma>0\), this forces
\[
p=(0,0,0).
\]
In particular,
\[
G(1,1,1)=\sigma(1,1,1)^{\mathsf T}\ne0,
\]
so \((1,1,1)\) cannot be a point equilibrium.

Next take
\[
Y_0=Z_0=0.
\]
Because both corresponding stochastic equations are multiplied by \(Y_t\) and \(Z_t\), pathwise uniqueness gives
\[
Y_t=Z_t=0
\]
for all \(t\). Hence
\[
dX_t
=
-\frac12ua^2X_t\,dt+\sigma X_t\,dW_t.
\]
Set
\[
k_A=\frac12ua^2.
\]
The unique strong solution is the geometric Brownian motion
\[
X_t=x_0
\exp\!\left[
\left(-k_A-\frac{\sigma^2}{2}\right)t+\sigma W_t
\right].
\]
The event \(X_t>1\) is equivalent to
\[
\frac{W_t}{\sqrt t}
>
\frac{\log(1/x_0)+(k_A+\sigma^2/2)t}
{\sigma\sqrt t}.
\]
Since \(W_t/\sqrt t\) is standard normal and the threshold is finite, its upper tail has strictly positive probability. This proves that \([0,1]^3\) is not invariant.

Finally, compare the deterministic equations. The original replicator equation has the factor \(x(1-x)\), so \(x=1\) is a boundary equilibrium for every value of the payoff bracket. The modified equation has only the factor \(x\), so at the all-join corner its enterprise-\(A\) drift equals
\[
B_A(1,1)=\pi r_A-\frac12ua^2.
\]
For the source's numerical parameters this equals \(3.8\), so deleting \(1-x\) changes the equilibrium set even before stochastic noise is added.

## Verification

The bundled script `verify.py` checks the source's enterprise-\(A\) arithmetic exactly:
\[
k_A=\frac65=1.2,
\qquad
B_A(1,1)=\frac{19}{5}=3.8.
\]

It also evaluates the exact lognormal escape formula at a source-listed noise intensity:
\[
x_0=0.8,\qquad
\sigma=2,\qquad
t=0.05,
\]
obtaining
\[
\Pr(X_t>1)\approx0.1957956707.
\]

The general noninvariance result is analytic and does not depend on this numerical example. The script also checks that the proposed boundary-vanishing repair has zero drift and diffusion coefficients at \(X=0\) and \(X=1\).

## Relationship to prior work

The primary source is Lu et al. (2024), DOI 10.3934/math.2024452. It explicitly states that \(x,y,z\) are strategy probabilities, derives the deterministic \(x(1-x)\), \(y(1-y)\), \(z(1-z)\) replicator equations, deletes the second boundary factors in Section 3, adds multiplicative terms \(\sigma x\,dW\), \(\sigma y\,dW\), \(\sigma z\,dW\), and later calls \((1,1,1)\) an exponentially stable equilibrium of the stochastic system.

Benaïm, Hofbauer, and Sandholm (2008), DOI 10.1080/17513750801915269, formulate stochastic replicator dynamics on the unit simplex and require both drift and diffusion directions to be tangent to the simplex; they state invariance of the simplex for those stochastic perturbations. This supplies a broader structural benchmark but does not analyze the 2024 pollution-control equations or identify the missing-boundary-factor error.

Liang, Cui, Zhou, and Ding (2022), DOI 10.1002/acs.3301, study stochastic stability for two-strategy replicator dynamics with multiplicative noise and delay. Their work is relevant stochastic evolutionary-game literature but does not imply the source-specific conclusions above.

Exact-title, DOI, equilibrium, probability-invariance, and multiplicative-noise searches located no published correction or erratum for the 2024 paper.

## Limitations

The result establishes a structural incompatibility in the published stochastic equations. It does not determine what equations were used in undocumented numerical code.

The example probability \(0.1957956707\) is an illustration of the exact escape formula, not an empirical probability for a real enterprise coalition.

The proposed boundary-vanishing equation is only a mathematically consistent repair target. Its stochastic stability, stationary behavior, and policy interpretation require a fresh analysis and are not asserted here.

## References

1. Z. Lu, L. Xing, R. Xu, M. Li, J. Li, “Stochastic evolution game analysis of the strategic coalition of enterprise pollution control,” AIMS Mathematics 9 (2024), 9287–9310. DOI: 10.3934/math.2024452.
2. M. Benaïm, J. Hofbauer, W. H. Sandholm, “Robust permanence and impermanence for stochastic replicator dynamics,” Journal of Biological Dynamics 2 (2008), 180–195. DOI: 10.1080/17513750801915269.
3. H. Liang, Y. Cui, Z. Zhou, B. Ding, “Two-strategy evolutionary games with stochastic adaptive control,” International Journal of Adaptive Control and Signal Processing 36 (2022), 251–263. DOI: 10.1002/acs.3301.
