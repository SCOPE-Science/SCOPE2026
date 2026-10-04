# Review of Closed-range \(K\)-frame reconstruction requires range compression

## Correctness
PASS. In the explicit \(\mathbb C^3\) example, the coefficient energy is \(|x_1|^2+|x_1+x_2|^2\), which dominates \(\|K^*x\|^2=|x_1|^2\). The resulting frame operator is exactly \(\begin{pmatrix}2&1&0\\1&1&0\\0&0&0\end{pmatrix}\), so \(S(R(K))\not\subseteq R(K)\) and \((S|_{R(K)})^{-1}e_1\) is undefined. For the repair, \((K^\dagger)^*K^*x=x\) on \(R(K)\) gives the stated coercive bound for \(C=P_{R(K)}S|_{R(K)}\), which implies bounded invertibility and both reconstruction identities.

## Originality
PASS. Searches covered the target source, exact inverse-on-range formulation, range-to-range formulation, compression aliases, and the reconstruction formula. The closest checked literature states the correct map \(S:R(K)\to S(R(K))\) or adds the extra invariance \(S(R(K))=R(K)\); it does not imply the universal compression theorem or provide the displayed three-dimensional obstruction to formula (2.10). The main residual risk is an unindexed correction or informal observation.

## Value
PASS. The issue is structural rather than cosmetic: without range invariance the published reconstruction expression can be undefined even for a two-operator finite-dimensional \(K\)-g-fusion frame. The compression theorem supplies a direct, quantitative replacement valid for every closed-range \(K\), preserving the intended reconstruction on \(R(K)\) without adding an unnecessary invariance hypothesis.

## Closest literature and limitations
Huang--Yang (2020) is the target source. Cheshmavar--Rezaei Sarkhaei (2018/2021) uses similar inverse-on-\(R(K)\) shorthand. Alvani--Janfada--Sadeghi (2025) explicitly gives the correct codomain \(S(R(K))\), while the 2022 equal-norm Parseval \(K\)-frame paper imposes \(S(R(K))=R(K)\) before using an inverse on \(R(K)\). The finding does not invalidate results formulated with the correct range-to-range inverse, and it does not exclude prior unindexed observations.

Same-model review: passed. Independent audit: not yet performed.
