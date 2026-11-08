# Independent mathematical audit

## correctness

PASS

The backward moment generator with signed speed and flip rate xi and Bernoulli absorption/reflection gives H_n'= -n*S_(n-1), S_n'=2*xi*H_n-n*H_(n-1). Solving collision boundary conditions yields mean F_(xi,Q)(P); differentiation gives sign (1-2xi)(4-Q+2Qxi)/denominator^2 on feasible P from max(0,Q-1) to Q^2/4. Thus maximal asymmetry below xi=1/2 and equal split above, all tied at equality. An independently solved second-moment boundary ODE at xi=1/2 reproduces Var(vT/h)=(96-32Q-11Q^2+32P)/(6Q^2), strictly increasing with P, including both exact variance penalties. Handles Q=2 and xi=0. No Monte Carlo substituted for proof.

## originality

PASS

Best-of-knowledge PASS for fixed-Q constrained global optimization and variance selection. Angelani 2016 supplies strictly broader unconstrained law for first-passage times, including computable moments; these ingredients are fully credited, while the optimization and sharp tie break were not stated in inspected equations.

## value

PASS

The exact optimizer switches sharply as persistence changes, and an entire degenerate mean-optimal allocation interval is resolved by an exact variance tie-break. Boundary allocation under a natural fixed sum of per-collision capture probabilities is a mathematically motivated design problem; the exact threshold and budget-dependent tie penalty are not mere restatement of a telegraph MFPT formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
