# Independent mathematical audit

## correctness

PASS

The all-positive-mass all-n proof reconstructs the free-path mass-weighted Rayleigh characterization. For w_j=j-mu with sum m_jw_j=0 and each edge difference 1, every design has lambda2<=K/V. The proposed C_i=sum_{j<=i}m_j(mu-j) has pair representation C_i=(1/M0) sum_{j<=i<l}m_jm_l(l-j)>0, and sum C_i=V, so k_i=(K/V)C_i is admissible. Coordinate differences C_i-C_{i-1}=m_i(mu-i) yield Lw=(K/V)Mw. Symmetrized M^-1/2LM^-1/2 is an irreducible symmetric Jacobi matrix, and w is a monotone eigenvector with exactly one nodal change (possibly one zero), identifying the FIRST positive eigenmode by Sturm. Equality in Rayleigh for any other allocation forces w to be a first eigenmode and the endpoint plus successive coordinate equations recover every k_i uniquely. For m constant, mu=(n+1)/2, C_i=mi(n-i)/2 and V=mn(n²-1)/12. Series springs under ±endpoint force have compliance sum_i1/k_i=(n²-1)H_{n-1}/(3K), while Cauchy-Schwarz gives the sharp uniform-stiffness minimum (n-1)²/K, yielding ratio [(n+1)/(3(n-1))]H_{n-1} ~ (log n)/3. Boundary n=2 ratio=1; n=3 the dynamic optimum is uniform and ratio=1. Independent numerical generalized eigensolvers checked 408 heterogeneous-mass instances n=2..35 against 5 random competitors each plus 2..199 equal-mass compliance identities; largest absolute spectral mismatch 8.18e-14. Finite numeric checks corroborate, not prove, the theorem. Independent seven-Git-blob tree hash calculation matched 336489d599e998689046d6c63fd62ef5a01cbe53.

## originality

PASS

Best-of-knowledge originality restricted to the arbitrary unequal-positive-inertia generalized path eigenvalue optimizer; graph Fiedler method, equal-mass special case and simple harmonic-number evaluation already follow from prior work. Three genuine Resultary queries and targeted primary-text searches did not find a dominating all-mass formula, with explicit close-source and access risks.

## value

PASS

This is a natural finite but all-length physical spectral design problem: a fixed spring-material budget, any heterogeneous inertial masses, and free rigid translation. The complete unique allocation and closed performance envelope K/V are operationally useful without an arbitrary numerical cutoff. A weighted center produces genuinely distinct tuning from the ordinary equal-mass graph solution. The exact endpoint static compliance penalty makes a real trade-off explicit; its harmonic-number evaluation alone is elementary and not independently priority-bearing. The claim does not imply robustness, multiobjective optimality, other graph topologies or nonlinear regimes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
