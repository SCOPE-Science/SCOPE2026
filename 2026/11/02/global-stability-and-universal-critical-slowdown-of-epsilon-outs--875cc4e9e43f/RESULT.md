# Global stability and universal critical slowdown of epsilon-outside RMSProp

## Finding

**Theorem (the endpoint of the RMSProp stability frontier).** Fix an integer \(d\ge1\), \(0<\beta<1\), \(\varepsilon>0\), and a continuously differentiable, \(\mu\)-strongly convex function \(f:\mathbb R^d\to\mathbb R\) whose gradient is globally \(L\)-Lipschitz, where \(0<\mu\le L\). Write \(x_*\) for its unique minimizer. For every \(x_0\in\mathbb R^d\) and \(v_0\in[0,\infty)^d\), consider the **epsilon-outside, uncorrected** RMSProp recursion

\[
 g_k=\nabla f(x_k),\qquad
 v_{k+1}=\beta v_k+(1-\beta)g_k^{\odot2},\qquad
 x_{k+1}=x_k-h\,g_k\oslash(\varepsilon\mathbf1+\sqrt{v_{k+1}}),
\]

where square, square root, and division are coordinatewise and the constant learning rate is exactly

\[
 h=\frac{2\varepsilon}{L}.
\]

Then \((x_*,0)\) is **globally asymptotically stable** in \(\mathbb R^d\times[0,\infty)^d\): every orbit satisfies \(x_k\to x_*\) and \(v_k\to0\), and the full-state fixed point is Lyapunov stable.

For the scalar quadratic \(d=1\), \(f(x)=a x^2/2\), \(a>0\), and the sharp choice \(L=a\), there is a further exact dichotomy. If \(x_0=0\), or if some finite update lands at \(x_{k+1}=0\), all subsequent spatial states vanish. For **every other initial state** (no finite hit),

\[
 \lim_{k\to\infty}k|x_k|=\frac{\varepsilon}{2a},\qquad
 \lim_{k\to\infty}k^2v_k=\frac{\varepsilon^2}{4}.
\]

The signs of \(x_k\) eventually alternate. Both limit constants are independent of the memory-decay parameter \(\beta\). The finite-hit exception is real: with \(a=2\), \(\varepsilon=1\), \(\beta=4/5\), \(x_0=1/10\), \(v_0=31/25\), the first updated memory is exactly \(v_1=1\) and the first updated position is exactly \(x_1=0\).

## Assumptions and scope

All statements are deterministic and concern the **epsilon-outside** denominator \(\varepsilon+\sqrt{v_{k+1,i}}\), with the new memory used in the position update. They do not assert the same conclusions for epsilon-inside, bias-corrected, stochastic, or momentum RMSProp. The multidimensional endpoint result uses only strong convexity and global smoothness. The sharp inverse-time laws use the scalar **quadratic** and a non-terminating orbit, with no restriction on the initial nonnegative memory. The rate assertions do not imply a uniform transient length in \(\beta\) or the initial state.

## Proof

**Step 1: strict descent exactly at the endpoint.** Let \(g=\nabla f(x)\), \(w=\beta v+(1-\beta)g^{\odot2}\), \(d_i=\varepsilon+\sqrt{w_i}\), and \(x^+=x-h(g_i/d_i)_i\). The global \(L\)-smooth descent lemma and \(h=2\varepsilon/L\) give

\[
\begin{aligned}
 f(x^+)-f(x)
 &\le-h\sum_i\frac{g_i^2}{d_i}+\frac{Lh^2}{2}\sum_i\frac{g_i^2}{d_i^2}\\
 &=-h\sum_i\frac{g_i^2\sqrt{w_i}}{(\varepsilon+\sqrt{w_i})^2}.
\end{aligned}
\]

Every summand is nonnegative. If \(x\ne x_*\), then at least one \(g_i\ne0\); for this index \(w_i\ge(1-\beta)g_i^2>0\). Hence **the objective strictly decreases at each nonminimizing spatial state**, even though the basic constant-step smoothness coefficient has reached its usual zero-margin endpoint.

**Step 2: global convergence and full-state stability.** The objective values decrease and are bounded below by \(f(x_*)\). Strong convexity bounds all spatial iterates inside a compact sublevel set, on which \(\|\nabla f\|\) is bounded. Since each memory coordinate is a convex combination of its preceding value and a bounded squared gradient, all memory iterates are bounded. The trajectory therefore stays inside a compact subset of the full state space.

The decrement function

\[
 \Delta(x,v)=h\sum_i\frac{(\nabla_i f(x))^2\sqrt{\beta v_i+(1-\beta)(\nabla_i f(x))^2}}{\bigl(\varepsilon+\sqrt{\beta v_i+(1-\beta)(\nabla_i f(x))^2}\bigr)^2}
\]

is continuous, nonnegative, and strictly positive whenever \(x\ne x_*\). Because \(f(x_k)\) converges, its successive decrements tend to zero; the inequality in Step 1 implies \(\Delta(x_k,v_k)\to0\). Compactness and continuity then force every spatial accumulation point to equal \(x_*\), whence \(x_k\to x_*\). The filter identity

\[
 v_k=\beta^k v_0+(1-\beta)\sum_{j=0}^{k-1}\beta^{k-1-j}\bigl(\nabla f(x_j)\bigr)^{\odot2}
\]

now gives \(v_k\to0\) because \(0<\beta<1\).

For Lyapunov stability, the descent and strong-convexity bounds imply

\[
 \|x_k-x_*\|^2\le\frac{2}{\mu}\bigl(f(x_0)-f(x_*)\bigr).
\]

Also, global gradient Lipschitzness and \(\nabla f(x_*)=0\) give, coordinatewise,

\[
 0\le v_{k,i}\le \max\left\{v_{0,i},\;\frac{2L^2}{\mu}\bigl(f(x_0)-f(x_*)\bigr)\right\}.
\]

Both right sides tend to zero as \((x_0,v_0)\to(x_*,0)\) in the stated phase space. This proves Lyapunov stability and therefore global asymptotic stability.

**Step 3: the scalar memory tracks the squared gradient.** Take the scalar quadratic and assume \(x_k\ne0\) at every index. Write \(r_k=|x_k|\) and \(w_{k+1}=\sqrt{v_{k+1}}\). Step 2 implies \(r_k,w_k\to0\). Eventually \(w_{k+1}<\varepsilon\), so

\[
 q_k:=\frac{r_{k+1}}{r_k}=\frac{\varepsilon-w_{k+1}}{\varepsilon+w_{k+1}}\longrightarrow1,
\]

and the spatial sign reverses at each such step. Define \(y_k=v_k/(a^2r_k^2)\). For all sufficiently large \(k\),

\[
 y_{k+1}=\frac{\beta y_k+(1-\beta)}{q_k^2},\qquad
 y_{k+1}-1=\frac{\beta}{q_k^2}(y_k-1)+\frac{1-q_k^2}{q_k^2}.
\]

Since \(q_k\to1\) and \(0<\beta<1\), the first coefficient is eventually bounded above by a number strictly less than one, while the forcing term tends to zero. Iterating this scalar contractive inequality establishes \(y_k\to1\). Thus \(v_k\sim a^2r_k^2\), a fact that is *not* an assumption of instantaneous memory equilibration.

**Step 4: exact algebraic slowing.** For sufficiently large \(k\),

\[
 \frac1{r_{k+1}}-\frac1{r_k}
 =\frac{2w_{k+1}}{r_k(\varepsilon-w_{k+1})}
 \longrightarrow\frac{2a}{\varepsilon},
\]

because \(w_{k+1}/r_k=a\sqrt{\beta y_k+(1-\beta)}\to a\). Taking Cesàro averages gives \(1/(kr_k)\to2a/\varepsilon\), hence \(kr_k\to\varepsilon/(2a)\). Finally, \(y_k\to1\) yields \(k^2v_k=a^2(kr_k)^2y_k\to\varepsilon^2/4\). This proves the asserted universal constants. If any nonzero iterate satisfies \(v_{k+1}=\varepsilon^2\), its spatial multiplier is zero and the subsequent dynamics follows the finite-hit branch, which is why that exception cannot be suppressed.

## Verification

The standalone `check.py` verifies the exact finite-hit witness using rational arithmetic, numerically checks the multidimensional descent inequality on a non-diagonal positive-definite quadratic, and evaluates two distinct nonterminating scalar orbits at increasing iteration lengths. It prints the observed scaled quantities alongside their predicted limits. This testing checks only finite examples. Steps 1–4 above provide the infinite-time proof.

Run with a standard Python 3 interpreter: `python3 check.py`. No external packages or data files are required.

## Relationship to prior work

The originating dynamical-systems paper by Loh, Mireles James, Xu, and Tao (arXiv:2610.30078v1, first public 21 October 2026) studies this precise epsilon-outside update for quadratic objectives. Its Section 4 quotes global attraction only for \(0<h<2\varepsilon/L\) and proves Lyapunov instability on quadratics for \(h>2\varepsilon/\lambda_{\max}(A)\). Its Section 5 places the nonzero two-cycle existence threshold strictly above the same boundary. The endpoint of the phase diagram and its algebraic trajectory scale are not among those statements; the results above fill that boundary without reasserting the known strict-regime results.

Dimitrieski, Honecker, Scherer, and Ebenbauer (arXiv:2603.15823, 2026) prove global stability in the strictly subcritical constant-step regime, using a Lyapunov construction whose stated step-size hypothesis is strict. Dereich, Jentzen, and Riekert (arXiv:2504.19426, 2025) study local geometric rates under strict spectral stability. Dereich and Jentzen (arXiv:2608.30382, 2026) study stochastic/bias-corrected hyperparameter-controlled RMSProp rather than this uncorrected fixed-step boundary. These theorems are complementary and do not, as stated in the material inspected, imply the present exact endpoint limits.

## Limitations

The result concerns a fixed step with \(\varepsilon\) *outside* the square root and \(\beta\in(0,1)\). It does not claim a universal exact rate for nonquadratic objectives or for general higher-dimensional Hessians. In the scalar model the rate requires no finite-time zero hit; such exceptional initial states exist. The limits need not be numerically observable on moderate horizons because memory preloading can create very long transients. Publication-priority assessment beyond the identified and inspected literature remains open, and there is no independent verification reported here.

## References

1. K. Loh, J. Mireles James, Z. Xu, M. Tao, *The Dynamics of RMSProp Beyond the Stability Threshold*, arXiv:2610.30078v1 (first public 2026-10-21), Sections 3–5.
2. N. Dimitrieski, M. C. Honecker, C. Scherer, C. Ebenbauer, *Global Stability and Step Size Robustness of RMSProp*, arXiv:2603.15823 (first public 2026-03-16), Theorem 1.
3. S. Dereich, A. Jentzen, A. Riekert, *Sharp higher order convergence rates for the Adam optimizer*, arXiv:2504.19426 (first public 2025-04-28), Section 2.5.
4. S. Dereich, A. Jentzen, *Convergence rates for the RMSprop optimizer with full control of the hyperparameters*, arXiv:2608.30382 (first public 2026-08-31), Section 1.
