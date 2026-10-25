# Independent mathematical audit

## correctness

PASS

Checked actual RESULT.md and nested verification/check.py in pinned tree. Conserved first and second half-step energies force equal interface x=s and opposite velocities ±v; positive-root energy quadratures give ξ=v²/(a√s)=6β(β−1)/(1+β²), with existence exactly 0<ξ<4, β in asserted interval. Scaling exhibits two independent segment-variational solutions X′ and X−3θX′/4; endpoint fundamental matrices have nonzero determinants and their product has det=1, rational trace and M21=−6q(β²−1)/(1+β²) ≠0. Factorizations trace−2=−36(β²−1)²/(1+β²)² and trace+2=−16(β²−2)(2β²−1)/(1+β²)² give spectral regimes. Independent SymPy calculations at rational β=11/10,4/3,3/2,2,3 give exact agreement (β=2 trace=−274/25). The defective Jordan conclusion uses nonzero offdiagonal, not just trace. No nonlinear stability or period-doubling asserted.

## originality

PASS

Godoy–Zamora and Boscaggin–Feltrin–Zanolin provide existence theories; Cagnetta 2026 extends existence/uniqueness to this exponent. Those facts alone do not determine the derivative of a forcing-period map. An actual close reading of Cagnetta arXiv:2610.06068 PDF introduction, main theorem and time-map sections found focus on existence and uniqueness, not a Floquet trace or resonance. Distinct exact trace β=sqrt(2) threshold is the incremental claim, not rediscovery of the domain.

## value

PASS

A sharp stability-type transition strictly *inside* the periodic-state existence interval is a motivated Floquet invariant: it separates bounded linearized oscillation from exponential instability, with an explicit defective resonance at an exact dimensionless forcing ratio. The proof demonstrates a useful scaling-mode monodromy mechanism.

The dated certificate retains the supplied scientific assessment, sources and limitations.
