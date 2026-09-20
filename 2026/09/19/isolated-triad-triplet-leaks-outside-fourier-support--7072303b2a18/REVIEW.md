# Scientific review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS. The source explicitly writes the full Euler/Navier--Stokes Fourier convolution and separately writes the seven-mode isolated-triplet equations. The proposed finite reconstruction can solve the full PDE only if its Fourier support is invariant under every quadratic interaction. In the source's displayed parameter example, the retained modes `p` and `qg` form an additional triad with a wavevector outside the retained support. Substitution into the source's own helical coefficient formula gives nonzero forcing for both possible output helicities. The generating signed pair is unique, excluding cancellation by another retained pair. A standalone calculation reproduces these statements.

The conclusion is also consistent with Kishimoto--Yoneda's classification theorem: a real-valued 3D Euler solution with finite Fourier support is time-independent. The source's claimed finite-mode solution is explicitly time-periodic and nonstationary.

## Originality

PASS, narrowly scoped. The general fact that a Galerkin/triad truncation is not automatically an invariant Fourier subsystem is standard, and the Kishimoto--Yoneda finite-mode classification is prior art; neither is claimed as new. The contribution is the source-specific diagnosis of arXiv:2609.20710v1: identification of an explicit omitted cross-triplet triad in the paper's own numerical example, evaluation of its nonzero helical forcing, and consequent correction of the paper's claim that its isolated-triplet periodic orbit is an exact full-Euler solution.

Searches for the arXiv identifier, exact title, "triad triplet" together with finite-Fourier/Euler terminology, and repository overlap found no public correction or SCOPE record stating this source-specific leakage result. The source full text does not cite Kishimoto or use the phrases "finite Fourier" or "Galerkin". Because the preprint is very recent, an unindexed author revision or independent comment remains a residual originality risk.

## Value

PASS. The distinction changes the mathematical status of the main advertised object: it remains an exact solution of a finite-dimensional triad-network model, but not an exact solution of the full inviscid Navier--Stokes PDE. This matters for interpretation of energy trapping and for the paper's proposed use as a nonlinear PDE benchmark.

## Limitations

The explicit numerical leakage is demonstrated for the parameter set used in the paper's Fig. 2 / Sec. IV.2. Generically the same cross-triplet mechanism persists whenever the corresponding external triad is nondegenerate and does not collide with retained support, but no exhaustive classification of exceptional `(g,h)` geometries is claimed here. The result does not assess the paper's infinite-chain/fractal ansatz, nor does it deny the exactness of Eq. (42) as a reduced ODE system.

The Kishimoto--Yoneda theorem applies to real-valued Euler fields. That is the natural physical interpretation of the paper's velocity field; if its finite Fourier sum were instead read literally as a complex-valued field without conjugate completion, the seven-mode equations involving conjugated amplitudes would no longer be the standard Fourier convolution of that literal field, so that reading does not restore the advertised exact-PDE claim.
