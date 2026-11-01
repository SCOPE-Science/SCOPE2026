# Independent mathematical audit

## correctness

PASS

The actual Smith inner recursion yields cubic error polynomial g3(z;alpha)=(1−alpha)z+alpha(1−alpha)z²+alpha²z³. J-conjugation on symmetric 2×2 matrices is an isometric self-adjoint involution with BOTH ±r eigenmodes, so the Frobenius worst-case factor is exactly max(|g3(r)|,|g3(−r)|). Directly rederived sums and derivatives: u+v=2r²alpha(1−alpha), u−v=2r(1−alpha+r²alpha²), u′=−r(1−r)(1+2r alpha), v′=r(1+r)(1−2r alpha). On alpha<0 the negative mode is worse than unrelaxed; alpha∈[0,1] cannot improve on r³. For r≥1/2 v is maximally negative at alpha=1 on the remaining ray; for 2/5≤r≤1/2 its stationary maximal value gives a global lower bound; for r≤2/5 equating negative mode values yields alpha_c and the two monotonic flanks. Equality and strictness at both interfaces check uniquely. Independent Sympy rederivation and 12 finite minimax grids passed. This does NOT optimize other spectral families, stagewise positivity or floating-point work.

## originality

PASS

Exact MINIMAX SOLUTION of a natural two-mode l=3 problem appears additional to the known recurrence, with explicit boundaries and uniqueness; no previously inspected theorem or table gives it.

## value

PASS

The signed pair is a physically realized minimal nontrivial stochastic-Lyapunov spectrum, and the sharp three-regime optimizer quantifies when restricting to one real inner-step parameter can improve unrelaxed Smith from r³ to r⁴ at small coupling. This solves an optimization left open at higher step count, not merely a polynomial substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
