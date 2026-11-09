# Independent mathematical audit

## correctness

PASS

Substitution of a four-periodic block gives exactly four product-one constraints P_j=x_{j+1}y_jw_{j+3}z_{j+2}=1 with independent logarithmic gradients, leaving dimension 16−4=12. At each such history, all denominators equal one and the log-linearized one-step 20x20 matrix T_p has four cyclic Fourier factors L_q. Their exact factorizations give (λ−1)^3(λ+1)^3(λ²+1)^3(λ²−p)^2(λ²+p)^2; roots are semisimple for p>0,p≠1, so T_p^4 has 12 neutral and eight p² multipliers. Tangent directions equal the neutral fixed-manifold eigenspace; a normal contraction plus summable tangential drift yields local convergence to some periodic manifold point for p<1, and p>1 has eight unstable directions. Independent SymPy block expansion and exact 20x20 specializations p=1/2 and 2 confirmed the two-eigenvalue annihilator, ranks, and all factors. This does not establish global attraction or p=1 dynamics.

## originality

PASS

Murovhi–Folly-Gbetoula–Anani 2026 already solve more general nonautonomous recurrences and show reciprocal-product affine reductions with factor AE=p² on the common-parameter specialization. This element is explicitly prior-covered. Their inspected theorem and closing discussion do not classify the full ORIGINAL 20-dimensional return derivative, 12-dimensional semisimple neutral eigenspace and local manifold attraction/instability. Earlier autonomous sign-case paper (Elsayed–Alofi 2023) remained inaccessible in full text and may overlap. Qualified best-of-knowledge PASS for the full spectral/multiplicity/manifold-stability package.

## value

PASS

The system is an explicit natural four-component higher-order rational recurrence with a nonisolated periodic manifold. Separating the 12 neutral directions from eight normal p² directions, including stable p<1 and unstable p>1 regimes, is a meaningful local dynamical classification absent from a scalar-product multiplier alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
