# Above-threshold loop-trapped non-scattering flow for focusing quintic NLS on the Kirchhoff tadpole

## Context
Whether the real-line mass-critical scattering threshold survives a bound loop is the open above-threshold regime beyond the settled below-threshold scattering/blow-up dichotomy on star graphs (Hamano et al., arXiv:2212.06411). The Kirchhoff tadpole (loop plus half-line) is the canonical minimal loop-plus-tail resonator, also modeling ring-with-lead photonic and BEC loop-junction trapped vs radiating pulses.

## Definitions
- `T`: tadpole graph with loop `[-pi,pi]` (endpoints identified at vertex, circumference `2pi`) plus half-line `[0,infinity)`, with Kirchhoff vertex conditions `u(pi)=u(-pi)=v(0)`, `u'(pi)-u'(-pi)=v'(0)`.
- Flow: focusing mass-critical quintic NLS `i dt Psi + Delta_T Psi + |Psi|^4 Psi = 0`, `Psi(t) in H^1(T)=H^1_C(T)`, `Delta_T <= 0` Kirchhoff Laplacian.
- `Q`: 1D line quintic ground state for the same coefficient-1 equation, `-Q''+Q-Q^5=0`, with mass `M(Q)=||Q||_{L^2(R)}^2=sqrt(3)*pi/2`.
- Noja–Pelinovsky family: `Phi_3(.,omega)` solving `-Delta Phi_3-3Phi_3^5=omega Phi_3`, `omega<0`, from arXiv:2001.00881.

## Result
There exist `delta>0`, `c0>0`, and `Psi0 in H^1(T)` with `M(Psi0) in (M(Q),M(Q)+delta)` — in fact with masses attainable arbitrarily close above `M(Q)` — whose forward `H^1` flow `Psi(t)` satisfies `||Psi||_{L^6([0,infinity) x T)}=infinity` (no scattering in the target's stated sense) and loop-trapping `limsup_{t->infinity} ||Psi(t)||_{L^2(loop)} >= c0 > 0`.

Explicitly: `Psi0 = Phi_1(.,omega*)` with `Phi_1 = 3^{1/4} Phi_3`, `omega*=omega_1` (mass-maximizing frequency), `M(Psi0)=M_max=sqrt(3)*mu_max > M(Q)`, `Psi(t)=e^{-i omega* t}Phi_1`, `||Psi||_{L^6([0,T)xT)}^6=T a^6` with `0<a<infinity`, and `||Psi(t)||_{L^2(loop)} equiv c0 >= m sqrt(2pi)>0` where `m=min_loop Phi_1>0`.

## Proof / evidence
1. **Stationary input (cited):** Noja–Pelinovsky arXiv:2001.00881 v3, Thms 1.1–1.3: for every `omega<0` a minimizer of `B(omega)=inf{B_omega(U):||U||_{L^6}=1}` yields a strong solution `Phi_3(.,omega) in H^2_{NK}(T)` of `-Delta Phi_3-3Phi_3^5=omega Phi_3`, real/positive/symmetric/monotone; mass `mu(omega)` is `C^1` with `mu->pi/4` (`omega->0`), `mu->pi/2` (`omega->-inf`), `mu'>0` on `(-inf,omega_1)`, `mu'<0` on `(omega_1,0)`, and window (1.21).
2. **Strict exceedance (proved):** `mu_max:=mu(omega_1)>pi/2` by contradiction with the `-inf` limit (strict increase forces `mu(omega**)<mu(omega_1)` for any `omega**<omega_1`, hence limit `<=mu(omega**)`). `mu_max` is the finite global maximum by strict monotonicity on each side.
3. **Scaling (exact):** `lambda=3^{1/4}` maps coefficient-3 to coefficient-1: `Phi_1=lambda Phi_3` solves `-Delta Phi_1-Phi_1^5=omega Phi_1` since `3 lambda^{-4}=1`; masses scale by `lambda^2=sqrt(3)`; Kirchhoff conditions preserved by linearity.
4. **Threshold:** line soliton `phi=sech^{1/2}(2x)` solves `-phi''+phi-3phi^5=0` (analytic check via `phi'/phi=-tanh 2x`); masses `pi/2` (line), `pi/4` (half-line) via `sech` integral `=arctan=pi/2`; `Q=lambda phi` is the GN optimizer for coefficient-1 normalization by homogeneity of the GN ratio (Weinstein/Kwong), so `M(Q)=sqrt(3)pi/2`, independent of `omega<0`; witness exceeds threshold under either normalization.
5. **Arbitrarily close above (proved):** continuity + strict decrease on `(omega_1,0)` + limit `pi/4` gives via IVT full coverage of `(mu_R,mu_max]`, hence `(M(Q),M_max]` after `sqrt(3)` scaling.
6. **Dynamical lift (verified term-by-term):** with the phase-convention flip (`e^{-i omega t}` for the target vs NP's `e^{+i omega t}`), `Psi(t)=e^{-i omega* t}Phi_1` satisfies `i dt Psi+Delta Psi+|Psi|^4 Psi=(omega*Phi_1+Delta Phi_1+Phi_1^5)e^{-i omega* t}=0` using `|e^{itheta}r|^4e^{itheta}r=e^{itheta}r^5`; `Psi in C(R;H^1)` by phase rotation; forward restriction is the forward flow via cited `H^1_C` LWP uniqueness.
7. **Scattering norm and trapping:** `|Psi|` time-independent gives `||Psi||_{L^6([0,T)xT)}^6=T a^6`, `a` finite via `H^1->L^6` and positive via `a^6>=2pi m^6>0`; hence infinite on `[0,infinity)`, finite on every finite truncation. Loop mass constant `c0>=m sqrt(2pi)>0`.
8. **Machine replay:** `verify_masses.py` (masses, ODE, scaling, lift algebra) and `verify_target_logic.py` (9 mechanism checks) replay `VERIFY_OK` with stdlib only. Supporting RK4 shooting (`mu~1.631>pi/2`) is evidence only, not used in proof.

## Limitations
- Stationary existence/regularity/monotonicity/`C^1` (Thms 1.1–1.3) imported from peer-reviewed Noja–Pelinovsky, not re-proved.
- Witness is a standing (periodic, non-dispersing) wave; no blow-up, asymptotic stability, or Kenig–Merle rigidity claim.
- Operative non-scattering criterion is exactly the target's stated infinite-`L^6` condition, verified exactly; the remark linking it to `H^1`-asymptotic-completeness scattering cites the tadpole `(6,6)` Strichartz estimate (edgewise plus Kirchhoff-vertex argument) without proof.
- Forward-flow identity uses standard cited quantum-graph `H^1_C` LWP uniqueness.

## Reproducibility
- `python3 output/artifacts/verify_masses.py` -> `VERIFY_OK` (line/half-line quadrature to 1e-8, ODE residual ~2.7e-6, scaling identities).
- `python3 output/artifacts/verify_target_logic.py` -> `VERIFY_OK` (scaling, exceedance/IVT patterns, ordering, L6 growth, loop bound, Kirchhoff, phase factoring, rescaling invariance).
- Analytic steps checkable line by line without new computation.

## References
- D. Noja, D. Pelinovsky, Standing waves of the quintic NLS equation on the tadpole graph, arXiv:2001.00881.
- D. Noja, D. Pelinovsky, G. Shaikhova, Bifurcations and stability of standing waves in the NLS equation on the tadpole graph, arXiv:1412.8232.
- M. Hamano et al., Global dynamics below a threshold for NLS with Kirchhoff and repulsive Dirac delta on a star graph, arXiv:2212.06411.
- J. Angulo Pava, A. Perez Yepez, NLS-log on a tadpole graph, arXiv:2502.21200.
- N. Goloshchapova, M. Ohta, Blow-up and strong instability for NLS-delta on a star graph, arXiv:1908.07122.
