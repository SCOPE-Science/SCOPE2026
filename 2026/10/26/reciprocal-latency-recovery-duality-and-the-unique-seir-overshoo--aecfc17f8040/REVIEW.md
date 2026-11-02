# Independent mathematical audit

## correctness

PASS

For the dimensionless closed SEIR system S˙=−ρ S I, E˙=ρ S I−λ E, I˙=λ E−I, R˙=I, ρ>1, λ>0, take the vanishing-seed unstable-branch limit. Let u=−log S and J(u)=1−e^(−u)−u/ρ=E+I, and V=(1+λ)I/λ. Direct differentiation gives the scalar singular phase equation ρ V V′=κ(J−V), κ=(1+λ)^2/λ=2+λ+1/λ, with a unique admissible branch V(u)>0 and initial slope b>0 solving ρb²+κb−κ(1−1/ρ)=0. The change λ↦1/λ, t↦λt, (S,E,I,R)↦(S,E+(1−1/λ)I,I/λ,R) is a direct exact SEIR conjugacy for λ≥1 and extends by inversion; the susceptible/removed trajectories are identical up to time scaling. The infectious peak occurs at V=J after u=logρ. The singular-ODE comparison gives strict earlier approach to J as κ increases, so S_peak is strictly increasing in κ (and the infection overshoot after peak is S_peak−S_∞). As κ=2+λ+1/λ is uniquely minimized at λ=1, the infectious peak overshoot is uniquely minimized there for fixed ρ; λ→0 or ∞ gives the SIR limit. Independently checked the exact transformed nonlinear vector field and solved the reduced phase ODE at ρ=1.4,2,3.5 for seven reciprocal rates; resulting reciprocal pairs agreed to 1e−12 and minima were strict. Numerical checks corroborate rather than prove global comparison.

## originality

PASS

Qualified best-of-knowledge PASS for the exact reciprocal full-state/time conjugacy and unique λ=1 infectious-peak-overshoot minimizer. Heng–Althaus 2020 carefully analyze the same homogeneous SEIR model but explicitly introduce an approximation dropping a third derivative and infer approximate universal curves; the paper does not prove the claimed exact λ↔1/λ stage transformation or global strict monotone overshoot comparison. Nguyen–Freedman–Ozbay–Levin 2023 establish the SIR overshoot bound 0.2984..., which is reused in the λ→0/∞ limit rather than claimed new. General cooperative epidemic phase-plane theory could contain an implicit ordering or reparameterization, and remains an originality risk.

## value

PASS

The theorem identifies an exact, otherwise concealed parameter symmetry in a standard epidemiological system and settles a natural optimization of the post-peak infection burden over the latency-to-recovery ratio. Its unique equal-rates minimum, reciprocal symmetry and SIR extreme limit are structural global statements rather than a small numerical improvement or parameter rescaling alone. The proof distinguishes an exact susceptible/removal phase conjugacy from prior approximately universal epidemic curve shapes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
