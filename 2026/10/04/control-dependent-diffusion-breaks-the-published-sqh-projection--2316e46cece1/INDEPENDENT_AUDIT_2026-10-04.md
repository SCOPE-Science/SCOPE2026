# Independent mathematical audit

## correctness

PASS

The source theorem's algebraic defect is real. The published Theorem 4.3 defines \(r(w)\) by a spatial integral, hence as a scalar, but then takes a three-component \(L^2\) norm of differences of \(r\) and inserts \(r(u^k)\) into a three-vector projected update. For the paper's own simulation diffusion \(\sigma_S=-\sigma_I=\sqrt{0.02}(1-w_1)SI\), freezing \(f^k,q^k\) gives a diffusion contribution \(D_k(1-w_1)^2\), with \(D_k=0.01\int f^kS^2I^2(q^k_{SS}+q^k_{II})\). Thus the first-coordinate augmented objective has curvature \(\beta_2+2\varepsilon-2D_k\), and when this is positive its unconstrained minimizer is \((d_{1,k}-\beta_1-2D_k+2\varepsilon u_1^k)/(\beta_2+2\varepsilon-2D_k)\), not the printed value-based formula. Independently, a fixed point of the proximal subproblem yields only \(H(u^*)\le H(w)+\varepsilon\lVert w-u^*\rVert^2\); the nonnegative proximal term cannot be discarded. These are proof-level failures of the stated contraction/minimum conclusion, without implying divergence of the implementation or invalidating the separate descent statements.

## originality

PASS

The directly relevant article was inspected at theorem level and a targeted Resultary/current-literature search found no correction or prior statement of the source-specific \(D_k(1-w_1)^2\) term or the scalar-versus-vector defect. Earlier SQH work treats different smooth ODE/PDE settings and does not imply the corrected minimizer for this Hamiltonian with control-dependent diffusion. The result is therefore best-of-knowledge original as a concrete correction of the 2026 theorem.

## value

PASS

The result identifies two concrete mathematical failures in a newly published convergence theorem and derives the correct frozen-coordinate minimizer for the paper's actual control-dependent diffusion. That is a motivated correction with direct consequences for what the stated SQH theorem certifies, while carefully preserving unaffected descent results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
