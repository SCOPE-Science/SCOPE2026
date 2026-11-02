# Scientific review: parity-sensitive planar spin response

## Correctness

**PASS.** The spectral lower bound is attained by three-dimensional cones, alternating planar spins on even cycles, and planar triangle configurations. Equality for longer odd XY cycles would require a constant-modulus three-term Fourier polynomial with a nonzero but nonsaturated average; separating the five Fourier frequencies rules that out. The weak-field expansion is uniform because the zero-field spiral families are compact and the transverse Laplacian has a positive gap. Direct nonlinear optimization and exact Fourier tests are provided in `check.py` (97 tests passed). The proof is finite-dimensional and applies for every stated \(N,J,h\).

## Originality

**PASS on inspected sources, with historical-priority risk.** Schmidt–Luban (arXiv:cond-mat/0209157, §§6.3.1–6.3.2) already proves the isotropic spatial spectral bound, and explicitly reports but does not rigorously prove the coplanar pentagon deficit. That is credited. The new statement proves strict separation for all odd \(N\ge5\), exact equality in the even/triangle cases, and an explicit planar weak-field curvature that is not given by the isotropic parabola. Konstantinidis (arXiv:1405.5931) has open chains and biquadratic terms; Owerre–Nsofini (arXiv:1502.05684) analyzes quantum/anisotropic solitons. Their assumptions do not imply the claim. Priority for more obscure earlier planar ring analyses is not independently settled.

## Mathematical value

**PASS.** This gives a nonperturbative obstruction to realizing the optimal isotropic magnetization response in a planar frustrated odd ring, resolving the precise type of coplanar deficiency identified without proof in the 2002 primary paper. The exact field interval and susceptibility ratio quantify a finite-molecule signature of spin dimensionality, including a special pentagonal golden-ratio value, rather than merely restating a spectral lower bound.

## Limitations

Finite, classical, nearest-neighbor homogeneous rings only; no finite-temperature or quantum conclusion. Numerical calculations corroborate but do not replace the analytic proof. General historical priority remains subject to independent inspection.

Self-review: passed. Independent audit: not yet performed.
