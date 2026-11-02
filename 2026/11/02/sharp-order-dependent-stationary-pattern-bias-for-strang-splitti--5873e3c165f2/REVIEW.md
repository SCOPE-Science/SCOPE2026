# Mathematical review

## Correctness — PASS

For any connected finite unweighted \(d\)-regular bipartite graph, the bipartition-sign vector has Laplacian eigenvalue \(2d\). All odd pointwise powers preserve its one-dimensional span, so both exact propagators reduce to one-dimensional maps. Direct composition of the analytic reaction flow and the scalar heat multiplier gives two rational-power maps \(F(x)=a x(1+b|x|^{2p})^{-1/(2p)}\), both with \(a=e^{(1-\lambda)\tau}>1\) and explicit positive denominators. Their reciprocal-amplitude iterates obey an exact affine contraction, proving the three fixed points, global sign-conditional convergence and equal derivative \(e^{-2p(1-\lambda)\tau}\) on the invariant line. The hyperbolic identities are obtained by explicit algebra; the threshold signs follow from strict growth of \(\sinh z/z\), and the exponential-rate conclusion follows from the standard \(\log\cosh\) asymptotics. The proof covers every integer \(p\ge1\), every eligible graph and every \(\tau>0\). A bundled checker provides supplementary symbolic and numerical tests but is not treated as a universal proof.

## Originality — PASS, subject to residual priority risks

The 2026 periodic-PDE Strang study and the 2021 scalar Allen–Cahn predecessor address maximum principles, uniform Sobolev stability, energy decay and fixed-time error, rather than a two-order comparison of exact stationary checkerboard branches on a graph. The 2025 Neumann-boundary paper similarly addresses regularity and finite-time convergence. Bösenhofer's 2023 study does give general steady-state splitting bias for a linear-affine reaction–diffusion surrogate, and that established phenomenon is explicitly excluded from the novelty claim. Its equations do not determine the nonlinear odd-power checkerboard amplitudes or the sharp sign transition \(\lambda=1/2\). Literature and related exact-claim databases were compared for equivalent parameterizations and stronger implications. No direct coverage was located in material inspected; an unexamined specialized source might still contain an equivalent calculation.

## Mathematical value — PASS

The example is not a one-off numerical anomaly: it spans every finite regular bipartite graph and every odd power, including cubic Allen–Cahn. Both Strang orders are exact subflow compositions with identical local contraction multipliers on each patterned equilibrium, yet yield opposite stationary bias signs on a full interval, all-step stationary exactness in only one order at the sharp critical diffusion rate, and an exponential separation rate that is independent of the power. This provides a precise benchmark for long-time pattern fidelity that is not explained by usual finite-time second-order truncation bounds. The checked boundary is necessary for deciding whether a diffusion-outside or reaction-outside method is suitable for faithfully representing the nontrivial stationary branch.

## Closest sources and limitations

Closest sources: Luo–Quan–Tan–Wu (2026), arXiv:2610.14867v1; Li–Quan–Xu (2021), arXiv:2108.05214; Quan–Tan–Wu (2025), arXiv:2504.07520v1; Bösenhofer (2023), DOI 10.1016/j.combustflame.2023.112881. General equilibrium bias under Strang splitting predates the present calculation. The theorem says nothing about transverse stability of its checkerboard fixed points in the full graph system or infinite-dimensional periodic PDE stationary states. Independent mathematical validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
