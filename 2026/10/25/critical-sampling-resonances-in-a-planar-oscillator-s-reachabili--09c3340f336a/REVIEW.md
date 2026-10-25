# Review

**Correctness — PASS.** The continuous-time controllability determinant is \(\omega\ne0\). Exact zero-order-hold formulas yield \(W_h^\top W_h=r^2\begin{pmatrix}1&\cos\theta\\\cos\theta&1\end{pmatrix}\), so the singular set and both asymptotic constants follow analytically. The script is only a numerical cross-check.

**Originality — PASS, with residual risk.** The broad fact that sampling can destroy controllability is classical and is not claimed as new. Targeted database searches found no exact oscillator singular-value formula or parity-dependent inverse-norm law. The relevant section of the primary preprint was read; two classical sources were available only through abstracts, so exact overlap with their full texts remains unresolved.

**Value — PASS.** The result identifies sampling periods at which the exact-tracking matrix cannot be inverted and quantifies how rapidly its inverse norm deteriorates nearby. The different blow-up exponents distinguish a practical failure mode that a binary controllability test does not quantify.

**Closest literature and limitation.** The primary source is *Consistent discretization of finite/fixed-time controllers* (arXiv:2207.03235; later published as DOI 10.1016/j.automatica.2023.111118). Classical sampled-data controllability work discusses loss of controllability under sampling, but the available material did not establish the specific parity-dependent asymptotics proved here. The conclusion is restricted to the planar oscillator and its matrix \(W_h\).

Self-review: passed. Independent audit: not yet performed.
