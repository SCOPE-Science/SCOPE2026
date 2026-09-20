# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The global threshold follows from an exact cyclic energy estimate. For
\(V=\tfrac12\sum_i x_i^2\), the inequality
\[
\dot V\le -(b-1)\sum_i x_i^2-\frac12\sum_i(|x_i|-|x_{i+1}|)^2
\]
is valid in every cyclic dimension. At \(b=1\), equality away from the origin is impossible: equality in the cyclic square term would force all component magnitudes to coincide, while \(|\sin u|<|u|\) is strict for every nonzero real \(u\). This gives a strict radially unbounded Lyapunov function and therefore global asymptotic stability at the nonhyperbolic threshold. For \(b<1\), the synchronized scalar equation has positive linear slope at the origin and nonzero equilibria, so the converse is immediate.

The critical-rate argument was checked separately. Once convergence places the trajectory in \(\|x\|_\infty\le1\), the upper Dini derivative of the active maximum obeys
\(D^+\|x\|_\infty\le\sin\|x\|_\infty-\|x\|_\infty\). Comparison with the scalar synchronized equation is therefore valid. For that scalar equation,
\(d(q^{-2})/dt=2(q-\sin q)/q^3\to1/3\), proving \(q\sim\sqrt{3/t}\). Synchronized trajectories attain the resulting infinity- and Euclidean-norm constants, so the envelope is sharp. A direct numerical integration of the scalar comparison equation was also consistent with \(\sqrt t\,q(t)\to\sqrt3\); the proof does not depend on that computation.

## Originality

**PASS, to the best of our knowledge.** The search covered the canonical Thomas attractor, labyrinth chaos, hyperlabyrinth chaos, high-dimensional cyclic extensions, the pitchfork threshold, global stability, critical damping and algebraic decay.

Thomas (1999) introduced the feedback construction. Sprott--Chlouverakis (2007) and Chlouverakis--Sprott (2007) studied the three-dimensional and higher-dimensional labyrinth systems, with emphasis on chaos, diffusion, Lyapunov spectra and routes to chaos. Ho (2019) explicitly studies an \(n\)-dimensional Thomas generalization, mainly in the moderate- and low-damping random-walk regimes. Basios--Antonopoulos--Latifi (2020) revisit the conservative labyrinth-walk structure and coupled systems.

The most relevant current source inspected in detail is Sorin--Tulchinsky (2024). Its stability section treats \(b>1\), where it uses the same quadratic energy but supplements the sign argument with a numerical surface check; the following section discusses \(b<1\) and the pitchfork branch. No inspected portion gives a rigorous equality-case theorem at \(b=1\), a critical algebraic convergence rate, or the sharp constants proved here.

No inspected source states the dimension-independent exact criterion together with the sharp \(t^{-1/2}\) critical envelope. The complete text of Thomas (1999) was not inspected, and the full high-dimensional literature was not exhaustively checked. The 2007 hyperlabyrinth paper and Ho (2019) are the most relevant residual risks for the \(n\)-dimensional extension. The novelty claim is therefore deliberately limited to the rigorous boundary closure and sharp critical-rate theorem, not to the known pitchfork or the known \(b>1\) stable regime.

## Value

**PASS.** The result closes the only nonhyperbolic point in the standard damping threshold and replaces a partly numerical three-dimensional sign check by a short analytic inequality valid in every cyclic dimension. The sharp critical law also explains what changes dynamically at the threshold: exponential damping for \(b>1\) degenerates to an optimal \(t^{-1/2}\) relaxation at \(b=1\), while the origin becomes unstable below it. This gives a precise global counterpart to the familiar local pitchfork picture.

## Scientific limitations

The theorem does not address the existence, stability or multiplicity of limit cycles and chaotic attractors below \(b=1\). The sharp constants describe a global worst-case asymptotic envelope and are attained on the synchronized invariant line; they are not claimed as the asymptotic constant of every trajectory. The full text of Thomas (1999) and complete coverage of every higher-dimensional follow-up were not available for inspection, so equivalent earlier statements remain a residual originality risk.
