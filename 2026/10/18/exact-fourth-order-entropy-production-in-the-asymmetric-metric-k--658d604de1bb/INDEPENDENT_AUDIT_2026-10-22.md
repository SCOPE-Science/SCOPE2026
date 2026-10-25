# Independent mathematical audit

## correctness

PASS

For each fixed finite L≥3 and α∈[0,1], strictly positive synchronous heat-bath transitions imply an analytic stationary law near J=0. Stationarity cancels π and log cosh terms from path-reversal KL, leaving directed left/right flux J(1−α)(<σ_left tanh JS_0>−<σ_right tanh JS_0>). Off-diagonal same-time C_ij starts at J²Σ_k w_ik w_jk, while C_ii≡1; cubic fair-spin Wick parity gives E0[σ_j S_0³]=3 w_0j(3+α²)−2w_0j³. Local common-input walks add the anomalous extra overlap only at L=4 (a displacement ±2 coincidence); all L≥5 and L=3 share ordinary overlap count. Therefore E_L=(1−α)²J²−(1−α)²(7+α+α²+3α 1_{L=4})J^4/3+O_{L,α}(J^6). Independent SymPy construction of the directed-neighbor map reproduced polynomial coefficients for L=3,...,10; original 207 exact rational assertion source inspected. Crucially the all-L conclusion comes from finite displacement classification, not the finite test range.

## originality

PASS

Di Carlo (2024/2025) studies the exactly matching four-neighbor asymmetric metric kinetic Ising model and derives its flux identity, but Eq. (6) is an empirically successful (1−α)² ansatz and explicitly not proven exact. The new microscopic exact J^4 term proves failure of exact α-factorization and identifies a torus-specific L=4 correction missing in that source. More general mean-field asymmetric Ising and directed-network entropy models do not automatically impose this finite-torus coefficient. Priority against a hidden general perturbation theorem remains uncertain.

## value

PASS

It resolves the explicit mathematical validity of a widely motivated quadratic asymmetry ansatz in the same model by producing its first nonfactorizing correction. The finite-size wrapping term is important for comparing discrete microscopic simulation sizes and continuum/thermodynamic approximations. It is a natural model-specific exact high-temperature law, not a randomly selected coefficient with no comparison target.

The dated certificate retains the supplied scientific assessment, sources and limitations.
