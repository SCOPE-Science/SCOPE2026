# A sharp infection-decay floor in an unconditionally stable NSFD SIR scheme

## Finding

For the SIR model of Suryanto and Darti, put
\[
c=\mu+\gamma+\delta,\qquad
\mathcal R_0=\frac{\Lambda\beta}{(\mu+\nu)c},
\]
and assume
\[
0<\mathcal R_0<1.
\]
At the disease-free equilibrium the exact continuous infected multiplier over a physical interval \(h\) is
\[
q(h)=e^{-c(1-\mathcal R_0)h}.
\]

For the paper's nonlocal update, any finite positive denominator value \(\phi\) gives the infected multiplier
\[
\lambda(\phi)
=
\frac{1+c\mathcal R_0\phi}{1+c\phi}
=
\mathcal R_0+\frac{1-\mathcal R_0}{1+c\phi}.
\]
Therefore
\[
\mathcal R_0<\lambda(\phi)<1.
\]

Define
\[
h_*=
\frac{-\log\mathcal R_0}{c(1-\mathcal R_0)}.
\]
For every
\[
h\ge h_*,
\]
\[
q(h)\le\mathcal R_0<\lambda(\phi),
\]
so no positive denominator within the published update architecture can exactly match the continuous disease-free infection multiplier.

For the source choice
\[
\phi(h)=\frac{e^{\mu h}-1}{\mu},
\]
\[
\lambda(h)\to\mathcal R_0
\]
as \(h\to\infty\). Hence the physical-time decay rate
\[
\rho_{\rm NSFD}(h)
=
-\frac1h\log\lambda(h)
\]
obeys
\[
\rho_{\rm NSFD}(h)\to0,
\qquad
h\rho_{\rm NSFD}(h)\to-\log\mathcal R_0.
\]
The continuous decay rate remains
\[
c(1-\mathcal R_0)>0.
\]

For the exact positive parameter choice
\[
\mu=1,\quad \nu=1,\quad \gamma=1,\quad \delta=1,\quad
\Lambda=2,\quad \beta=\frac32,\quad \alpha=\frac1{10},
\]
one has
\[
c=3,\qquad \mathcal R_0=\frac12.
\]
At
\[
h=\log2,
\]
the source denominator is
\[
\phi=1,
\]
so
\[
\lambda=\frac58.
\]
The continuous multiplier is
\[
q=\frac1{2\sqrt2},
\]
and therefore
\[
q<\frac12<\frac58.
\]
The corresponding decay rates are
\[
\frac32
\]
for the continuous infected mode and
\[
\frac{\log(8/5)}{\log2}
\approx0.6780719051
\]
for the NSFD mode.

## Assumptions and scope

All model parameters are positive and
\[
0<\mathcal R_0<1.
\]
The hard-floor theorem concerns the disease-free infected linear mode and retains the source's nonlocal update form while allowing any finite positive denominator.

The conclusion does not dispute positivity, boundedness, equilibrium preservation, local stability type, or global convergence proved by the source. It concerns physical-time relaxation-rate fidelity.

## Proof

At the disease-free equilibrium,
\[
S_0=\frac{\Lambda}{\mu+\nu}.
\]
The continuous infected equation linearizes to
\[
I'
=
(\beta S_0-c)I
=
-c(1-\mathcal R_0)I.
\]
Thus
\[
q(h)=e^{-c(1-\mathcal R_0)h}.
\]

The source update has
\[
I_{n+1}
=
\frac{I_n+\phi\Psi_nS_{n+1}}{1+c\phi},
\qquad
\Psi_n=\frac{\beta I_n}{1+\alpha I_n}.
\]
At the disease-free equilibrium,
\[
\Psi_n'=\beta
\]
and \(S_{n+1}=S_0\) at zeroth order in the infected perturbation, giving
\[
\lambda(\phi)
=
\frac{1+\phi\beta S_0}{1+c\phi}
=
\frac{1+c\mathcal R_0\phi}{1+c\phi}.
\]
Hence
\[
\lambda(\phi)-\mathcal R_0
=
\frac{1-\mathcal R_0}{1+c\phi}>0
\]
and
\[
1-\lambda(\phi)
=
\frac{c\phi(1-\mathcal R_0)}{1+c\phi}>0.
\]

The exact continuous multiplier reaches the floor when
\[
e^{-c(1-\mathcal R_0)h}=\mathcal R_0,
\]
which is exactly
\[
h=h_*.
\]
This proves the sharp exact-matching obstruction.

For
\[
\phi(h)=\frac{e^{\mu h}-1}{\mu},
\]
one has \(\phi(h)\to\infty\), and therefore
\[
\lambda(h)\to\mathcal R_0.
\]
Since
\[
h\rho_{\rm NSFD}(h)=-\log\lambda(h),
\]
the large-step claims follow.

As \(h\downarrow0\),
\[
\phi(h)=h+O(h^2),
\]
so
\[
\lambda(h)
=
1-c(1-\mathcal R_0)h+O(h^2),
\]
and therefore
\[
\rho_{\rm NSFD}(h)
=
c(1-\mathcal R_0)+O(h).
\]

## Verification

The bundled `verify.py` symbolically checks the multiplier identity, the floor, the crossover formula, the small-step limit, and the large-step limits.

For the exact witness it verifies
\[
\mathcal R_0=\frac12,\qquad
h_*=\frac{2\log2}{3},\qquad
h=\log2>h_*,
\]
\[
\phi=1,\qquad
\lambda=\frac58,\qquad
q=\frac1{2\sqrt2},
\]
with
\[
q<\mathcal R_0<\lambda.
\]

No finite experiment is used to establish the structural theorem.

## Relationship to prior work

Suryanto and Darti construct the nonlocal NSFD scheme, use
\[
\phi(h)=\frac{e^{\mu h}-1}{\mu},
\]
and prove positivity, boundedness, equilibrium preservation, and the same local and global stability classification as the continuous model for all step sizes.

Broader NSFD literature uses elementary stability in the qualitative sense that equilibria and their linear stability properties are preserved for arbitrary step size. This is compatible with the present result: preserving whether a multiplier lies inside the unit disk does not require matching the continuous semigroup multiplier or physical decay exponent.

The new content is the source-specific sharp quantitative boundary. Every positive denominator in the source update has multiplier strictly above \(\mathcal R_0\); once \(h\ge h_*\), the exact continuous multiplier lies at or below that floor. With the source's exponential denominator, the per-unit-time decay rate tends to zero for large steps.

Searches by source identity, decay-rate terminology, eigenvalue-floor language, large-step physical-time decay, and elementary-stability terminology did not locate this source-specific obstruction.

## Limitations

The result is local to the disease-free infected mode and does not quantify nonlinear transient error far from the disease-free equilibrium.

The floor is an obstruction for the source's update architecture with a finite positive denominator. A different discretization architecture can have different rate properties.

The source's qualitative dynamic-consistency results remain intact.

## References

1. A. Suryanto, I. Darti, “On the nonstandard numerical discretization of SIR epidemic model with a saturated incidence rate and vaccination,” AIMS Mathematics 6 (2021), 141–155. DOI: 10.3934/math.2021010.
2. M. M. Khalsaraei et al., “Nonstandard Finite Difference Schemes for an SIR Epidemic Model,” Mathematics 9 (2021), 3082. DOI: 10.3390/math9233082.
