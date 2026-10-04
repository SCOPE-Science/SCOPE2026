# Vaccination monotonicity and an exact importation-amplification bound in an SEIR model

## Finding

Consider the susceptible–exposed–infectious subsystem
\[
\dot S=A_0-\theta(I)SE-(\mu+z)S,
\]
\[
\dot E=A_1+\theta(I)SE-\mu_1E,
\qquad
\dot I=\alpha E-\mu_2I,
\]
where
\[
\mu_1=\mu+\delta_1+\alpha+\omega_1,
\qquad
\mu_2=\mu+\delta_2+\omega_2.
\]
Assume \(A_1>0\), \(z\ge0\), all other rate parameters are positive, and \(\theta\) is positive, continuously differentiable, and nonincreasing.

Write
\[
I_{\mathrm{imp}}=\frac{\alpha A_1}{\mu_1\mu_2},
\qquad
R_{\mathrm{cl}}(z)=\frac{\theta(0)A_0}{(\mu+z)\mu_1}.
\]
For the unique endemic equilibrium of the model, \(I^*(z)\) is strictly decreasing in \(z\), satisfies
\[
I^*(z)>I_{\mathrm{imp}}
\]
for every finite \(z\), and converges to the importation floor
\[
\lim_{z\to\infty}I^*(z)=I_{\mathrm{imp}}.
\]
Likewise,
\[
E^*(z)>\frac{A_1}{\mu_1},
\qquad
E^*(z)\downarrow\frac{A_1}{\mu_1}.
\]

The exact fraction of equilibrium entries to the exposed class produced by local transmission is
\[
\ell^*(z):=\frac{\theta(I^*)S^*}{\mu_1}
=1-\frac{A_1}{\mu_1E^*}.
\]
It obeys the strict comparison
\[
0<\ell^*(z)<R_{\mathrm{cl}}(z).
\]
Therefore, whenever \(R_{\mathrm{cl}}(z)<1\),
\[
E^*(z)<\frac{A_1/\mu_1}{1-R_{\mathrm{cl}}(z)},
\qquad
I^*(z)<\frac{I_{\mathrm{imp}}}{1-R_{\mathrm{cl}}(z)}.
\]
Thus the quantity that is an elimination threshold when infected inflow is absent becomes, under continuing infected inflow, an explicit cap on equilibrium amplification above the imported-infection floor.

Finally, if \(\theta_{\mathrm{imp}}=\theta(I_{\mathrm{imp}})\), then
\[
I^*(z)=I_{\mathrm{imp}}+
\frac{\alpha A_0A_1\theta_{\mathrm{imp}}}
{\mu_1^2\mu_2(\mu+z)}+o(z^{-1}),
\]
and
\[
E^*(z)=\frac{A_1}{\mu_1}+
\frac{A_0A_1\theta_{\mathrm{imp}}}
{\mu_1^2(\mu+z)}+o(z^{-1}).
\]

## Assumptions and scope

The result concerns the model and equilibrium equations printed by Witbooi, Vyambwera, and Nsuami (2023), with a strictly positive inflow \(A_1\) into the exposed class. The function \(\theta\) may be constant or decreasing; only positivity, continuity, and monotonic nonincrease are used. The result is an equilibrium comparative-statics theorem. It does not assert eradication under infected inflow, global monotonicity of transient trajectories with respect to vaccination, or optimality of any time-dependent control.

The notation \(R_{\mathrm{cl}}(z)\) emphasizes that the source derives this reproduction quantity in the zero-inflow setting. For \(A_1>0\), there is no disease-free equilibrium, so it is used here only as a comparison quantity.

## Proof

At equilibrium, the printed model gives
\[
E^*=\frac{\mu_2}{\alpha}I^*,
\qquad
S^*=\frac{A_0}{\mu_0+\theta(I^*)E^*},
\qquad
\mu_0=\mu+z.
\]
The exposed balance is
\[
\mu_1E^*=A_1+\theta(I^*)S^*E^*.
\]
Because the local-transmission term is strictly positive, this immediately yields
\[
E^*>\frac{A_1}{\mu_1},
\qquad
I^*>I_{\mathrm{imp}}.
\]
It also gives the exact identity
\[
\ell^*=\frac{\theta(I^*)S^*}{\mu_1}
=1-\frac{A_1}{\mu_1E^*},
\]
so that
\[
E^*=\frac{A_1/\mu_1}{1-\ell^*},
\qquad
I^*=\frac{I_{\mathrm{imp}}}{1-\ell^*}.
\]

For monotonicity, the source's scalar endemic-equilibrium equation can be written
\[
\theta(I)=\mu_0H(I),
\]
where
\[
H(I)=
\frac{\alpha(\mu_1\mu_2 I-\alpha A_1)}
{\mu_2 I\,[\alpha(A_0+A_1)-\mu_1\mu_2I]}.
\]
On the biologically relevant interval
\[
I_{\mathrm{imp}}<I<\frac{\alpha(A_0+A_1)}{\mu_1\mu_2},
\]
the source's derivative calculation shows that \(H\) is strictly increasing from zero to infinity. Since \(\theta\) is nonincreasing, the equation has one intersection. Increasing \(z\) increases \(\mu_0\), hence increases the right-hand side strictly at each fixed interior \(I\); the unique intersection therefore moves strictly to the left. Thus \(I^*(z)\) is strictly decreasing.

The monotone family is bounded below by \(I_{\mathrm{imp}}\), so it has a limit \(L\ge I_{\mathrm{imp}}\). If \(L>I_{\mathrm{imp}}\), then \(H(L)>0\), while the equilibrium equation \(\theta(I^*)=\mu_0H(I^*)\) would have a right-hand side diverging as \(z\to\infty\), contradicting the finite positive limit \(\theta(L)\). Hence \(L=I_{\mathrm{imp}}\). The relation \(E^*=\mu_2I^*/\alpha\) gives the exposed-class limit.

For the amplification bound, the susceptible balance gives
\[
S^*=\frac{A_0}{\mu_0+\theta(I^*)E^*}<\frac{A_0}{\mu_0},
\]
and monotonicity of \(\theta\) gives \(\theta(I^*)\le\theta(0)\). Hence
\[
\ell^*=\frac{\theta(I^*)S^*}{\mu_1}
<\frac{\theta(0)A_0}{\mu_0\mu_1}
=R_{\mathrm{cl}}(z).
\]
Substitution into the exact formulas for \(E^*\) and \(I^*\) proves the stated upper bounds whenever \(R_{\mathrm{cl}}(z)<1\).

For the asymptotic expansion, the limits already proved imply
\[
(\mu+z)S^*\to A_0,
\qquad
\theta(I^*)\to\theta_{\mathrm{imp}},
\]
so
\[
(\mu+z)\ell^*\to\frac{A_0\theta_{\mathrm{imp}}}{\mu_1}.
\]
Using \(I^*=I_{\mathrm{imp}}/(1-\ell^*)\) and \(E^*=(A_1/\mu_1)/(1-\ell^*)\) gives the two first-order expansions.

## Verification

A standalone script replays the identities for the admissible test function
\[
\theta(I)=\frac{0.5}{1+0.7I}
\]
and the positive parameters
\[
A_0=10,\quad A_1=0.3,\quad \mu=0.1,\quad
\delta_1=0.02,\quad \alpha=0.4,\quad \omega_1=0.05,
\]
\[
\delta_2=0.03,\quad \omega_2=0.2.
\]
Here
\[
I_{\mathrm{imp}}\approx0.6379585327.
\]
The computed endemic infectious levels at vaccination rates \(z=10,100,1000\) are approximately
\[
1.1863380294,\quad0.6781814054,\quad0.6418422313,
\]
confirming the predicted decrease toward the floor. At \(z=100\), the comparison quantity is \(R_{\mathrm{cl}}\approx0.0876316666\), and the exact equilibrium satisfies the derived bound. The script also checks the equilibrium residuals, the identity for \(\ell^*\), and convergence of the scaled first-order excess to its analytic coefficient.

The numerical checks illustrate the theorem; they are not used to prove the all-parameter statement.

## Relationship to prior work

Witbooi, Vyambwera, and Nsuami (2023) prove existence and uniqueness of the endemic equilibrium for \(A_1>0\) and derive the scalar equation used above. Their analysis does not state monotonicity of the endemic equilibrium with respect to the vaccination rate, the exact local-transmission fraction identity as an amplification decomposition, the upper bound in terms of the closed-system reproduction quantity, or the large-vaccination asymptotic.

Witbooi (2021) studies a related SEIR model with infected immigration and proves positive lower threshold levels for infected classes; vaccination there is represented through recruitment of vaccinated newborns rather than the susceptible vaccination rate used in the 2023 model. Almarashi and McCluskey (2019) give a general perturbation theorem describing how a disease-free equilibrium moves when infected immigration is introduced, but do not analyze vaccination-rate comparative statics at fixed positive importation.

Sridevi and Reddy (2019) study optimal vaccination in a different SIR model with infected recruitment and saturated incidence. Duve et al. (2023) study vaccination and infected immigration in a malaria human–vector model and emphasize that positive infected influx removes the disease-free equilibrium. These works cover the broad qualitative interaction between vaccination and immigration but do not imply the source-specific monotonicity, amplification bound, or asymptotic coefficient proved here.

## Limitations

The theorem is tied to the structural assumptions of the source model, particularly a vaccination term acting on susceptibles and a contact function that is nonincreasing in symptomatic infection. It does not compare full transient trajectories under two vaccination rates, does not optimize vaccination cost, and does not account for vaccination of imported cases. The bound using \(R_{\mathrm{cl}}\) is informative only after that quantity is below one, although the monotonicity and floor statements hold for every finite \(z\ge0\).

## References

1. P. J. Witbooi, S. M. Vyambwera, M. U. Nsuami, “Control and elimination in an SEIR model for the disease dynamics of COVID-19 with vaccination,” AIMS Mathematics 8 (2023), 8144–8161. DOI: 10.3934/math.2023411.
2. P. J. Witbooi, “An SEIR model with infected immigrants and recovered emigrants,” Advances in Difference Equations 2021, article 337. DOI: 10.1186/s13662-021-03488-5.
3. R. M. Almarashi, C. C. McCluskey, “The effect of immigration of infectives on disease-free equilibria,” Journal of Mathematical Biology 79 (2019), 1015–1028. DOI: 10.1007/s00285-019-01387-8.
4. M. Sridevi, B. Ravindra Reddy, “Stability Analysis of an Epidemic Model with Infected Immigrants and Optimal Vaccination,” International Journal of Recent Technology and Engineering 8 (2019), 3071–3077. DOI: 10.35940/ijrte.B1566.078219.
5. P. Duve, S. Charles, J. Munyakazi, R. Lühken, P. Witbooi, “A mathematical model for malaria disease dynamics with vaccination and infected immigrants,” Mathematical Biosciences and Engineering 21 (2024), 1082–1109. DOI: 10.3934/mbe.2024045.
