# Review

## Correctness
PASS. The two full families have the exact coefficient energy
\[
2|x|^2+2a^2|y|^2
\]
and hence are \(K\)-frames for \(K=P_{\operatorname{span}\{e_1\}}\) with admissible bounds \(2,2\). Their synthesis-operator difference has exact norm
\[
2\sqrt2\,a.
\]
With
\[
\lambda=2\sqrt2\,a
\]
and \(0<a\le1/8\), both printed hypotheses of Proposition 3.3 hold. The specified mixed weave consists of two copies of \(e_1+a e_2\) and annihilates \(-a e_1+e_2\), whose \(K^*\)-image is nonzero.

The source proof was checked at the critical step. It applies
\[
\|f\|\le\|K^\dagger\|\|K^*f\|
\]
to arbitrary \(f\in H\), although the closed-range lower estimate is only available on \(R(K)\).

## Originality
PASS. The exact source, proposition number, synthesis-operator formulation, range/complement formulation, Moore--Penrose formulation, older woven-\(K\)-frame perturbation work, and later operator-weaving corrections were compared. No checked indexed source gives this one-parameter counterfamily or a result that implies it.

The closest K-frame range-compression and perturbation counterexamples concern reconstruction or destruction of a full frame. They do not cover the present situation in which both complete families remain \(K\)-frames while a single mixed weave fails.

## Value
PASS. The proposition is meant to turn quantitative synthesis closeness into a uniform weaving guarantee. The example shows failure for arbitrarily small synthesis distance, not merely at a large or degenerate perturbation. It also identifies the exact geometric vulnerability: components in \(R(K)^\perp\) can cancel selected coefficients while \(K^*f\) remains nonzero.

## Closest literature and limitations
The 2017/2018 Paley--Wiener theorem for woven \(K\)-frames uses extra hypotheses and restricts its critical estimate to \(N(K^*)^\perp\). The target paper's Proposition 3.5 instead uses a directly \(K^*\)-scaled perturbation condition.

A simple sufficient repair of Proposition 3.3 is to require every atom of both families to lie in \(R(K)\). This is not claimed necessary; broader valid repairs may control perturbations directly in the \(K^*\)-seminorm.

Same-model review: passed. Independent audit: not yet performed.
