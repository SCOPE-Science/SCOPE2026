# Critical damping rigidity and logarithmic relaxation in the Thomas cyclic sine ring

## Statement

Consider the cyclic sine-feedback system
\[
\dot x_i=\sin(x_{i+1})-b x_i,\qquad i\in\mathbb Z/N\mathbb Z,
\]
with \(N\ge 3\), \(b>0\), and \(x_{N+1}=x_1\).  For \(N=3\) this is the standard Thomas cyclically symmetric system; the same ring is also studied in the higher-dimensional hyperlabyrinth literature.

### Theorem 1: exact global damping threshold

The origin is globally asymptotically stable if and only if
\[
\boxed{b\ge 1}.
\]
More precisely, for \(b>1\),
\[
\|x(t)\|_2\le e^{-(b-1)t}\|x(0)\|_2.
\]
At the nonhyperbolic endpoint \(b=1\), the origin is still globally asymptotically stable.  For \(b<1\), it is linearly unstable in the common-mode direction \((1,\ldots,1)\).

### Theorem 2: complete critical-rate dichotomy at \(b=1\)

At \(b=1\), there is a smooth invariant strong-stable manifold \(W^{ss}(0)\) of codimension one, tangent at the origin to
\[
\left\{x:\sum_{i=1}^N x_i=0\right\}.
\]
Initial data in \(W^{ss}(0)\) converge to the origin exponentially.

Every initial condition outside \(W^{ss}(0)\) has a sign \(\sigma\in\{+1,-1\}\) such that all coordinates eventually have sign \(\sigma\), synchronize exponentially, and satisfy
\[
\boxed{
\frac1{x_i(t)^2}=\frac t3-\frac1{20}\log t+C+o(1)
}
\qquad (i=1,\ldots,N)
\]
with the same finite constant \(C\) for every coordinate.  In particular,
\[
\boxed{\sqrt t\,x_i(t)\longrightarrow \sigma\sqrt3}
\qquad (i=1,\ldots,N).
\]
Thus the pitchfork threshold itself is attracting: generic critical trajectories relax only algebraically, while the exceptional codimension-one set relaxes exponentially.

## Proof

### 1. A global Lyapunov inequality

Let
\[
V(x)=\frac12\sum_{i=1}^N x_i^2.
\]
Then
\[
\dot V=\sum_i x_i\sin x_{i+1}-b\sum_i x_i^2.
\]
Using \(|\sin s|\le |s|\) and cyclic indexing,
\[
\dot V
\le \sum_i |x_i|\,|x_{i+1}|-b\sum_i x_i^2
=-(b-1)\sum_i x_i^2
-\frac12\sum_i\bigl(|x_i|-|x_{i+1}|\bigr)^2.
\]
For \(b>1\) this gives \(\dot V\le-2(b-1)V\), hence the stated global exponential estimate.

At \(b=1\), the derivative is strictly negative for every nonzero state.  Indeed, equality in the last quadratic term requires all \(|x_i|\) to be equal.  If their common value is positive, then \(|\sin x_i|<|x_i|\) for every coordinate, so the preceding sine inequality is strict.  If the common value is zero, the state is the origin.  Therefore \(V\) is proper and has a negative-definite derivative, proving global asymptotic stability at \(b=1\).

The linearization at the origin is \(P-bI\), where \(P\) is the cyclic shift.  Its common-mode eigenvalue is \(1-b\).  Hence \(b<1\) makes the origin linearly unstable.  This proves Theorem 1.

A related endpoint observation is that at \(b=1\) the origin is the only equilibrium.  If an equilibrium had \(M=\max_i|x_i|>0\), choose an index with \(|x_i|=M\).  From \(x_i=\sin x_{i+1}\),
\[
M=|\sin x_{i+1}|<|x_{i+1}|\le M,
\]
a contradiction.

### 2. Center and transverse dynamics at the threshold

Now set \(b=1\).  Write \(e=(1,\ldots,1)^T\) and
\[
x=m e+d,\qquad m=\frac1N\sum_i x_i,\qquad \sum_i d_i=0.
\]
The linearization is \(A=P-I\).  Its eigenvalues are
\[
\lambda_k=e^{2\pi i k/N}-1,\qquad k=0,\ldots,N-1.
\]
Thus \(\lambda_0=0\) is simple, with eigenvector \(e\), while every transverse eigenvalue has strictly negative real part.  The transverse spectral gap is
\[
\gamma_N=1-\cos(2\pi/N)>0.
\]

The diagonal
\[
D=\{u e:u\in\mathbb R\}
\]
is exactly invariant, and its scalar dynamics is
\[
\dot u=\sin u-u.
\]
Hence \(D\) is an exact one-dimensional center manifold.  Standard center/strong-stable foliation theory for a simple center eigenvalue separated from a stable spectrum gives a local codimension-one strong-stable manifold through the origin and stable fibers of \(D\).  Because the vector field is globally Lipschitz and Theorem 1 brings every orbit into the local neighborhood, the local strong-stable set extends by the flow to a global invariant codimension-one manifold \(W^{ss}(0)\).

Consequently, points of \(W^{ss}(0)\) converge exponentially.  Every point outside \(W^{ss}(0)\), after entering the local neighborhood, lies on a stable fiber of a nonzero diagonal orbit \(u(t)e\), and for some \(\eta>0\),
\[
x_i(t)-u(t)=O(e^{-\eta t})
\]
uniformly in \(i\).  This also yields exponential synchronization of all coordinates.

### 3. Sharp scalar critical asymptotics

For a nonzero diagonal orbit, the sign of \(u(t)\) is fixed and \(u(t)\to0\).  Put \(w=u^{-2}\).  Taylor expansion gives
\[
\sin u-u=-\frac{u^3}{6}+\frac{u^5}{120}-\frac{u^7}{5040}+O(u^9),
\]
and therefore
\[
\dot w=-2\frac{\sin u-u}{u^3}
=\frac13-\frac{u^2}{60}+\frac{u^4}{2520}+O(u^6)
=\frac13-\frac1{60w}+O(w^{-2}).
\]
First \(\dot w\to1/3\), so \(w\sim t/3\).  Substituting this back gives
\[
\dot w=\frac13-\frac1{20t}+O\!\left(\frac{\log t}{t^2}\right),
\]
where the remainder is integrable after one bootstrap.  Hence
\[
\frac{d}{dt}\left(w-\frac t3+\frac1{20}\log t\right)
=O\!\left(\frac{\log t}{t^2}\right),
\]
so there is a finite constant \(C\) such that
\[
\frac1{u(t)^2}=\frac t3-\frac1{20}\log t+C+o(1).
\]
Because \(x_i-u=O(e^{-\eta t})\) while \(|u|\asymp t^{-1/2}\),
\[
\frac1{x_i(t)^2}-\frac1{u(t)^2}\to0.
\]
The same constant \(C\) therefore works for every coordinate.  Moreover the exponentially small transverse error is eventually smaller than \(|u(t)|\), so all coordinates eventually have the sign of \(u\).  Theorem 2 follows.

## Relation to prior work

Thomas introduced the three-dimensional cyclic sine-feedback flow in 1999.  Sprott and Chlouverakis (2007) studied the three-dimensional labyrinth system, while Chlouverakis and Sprott (2007) analyzed the \(N\)-dimensional cyclic ring and its bifurcation sequence.  Their higher-dimensional paper states that the origin is stable for \(b>1\) and describes the pitchfork at \(b=1\), with the nonzero equilibria satisfying \(b x^*=\sin x^*\) and \(x^*\approx\pm\sqrt{6(1-b)}\) on the \(b<1\) side.  Sorin and Tulchinsky (2024) likewise analyze the three-dimensional route to chaos and give a Lyapunov argument in the strict \(b>1\) regime.

The endpoint needs separate treatment: at exactly \(b=1\), \(\sin u=u\) has no nonzero real solution, and the origin remains globally attracting despite its zero common-mode eigenvalue.  The contribution here is the closed global threshold \(b\ge1\), together with the critical strong-stable/generic dichotomy and the sharp universal reciprocal-square law with its logarithmic correction.  No novelty is claimed for the existence of the Thomas system, the location of the pitchfork parameter, the strict \(b>1\) stable regime, the higher-dimensional ring itself, or general center-manifold/strong-stable theory.

To the best of our knowledge, targeted searches of the Thomas/labyrinth/hyperlabyrinth literature did not locate the critical formula
\[
1/x_i(t)^2=t/3-(1/20)\log t+C+o(1)
\]
or a theorem closing the exact endpoint globally for the cyclic sine ring.  The original Thomas (1999) article was identified bibliographically but was not fully inspected at theorem level, so it remains a residual priority risk.  The accessible 2007 hyperlabyrinth paper and the 2024 Thomas-system paper were inspected at the relevant stability/bifurcation sections.

## Scientific limitations

The sharp rate statement is specific to the unforced cyclic sine ring at exactly \(b=1\).  It does not give uniform asymptotics as \(b\to1\), nor does it treat delays, forcing, fractional derivatives, network couplings beyond the single cyclic shift, or perturbations of the sine nonlinearity.  The strong-stable classification uses standard invariant-manifold theory; the model-specific content is the global endpoint closure and the explicit critical coefficients.  Originality is asserted only to the best of our knowledge.

## Reproducibility

`artifacts/verify_series.py` symbolically checks the Taylor series used in the reciprocal-square asymptotic.  `artifacts/VERIFIED_OUTPUT.txt` records the verified output.  The artifact uses SymPy 1.14.0.

## References

1. R. Thomas, “Deterministic chaos seen in terms of feedback circuits: Analysis, synthesis, ‘labyrinth chaos’,” *International Journal of Bifurcation and Chaos* 9 (1999), 1889–1905. DOI: https://doi.org/10.1142/S0218127499001383
2. J. C. Sprott and K. E. Chlouverakis, “Labyrinth Chaos,” *International Journal of Bifurcation and Chaos* 17 (2007), 2097–2108. DOI: https://doi.org/10.1142/S0218127407018245
3. K. E. Chlouverakis and J. C. Sprott, “Hyperlabyrinth chaos: From chaotic walks to spatiotemporal chaos,” *Chaos* 17 (2007), 023110. DOI: https://doi.org/10.1063/1.2721237
4. R. D. J. G. Ho, “High dimensional chaotic systems which behave like random walks in state space,” arXiv:1908.05989 (2019). https://arxiv.org/abs/1908.05989
5. I. Sorin and M. Tulchinsky, “Infinite Bifurcations in Thomas system,” arXiv:2408.09525 (2024). https://arxiv.org/abs/2408.09525
