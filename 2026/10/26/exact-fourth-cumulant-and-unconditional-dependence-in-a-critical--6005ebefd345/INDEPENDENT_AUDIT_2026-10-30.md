# Independent mathematical audit

## correctness

PASS

C PASS: Inspected the actual stationary two-sided diffusion with positive Q_t=1/8−(rU_t+delta E_t)^2/2. U_t=delta∫_{−∞}^t e^(−a(t−s))E_s ds has |rU+delta E|<=delta/a<1/2, so Q>0 and stochastic integrals exist. Generator L on UE,U²,U³E,U⁴ yields stated exact moments; the centered pair (U²−EU²,UE−EUE) has triangular drift M and covariance S. For r>0, v=(r²,2r delta) has positive components; S and e^(M^Tt) are entrywise positive, proving C_Q(t)>0. Laplace resolvent L(z)=v^TS(zI−M^T)^−1v/4 gives Var(V_k)=L(k)/k, Cov(V_k,V_l)=[L(k)+L(l)]/(k+l), and conditional Gaussian identities give cum4=3L(k)/k and positive cross-squares covariance. Algebra simplifies to the printed rational cumulant; its denominator and residual polynomial are strictly positive on 1/2<a<=1 and c>0, and factor (a−1)^2 enforces the iff r=0 boundary. At r=0 Q constant, so the Brownian-driven modes really are independent Gaussians; their unconditional zero covariance for r>0 does not imply independence. Independently derived the same symbolic cumulant from both resolvent and stationary mixed U,V moment recursion, using SymPy identity simplification, not source code.

## originality

PASS

O PASS qualified: the cited 2026 limiting process and conditional Gaussianity, as well as Markov-modulated OU moment techniques, are prior. The contribution is its specific closed fourth cumulant and exact positive cross-square dependence criterion. Direct switching coefficients in general MMOUs do not by themselves state the identity for a causal continuously filtered telegraph factor. A general older OU-mixture stochastic-volatility theorem may allow derivation, but no exact same-parameter implication was established.

## value

PASS

V PASS: Detecting strictly non-Gaussian stationary marginals and dependence between two uncorrelated fluctuation modes in a natural, already-studied critical switching model directly answers a structural probabilistic question that second moments cannot resolve. The exact iff boundary and positive dependence are independently useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
