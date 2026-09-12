# No PING-ING delay-asymmetry switch at fixed E-I loop delay: exact determinant invariance plus validated mean-field and spiking evidence

## Context
Gamma oscillations (30-90 Hz) arise in cortical circuits via Pyramidal-Interneuron Network Gamma (PING, E leads I) and Interneuron Network Gamma (ING, I leads or near-synchronous) mechanisms. A natural question is whether redistributing conduction delay around the E-I loop at fixed total loop delay can switch the dominant mechanism. This record resolves the admitted target: balanced two-population excitatory-inhibitory leaky integrate-and-fire (LIF) network with tau_m,E=20 ms, tau_m,I=10 ms, shared threshold V_th=20 mV, reset 10 mV, refractory 2/1 ms, fast exponential synapses tau_s,E=3 ms, tau_s,I=2 ms (external 2 ms), fixed recurrent peak conductances near PING/ING coexistence at 3-20 Hz fluctuation-driven rates, fixed total loop delay T*=d_EI+d_IE=4 ms, intra-population EE/II delays fixed, asymmetry ratio r=d_EI/d_IE in [0.2,5].

## Definitions
- d_EI, d_IE: cross-population delays E->I? Notation follows target: d_EI+d_IE=T*=4 ms fixed; r=d_EI/d_IE.
- chi_E(w), chi_I(w): single-cell dynamic susceptibilities d nu/d mu at angular frequency w from the Fokker-Planck resolvent.
- A_ab(w)=g_ab/(1+i w tau_s,b): synaptic filters with g_ab=C_ab J_ab tau_s,b.
- M(w;r): 2x2 linearized rate matrix; D(w;r)=det M with separate factors exp(-i w d_EI), exp(-i w d_IE).
- PING vs ING: distinguished by dominant Hopf branch frequency and E-minus-I phase lag; target switch requires discontinuous >=15 Hz dominant-frequency jump plus phase-lag jump at some finite r_c.

## Result
No such critical ratio r_c in [0.2,5] exists. The target claim of a finite asymmetry-driven PING-ING switch with >=15 Hz jump and phase-lag jump is FALSE:
1. The closed two-delay mean-field determinant depends on r only through exp(-i w T*) and is exactly r-invariant, so Hopf frequencies, growth rates, and branch-dominance ordering cannot cross as r varies, while the E-I eigenvector phase rotates continuously.
2. Validated mean-field scans at r=0.2,0.5,1,2,5 give max|D(w;r)-D(w;1)|=9.2e-16 (relative 3.7e-16), identical gamma minima f*=30.10 Hz (second operating point 33.85 Hz, 1.4e-15), and monotone continuous phases 1.304/1.178/1.052/0.926/0.800 rad. Hence no branch crossing, no frequency jump, no bistability interval.
3. Spiking LIF network simulations (NE=2000, NI=500, dt=0.1 ms, T=2500 ms, burn 500 ms) show r-independent stationary rates (~6.2/31.5 Hz E/I) and smooth cross-correlation lags (+0.3,-0.1,-0.9,-1.6,-2.3 ms); PSD-peak argmax variation is seed-level peak-selection noise (23 Hz shift at fixed r=0.5), not a robust mechanism switch; seeds agree to <0.1 Hz (no bistability).
A genuine asymmetry-driven switch would require breaking the fixed-T* constraint (e.g. r-dependent EE/II delays or r-dependent gains), outside the admitted model.

## Proof / Evidence
Closed determinant: linearizing coupled 2x2 Fokker-Planck rate dynamics about the self-consistent fixed point,
M(w;r)=[[chi_E A_EE-1, chi_E A_EI exp(-i w d_EI(r))],[chi_I A_IE exp(-i w d_IE(r)), chi_I A_II-1]],
diagonal EE/II terms carry only fixed delays absorbed in A_EE, A_II. Hence
D(w;r)=(1-chi_E A_EE)(1-chi_I A_II)-chi_E A_EI chi_I A_IE exp(-i w(d_EI+d_IE)).
Since d_EI(r)+d_IE(r)=T* fixed, exp(-i w(d_EI+d_IE))=exp(-i w T*), so D(w;r)=D(w;T*) for all r. Consequences: (i) zero set, Hopf frequencies, margins, dominance ordering exactly r-independent, crossing impossible; (ii) from I-row, v_E/v_I=(1-chi_I A_II)/(chi_I A_IE) exp(+i w d_IE(r)), phase varies continuously linearly in d_IE(r), no jump; (iii) operating-point independent (every fixed point, gain, band). Honest caveat: if EE/II delays were redistributed with r, invariance breaks; admitted model fixes them.
Mean-field computation: self-consistent Siegert iteration from three starts, unique solution; primary point L=1.0, nu_ext=18 Hz: nu_E=9.08 Hz, nu_I=7.27 Hz, mu_E=5.85 mV, sigma_E=11.87 mV, mu_I=8.11 mV, sigma_I=7.75 mV (both means below threshold: fluctuation-driven); second point L=1.5: 9.03/13.01 Hz. Edge-based Scharfetter-Gummel finite volume N=250, adaptive lower bound mu-6 sigma. Validation: FP rate vs Siegert within ~4% (E 8.72 vs 9.08, I 7.00 vs 7.27 Hz); chi(0) vs d nu/d mu within ~5%; zero negative densities. Scan 2-150 Hz confirms invariance to machine precision; zero-delay reference differs (f*=88.2 Hz), confirming delays matter only via total T*.
Spiking validation: Bruno-style current-based LIF with matched exponential-kernel means <s>=tau x rate so currents equal mean-field mu by construction. Mean rates r-independent as theorem demands; PSD-peak argmax varies (39.0,129.5,129.5,124.0,49.5 Hz) but seed change at fixed r=0.5 shifts peak 129.5->106.5 Hz, proving peak-selection noise among competing bumps.

## Limitations
- Mean-field susceptibilities use N=250 finite-volume cells (~4-5% absolute accuracy); invariance itself is exact analytically and confirmed to 1e-15, so grid error cannot affect conclusion.
- Spiking runs use smaller K than mean-field C (200 vs 800) with matched means but larger relative fluctuations; absolute rates differ from mean-field (6/31 vs 9/7 Hz) yet satisfy predicted r-independence.
- Only two mean-field operating points and one spiking drive tested; theorem covers all, so this is a check. Simulations cannot logically rule out chaotic transients mistaken for jumps; seed test addresses it.
- Proof, computed evidence, interpretation separated; no originality claimed for standard FP/Siegert machinery.

## Reproducibility
Run output/artifacts/meanfield2.py (default operating point; `scan` mode surveys loop/drive grid) to reproduce meanfield_results.json and meanfield_curves.npz; second point in meanfield_L15_nue18.json. Run output/artifacts/spikesim.py `python spikesim.py [loop] [r] [seed] [nue]` then analyze_trace to reproduce sim_r_sweep.json rates, PSD peaks, lags, phases. Parameters, fixed-point sols, FP checks, per-r minima/phases, invariance norms, and sim sweep values listed above and in JSON artifacts.

## References
- Z. Liu, F. Han, Q. Wang, review of computational models for gamma oscillation dynamics, Nonlinear Dynamics 108:1849-1866 (2022).
- S. Keeley et al., Firing rate models for gamma oscillations in I-I and E-I networks; PING-to-ING transition via external drive.
- N. Brunel, V. Hakim, Fast global oscillations in networks of integrate-and-fire neurons with low firing rates, Neural Comput. 11:1621 (1999); sparsely synchronized oscillations, Chaos 18:015113 (2008).
- X.-J. Wang, G. Buzsaki, Gamma oscillation by synaptic inhibition in hippocampal interneuronal network model, J. Neurosci. 16:6402 (1996).
- B. Tao, M. Xiao, Q. Sun, Stability and Hopf bifurcation of a two-neuron network with discrete and distributed delays (2017); S. Li et al., Hopf bifurcation of a two-neuron network with different discrete delays (2005); K. Rozier, V. Bondarenko, Hopfield network with two time delays (2022).
