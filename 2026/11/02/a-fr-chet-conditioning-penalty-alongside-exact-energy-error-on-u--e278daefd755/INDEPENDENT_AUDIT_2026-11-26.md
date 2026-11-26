# Independent mathematical audit

## correctness

PASS

Reconstructed RESULT.md lines 26–48. Element derivatives of the nodal interpolant are averages of the exact derivative, giving Ritz orthogonality and error Σh_j³/12. The Dirichlet mixed moments give 36n(n+19)/(n)_6 before division by 144 for the second raw moment; subtracting the squared mean yields the stated variance. The exponential ratio has delta-method influence (Y³−18Y+12)/12 with variance 5/2. Integration against the empirical knot measure differs from Lebesgue integration of v² by at most 2δ||v′||²/π; Poincaré and a sine-interpolant trial sandwich n λ_min at π². For fixed M, the probability that Y_j≤M/n occurs at a boundary or in adjacent edges is O((M+M²)/n); the probability no such edge exists is e^(−M). On the complement, the short-edge sum has top eigenvalue 2T_n/Y_(1), and the scaled norm of the other edges is at most 4(T_n/n)/M. Letting n then M grow yields λ_max/n² ⇒ 2/Z and the stated Fréchet law by Slutsky. Inverse minimum-spacing moments bound κ_n moments for q<1. For the reverse, take h_2 arbitrarily small with h_1,h_n bounded away from zero on a positive-density simplex family: the all-ones nodal trial bounds λ_min from above using only boundary edges, whereas the opposite-sign interior-edge trial gives λ_max≥2/h_2. This proves divergence including q=1 and requires n≥3. The n=2 condition number is one and n=1 has no free matrix. The uniform eigenvalues 4n sin²(kπ/(2n)) give the comparison. VERIFICATION.md and verify.py were inspected, not executed; their finite tests do not certify the limit or divergence.

## originality

PASS

The supported distinct result is the exact Fréchet law for the unpreconditioned condition number and its accompanying finite-moment/accuracy benchmark, not a new law for uniform spacings or the diffusive lower spectral edge. The nearest weighted-path theorem covers the latter exactly, not the large eigenvalue; the nearest indexed record analyzes a different operator and invariant on the same meshes.

## value

PASS

The sharp benchmark distinguishes a finite factor-six expected squared-energy penalty from an order-n typical conditioning penalty and a genuinely infinite conditioning mean at each nontrivial resolution. The exact scale identifies which mesh defect causes the conditioning problem and makes the result useful when comparing knot-generation rules or conditioning remedies; it does not make assertions about a preconditioner or runtime.

The dated certificate retains the supplied scientific assessment, sources and limitations.
