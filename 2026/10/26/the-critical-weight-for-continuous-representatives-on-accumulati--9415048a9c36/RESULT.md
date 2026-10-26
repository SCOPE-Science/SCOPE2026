# The critical weight for continuous representatives on accumulating intervals

## Finding

Fix \(1\le p<\infty\). Let
\[
P=\{0\}\cup\bigcup_{n=1}^{\infty} I_n,\qquad I_n=[2^{-2n-1},2^{-2n}],
\]
with the Euclidean metric and Lebesgue measure restricted to \(P\). For \(\alpha\in\mathbb R\), define the weighted function lattice
\[
\|f\|_{X_\alpha}^{p}=\sum_{n=1}^{\infty}\int_{I_n}|f(x)|^{p}x^{-\alpha}\,dx.
\]
Let \(N^{1}X_\alpha(P)\) consist of functions in \(X_\alpha\) having an upper gradient in \(X_\alpha\), where upper gradients are tested along every rectifiable curve in \(P\). Then
\[
\boxed{\text{every }u\in N^{1}X_\alpha(P)\text{ has a continuous representative}\iff \alpha\ge1.}
\]
When \(\alpha\ge1\), the representative can be chosen with value \(0\) at the accumulation point and satisfies \(\sup_{x\in I_n}|u(x)|\to0\). When \(\alpha<1\), the function equal to \(1\) on even-indexed intervals and \(0\) on odd-indexed intervals belongs to \(N^{1}X_\alpha(P)\), has upper gradient \(0\), and has no continuous representative.

## Assumptions and scope

The norm uses the weight \(x^{-\alpha}\) on \(P\setminus\{0\}\); the metric and curve lengths remain Euclidean. The value at \(0\) has no effect on the norm. The connected components of \(P\) are the intervals \(I_n\) and the singleton \(\{0\}\), so no rectifiable curve joins distinct components. A continuous representative means a continuous function equal to the given function almost everywhere with respect to Lebesgue measure on \(P\). For \(\alpha\ge1\), \(X_\alpha\) is understood as a Banach function lattice; its constant function need not belong to the lattice.

## Proof

Let \(g\in X_\alpha\) be an upper gradient of \(u\). On each fixed interval \(I_n\), the weight is bounded above and below by positive constants. The upper-gradient inequality therefore gives a continuous representative on \(I_n\), and
\[
\operatorname{osc}_{I_n}u\le\int_{I_n}g(x)\,dx.
\]
Suppose first that \(\alpha\ge1\). If \(p>1\), Hölder's inequality gives
\[
\operatorname{osc}_{I_n}u\le
\left(\int_{I_n}g(x)^p x^{-\alpha}\,dx\right)^{1/p}
\left(\int_{I_n}x^{\alpha/(p-1)}\,dx\right)^{1-1/p}.
\]
The first factor is at most \(\|g\|_{X_\alpha}\), and the second tends to zero because \(I_n\subset(0,2^{-2n}]\) and \(\alpha/(p-1)>0\). For \(p=1\),
\[
\operatorname{osc}_{I_n}u\le 2^{-2n\alpha}\int_{I_n}g(x)x^{-\alpha}\,dx
\le 2^{-2n\alpha}\|g\|_{X_\alpha}\longrightarrow0.
\]
Thus \(\operatorname{osc}_{I_n}u\to0\) for every \(1\le p<\infty\).

Write \(m_n=\int_{I_n}x^{-\alpha}\,dx\). At the endpoint, \(m_n=\log2\) when \(\alpha=1\); for \(\alpha>1\),
\[
m_n=\frac{2^{2n(\alpha-1)}(2^{\alpha-1}-1)}{\alpha-1},
\]
so \(m_n\ge c_\alpha>0\) for all \(n\). Since \(u\in X_\alpha\), the series \(\sum_n\int_{I_n}|u|^p x^{-\alpha}\,dx\) converges. Hence \(\inf_{I_n}|u|\to0\); otherwise infinitely many summands would be at least \(c_\alpha\varepsilon^p\) for some \(\varepsilon>0\). Combining this with the oscillation estimate yields \(\sup_{I_n}|u|\to0\). Defining the representative's value at \(0\) to be \(0\) makes it continuous on all of \(P\).

Now suppose \(\alpha<1\). Direct integration gives
\[
m_n=\frac{2^{-2n(1-\alpha)}(1-2^{-(1-\alpha)})}{1-\alpha},
\]
so \(\sum_n m_n<\infty\). Define \(u=1\) on each even-indexed \(I_n\), \(u=0\) on each odd-indexed \(I_n\), and set \(u(0)=0\). The finite sum of the even-indexed masses implies \(u\in X_\alpha\). It is constant on every connected component, so \(g=0\) is an upper gradient and \(u\in N^{1}X_\alpha(P)\). If a continuous function agreed with \(u\) almost everywhere, continuity would force it to be identically the corresponding constant on each interval \(I_n\). Those constants alternate while the intervals approach \(0\), contradicting continuity at \(0\). Thus no continuous representative exists for \(\alpha<1\), completing both directions.

## Verification

The sufficiency proof uses only the upper-gradient inequality, Hölder's inequality (with a separate direct estimate for \(p=1\)), and summability of the weighted component masses. The necessity example has an explicitly computed finite norm and upper gradient zero. The endpoint \(\alpha=1\) is included in the sufficient case because each component has the same positive weighted mass \(\log2\); the strict subcritical case has summable component masses. No finite experiment is used as a substitute for the proof.

## Relationship to prior work

Björn, Björn, and Malý study the same accumulating-interval geometry in Example 7.2(a) of their 2025 paper and treat the critical weight \(x^{-1}\), proving existence of a continuous representative and density of continuous functions in the corresponding Newtonian space. The present statement identifies the full power-weight threshold: it proves the same continuous-representative property for every \(\alpha\ge1\) and gives an explicit obstruction for every \(\alpha<1\). The general quasicontinuity results discussed in that paper do not imply existence of a continuous representative, so they do not determine this threshold.

## Limitations

The classification is for this fixed disconnected geometric family and the power weights \(x^{-\alpha}\). It does not classify arbitrary weights or connected metric spaces, and it makes no claim about outer-capacity properties or all weakly quasicontinuous functions. The weighted lattice for \(\alpha\ge1\) need not contain the constant function.

## References

Anders Björn, Jana Björn, and Lukáš Malý, “Non-quasicontinuous Newtonian functions and outer capacities based on Banach function spaces,” arXiv:2503.21665v1 [math.FA], first public version dated 27 March 2025, Example 7.2(a) and its proof.
