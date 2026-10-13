# Continuous endpoint-remainder sharpening of staircase entanglement bounds
## Finding
Let \(f_x(t)=(1+t)^x-t^x\). The 2026 hierarchy of Cao, Jing, Misra, and Wang obtains monogamy and polygamy bounds by Taylor-expanding this function and discarding the Lagrange remainder according to its sign. The discarded remainder can be bounded again, using its monotonicity across the interval rather than only its sign.

For noninteger \(x>0\), write \(q=\lfloor x\rfloor\) and \(\theta=x-q\in(0,1)\). For \(t\ge k>0\), the source lower truncation has the strict refinement
\[
 f_x(t)\ge \sum_{n=0}^{q-1}\binom{x}{n}\bigl((1+k)^{x-n}-k^{x-n}\bigr)(t-k)^n
 +\binom{x}{q}\bigl((1+t)^\theta-t^\theta\bigr)(t-k)^q,
\]
whenever \(x\ge1\). The added term is positive if \(t>k\).

The source upper truncation has the dual refinement
\[
 f_x(t)\le \sum_{n=0}^{q}\binom{x}{n}\bigl((1+k)^{x-n}-k^{x-n}\bigr)(t-k)^n
 +\binom{x}{q+1}\bigl((1+t)^{\theta-1}-t^{\theta-1}\bigr)(t-k)^{q+1},
\]
for every \(x>0\). The added term is negative if \(t>k\).

Substitution into the source induction gives continuous refinements of both entanglement hierarchies. For monogamy, put \(x=\alpha/\gamma\ge1\), \(p_i=\mathcal E_i^\gamma\) in nonincreasing order, and
\[
 \tau_l=\frac{p_1+\cdots+p_{l-1}}{p_l}.
\]
If \(x\) is noninteger, then the coefficient \(B_l\) in the source's Theorem 3.1 can be replaced by
\[
 B_l+\Delta_l^-,\qquad
 \Delta_l^-=\binom{x}{q}\bigl((1+\tau_l)^\theta-\tau_l^\theta\bigr)\bigl(\tau_l-(l-1)\bigr)^q.
\]
Hence
\[
 \mathcal E_{A|B_1\cdots B_{N-1}}^\alpha
 \ge \mathcal E_1^\alpha+\sum_{l=2}^{N-1}(B_l+\Delta_l^-)\mathcal E_l^\alpha.
\]
The correction is strict whenever \(\tau_l>l-1\). For assisted entanglement, put \(y=\beta/\delta>0\), \(r=\lfloor y\rfloor\), and \(\eta=y-r\). The source's Theorem 4.1 coefficient is lowered by
\[
 \Delta_l^+=\binom{y}{r+1}\bigl((1+\tau_{a,l})^{\eta-1}-\tau_{a,l}^{\eta-1}\bigr)\bigl(\tau_{a,l}-(l-1)\bigr)^{r+1}<0.
\]
At integer exponents the source truncations are already exact, while the new endpoint terms tend continuously to the next source Taylor term as an integer threshold is approached. Thus the new bounds fill the source's staircase gaps rather than waiting for the next integer threshold to activate an entire Taylor order.

In Example 3.7 of the source, using concurrence with \(\gamma=2\) and \(\alpha=5\), the non-asymmetric source bound is \(0.08222754895193034\). The endpoint correction raises it to \(0.08551971015395557\). The exact algebraic target from the base pairwise squared-concurrence sum is \(0.08611487376972111\), so the added term closes approximately \(84.69\%\) of the Taylor-truncation gap in this example.

## Assumptions and scope
The lower refinement assumes \(x\ge1\), \(t\ge k>0\), and noninteger \(x\) for strict improvement. The upper refinement assumes \(x>0\), \(t\ge k>0\), and noninteger \(x\). The multipartite corollaries inherit the source assumptions: positive ordered pairwise entanglement values, a valid \(\gamma\)-power monogamy relation for \(\mathcal E\), or a valid \(\delta\)-power polygamy relation for the assisted measure.

The statement does not alter the underlying base monogamy or polygamy exponent, does not claim a globally optimal entanglement bound, and does not remove slack already present in the base relation. It sharpens only the Taylor step that the source uses to lift the base relation to other powers.

## Proof
Fix noninteger \(x=q+\theta\) with \(q=\lfloor x\rfloor\) and \(0<\theta<1\). For
\[
 f_x(t)=(1+t)^x-t^x,
\]
the source computes
\[
 \frac{f_x^{(n)}(s)}{n!}=\binom{x}{n}\bigl((1+s)^{x-n}-s^{x-n}\bigr).
\]
For the lower estimate, Taylor's theorem through order \(q-1\) gives a remainder
\[
 R_q=\binom{x}{q}\bigl((1+\xi)^\theta-\xi^\theta\bigr)(t-k)^q
\]
for some \(\xi\in(k,t)\). The function
\[
 h_\theta(s)=(1+s)^\theta-s^\theta
\]
is positive and strictly decreasing because
\[
 h_\theta'(s)=\theta\bigl((1+s)^{\theta-1}-s^{\theta-1}\bigr)<0.
\]
Therefore \(h_\theta(\xi)\ge h_\theta(t)\), proving the new lower term. Strictness holds when \(t>k\).

For the upper estimate, Taylor's theorem through order \(q\) has remainder
\[
 R_{q+1}=\binom{x}{q+1}\bigl((1+\xi)^{\theta-1}-\xi^{\theta-1}\bigr)(t-k)^{q+1}.
\]
Now
\[
 g_\theta(s)=(1+s)^{\theta-1}-s^{\theta-1}<0
\]
and
\[
 g_\theta'(s)=(\theta-1)\bigl((1+s)^{\theta-2}-s^{\theta-2}\bigr)>0.
\]
Hence \(g_\theta(\xi)\le g_\theta(t)<0\), which proves the corrected upper bound.

The multipartite formulas follow by inserting \(k=l-1\) and \(t=\tau_l\) at each induction step in the source's proof of Lemma 2.3. Since the entanglement theorems substitute \(p_i=\mathcal E_i^\gamma\) or \(p_i=\mathcal E_{a,i}^\delta\), the displayed corrections transfer directly.

When \(x\) is an integer, \(f_x\) is a polynomial of degree \(x-1\), so the source lower Taylor polynomial is exact. As \(x\to(q+1)^-\), the lower endpoint term tends to
\[
 (q+1)(t-k)^q,
\]
which is exactly the next source term activated at \(x=q+1\); the analogous upper correction vanishes at the integer endpoint. This proves continuous threshold matching.

## Verification
The accompanying checker evaluates both inequalities on a deterministic grid of noninteger exponents and positive intervals, verifies exactness at integer exponents, and reproduces the Example 3.7 numbers with high-precision decimal arithmetic. It reports `VERIFY_OK`.

For the concurrence example it returns
\[
 Z_{\mathrm{old}}=0.0822275489519303411\ldots,
\]
\[
 Z_{\mathrm{new}}=0.0855197101539555713\ldots,
\]
and
\[
 S^{5/2}=0.0861148737697211050\ldots,
\]
with a recovered Taylor-gap fraction \(0.846896350662105\ldots\).

## Relationship to prior work
Cao, Jing, Misra, and Wang derive their 2026 hierarchy from the sign of the Lagrange remainder of the same function and explicitly describe the resulting optimal source bound as piecewise, with higher-order corrections activated at integer thresholds. Their Appendix proof retains an unknown intermediate point \(\xi\) and then drops the remainder after establishing its sign. The present result instead uses monotonicity of that remainder factor to replace \(\xi\) by the known endpoint \(t\), producing a nonzero correction between integer thresholds.

The authors' 2024 parameterized monogamy paper and their 2025 unified strengthening develop different weighted and state-dependent refinements. The 2023 general monogamy/polygamy work likewise gives weighted power-transfer inequalities. None of the inspected statements supplies the endpoint-remainder term above or a continuous interpolation of the 2026 staircase hierarchy.

## Limitations
The new terms sharpen only the algebraic Taylor stage. They do not prove that the base \(\gamma\)-power monogamy or \(\delta\)-power polygamy relation is tight for a given state, so the final quantum bound may retain unrelated slack. The originality search cannot exclude differently phrased or newly indexed equivalent results outside the inspected literature. The numerical example illustrates the size of one improvement and is not a proof of uniform relative improvement magnitude.

## References
1. Y. Cao, N. Jing, K. Misra, Y. Wang, “Unified monogamy and polygamy relations for multipartite systems,” Quantum Information Processing 25, 61 (2026), DOI: 10.1007/s11128-026-05076-6.
2. Y. Cao, N. Jing, K. Misra, Y. Wang, “Tighter parameterized monogamy relations,” Quantum Information Processing 23, 282 (2024), DOI: 10.1007/s11128-024-04495-7.
3. Y. Cao, N. Jing, K. Misra, Y. Wang, “Superior monogamy and polygamy relations and estimates of concurrence,” European Physical Journal Plus 140, 101 (2025), DOI: 10.1140/epjp/s13360-025-06029-1.
4. B. Xie, M.-J. Zhao, B. Li, “General Monogamy and polygamy properties of quantum systems,” arXiv:2302.13601.
