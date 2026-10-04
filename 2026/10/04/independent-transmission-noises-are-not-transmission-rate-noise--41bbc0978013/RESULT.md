# Independent transmission noises are not transmission-rate noise
## Finding
Parkinson and Roy formulate a controlled stochastic SIR system with independent Brownian motions in the susceptible and infected equations. In their numerical experiments they set
\[
\sigma_S=-\sigma_I=q,\qquad q=\sqrt{0.02}(1-\alpha)SI,
\]
and state that this choice is meant to represent uncertainty in the infection rate. For every state with \(q\neq0\), this independent-noise model is not the stochastic model obtained by randomizing the transmission rate.

A stochastic replacement
\[
\beta\mapsto\beta+\sigma_\beta\dot W
\]
in the deterministic transmission flux requires a *single* Brownian driver in the two transfer equations:
\[
dS=F_S\,dt-q\,dW,\qquad dI=F_I\,dt+q\,dW,
\]
where \(q=(1-\alpha)\sigma_\beta SI\). Its diffusion covariance is
\[
a_{\mathrm{tr}}=q^2
\begin{pmatrix}
1&-1\\
-1&1
\end{pmatrix}.
\]
By contrast, the published independent drivers with amplitudes of opposite sign have
\[
a_{\mathrm{ind}}=q^2
\begin{pmatrix}
1&0\\
0&1
\end{pmatrix}.
\]
Consequently, the Fokker--Planck diffusion operator for genuine transmission-rate noise is
\[
\frac12(\partial_S-\partial_I)^2(q^2f)
=\frac12\partial_{SS}(q^2f)-\partial_{SI}(q^2f)+\frac12\partial_{II}(q^2f),
\]
whereas the published equation contains only the two diagonal second derivatives. The missing mixed term is therefore structural, not a sign convention.

The same distinction is visible without writing the density equation. Genuine transmission-rate noise is an internal susceptible-to-infected transfer, so its stochastic increment cancels exactly in \(S+I\). With independent drivers, the stochastic increment in \(S+I\) is \(q(dW_1-dW_2)\), whose quadratic-variation rate is \(2q^2\). Thus the published simulation model injects stochastic variation into \(S+I\) that a random transmission rate cannot create.

## Assumptions and scope
The claim concerns the two-dimensional susceptible-infected SDE and its associated Fokker--Planck equation in Parkinson and Roy, together with their numerical choice \(\sigma_S=-\sigma_I=\sqrt{0.02}(1-\alpha)SI\). It applies on the interior where \(q\neq0\); at states where \(q=0\), the two diffusion tensors agree trivially.

No claim is made that independent compartment noise is mathematically invalid. It defines a different stochastic model. The claim is specifically that it is not equivalent to uncertainty in the single transmission-rate parameter \(\beta\), and therefore the reported Fokker--Planck simulations do not have that stated interpretation. Boundary modeling and the separate deterministic control-coordinate notation are outside the claim.

## Proof
Write the deterministic transmission contribution to the susceptible-infected drift as
\[
(1-\alpha)\beta SI(-1,1)^T.
\]
If \(\beta\) is perturbed by scalar Itô white noise of intensity \(\sigma_\beta\), the diffusion vector is
\[
B_{\mathrm{tr}}=q(-1,1)^T,\qquad q=(1-\alpha)\sigma_\beta SI.
\]
Therefore
\[
B_{\mathrm{tr}}B_{\mathrm{tr}}^T
=q^2
\begin{pmatrix}1&-1\\-1&1\end{pmatrix}.
\]
The forward Kolmogorov diffusion term for an Itô SDE with covariance matrix \(a\) is \(\tfrac12\sum_{i,j}\partial_{ij}(a_{ij}f)\), which yields the mixed derivative above.

For the published SDE, \(W_1\) and \(W_2\) are independent and the diffusion matrix is diagonal. With the numerical amplitudes \(\sigma_S=q\) and \(\sigma_I=-q\),
\[
B_{\mathrm{ind}}=\begin{pmatrix}q&0\\0&-q\end{pmatrix},\qquad
B_{\mathrm{ind}}B_{\mathrm{ind}}^T=q^2I_2.
\]
The off-diagonal covariance is therefore zero rather than \(-q^2\). This proves that the two SDEs and their Fokker--Planck equations differ whenever \(q\neq0\).

For the scalar total \(T=S+I\), the diffusion coefficient under common transfer noise is \((-q)+q=0\), so transmission noise contributes no quadratic variation to \(T\). Under independent drivers, \(dT\) contains \(q\,dW_1-q\,dW_2\), and independence gives
\[
d[T]_t=(q^2+q^2)dt=2q^2dt.
\]
This is an invariant diagnostic of the mismatch.

## Verification
The bundled checker `verify.py` verifies the two covariance matrices, their ranks, the total-population quadratic-variation coefficients, and an exact rational witness. At \(S=1/2\), \(I=1/4\), and \(\alpha=0\), the paper's coefficient has \(q^2=1/3200\). Genuine transmission noise then gives zero transmission-induced quadratic variation for \(S+I\), while the independent-noise model gives \(1/1600\) per unit time and cross-covariance zero instead of \(-1/3200\).

## Relationship to prior work
Parkinson and Roy explicitly state that taking opposite susceptible and infected noise amplitudes proportional to \(SI\) is equivalent to formally replacing \(\beta\) by a white-noise-perturbed transmission rate, but their displayed SDE immediately thereafter declares the two Wiener components independent. Their simulation section then uses opposite amplitudes and says the choice is meant to express uncertainty in the infection rate.

A closely related earlier model by Parkinson and Wang makes the parameter-perturbation structure explicit: it introduces a single scalar Brownian motion and places the disease-transmission noise with opposite signs in the corresponding susceptible and infected transfer equations. That common-driver structure makes internal transmission noise cancel from the total population. It supports the covariance comparison above but does not state the source-specific Fokker--Planck correction identified here.

## Limitations
The finding does not recompute the optimal controls or quantify how much the corrected rank-one diffusion would alter any particular control trajectory or objective value. It also does not claim that every epidemiological noise model should conserve \(S+I\); conservation is required here only for noise introduced by perturbing the internal transmission rate itself. The conclusion is about the stochastic interpretation and covariance structure of the published numerical model.

## References
1. C. Parkinson and S. Roy, *A Fokker--Planck framework for control of epidemics*, arXiv:2601.20181v1 (first public 2026-01-28); Journal of Mathematical Biology 93, 47 (2026), DOI:10.1007/s00285-026-02462-7.
2. C. Parkinson and W. Wang, *A compartmental model for epidemiology with human behavior and stochastic effects*, arXiv:2507.01046v1; Mathematical Biosciences 392, 109588 (2026), DOI:10.1016/j.mbs.2025.109588.
