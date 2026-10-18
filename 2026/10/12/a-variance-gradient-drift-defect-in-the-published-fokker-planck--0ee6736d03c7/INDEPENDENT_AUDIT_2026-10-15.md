# Independent mathematical audit

## correctness

PASS

Direct differentiation of the forward operator ∂tf+Σ∂j(Fj f)=1/2Σ∂j²(Dj f) gives divergence drift F−(1/2)∂jDj; the published Equation (8) instead has F−∂jDj, yielding exactly L8−L6=−(1/2)Σ∂j((∂jDj)f). For the published Section-5 independent-noise variance D_S=D_I=(1/50)(1−α)²S²I² this changes Ito drifts by −(1/50)(1−α)²SI² and −(1/50)(1−α)²S²I. Independently expanded a polynomial f and rational diffusion with SymPy; residual identity vanished identically. Eq. (9) separately halves the first-order transport term; with D=1, F=(2,0), f=1+S−2t, the weak residual is −∫φ (nonzero), despite f solving Eqs. 6 and 8. Equivalence fails locally for smooth tests, independently of boundaries or solver choice.

## originality

PASS

Exact corrections to the printed Parkinson–Roy strong/weak operator chain diagnose a specific two-stage coefficient error, not a claim to rediscover the general Ito/forward equation. Closely related published research on the same paper treats correlated versus independent Brownian noise and optimization, not its Eq. (8)/(9) equivalence. Best-of-knowledge priority restricted to these displayed equations.

## value

PASS

The discrepancy changes the forward generator and susceptibility/infection mean drifts under the very state-dependent diffusion used in the printed simulations; its second independent weak-form defect affects the published existence argument. This is a concrete, motivated source correction with nontrivial modeling implications, not an isolated typo.

The dated certificate retains the supplied scientific assessment, sources and limitations.
