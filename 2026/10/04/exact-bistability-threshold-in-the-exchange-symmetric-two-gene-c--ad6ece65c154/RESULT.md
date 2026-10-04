# Exact bistability threshold in the exchange-symmetric two-gene competitive system
## Finding
Consider the exchange-symmetric specialization
\[
\alpha_{01}=\alpha_{02}=a_0>0,\qquad
\alpha_1=\alpha_2=a_1\ge 0,\qquad
\delta_1=\delta_2=d>0,
\]
\[
K_1=K_2=K>0,\qquad K_{12}=K_{21}=L>0
\]
of the two-gene competitive system
\[
\dot x_1=\frac{a_0+a_1x_1/K}{1+x_1/K+x_2/L}-dx_1,\qquad
\dot x_2=\frac{a_0+a_1x_2/K}{1+x_2/K+x_1/L}-dx_2.
\]
There are exactly three distinct equilibria in \(\mathbb R_{>0}^2\) if and only if
\[
a_1>dK,\qquad L<K,\qquad
\left(\frac{a_1}{d}-K\right)^2>
\frac{4a_0}{d(1/L-1/K)}.
\]
In that case Sontag's Theorem 1 applies: the two off-diagonal equilibria are asymptotically stable nodes, the diagonal equilibrium is a hyperbolic saddle, and every positive trajectory converges to one of the three equilibria. Thus the displayed inequalities are an exact parameter criterion for global bistability in the exchange-symmetric family.

Writing
\[
S=\frac{a_1}{d}-K,\qquad P=\frac{a_0}{d(1/L-1/K)},
\]
the two off-diagonal equilibria are \((x_-,x_+)\) and \((x_+,x_-)\), where
\[
x_\pm=\frac12\left(S\pm\sqrt{S^2-4P}\right).
\]
The diagonal equilibrium \((s,s)\) is always unique and is determined by
\[
d(1/K+1/L)s^2+(d-a_1/K)s-a_0=0.
\]
At the boundary \(S^2=4P\), with \(a_1>dK\) and \(L<K\), the two off-diagonal branches meet the diagonal branch at \(s=S/2\); there is then only one distinct positive equilibrium. Outside the strict three-equilibrium region there is likewise exactly one distinct positive equilibrium.

## Assumptions and scope
All parameters are real and satisfy \(a_0,d,K,L>0\) and \(a_1\ge0\). The result concerns the exchange-symmetric subfamily of the Hill-exponent-one competitive-promoter model in arXiv:2609.27270. It classifies distinct equilibria in the open positive quadrant and, in the strict three-equilibrium regime, inherits the global dynamical conclusions of that paper. It does not classify asymmetric parameter choices or stochastic switching.

The primary mathematical scope is dynamical systems (MSC 37), matching the source's primary arXiv classification math.DS.

## Proof
Clearing the positive denominators in the two equilibrium equations gives
\[
Ax_1^2+Bx_1x_2+Cx_1-a_0=0,
\]
\[
Ax_2^2+Bx_1x_2+Cx_2-a_0=0,
\]
where
\[
A=\frac dK>0,\qquad B=\frac dL>0,\qquad C=d-\frac{a_1}K.
\]
Subtracting the equations yields
\[
(x_1-x_2)\bigl(A(x_1+x_2)+C\bigr)=0.
\]
Hence every equilibrium is either diagonal or, if it is off diagonal, satisfies
\[
x_1+x_2=-\frac CA=\frac{a_1}d-K=:S.
\]

On the diagonal, \(x_1=x_2=s\), the equilibrium equation is
\[
(A+B)s^2+Cs-a_0=0.
\]
Its leading coefficient is positive and its constant term is negative, so it has exactly one positive root. Thus there is always exactly one positive diagonal equilibrium.

Now suppose \(x_1\ne x_2\). Put \(P=x_1x_2\). Since \(C=-AS\), the first cleared equilibrium equation becomes
\[
A(x_1^2-Sx_1)+BP-a_0=0.
\]
Because \(x_1^2-Sx_1=-x_1x_2=-P\), this is
\[
(B-A)P=a_0.
\]
A positive off-diagonal equilibrium therefore forces
\[
S>0,\qquad B-A>0,\qquad P=\frac{a_0}{B-A}>0.
\]
These conditions are respectively \(a_1>dK\), \(L<K\), and
\[
P=\frac{a_0}{d(1/L-1/K)}.
\]
The coordinates \(x_1,x_2\) must be the two roots of
\[
t^2-St+P=0.
\]
They are positive and distinct exactly when \(S>0\), \(P>0\), and \(S^2-4P>0\). This is precisely the criterion in the finding.

Conversely, assume the three strict inequalities. The quadratic \(t^2-St+P\) has two distinct positive roots \(x_-<x_+\). For either ordered pair \((x_-,x_+)\) or \((x_+,x_-)\), the identity \(x_i^2-Sx_i=-P\) and \((B-A)P=a_0\) show directly that both cleared equilibrium equations vanish. Together with the unique positive diagonal equilibrium, these are exactly three distinct positive equilibria. Sontag's Theorem 1 then gives the global bistable phase portrait.

If \(S^2=4P\) under \(S>0\) and \(P>0\), the two roots coincide at \(S/2\). Substitution into the diagonal equation gives zero because \((B-A)S^2/4=a_0\), so the collision point is the unique diagonal equilibrium. If any positivity condition fails, no positive off-diagonal pair can exist. Hence every parameter choice outside the strict region has exactly the unique diagonal positive equilibrium.

## Verification
The proof uses only the source's cleared quadratic equilibrium equations and elementary factorization. The converse was checked by substituting the reconstructed roots back into both cleared equations, not merely by counting roots of an elimination polynomial.

Two numerical checks reproduce the symmetric examples in arXiv:2609.27270. For \(a_0=0.1\), \(a_1=10\), \(d=K=1\), \(L=0.2\), the formulas give \(S=9\), \(P=0.025\), and \(x_-\approx0.00277864\), \(x_+\approx8.99722136\), matching the paper. For \(a_0=a_1=100\), \(d=K=1\), \(L=0.01\), they give \(x_-\approx0.01020409\), \(x_+\approx98.98979591\), again matching the reported values.

Boundary checks were also made explicitly: \(L=K\) makes \(B-A=0\), so an off-diagonal equilibrium would require \(a_0=0\), contrary to the hypotheses; \(a_1\le dK\) gives \(S\le0\), incompatible with two positive off-diagonal coordinates; and equality \(S^2=4P\) collapses the reflected pair to the diagonal point rather than creating two distinct equilibria.

## Relationship to prior work
Sontag, arXiv:2609.27270, proves the general one/two/three-equilibrium bound and the complete global phase portrait whenever three distinct positive equilibria exist. It gives two symmetric three-equilibrium examples and separately proves monostability of the much narrower symmetric exclusive-switch specialization \(K=L\) and \(a_0=a_1\). The paper does not state the displayed if-and-only-if parameter criterion for its full exchange-symmetric five-parameter family.

The older exclusive-switch literature concerns the equal-binding special case and emphasizes stochastic bistability without deterministic bistability for monomeric binding. That special case lies on \(L=K\), where the present criterion rules out off-diagonal positive equilibria identically. Standard cooperative toggle-switch models use different Hill-function equations and do not imply this criterion.

## Limitations
The result relies essentially on exchange symmetry. It does not supply a comparable closed parameter criterion for the fully asymmetric model, and it does not analyze stochastic stationary distributions. The equality surface is identified algebraically as a coalescence of the reflected steady states with the diagonal steady state; no separate local normal-form classification of that degeneracy is claimed.

## References
1. E. D. Sontag, “A note on bistability of a two-gene competitive system,” arXiv:2609.27270v2, 2026; first public version 2026-09-23.
2. A. Lipshtat, A. Loinger, N. Q. Balaban, and O. Biham, “Genetic toggle switch without cooperative binding,” Physical Review Letters 96 (2006), 188101.
3. A. Loinger, A. Lipshtat, N. Q. Balaban, and O. Biham, “Stochastic simulations of genetic switch systems,” Physical Review E 75 (2007), 021904.
