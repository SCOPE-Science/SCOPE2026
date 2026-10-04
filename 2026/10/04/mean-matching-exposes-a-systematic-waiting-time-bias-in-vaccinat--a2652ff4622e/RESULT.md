# Mean matching exposes a systematic waiting-time bias in vaccination models

## Finding

Consider the vaccination mechanism used to contrast Models (2) and (3) of Colombo, Marcellini, and Rossi. Hold the post-vaccination infection pressure constant, so that every not-yet-immunized vaccinee faces a constant breakthrough hazard \(h>0\). Let \(T\) denote the time from vaccination to full immunization and assume
\[
T\ge 0,\qquad \mathbb E[T]=T_*>0,
\]
with \(T\) independent of an exponential infection clock of rate \(h\).

The exact probability that a vaccinee reaches immunization before breakthrough infection is
\[
P_{\mathrm{imm}}=\mathbb E[e^{-hT}].
\]
Since \(t\mapsto e^{-ht}\) is strictly convex,
\[
P_{\mathrm{imm}}\ge e^{-hT_*},
\]
with equality if and only if \(T=T_*\) almost surely. Hence, among all nonnegative immunization-time laws with the same mean, deterministic waiting is extremal: it minimizes successful immunization and maximizes breakthrough infection under a constant infection hazard.

The standard ODE vaccinated compartment in Model (2) has an exponential exit clock. The natural mean-matched calibration to the fixed immunization time in Model (3) is
\[
\vartheta_V=\frac1{T_*}.
\]
Write \(x=hT_*\). Then
\[
P_{\mathrm{imm}}^{\mathrm{exp}}=\frac1{1+x},
\qquad
P_{\mathrm{imm}}^{\mathrm{fix}}=e^{-x},
\]
and therefore, for every \(x>0\),
\[
P_{\mathrm{imm}}^{\mathrm{exp}}>P_{\mathrm{imm}}^{\mathrm{fix}}.
\]
The relative factor
\[
\frac{P_{\mathrm{imm}}^{\mathrm{exp}}}{P_{\mathrm{imm}}^{\mathrm{fix}}}
=\frac{e^x}{1+x}
\]
is strictly increasing for \(x>0\) and diverges as \(x\to\infty\).

With a constant vaccination inflow \(p_0>0\), the steady fluxes and waiting stocks are
\[
J_{\mathrm{exp}}=\frac{p_0}{1+x},\qquad
C_{\mathrm{exp}}=\frac{p_0x}{1+x},\qquad
V_{\mathrm{exp}}=\frac{p_0T_*}{1+x},
\]
for exponential waiting, and
\[
J_{\mathrm{fix}}=p_0e^{-x},\qquad
C_{\mathrm{fix}}=p_0(1-e^{-x}),\qquad
V_{\mathrm{fix}}=p_0T_*\frac{1-e^{-x}}x,
\]
for fixed waiting. Thus
\[
J_{\mathrm{exp}}>J_{\mathrm{fix}},\qquad
C_{\mathrm{exp}}<C_{\mathrm{fix}},\qquad
V_{\mathrm{exp}}<V_{\mathrm{fix}}
\]
whenever \(x>0\).

## Assumptions and scope

The comparison freezes the breakthrough hazard at a common constant \(h=\rho_V I>0\) and, for the steady-flow formulas, freezes vaccination inflow at \(p_0>0\). The vaccine protection parameter is taken constant over vaccination age. These assumptions isolate the waiting-time mechanism; they do not assert that the infection prevalence in the fully coupled ODE and transport systems is the same.

Model (3) corresponds to deterministic waiting \(T=T_*\). Model (2), when interpreted as an individual-level Markov compartment with exit rate \(\vartheta_V\), corresponds to exponential waiting of mean \(1/\vartheta_V\). Setting \(\vartheta_V=1/T_*\) therefore matches the mean time to immunization in the absence of breakthrough infection.

## Proof

Let \(E_h\) be an exponential random variable of rate \(h\), independent of \(T\). Conditional on \(T=t\), immunization precedes infection exactly when \(E_h>t\), so
\[
\Pr(E_h>T\mid T=t)=e^{-ht}.
\]
Averaging over \(T\) yields
\[
P_{\mathrm{imm}}=\mathbb E[e^{-hT}].
\]
Because \(e^{-ht}\) is strictly convex for \(h>0\), Jensen's inequality gives
\[
\mathbb E[e^{-hT}]\ge e^{-h\mathbb E[T]}=e^{-hT_*}.
\]
Strict convexity gives equality precisely when \(T\) is almost surely constant.

For exponential waiting with rate \(1/T_*\), competing exponential clocks give
\[
P_{\mathrm{imm}}^{\mathrm{exp}}
=\frac{1/T_*}{h+1/T_*}
=\frac1{1+x}.
\]
For deterministic waiting, survival against breakthrough infection through time \(T_*\) gives
\[
P_{\mathrm{imm}}^{\mathrm{fix}}=e^{-hT_*}=e^{-x}.
\]
The strict inequality follows from \(e^x>1+x\) for \(x>0\).

For a constant inflow \(p_0\), each entering vaccinee eventually exits either by immunization or infection. Thus the steady immunization and breakthrough fluxes are \(p_0P_{\mathrm{imm}}\) and \(p_0(1-P_{\mathrm{imm}})\). The mean residence time before either exit is
\[
\mathbb E[\min(T,E_h)]
=\int_0^\infty e^{-ht}\Pr(T>t)\,dt
=\frac{1-\mathbb E[e^{-hT}]}h.
\]
Multiplying by \(p_0\) gives the steady waiting stock. Substitution of the exponential and deterministic Laplace transforms produces the stated formulas.

Finally,
\[
\frac{d}{dx}\frac{e^x}{1+x}=\frac{xe^x}{(1+x)^2}>0,
\]
so the relative immunization overstatement is strictly increasing and unbounded.

## Verification

The bundled `verify.py` evaluates the formulas over a broad deterministic grid of positive \(x\), verifies all three strict inequalities, checks conservation of the two exit fluxes, and checks the analytic derivative sign of \(e^x/(1+x)\). It also evaluates several nondegenerate two-point waiting-time laws with mean \(T_*\) and confirms that their Laplace transforms strictly exceed the deterministic benchmark, as required by Jensen's inequality.

For example, at \(x=1\),
\[
P_{\mathrm{imm}}^{\mathrm{fix}}=e^{-1}\approx0.367879,
\qquad
P_{\mathrm{imm}}^{\mathrm{exp}}=\frac12,
\]
so mean-matched exponential waiting raises the successful-immunization fraction by about \(35.9\%\) relative to fixed waiting under the benchmark.

## Relationship to prior work

Colombo, Marcellini, and Rossi introduce the fixed-immunization-time transport formulation and explicitly contrast it with a standard vaccinated ODE compartment. They state that a direct comparison is highly arbitrary because the ODE exit parameter \(\vartheta_V\) has no counterpart in the transport model and the fixed time \(T_*\) has no analogue in the ODE. Matching the mean residence time by \(\vartheta_V=1/T_*\) provides a natural calibration, and the result above shows that this calibration still leaves a systematic directional discrepancy caused solely by the waiting-time distribution.

Liu, Takeuchi, and Iwami study the earlier SVIR compartmental model from which the ODE formulation is adapted. Their published abstract emphasizes both the time needed to obtain immunity and infection before immunity, but does not provide a fixed-versus-exponential same-mean comparison. Wang, Guo, and Liu study continuous vaccination-age structure and threshold dynamics in a different SVIR model; the available indexed material does not state the constant-hazard extremal comparison above.

The general fact that Markov compartments impose exponential waiting times is classical. The new point asserted here is source-specific: once the two vaccination mechanisms in the 2022 paper are put on the same mean-time scale, their constant-hazard discrepancy has a fixed sign, admits closed formulas, and extends to an extremal theorem over all mean-matched waiting-time laws.

## Limitations

The result is an exact benchmark for a frozen constant infection hazard and constant vaccination inflow. It does not order solutions, deaths, reproduction numbers, or optimal policies in the fully coupled epidemic models, where \(I(t)\), vaccination input, and vaccination-age-dependent susceptibility can vary with time. A later unindexed source could contain the same calibration argument.

## References

1. R. M. Colombo, F. Marcellini, E. Rossi, “Vaccination strategies through intra-compartmental dynamics,” Networks and Heterogeneous Media 17 (2022), 385–400. DOI: 10.3934/nhm.2022012.
2. X. Liu, Y. Takeuchi, S. Iwami, “SVIR epidemic models with vaccination strategies,” Journal of Theoretical Biology 253 (2008), 1–11. DOI: 10.1016/j.jtbi.2007.10.014.
3. J. Wang, M. Guo, S. Liu, “SVIR epidemic model with age structure in susceptibility, vaccination effects and relapse,” IMA Journal of Applied Mathematics 82 (2017), 945–970. DOI: 10.1093/imamat/hxx020.
