# Scientific review

## Correctness — PASS

The stated scalar SDC map is fully specified by two three-by-three rational matrices and constant-stage initialization. Direct interpolation verifies the quadrature weights; linear error reduction gives the dynamic trace, determinant and strict contraction radius for each finite negative real step. Taking the rational stiff limit gives a two-dimensional affine map, whose characteristic polynomial yields an exact endpoint recurrence and its trigonometric solution. Irrationality of \(\arccos(11/12)/\pi\), by the algebraic-integer argument, and circle equidistribution prove the infinite density statement. The finite witness at \(z=-5000\) is checked in exact rational arithmetic. The standalone verifier checks 114 exact algebraic and recurrence assertions; finite checking is not substituted for infinite proof.

## Originality — PASS, with specified residual risk

The closest source, arXiv:2403.13454, defines the SDC sweep and its implicit-Euler preconditioners but does not present the exact half-density law in the inspected methods, adaptivity, and stability discussion. DOI:10.1137/24M1649800 develops general stiff-limit SDC matrices and empirical stability regions for other preconditioners; that framework is acknowledged, not claimed. The abstract of Minion's earlier stability analysis, DOI:10.4310/CMS.2003.v1.n3.a6, is relevant but its entire source was not materially compared here, so it remains a residual priority risk rather than being labeled non-covering. Targeted searches found no equivalent theorem. This is a reasoned self-review, not a certificate of uniqueness.

## Value — PASS

The result isolates a numerically meaningful paradox: a uniform strict spectral contraction for the inner correction iteration does not prevent finite-sweep time-stepping instability, even for negative real scalar decay and stable collocation. Its exact first failing stiff sweep and natural density \(1/2\) show the issue is recurrent across sweep counts, not an isolated anomaly. This matters for selecting fixed sweep counts in stiff time integration without assuming that more correction iterations monotonically improve absolute stability.

## Closest literature and limitations

The numerical method and generic SDC machinery are established prior art. The theorem applies only to a three-node Lobatto rule, backward-Euler preconditioning, exact stages, constant initialization, and scalar negative real tests. It does not assert nonlinear instability, failure for every timestep, or nonconvergence of the correction solver. Older SDC stability calculations remain a residual possible equivalence.

Self-review: passed. Independent audit: not yet performed.
