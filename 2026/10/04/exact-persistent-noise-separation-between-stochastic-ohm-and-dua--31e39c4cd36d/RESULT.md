# Exact persistent-noise separation between stochastic OHM and Dual-OHM at reflection
## Finding

Let \(L>0\), choose the endpoint step
\[
\alpha=\frac{2}{L},
\]
and consider the scalar cocoercive root problem
\[
\mathbb F(x)=Lx,\qquad x_\star=0.
\]
At iteration \(k\), suppose a minibatch oracle returns
\[
\mathbb F_{B_k}(x)=Lx+\varepsilon_k,
\]
where the \(\varepsilon_k\) are independent, centered, and satisfy
\[
\mathbb E\varepsilon_k^2=\nu^2=\frac{\sigma^2}{B}.
\]
Then
\[
\mathbb T=I-\alpha\mathbb F=-I,
\qquad
\mathbb T_{B_k}(x)=-x-\alpha\varepsilon_k.
\]

For any fixed horizon \(N\ge2\), run the stochastic Dual-OHM and stochastic OHM updates defined in the cited source, from the same deterministic starting point \(x_0\). Their terminal squared residuals are exactly
\[
\mathbb E\!\left|\mathbb F(x_{N-1}^{D})\right|^2
=
\frac{4x_0^2}{\alpha^2N^2}\mathbf 1_{\{N\ {\rm odd}\}}
+
\nu^2D_N,
\]
and
\[
\mathbb E\!\left|\mathbb F(x_{N-1}^{H})\right|^2
=
\frac{4x_0^2}{\alpha^2N^2}\mathbf 1_{\{N\ {\rm odd}\}}
+
\frac{2\nu^2(N-1)(2N-1)}{3N},
\]
where
\[
D_N
=
\sum_{\substack{2\le m\le N\\m\ {\rm even}}}\frac{1}{(m-1)^2}
+
\sum_{\substack{3\le m\le N\\m\ {\rm odd}}}\frac{1}{m^2}.
\]
Consequently,
\[
D_N\uparrow \frac{\pi^2}{4}-1,
\]
so the Dual-OHM noise contribution is uniformly bounded and converges to
\[
\left(\frac{\pi^2}{4}-1\right)\frac{\sigma^2}{B},
\]
whereas the OHM noise contribution obeys
\[
\frac{2\nu^2(N-1)(2N-1)}{3N}
=
\frac{4}{3}\frac{\sigma^2}{B}N+O(1).
\]
Thus this one-dimensional reflected endpoint turns the source paper's qualitative noise-accumulation contrast into an exact separation: fixed-batch stochastic OHM has linearly diverging mean-square residual, while fixed-batch stochastic Dual-OHM has a finite limiting noise floor.

## Assumptions and scope

The oracle is additive: each single-sample call is
\[
\widehat{\mathbb F}(x;\xi)=Lx+\xi,
\qquad
\mathbb E\xi=0,
\qquad
\mathbb E\xi^2=\sigma^2,
\]
and a batch of size \(B\) is averaged. This satisfies the source paper's stochastic-oracle assumptions. In particular,
\[
\widehat{\mathbb F}(x;\xi)-\widehat{\mathbb F}(y;\xi)=L(x-y),
\]
so the samplewise difference is exactly \(1/L\)-cocoercive, and averaging gives
\[
\mathbb E\varepsilon_k^2=\frac{\sigma^2}{B}.
\]

The source permits \(0<\alpha\le2/L\); the choice \(\alpha=2/L\) is therefore the nonexpansive boundary at which the deterministic fixed-point map is the reflection \(-I\). Independence of successive minibatches is used only to add terminal variances without cross-covariances.

The finding concerns this exact scalar boundary model. It does not assert that reflection is worst-case over all stochastic nonexpansive maps, nor that the displayed constants describe state-dependent noise, correlated minibatches, variable batch sizes, or different Halpern coefficients.

## Proof

Write \(a_k=(N-k-1)/(N-k)\). The stochastic Dual-OHM recurrence is
\[
x_{k+1}^{D}
=
x_k^{D}
+
a_k\!\left(
\mathbb T_{B_k}(x_k^{D})
-
\mathbb T_{B_{k-1}}(x_{k-1}^{D})
\right),
\]
with the source convention
\[
\mathbb T_{B_{-1}}(x_{-1}^{D})=x_0.
\]

It is useful first to allow a scalar linear map \(\mathbb T(x)=rx\) and write
\[
\mathbb T_{B_k}(x)=rx-\alpha\varepsilon_k.
\]
A direct expansion of the first-difference recurrence shows that the terminal iterate is
\[
x_{N-1}^{D}
=
p_N(r)x_0
-
\alpha\sum_{j=0}^{N-2}c_{N-j}(r)\varepsilon_j,
\]
where
\[
p_N(r)=\frac1N\sum_{\ell=0}^{N-1}r^\ell
\]
and, for \(m\ge2\),
\[
c_m(r)
=
\frac{1}{m(m-1)}
\sum_{\ell=0}^{m-2}(\ell+1)r^\ell.
\]
For completeness, the noise coefficient follows by tracking one impulse \(\varepsilon_j\). If \(m=N-j\), its contribution to the first differences begins with
\[
-\alpha\frac{m-1}{m}
\]
and then propagates geometrically with the telescoping factors \(a_k\); summing those differences and simplifying the resulting finite geometric derivative gives exactly \(-\alpha c_m(r)\). The deterministic coefficient follows from
\[
x_{k+1}^{D}-x_k^{D}
=
\frac{N-k-1}{N-k}\,r\,(x_k^{D}-x_{k-1}^{D}),
\]
after the initial deterministic difference, and sums to \(p_N(r)\).

Now set \(r=-1\). The alternating derivative sum is
\[
\sum_{\ell=0}^{m-2}(\ell+1)(-1)^\ell
=
\begin{cases}
m/2,&m\ {\rm even},\\
-(m-1)/2,&m\ {\rm odd},
\end{cases}
\]
so
\[
c_m(-1)
=
\begin{cases}
\dfrac{1}{2(m-1)},&m\ {\rm even},\\[2mm]
-\dfrac{1}{2m},&m\ {\rm odd}.
\end{cases}
\]
Also
\[
p_N(-1)=\frac{\mathbf 1_{\{N\ {\rm odd}\}}}{N}.
\]
Therefore independence and centering give
\[
\mathbb E\!\left[(x_{N-1}^{D})^2\right]
=
\frac{x_0^2}{N^2}\mathbf 1_{\{N\ {\rm odd}\}}
+
\frac{\alpha^2\nu^2}{4}
\left(
\sum_{\substack{2\le m\le N\\m\ {\rm even}}}\frac{1}{(m-1)^2}
+
\sum_{\substack{3\le m\le N\\m\ {\rm odd}}}\frac{1}{m^2}
\right).
\]
Since \(L=2/\alpha\), multiplying by \(L^2=4/\alpha^2\) proves the Dual-OHM residual formula.

For stochastic OHM,
\[
x_{k+1}^{H}
=
\frac{1}{k+2}x_0
+
\frac{k+1}{k+2}\mathbb T_{B_k}(x_k^{H}).
\]
At \(r=-1\), induction gives
\[
x_{N-1}^{H}
=
\frac{\mathbf 1_{\{N\ {\rm odd}\}}}{N}x_0
-
\frac{\alpha}{N}
\sum_{j=0}^{N-2}
(j+1)(-1)^{N-2-j}\varepsilon_j.
\]
Hence
\[
\mathbb E\!\left[(x_{N-1}^{H})^2\right]
=
\frac{x_0^2}{N^2}\mathbf 1_{\{N\ {\rm odd}\}}
+
\frac{\alpha^2\nu^2}{N^2}\sum_{\ell=1}^{N-1}\ell^2.
\]
Using
\[
\sum_{\ell=1}^{N-1}\ell^2
=
\frac{(N-1)N(2N-1)}{6}
\]
and again multiplying by \(4/\alpha^2\) proves the OHM formula.

Finally,
\[
D_N
\longrightarrow
1+2\sum_{\substack{n\ge3\\n\ {\rm odd}}}\frac1{n^2}
=
1+2\left(\frac{\pi^2}{8}-1\right)
=
\frac{\pi^2}{4}-1.
\]

## Verification

The standalone script `artifacts/verify_reflection_noise.py` represents every terminal iterate as an exact rational linear combination of \(x_0\) and formal noise variables. For horizons \(2\le N\le24\), it independently executes both recurrences and checks all claimed deterministic and noise coefficients, the closed variance sum for OHM, and the finite \(D_N\) expression for Dual-OHM.

The script also checks the monotone increase of \(D_N\) on that finite range and reports the analytic limiting constant numerically. These finite computations are consistency checks only; the proof above establishes the formulas for every integer \(N\ge2\).

## Relationship to prior work

Yoon and Loizou define the stochastic Dual-OHM recurrence used above and prove the uniform terminal estimate
\[
\mathbb E\|\mathbb F(x_{N-1})\|^2
\le
\frac{4\|x_0-x_\star\|^2}{\alpha^2N^2}
+
\frac{6\sigma^2}{B}.
\]
They explicitly contrast its \(O(N)\) proof-weight accumulation with the \(\Theta(N^2)\) accumulation appearing in the stochastic OHM identity, and their experiments show a constant-batch S-OHM trajectory with diverging residual. Their paper does not state the scalar reflection formulas above, the exact linear divergence coefficient \(4/3\), or the Dual-OHM limiting constant \(\pi^2/4-1\).

The deterministic Dual-OHM paper proves that H-dual algorithms have identical terminal iterates on linear operators. That result explains why the deterministic terms of OHM and Dual-OHM coincide here, but it does not cover independent stochastic perturbations at different oracle calls and therefore does not imply the distinct variance laws.

Bravo and Contreras analyze stochastic Halpern iteration for general nonexpansive maps. They note that a direct noisy Halpern last iterate retains nonnegligible noise and use increasing minibatches to control it. Their inspected full text does not state the reflected-map fixed-batch exact variance formula above.

Relevant records on persistent-noise quadratics and exact stochastic-delay recurrences were also compared. They study different algorithms and mechanisms: one proves finite-time absorption for an online-scaled stochastic gradient method with discrete noise and exact objective feedback, while the other derives a delay-distribution law for randomized Gauss--Seidel. Neither statement implies the OHM/Dual-OHM noise-transfer formulas here.

## Limitations

The result is deliberately an exact boundary benchmark. The map \(-I\) is a one-dimensional reflection, the oracle noise is additive and independent, and the source step is taken at \(\alpha=2/L\). No claim is made that the finite constant \(\pi^2/4-1\) is a universal sharp constant for stochastic Dual-OHM.

The main residual originality risk is specialized work on noisy linear Halpern recurrences that might contain the same reflected-map calculation under different terminology. The primary stochastic Dual-OHM paper already gives the qualitative stability-versus-accumulation contrast and an empirical divergent S-OHM example; the new content is the exact closed-form stochastic separation on the scalar reflected endpoint.

## References

1. T. Yoon and N. Loizou, *Direct Acceleration of Stochastic Root-Finding Without Variance Reduction and Regularization*, arXiv:2608.12043v1, 2026.
2. T. Yoon, J. Kim, J. J. Suh, and E. K. Ryu, *Optimal Acceleration for Minimax and Fixed-Point Problems is Not Unique*, arXiv:2404.13228v2; ICML 2024.
3. M. Bravo and J. P. Contreras, *Stochastic Halpern Iteration in Normed Spaces and Applications to Reinforcement Learning*, arXiv:2403.12338v4; Mathematical Programming, 2026.
