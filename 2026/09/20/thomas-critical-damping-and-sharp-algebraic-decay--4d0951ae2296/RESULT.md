# Critical damping closure and sharp algebraic decay for the Thomas cyclic flow

## System

For an integer \(n\ge 2\) and \(b>0\), consider the cyclic Thomas system
\[
\dot x_i=\sin(x_{i+1})-b x_i,\qquad i\in\mathbb Z/n\mathbb Z.
\]
The classical Thomas attractor is the case \(n=3\).

## Main theorem

The origin is globally asymptotically stable if and only if
\[
\boxed{b\ge 1}.
\]
More precisely:

1. If \(b>1\), every solution satisfies the global exponential estimate
\[
\|x(t)\|_2\le e^{-(b-1)t}\|x(0)\|_2.
\]
2. At the nonhyperbolic threshold \(b=1\), the origin is still globally asymptotically stable.
3. At \(b=1\), the critical relaxation has the sharp global envelope
\[
\boxed{\limsup_{t\to\infty}\sqrt t\,\|x(t)\|_\infty\le\sqrt3},
\qquad
\boxed{\limsup_{t\to\infty}\sqrt t\,\|x(t)\|_2\le\sqrt{3n}}.
\]
Both constants are optimal: every nonzero synchronized trajectory
\(x_1=\cdots=x_n=u\) satisfies
\[
\sqrt t\,|u(t)|\longrightarrow\sqrt3,
\qquad
\sqrt t\,\|x(t)\|_2\longrightarrow\sqrt{3n}.
\]
4. If \(0<b<1\), the origin is unstable and a nonzero synchronized pair of equilibria \(x_i=\pm u_b\) exists, where \(u_b\in(0,\pi)\) solves \(\sin u_b=b u_b\).

Thus \(b=1\) is a genuine nonlinear stability boundary: linearization has a zero eigenvalue there, but attraction persists globally and changes from exponential to algebraic decay.

## Proof

The vector field is globally Lipschitz, so every initial condition has a unique global solution. Set
\[
V(x)=\frac12\sum_{i=1}^n x_i^2.
\]
Then
\[
\dot V=\sum_i x_i\sin(x_{i+1})-b\sum_i x_i^2.
\]
Using \(|\sin u|\le |u|\) and cyclicity,
\[
\begin{aligned}
\dot V
&\le \sum_i |x_i||x_{i+1}|-b\sum_i x_i^2\\
&=-(b-1)\sum_i x_i^2
-\frac12\sum_i\bigl(|x_i|-|x_{i+1}|\bigr)^2.
\end{aligned}
\]
For \(b>1\), this gives \(\dot V\le-2(b-1)V\) and hence the stated exponential bound.

Now let \(b=1\). If \(x\ne0\) and equality held in the displayed estimate, then the second term would force
\(|x_1|=\cdots=|x_n|=r>0\). But for every nonzero real \(u\), \(|\sin u|<|u|\), so each estimate
\(x_i\sin(x_{i+1})\le |x_i||x_{i+1}|\) is then strict. Hence
\[
\dot V(x)<0\qquad(x\ne0).
\]
Since \(V\) is positive definite and radially unbounded, the origin is globally asymptotically stable at the critical value \(b=1\).

For \(0<b<1\), the synchronized line \(x_1=\cdots=x_n=u\) is invariant and obeys
\[
\dot u=\sin u-bu.
\]
The derivative at the origin is \(1-b>0\), so the origin is unstable. Moreover, continuity of \(\sin u/u\) on \((0,\pi]\), with limiting value \(1\) at zero and value \(0\) at \(\pi\), gives a root \(u_b\in(0,\pi)\) of \(\sin u=bu\), and odd symmetry gives \(-u_b\).

It remains to establish the critical rate. Assume \(b=1\) and write
\[
M(t)=\|x(t)\|_\infty.
\]
Global convergence gives a time \(T\) after which \(M(t)\le1\). At any active index with \(|x_i|=M>0\), the upper Dini derivative satisfies
\[
D^+M\le |\sin(x_{i+1})|-M\le \sin M-M,
\]
because \(|x_{i+1}|\le M\le1\). Let \(q\) solve
\[
\dot q=\sin q-q,\qquad q(T)=M(T).
\]
Scalar comparison gives \(M(t)\le q(t)\) for \(t\ge T\). For \(q>0\),
\[
\frac{d}{dt}\frac1{q^2}=\frac{2(q-\sin q)}{q^3}\longrightarrow\frac13,
\]
so
\[
tq(t)^2\longrightarrow3.
\]
Therefore
\[
\limsup_{t\to\infty}\sqrt t\,M(t)\le\sqrt3,
\]
and \(\|x\|_2\le\sqrt n\,\|x\|_\infty\) yields the Euclidean bound. On the invariant synchronized line, \(|u|\) obeys the comparison equation exactly, so the constants \(\sqrt3\) and \(\sqrt{3n}\) are attained.

## Three-dimensional consequence

For the canonical system
\[
\dot x=\sin y-bx,\qquad
\dot y=\sin z-by,\qquad
\dot z=\sin x-bz,
\]
the exact global-stability condition is \(b\ge1\). At \(b=1\), every trajectory tends to the origin, while the slowest possible decay is exactly of order \(t^{-1/2}\):
\[
\limsup_{t\to\infty}\sqrt t\max(|x|,|y|,|z|)\le\sqrt3,
\]
and equality in the asymptotic constant occurs on the synchronized line \(x=y=z\).

## Relation to prior literature

Thomas introduced the cyclic feedback family as a source of labyrinth chaos. Sprott and Chlouverakis studied the three-dimensional dissipative system and its conservative limit, while Chlouverakis and Sprott and later Ho studied higher-dimensional cyclic extensions. These works focus on bifurcation structure, chaos, diffusion and high-dimensional wandering.

Sorin and Tulchinsky (2024) give a recent analytical and numerical treatment of the three-dimensional system. Their inspected stability section treats \(b>1\), using the quadratic Lyapunov function above together with a numerical check of a zero-derivative surface, and then turns to \(b<1\) and the pitchfork branch. The present theorem supplies a dimension-independent analytic inequality that closes the exact nonhyperbolic boundary \(b=1\), and additionally determines the sharp global critical decay rate.

To the best of our knowledge, the combination of (i) the exact global criterion \(b\ge1\), including the equality case, (ii) the sharp \(t^{-1/2}\) critical envelope with constants \(\sqrt3\) and \(\sqrt{3n}\), and (iii) its validity for every cyclic dimension \(n\ge2\), has not been stated in the inspected literature.

## Scientific limitations

The result concerns the damping threshold at the origin and does not classify the rich attractor structure for \(b<1\). The critical bounds are worst-case limsup estimates; they do not assert that every trajectory has the sharp asymptotic constant, since some trajectories can decay faster. The full text of Thomas (1999) was not inspected, and complete coverage of all higher-dimensional Thomas-system literature was not possible. The 2007 hyperlabyrinth and 2019 high-dimensional studies are therefore material residual originality risks, especially for the dimension-general statement, although the sources inspected emphasize chaotic and low-damping regimes rather than critical relaxation. Originality is claimed only to the best of our knowledge.

## References

1. R. Thomas, “Deterministic chaos seen in terms of feedback circuits: Analysis, synthesis, ‘labyrinth chaos’,” *International Journal of Bifurcation and Chaos* 9 (1999), 1889–1905. DOI: 10.1142/S0218127499001383.
2. J. C. Sprott and K. E. Chlouverakis, “Labyrinth Chaos,” *International Journal of Bifurcation and Chaos* 17 (2007), 2097–2108. DOI: 10.1142/S0218127407018245.
3. K. E. Chlouverakis and J. C. Sprott, “Hyperlabyrinth chaos: From chaotic walks to spatiotemporal chaos,” *Chaos* 17 (2007), 023110. DOI: 10.1063/1.2721237.
4. R. D. J. G. Ho, “High dimensional chaotic systems which behave like random walks in state space,” arXiv:1908.05989 (2019).
5. V. Basios, C. G. Antonopoulos and A. Latifi, “Labyrinth chaos: Revisiting the elegant, chaotic, and hyperchaotic walks,” *Chaos* 30 (2020), 113129. DOI: 10.1063/5.0022253.
6. I. Sorin and M. Tulchinsky, “Infinite Bifurcations in Thomas system,” arXiv:2408.09525 (2024).
