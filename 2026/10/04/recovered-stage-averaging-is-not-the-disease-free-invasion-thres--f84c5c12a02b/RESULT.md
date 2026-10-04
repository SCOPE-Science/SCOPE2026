# Recovered-stage averaging is not the disease-free invasion threshold in the seasonal SIRn model
## Finding
The seasonal SIRn model has one infectious compartment and \(n\) recovered compartments whose susceptibilities increase after infection. The article's Eq. (19) defines a time-dependent quantity by uniformly averaging the susceptible transmission rate \(\beta(t)\) and the recovered-stage rates \(\beta_k(t)\). That class average is not the disease-free invasion quantity.

At the disease-free state used by the case study,
\[
S=N,\qquad I=R_1=\cdots=R_n=0,
\]
the exact first-order infectious equation is
\[
\dot i=\bigl[\beta(t)-(\gamma+\mu)\bigr]i.
\]
Hence the recovered-stage susceptibilities do not enter disease-free invasion at first order. For the article's sinusoidal forcing
\[
\beta(t)=\frac{\beta_0}{2}\left[1+\cos\left(\frac{2\pi}{T}t-\phi_0\right)\right],
\]
the one-period infectious Floquet multiplier is
\[
M=\exp\left(\int_0^T[\beta(t)-(\gamma+\mu)]\,dt\right)
 =\exp\left(T\left[\frac{\beta_0}{2}-(\gamma+\mu)\right]\right).
\]
Therefore the disease-free infection direction is stable for \(\beta_0<2(\gamma+\mu)\), neutral at equality, and unstable for \(\beta_0>2(\gamma+\mu)\). This threshold is independent of \(n\), the partition of time since recovery, and the recovered-stage susceptibility profile.

## Assumptions and scope
The statement concerns the published deterministic seasonal SIRn equations and the case-study setting with constant total population, where the paper takes \(\lambda=\mu\). The disease-free state is the fully susceptible state \(S=N\) with all infected and recovered compartments zero. The claim is local and concerns invasion in the infectious direction. It does not assert global extinction or persistence, uniqueness of nontrivial periodic solutions, or validity of any particular convention for assigning a scalar periodic reproduction number away from the threshold property.

The source defines
\[
\beta_k(t)=s(\tau_k)\beta(t).
\]
Its Eq. (19) therefore equals
\[
\mathcal R_{\mathrm{printed}}(t)
=\frac{c_s\beta(t)}{\gamma+\mu},\qquad
c_s=\frac{1+\sum_{k=1}^n s(\tau_k)}{n+1}.
\]
For the stated susceptibility profiles, \(c_s<1\). The appearance of \(c_s\) is incompatible with disease-free linearization because every \(R_k\) is zero there.

## Proof
The infectious equation in the article is
\[
\dot I=\beta(t)\frac{SI}{N}+\sum_{k=1}^n\beta_k(t)\frac{R_k I}{N}-(\gamma+\mu)I.
\]
Linearize at \(S=N\), \(I=0\), and \(R_k=0\). The derivative of the susceptible infection term with respect to \(I\) is \(\beta(t)S/N=\beta(t)\). For each recovered stage, \(R_k I\) is a product of two perturbation variables. Its derivative with respect to \(I\) is proportional to \(R_k=0\), and its derivative with respect to \(R_k\) is proportional to \(I=0\). Thus all recovered-stage infection terms vanish from the Jacobian. The recovery and mortality terms contribute \(-(\gamma+\mu)i\), proving
\[
\dot i=[\beta(t)-(\gamma+\mu)]i.
\]

The scalar linear equation has the exact solution
\[
i(t)=i(0)\exp\left(\int_0^t[\beta(u)-(\gamma+\mu)]\,du\right).
\]
Over one forcing period, the cosine integrates to zero, so
\[
\int_0^T\beta(u)\,du=\frac{\beta_0T}{2}.
\]
This gives the multiplier \(M\) displayed above. Since \(M<1\), \(M=1\), and \(M>1\) exactly when \(\beta_0<2(\gamma+\mu)\), equality holds, and \(\beta_0>2(\gamma+\mu)\), respectively, the threshold follows.

For the article's case study, \(\gamma=1\) week\(^-1\) and \(\mu=1.622\times10^-4\) week\(^-1\), so
\[
\beta_{0,c}=2(1+1.622\times10^-4)=2.0003244.
\]
The article reports fitted amplitudes around \(2.25\), \(2.18\), and \(2.14\), all strictly above this threshold.

## Verification
The accompanying `verify.py` recomputes the threshold, checks that the reported rounded fitted amplitudes all produce positive one-period infection exponents, and evaluates the class-average factors implied by the three published susceptibility profiles over the stated 520-stage weekly partition. Those factors are approximately \(0.8005\), \(0.8353\), and \(0.8723\), confirming that Eq. (19) scales the disease-free transmission term by recovered-state information that is absent from the disease-free Jacobian.

The critical proof step is analytic rather than numerical: the products \(R_k I\) have zero first derivative at \(R_k=I=0\). The numerical checks only reproduce source-specific constants and do not substitute for that linearization.

## Relationship to prior work
The motivating article states Eq. (19) as its basic reproduction number and cites Ma and Ma's seasonally forced epidemic threshold work together with a seasonal-influenza calibration paper. Ma and Ma analyze threshold conditions by time-averaging time-varying parameters in appropriate seasonal models; they do not prescribe a uniform average across epidemiological compartments. More general periodic-epidemic literature likewise defines threshold quantities through the linearized infection process or next-generation operator. Those general results are consistent with the scalar Floquet calculation above.

The new point here is the source-specific comparison: applying the article's own equations at its disease-free state shows that its recovered-stage arithmetic average is not the invasion quantity and yields the exact corrected threshold for its sinusoidal case study. Searches by exact title, DOI, Eq. (19) language, reproduction-number aliases, and correction/erratum terms did not locate a published correction making this comparison.

## Limitations
The result does not say that the fitted trajectories are numerically incorrect, because Eq. (19) is presented as an interpretation after calibration rather than as the equation used to generate the trajectories. It does not prove global dynamics or a nonlinear persistence theorem. It also does not claim that every convention for a periodic basic reproduction number must numerically equal the Floquet multiplier; the proved invariant statement is the exact disease-free linear equation and its stability threshold.

The published case-study equation following the general seasonal formula contains a typographical omission of the time variable inside the cosine, while the general Eq. (4) and the surrounding description clearly specify the intended periodic forcing. The present claim uses that stated general periodic formula and does not rely on the case-study typographical line.

## References
Andreu-Vilarroig C, González-Parra G, Villanueva RJ. *Mathematical Modeling of Influenza Dynamics: Integrating Seasonality and Gradual Waning Immunity*. Bulletin of Mathematical Biology 87, 75 (2025). DOI: 10.1007/s11538-025-01454-w. PMCID: PMC12084257.

Ma J, Ma Z. *Epidemic threshold conditions for seasonally forced SEIR models*. Mathematical Biosciences and Engineering 3(1), 161–172 (2006). DOI: 10.3934/mbe.2006.3.161.

Wesley CL, Allen LJS. *The basic reproduction number in epidemic models with periodic demographics*. Journal of Biological Dynamics 3(2–3), 116–129 (2009). DOI: 10.1080/17513750802304893.
