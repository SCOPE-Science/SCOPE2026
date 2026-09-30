# Distributed-delay dispersion quench of delay-driven gamma in a homogeneous inhibitory LIF network

## Context
A homogeneous inhibitory leaky integrate-and-fire network can lose asynchronous-state stability through a delay-driven Hopf crossing. This record quantifies how broadening a gamma-distributed transmission delay at fixed mean suppresses that instability for one specified operating point. The repaired claim is deliberately a **linear-stability Hopf crossing plus finite-spiking quench**, not a proof of a supercritical nonlinear Fokker–Planck limit-cycle branch.

## Model
Parameters (mV, ms): `tau_m=20`, `Vth=20`, `Vr=10`, `tref=2`, `Vlb=-30`, `tau_s=2`, `mu_ext=28`, `sigma_noise=5`, and effective recurrent coupling `J_eff=-600 mV`. The delay kernel has mean `D*=4 ms` and standard deviation `sigma_D`; for `sigma_D>0`, shape `k=D*^2/sigma_D^2`, scale `theta=sigma_D^2/D*`, and Laplace factor

`K(s)=(1+theta*s)^(-k)`, with `K(s;0)=exp(-s D*)`.

With firing rate `nu` in `1/ms`, the synaptic variable obeys the dimensionally consistent equation

`tau_s ds/dt = -s + J_eff*tau_s*(K*nu)(t)`, `mu(t)=mu_ext+s(t)`.

Thus the normalized synaptic filter is `H_s(s)=1/(1+s tau_s)` and the feedback loop contains the DC-gain factor `J_eff*tau_s`.

## Result
The asynchronous stationary density has `nu0=10.53 Hz` and `mu0≈15.36 mV`. Linearizing the Scharfetter–Gummel Fokker–Planck discretization gives the characteristic equation

`F(s;sigma_D)=1-J_eff*tau_s*H_s(s)*A(s)*K(s;sigma_D)=0`,

where `A(s)` is the complex rate susceptibility of the stationary density. At `J_eff=-600 mV`, the gamma-band crossing moves from unstable to stable near `sigma_D≈1.1 ms`: on the N=600 voltage grid the critical-coupling values are approximately

- `sigma_D=0`: `f*=65.16 Hz`, `J_c=-542 mV`;
- `0.75`: `65.21 Hz`, `-569 mV`;
- `1.00`: `65.33 Hz`, `-591 mV`;
- `1.10`: `65.41 Hz`, `-602 mV`;
- `1.125`: `65.43 Hz`, `-605 mV`;
- `1.25`: `65.57 Hz`, `-622 mV`;
- `1.50`: `66.02 Hz`, `-663 mV`.

Hence the fixed coupling is unstable at `sigma_D=1.0 ms` and stable by `1.125 ms`, with a threshold close to `1.1 ms`; the onset frequency changes little. At `sigma_D=4 ms` the archived scan finds no 30–120 Hz negative-real crossing.

Matched finite spiking simulations show the corresponding phenomenology: the 55–100 Hz population-rate peak falls from about 3565 at zero dispersion to about 46–67 by `sigma_D=2 ms` and below about 10 by `sigma_D=4 ms`, while the single-cell rate remains near 10.5–10.7 Hz. The archived finite-size scan changes from an approximately N-independent peak at zero dispersion to a shrinking fluctuation peak above the crossing, consistent with quenching of a collective oscillation.

## Independent numerical check
A fresh implementation of the filed N=600 Scharfetter–Gummel stationary problem and complex susceptibility reproduced `nu0=10.5326 Hz`, `f*=65.1589 Hz, J_c=-541.99 mV` at zero dispersion, `65.4067 Hz, -602.09 mV` at `sigma_D=1.1 ms`, and `65.4301 Hz, -605.12 mV` at `1.125 ms`.

## Limitations
This record establishes a numerical linear stability crossing and compatible finite-network quenching for one parameter set. It does **not** compute a Hopf normal-form coefficient, Floquet multipliers, or a nonlinear Fokker–Planck periodic branch; therefore “supercritical” is not claimed. The monotonic `|J_c|` trend is numerical rather than a global theorem. Finite networks retain fluctuation peaks after mean-field stabilization.

## Reproducibility
Repository artifacts are under `artifacts/`: `fp.py`, `final_table.py`, `sigmac4.py`, `lammax.py`, the simulation scripts, and archived sweep files. Running `python3 artifacts/final_table.py` from the record directory reproduces the N=600 linear-stability table.

## References
- N. Brunel and V. Hakim, *Fast global oscillations in networks of integrate-and-fire neurons with low firing rates*, Neural Computation 11 (1999), doi:10.1162/089976699300016179.
- N. Brunel, *Dynamics of sparsely connected networks of excitatory and inhibitory spiking neurons*, Journal of Computational Neuroscience 8 (2000), doi:10.1023/A:1008925309027.
