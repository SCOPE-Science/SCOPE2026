# A sharp recovered-vaccination threshold for subcritical endemic bistability

## Finding

The vaccinated-recovered compartment in the COVID-19 model of Ihsanjaya and Susyanto permits a sharp intervention threshold that is invisible to the disease-free reproduction number. For the parameter family specified below, the entire equilibrium diagram can be solved exactly. At one end of that family, there are two coexisting locally asymptotically stable states (disease-free and endemic) although
\[
\mathcal R_0=\frac{1067}{1080}<1.
\]
Vaccinating recovered individuals at rate \(\theta\) suppresses the two positive endemic equilibria at the exact threshold
\[
\boxed{\theta_c=\frac{127-4\sqrt{858}}{150}\approx0.0655563458199}.
\]
For \(0\le\theta<\theta_c\), exactly two distinct endemic equilibria exist; at equality, exactly one positive equilibrium corresponds to a double algebraic root; above it none exist. Throughout, the disease-free equilibrium exists and \(\mathcal R_0\) is unchanged.

At \(\theta=0\) the two endemic asymptomatic coordinates are exactly
\[
a_- = \frac{13}{375},\qquad a_+=\frac1{10}.
\]
The disease-free equilibrium and the large-endemic equilibrium are hyperbolic sinks, whereas the small-endemic equilibrium is a hyperbolic saddle with exactly one unstable eigenvalue. Consequently both extinction and endemic persistence have nonempty open local attraction basins for this fixed subthreshold reproduction number.

## Assumptions and scope

In the order \((S,V_s,E,A,I,H,R,V_R)\), the original deterministic ODEs are
\[
\begin{aligned}
\dot S&=\Lambda-\beta_1SA-(v+\mu)S,\\
\dot V_s&=vS-\beta_2V_s A-\mu V_s,\\
\dot E&=A(\beta_1 S+\beta_2 V_s+\beta_3 R+\beta_4 V_R)-(\gamma+\mu)E,\\
\dot A&=\gamma(1-\omega)E-(\alpha_1+\alpha_2+\mu)A,\\
\dot I&=\gamma\omega E+\alpha_2 A-(\delta_1+\delta_2+\mu+d_1)I,\\
\dot H&=\delta_1 I-(\sigma+\mu+d_2)H,\\
\dot R&=\alpha_1 A+\delta_2 I+\sigma H-\beta_3RA-(\mu+\theta)R,\\
\dot V_R&=\theta R-\beta_4V_RA-\mu V_R.
\end{aligned}
\]
All parameters are positive except that the policy rate \(\theta\) is allowed to vanish, and \(0<\omega<1\). Set
\[
\Lambda=\frac{1067}{90},\quad
\mu=v=\beta_1=\beta_2=\beta_4=\alpha_2=\delta_1=\delta_2=d_1=d_2=\sigma=1,
\quad \gamma=\alpha_1=2,\quad \omega=\frac12,\quad \beta_3=5,
\]
and vary only \(\theta\ge0\).

The distinction \(\beta_4=1<\beta_3=5\) models lower reinfection contact susceptibility after vaccinating a recovered person. The equal values \(\beta_1=\beta_2=1\) isolate the intervention's effect in the recovered population; these rates are mathematical examples, not estimated epidemiological parameters. The theorem concerns nonnegative equilibria and the exact local linear spectrum at \(\theta=0\), not a global basin classification.

## Proof

**1. Reproduction number.** At the disease-free equilibrium the population is
\[
(S_0,V_{s,0},0,0,0,0,0,0),\qquad S_0=V_{s,0}=\frac\Lambda2.
\]
Only asymptomatic individuals create new infections, and the relevant exposed-to-asymptomatic progression is \(\gamma(1-\omega)=1\) while exposed and asymptomatic removal rates are \(3\) and \(4\). The next-generation reproduction number is therefore
\[
\mathcal R_0=\frac{S_0+V_{s,0}}{3\cdot4}
=\frac\Lambda{12}=\frac{1067}{1080}<1.
\]
Because both recovered classes vanish at this equilibrium, \(\theta\) does not appear in this expression.

**2. Complete reduction of equilibria.** Write \(a=A\). If \(a=0\), then successively \(E=I=H=R=V_R=0\), and the unique disease-free state follows. For \(a>0\), solving seven of the eight stationary equations gives uniquely
\[
\begin{aligned}
S(a)&=\frac\Lambda{2+a},
&V_s(a)&=\frac\Lambda{(2+a)(1+a)},\\
E(a)&=4a,
&I(a)&=\frac54a,\\
H(a)&=\frac5{12}a,
&R(a,\theta)&=\frac{11a}{3(1+\theta+5a)},\\
&&V_R(a,\theta)&=\frac{\theta R(a,\theta)}{1+a}.
\end{aligned}
\]
All these coordinates, except possibly \(V_R\) when \(\theta=0\), are strictly positive. (The term “endemic” means the infected coordinates \(E,A,I,H\) are positive; \(V_R=0\) is allowed for a zero vaccination policy.) The remaining stationary condition \(\dot E=0\) is
\[
\frac{\Lambda}{1+a}
+\frac{11a}{3(1+\theta+5a)}
\left(5+\frac\theta{1+a}\right)=12.
\]
Every denominator is positive for \(a>0\), \(\theta\ge0\). Clearing them gives the **equivalent** quadratic equation
\[
P_\theta(a)=3750a^2+(750\theta-505)a+13(1+\theta)=0.
\]
Thus no hidden equilibria arise from clearing denominators or from missing zero-infection branches.

**3. Sharp vaccination threshold.** The discriminant is
\[
\Delta(\theta)
=25\left(22500\theta^2-38100\theta+2401\right).
\]
Its zeros are
\[
\theta_-=\frac{127-4\sqrt{858}}{150},
\qquad
\theta_+=\frac{127+4\sqrt{858}}{150}.
\]
They satisfy
\[
0<\theta_-<\frac{101}{150}<\theta_+.
\]
For \(0\le\theta<\theta_-\), the discriminant is positive, the sum of the roots \((505-750\theta)/3750\) is positive, and their product \(13(1+\theta)/3750\) is positive: both roots are positive. At \(\theta=\theta_-\), the sole distinct positive root is
\[
a_c=\frac{505-750\theta_-}{7500}
=\frac{2\sqrt{858}-13}{750}>0.
\]
For \(\theta_-<\theta<\theta_+\), the roots are nonreal. At and beyond \(\theta_+\), their sum is negative and their product positive, so there is no positive root, including the repeated negative root at \(\theta_+\). Thus \(\theta_c=\theta_-\) yields the stated complete equilibrium diagram. At \(\theta=0\), factorization gives
\[
P_0(a)=3750\left(a-\frac{13}{375}\right)\left(a-\frac1{10}\right).
\]

**4. Full-dimensional linear stability.** Compute the Jacobian directly from the eight ODEs in the displayed compartment order, and write \(\chi(\lambda)=\det(\lambda I-J)\). At the disease-free equilibrium when \(\theta=0\), exact elimination gives
\[
\chi_{\mathrm{DFE}}(\lambda)
=(\lambda+1)^3(\lambda+2)(\lambda+3)(\lambda+4)
\left(\lambda^2+7\lambda+\frac{13}{90}\right).
\]
All factors are Hurwitz: in particular both coefficients of the last quadratic are positive. Therefore the disease-free equilibrium is a hyperbolic sink.

At the smaller endemic state \(a_-=13/375\), the *exact* degree-eight characteristic polynomial is
\[
\begin{aligned}
\chi_-(\lambda)=&\frac{(\lambda+4)(375\lambda+388)(375\lambda+763)}{7910156250}\\
&\quad\cdot\left(
56250\lambda^5+686700\lambda^4+2491538\lambda^3
+3289455\lambda^2+1411090\lambda-15925\right).
\end{aligned}
\]
The three linear factors are strictly stable. The real quintic has one positive real root by Descartes' rule of signs and has **exactly one** root in the open right half-plane by the rational Routh array (first-column signs \(+,+,+,+,+,-\)); its remaining roots have negative real parts, because the strict Routh calculation contains no zero pivots or imaginary-axis roots. Thus this endemic equilibrium is a hyperbolic saddle of unstable dimension one.

At the larger endemic state \(a_+=1/10\),
\[
\begin{aligned}
\chi_+(\lambda)=&\frac{(\lambda+4)(10\lambda+11)(10\lambda+21)}{18000}\\
&\quad\cdot\left(
180\lambda^5+2268\lambda^4+8757\lambda^3+12832\lambda^2+6274\lambda+147\right).
\end{aligned}
\]
All three linear factors are strictly stable, and the exact rational Routh first column for the quintic has signs \(+,+,+,+,+,+\). Hence every eigenvalue has negative real part, so this larger equilibrium is a hyperbolic sink. Hyperbolic sink stability gives an open attraction neighborhood for each of the two sinks, establishing genuine local bistability at \(\mathcal R_0<1\).

## Verification

The self-contained bundled `verify.py` uses only standard-library rational arithmetic. It reconstructs each source ODE and its exact Jacobian, verifies all eight stationarity equations at the disease-free and two endemic states, recomputes the full degree-eight characteristic polynomial using Faddeev–LeVerrier's formula, tests the displayed factorizations, and builds an exact Routh table without floating-point decisions. Output includes `VERIFY_OK` and exact unstable-root counts \(0,1,0\) for the three \(\theta=0\) equilibria. An additional \(\theta=1\) disease-free check establishes the source equations and stability there. The algebraic discriminant is derived symbolically in the proof; numerical evaluation of \(\theta_c\) is illustrative only.

## Relationship to prior work

Ihsanjaya and Susyanto introduce the eight-compartment reinfection/vaccination model and calculate its disease-free reproduction number; their Theorem 2 lists the disease-free equilibrium without a positive-endemic classification, whereas simulations depict persistent infection. The present result solves the complete positive-equilibrium count along one mathematically explicit recovered-vaccination intervention family and determines the local eight-dimensional spectral type of all three \(\theta=0\) equilibria.

Backward bifurcation, reinfection-driven subthreshold coexistence, and multiple endemic equilibria are well-known **general phenomena** and are not claimed here as new. Song's 2021 full-text study provides a broad reinfection-number framework and analyzes different epidemic models. Wang and collaborators' SEIRE reinfection preprint likewise addresses backward bifurcation in a distinct model, but only its accessible abstract was examined. An especially close 2024 paper by Alzaid and Alkahtani reproduces the *same eight ODEs* before converting them to a fractional-order system; inspection of its full text shows its mathematical focus is solution existence/uniqueness and its numerical focus is fractional-order trajectories and data fits, not the exact recovered-vaccination endemic-equilibrium fold or local spectra.

The closest prior result concerning the **same 2023 source** examines susceptible-vaccination monotonicity of \(\mathcal R_0\) and numerical parameter consistency, not recovered-vaccination variation of endemic equilibrium count or local bistability. Searches for alternate names, source DOI, reinfection bifurcation, root multiplicity, and equivalent vaccination-policy statements found no published record specifically implying the result here. This is a source-specific, not a universal, novelty claim.

## Limitations

All numerical parameters are deliberately rational structural witnesses, not fitted rates. The result classifies equilibria for one exact parameter family, not every parameter set of the original model. Its local-spectral assertions are made at \(\theta=0\), not at all values of \(\theta\). The double algebraic root at \(\theta_c\) is not claimed here to establish a fully verified nonlinear normal form or any global bifurcation theorem. Absence of endemic equilibria above threshold does **not** establish global convergence to the disease-free equilibrium: non-equilibrium recurrent attractors have not been excluded. General backward bifurcation and reinfection mechanisms have extensive prior literature; unindexed or inaccessible equivalent source-specific results remain possible.

## References

1. M. M. M. Ihsanjaya and N. Susyanto, “A mathematical model for policy of vaccinating recovered people in controlling the spread of COVID-19 outbreak,” *AIMS Mathematics* **8** (2023), 14508–14521, DOI: 10.3934/math.2023741. First published 19 April 2023.
2. S. S. Alzaid and B. S. T. Alkahtani, “Real-world validation of fractional-order model for COVID-19 vaccination impact,” *AIMS Mathematics* **9** (2024), 3685–3706, DOI: 10.3934/math.2024181.
3. B. Song, “Basic reinfection number and backward bifurcation,” *Mathematical Biosciences and Engineering* **18** (2021), 8064–8083, DOI: 10.3934/mbe.2021400.
4. S. Wang et al., “Backward bifurcation, basic reinfection number and robustness of a SEIRE epidemic model with reinfection,” arXiv:2205.07258 (2022). Only the abstract was inspected.
