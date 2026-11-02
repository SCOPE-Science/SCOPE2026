# Independent mathematical audit

## correctness

PASS

For fixed D,γ,v,L>0, real C∞ L-periodic nonconstant U, the D>0 elliptic tilted generator has an isolated simple principal eigenvalue near (ε,k)=(0,0). Its unperturbed value λ0(k)=Dk²−γ+sqrt(γ²+v²k²), giving base diffusivity D+v²/(2γ). First-order ε correction vanishes because ∫U′=0. Two Fourier transitions through q≠0 give λ2(k)=kΣ_(q≠0)(k+iq)q²|u_q|²H_q(k), where H is the explicitly displayed symmetric/antisymmetric-spin two-by-two resolvent. Independently recomputed H_q(0) and rationally differentiated H′_q(0) in SymPy: −q²[H_q(0)+iqH′_q(0)]=K(q²) identically for symbolic positive D,γ,v,q. Pair ±q cancels the linear-k coefficient, hence V(ε)=O(ε³) and D_eff=D+v²/(2γ)−2ε²Σ_(n≥1)|u_n|²K(q_n²)+O(ε³). The rational numerator K has positive coefficients for t>0 and the independently differentiated K′ equals the displayed strictly positive expression. K(0)=1/(D+v²/(2γ)), K(∞)=1/D+v²/(γD²), and v=0 reduces to classical K=1/D. Smooth U ensures differentiated Fourier series converges; error is for each fixed parameter set and not uniform in D→0 or γ→0. Independent 13-mode Fourier–Bloch matrix computation at k=±0.0007,0 and ε=0.08,0.04 for three D,γ,v,U combinations agreed with predicted coefficient to errors ≤2×10^−6 in diffusivity, corroborating but not proving the infinite-dimensional result.

## originality

PASS

Best-of-knowledge qualified originality: comparison against D>0 RTP ratchet stationary-current work (same generator, different observable), exact RTP transport at D=0 (different singular regime), general Markov-noise homogenization (implicit broad method, no stated spectral sign/strict frequency law), flashing-potential diffusion (different generator), and passive benchmark. Exact all-frequency second-order K and positive derivative remain unlocated. A general perturbative formula could yield it by further derivation; risk is explicit.

## value

PASS

For persistent active transport, the exact long-time variance is a natural and physically meaningful invariant distinct from stationary drift. The theorem supplies a universal sign for every real smooth nonconstant periodic potential, quantitative suppression by its Fourier spectrum, and a strict order of equal-amplitude spatial wavelengths for v>0. These are nontrivial statements not read from a stationary-current expression; it clarifies the active-vs-passive difference by an explicit nonconstant K(t), including a classical passive limit. No measured-experimental or finite-amplitude claim is added.

The dated certificate retains the supplied scientific assessment, sources and limitations.
