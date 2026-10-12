# Sharp generalized-smoothness intercept for a 2026 cubic-Newton benchmark
## Finding
For the scalar benchmark \(f(x)=\sqrt{1+x^2}-x\cos x\) used in arXiv:2607.10741v1, the least \(L_0\) such that \(|f'''(x)|\le L_0+|f'(x)|\) for every \(x\in\mathbb R\) is exactly \(L_0=3\). Equivalently, at the source's natural choice \(L_1=1\), the pointwise generalized-smoothness certificate improves sharply from the printed pair \((6,1)\) to \((3,1)\). This value is optimal because along \(x_n=2\pi n\), \(|f'''(x_n)|-|f'(x_n)|\to3\).

This sharpens the concrete generalized-smoothness certificate used for the source's benchmark while leaving the benchmark itself and the source algorithm unchanged.

## Assumptions and scope
The function is
\[
f(x)=\sqrt{1+x^2}-x\cos x,\qquad x\in\mathbb R.
\]
The source's pointwise third-order generalized-smoothness hypothesis in one dimension is
\[
|f'''(x)|\le L_0+L_1|f'(x)|.
\]
Only the slice \(L_1=1\) is classified here. No claim is made about the complete Pareto frontier of admissible pairs \((L_0,L_1)\).

Direct differentiation gives
\[
f'(x)=\frac{x}{\sqrt{1+x^2}}-\cos x+x\sin x
\]
and
\[
f'''(x)=-\frac{3x}{(1+x^2)^{5/2}}+3\cos x-x\sin x.
\]

## Proof
Define
\[
h(x)=\frac{x}{\sqrt{1+x^2}}-
\frac{3x}{(1+x^2)^{5/2}}
=
\frac{x(x^4+2x^2-2)}{(1+x^2)^{5/2}}.
\]
Adding the two derivative formulas yields the exact cancellation
\[
f'''(x)+f'(x)=h(x)+2\cos x.
\]

We first prove \(|h(x)|<1\) for every finite real \(x\). Put \(y=x^2\ge0\). Then
\[
(1+y)^5-y(y^2+2y-2)^2
=
1+y+18y^2+10y^3+y^4>0.
\]
Therefore
\[
y(y^2+2y-2)^2<(1+y)^5,
\]
which is exactly \(|h(x)|<1\).

The reverse triangle inequality now gives
\[
|f'''(x)|-|f'(x)|
\le |f'''(x)+f'(x)|
\le |h(x)|+2|\cos x|
<3.
\]
Hence
\[
|f'''(x)|\le3+|f'(x)|
\]
for every \(x\in\mathbb R\), so \(L_0=3\) is admissible at \(L_1=1\).

For sharpness, take \(x_n=2\pi n\). Then
\[
f'(x_n)=\frac{x_n}{\sqrt{1+x_n^2}}-1\longrightarrow0
\]
and
\[
f'''(x_n)=3-\frac{3x_n}{(1+x_n^2)^{5/2}}\longrightarrow3.
\]
Thus
\[
|f'''(x_n)|-|f'(x_n)|\longrightarrow3.
\]
Every \(L_0<3\) therefore fails for all sufficiently large \(n\). The least admissible intercept at \(L_1=1\) is exactly \(3\).

## Verification
The bundled script `artifacts/verify_sharp_generalized_smoothness.py` checks the exact polynomial identity behind \(|h|<1\), compares the differentiated formulas with finite differences only as a consistency test, evaluates the inequality on a deterministic grid, and verifies numerical approach to the sharpness sequence.

These finite computations are not used to prove the universal inequality or optimality. Those follow from the polynomial identity, triangle inequality, and the explicit sequence \(x_n=2\pi n\).

## Relationship to prior work
The primary source introduces the pointwise condition
\[
\|\nabla^3 f(x)\|\le L_0+L_1\|\nabla f(x)\|
\]
for its parameter-free cubic-regularized Newton analysis. For this exact scalar benchmark it prints the admissible pair \((L_0,L_1)=(6,1)\). The source also emphasizes that a fixed objective may admit many such pairs and that its complexity guarantee can be optimized over admissible choices. The exact calculation above therefore sharpens a quantitatively relevant source certificate rather than merely changing notation.

Targeted searches for the benchmark formula, the source identifier, sharp generalized-smoothness constants, and aliases of the fixed-slope intercept did not locate a prior statement of the exact value \(3\). The closest retrieved optimization records concern different algorithms or different smoothness/stability constants and do not imply this benchmark identity.

The source situates its pointwise condition relative to local two-point generalized smoothness and gradient-normalized smoothness. Its own Example 2 is specifically used to show that this benchmark can satisfy the pointwise condition while failing the stronger local two-point condition. The sharp intercept proved here is internal to that weaker pointwise model.

## Limitations
The result fixes \(L_1=1\), the coefficient naturally exposed by the source's decomposition of \(f'''\). It does not determine the full optimal tradeoff between \(L_0\) and \(L_1\), prove a lower bound on optimization complexity, or improve every term in the source theorem simultaneously.

The originality assessment is based on the inspected primary source, targeted published-result searches, exact-formula web searches, and ledger overlap checks. An equivalent elementary sharpening could exist in an unindexed note or under different notation.

## References
1. S. Fang, N. Marumo, and A. Takeda, *Parameter-Free Cubic-Regularized Newton Method: Sharp Complexity and Generalized Smoothness*, arXiv:2607.10741v1, first public 2026-07-12.
