# Independent audit — 2026-09-30

**Record:** `2026/09/20/thomas-critical-damping-and-sharp-algebraic-decay--4d0951ae2296`  
**Audited repository:** `SCOPE-Science/SCOPE2026` at `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Audited tree:** `1fce8f0e4b2e7ac7d3d6b85d9b122d667e9db37a`  
**Disposition:** **PASSED**

## Correctness — PASS

The global-stability and rate arguments were reconstructed independently. For V=1/2 sum_i x_i^2, cyclicity and |sin u|<=|u| give dot V<=-(b-1)sum_i x_i^2-(1/2)sum_i(|x_i|-|x_{i+1}|)^2. At b=1 equality away from the origin is impossible because equal nonzero component magnitudes would still make every |sin x_{i+1}|<|x_{i+1}| strict, so V is a strict radially unbounded Lyapunov function. For b<1 the synchronized invariant scalar equation u'=sin u-bu has positive derivative at zero and nonzero equilibria. At b=1, after convergence enters ||x||_inf<=1, the active maximum satisfies D^+M<=sin M-M; comparison with q'=sin q-q and d(q^-2)/dt=2(q-sin q)/q^3 -> 1/3 yields limsup sqrt(t) M<=sqrt(3), with the synchronized line attaining sqrt(3) and sqrt(3n). No algebraic or sign gap was found.

## Originality — PASS (literature-bounded)

Sorin and Tulchinsky (arXiv:2408.09525, 2024) was checked through its openly indexed full-text extraction. Its Section 2.1 is explicitly the case b>1 and uses the quadratic Lyapunov function together with a numerical zero-surface check; Section 2.2 moves directly to b<1 and the pitchfork, so it does not close the nonlinear equality case b=1 or give the t^{-1/2} law. Searches around the Thomas/labyrinth and higher-dimensional literature did not locate the sharp critical constants or the dimension-independent b=1 theorem. The originality claim remains bounded because the full 1999 Thomas paper and every higher-dimensional follow-up were not exhaustively inspected.

## Scientific value — PASS

Closing the nonhyperbolic threshold analytically is a real strengthening of the standard b>1 stability statement, and the sharp t^{-1/2} envelope identifies the precise loss of exponential damping at criticality. The proof also extends uniformly to every finite cyclic dimension n>=2.

## Evidence and literature

- Sorin and Tulchinsky, Infinite Bifurcations in Thomas system (2024): https://arxiv.org/abs/2408.09525
- Chlouverakis and Sprott, Hyperlabyrinth chaos (2007): https://doi.org/10.1063/1.2721237
- Ho, High dimensional chaotic systems which behave like random walks in state space (2019): https://arxiv.org/abs/1908.05989

## Limitations

- The theorem does not classify the rich subcritical attractor structure for b<1.
- The critical constants are worst-case global limsup constants; not every trajectory is asserted to have the synchronized asymptotic constant.
- Thomas (1999) and the full higher-dimensional literature were not exhaustively inspected, so priority is stated only to the best of the checked literature.

The independent audit finds the record scientifically complete on correctness, originality, and value at the audited tree. The originality verdict is bounded by the literature access and searches described above and does not treat inaccessible material as read.
