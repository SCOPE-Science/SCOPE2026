# Independent mathematical audit

## correctness

PASS

Substituting \(g_t=\lambda x_t\) and \(\beta_1=\beta_2=0\) into Algorithm 1 gives exactly \(x_{t+1}=x_t(1-q_t)\) with \(q_t=a/M_t^{2p}\). If \(q_t\le2\), the historical maximum freezes and the dynamics become linear; if \(q_t>2\), a new maximum is created and \(q_{t+1}=q_t/(q_t-1)^{2p}\). For \(p\le1/4\), \((q-1)^{2p}\le\sqrt{q-1}\) and \(q>2\sqrt{q-1}\), so the interval \((2,\infty)\) is invariant and the decreasing sequence tends to its only fixed point \(2\). For \(p>1/4\), the derivative at the fixed point is \(1-4p<0\), so a decreasing orbit approaching from above must enter a neighborhood mapped below \(2\), giving finite stabilization. Fresh map iterations reproduced both regimes, and the frozen direct-Padam verifier was read.

## originality

PASS

Chen et al. define the exact max-memory Padam rule and their published theory also singles out \(p\le1/4\) in a stochastic convergence corollary, but that is a different theorem under different assumptions. In particular, their Theorem 4.3 requires \(\beta_1<\beta_2^{2p}\), which the boundary choice \(\beta_1=\beta_2=0\) does not satisfy. The paper does not derive the scalar overshoot map, the critical radius, persistent two-cycle, finite-crossing dichotomy, or exact resonance set. The follow-up convergence paper treats broad adaptive methods rather than this max-memory dynamical normal form. Resultary returned no matching phase-transition theorem.

## value

PASS

The result exposes an exact bifurcation in a named adaptive optimizer, explains why the same numerical threshold \(1/4\) can arise from a completely different mechanism, and supplies both the persistent-cycle and self-stabilizing sides with an exact critical radius. The boundary model is intentionally simple but mathematically diagnostic rather than an arbitrary parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
