# Self-review

## Correctness — PASS
The four Fourier symbols produce an exact real circulant heat propagator with coefficient \(c=(1-2q+q^4)/4=(1-q)(1-q-q^2-q^3)/4\). Its single positive-root threshold, the stochasticity of its rows, and the cubic reaction map prove invariance of the unit cube at and above \(t=\theta\). The opposite output from an impulse saturates to \(1-2a<0\) below that threshold, proving a finite-reaction counterexample. The heat-only threshold follows from \(H_t^2=H_{2t}\), and the fixed-reaction counterexample below half-threshold follows from the derivative of the nonlinear flow at zero. The standalone checker passed 3,533 checks, but analytic steps—not tests—prove the universal quantifiers.

## Originality — PASS, with residual priority risk
The October 2026 Strang/Allen–Cahn source contains continuum bounds and Fourier numerics, not this exact finite-grid all-reaction classification. Dong Li's 2021 extensive work is close and already analyzes effective maximum principles and Fourier-collocation Strang schemes. Its inspected sections do not state the present four-node universal cutoff or nonlinear factor-two separation; earlier general observation that spectral maximum principles can fail is not claimed new. Published positivity-time semigroup and lattice-scheme results cover neighboring but nonidentical implications. The search does not certify absolute priority, and older specialized grid calculations could overlap.

## Mathematical value — PASS
A strict maximum principle is a structural property of numerical reaction–diffusion, not a routine detail of accuracy. The theorem provides a complete smallest-grid threshold and a concrete interval where even positive full-heat propagation is defeated by nonlinear composition. The result offers an exact diagnostic for implementation choices and for interpreting numerical maximum-principle evidence.

## Limits
The result is specific to the standard four-node periodic Fourier pseudospectral Laplacian, exact substeps, and the all-reaction-strength quantifier. Fixed-strength thresholds for every value, higher grids, and between-node positivity are not established. Existing work on effective maximum principles should be consulted before claiming broader priority.

Self-review: passed. Independent audit: not yet performed.
