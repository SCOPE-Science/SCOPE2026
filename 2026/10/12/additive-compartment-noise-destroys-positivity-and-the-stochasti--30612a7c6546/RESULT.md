# Additive compartment noise destroys positivity and the stochastic disease-free equilibrium
## Finding
Khan, Khan, and Alqarni model twelve epidemiological compartments by an Itô system whose stochastic part is additive: the \(i\)-th coordinate contains \(\sigma_i\,dB_i(t)\), with the noise intensities declared positive. For a compartment model, however, the state space is the nonnegative orthant. The printed diffusion is incompatible with that state space.

At any boundary point \(x\) with \(x_i=0\) and \(\sigma_i>0\), the \(i\)-th coordinate has a symmetric Brownian fluctuation of order \(\sqrt t\), while the drift contributes only order \(t\). Consequently the process enters \(X_i<0\) with probability tending to \(1/2\) as \(t\downarrow0\). In particular, the deterministic disease-free equilibrium used by the paper has zero infected-stage coordinates and is therefore not an equilibrium of the stated stochastic system when the corresponding additive noise intensities are positive. The stated stochastic asymptotic stability of that disease-free equilibrium cannot hold for equation (24) as printed.

## Assumptions and scope
Consider the paper's equation (24) as an Itô SDE in \(\mathbb R^{12}\), with continuous locally bounded drift \(b\) on the region where the incidence terms are defined and diagonal constant diffusion matrix \(\Sigma=\operatorname{{diag}}(\sigma_1,\ldots,\sigma_{{12}})\). The source states \(\sigma_i>0\). No reflecting, absorbing, truncating, or projection boundary mechanism is included in equation (24).

The finding addresses two precise statements: preservation of nonnegative compartment values and stochastic asymptotic stability of the deterministic disease-free equilibrium. It does not assert nonexistence of a strong solution on unrestricted Euclidean space, nor does it exclude a stationary distribution for an unconstrained extension if the drift is globally well defined there.

## Proof
Fix a boundary state \(x\) with \(x_i=0\) and \(\sigma_i>0\). For the \(i\)-th component,
\[
X_i(t)=\int_0^t b_i(X(s))\,ds+\sigma_i B_i(t).
\]
Continuity of the solution and local boundedness of \(b_i\) imply
\[
\frac{1}{\sqrt t}\int_0^t b_i(X(s))\,ds \xrightarrow[t\downarrow0]{\mathbb P}0.
\]
Since \(B_i(t)/\sqrt t\sim N(0,1)\), Slutsky's theorem yields
\[
\frac{X_i(t)}{\sqrt t}\Rightarrow N(0,\sigma_i^2).
\]
The limiting normal law has no atom at zero, so
\[
\lim_{t\downarrow0}\mathbb P\{X_i(t)<0\}=\frac12.
\]
Thus the closed orthant cannot be invariant whenever a diffusion coefficient remains nonzero on its corresponding boundary face. This is the standard stochastic viability boundary condition in its simplest constant-diffusion form.

The disease-free equilibrium in the source sets the infected and latent compartments to zero. Equation (24) nevertheless assigns those coordinates additive noises such as \(\sigma_2dB_2\), \(\sigma_3dB_3\), \(\sigma_4dB_4\), \(\sigma_7dB_7\), \(\sigma_8dB_8\), and \(\sigma_9dB_9\), with positive intensities. Starting exactly at the disease-free state, each such coordinate therefore has positive probability to become negative immediately. A stochastic equilibrium must remain fixed when initialized there; this one does not. Hence it cannot be stochastically asymptotically stable for the printed SDE.

For completeness, the same obstruction is not confined to boundary initial data. From any strictly positive state, stop the solution upon exiting a compact neighborhood on which the drift is bounded. Wiener measure assigns positive probability to every uniform tube around a Cameron--Martin path. Choosing one Brownian coordinate to follow a sufficiently steep negative linear path and the others to remain in small tubes forces that compartment through zero before the stopping time. Thus positivity also fails with positive probability from interior initial data.

## Verification
The source's HTML full text was inspected at equation (24), where all twelve stochastic terms are additive constants multiplying independent Brownian motions, and at Remark 2, where stochastic asymptotic stability of the disease-free equilibrium is asserted under nonzero noise bounds. The publisher page also gives the publication date 2026-09-02 and primary MSC 92D30.

The boundary argument is analytic and depends only on the small-time orders \(B_i(t)=O_{\mathbb P}(\sqrt t)\) and \(\int_0^t b_i(X(s))ds=O_{\mathbb P}(t)\). `verify.py` checks the exact structural implication that a constant positive diffusion coefficient does not vanish on the boundary and that the listed disease-free infected coordinates retain nonzero diffusion.

## Relationship to prior work
The source itself cites standard stochastic epidemic literature in which positivity is obtained with state-dependent, typically multiplicative, noise. A directly inspected stochastic SIS/SIR comparison likewise uses diffusion coefficients proportional to compartment values or incidence, so the diffusion vanishes on biologically relevant boundary faces. That mechanism is absent from equation (24).

Database searches for the source title together with additive noise, nonnegativity, positivity, orthant invariance, and disease-free equilibrium did not locate a prior record stating this source-specific incompatibility. Earlier findings in the checked ledger concern a Milstein-sign error and a degenerate-diffusion ergodicity proof gap in different models; neither implies the present constant-additive-noise boundary obstruction.

## Limitations
This is a statement about the SDE exactly as printed. Replacing additive noise by multiplicative noise, imposing reflection, stopping at the boundary, or otherwise changing the stochastic model could restore nonnegativity, but those are different systems. The result does not assess the deterministic syphilis model, numerical parameter fitting, or whether an unconstrained diffusion on \(\mathbb R^{12}\) can possess a stationary law.

## References
1. A. Khan, I. Khan, and A. J. Alqarni, “Stochastic dynamics of a syphilis epidemic model with perturbation: Stationary distribution and extinction thresholds,” AIMS Mathematics 11 (2026), 27890–27920, doi:10.3934/math.20261114.
2. L. J. S. Allen, “A primer on stochastic epidemic models: Formulation, numerical simulation, and analysis,” Infectious Disease Modelling 2 (2017), 128–142, doi:10.1016/j.idm.2017.03.001.
3. “Random periodic solution for a stochastic SIS epidemic model with constant population size,” Advances in Difference Equations (2018), doi:10.1186/s13662-018-1511-4.
