# Exact heightwise size-bias law for stationary Shimizu–Morioka dynamics
## Finding
Consider the standard Shimizu–Morioka system
\[
\dot x=y,\qquad
\dot y=x-\lambda y-xz,\qquad
\dot z=x^2-\alpha z,
\]
with
\[
\alpha>0,\qquad \lambda>0.
\]

Every compactly supported invariant probability measure \(\mu\) is supported in
\[
z\ge0.
\]
Moreover, an invariant support point with
\[
z=0
\]
can only be the origin.

The stationary law sharpens from an integrated moment relation to the exact heightwise identity
\[
\mathbb E_\mu[x^2\mid z]=\alpha z.
\]
Equivalently, for every Borel set \(B\subseteq[0,\infty)\),
\[
\int_{\{z\in B\}}x^2\,d\mu
=
\alpha\int_{\{z\in B\}}z\,d\mu.
\]

If \(\mu\ne\delta_{(0,0,0)}\), then
\[
\mathbb E_\mu[z]>0
\]
and the probability measure obtained by weighting \(\mu\) with \(x^2\) has \(z\)-marginal equal to the size-biased \(z\)-marginal of \(\mu\):
\[
\frac{x^2\,d\mu}{\mathbb E_\mu[x^2]}
\ \xrightarrow{\ z\ }\ 
\frac{z\,d\mu_z}{\mathbb E_\mu[z]}.
\]
Here \(\mu_z\) denotes the \(z\)-marginal.

In particular, for every integer \(k\ge0\),
\[
\mathbb E_\mu[x^2z^k]
=
\alpha\,\mathbb E_\mu[z^{k+1}].
\]
Thus all mixed moments with one factor \(x^2\) and an arbitrary power of height are fixed by the height marginal alone.

## Assumptions and scope
The measure \(\mu\) is a Borel probability measure invariant under the polynomial flow and supported on a compact subset of \(\mathbb R^3\). Compact support guarantees integrability of every test function used below and ensures that every point in the support lies on a bounded complete trajectory.

The normalization is
\[
\dot z=x^2-\alpha z.
\]
Another common normalization writes the last equation as
\[
\dot z=-\alpha(z-x^2).
\]
The two forms differ by a constant rescaling of the \(x\)- and \(y\)-coordinates. The present form is the one used explicitly in later global-dynamics and integrability treatments.

The earliest verified public source date for the Shimizu–Morioka simple model is 31 March 1980.

## Proof
Let
\[
(x(t),y(t),z(t))
\]
be a bounded complete trajectory in the support. The last equation has the variation-of-constants formula
\[
z(t)
=
e^{-\alpha(t-s)}z(s)
+
\int_s^t e^{-\alpha(t-u)}x(u)^2\,du.
\]
Letting
\[
s\to-\infty
\]
and using boundedness gives
\[
z(t)
=
\int_{-\infty}^t e^{-\alpha(t-u)}x(u)^2\,du
\ge0.
\]
Hence every compact invariant support is contained in \(z\ge0\).

If \(z(t_0)=0\), the nonnegative integral above vanishes. Therefore
\[
x(u)=0
\]
for every \(u\le t_0\). Then
\[
y(u)=\dot x(u)=0
\]
there as well. At \(t_0\) the state is the origin, and uniqueness of the polynomial differential equation makes the entire trajectory the equilibrium at the origin. This proves the support statement.

Now let \(\varphi\) be any continuous function on the compact \(z\)-range of the support. Choose a continuously differentiable antiderivative \(H\) with
\[
H'(z)=\varphi(z).
\]
For the generator \(L\),
\[
LH
=
\varphi(z)(x^2-\alpha z).
\]
Invariance gives
\[
0
=
\int LH\,d\mu
=
\int \varphi(z)(x^2-\alpha z)\,d\mu.
\]
Because this holds for every continuous \(\varphi\) on the compact \(z\)-range,
\[
\mathbb E_\mu[x^2-\alpha z\mid z]=0.
\]
Therefore
\[
\mathbb E_\mu[x^2\mid z]=\alpha z
\]
almost surely.

Approximating indicators of Borel subsets of the compact \(z\)-range by bounded measurable test functions gives the equivalent localized identity
\[
\int_{\{z\in B\}}x^2\,d\mu
=
\alpha\int_{\{z\in B\}}z\,d\mu.
\]

Taking \(B=[0,\infty)\) gives
\[
\mathbb E_\mu[x^2]=\alpha\mathbb E_\mu[z].
\]
If the latter mean were zero, nonnegativity of \(z\) would force \(z=0\) almost surely, and the support result would force \(\mu=\delta_{(0,0,0)}\). Hence every other invariant measure has positive mean height.

For such a measure, divide the localized identity by
\[
\mathbb E_\mu[x^2]
=
\alpha\mathbb E_\mu[z].
\]
This proves the exact size-bias statement. Taking
\[
\varphi(z)=z^k
\]
gives the complete moment hierarchy
\[
\mathbb E_\mu[x^2z^k]
=
\alpha\mathbb E_\mu[z^{k+1}]
\]
for every integer \(k\ge0\).

## Verification
The accompanying checker uses exact sparse-polynomial arithmetic over rational coefficients.

It verifies the generator identities
\[
Lz=x^2-\alpha z,
\qquad
L\left(\frac{x^2}{2}\right)=xy,
\]
and
\[
L(xy)
=
y^2+x^2(1-z)-\lambda xy.
\]

It also verifies that the equilibrium constraints
\[
y=0,\qquad z=1,\qquad x^2=\alpha
\]
annihilate the vector field, together with the origin equilibrium.

The stored checker output is `VERIFY_OK`.

The checker verifies the algebraic premises. The heightwise conclusion uses arbitrary one-variable test functions and conditional expectation; the support positivity uses the exact variation-of-constants formula on bounded complete trajectories. Neither conclusion is inferred from a finite numerical experiment.

## Relationship to prior work
Shimizu and Morioka introduced the simple Lorenz-like model in 1980 and used perturbation theory to study the bifurcation of a symmetric limit cycle to asymmetric cycles.

Tigan and Turaev later studied the same model in a coordinate-scaled normalization. Their full analysis establishes a homoclinic butterfly in a parameter subfamily and explicitly identifies the three equilibria in the scaled coordinates. It also proves that a distinguished unstable separatrix crosses a surface with height greater than the nonzero-equilibrium height. That orbit-specific result does not give a conditional law for arbitrary invariant probability measures.

Messias, Gouveia, and Pessoa use the standard normalization
\[
\dot z=x^2-\alpha z
\]
and give a global description at infinity together with equilibrium and heteroclinic information. Their analysis addresses phase-space geometry rather than stationary disintegration by height.

Huang, Shi, and Li show that for nonzero \(\alpha\) the Shimizu–Morioka system is linearly related to a special Rucklidge system and study integrability and nonintegrability. This equivalence is important for prior-work comparison: existing balance results in the Rucklidge form already imply integrated stationary moment identities after scaling. Those integrated identities are therefore not claimed as new here.

The present statement is the stricter heightwise refinement:
\[
\mathbb E[x^2\mid z]=\alpha z.
\]
It identifies the complete \(x^2\)-weighted height distribution, not only its total mass or finitely many integrated moments.

## Limitations
The result concerns compactly supported invariant probability measures. It does not prove existence of a Lorenz attractor for any particular parameter pair, classify unbounded trajectories, or determine the full joint invariant distribution.

The heightwise law is a necessary stationary identity, not a uniqueness theorem for invariant measures.

A published balance theorem for the linearly equivalent Rucklidge form already covers certain integrated stationary moments and recurrence barriers. The novelty claim is restricted to the conditional heightwise law, its localized Borel-set formulation, and the resulting exact size-bias interpretation.

A differently phrased or non-indexed conditional-disintegration statement could remain unlocated. The complete text of the 2020 integrability paper was not securely available in the inspected lawful sources; its accessible abstract and bibliographic record establish the scaling relation and integrability scope, and this remains a specific residual literature risk.

## References
1. T. Shimizu and N. Morioka, “On the bifurcation of a symmetric limit cycle to an asymmetric one in a simple model,” Physics Letters A 76, 201–204 (1980), DOI 10.1016/0375-9601(80)90466-1.
2. G. Tigan and D. Turaev, “Analytical search for homoclinic bifurcations in the Shimizu-Morioka model,” Physica D 240, 985–989 (2011), DOI 10.1016/j.physd.2011.02.013.
3. M. Messias, M. R. A. Gouveia, and C. Pessoa, “Dynamics at infinity and other global dynamical aspects of Shimizu–Morioka equations,” Nonlinear Dynamics 69, 577–587 (2012), DOI 10.1007/s11071-011-0288-8.
4. K. Huang, S. Shi, and W. Li, “Integrability analysis of the Shimizu–Morioka system,” Communications in Nonlinear Science and Numerical Simulation 84, 105101 (2020), DOI 10.1016/j.cnsns.2019.105101.
5. I. I. Ovsyannikov and D. V. Turaev, “Analytic proof of the existence of the Lorenz attractor in the extended Lorenz model,” arXiv:1508.07565.
