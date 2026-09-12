# Dense E-I QIF heterogeneity-ratio gamma restoration: existence, critical ratio, and spiking confirmation

## Context

Gamma oscillations (30–100 Hz) in cortex arise from excitatory–inhibitory (E–I) interaction, but the role of heterogeneous excitability across versus within populations is not settled. For quadratic integrate-and-fire (QIF) networks the Ott-Antonsen / Montbrió-Pazó-Roxin (MPR) reduction gives an exact neural mass whose bifurcations can be computed. The admitted target asks, for a dense (globally coupled, mean-field limit) E–I QIF network at fixed total Lorentzian heterogeneity S* = Delta_E + Delta_I = 2.0 with all other parameters fixed and a stable asynchronous baseline at uniform Delta_E = Delta_I = 1.0 with no 30–100 Hz gamma peak: does redistributing the fixed budget along rho = Delta_E/Delta_I over [0.1, 10] restore a stable gamma limit cycle through a Hopf bifurcation, in which direction, at what threshold and frequency, with what E-vs-I signature, and is it confirmed in finite spiking simulations?

## Definitions

- Populations a in {E, I}; membrane time constant tau_m = 5 ms; synaptic filters tau_sE = 2 ms, tau_sI = 4 ms.
- Rate coupling JEE = 6, JEI = −20, JIE = 8, JII = −6; mean excitabilities etaBar_E = 1.0, etaBar_I = −2.0.
- Lorentzian half-widths Delta_E(rho) = S* rho/(1+rho), Delta_I(rho) = S*/(1+rho), S* = 2.0, rho in [0.1, 10].
- Exact MPR mass, time in ms, rates in 1/ms (×1000 = Hz), state y = (rE, vE, rI, vI, sE, sI):
  dr_a/dt = Delta_a/(pi tau_m^2) + 2 r_a v_a/tau_m,
  dv_a/dt = (v_a^2 + etaBar_a + tau_m (J_aE sE + J_aI sI) − (pi tau_m r_a)^2)/tau_m,
  ds_a/dt = (−s_a + r_a)/tau_sa.
- At steady state s_a = r_a. The 6×6 Jacobian A(rho) (4 MPR + 2 synaptic rows) gives the closed rho-parametrized stability condition p(l; rho) = det(l I_6 − A(rho)) = 0; Hopf: p(iw; rho) = 0 with w = 2 pi f/1000 plus transversality d Re l/d rho ≠ 0.

## Result

YES — E-concentrated restoration (rho_c > 1). For the fixed parameter set above, the exact mass has a unique physical fixed-point branch over rho in [0.1, 10]; it is stable with no gamma peak at rho = 1 and loses stability in a simple transversal Hopf at rho_c = 2.545 (Delta_E = 1.436, Delta_I = 0.564) with onset frequency f_c = 34.6 Hz. The bifurcating branch is a stable gamma limit cycle (direct integration: persistent large-amplitude oscillation at 34.7–38.7 Hz for rho = 2.8–6.0, E leading I by ~1.29 rad), with no bifurcation on the I-concentrated side (rho < 1 stable down to 0.1). Finite heterogeneous spiking QIF simulations (N = 7500) confirm: asynchronous at rho = 1, coherent ~38 Hz gamma at rho = 4 matching mass cycle means within ~2% and frequency within 10 Hz.

Branch (rates in 1/ms; maxRe = max eigenvalue real part; mode frequency): rho=0.1: (0.0039,−1.475,0.0329,−1.760), maxRe=−0.299, 19.0 Hz; rho=0.5: (0.0184,−1.154,0.0280,−1.516), −0.176, 24.0 Hz; rho=1.0: (0.0351,−0.907,0.0257,−1.238), −0.093, 26.8 Hz; rho=1.5: (0.0473,−0.808,0.0252,−1.011), −0.047, 30.3 Hz; rho=2.0: (0.0547,−0.776,0.0250,−0.847), −0.020, 32.8 Hz; rho=2.545: (0.0597,−0.766,0.0250,−0.719), 0.000, 34.6 Hz (Hopf); rho=3.0: (0.0624,−0.765,0.0250,−0.638), +0.013, 35.6 Hz; rho=4.0: (0.0661,−0.771,0.0250,−0.510), +0.034, 36.9 Hz; rho=6.0: (0.0694,−0.786,0.0251,−0.362), +0.060, 38.1 Hz; rho=10.0: (0.0717,−0.808,0.0253,−0.228), +0.086, 38.9 Hz. Bisection: rho_c = 2.54534, critical pair ±0.21729i/ms (34.58 Hz), d Re/d rho = +0.0317/ms; other eigenvalues −0.571 (×2), −0.399 (×2).

Cycle survey (RK4 dt = 0.05 ms, 3 s; means ± half peak-to-peak, Hz): rho=1.0 decayed amp 0; rho=2.0 decayed; rho=2.8: 34.7 Hz, E 59.4±20.6, I 26.2±13.7, persist 1.00; rho=3.2: 35.3 Hz, E 59.3±30.3, I 28.5±26.7; rho=4.0: 36.7 Hz, E 60.2±39.3, I 32.5±53.9; rho=6.0: 38.7 Hz, E 63.2±47.9, I 37.7±127.7. Cross-spectrum arg(S_IE) = −1.29 rad (E leads I ~74°, ~5.6 ms at 36.7 Hz), consistent −1.24 to −1.29 rad across rho = 2.8–6.0.

## Proof / evidence

Numerical-computational (not analytic closed form). Newton continuation from 6 spread starts finds one physical fixed point at each probed rho; 6D Jacobian eigenvalues give stability; bisection on the warm-started branch locates the simple Hopf with transversality verified at two finite-difference steps. Baseline no-peak check at rho = 1: linear-response power of (rE+rI) to voltage noise at 5/10/20/30/40/60/80/100 Hz = 0.0129/0.0146/0.0212/0.0215/0.0119/0.0036/0.0017/0.0009; 30–100 Hz max / 5 Hz = 1.66 (no gamma peak); perturbed integration decays to amplitude 0. Spiking: heterogeneous QIF, NE = 6000/NI = 1500, Lorentzian currents etaBar + Delta tan(pi(u−1/2)) clipped ±150, Euler dt = 0.01 ms with overshoot-carry reset (vp = 100, vr = −100), T = 2 s, 1-ms-binned rates, Hann-windowed (500 ms, 50% overlap) PSD. rho = 1: mean E/I 34.5/25.3 Hz (mass fp 35.1/25.7), sd 2.2/3.7, gamma/base ratio ~188 broad fluctuation bump peaking 34 Hz; rho = 4: mean 59.3/32.0 Hz (mass cycle 60.2/32.5, within 2%), f_pk = 38.0 Hz (mass 36.7 Hz, within 10 Hz), gamma/base 3.2e5/2.4e5, sd 28.9/32.7 Hz — coherent gamma restored. Independent audit recomputation reproduced residuals (~3e-14), eigenvalues, transversality, and spectrum ratio.

## Limitations

Existential witness for one fixed admissible parameter set, not a universal statement over all drives/couplings. Mass proof is numerical (Newton + eig + bisection + integration). Spiking check is N = 7500, T = 2 s, single seed per rho. No delays or sparsity by design (dense limit). Uniqueness rests on spread-start Newton at probed rho values; cycle stability from persistent integration rather than Floquet analysis.

## Reproducibility

Scripts use NumPy only: stage5.py (branch + bisection → bisect.json), stage6.py (cycles → cycle_rho*.json), stage7b.py (spiking → spikeB_rho*.json), stage8.py (branch table + baseline spectrum). Precomputed JSON outputs archived alongside.

## References

- Montbrió E., Pazó D., Roxin A., Macroscopic Description for Networks of Spiking Neurons, Phys. Rev. X 5:021028 (2015).
- Devalle F., Roxin A., Montbrió E., Firing rate equations require a spike synchrony mechanism..., PLoS Comput. Biol. (2017).
- Tahvili F., Destexhe A., A mean-field model of gamma-frequency oscillations..., bioRxiv 2023.11.20.567709.
- Zheng Q., Rinzel J., Gamma Oscillations in QIF based E-I Network, JoCN Forum (2026).
