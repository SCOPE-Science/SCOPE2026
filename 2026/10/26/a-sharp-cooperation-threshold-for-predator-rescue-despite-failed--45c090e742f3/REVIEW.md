# Scientific review

## Correctness — PASS

The model is specified with positive rates, a subunit prey harvest, and a strict predator-free invasion barrier. The predator nullcline gives \(u=B/(1+\alpha v)\) exactly; clearing positive denominators produces a quartic with negative constant and all higher coefficients except the linear one strictly negative. Descartes' rule bounds positive roots by two, counted with multiplicity. Reparametrizing by \(z=\alpha v\) and \(t=1/\alpha\) gives a strictly decreasing quadratic threshold in \(t\) for every allowable \(z\). Its maximizer exists by endpoint decay, and the root count and tangency follow without numerical extrapolation. The determinant identity fixes the lower root as a saddle, and the upper root in the exact rational example is a sink by root brackets and a strictly negative trace. The predator-free equilibrium has two strictly negative eigenvalues. `verify.py` independently confirms the algebraic identities and exact rational certificate. Limits: no global basin or universal upper-branch stability claims.

## Originality — PASS, with residual priority risk

The motivating source is Belew and Melese's 2022 published full-text model, which treats a one-positive-root sign regime and stability/Hopf analysis; its inspected discussion does not give the sharp cooperation threshold in the predator-free-stable regime or an exact bistable parameter witness. Du–Niu–Wei (2021/2022) use a different nondifferentiable group-defense response, while Jang–Yousef (2023) use a discrete-time refuge model; both exhibit cooperative-hunting bifurcations but neither accessible statement entails this exact continuous-time harvesting/fear theorem. Query-based searches of prior mathematical findings found related results for different flow/map equations rather than the same nullcline polynomial. No search establishes absolute novelty; relevant full texts beyond the motivating source remained inaccessible, so publication priority has residual uncertainty.

## Value — PASS

The scientific question is whether cooperative hunting can rescue a predator even when the predator-free equilibrium remains locally stable against rare predator invasion. The finding gives a complete equilibrium-count transition at a single sharp cooperation value for all admissible parameters in that regime, and an exact positive-parameter sink–saddle–sink example establishing robust coexistence-versus-extinction bistability. This is a structural classification of a biologically motivated persistence threshold, not a routine restatement of local linearization or a small numerical parameter sweep.

Self-review: passed. Independent audit: not yet performed.
