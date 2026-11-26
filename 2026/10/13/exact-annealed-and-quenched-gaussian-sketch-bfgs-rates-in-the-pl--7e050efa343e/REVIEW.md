# Independent mathematical audit

## correctness

PASS

For fixed SPD H in dimension two, whitening gives the exact update E_j=(v_j v_j^T) E_{j-1} (v_j v_j^T), where v_j is orthogonal to the whitened sketch. The squared Frobenius error is the initial squared quadratic form times the product of successive cos^4 angle differences. Every nonzero symmetric E_0 has a nonzero initial projection almost surely. The doubled Gaussian direction is Poisson-kernel distributed with Fourier moments r^|m|, so the difference has moments r^(2|m|). The log of the product obeys the ergodic theorem (or apply the strong law separately to its odd and even pairs), and the Poisson mean of log|cos| is log((1+r²)/2). For the expectation, the cos^4 kernel is finite rank, positive semidefinite by its Fourier expansion and positive almost everywhere. Its top eigenvalue is simple, and the positive eigenfunction has nonzero pairing with both the initial squared quadratic form and 1. Reflection puts the eigenfunction in the even sector, with matrix D times the angular Gram matrix on (1,cos 2θ,cos 4θ), D=diag(3/8,1/2,1/8). The trace, principal-minor sum and determinant are (11+4r²+r⁴)/16, (17−12r²−5r⁴)/128 and 3(1−r²)²/512, confirming the cubic. The uniform row-integral bound is strictly below one for r<1; entrywise Perron comparison is strict, including from r=0 where the first diagonal entry 3/8 is exceeded by the Perron root of any positive T(r). At r=0 and the stated initial matrix the first factor is one and successive conditional expected factors equal 3/8. The general claims are asymptotic nth-root factors, not per-step deterministic contractions or optimization-iterate rates. Replay: RESULT.md lines 35–90; verify.py was inspected, not executed. The frozen finite rational, quadrature and simulated checks are corroborative only.

## originality

PASS

The supported distinct content is the explicit pair of planar Gaussian inverse-error factors and the proof that the mean-square Perron factor is attained for all nonzero symmetric initial errors. The BFGS update, projection formulation, and general convergence guarantee are prior work. Neither the closest catalogue claims nor the primary statements inspected provide the exact factors for this recurrence.

## value

PASS

The planar case is the first in which Gaussian BFGS has genuinely random relative directions. The exact expected rate replaces a loose projector bound, and the simultaneous pathwise factor quantifies why that expectation can describe a very different timescale from a typical run. The all-start attainment result and anisotropy dependence make this a useful benchmark for stochastic inversion rather than just a recomputation of the isotropic example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
