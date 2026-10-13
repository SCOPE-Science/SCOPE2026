# Exact common-mobility threshold for a hostile-boundary SIS model

## Finding

Consider the mass-action SIS reaction-diffusion model
\[
S_t-d_S\Delta S=\Lambda(x)-\beta(x)SI+\gamma(x)I,
\]
\[
I_t-d_I\Delta I=\beta(x)SI-\gamma(x)I,
\]
with homogeneous Dirichlet boundary conditions on a bounded smooth domain \(\Omega\). Restrict the two movement rates to the common-mobility ray
\[
d_S=d_I=d>0.
\]

Let \(\Psi\) be the unique positive solution of
\[
-\Delta\Psi=\Lambda(x),
\qquad
\Psi|_{\partial\Omega}=0.
\]
The disease-free susceptible profile is then
\[
\widetilde S_d=\frac{\Psi}{d}.
\]
Substitution into the source's variational reproduction number gives
\[
\mathcal R_0(d)=
\sup_{\phi\in H_0^1(\Omega)\setminus\{0\}}
\frac{\int_\Omega \beta\Psi\phi^2\,dx}
{d^2\int_\Omega |\nabla\phi|^2\,dx+d\int_\Omega\gamma\phi^2\,dx}.
\]

For each nonzero \(\phi\), define
\[
A_\phi=\int_\Omega|\nabla\phi|^2\,dx,
\qquad
B_\phi=\int_\Omega\gamma\phi^2\,dx,
\qquad
C_\phi=\int_\Omega\beta\Psi\phi^2\,dx.
\]
Because \(\phi\in H_0^1(\Omega)\setminus\{0\}\), one has \(A_\phi>0\), and positivity of \(\beta\), \(\gamma\), and \(\Psi\) gives \(B_\phi,C_\phi>0\). Let
\[
r_\phi=
\frac{-B_\phi+\sqrt{B_\phi^2+4A_\phi C_\phi}}{2A_\phi},
\]
the unique positive solution of
\[
r^2A_\phi+rB_\phi=C_\phi.
\]
Then the exact common-mobility threshold is
\[
\boxed{
 d_c=\sup_{\phi\ne0}r_\phi
}.
\]
It satisfies
\[
0<d<d_c\iff\mathcal R_0(d)>1,
\]
\[
d=d_c\iff\mathcal R_0(d)=1,
\]
and
\[
d>d_c\iff\mathcal R_0(d)<1.
\]

Consequently, the source's equal-diffusion global-attractivity theorem becomes a complete mobility classification:

- for \(0<d<d_c\), the unique endemic equilibrium is globally attractive;
- for \(d=d_c\), the disease-free equilibrium is globally attractive;
- for \(d>d_c\), the disease-free equilibrium is globally attractive.

There is therefore exactly one common-mobility eradication threshold.

A useful quantitative strengthening is
\[
\mathcal R_0(d_2)
\le
\frac{d_1}{d_2}\mathcal R_0(d_1)
\qquad
(0<d_1<d_2),
\]
so \(\mathcal R_0(d)\) is strictly decreasing.

Finally, if \(\lambda_1\) is the first Dirichlet eigenvalue, \(\gamma_m\) is the minimum of \(\gamma\), and \(M\) is the maximum of \(\beta\Psi\), then
\[
d_c\le
\frac{-\gamma_m+\sqrt{\gamma_m^2+4\lambda_1M}}{2\lambda_1}.
\]
Every nonzero test function supplies the certified lower bound
\[
d_c\ge r_\phi.
\]

## Assumptions and scope

The coefficients \(\Lambda\), \(\beta\), and \(\gamma\) satisfy the positivity and regularity hypotheses of the source, and \(\Omega\) is the bounded smooth domain used there. The claim is restricted to equal susceptible and infected diffusion,
\[
d_S=d_I=d.
\]

The source's theorem proves global attractivity, so that is the dynamical conclusion used here. No stronger convergence rate or nonlinear stability assertion is added at the critical value.

The formula \(d_c\) is an exact variational characterization. It need not have an elementary closed form for heterogeneous coefficients.

## Proof

On the common-mobility ray, the disease-free profile solves
\[
-d\Delta\widetilde S_d=\Lambda,
\qquad
\widetilde S_d|_{\partial\Omega}=0.
\]
Hence
\[
\widetilde S_d=\frac{\Psi}{d}.
\]
The source defines
\[
\mathcal R_0
=
\sup_{\phi\ne0}
\frac{\int_\Omega\beta\widetilde S_d\phi^2\,dx}
{\int_\Omega(d|\nabla\phi|^2+\gamma\phi^2)\,dx}.
\]
Multiplying numerator and denominator by \(d\) yields the displayed formula for \(\mathcal R_0(d)\).

For fixed \(\phi\), the inequality
\[
\frac{C_\phi}{d^2A_\phi+dB_\phi}>1
\]
is equivalent to
\[
d<r_\phi.
\]
Therefore, if \(d<d_c\), the definition of the supremum gives a test function with \(r_\phi>d\), and hence \(\mathcal R_0(d)>1\).

If \(d>d_c\), then \(r_\phi\le d_c\) for every \(\phi\). Since
\[
C_\phi=r_\phi^2A_\phi+r_\phi B_\phi,
\]
one obtains
\[
C_\phi
\le
d_c^2A_\phi+d_cB_\phi
\le
\frac{d_c}{d}
\left(d^2A_\phi+dB_\phi\right).
\]
Thus
\[
\mathcal R_0(d)\le\frac{d_c}{d}<1.
\]

At \(d=d_c\), the same inequality gives \(\mathcal R_0(d_c)\le1\). Conversely, take a sequence of test functions with
\[
r_{\phi_j}\to d_c.
\]
Because \(r_{\phi_j}\le d_c\),
\[
\frac{C_{\phi_j}}
{d_c^2A_{\phi_j}+d_cB_{\phi_j}}
\ge
\left(\frac{r_{\phi_j}}{d_c}\right)^2.
\]
The right side tends to one, so
\[
\mathcal R_0(d_c)\ge1.
\]
Therefore
\[
\mathcal R_0(d_c)=1.
\]

For monotonicity, if \(d_2>d_1>0\), then
\[
d_2^2A_\phi+d_2B_\phi
\ge
\frac{d_2}{d_1}
\left(d_1^2A_\phi+d_1B_\phi\right).
\]
Taking suprema gives
\[
\mathcal R_0(d_2)
\le
\frac{d_1}{d_2}\mathcal R_0(d_1),
\]
which is strict because \(\mathcal R_0(d_1)>0\).

To see that \(d_c\) is finite, normalize \(\phi\) by \(\int_\Omega\phi^2=1\). The Poincaré inequality and coefficient bounds give
\[
A_\phi\ge\lambda_1,
\qquad
B_\phi\ge\gamma_m,
\qquad
C_\phi\le M.
\]
Thus every \(r_\phi\) is at most the positive root of
\[
\lambda_1d^2+\gamma_md=M,
\]
which is the displayed upper bound. Positivity of \(d_c\) follows from any nonzero test function.

The source proves that when \(d_S=d_I\), the disease-free equilibrium is globally attractive for \(\mathcal R_0\le1\) and the endemic equilibrium is globally attractive for \(\mathcal R_0>1\). Substitution of the exact threshold classification completes the dynamical statement.

## Verification

The accompanying checker verifies the algebraic threshold identities for a collection of exact rational triples \((A,B,C)\), checks the comparison inequalities used at \(d=d_c\), and verifies the monotonicity scaling inequality.

These finite algebra checks do not substitute for the variational proof. No numerical discretization of the PDE is used as evidence for the universal claim.

## Relationship to prior work

Deng's 2024 mass-action paper defines the reproduction number variationally, proves existence and uniqueness of the endemic equilibrium for \(\mathcal R_0>1\), and proves global attractivity of the disease-free or endemic equilibrium in the special equal-diffusion case. It also proves separate large-diffusion extinction statements. It does not state an exact critical value when both diffusion coefficients are increased together.

An earlier paper by Deng on a Dirichlet SIS model studies asymptotic endemic profiles under small and large diffusion. Huang, Han, and Liu established threshold dynamics for related Dirichlet SIS models. These works motivate movement as a disease-control parameter, but the searches and inspected statements did not yield the common-mobility variational threshold above for this mass-action source model.

The formula is not a new abstract spectral theorem. It is the source-specific consequence of the fact that on the equal-diffusion ray the disease-free susceptible profile itself scales as \(d^{-1}\), while the infected dispersal cost contributes another factor of \(d\). This produces the quadratic denominator
\[
d^2A_\phi+dB_\phi
\]
and permits an exact one-parameter global phase boundary.

## Limitations

The exact threshold applies to the common-mobility ray. If \(d_S\) and \(d_I\) vary independently, the threshold is a two-parameter surface rather than the scalar \(d_c\).

The theorem gives global attractivity because that is the level proved by the source for equal diffusion; it does not add a critical convergence rate.

The literature search cannot rule out an equivalent variational rearrangement under substantially different terminology. The result should therefore be read as a source-specific exact classification, not as a claim that the underlying Rayleigh-quotient technique is new.

## References

1. K. Deng, “Asymptotic behavior of a diffusive SIS epidemic model with mass action infection mechanism,” Discrete and Continuous Dynamical Systems - B 29 (2024), 3677–3689. DOI: 10.3934/dcdsb.2024019.
2. K. Deng, “Asymptotic profiles of the steady state for a diffusive SIS epidemic model with Dirichlet boundary conditions,” Communications on Pure and Applied Analysis 23 (2024), 80–87. DOI: 10.3934/cpaa.2023129.
3. W. Huang, M. Han, K. Liu, “Dynamics of an SIS reaction-diffusion epidemic model for disease transmission,” Mathematical Biosciences and Engineering 7 (2010), 51–66. DOI: 10.3934/mbe.2010.7.51.
