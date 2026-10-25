# Independent mathematical audit

## correctness

PASS

Synchrony makes each softmax row uniform; row-sum differentiation cancels each attention-weight derivative, so D F acting on tangent perturbations equals r^{-1}P_{Rv}(h_i+eta V hbar), independently of queries and keys. On extreme eigenspace B=I+eta V acts as r diag(1,-1), producing the reflected synchronized eigencircle, fixed under F². The mean/zero-sum token splitting gives circle tangent multiplier 1, remaining common modes ((1+eta lambda_j)/r)^2, n-1 disagreement tangent modes cos²(2theta)/r², and (n-1)(d-2) other disagreements at 1/r². Multiplicities add to n(d-1); strict endpoint simplicity and r>1 force every transverse multiplier <1. The F² derivative has no normal-to-tangent linear component, so smooth tubular coordinates yield O(z²) angular increments and geometric normal contraction, selecting a unique asymptotic phase. Independently tested the nonlinear three-token two-head attention map with arbitrary Q/K heads and nonidentical value matrices summing to diag(2,-1/2,-5): four phases and finite-difference Floquet normal spectra agreed to <3e-7; bounded checks only support the universal proof.

## originality

PASS

The synchronized extreme-plane reflection is ordinary normalized power iteration and cannot be claimed new. The original same mathematical model Altafini paper establishes strict stability below the spectral boundary but the available abstract/secondary evidence cannot exclude an uninspected boundary theorem. Gao--Yang--Chen examine repulsive negative scalar value with a different diagonal attention mask and flip consensus, which does not yield the mixed-sign, fully self-inclusive multihead normal Floquet spectrum. The claimed contribution is the precise interacting-token phase-dependent normal multipliers and nonlinear phase selection.

## value

PASS

A sharp exceptional parameter boundary between stable consensus and mixed-sign flip dynamics is a natural dynamical question for residual normalized multihead maps. The exact transverse rates, universality with respect to query/key matrices, and local phase-selection law quantify robustness of an entire neutral periodic family rather than only noting a trivial eigencircle.

The dated certificate retains the supplied scientific assessment, sources and limitations.
