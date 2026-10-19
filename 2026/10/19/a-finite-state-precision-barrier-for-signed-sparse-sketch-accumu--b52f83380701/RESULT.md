# A finite-state precision barrier for signed sparse sketch accumulation

## Finding
Consider the exact sparse sketch and floating-point realization specified below. The output of the binary16 computation has an absolute energy ceiling even on a rank-one subspace with exactly equal leverage scores. The exact-arithmetic sketch, on the same input, preserves squared norm with a dimension-free variance estimate. The binary16 accumulator additionally has an explicit finite-state limiting law.

**Theorem.** Let \(\zeta\in\{1,4\}\), let \(m\ge\zeta\) be a multiple of \(\zeta\), and write \(b=m/\zeta\), \(K=2048\). For any integer \(N\ge1\) form independent assignments and signs as defined below. Write \(Q_{16}\) and \(Q_\infty\) for the squared Euclidean norms of the binary16 and exact-arithmetic outputs, respectively. Then
\[
0\le Q_{16}\le\frac{mK^2}{\zeta}\quad\text{for every assignment of signs and buckets},
\]
and the upper bound is attained by a possible assignment whenever \(N\ge Kb\). For every \(0<\varepsilon<1\), whenever
\[
N>\frac{mK^2}{\zeta(1-\varepsilon)},
\]
the binary16 output violates \(Q_{16}\ge (1-\varepsilon)N\) with probability one. In contrast,
\[
\mathbb E Q_\infty=N,\qquad
\operatorname{Var}(Q_\infty)=\frac{2N(N-1)}m,\qquad
\Pr\!\left(\left|Q_\infty/N-1\right|\ge\varepsilon\right)
\le\frac{2(N-1)}{mN\varepsilon^2}.
\]
For fixed \(m,\zeta\), as \(N\to\infty\) the \(m\) binary16 accumulators converge **jointly in law** to independent discrete uniforms on
\[
\left\{\frac{j}{\sqrt\zeta}:-K\le j\le K,\ j\in\mathbb Z\right\};
\]
consequently
\[
\lim_{N\to\infty}\mathbb E Q_{16}
=\frac{mK(K+1)}{3\zeta}
=\frac{1\,398\,784m}{\zeta}.
\]
Here all moments and probability statements refer to the random hashing and signs, not to stochastic rounding.

## Assumptions and scope
Fix the real rank-one column \(a_N=(1,\ldots,1)^\mathsf T\in\mathbb R^N\). Its column space has equal leverage scores \(1/N\), and \(\|a_N\|_2^2=N\). For each input index \(i\in\{1,\ldots,N\}\) and layer \(\ell\in\{1,\ldots,\zeta\}\), independently draw a bucket \(H_{i\ell}\) uniformly from \(\{1,\ldots,b\}\) and sign \(\sigma_{i\ell}\in\{-1,1\}\) uniformly. Layer \(\ell\) has its own \(b\) output coordinates. The exact output at bucket \((\ell,r)\) is \(\zeta^{-1/2}\sum_{i:H_{i\ell}=r}\sigma_{i\ell}\).

The **binary16 output** is obtained from zero by sequentially adding \(\sigma_{i\ell}/\sqrt\zeta\) to each assigned accumulator, rounding **each sum** to IEEE binary16 under round-to-nearest, ties-to-even (RN), with no other perturbation. The processing order in each bucket may be any order determined independently of the signs; the pointwise bound does not even require that independence. This is a mathematical model for correctly rounded low-precision signed atomic accumulation, not a hardware-level proof about every GPU instruction, execution order, or other rounding mode. The values \(1\) and \(1/2\) are exactly representable; overflow and underflow do not occur in this model. Evaluate the final squared Euclidean norm in exact arithmetic.

## Proof
**1. Exact reflected-state reduction.** In IEEE binary16, the significand has eleven binary digits. Every integer \(j\) with \(|j|\le K=2048\) is representable, and so is each \(j/2\). For \(|j|<K\), adding \(\pm1\) to \(j\) (or \(\pm1/2\) to \(j/2\)) is exact. At \(j=K\), the outward exact sum \(K+1\) lies midway between successive binary16 representable numbers \(K\) and \(K+2\); ties-to-even selects \(K\). The analogous midpoint is \(K/2+1/2\) between \(K/2\) and \(K/2+1\), which rounds to \(K/2\). The negative endpoint behaves symmetrically. Induction shows that an accumulator, divided by \(1/\sqrt\zeta\), evolves exactly as
\[
J\longmapsto \min\{K,\max\{-K,J+\sigma\}\},\qquad J\in\{-K,\ldots,K\}.
\]
Thus each coordinate has absolute value at most \(K/\sqrt\zeta\), proving the uniform energy bound. If \(N\ge Kb\), choose hashes so each bucket in every layer receives at least \(K\) updates, all of sign \(+1\). Every coordinate then equals \(K/\sqrt\zeta\), attaining the bound. Since \(\|a_N\|_2^2=N\), the stated strict inequality forces lower-embedding failure for every choice of signs and buckets.

**2. Exact-arithmetic moments.** Expanding the real-arithmetic energy gives
\[
Q_\infty=N+\frac2\zeta\sum_{\ell=1}^\zeta\sum_{1\le i<j\le N}
\sigma_{i\ell}\sigma_{j\ell}\mathbf 1\{H_{i\ell}=H_{j\ell}\}.
\]
Each summand has mean zero and variance \(1/b\). Distinct pair-layer terms have zero covariance, even when pairs share an index, because a sign then appears to the first power and has zero mean. Hence
\[
\operatorname{Var}(Q_\infty)=\frac4{\zeta^2}\cdot\zeta\binom N2\frac1b
=\frac{2N(N-1)}m.
\]
Chebyshev's inequality gives the tail probability. For fixed distortion tolerance and sufficiently many output rows, the exact sketch is therefore a high-probability squared-norm embedding of the same one-dimensional subspace in a regime in which the binary16 realization always fails.

**3. Joint stationary law.** Conditional on the hashes, the signs assigned to each bucket are mutually independent fair signs. After \(t\) visits that bucket follows the reflected random walk above. Its transition matrix is symmetric and irreducible; its endpoints have holding probability \(1/2\), so it is aperiodic. Its unique stationary law is uniform on the \(2K+1\) states. For fixed \(m\) and \(\zeta\), each bucket visit count is binomial \(\operatorname{Bin}(N,1/b)\), and its minimum over finitely many buckets tends to infinity in probability. Conditional independence across buckets and convergence of every walk to equilibrium imply joint convergence to independent uniforms. The energies are uniformly bounded, so convergence in distribution gives convergence of their expectations. Finally
\[
\frac{1}{2K+1}\sum_{j=-K}^K j^2=\frac{K(K+1)}3,
\]
which yields the asserted expectation limit.

## Verification
The included standalone `check.py` uses the standard-library binary16 serializer and exhaustively verifies both signed transition directions from every one of the \(4097\) allowable accumulator states for each \(\zeta\in\{1,4\}\) (16,388 cases). It also checks absorption at the endpoints, computes exact first and second sketch moments over four fully enumerated small hash/sign spaces (64, 216, 256, and 65,536 outcomes), and checks the uniform-law second moment. These finite checks corroborate, but do not substitute for, the all-\(N\) proof. Reproduce with `python3 check.py`; `CHECKS.txt` contains the exact output.

## Relationship to prior work
Jeendgar, Flint, and Anzt (2026) investigate the same SparseStack sign/hash arrangement and deterministic binary16 atomic accumulation, empirically finding similar sketch distortion for three rounding modes **in their tested input ranges**. Their Section 4 specifies one signed update per block with scale \(1/\sqrt\zeta\); Section 5 studies input sizes up to approximately two million. This finding addresses the mathematically different unbounded-input and fixed-output-precision regime: it gives an absolute norm ceiling and an explicit limiting law rather than extrapolating the measured finite-regime behavior. Carson and Daužickaitė (2024/2025) analyze mixed-precision sketched QR and iterative refinement using normwise roundoff-error assumptions; their sufficient conditions do not imply this exact discrete-state obstruction. The elementary binary16 midpoint rule and reflected-walk stationary measure are standard ingredients, not claimed as discoveries in themselves.

## Limitations
The result concerns only \(\zeta=1\) and \(\zeta=4\), the fixed all-ones one-column input, correctly rounded deterministic binary16 accumulators, and the specified independently signed sparse sketch. It does not prove a threshold for arbitrary matrices, stochastic or dithered rounding, BF16 or FP32, compensated reductions, or GPU-dependent atomic scheduling. The displayed sufficient size for certain embedding failure is not claimed to be the smallest size at which failure can occur with substantial probability. The asymptotic stationary law holds with the output dimension fixed and the input height increasing; finite tests do not establish mixing-time bounds. No independent validation has been performed.

## References
- A. Jeendgar, C. Flint, H. Anzt, *Randomized Sketching is Robust to Low-Precision Rounding on GPUs*, arXiv:2606.20195v1, first public June 18, 2026. https://arxiv.org/abs/2606.20195
- E. Carson, I. Daužickaitė, *Mixed precision sketching for least-squares problems and its application in GMRES-based iterative refinement*, arXiv:2410.06319v2. https://arxiv.org/abs/2410.06319
- IEEE 754 binary16 round-to-nearest, ties-to-even arithmetic (standard definition; the result uses only the eleven-digit significand and midpoint rule).
